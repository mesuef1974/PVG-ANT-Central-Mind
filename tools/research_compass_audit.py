#!/usr/bin/env python3
"""Audit the canonical PVG–ANT research compass and operational goals.

This is a governance consistency check, not a mathematical proof checker.
Standard library only. Run from anywhere:

    python tools/research_compass_audit.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    "central-mind-charter.md",
    "central-mind-goals.md",
    "governance/pvg-ant-research-compass-v1.md",
    "governance/pvg-ant-goal-memory-and-return-protocol-v1.md",
    "governance/pvg-inverse-geometry-engine-architecture-v1.md",
    "maps/pvg-ant-language-kernel-v1.md",
    "governance/task-triggered-knowledge-activation-policy.md",
    "governance/stage-review-and-ceiling-escalation-policy.md",
    "governance/templates/research-readiness-card.md",
    "governance/readiness/SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS.md",
    "registries/program-goals.jsonl",
    "registries/goal-links.jsonl",
    "registries/rules.jsonl",
]

REQUIRED_RULE_IDS = {
    "RULE-TASK-FIRST-001",
    "RULE-READINESS-GATE-001",
    "RULE-MINIMUM-SUFFICIENT-KNOWLEDGE-001",
    "RULE-KNOWLEDGE-RETURN-001",
    "RULE-ONE-ACTIVE-RESEARCH-FRONT-001",
    "RULE-NO-REBUILD-BRIDGE-001",
    "RULE-CEILING-ESCALATION-001",
    "RULE-PVG-NECESSITY-TEST-001",
}

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
}


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


def main() -> None:
    issues: list[str] = []

    for relative_path in REQUIRED_FILES:
        require((ROOT / relative_path).is_file(), f"missing required compass file: {relative_path}", issues)

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)

    charter = (ROOT / "central-mind-charter.md").read_text(encoding="utf-8")
    goals_doc = (ROOT / "central-mind-goals.md").read_text(encoding="utf-8")
    compass = (ROOT / "governance/pvg-ant-research-compass-v1.md").read_text(encoding="utf-8")
    inverse_architecture = (ROOT / "governance/pvg-inverse-geometry-engine-architecture-v1.md").read_text(encoding="utf-8")
    kernel = (ROOT / "maps/pvg-ant-language-kernel-v1.md").read_text(encoding="utf-8")
    readiness = (ROOT / "governance/templates/research-readiness-card.md").read_text(encoding="utf-8")
    goal_memory = (
        ROOT / "governance/pvg-ant-goal-memory-and-return-protocol-v1.md"
    ).read_text(encoding="utf-8")
    synthesis_readiness = (
        ROOT / "governance/readiness/SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS.md"
    ).read_text(encoding="utf-8")

    require("Research Operating Charter v1.0" in charter, "charter is not v1.0", issues)
    require("One active research front" in charter, "charter omits one-active-front rule", issues)
    require("Original ANT contribution" in goals_doc, "goals omit strategic originality target", issues)
    require("Central Mind Goals v1.2" in goals_doc, "goals document is not v1.2", issues)
    require("GOAL-PVG-INVERSE-GEOMETRY-001" in goals_doc, "goals omit inverse geometry engine", issues)
    require("PASS-025 as first certified prototype" in inverse_architecture, "inverse architecture omits PASS-025 prototype classification", issues)
    require("Task-first" in compass or "المهمة أولًا" in compass, "compass omits task-first operation", issues)
    require("PVG–ANT Language Kernel" in kernel, "language kernel title missing", issues)
    require("READY | NOT_READY" in readiness, "readiness card omits binary decision", issues)
    require("Mandatory return rule" in goal_memory, "goal-memory protocol omits mandatory return", issues)
    require("READY" in synthesis_readiness, "SYNTHESIS-001 readiness is not READY", issues)

    goals = load_jsonl("registries/program-goals.jsonl")
    require(bool(goals), "program goals registry is empty", issues)

    goal_ids = [str(row.get("id", "")) for row in goals]
    require(len(goal_ids) == len(set(goal_ids)), "duplicate goal IDs", issues)
    require("GOAL-PVG-INVERSE-GEOMETRY-001" in goal_ids, "inverse geometry goal missing from registry", issues)

    for row in goals:
        missing = REQUIRED_GOAL_FIELDS - set(row)
        require(not missing, f"goal {row.get('id')} missing fields: {sorted(missing)}", issues)

    strategic = [row for row in goals if row.get("kind") == "strategic_goal"]
    require(len(strategic) == 1, f"expected one strategic goal, found {len(strategic)}", issues)
    if strategic:
        require(strategic[0].get("status") == "active_fixed", "strategic goal is not active_fixed", issues)

    inverse_goal = [row for row in goals if row.get("id") == "GOAL-PVG-INVERSE-GEOMETRY-001"]
    require(len(inverse_goal) == 1, "expected exactly one inverse geometry goal", issues)
    if inverse_goal:
        require(inverse_goal[0].get("kind") == "general_goal", "inverse geometry goal is not general_goal", issues)
        require(inverse_goal[0].get("status") == "active_long_term", "inverse geometry goal is not active_long_term", issues)

    active_operational = [
        row
        for row in goals
        if row.get("kind") == "operational_goal"
        and str(row.get("status", "")).startswith("active")
    ]
    require(
        len(active_operational) == 1,
        f"expected exactly one active operational research goal, found {len(active_operational)}",
        issues,
    )

    rules = load_jsonl("registries/rules.jsonl")
    rule_ids = {str(row.get("id", "")) for row in rules}
    require(REQUIRED_RULE_IDS <= rule_ids, f"missing compass rules: {sorted(REQUIRED_RULE_IDS - rule_ids)}", issues)

    links = load_jsonl("registries/goal-links.jsonl")
    require(bool(links), "goal links registry is empty", issues)

    for row in goals:
        if row.get("kind") == "operational_goal":
            require("research_front" in row, f"operational goal {row.get('id')} lacks research_front", issues)
            require("prerequisites" in row, f"operational goal {row.get('id')} lacks prerequisites", issues)
            require("next_review" in row, f"operational goal {row.get('id')} lacks next_review", issues)
            require("return_gate" in row, f"operational goal {row.get('id')} lacks return_gate", issues)

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)

    active_id = active_operational[0]["id"]
    print("Research Compass Audit: PASS")
    print(f"Strategic goal: {strategic[0]['id']}")
    print("Long-term inverse geometry goal: GOAL-PVG-INVERSE-GEOMETRY-001")
    print(f"Active operational goal: {active_id}")
    print(f"Registered goals: {len(goals)}")
    print(f"Registered goal links: {len(links)}")
    print(f"Required operating rules: {len(REQUIRED_RULE_IDS)}")


if __name__ == "__main__":
    main()
