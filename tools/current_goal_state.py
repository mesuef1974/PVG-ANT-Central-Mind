#!/usr/bin/env python3
"""Resolve the current governed goal state from base rows plus ordered overrides.

The base registry is append-only historical memory. Override registries carry
explicit owner-authorized state transitions and are applied in filename order.
This module centralizes that resolution so audits do not disagree about which
operational goal is current.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
BASE_GOALS = ROOT / "registries" / "program-goals.jsonl"
OVERRIDE_GLOB = "goal-state-overrides-*.jsonl"


def load_jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{path.relative_to(ROOT)}:{line_number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise RuntimeError(
                f"{path.relative_to(ROOT)}:{line_number}: row is not a JSON object"
            )
        if not str(value.get("id", "")).strip():
            raise RuntimeError(f"{path.relative_to(ROOT)}:{line_number}: missing id")
        rows.append(value)
    return rows


def override_paths() -> tuple[Path, ...]:
    return tuple(sorted((ROOT / "registries").glob(OVERRIDE_GLOB)))


def current_goals() -> list[dict[str, object]]:
    ordered = load_jsonl(BASE_GOALS)
    by_id = {str(row["id"]): row for row in ordered}
    order = [str(row["id"]) for row in ordered]
    for path in override_paths():
        for row in load_jsonl(path):
            goal_id = str(row["id"])
            if goal_id not in by_id:
                order.append(goal_id)
            by_id[goal_id] = row
    return [by_id[goal_id] for goal_id in order]


def active_operational_goals(
    goals: Iterable[dict[str, object]] | None = None,
) -> list[dict[str, object]]:
    source = current_goals() if goals is None else list(goals)
    return [
        row
        for row in source
        if row.get("kind") == "operational_goal"
        and str(row.get("status", "")).startswith("active")
    ]


def current_goal_by_id(goal_id: str) -> dict[str, object]:
    for row in current_goals():
        if row.get("id") == goal_id:
            return row
    raise KeyError(goal_id)


if __name__ == "__main__":
    goals = current_goals()
    active = active_operational_goals(goals)
    print(json.dumps({
        "base": str(BASE_GOALS.relative_to(ROOT)),
        "overrides": [str(path.relative_to(ROOT)) for path in override_paths()],
        "goal_count": len(goals),
        "active_operational_goal_ids": [row["id"] for row in active],
    }, ensure_ascii=False, indent=2))
