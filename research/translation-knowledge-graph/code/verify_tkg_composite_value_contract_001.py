from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable

from sympy import factorint

from tkg_composite_value_contract_001 import (
    PRIME_FACTORIZATION_KIND,
    reconstruct_n,
    validate_prime_factorization_value,
)


def expect_rejected(value: Any) -> None:
    try:
        validate_prime_factorization_value(value)
    except ValueError:
        return
    raise AssertionError(f"invalid value was accepted: {value!r}")


def factorization_value(n: int) -> dict[str, Any]:
    if n < 1:
        raise ValueError("n must be positive")
    return {
        "kind": PRIME_FACTORIZATION_KIND,
        "factors": [
            {"prime": int(prime), "exponent": int(exponent)}
            for prime, exponent in sorted(factorint(n).items())
        ],
    }


def prove_mutation_applied_and_rejected(
    name: str,
    valid_value: dict[str, Any],
    mutate: Callable[[dict[str, Any]], None],
) -> str:
    mutated = copy.deepcopy(valid_value)
    before = json.dumps(mutated, sort_keys=True)
    mutate(mutated)
    after = json.dumps(mutated, sort_keys=True)
    assert before != after, f"mutation {name} was a no-op"
    expect_rejected(mutated)
    return "REJECTED"


def run_prior_non_regression(repo_root: Path) -> dict[str, int]:
    code_dir = repo_root / "research" / "translation-knowledge-graph" / "code"
    scripts = [
        "verify_tkg_002_executable_rule_double_deletion_001.py",
        "verify_tkg_002_mu_two_concept_execution_001.py",
        "verify_tkg_multi_registry_loading_001.py",
        "verify_tkg_001_lambda_structured_execution_001.py",
        "verify_tkg_three_concept_non_regression_001.py",
    ]
    exit_codes: dict[str, int] = {}
    for script in scripts:
        completed = subprocess.run(
            [sys.executable, str(code_dir / script)],
            cwd=repo_root,
            text=True,
            capture_output=True,
            check=False,
        )
        exit_codes[script] = completed.returncode
        if completed.returncode != 0:
            raise AssertionError(
                f"prior non-regression failed in {script}:\n"
                f"STDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
            )
    return exit_codes


def main() -> None:
    checks: list[str] = []

    # Positive contract cases.
    one = {"kind": PRIME_FACTORIZATION_KIND, "factors": []}
    assert validate_prime_factorization_value(one) == one
    assert reconstruct_n(one) == 1
    checks.append("positive_empty_factorization_of_one")

    seventy_two = {
        "kind": PRIME_FACTORIZATION_KIND,
        "factors": [
            {"prime": 2, "exponent": 3},
            {"prime": 3, "exponent": 2},
        ],
    }
    assert validate_prime_factorization_value(seventy_two) == seventy_two
    assert reconstruct_n(seventy_two) == 72
    checks.append("positive_composite_factorization")

    prime_power = {
        "kind": PRIME_FACTORIZATION_KIND,
        "factors": [{"prime": 7, "exponent": 4}],
    }
    assert reconstruct_n(prime_power) == 2401
    checks.append("positive_prime_power")

    # Negative cases: exact object shape, kind, factor list, component shape,
    # primality, deterministic order/uniqueness, and positive integer exponent.
    negative_cases = [
        72,
        {"kind": PRIME_FACTORIZATION_KIND, "factors": [], "extra": True},
        {"kind": "OTHER", "factors": []},
        {"kind": PRIME_FACTORIZATION_KIND, "factors": {}},
        {"kind": PRIME_FACTORIZATION_KIND, "factors": [2]},
        {
            "kind": PRIME_FACTORIZATION_KIND,
            "factors": [{"prime": 4, "exponent": 1}],
        },
        {
            "kind": PRIME_FACTORIZATION_KIND,
            "factors": [
                {"prime": 3, "exponent": 1},
                {"prime": 2, "exponent": 1},
            ],
        },
        {
            "kind": PRIME_FACTORIZATION_KIND,
            "factors": [
                {"prime": 2, "exponent": 1},
                {"prime": 2, "exponent": 3},
            ],
        },
        {
            "kind": PRIME_FACTORIZATION_KIND,
            "factors": [{"prime": 2, "exponent": 0}],
        },
    ]
    for index, value in enumerate(negative_cases, 1):
        expect_rejected(value)
        checks.append(f"negative_{index}")

    # 3 positive + 9 negative = 12 explicit invariant checks.
    assert len(checks) == 12

    # Check 13: independent oracle round trip over a broad finite range.
    round_trip_count = 0
    for n in range(1, 3011):
        value = factorization_value(n)
        assert validate_prime_factorization_value(value) == value
        assert reconstruct_n(value) == n
        round_trip_count += 1
    checks.append("sympy_round_trip_1_to_3010")
    assert len(checks) == 13

    mutation_results = {
        "ordering": prove_mutation_applied_and_rejected(
            "ordering",
            seventy_two,
            lambda value: value["factors"].reverse(),
        ),
        "exponent": prove_mutation_applied_and_rejected(
            "exponent",
            seventy_two,
            lambda value: value["factors"][0].__setitem__("exponent", 0),
        ),
        "primality": prove_mutation_applied_and_rejected(
            "primality",
            prime_power,
            lambda value: value["factors"][0].__setitem__("prime", 9),
        ),
    }

    repo_root = Path(__file__).resolve().parents[3]
    prior_non_regression = run_prior_non_regression(repo_root)

    report = {
        "phase": "PHASE-003-A",
        "scope": "COMPOSITE_EXECUTION_VALUE_CONTRACT_ONLY",
        "checks": checks,
        "check_count": len(checks),
        "sympy_round_trip_count": round_trip_count,
        "mutation_application_proved": True,
        "mutation_results": mutation_results,
        "prior_non_regression_exit_codes": prior_non_regression,
        "operator_added": False,
        "executable_rule_added": False,
        "execution_value_union_closed": False,
        "remaining_debt": "INTEGER, ZERO, and LOG_PRIME still lack one unified validator",
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
