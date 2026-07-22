#!/usr/bin/env python3
"""Audit goal memory and traceability across ordered state overrides."""

from __future__ import annotations

import json
from pathlib import Path

try:
    from tools.current_goal_state import active_operational_goals, current_goals
except ModuleNotFoundError:
    from current_goal_state import active_operational_goals, current_goals

ROOT = Path(__file__).resolve().parent.parent
ACTIVE_ID = "GOAL-OP-TWO-PRIME-PLANE-GEOMETRY-001"


def load_jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{path.relative_to(ROOT)}:{number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise RuntimeError(f"{path.relative_to(ROOT)}:{number}: row is not an object")
        rows.append(value)
    return rows


def main() -> None:
    required = [
        ROOT / "registries/program-goals.jsonl",
        ROOT / "registries/goal-state-overrides-engine-004.jsonl",
        ROOT / "registries/goal-state-overrides-pvg-two-prime-plane.jsonl",
        ROOT / "registries/goal-links-two-prime-plane.jsonl",
        ROOT / "governance/readiness/PVG-TWO-PRIME-PLANE-GEOMETRY-001.md",
        ROOT / "tools/pvg_two_prime_plane.py",
        ROOT / "tests/test_pvg_two_prime_plane.py",
        ROOT / "research/pvg-space-deepening/pvg-two-prime-plane-geometry-001.md",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.is_file()]
    if missing:
        raise SystemExit("\n".join(f"FAIL: missing required file: {path}" for path in missing))

    goals = current_goals()
    by_id = {str(row["id"]): row for row in goals}
    if len(by_id) != len(goals):
        raise SystemExit("FAIL: duplicate current goal IDs")

    active = active_operational_goals(goals)
    active_ids = [str(row.get("id")) for row in active]
    if active_ids != [ACTIVE_ID]:
        raise SystemExit(f"FAIL: unexpected active operational goals: {active_ids}")

    theorem = by_id.get("GOAL-OP-ONE-THEOREM-001", {})
    if theorem.get("status") != "superseded_with_reason" or theorem.get("return_to_goal_ids") != []:
        raise SystemExit("FAIL: theorem route is not fully archived")

    engine_004 = by_id.get("GOAL-OP-INVERSE-PRIME-FIBERS-001", {})
    if engine_004.get("status") != "paused_by_owner":
        raise SystemExit("FAIL: ENGINE-004 is not paused_by_owner")

    active_goal = by_id.get(ACTIVE_ID, {})
    if active_goal.get("status") != "active_current":
        raise SystemExit("FAIL: two-prime-plane goal is not active_current")
    if "three axes" not in str(active_goal.get("return_gate", "")):
        raise SystemExit("FAIL: active goal return gate does not control three-axis expansion")

    link_paths = sorted((ROOT / "registries").glob("goal-links*.jsonl"))
    links = [row for path in link_paths for row in load_jsonl(path)]
    linked = {
        (str(row.get("from_goal_id", "")), str(row.get("relation", "")), str(row.get("to_goal_id", "")))
        for row in links
    }
    for parent in active_goal.get("parent_goal_ids", []):
        if (ACTIVE_ID, "serves", str(parent)) not in linked:
            raise SystemExit(f"FAIL: missing serves link to {parent}")
    for target in active_goal.get("return_to_goal_ids", []):
        if (ACTIVE_ID, "returns_to", str(target)) not in linked:
            raise SystemExit(f"FAIL: missing return link to {target}")

    print("PVG–ANT Goal Memory and Traceability Audit: PASS")
    print(f"Current goals: {len(goals)}")
    print(f"Governing operational goal: {ACTIVE_ID}")
    print("ENGINE-004: paused_by_owner / retained / not closed")
    print("Mandatory return: GOAL-PVG-INVERSE-GEOMETRY-001")
    print("Three-axis expansion: NOT AUTHORIZED")


if __name__ == "__main__":
    main()
