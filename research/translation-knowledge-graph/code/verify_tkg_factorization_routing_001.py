from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from sympy import factorint

from tkg_002_executable_rule_engine_001 import (
    EXECUTED_FROM_REGISTRY_RULE,
    INSUFFICIENT_KNOWLEDGE,
    TKG002Executor,
    load_registry_jsonl,
    load_rule_jsonl,
)
from tkg_composite_value_contract_001 import reconstruct_n
from tkg_execution_value_contract_001 import validate_execution_value


FACTOR_RULE_ID = "TKG002-EXEC-FACTORIZE-001"
FACTOR_NODE_ID = "TKG002-NODE-DIVISOR-BOX"
FACTOR_OPERATOR_ID = "OP-FACTORIZE-INTEGER-001"


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.write_text(
        "".join(
            json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
            for record in records
        ),
        encoding="utf-8",
    )


def run_script(code_dir: Path, script: str) -> int:
    completed = subprocess.run(
        [sys.executable, str(code_dir / script)],
        cwd=code_dir,
        text=True,
        capture_output=True,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(
            f"non-regression failed in {script}:\n"
            f"STDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )
    return completed.returncode


def expected_factorization(n: int) -> dict:
    return {
        "kind": "PRIME_FACTORIZATION",
        "factors": [
            {"prime": int(prime), "exponent": int(exponent)}
            for prime, exponent in sorted(factorint(n).items())
        ],
    }


def execute_factorize(executor: TKG002Executor, n: int):
    result = executor.execute(f"factorize({n})")
    assert result.status == EXECUTED_FROM_REGISTRY_RULE
    assert result.source_node_id == FACTOR_NODE_ID
    assert result.rule_id == FACTOR_RULE_ID
    assert result.result == expected_factorization(n)
    assert validate_execution_value(result.result) == result.result
    assert reconstruct_n(result.result) == n
    assert result.steps
    assert result.steps[0].source_node_id == FACTOR_NODE_ID
    assert result.steps[0].operator_id is None
    operator_steps = result.steps[1:]
    assert operator_steps
    assert all(step.operator_id is not None and step.source_node_id is None for step in operator_steps)
    assert operator_steps[-1].operator_id == FACTOR_OPERATOR_ID
    return result


def remove_rule(records: list[dict], rule_id: str) -> list[dict]:
    changed = [copy.deepcopy(record) for record in records if record.get("rule_id") != rule_id]
    assert len(changed) + 1 == len(records)
    return changed


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    code_dir = repo_root / "research" / "translation-knowledge-graph" / "code"
    registry_dir = repo_root / "research" / "translation-knowledge-graph" / "registry"
    tkg001_path = registry_dir / "tkg-001-von-mangoldt-core.jsonl"
    tkg002_path = registry_dir / "tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl"
    rules_path = registry_dir / "executable" / "tkg-002-executable-rules-001.jsonl"

    # Gate 1: strict parse and exact local rule contract.
    registry_records = load_registry_jsonl([tkg001_path, tkg002_path])
    rule_records = load_rule_jsonl(rules_path)
    factor_rules = [record for record in rule_records if record.get("rule_id") == FACTOR_RULE_ID]
    assert len(factor_rules) == 1
    factor_rule = factor_rules[0]
    assert factor_rule["source_node_id"] == FACTOR_NODE_ID
    assert factor_rule["executable_rule"] == {
        "operator_id": FACTOR_OPERATOR_ID,
        "args": {},
        "result_symbol": "factorize",
    }

    # Gate 2: all earlier permanent gates remain green.
    prior_exit_code = run_script(code_dir, "verify_tkg_factorization_operator_001.py")

    executor = TKG002Executor([tkg001_path, tkg002_path], rules_path)

    # Gates 3-5: routed correctness, composite oracle, and round trip.
    branch_cases = [1, 2, 8, 72, 360, 2401, 9973]
    branch_results = {n: execute_factorize(executor, n).result for n in branch_cases}

    oracle_count = 0
    for n in range(1, 3011):
        execute_factorize(executor, n)
        oracle_count += 1

    # Gate 6: routing is exact; aliases are not silently authorized.
    for alias in ("factor", "factorization"):
        refusal = executor.execute(f"{alias}(360)")
        assert refusal.status == INSUFFICIENT_KNOWLEDGE
        assert refusal.result is None
        assert refusal.steps == ()

    # Gate 7: existing routed concepts still execute in the four-rule world.
    expected_existing = {
        "tau(360)": 24,
        "mu(30)": -1,
        "lambda(49)": {"kind": "LOG_PRIME", "prime": 7},
        "lambda(72)": {"kind": "ZERO"},
    }
    existing_results = {}
    for query, expected in expected_existing.items():
        result = executor.execute(query)
        assert result.status == EXECUTED_FROM_REGISTRY_RULE
        assert result.result == expected
        existing_results[query] = result.result

    with tempfile.TemporaryDirectory() as temporary_directory:
        temporary = Path(temporary_directory)

        # Gate 8A: deleting factorize rule refuses factorize; old concepts survive.
        no_factor_rules_path = temporary / "without-factorize-rule.jsonl"
        write_jsonl(no_factor_rules_path, remove_rule(rule_records, FACTOR_RULE_ID))
        no_factor_executor = TKG002Executor([tkg001_path, tkg002_path], no_factor_rules_path)
        factor_refusal = no_factor_executor.execute("factorize(360)")
        assert factor_refusal.status == INSUFFICIENT_KNOWLEDGE
        assert factor_refusal.steps == ()
        for query, expected in expected_existing.items():
            result = no_factor_executor.execute(query)
            assert result.status == EXECUTED_FROM_REGISTRY_RULE
            assert result.result == expected

        # Gate 8B: deleting each old rule leaves factorize alive.
        old_rule_ids = [
            "TKG002-EXEC-TAU-001",
            "TKG002-EXEC-MU-001",
            "TKG001-EXEC-LAMBDA-001",
        ]
        factor_survival = {}
        for old_rule_id in old_rule_ids:
            reduced_rules_path = temporary / f"without-{old_rule_id}.jsonl"
            write_jsonl(reduced_rules_path, remove_rule(rule_records, old_rule_id))
            reduced_executor = TKG002Executor([tkg001_path, tkg002_path], reduced_rules_path)
            factor_survival[old_rule_id] = execute_factorize(reduced_executor, 360).result

        # Gate 9A: deleting the source node blocks routing while other rules survive.
        without_factor_node = [
            copy.deepcopy(record)
            for record in registry_records
            if record.get("record_id") != FACTOR_NODE_ID
        ]
        assert len(without_factor_node) + 1 == len(registry_records)
        no_factor_node_path = temporary / "without-factor-node.jsonl"
        write_jsonl(no_factor_node_path, without_factor_node)
        no_factor_node_executor = TKG002Executor(no_factor_node_path, rules_path)
        node_refusal = no_factor_node_executor.execute("factorize(360)")
        assert node_refusal.status == INSUFFICIENT_KNOWLEDGE
        assert node_refusal.steps == ()
        for query, expected in expected_existing.items():
            result = no_factor_node_executor.execute(query)
            assert result.status == EXECUTED_FROM_REGISTRY_RULE
            assert result.result == expected

        # Gate 9B: deleting descriptive examples does not affect rule execution.
        without_examples = copy.deepcopy(registry_records)
        for record in without_examples:
            record.pop("examples", None)
        no_examples_path = temporary / "without-examples.jsonl"
        write_jsonl(no_examples_path, without_examples)
        no_examples_executor = TKG002Executor(no_examples_path, rules_path)
        no_examples_result = execute_factorize(no_examples_executor, 360)

        # Gate 10: local contract mutations are rejected by routing/execution.
        wrong_operator_rules = copy.deepcopy(rule_records)
        for record in wrong_operator_rules:
            if record.get("rule_id") == FACTOR_RULE_ID:
                record["executable_rule"]["operator_id"] = "OP-NOT-REGISTERED-001"
        wrong_operator_path = temporary / "wrong-operator.jsonl"
        write_jsonl(wrong_operator_path, wrong_operator_rules)
        wrong_operator_executor = TKG002Executor([tkg001_path, tkg002_path], wrong_operator_path)
        wrong_operator_refusal = wrong_operator_executor.execute("factorize(360)")
        assert wrong_operator_refusal.status == INSUFFICIENT_KNOWLEDGE
        assert wrong_operator_refusal.result is None

        wrong_symbol_rules = copy.deepcopy(rule_records)
        for record in wrong_symbol_rules:
            if record.get("rule_id") == FACTOR_RULE_ID:
                record["executable_rule"]["result_symbol"] = "not_factorize"
        wrong_symbol_path = temporary / "wrong-symbol.jsonl"
        write_jsonl(wrong_symbol_path, wrong_symbol_rules)
        wrong_symbol_executor = TKG002Executor([tkg001_path, tkg002_path], wrong_symbol_path)
        wrong_symbol_refusal = wrong_symbol_executor.execute("factorize(360)")
        assert wrong_symbol_refusal.status == INSUFFICIENT_KNOWLEDGE
        assert wrong_symbol_refusal.steps == ()

    report = {
        "phase": "PHASE-003-B2B",
        "scope": "FACTORIZATION_EXECUTABLE_RULE_AND_ROUTING",
        "strict_parse_gate": "PASS",
        "factorization_rule_contract": "PASS",
        "prior_non_regression_exit_code": prior_exit_code,
        "branch_results": branch_results,
        "sympy_oracle_count": oracle_count,
        "round_trip": "PASS",
        "exact_symbol_routing": "PASS",
        "existing_concepts_non_regression": existing_results,
        "bidirectional_rule_isolation": {
            "factorize_refused_after_own_rule_deletion": factor_refusal.status,
            "factorize_survives_old_rule_deletions": factor_survival,
        },
        "double_deletion": {
            "source_node_deletion_status": node_refusal.status,
            "examples_deletion_result": no_examples_result.result,
        },
        "contract_mutation_rejection": {
            "wrong_operator": wrong_operator_refusal.status,
            "wrong_symbol": wrong_symbol_refusal.status,
        },
        "provenance": "PASS",
        "verified_routed_concepts_candidate": ["tau", "mu", "lambda", "factorize"],
        "reasoning_engine": "NOT_AUTHORIZED",
        "math": "MATH-M0",
        "pnt": "NONE",
        "pnt_ap": "NONE",
        "goldbach": "NONE",
        "rh": "NONE",
        "grh": "NONE",
        "merge_to_main": "NOT_AUTHORIZED",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
