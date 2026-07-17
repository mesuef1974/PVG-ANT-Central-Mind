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
    load_registry_jsonl,
    load_rule_jsonl,
)


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n" for record in records),
        encoding="utf-8",
    )


def execute(executor: TKG002Executor, query: str, expected):
    result = executor.execute(query)
    assert result.status == EXECUTED_FROM_REGISTRY_RULE
    assert result.result == expected
    assert result.steps
    for step in result.steps:
        assert (step.source_node_id is None) != (step.operator_id is None)
    return result


def remove_rule_contract(records: list[dict], rule_id: str) -> list[dict]:
    changed = copy.deepcopy(records)
    found = False
    for record in changed:
        if record.get("rule_id") == rule_id:
            record.pop("executable_rule", None)
            found = True
    assert found
    return changed


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    tkg001 = repo_root / "research/translation-knowledge-graph/registry/tkg-001-von-mangoldt-core.jsonl"
    tkg002 = repo_root / "research/translation-knowledge-graph/registry/tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl"
    rules_path = repo_root / "research/translation-knowledge-graph/registry/executable/tkg-002-executable-rules-001.jsonl"

    # Gate 1: strict parse of both registries and the executable-rule registry.
    registry_records = load_registry_jsonl((tkg001, tkg002))
    rule_records = load_rule_jsonl(rules_path)
    assert len({record["record_id"] for record in registry_records}) == len(registry_records)
    assert len({record["rule_id"] for record in rule_records}) == len(rule_records)

    # Gate 2: the reviewed source node and exact executable contract are explicit.
    nodes = {record["record_id"]: record for record in registry_records}
    rules = {record["rule_id"]: record for record in rule_records}
    assert "TKG001-NODE-LAMBDA" in nodes
    lambda_rule = rules["TKG001-EXEC-LAMBDA-001"]
    assert lambda_rule["source_node_id"] == "TKG001-NODE-LAMBDA"
    assert lambda_rule["executable_rule"] == {
        "operator_id": "OP-EVALUATE-VON-MANGOLDT-001",
        "args": {},
        "result_symbol": "lambda",
    }
    assert "OP-EVALUATE-VON-MANGOLDT-001" in OPERATORS

    with tempfile.TemporaryDirectory() as directory:
        temporary = Path(directory)
        combined_registry = temporary / "combined-registry.jsonl"
        rules = temporary / "rules.jsonl"
        write_jsonl(combined_registry, registry_records)
        write_jsonl(rules, rule_records)
        executor = TKG002Executor(combined_registry, rules)

        # Gates 3-5: exact symbolic values for every logical branch; no floats.
        cases = {
            1: {"kind": "ZERO"},
            2: {"kind": "LOG_PRIME", "prime": 2},
            8: {"kind": "LOG_PRIME", "prime": 2},
            12: {"kind": "ZERO"},
            27: {"kind": "LOG_PRIME", "prime": 3},
            49: {"kind": "LOG_PRIME", "prime": 7},
            125: {"kind": "LOG_PRIME", "prime": 5},
            72: {"kind": "ZERO"},
            97: {"kind": "LOG_PRIME", "prime": 97},
        }
        lambda_results = {n: execute(executor, f"lambda({n})", expected) for n, expected in cases.items()}
        for result in lambda_results.values():
            assert isinstance(result.result, dict)
            assert not any(isinstance(value, float) for value in result.result.values())

        # Gate 6: operator-owned provenance; no inherited tau or mu steps.
        lambda_descriptions = [step.description for step in lambda_results[49].steps[1:]]
        assert lambda_descriptions == [
            "Factor input integer",
            "Count distinct prime support",
            "Detect single-axis prime-power support",
            "Evaluate von Mangoldt as a structured symbolic value",
        ]
        assert "Enumerate divisors" not in lambda_descriptions
        assert "Detect exponent greater than one" not in lambda_descriptions

        # Gate 7: tau and mu non-regression under three-rule routing.
        tau = execute(executor, "tau(360)", 24)
        mu = execute(executor, "mu(12)", 0)
        assert tau.source_node_id == "TKG002-NODE-TAU"
        assert mu.source_node_id == "TKG002-NODE-MU"

        # Gate 8: deleting only Lambda refuses Lambda and preserves tau/mu.
        without_lambda = temporary / "without-lambda.jsonl"
        write_jsonl(without_lambda, remove_rule_contract(rule_records, "TKG001-EXEC-LAMBDA-001"))
        no_lambda_executor = TKG002Executor(combined_registry, without_lambda)
        refused = no_lambda_executor.execute("lambda(49)")
        assert refused.status == INSUFFICIENT_KNOWLEDGE and refused.steps == ()
        execute(no_lambda_executor, "tau(360)", 24)
        execute(no_lambda_executor, "mu(12)", 0)

        # Gate 9: deleting descriptive examples does not affect execution.
        without_examples = copy.deepcopy(registry_records)
        for record in without_examples:
            record.pop("examples", None)
        no_examples_registry = temporary / "without-examples.jsonl"
        write_jsonl(no_examples_registry, without_examples)
        no_examples_executor = TKG002Executor(no_examples_registry, rules)
        execute(no_examples_executor, "lambda(49)", {"kind": "LOG_PRIME", "prime": 7})
        execute(no_examples_executor, "tau(360)", 24)
        execute(no_examples_executor, "mu(12)", 0)

    # Gate 10 remains an external pinned clean-checkout replay requirement.
    print(json.dumps({
        "gate": "TKG001-NODE-LAMBDA-STRUCTURED-EXECUTION-001",
        "parse_gate": "PASS",
        "duplicate_id_audit": "PASS",
        "structured_value": "PASS_NO_FLOAT_NO_EPSILON",
        "operator_owned_steps": "PASS",
        "three_rule_routing": {"tau(360)": tau.result, "mu(12)": mu.result, "lambda(49)": cases[49]},
        "lambda_rule_isolation": refused.status,
        "classification": "THREE_CONCEPT_EXECUTION_CANDIDATE_PENDING_PINNED_REPLAY",
        "general_reasoning_engine": "NOT_AUTHORIZED",
        "math": "MATH-M0",
        "pnt": "NONE",
        "pnt_ap": "NONE",
        "goldbach": "NONE",
        "rh": "NONE",
        "grh": "NONE",
        "merge_to_main": "NOT_AUTHORIZED",
    }, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
