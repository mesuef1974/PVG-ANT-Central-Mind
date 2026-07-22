#!/usr/bin/env python3
"""Audit the current one-front Research Compass state."""

from __future__ import annotations

from pathlib import Path

try:
    from tools.current_goal_state import active_operational_goals, current_goals
except ModuleNotFoundError:
    from current_goal_state import active_operational_goals, current_goals

ROOT = Path(__file__).resolve().parent.parent
ACTIVE_ID = "GOAL-OP-TWO-PRIME-PLANE-GEOMETRY-001"
READINESS = ROOT / "governance/readiness/PVG-TWO-PRIME-PLANE-GEOMETRY-001.md"


def main() -> None:
    required = [
        ROOT / "central-mind-charter.md",
        ROOT / "central-mind-goals.md",
        ROOT / "governance/pvg-ant-research-compass-v1.md",
        ROOT / "governance/pvg-inverse-geometry-engine-architecture-v1.md",
        READINESS,
        ROOT / "registries/program-goals.jsonl",
        ROOT / "registries/goal-state-overrides-engine-004.jsonl",
        ROOT / "registries/goal-state-overrides-pvg-two-prime-plane.jsonl",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("\n".join(f"FAIL: missing {path}" for path in missing))

    goals = current_goals()
    by_id = {str(row["id"]): row for row in goals}
    strategic = [row for row in goals if row.get("kind") == "strategic_goal"]
    if len(strategic) != 1 or strategic[0].get("status") != "active_fixed":
        raise SystemExit("FAIL: strategic goal invariant broken")

    inverse = by_id.get("GOAL-PVG-INVERSE-GEOMETRY-001", {})
    if inverse.get("status") != "active_long_term":
        raise SystemExit("FAIL: inverse geometry long-term goal missing")

    active = active_operational_goals(goals)
    active_ids = [str(row.get("id")) for row in active]
    if active_ids != [ACTIVE_ID]:
        raise SystemExit(f"FAIL: active front mismatch: {active_ids}")

    theorem = by_id.get("GOAL-OP-ONE-THEOREM-001", {})
    if theorem.get("status") != "superseded_with_reason":
        raise SystemExit("FAIL: theorem goal is still governing")

    engine_004 = by_id.get("GOAL-OP-INVERSE-PRIME-FIBERS-001", {})
    if engine_004.get("status") != "paused_by_owner":
        raise SystemExit("FAIL: ENGINE-004 is not paused_by_owner")

    readiness = READINESS.read_text(encoding="utf-8")
    for token in (
        "Decision: READY",
        "PVG-TWO-PRIME-PLANE-GEOMETRY-001 = ACTIVE_CURRENT",
        "ENGINE-004 PASS-004 = PAUSED_BY_OWNER",
        "ENGINE-005 = CANDIDATE / inactive",
        "moving to the `2,3,5` three-axis simplex",
    ):
        if token not in readiness:
            raise SystemExit(f"FAIL: readiness omits required token: {token}")

    print("Research Compass Audit: PASS")
    print(f"Strategic goal: {strategic[0]['id']}")
    print("Governing program: GOAL-PVG-INVERSE-GEOMETRY-001")
    print(f"Active operational goal: {ACTIVE_ID}")
    print("ENGINE-004: paused_by_owner / retained / not closed")
    print("ENGINE-005: inactive candidate")
    print("Three-axis expansion: NOT AUTHORIZED")


if __name__ == "__main__":
    main()
