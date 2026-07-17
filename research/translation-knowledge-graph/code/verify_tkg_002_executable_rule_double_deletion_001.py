from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

from tkg_002_executable_rule_engine_001 import (
    EXECUTED_FROM_REGISTRY_RULE,
    INSUFFICIENT_KNOWLEDGE,
    TKG002Executor,
    load_jsonl,
)


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.write_text(
        "".join(
            json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
            for record in records
        ),
        encoding="utf-8",
    )


def assert_provenance(result) -> None:
    assert result.steps
    for step in result.steps:
        assert (step.source_node_id is None) != (step.operator_id is None)


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    registry_path = (
        repo_root
        / "research"
        / "translation-knowledge-graph"
        / "registry"
        / "tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl"
    )
    rules_path = (
        repo_root
        / "research"
        / "translation-knowledge-graph"
        / "registry"
        / "executable"
        / "tkg-002-executable-rules-001.jsonl"
    )

    base_records = load_jsonl(registry_path)
    rule_records = load_jsonl(rules_path)

    # Structural contamination audit. Raw occurrence of 24 is not disqualifying:
    # TKG-002 contains n=24 as an example input, but not the tested pair tau(360)=24.
    direct_answer_present = False
    for record in base_records:
        for example in record.get("examples") or []:
            if not isinstance(example, dict):
                continue
            if example.get("n") == 360 and example.get("value") == 24:
                direct_answer_present = True
    assert not direct_answer_present

    with tempfile.TemporaryDirectory() as temporary_directory:
        temporary = Path(temporary_directory)
        baseline_registry = temporary / "baseline-registry.jsonl"
        baseline_rules = temporary / "baseline-rules.jsonl"
        write_jsonl(baseline_registry, base_records)
        write_jsonl(baseline_rules, rule_records)

        baseline = TKG002Executor(baseline_registry, baseline_rules).execute("tau(360)")
        assert baseline.status == EXECUTED_FROM_REGISTRY_RULE
        assert baseline.result == 24
        assert baseline.source_node_id == "TKG002-NODE-TAU"
        assert baseline.rule_id == "TKG002-EXEC-TAU-001"
        assert_provenance(baseline)

        # Deletion A: remove all examples while preserving the general rule.
        without_examples = copy.deepcopy(base_records)
        for record in without_examples:
            record.pop("examples", None)
        no_examples_registry = temporary / "without-examples.jsonl"
        write_jsonl(no_examples_registry, without_examples)
        deletion_a = TKG002Executor(no_examples_registry, baseline_rules).execute("tau(360)")
        assert deletion_a.status == EXECUTED_FROM_REGISTRY_RULE
        assert deletion_a.result == 24
        assert_provenance(deletion_a)

        # Deletion B: preserve examples but remove the executable contract.
        without_rule = copy.deepcopy(rule_records)
        for record in without_rule:
            record.pop("executable_rule", None)
        no_rule_path = temporary / "without-executable-rule.jsonl"
        write_jsonl(no_rule_path, without_rule)
        deletion_b = TKG002Executor(baseline_registry, no_rule_path).execute("tau(360)")
        assert deletion_b.status == INSUFFICIENT_KNOWLEDGE
        assert deletion_b.result is None
        assert deletion_b.steps == ()

    report = {
        "gate": "TKG-002-EXECUTABLE-RULE-DOUBLE-DELETION-001",
        "contamination": "CLEAN_RULE_ONLY",
        "baseline": {
            "query": "tau(360)",
            "status": baseline.status,
            "result": baseline.result,
            "source_node_id": baseline.source_node_id,
            "rule_id": baseline.rule_id,
        },
        "delete_examples_keep_rule": {
            "status": deletion_a.status,
            "result": deletion_a.result,
        },
        "delete_rule_keep_examples": {
            "status": deletion_b.status,
            "result": deletion_b.result,
        },
        "provenance": "PASS",
        "engine_contains_case_result": False,
        "reasoning_claim": "NOT_AUTHORIZED",
        "math": "MATH-M0",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
