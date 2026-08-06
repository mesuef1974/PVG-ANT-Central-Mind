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
    "maps/pvg-ant-language-kernel-v1.md",
    "governance/task-triggered-knowledge-activation-policy.md",
    "governance/stage-review-and-ceiling-escalation-policy.md",
    "governance/templates/research-readiness-card.md",
    "registries/program-goals.jsonl",
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
    "assimilation_target",
    "math_contribution_target",
    "operational_target",
    "certificate_target",
    "pvg_necessity_target",
    "claim_ceiling",
    "classification",
    "source",
}

TARGET_PREFIXES = {
    "assimilation_target": "ASSIM-",
    "math_contribution_target": "MATH-",
    "operational_target": "OPS-",
    "certificate_target": "CERT-",
    "pvg_necessity_target": "PVG-N",
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
    kernel = (ROOT / "maps/pvg-ant-language-kernel-v1.md").read_text(encoding="utf-8")
    readiness = (ROOT / "governance/templates/research-readiness-card.md").read_text(encoding="utf-8")

    require("Research Operating Charter v1.0" in charter, "charter is not v1.0", issues)
    require("One active research front" in charter, "charter omits one-active-front rule", issues)
    require("Original ANT contribution" in goals_doc, "goals omit strategic originality target", issues)
    require("Task-first" in compass or "المهمة أولًا" in compass, "compass omits task-first operation", issues)
    require("PVG–ANT Language Kernel" in kernel, "language kernel title missing", issues)
    require("READY | NOT_READY" in readiness, "readiness card omits binary decision", issues)

    goals = load_jsonl("registries/program-goals.jsonl")
    require(bool(goals), "program goals registry is empty", issues)

    goal_ids = [str(row.get("id", "")) for row in goals]
    require(len(goal_ids) == len(set(goal_ids)), "duplicate goal IDs", issues)

    for row in goals:
        missing = REQUIRED_GOAL_FIELDS - set(row)
        require(not missing, f"goal {row.get('id')} missing fields: {sorted(missing)}", issues)
        require("maturity_target" not in row, f"goal {row.get('id')} still uses deprecated maturity_target", issues)
        for field, prefix in TARGET_PREFIXES.items():
            value = str(row.get(field, ""))
            require(value.startswith(prefix), f"goal {row.get('id')} has invalid {field}: {value}", issues)

    strategic = [row for row in goals if row.get("kind") == "strategic_goal"]
    require(len(strategic) == 1, f"expected one strategic goal, found {len(strategic)}", issues)
    if strategic:
        require(strategic[0].get("status") == "active_fixed", "strategic goal is not active_fixed", issues)

    active_operational = [
        row for row in goals
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

    for row in goals:
        if row.get("kind") == "operational_goal":
            require("research_front" in row, f"operational goal {row.get('id')} lacks research_front", issues)
            require("prerequisites" in row, f"operational goal {row.get('id')} lacks prerequisites", issues)
            require("next_review" in row, f"operational goal {row.get('id')} lacks next_review", issues)

    if issues:
        for issue in issues:
            print(f"FAIL: {issue}")
        raise SystemExit(1)

    active_id = active_operational[0]["id"]
    print("Research Compass Audit: PASS")
    print(f"Strategic goal: {strategic[0]['id']}")
    print(f"Active operational goal: {active_id}")
    print(f"Registered goals: {len(goals)}")
    print(f"Required operating rules: {len(REQUIRED_RULE_IDS)}")


if __name__ == "__main__":
    main()
