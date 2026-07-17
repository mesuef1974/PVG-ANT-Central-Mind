from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Callable

from sympy import factorint

import tkg_002_executable_rule_engine_001 as engine
from tkg_composite_value_contract_001 import reconstruct_n
from tkg_execution_value_contract_001 import validate_execution_value


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


def expected_value(n: int) -> dict:
    return {
        "kind": "PRIME_FACTORIZATION",
        "factors": [
            {"prime": int(prime), "exponent": int(exponent)}
            for prime, exponent in sorted(factorint(n).items())
        ],
    }


def assert_operator_case(n: int) -> dict:
    execution = engine.evaluate_factorize({}, n)
    expected = expected_value(n)
    assert execution.result == expected
    assert validate_execution_value(execution.result) == execution.result
    assert reconstruct_n(execution.result) == n
    assert len(execution.steps) == 2
    assert execution.steps[0].operator_id == "OP-FACTOR-INTEGER-001"
    assert execution.steps[1].operator_id == "OP-FACTORIZE-INTEGER-001"
    assert all(step.source_node_id is None for step in execution.steps)
    return execution.result


def prove_mutation_applied_and_detected(
    name: str,
    mutant: Callable[[int], dict[int, int]],
    n: int,
) -> str:
    original = engine.factor_integer
    assert mutant is not original, f"mutation {name} did not replace factor_integer"
    engine.factor_integer = mutant
    assert engine.factor_integer is mutant, f"mutation {name} was not applied"
    try:
        try:
            assert_operator_case(n)
        except (AssertionError, ValueError):
            return "DETECTED"
        raise AssertionError(f"mutation {name} escaped detection")
    finally:
        engine.factor_integer = original
        assert engine.factor_integer is original


def main() -> None:
    assert "OP-FACTORIZE-INTEGER-001" in engine.OPERATORS
    assert engine.OPERATORS["OP-FACTORIZE-INTEGER-001"] is engine.evaluate_factorize

    explicit_cases = {
        1: {"kind": "PRIME_FACTORIZATION", "factors": []},
        2: {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 2, "exponent": 1}],
        },
        72: {
            "kind": "PRIME_FACTORIZATION",
            "factors": [
                {"prime": 2, "exponent": 3},
                {"prime": 3, "exponent": 2},
            ],
        },
        2401: {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 7, "exponent": 4}],
        },
        9973: {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 9973, "exponent": 1}],
        },
    }
    observed_explicit = {}
    for n, expected in explicit_cases.items():
        observed = assert_operator_case(n)
        assert observed == expected
        observed_explicit[n] = observed

    round_trip_count = 0
    for n in range(1, 3011):
        assert_operator_case(n)
        round_trip_count += 1

    # Unsupported arguments are rejected locally by this operator.
    try:
        engine.evaluate_factorize({"unexpected": True}, 72)
    except ValueError:
        unsupported_args = "REJECTED"
    else:
        raise AssertionError("factorization operator accepted unsupported arguments")

    # Canonical ordering is robust to insertion order in the mechanical map.
    original = engine.factor_integer
    reverse_insertion = lambda n: {3: 2, 2: 3} if n == 72 else original(n)
    engine.factor_integer = reverse_insertion
    try:
        assert engine.factor_integer is reverse_insertion
        reverse_order_result = assert_operator_case(72)
    finally:
        engine.factor_integer = original
    assert reverse_order_result == explicit_cases[72]

    mutation_results = {
        "omit_factor": prove_mutation_applied_and_detected(
            "omit_factor", lambda n: {2: 3} if n == 72 else original(n), 72
        ),
        "wrong_exponent": prove_mutation_applied_and_detected(
            "wrong_exponent", lambda n: {2: 2, 3: 2} if n == 72 else original(n), 72
        ),
        "composite_prime": prove_mutation_applied_and_detected(
            "composite_prime", lambda n: {4: 1} if n == 4 else original(n), 4
        ),
        "spurious_factor": prove_mutation_applied_and_detected(
            "spurious_factor", lambda n: {2: 3, 3: 2, 5: 1} if n == 72 else original(n), 72
        ),
    }

    repo_root = Path(__file__).resolve().parents[3]
    code_dir = repo_root / "research" / "translation-knowledge-graph" / "code"
    prior_exit_code = run_script(code_dir, "verify_tkg_unified_execution_value_001.py")

    report = {
        "phase": "PHASE-003-B2A",
        "scope": "FACTORIZATION_OPERATOR_ONLY",
        "operator_id": "OP-FACTORIZE-INTEGER-001",
        "explicit_cases": observed_explicit,
        "sympy_round_trip_count": round_trip_count,
        "reconstruct_n_invariant": "PASS",
        "unsupported_args": unsupported_args,
        "reverse_insertion_canonicalization": "PASS",
        "mutation_application_proved": True,
        "mutation_results": mutation_results,
        "prior_non_regression_exit_code": prior_exit_code,
        "executable_rule_added": False,
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
