#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    checks = []

    report = ROOT / "governance" / "RMG-GOV-003-EXECUTED-INVENTORY-REPORT.md"
    queue = ROOT / "governance" / "rmg-claim-reclassification-queue.jsonl"
    hook = ROOT / "code" / "enforce_rmg_new_record_policy.py"
    unit = ROOT / "units" / "RMG-GOV-003.md"

    checks.append(("inventory report exists", report.exists()))
    checks.append(("queue exists", queue.exists()))
    checks.append(("enforcement hook exists", hook.exists()))
    checks.append(("unit card exists", unit.exists()))

    rows = [json.loads(line) for line in queue.read_text(encoding="utf-8").splitlines() if line.strip()]
    checks.append(("queue has unique ids", len({r["queue_id"] for r in rows}) == len(rows)))
    checks.append(("queue has P0 items", any(r.get("priority") == "P0" for r in rows)))
    checks.append(("all queue items remain explicit", all(r.get("status") in {"OPEN", "CLOSED", "BLOCKED"} for r in rows)))

    hook_text = hook.read_text(encoding="utf-8")
    for token in ("ASSIM-", "MATH-", "pvg_necessity_level", "regression evidence cannot automatically imply mathematical contribution"):
        checks.append((f"hook contains {token}", token in hook_text))

    report_text = report.read_text(encoding="utf-8")
    checks.append(("report does not overclaim full compliance", "FULL_REPOSITORY_COMPLIANCE = NOT_CLAIMED" in report_text))

    failed = [name for name, ok in checks if not ok]
    for name, ok in checks:
        print(("PASS" if ok else "FAIL") + " " + name)
    print(f"TOTAL {len(checks) - len(failed)}/{len(checks)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
