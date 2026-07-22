#!/usr/bin/env python3
"""Audit PVG–ANT goal memory, dependency links, and mandatory return gates.

Governance consistency only. This does not check mathematical truth.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "central-mind-goals.md",
    "governance/pvg-ant-goal-memory-and-return-protocol-v1.md",
    "governance/readiness/SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS.md",
    "governance/closures/SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS-CLOSURE.md",
    "research/pvg-space-deepening/synthesis-001-support-fiber-dynamics.md",
    "registries/program-goals.jsonl",
    "registries/goal-links.jsonl",
]

REQUIRED_GOAL_FIELDS = {
    "kind",
    "id",
    "title",
    "status",
    "deliverable",
    "exit_criterion",
    "maturity_target",
    "claim_ceiling",
    "classification",
    "source",
    "parent_goal_ids",
    "return_to_goal_ids",
}

REQUIRED_OPERATIONAL_FIELDS = {
    "research_front",
    "prerequisites",
    "blocked_by",
    "next_review",
    "return_gate",
}

REQUIRED_GOAL_IDS = {
    "GOAL-PVG-ANT-STRATEGIC-001",
    "GOAL-PVG-ANT-LANGUAGE-001",
    "GOAL-PVG-ANT-ORIGINALITY-001",
    "GOAL-PVG-FOUNDATIONS-001",
    "GOAL-PVG-ADDITIVE-DYNAMICS-001",
    "GOAL-PVG-ANT-ADDITIVE-BRIDGE-001",
    "GOAL-CENTRAL-MIND-SPECIALIST-001",
    "GOAL-PVG-FORMAL-LEAN-001",
    "GOAL-PVG-COMPUTATIONAL-LAB-001",
    "GOAL-GOVERNANCE-MEMORY-001",
    "GOAL-SUPPORT-ANT-ENCYCLOPEDIA-001",
    "GOAL-SUPPORT-EXPOSITION-001",
    "GOAL-OP-ONE-THEOREM-001",
    "GOAL-OP-SUPPORT-FIBER-SYNTHESIS-001",
    "GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001",
}

EXPECTED_ACTIVE_OPERATIONAL = "GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001"
EXPECTED_CLOSED_SYNTHESIS = "GOAL-OP-SUPPORT-FIBER-SYNTHESIS-001"
MANDATORY_RETURN_GOAL = "GOAL-OP-ONE-THEOREM-001"


def load_jsonl(relative_path: str) -> list[dict[str, object]]:
    path = ROOT / relative_path
    rows: list[dict[str, object]] = []
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{relative_path}:{line_number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise RuntimeError(f"{relative_path}:{line_number}: row is not an object")
        rows.append(value)
    return rows


def require(condition: bool, message: str, issues: list[str]) -> None:
    if not condition:
        issues.append(message)


def goal_refs(values: object) -> list[str]:
    if not isinstance(values, list):
        return []
    return [str(value) for value in values if str(value).startswith("GOAL-")]


def main() -> None:
    issues: list[str] = []

    for relative_path in REQUIRED_FILES:
        require((ROOT / relative_path).is_file(), f"missing required goal-memory file: {relative_path}", issues)

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)

    goals_doc = (ROOT / "central-mind-goals.md").read_text(encoding="utf-8")
    protocol = (
        ROOT / "governance/pvg-ant-goal-memory-and-return-protocol-v1.md"
    ).read_text(encoding="utf-8")
    readiness = (
        ROOT / "governance/readiness/SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS.md"
    ).read_text(encoding="utf-8")
    closure = (
        ROOT / "governance/closures/SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS-CLOSURE.md"
    ).read_text(encoding="utf-8")

    require("Central Mind Goals v1.1" in goals_doc, "goals document is not v1.1", issues)
    require("قاعدة عدم ضياع الأهداف" in goals_doc, "goals document omits non-loss rule", issues)
    require("SYNTHESIS-001" in goals_doc, "goals document omits SYNTHESIS-001", issues)
    require("PASS-025" in goals_doc, "goals document omits PASS-025", issues)
    require("Mandatory return rule" in protocol, "return protocol omits mandatory return rule", issues)
    require("READY" in readiness, "SYNTHESIS-001 readiness card is not READY", issues)
    require("Decision: CLOSED" in closure, "SYNTHESIS-001 closure is not CLOSED", issues)
    require("bounded_extension" in closure, "SYNTHESIS-001 closure lacks bounded extension decision", issues)

    goals = load_jsonl("registries/program-goals.jsonl")
    links = load_jsonl("registries/goal-links.jsonl")

    goal_ids = [str(row.get("id", "")) for row in goals]
    goal_id_set = set(goal_ids)
    require(len(goal_ids) == len(goal_id_set), "duplicate goal IDs", issues)
    require(REQUIRED_GOAL_IDS <= goal_id_set, f"missing required goals: {sorted(REQUIRED_GOAL_IDS - goal_id_set)}", issues)

    by_id = {str(row["id"]): row for row in goals if "id" in row}

    for row in goals:
        goal_id = str(row.get("id", ""))
        missing = REQUIRED_GOAL_FIELDS - set(row)
        require(not missing, f"goal {goal_id} missing fields: {sorted(missing)}", issues)

        for ref in goal_refs(row.get("parent_goal_ids")) + goal_refs(row.get("return_to_goal_ids")):
            require(ref in goal_id_set, f"goal {goal_id} references missing goal {ref}", issues)

        if row.get("kind") == "operational_goal":
            missing_operational = REQUIRED_OPERATIONAL_FIELDS - set(row)
            require(
                not missing_operational,
                f"operational goal {goal_id} missing fields: {sorted(missing_operational)}",
                issues,
            )
            for ref in goal_refs(row.get("prerequisites")):
                require(ref in goal_id_set, f"goal {goal_id} prerequisite missing: {ref}", issues)
            if "paused" in str(row.get("status", "")):
                require(bool(row.get("return_gate")), f"paused goal {goal_id} lacks return_gate", issues)
                require(
                    bool(row.get("return_to_goal_ids")),
                    f"paused goal {goal_id} lacks return_to_goal_ids",
                    issues,
                )
            if str(row.get("status", "")).startswith("queued"):
                require(bool(row.get("prerequisites")), f"queued goal {goal_id} lacks prerequisites", issues)

    strategic = [row for row in goals if row.get("kind") == "strategic_goal"]
    require(len(strategic) == 1, f"expected one strategic goal, found {len(strategic)}", issues)
    if strategic:
        require(strategic[0].get("status") == "active_fixed", "strategic goal is not active_fixed", issues)

    active_operational = [
        row
        for row in goals
        if row.get("kind") == "operational_goal"
        and str(row.get("status", "")).startswith("active")
    ]
    require(
        len(active_operational) == 1,
        f"expected exactly one active operational goal, found {len(active_operational)}",
        issues,
    )
    if active_operational:
        require(
            active_operational[0].get("id") == EXPECTED_ACTIVE_OPERATIONAL,
            f"unexpected active operational goal: {active_operational[0].get('id')}",
            issues,
        )

    require(
        by_id.get(EXPECTED_CLOSED_SYNTHESIS, {}).get("status") == "closed",
        "SYNTHESIS-001 goal is not closed",
        issues,
    )
    require(
        by_id.get(EXPECTED_ACTIVE_OPERATIONAL, {}).get("status") == "active_current",
        "PASS-025 goal is not active_current",
        issues,
    )
    require(
        not by_id.get(EXPECTED_ACTIVE_OPERATIONAL, {}).get("blocked_by"),
        "PASS-025 remains blocked after synthesis closure",
        issues,
    )
    require(
        by_id.get(MANDATORY_RETURN_GOAL, {}).get("status") == "paused_governed_return_required",
        "ONE-THEOREM-001 is not preserved as a governed return goal",
        issues,
    )
    require(
        MANDATORY_RETURN_GOAL
        in goal_refs(by_id.get(EXPECTED_ACTIVE_OPERATIONAL, {}).get("return_to_goal_ids")),
        "PASS-025 does not return to ONE-THEOREM-001",
        issues,
    )
    require(
        "No PASS-026" in str(by_id.get(EXPECTED_ACTIVE_OPERATIONAL, {}).get("return_gate", "")),
        "PASS-025 return gate does not prohibit automatic PASS-026",
        issues,
    )

    link_ids = [str(row.get("id", "")) for row in links]
    require(len(link_ids) == len(set(link_ids)), "duplicate goal-link IDs", issues)
    linked_pairs: set[tuple[str, str, str]] = set()
    for row in links:
        link_id = str(row.get("id", ""))
        for field in ("from_goal_id", "relation", "to_goal_id", "status", "source"):
            require(field in row, f"goal link {link_id} missing {field}", issues)
        source_id = str(row.get("from_goal_id", ""))
        target_id = str(row.get("to_goal_id", ""))
        relation = str(row.get("relation", ""))
        require(source_id in goal_id_set, f"goal link {link_id} source missing: {source_id}", issues)
        require(target_id in goal_id_set, f"goal link {link_id} target missing: {target_id}", issues)
        require(relation in {"serves", "returns_to"}, f"goal link {link_id} invalid relation: {relation}", issues)
        linked_pairs.add((source_id, relation, target_id))

    for row in goals:
        source_id = str(row["id"])
        for target_id in goal_refs(row.get("parent_goal_ids")):
            require(
                (source_id, "serves", target_id) in linked_pairs,
                f"missing serves link: {source_id} -> {target_id}",
                issues,
            )
        for target_id in goal_refs(row.get("return_to_goal_ids")):
            require(
                (source_id, "returns_to", target_id) in linked_pairs,
                f"missing returns_to link: {source_id} -> {target_id}",
                issues,
            )

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)

    print("PVG–ANT Goal Memory and Traceability Audit: PASS")
    print(f"Registered goals: {len(goals)}")
    print(f"Registered links: {len(links)}")
    print(f"Closed synthesis goal: {EXPECTED_CLOSED_SYNTHESIS}")
    print(f"Active operational goal: {EXPECTED_ACTIVE_OPERATIONAL}")
    print(f"Mandatory return goal: {MANDATORY_RETURN_GOAL}")


if __name__ == "__main__":
    main()
