#!/usr/bin/env python3
"""Audit the current one-front research compass with ENGINE-004 overrides."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "registries/program-goals.jsonl"
OVERRIDES = ROOT / "registries/goal-state-overrides-engine-004.jsonl"


def load(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    required = [
        ROOT / "central-mind-charter.md",
        ROOT / "central-mind-goals.md",
        ROOT / "governance/pvg-ant-research-compass-v1.md",
        ROOT / "governance/pvg-inverse-geometry-engine-architecture-v1.md",
        ROOT / "governance/readiness/ENGINE-004-INVERSE-PRIME-FIBERS.md",
        BASE,
        OVERRIDES,
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("\n".join(f"FAIL: missing {path}" for path in missing))

    base = load(BASE)
    by_id = {str(row["id"]): row for row in base}
    order = [str(row["id"]) for row in base]
    for row in load(OVERRIDES):
        goal_id = str(row["id"])
        if goal_id not in by_id:
            order.append(goal_id)
        by_id[goal_id] = row
    goals = [by_id[goal_id] for goal_id in order]

    strategic = [row for row in goals if row.get("kind") == "strategic_goal"]
    if len(strategic) != 1 or strategic[0].get("status") != "active_fixed":
        raise SystemExit("FAIL: strategic goal invariant broken")

    inverse = by_id.get("GOAL-PVG-INVERSE-GEOMETRY-001", {})
    if inverse.get("status") != "active_long_term":
        raise SystemExit("FAIL: inverse geometry long-term goal missing")

    active = [
        row for row in goals
        if row.get("kind") == "operational_goal"
        and str(row.get("status", "")).startswith("active")
    ]
    if len(active) != 1 or active[0].get("id") != "GOAL-OP-INVERSE-PRIME-FIBERS-001":
        raise SystemExit(f"FAIL: active front mismatch: {[row.get('id') for row in active]}")

    theorem = by_id.get("GOAL-OP-ONE-THEOREM-001", {})
    if theorem.get("status") != "superseded_with_reason":
        raise SystemExit("FAIL: theorem goal is still governing")

    readiness = (ROOT / "governance/readiness/ENGINE-004-INVERSE-PRIME-FIBERS.md").read_text(encoding="utf-8")
    if "Decision: READY" not in readiness or "Phase D" not in readiness:
        raise SystemExit("FAIL: ENGINE-004 readiness or stop rule missing")

    print("Research Compass Audit: PASS")
    print(f"Strategic goal: {strategic[0]['id']}")
    print("Governing program: GOAL-PVG-INVERSE-GEOMETRY-001")
    print("Active operational goal: GOAL-OP-INVERSE-PRIME-FIBERS-001")
    print("Theorem goal: superseded_with_reason")
    print("Phase D: NOT AUTHORIZED")


if __name__ == "__main__":
    main()
