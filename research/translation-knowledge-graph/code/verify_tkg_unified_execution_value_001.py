from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from tkg_002_executable_rule_engine_001 import (
    EXECUTED_FROM_REGISTRY_RULE,
    OPERATORS,
    ExecutionResult,
    OperatorExecution,
    TKG002Executor,
    load_rule_jsonl,
)
from tkg_execution_value_contract_001 import validate_execution_value


def expect_rejected(value: Any) -> None:
    try:
        validate_execution_value(value)
    except ValueError:
        return
    raise AssertionError(f"invalid execution value was accepted: {value!r}")


def expect_constructor_rejected(value: Any) -> None:
    try:
        OperatorExecution(value, ())
    except ValueError:
        pass
    else:
        raise AssertionError(f"OperatorExecution accepted invalid result: {value!r}")

    try:
        ExecutionResult("TEST", "q", None, None, value, ())
    except ValueError:
        return
    raise AssertionError(f"ExecutionResult accepted invalid result: {value!r}")


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


def main() -> None:
    # Positive cases cover every currently authorized execution-result family.
    positive_values = [
        24,
        -1,
        0,
        {"kind": "ZERO"},
        {"kind": "LOG_PRIME", "prime": 9973},
        {"kind": "PRIME_FACTORIZATION", "factors": []},
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [
                {"prime": 2, "exponent": 3},
                {"prime": 3, "exponent": 2},
            ],
        },
    ]
    for value in positive_values:
        assert validate_execution_value(value) == value
        assert OperatorExecution(value, ()).result == value
        assert ExecutionResult("TEST", "q", None, None, value, ()).result == value

    # Negative cases exercise type, exact object shape, symbolic payload,
    # composite payload, and the bool-is-int edge case.
    negative_values = [
        True,
        False,
        1.0,
        "ZERO",
        [],
        {},
        {"kind": "ZERO", "extra": 1},
        {"kind": "LOG_PRIME"},
        {"kind": "LOG_PRIME", "prime": 9},
        {"kind": "LOG_PRIME", "prime": True},
        {"kind": "UNKNOWN"},
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 4, "exponent": 1}],
        },
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [
                {"prime": 3, "exponent": 1},
                {"prime": 2, "exponent": 1},
            ],
        },
    ]
    for value in negative_values:
        expect_rejected(value)
        expect_constructor_rejected(value)

    repo_root = Path(__file__).resolve().parents[3]
    code_dir = repo_root / "research" / "translation-knowledge-graph" / "code"
    registry_dir = repo_root / "research" / "translation-knowledge-graph" / "registry"
    rules_path = registry_dir / "executable" / "tkg-002-executable-rules-001.jsonl"

    # One source of truth for all earlier gates, including PHASE-003-A.
    prior_exit_code = run_script(code_dir, "verify_tkg_composite_value_contract_001.py")

    executor = TKG002Executor(
        [
            registry_dir / "tkg-001-von-mangoldt-core.jsonl",
            registry_dir / "tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl",
        ],
        rules_path,
    )
    observed = {
        "tau": executor.execute("tau(360)"),
        "mu": executor.execute("mu(30)"),
        "lambda_prime_power": executor.execute("lambda(49)"),
        "lambda_zero": executor.execute("lambda(72)"),
    }
    expected_values = {
        "tau": 24,
        "mu": -1,
        "lambda_prime_power": {"kind": "LOG_PRIME", "prime": 7},
        "lambda_zero": {"kind": "ZERO"},
    }
    for name, result in observed.items():
        assert result.status == EXECUTED_FROM_REGISTRY_RULE
        assert result.result == expected_values[name]
        assert validate_execution_value(result.result) == result.result

    # B1 must not silently start B2/B3.
    assert "OP-FACTORIZE-INTEGER-001" not in OPERATORS
    rules = load_rule_jsonl(rules_path)
    assert not any(
        str((rule.get("executable_rule") or {}).get("result_symbol", "")).lower()
        in {"factor", "factorize", "factorization"}
        for rule in rules
    )

    report = {
        "phase": "PHASE-003-B1",
        "scope": "UNIFIED_EXECUTION_VALUE_CONTRACT",
        "positive_case_count": len(positive_values),
        "negative_case_count": len(negative_values),
        "engine_boundary_validation": "PASS",
        "prior_non_regression_exit_code": prior_exit_code,
        "pointwise_replay": {name: result.result for name, result in observed.items()},
        "result_any_debt": "CLOSED_FOR_OPERATOR_AND_EXECUTION_RESULTS",
        "provenance_step_value_any": "INTENTIONALLY_OPEN",
        "factorization_operator_added": False,
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
