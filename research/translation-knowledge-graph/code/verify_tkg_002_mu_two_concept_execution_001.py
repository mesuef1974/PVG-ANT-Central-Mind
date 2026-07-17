from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

from tkg_002_executable_rule_engine_001 import (
    EXECUTED_FROM_REGISTRY_RULE,
    INSUFFICIENT_KNOWLEDGE,
    OPERATORS,
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


def remove_rule_contract(records: list[dict], rule_id: str) -> list[dict]:
    changed = copy.deepcopy(records)
    found = False
    for record in changed:
        if record.get("rule_id") == rule_id:
            record.pop("executable_rule", None)
            found = True
    assert found
    return changed


def execute(executor: TKG002Executor, query: str, expected: int):
    result = executor.execute(query)
    assert result.status == EXECUTED_FROM_REGISTRY_RULE
    assert result.result == expected
    assert_provenance(result)
    return result


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

    # Gate 1: strict parse of every physical record in both sources.
    base_records = load_jsonl(registry_path)
    rule_records = load_jsonl(rules_path)
    assert base_records
    assert len(rule_records) == 2

    # Gates 2 and 3: reviewed rule and operator contracts are explicit.
    rules_by_id = {record.get("rule_id"): record for record in rule_records}
    mu_rule = rules_by_id["TKG002-EXEC-MU-001"]
    tau_rule = rules_by_id["TKG002-EXEC-TAU-001"]
    assert mu_rule["source_node_id"] == "TKG002-NODE-MU"
    assert mu_rule["executable_rule"] == {
        "operator_id": "OP-EVALUATE-MOBIUS-001",
        "args": {},
        "result_symbol": "mu",
    }
    assert tau_rule["source_node_id"] == "TKG002-NODE-TAU"
    assert "OP-EVALUATE-MOBIUS-001" in OPERATORS
    assert "OP-EVALUATE-DIVISOR-SUM-001" in OPERATORS

    # Gate 4: structural contamination audit. Branch examples may be authored;
    # unseen values must not occur as example inputs anywhere in TKG-002.
    unseen_cases = {
        10: 1,
        105: -1,
        18: 0,
        510510: -1,
        2: -1,
        4: 0,
        988027: 1,
    }
    authored_example_inputs: set[int] = set()
    for record in base_records:
        for example in record.get("examples") or []:
            if isinstance(example, dict) and isinstance(example.get("n"), int):
                authored_example_inputs.add(example["n"])
    assert not (set(unseen_cases) & authored_example_inputs)

    with tempfile.TemporaryDirectory() as temporary_directory:
        temporary = Path(temporary_directory)
        baseline_registry = temporary / "baseline-registry.jsonl"
        baseline_rules = temporary / "baseline-rules.jsonl"
        write_jsonl(baseline_registry, base_records)
        write_jsonl(baseline_rules, rule_records)
        baseline_executor = TKG002Executor(baseline_registry, baseline_rules)

        # Gate 5: every logical branch, including empty support at n=1.
        branch_cases = {1: 1, 6: 1, 30: -1, 12: 0}
        branch_results = {
            n: execute(baseline_executor, f"mu({n})", expected).result
            for n, expected in branch_cases.items()
        }

        # Gate 4/5 extension: values absent from all authored examples.
        unseen_results = {
            n: execute(baseline_executor, f"mu({n})", expected).result
            for n, expected in unseen_cases.items()
        }

        # Gate 6: codomain over a wider range, in addition to branch values.
        codomain_values = {
            baseline_executor.execute(f"mu({n})").result for n in range(1, 2001)
        }
        assert codomain_values <= {-1, 0, 1}
        assert codomain_values == {-1, 0, 1}

        # Gate 7: multi-rule routing and tau regression after refactor.
        tau_baseline = execute(baseline_executor, "tau(360)", 24)
        mu_baseline = execute(baseline_executor, "mu(12)", 0)
        assert tau_baseline.source_node_id == "TKG002-NODE-TAU"
        assert tau_baseline.rule_id == "TKG002-EXEC-TAU-001"
        assert mu_baseline.source_node_id == "TKG002-NODE-MU"
        assert mu_baseline.rule_id == "TKG002-EXEC-MU-001"

        # Gate 8A: deleting mu leaves tau alive and mu refused.
        no_mu_rules = temporary / "without-mu-rule.jsonl"
        write_jsonl(no_mu_rules, remove_rule_contract(rule_records, "TKG002-EXEC-MU-001"))
        no_mu_executor = TKG002Executor(baseline_registry, no_mu_rules)
        mu_refusal = no_mu_executor.execute("mu(12)")
        assert mu_refusal.status == INSUFFICIENT_KNOWLEDGE
        assert mu_refusal.steps == ()
        tau_survives_mu_deletion = execute(no_mu_executor, "tau(360)", 24)

        # Gate 8B: deleting tau leaves mu alive and tau refused.
        no_tau_rules = temporary / "without-tau-rule.jsonl"
        write_jsonl(no_tau_rules, remove_rule_contract(rule_records, "TKG002-EXEC-TAU-001"))
        no_tau_executor = TKG002Executor(baseline_registry, no_tau_rules)
        tau_refusal = no_tau_executor.execute("tau(360)")
        assert tau_refusal.status == INSUFFICIENT_KNOWLEDGE
        assert tau_refusal.steps == ()
        mu_survives_tau_deletion = execute(no_tau_executor, "mu(12)", 0)

        # Gate 9A: delete all descriptive examples; both rules still execute.
        without_examples = copy.deepcopy(base_records)
        for record in without_examples:
            record.pop("examples", None)
        no_examples_registry = temporary / "without-examples.jsonl"
        write_jsonl(no_examples_registry, without_examples)
        no_examples_executor = TKG002Executor(no_examples_registry, baseline_rules)
        mu_without_examples = execute(no_examples_executor, "mu(12)", 0)
        tau_without_examples = execute(no_examples_executor, "tau(360)", 24)

        # Gate 9B is the mu deletion above: examples retained, rule absent, refusal.
        assert mu_refusal.status == INSUFFICIENT_KNOWLEDGE

    report = {
        "gate": "TKG-002-MU-TWO-CONCEPT-EXECUTION-001",
        "parse_gate": "PASS",
        "rule_and_operator_review": "PASS",
        "contamination": "CLEAN_RULE_ONLY_FOR_UNSEEN_CASES",
        "branch_cases": branch_results,
        "unseen_cases": unseen_results,
        "codomain_1_to_2000": sorted(codomain_values),
        "multi_rule_routing": {
            "tau": tau_baseline.result,
            "mu": mu_baseline.result,
        },
        "bidirectional_isolation": {
            "delete_mu_mu_status": mu_refusal.status,
            "delete_mu_tau_result": tau_survives_mu_deletion.result,
            "delete_tau_tau_status": tau_refusal.status,
            "delete_tau_mu_result": mu_survives_tau_deletion.result,
        },
        "double_deletion": {
            "delete_examples_mu_result": mu_without_examples.result,
            "delete_examples_tau_result": tau_without_examples.result,
            "delete_mu_rule_status": mu_refusal.status,
        },
        "provenance": "PASS",
        "reasoning_claim": "NOT_AUTHORIZED",
        "classification": "TWO_CONCEPT_EXECUTION_FRAMEWORK_CANDIDATE_PENDING_PINNED_REPLAY",
        "math": "MATH-M0",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
