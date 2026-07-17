from __future__ import annotations

import inspect
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from tkg_factorization_consumer_contract_001 import (
    apply_factorization_consumer,
    validate_factorization_consumer_input,
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


def expect_value_error(action, description: str) -> None:
    try:
        action()
    except ValueError:
        return
    raise AssertionError(f"expected ValueError: {description}")


def expect_type_error(action, description: str) -> None:
    try:
        action()
    except TypeError:
        return
    raise AssertionError(f"expected TypeError: {description}")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    code_dir = repo_root / "research" / "translation-knowledge-graph" / "code"

    # Gate 1: the public application boundary has exactly two positional-only
    # parameters. The consumer itself receives only the factorization value.
    signature = inspect.signature(apply_factorization_consumer)
    parameters = list(signature.parameters.values())
    assert [parameter.name for parameter in parameters] == ["consumer", "factorization"]
    assert all(
        parameter.kind is inspect.Parameter.POSITIONAL_ONLY
        for parameter in parameters
    )

    # Gate 2: canonical PRIME_FACTORIZATION values are accepted and copied.
    canonical_cases = [
        {"kind": "PRIME_FACTORIZATION", "factors": []},
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [
                {"prime": 2, "exponent": 3},
                {"prime": 3, "exponent": 2},
                {"prime": 5, "exponent": 1},
            ],
        },
    ]
    canonical_copy_count = 0
    for value in canonical_cases:
        validated = validate_factorization_consumer_input(value)
        assert validated == value
        assert validated is not value
        assert validated["factors"] is not value["factors"]
        canonical_copy_count += 1

    # Gate 3: invalid intermediates are rejected before the consumer is called.
    invalid_inputs: list[Any] = [
        360,
        True,
        None,
        {},
        {"kind": "PRIME_FACTORIZATION"},
        {"kind": "PRIME_FACTORIZATION", "factors": "2^3*3^2*5"},
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 4, "exponent": 1}],
        },
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 2, "exponent": 0}],
        },
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [
                {"prime": 3, "exponent": 2},
                {"prime": 2, "exponent": 3},
            ],
        },
    ]
    consumer_calls: list[Any] = []

    def recording_consumer(factorization):
        consumer_calls.append(factorization)
        return 1

    for invalid in invalid_inputs:
        expect_value_error(
            lambda invalid=invalid: apply_factorization_consumer(
                recording_consumer,
                invalid,
            ),
            f"invalid factorization input {invalid!r}",
        )
    assert consumer_calls == []

    # Gate 4: the validated intermediate is genuinely delivered to the consumer.
    delivered: list[Any] = []
    source_value = canonical_cases[1]

    def spy_consumer(factorization):
        delivered.append(factorization)
        return len(factorization["factors"])

    spy_result = apply_factorization_consumer(spy_consumer, source_value)
    assert spy_result == 3
    assert delivered == [source_value]
    assert delivered[0] is not source_value
    assert delivered[0]["factors"] is not source_value["factors"]

    # Gate 5: every current ExecutionValue family is legal as a consumer result.
    legal_outputs = [
        24,
        -1,
        {"kind": "ZERO"},
        {"kind": "LOG_PRIME", "prime": 7},
        canonical_cases[1],
    ]
    observed_outputs = []
    for expected in legal_outputs:
        observed = apply_factorization_consumer(
            lambda factorization, expected=expected: expected,
            canonical_cases[0],
        )
        assert observed == expected
        observed_outputs.append(observed)

    # Gate 6: invalid outputs are rejected after the consumer runs.
    invalid_outputs: list[Any] = [
        True,
        1.5,
        "ZERO",
        {"kind": "ZERO", "extra": 1},
        {"kind": "LOG_PRIME", "prime": 9},
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 2, "exponent": 0}],
        },
    ]
    invalid_output_call_count = 0
    for invalid_output in invalid_outputs:
        def invalid_output_consumer(factorization, value=invalid_output):
            nonlocal invalid_output_call_count
            invalid_output_call_count += 1
            return value

        expect_value_error(
            lambda consumer=invalid_output_consumer: apply_factorization_consumer(
                consumer,
                canonical_cases[0],
            ),
            f"invalid consumer output {invalid_output!r}",
        )
    assert invalid_output_call_count == len(invalid_outputs)

    # Gate 7: no integer is supplied implicitly. A two-input callable cannot run.
    def consumer_requiring_integer(factorization, n):
        return n

    expect_type_error(
        lambda: apply_factorization_consumer(
            consumer_requiring_integer,
            canonical_cases[0],
        ),
        "consumer requiring hidden integer input",
    )
    expect_type_error(
        lambda: apply_factorization_consumer(17, canonical_cases[0]),
        "non-callable consumer",
    )

    # Gate 8: the validated copy protects the source intermediate from mutation.
    mutation_source = canonical_cases[1]
    mutation_snapshot = {
        "kind": mutation_source["kind"],
        "factors": [dict(factor) for factor in mutation_source["factors"]],
    }

    def mutating_consumer(factorization):
        factorization["factors"].clear()
        return 0

    assert apply_factorization_consumer(mutating_consumer, mutation_source) == 0
    assert mutation_source == mutation_snapshot

    # Gate 9: all PHASE-003 permanent verification remains green.
    prior_exit_code = run_script(code_dir, "verify_tkg_factorization_routing_001.py")

    report = {
        "phase": "PHASE-004-A",
        "scope": "FACTORIZATION_CONSUMER_INTERFACE_CONTRACT",
        "intermediate_kind": "PRIME_FACTORIZATION",
        "application_boundary_parameters": ["consumer", "factorization"],
        "integer_input_excluded_by_signature": "PASS",
        "canonical_copy_count": canonical_copy_count,
        "invalid_input_count": len(invalid_inputs),
        "invalid_input_rejected_before_consumer": "PASS",
        "intermediate_delivery": "PASS",
        "legal_output_family_count": len(legal_outputs),
        "invalid_output_count": len(invalid_outputs),
        "consumer_output_validation": "PASS",
        "source_intermediate_mutation_isolation": "PASS",
        "prior_non_regression_exit_code": prior_exit_code,
        "composition_classification": "TYPED_EXECUTION_COMPOSITION_ONLY",
        "reasoning_composition": "NONE",
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
