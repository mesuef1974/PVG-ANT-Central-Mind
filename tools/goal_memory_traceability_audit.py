#!/usr/bin/env python3
"""Audit goal memory with append-only state overrides for ENGINE-004."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE_GOALS = "registries/program-goals.jsonl"
OVERRIDES = "registries/goal-state-overrides-engine-004.jsonl"
LINK_FILES = [
    "registries/goal-links.jsonl",
    "registries/goal-links-engine-002.jsonl",
    "registries/goal-links-engine-003.jsonl",
    "registries/goal-links-engine-004.jsonl",
]
REQUIRED_FILES = [
    BASE_GOALS,
    OVERRIDES,
    *LINK_FILES,
    "governance/pvg-inverse-geometry-engine-architecture-v1.md",
    "governance/readiness/ENGINE-004-INVERSE-PRIME-FIBERS.md",
    "tools/pvg_inverse_prime_fibers.py",
    "tests/test_pvg_inverse_prime_fibers.py",
    "research/pvg-space-deepening/engine-004-inverse-prime-fibers.md",
]


def load_jsonl(path: str) -> list[dict[str, object]]:
    rows = []
    for number, raw in enumerate((ROOT / path).read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{path}:{number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise RuntimeError(f"{path}:{number}: row is not an object")
        rows.append(value)
    return rows


def current_goals() -> list[dict[str, object]]:
    ordered = load_jsonl(BASE_GOALS)
    by_id = {str(row["id"]): row for row in ordered}
    order = [str(row["id"]) for row in ordered]
    for row in load_jsonl(OVERRIDES):
        goal_id = str(row["id"])
        if goal_id not in by_id:
            order.append(goal_id)
        by_id[goal_id] = row
    return [by_id[goal_id] for goal_id in order]


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit("\n".join(f"FAIL: missing required file: {path}" for path in missing))

    goals = current_goals()
    by_id = {str(row["id"]): row for row in goals}
    if len(by_id) != len(goals):
        raise SystemExit("FAIL: duplicate current goal IDs")

    active = [
        row for row in goals
        if row.get("kind") == "operational_goal"
        and str(row.get("status", "")).startswith("active")
    ]
    if len(active) != 1 or active[0].get("id") != "GOAL-OP-INVERSE-PRIME-FIBERS-001":
        raise SystemExit(f"FAIL: unexpected active operational goals: {[row.get('id') for row in active]}")

    theorem = by_id.get("GOAL-OP-ONE-THEOREM-001", {})
    if theorem.get("status") != "superseded_with_reason":
        raise SystemExit("FAIL: theorem goal was not archived by owner directive")
    if theorem.get("return_to_goal_ids") != []:
        raise SystemExit("FAIL: archived theorem goal still has a mandatory return")

    engine = by_id.get("GOAL-OP-INVERSE-PRIME-FIBERS-001", {})
    if engine.get("status") != "active_current":
        raise SystemExit("FAIL: ENGINE-004 is not active_current")
    if "GOAL-PVG-INVERSE-GEOMETRY-001" not in engine.get("return_to_goal_ids", []):
        raise SystemExit("FAIL: ENGINE-004 does not return to inverse geometry")
    if "Phase D" not in str(engine.get("return_gate", "")):
        raise SystemExit("FAIL: ENGINE-004 return gate does not control Phase D")

    links = [row for path in LINK_FILES for row in load_jsonl(path)]
    linked = {
        (str(row.get("from_goal_id", "")), str(row.get("relation", "")), str(row.get("to_goal_id", "")))
        for row in links
    }
    for parent in engine.get("parent_goal_ids", []):
        if (str(engine["id"]), "serves", str(parent)) not in linked:
            raise SystemExit(f"FAIL: missing ENGINE-004 serves link to {parent}")
    for target in engine.get("return_to_goal_ids", []):
        if (str(engine["id"]), "returns_to", str(target)) not in linked:
            raise SystemExit(f"FAIL: missing ENGINE-004 return link to {target}")

    print("PVG–ANT Goal Memory and Traceability Audit: PASS")
    print(f"Current goals: {len(goals)}")
    print("Governing operational goal: GOAL-OP-INVERSE-PRIME-FIBERS-001")
    print("GOAL-OP-ONE-THEOREM-001: superseded_with_reason")
    print("Mandatory return: GOAL-PVG-INVERSE-GEOMETRY-001")
    print("Phase D: NOT AUTHORIZED")


if __name__ == "__main__":
    main()
