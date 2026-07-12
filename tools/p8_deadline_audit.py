#!/usr/bin/env python3
"""P8 outreach decision guard (Stage Review 001 PR-A).

Enforces the non-renegotiable external-validation deadline:
PREPARED_NOT_SENT is an illegal steady state after decision_deadline_utc.
Allowed states after the deadline: SENT or HOLD_AUTHORIZED (with explicit
authorization reference, named blocker, evidence, and a new deadline at
most 14 days after the hold record). This guard reads exactly one machine
record: registries/p8-outreach-decision.json. It intentionally uses the
current UTC time: after the deadline every CI run fails until a PR flips
the record to an allowed state - and that PR passes by construction, so
no deadlock exists.

Exit 0 = PASS, 1 = FAIL. Stdlib only.
"""
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECORD = ROOT / "registries" / "p8-outreach-decision.json"

ALLOWED = {"PREPARED_NOT_SENT", "SENT", "HOLD_AUTHORIZED"}
# The deadline is pinned HERE, not only in the JSON record: silently moving
# decision_deadline_utc in the registry cannot renegotiate it (adversarial
# review finding, PR #28). Changing this constant requires editing the guard
# itself in a reviewed PR.
PINNED_DEADLINE = "2026-07-19T20:59:59Z"
MAX_HOLD_DAYS = 14


def parse_utc(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def main() -> int:
    issues = []
    try:
        record = json.loads(RECORD.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - guard must report, not crash
        print(f"FAIL - cannot read {RECORD.name}: {exc}")
        return 1

    status = record.get("status")
    if status not in ALLOWED:
        issues.append(f"unknown outreach status: {status!r}")

    now = datetime.now(timezone.utc)
    try:
        deadline = parse_utc(record["decision_deadline_utc"])
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL - invalid decision_deadline_utc: {exc}")
        return 1

    if status == "PREPARED_NOT_SENT" and record["decision_deadline_utc"] != PINNED_DEADLINE:
        issues.append(
            "decision_deadline_utc diverges from the guard-pinned deadline "
            f"{PINNED_DEADLINE}; the deadline is not renegotiable via the registry"
        )
        deadline = parse_utc(PINNED_DEADLINE)

    if status == "PREPARED_NOT_SENT" and now > deadline:
        issues.append(
            "P8 decision deadline passed while status is PREPARED_NOT_SENT; "
            "flip to SENT or HOLD_AUTHORIZED via a reviewed PR"
        )

    if status == "SENT":
        sent = record.get("sent") or {}
        for field in ("priority_packet_sent_utc", "proof_packet_sent_utc"):
            value = sent.get(field)
            if not value:
                issues.append(f"status SENT but sent.{field} is empty")
            else:
                try:
                    parse_utc(value)
                except Exception:
                    issues.append(f"sent.{field} is not a valid UTC timestamp: {value!r}")
        if sent.get("recipients_verified") is not True:
            issues.append("status SENT but sent.recipients_verified is not true")

    if status == "HOLD_AUTHORIZED":
        hold = record.get("hold") or {}
        for field in ("authorization_ref", "named_blocker", "blocker_evidence",
                      "hold_recorded_utc", "new_decision_deadline_utc"):
            if not hold.get(field):
                issues.append(f"status HOLD_AUTHORIZED but hold.{field} is empty")
        if not issues:
            try:
                recorded = parse_utc(hold["hold_recorded_utc"])
                new_deadline = parse_utc(hold["new_decision_deadline_utc"])
            except Exception as exc:  # noqa: BLE001
                print(f"FAIL - invalid hold timestamp: {exc}")
                return 1
            if new_deadline > recorded + timedelta(days=MAX_HOLD_DAYS):
                issues.append(
                    f"hold.new_decision_deadline_utc exceeds {MAX_HOLD_DAYS} days "
                    "after hold_recorded_utc"
                )
            if now > new_deadline:
                issues.append(
                    "hold period expired; record a new reviewed decision "
                    "(SENT or a freshly authorized HOLD)"
                )

    if issues:
        print(f"FAIL - {len(issues)} issue(s):")
        for issue in issues:
            print("  [p8-deadline] " + issue)
        return 1
    print(f"PASS - P8 outreach decision state '{status}' is legal "
          f"(deadline {record['decision_deadline_utc']}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
