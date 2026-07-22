#!/usr/bin/env python3
"""Audit PVG–ANT goal memory, dependency links, and mandatory returns."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "central-mind-goals.md",
    "governance/pvg-ant-goal-memory-and-return-protocol-v1.md",
    "governance/pvg-inverse-geometry-engine-architecture-v1.md",
    "governance/closures/PASS-025-REVERSE-SUPPORT-PREIMAGE-CLOSURE.md",
    "research/pvg-space-deepening/data/reverse-support-preimage-summary.json",
    "governance/readiness/ENGINE-002-GENERAL-INVERSE-SUPPORT-KERNEL.md",
    "governance/closures/ENGINE-002-GENERAL-INVERSE-SUPPORT-KERNEL-CLOSURE.md",
    "research/pvg-space-deepening/data/inverse-support-kernel-summary.json",
    "governance/readiness/ENGINE-003-INVERSE-INTEGER-FIBERS.md",
    "research/pvg-space-deepening/engine-003-inverse-integer-fibers.md",
    "research/pvg-space-deepening/data/inverse-integer-fibers-summary.json",
    "tools/pvg_inverse_integer_fibers.py",
    "tests/test_pvg_inverse_integer_fibers.py",
    "registries/program-goals.jsonl",
    "registries/goal-links.jsonl",
    "registries/goal-links-engine-002.jsonl",
    "registries/goal-links-engine-003.jsonl",
]

REQUIRED_GOAL_FIELDS = {
    "kind", "id", "title", "status", "deliverable", "exit_criterion",
    "maturity_target", "claim_ceiling", "classification", "source",
    "parent_goal_ids", "return_to_goal_ids",
}
REQUIRED_OPERATIONAL_FIELDS = {
    "research_front", "prerequisites", "blocked_by", "next_review", "return_gate",
}
REQUIRED_GOAL_IDS = {
    "GOAL-PVG-ANT-STRATEGIC-001", "GOAL-PVG-ANT-LANGUAGE-001",
    "GOAL-PVG-ANT-ORIGINALITY-001", "GOAL-PVG-FOUNDATIONS-001",
    "GOAL-PVG-ADDITIVE-DYNAMICS-001", "GOAL-PVG-INVERSE-GEOMETRY-001",
    "GOAL-PVG-ANT-ADDITIVE-BRIDGE-001", "GOAL-CENTRAL-MIND-SPECIALIST-001",
    "GOAL-PVG-FORMAL-LEAN-001", "GOAL-PVG-COMPUTATIONAL-LAB-001",
    "GOAL-GOVERNANCE-MEMORY-001", "GOAL-SUPPORT-ANT-ENCYCLOPEDIA-001",
    "GOAL-SUPPORT-EXPOSITION-001", "GOAL-OP-ONE-THEOREM-001",
    "GOAL-OP-SUPPORT-FIBER-SYNTHESIS-001",
    "GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001",
    "GOAL-OP-INVERSE-SUPPORT-KERNEL-001",
    "GOAL-OP-INVERSE-INTEGER-FIBERS-001",
}

EXPECTED_ACTIVE = "GOAL-OP-INVERSE-INTEGER-FIBERS-001"
THEOREM_GOAL = "GOAL-OP-ONE-THEOREM-001"
INVERSE_GOAL = "GOAL-PVG-INVERSE-GEOMETRY-001"


def load_jsonl(path: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line_number, raw in enumerate((ROOT / path).read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            value = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"{path}:{line_number}: invalid JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise RuntimeError(f"{path}:{line_number}: row is not an object")
        rows.append(value)
    return rows


def refs(values: object) -> list[str]:
    return [str(value) for value in values] if isinstance(values, list) else []


def require(condition: bool, message: str, issues: list[str]) -> None:
    if not condition:
        issues.append(message)


def main() -> None:
    issues: list[str] = []
    for path in REQUIRED_FILES:
        require((ROOT / path).is_file(), f"missing required file: {path}", issues)
    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)

    engine002_closure = (ROOT / "governance/closures/ENGINE-002-GENERAL-INVERSE-SUPPORT-KERNEL-CLOSURE.md").read_text(encoding="utf-8")
    engine003_readiness = (ROOT / "governance/readiness/ENGINE-003-INVERSE-INTEGER-FIBERS.md").read_text(encoding="utf-8")
    engine003_note = (ROOT / "research/pvg-space-deepening/engine-003-inverse-integer-fibers.md").read_text(encoding="utf-8")
    engine003_summary = json.loads((ROOT / "research/pvg-space-deepening/data/inverse-integer-fibers-summary.json").read_text(encoding="utf-8"))

    require("Decision: CLOSED" in engine002_closure, "ENGINE-002 is not closed", issues)
    require("READY" in engine003_readiness, "ENGINE-003 readiness is not READY", issues)
    require("Exponent-lattice bijection" in engine003_note, "ENGINE-003 note omits exponent-lattice law", issues)
    require("Phase C is not authorized" in engine003_note, "ENGINE-003 note does not block Phase C", issues)
    require(engine003_summary.get("scope", {}).get("support_face_count") == 25, "ENGINE-003 face count mismatch", issues)
    require(engine003_summary.get("totals", {}).get("total_fiber_points_across_faces") == 884, "ENGINE-003 point count mismatch", issues)
    require(engine003_summary.get("totals", {}).get("complete_scan_mismatch_count") == 0, "ENGINE-003 complete scan mismatch", issues)
    require(all(engine003_summary.get("verification", {}).values()), "ENGINE-003 verification flags are not all true", issues)
    require(engine003_summary.get("claim_ceiling", {}).get("phase_c_authorized") is False, "Phase C is unexpectedly authorized", issues)

    goals = load_jsonl("registries/program-goals.jsonl")
    links = (
        load_jsonl("registries/goal-links.jsonl")
        + load_jsonl("registries/goal-links-engine-002.jsonl")
        + load_jsonl("registries/goal-links-engine-003.jsonl")
    )
    goal_ids = [str(row.get("id", "")) for row in goals]
    goal_set = set(goal_ids)
    require(len(goal_ids) == len(goal_set), "duplicate goal IDs", issues)
    require(REQUIRED_GOAL_IDS <= goal_set, f"missing goals: {sorted(REQUIRED_GOAL_IDS - goal_set)}", issues)
    by_id = {str(row["id"]): row for row in goals}

    for row in goals:
        goal_id = str(row.get("id", ""))
        require(not (REQUIRED_GOAL_FIELDS - set(row)), f"goal {goal_id} missing required fields", issues)
        for target in refs(row.get("parent_goal_ids")) + refs(row.get("return_to_goal_ids")):
            if target.startswith("GOAL-"):
                require(target in goal_set, f"goal {goal_id} references missing goal {target}", issues)
        if row.get("kind") == "operational_goal":
            require(not (REQUIRED_OPERATIONAL_FIELDS - set(row)), f"operational goal {goal_id} missing fields", issues)

    active = [
        row for row in goals
        if row.get("kind") == "operational_goal"
        and str(row.get("status", "")).startswith("active")
    ]
    require(len(active) == 1, f"expected one active operational goal, found {len(active)}", issues)
    if active:
        require(active[0].get("id") == EXPECTED_ACTIVE, f"unexpected active goal: {active[0].get('id')}", issues)

    require(by_id.get(INVERSE_GOAL, {}).get("status") == "active_long_term", "inverse geometry goal is not active_long_term", issues)
    require(by_id.get("GOAL-OP-INVERSE-SUPPORT-KERNEL-001", {}).get("status") == "closed", "ENGINE-002 is not closed in registry", issues)
    require(by_id.get(EXPECTED_ACTIVE, {}).get("status") == "active_current", "ENGINE-003 is not active_current", issues)
    require(by_id.get(THEOREM_GOAL, {}).get("status") == "paused_governed_return_required", "theorem goal is not paused for ENGINE-003", issues)
    require(THEOREM_GOAL in refs(by_id.get(EXPECTED_ACTIVE, {}).get("return_to_goal_ids")), "ENGINE-003 does not return to theorem goal", issues)
    require("Phase C" in str(by_id.get(EXPECTED_ACTIVE, {}).get("return_gate", "")), "ENGINE-003 return gate does not control Phase C", issues)

    link_ids = [str(row.get("id", "")) for row in links]
    require(len(link_ids) == len(set(link_ids)), "duplicate goal-link IDs", issues)
    linked_pairs = {
        (str(row.get("from_goal_id", "")), str(row.get("relation", "")), str(row.get("to_goal_id", "")))
        for row in links
    }
    for row in goals:
        source = str(row["id"])
        for target in refs(row.get("parent_goal_ids")):
            if target.startswith("GOAL-"):
                require((source, "serves", target) in linked_pairs, f"missing serves link: {source} -> {target}", issues)
        for target in refs(row.get("return_to_goal_ids")):
            if target.startswith("GOAL-"):
                require((source, "returns_to", target) in linked_pairs, f"missing returns_to link: {source} -> {target}", issues)

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)

    print("PVG–ANT Goal Memory and Traceability Audit: PASS")
    print(f"Registered goals: {len(goals)}")
    print(f"Registered links: {len(links)}")
    print(f"Active Phase B goal: {EXPECTED_ACTIVE}")
    print(f"Mandatory return goal: {THEOREM_GOAL}")
    print("Phase C: NOT AUTHORIZED")


if __name__ == "__main__":
    main()
