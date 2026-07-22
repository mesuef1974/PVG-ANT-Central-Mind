#!/usr/bin/env python3
"""Audit PVG–ANT goal memory, dependency links, and mandatory returns.

Governance consistency only. This does not check mathematical truth.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "central-mind-goals.md",
    "governance/pvg-ant-goal-memory-and-return-protocol-v1.md",
    "governance/pvg-inverse-geometry-engine-architecture-v1.md",
    "governance/readiness/SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS.md",
    "governance/closures/SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS-CLOSURE.md",
    "research/pvg-space-deepening/synthesis-001-support-fiber-dynamics.md",
    "governance/readiness/PASS-025-REVERSE-SUPPORT-PREIMAGE.md",
    "governance/frozen-config/PASS-025-REVERSE-SUPPORT-PREIMAGE-FROZEN-CONFIG.md",
    "governance/closures/PASS-025-REVERSE-SUPPORT-PREIMAGE-CLOSURE.md",
    "research/pvg-space-deepening/pass-025-reverse-support-preimage.md",
    "research/pvg-space-deepening/data/reverse-support-preimage-summary.json",
    "governance/readiness/ENGINE-002-GENERAL-INVERSE-SUPPORT-KERNEL.md",
    "governance/closures/ENGINE-002-GENERAL-INVERSE-SUPPORT-KERNEL-CLOSURE.md",
    "research/pvg-space-deepening/engine-002-general-inverse-support-kernel.md",
    "research/pvg-space-deepening/data/inverse-support-kernel-summary.json",
    "tools/pvg_inverse_support_kernel.py",
    "tests/test_pvg_inverse_support_kernel.py",
    "registries/program-goals.jsonl",
    "registries/goal-links.jsonl",
    "registries/goal-links-engine-002.jsonl",
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
}

EXPECTED_ACTIVE_OPERATIONAL = "GOAL-OP-ONE-THEOREM-001"
EXPECTED_CLOSED_ENGINE = "GOAL-OP-INVERSE-SUPPORT-KERNEL-001"
EXPECTED_CLOSED_SYNTHESIS = "GOAL-OP-SUPPORT-FIBER-SYNTHESIS-001"
EXPECTED_CLOSED_PASS025 = "GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001"
INVERSE_GEOMETRY_GOAL = "GOAL-PVG-INVERSE-GEOMETRY-001"


def load_jsonl(relative_path: str) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    path = ROOT / relative_path
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
    protocol = (ROOT / "governance/pvg-ant-goal-memory-and-return-protocol-v1.md").read_text(encoding="utf-8")
    inverse_architecture = (ROOT / "governance/pvg-inverse-geometry-engine-architecture-v1.md").read_text(encoding="utf-8")
    engine_readiness = (ROOT / "governance/readiness/ENGINE-002-GENERAL-INVERSE-SUPPORT-KERNEL.md").read_text(encoding="utf-8")
    engine_closure = (ROOT / "governance/closures/ENGINE-002-GENERAL-INVERSE-SUPPORT-KERNEL-CLOSURE.md").read_text(encoding="utf-8")
    engine_note = (ROOT / "research/pvg-space-deepening/engine-002-general-inverse-support-kernel.md").read_text(encoding="utf-8")
    engine_summary = json.loads((ROOT / "research/pvg-space-deepening/data/inverse-support-kernel-summary.json").read_text(encoding="utf-8"))
    pass025_closure = (ROOT / "governance/closures/PASS-025-REVERSE-SUPPORT-PREIMAGE-CLOSURE.md").read_text(encoding="utf-8")
    pass025_summary = json.loads((ROOT / "research/pvg-space-deepening/data/reverse-support-preimage-summary.json").read_text(encoding="utf-8"))

    require("Central Mind Goals v1.2" in goals_doc, "goals document is not v1.2", issues)
    require("قاعدة عدم ضياع الأهداف" in goals_doc, "goals document omits non-loss rule", issues)
    require("GOAL-PVG-INVERSE-GEOMETRY-001" in goals_doc, "goals document omits inverse geometry goal", issues)
    require("Mandatory return rule" in protocol, "return protocol omits mandatory return rule", issues)
    require("Phase A — Inverse Support" in inverse_architecture, "inverse architecture omits Phase A", issues)
    require("Phase E — Inverse Analytic Translation" in inverse_architecture, "inverse architecture omits analytic phase", issues)
    require("PASS-025 as first certified prototype" in inverse_architecture, "inverse architecture does not classify PASS-025 as prototype", issues)
    require("Decision: READY" in engine_readiness, "ENGINE-002 readiness is not READY", issues)
    require("Decision: CLOSED" in engine_closure and "Stage decision: return" in engine_closure, "ENGINE-002 closure/return is incomplete", issues)
    require("Phase B: NOT AUTHORIZED" in engine_closure, "ENGINE-002 closure does not prohibit Phase B", issues)
    require("Depth search: NOT AUTHORIZED" in engine_closure, "ENGINE-002 closure does not prohibit depth search", issues)
    require("قانون حافة الشاهد" in engine_note, "ENGINE-002 note omits witness-edge law", issues)
    require(engine_summary.get("schema") == "PVG-INVERSE-SUPPORT-KERNEL-ENGINE-002-REGISTERED-SUMMARY", "ENGINE-002 summary schema mismatch", issues)
    require(engine_summary.get("reachable_target_count") == 20, "ENGINE-002 reachable count mismatch", issues)
    require(engine_summary.get("unreachable_target_count") == 541, "ENGINE-002 unreachable count mismatch", issues)
    require(engine_summary.get("verification", {}).get("soundness") is True, "ENGINE-002 soundness is not certified", issues)
    require(engine_summary.get("verification", {}).get("completeness_against_full_forward_enumeration") is True, "ENGINE-002 completeness is not certified", issues)
    require("Decision: CLOSED" in pass025_closure and "Stage decision: return" in pass025_closure, "PASS-025 closure/return is incomplete", issues)
    require(pass025_summary.get("outcome") == "DEPTH_12_WITNESS_FOUND_WITHIN_FROZEN_CLASS", "PASS-025 registered outcome mismatch", issues)

    goals = load_jsonl("registries/program-goals.jsonl")
    links = load_jsonl("registries/goal-links.jsonl") + load_jsonl("registries/goal-links-engine-002.jsonl")
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
            require(not missing_operational, f"operational goal {goal_id} missing fields: {sorted(missing_operational)}", issues)
            for ref in goal_refs(row.get("prerequisites")):
                require(ref in goal_id_set, f"goal {goal_id} prerequisite missing: {ref}", issues)

    active_operational = [
        row for row in goals
        if row.get("kind") == "operational_goal"
        and str(row.get("status", "")).startswith("active")
    ]
    require(len(active_operational) == 1, f"expected exactly one active operational goal, found {len(active_operational)}", issues)
    if active_operational:
        require(active_operational[0].get("id") == EXPECTED_ACTIVE_OPERATIONAL, f"unexpected active goal: {active_operational[0].get('id')}", issues)

    require(by_id.get(INVERSE_GEOMETRY_GOAL, {}).get("status") == "active_long_term", "inverse geometry goal is not active_long_term", issues)
    require(by_id.get(EXPECTED_CLOSED_SYNTHESIS, {}).get("status") == "closed", "SYNTHESIS-001 is not closed", issues)
    require(by_id.get(EXPECTED_CLOSED_PASS025, {}).get("status") == "closed", "PASS-025 is not closed", issues)
    require(by_id.get(EXPECTED_CLOSED_ENGINE, {}).get("status") == "closed", "ENGINE-002 is not closed", issues)
    require(by_id.get(EXPECTED_ACTIVE_OPERATIONAL, {}).get("status") == "active_external_validation_hold", "ONE-THEOREM-001 is not active_external_validation_hold", issues)
    require(EXPECTED_ACTIVE_OPERATIONAL in goal_refs(by_id.get(EXPECTED_CLOSED_ENGINE, {}).get("return_to_goal_ids")), "ENGINE-002 does not return to theorem goal", issues)
    require("Phase B" in str(by_id.get(EXPECTED_CLOSED_ENGINE, {}).get("return_gate", "")), "ENGINE-002 return gate does not prohibit Phase B", issues)

    link_ids = [str(row.get("id", "")) for row in links]
    require(len(link_ids) == len(set(link_ids)), "duplicate goal-link IDs", issues)
    linked_pairs: set[tuple[str, str, str]] = set()
    for row in links:
        source_id = str(row.get("from_goal_id", ""))
        target_id = str(row.get("to_goal_id", ""))
        relation = str(row.get("relation", ""))
        require(source_id in goal_id_set, f"goal link source missing: {source_id}", issues)
        require(target_id in goal_id_set, f"goal link target missing: {target_id}", issues)
        require(relation in {"serves", "returns_to"}, f"invalid goal-link relation: {relation}", issues)
        linked_pairs.add((source_id, relation, target_id))

    for row in goals:
        source_id = str(row["id"])
        for target_id in goal_refs(row.get("parent_goal_ids")):
            require((source_id, "serves", target_id) in linked_pairs, f"missing serves link: {source_id} -> {target_id}", issues)
        for target_id in goal_refs(row.get("return_to_goal_ids")):
            require((source_id, "returns_to", target_id) in linked_pairs, f"missing returns_to link: {source_id} -> {target_id}", issues)

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)

    print("PVG–ANT Goal Memory and Traceability Audit: PASS")
    print(f"Registered goals: {len(goals)}")
    print(f"Registered links: {len(links)}")
    print(f"Closed inverse kernel: {EXPECTED_CLOSED_ENGINE}")
    print(f"Returned active goal: {EXPECTED_ACTIVE_OPERATIONAL}")
    print("Phase B and depth search: NOT AUTHORIZED")


if __name__ == "__main__":
    main()
