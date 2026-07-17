from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from copy import deepcopy
from pathlib import Path
from typing import Any, Callable

import tkg_002_executable_rule_engine_001 as execution_engine
from tkg_002_executable_rule_engine_001 import (
    EXECUTED_FROM_REGISTRY_RULE,
    TKG002Executor,
)
from tkg_execution_value_contract_001 import ExecutionValue, validate_execution_value
from tkg_factorization_consumer_contract_001 import apply_factorization_consumer
from tkg_lambda_factorization_projection_001 import project_lambda_from_factorization
from tkg_mu_factorization_projection_001 import project_mu_from_factorization
from tkg_tau_factorization_projection_001 import project_tau_from_factorization


Projector = Callable[[dict[str, Any]], ExecutionValue]


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


def execution_value_bytes(value: ExecutionValue) -> bytes:
    """Encode the returned ExecutionValue as exact compact UTF-8 JSON bytes.

    The comparison intentionally preserves mapping insertion order. Both the
    direct operator boundary and apply_factorization_consumer already validate
    their outputs, so equality here is equality of the actual returned wire
    representation rather than equality after sorting or normalizing keys.
    """

    assert validate_execution_value(value) == value
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=False,
    ).encode("utf-8")


def expect_value_error(action: Callable[[], Any], description: str) -> None:
    try:
        action()
    except ValueError:
        return
    raise AssertionError(f"expected ValueError: {description}")


def load_mutated_projector(
    projector_path: Path,
    function_name: str,
    old: str,
    new: str,
) -> Projector:
    source = projector_path.read_text(encoding="utf-8")
    assert source.count(old) == 1, f"mutation target must occur exactly once: {old!r}"
    mutated_source = source.replace(old, new, 1)
    assert mutated_source != source
    namespace: dict[str, Any] = {}
    exec(compile(mutated_source, str(projector_path), "exec"), namespace)
    return namespace[function_name]


def assert_byte_mismatch(
    executor: TKG002Executor,
    query_name: str,
    mutant: Projector,
    n: int,
) -> dict[str, str]:
    factor_result = executor.execute(f"factorize({n})")
    direct_result = executor.execute(f"{query_name}({n})")
    assert factor_result.status == EXECUTED_FROM_REGISTRY_RULE
    assert direct_result.status == EXECUTED_FROM_REGISTRY_RULE
    mutant_result = apply_factorization_consumer(mutant, factor_result.result)
    direct_bytes = execution_value_bytes(direct_result.result)
    mutant_bytes = execution_value_bytes(mutant_result)
    assert mutant_bytes != direct_bytes
    return {
        "direct": direct_bytes.decode("utf-8"),
        "mutant": mutant_bytes.decode("utf-8"),
    }


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    code_dir = repo_root / "research" / "translation-knowledge-graph" / "code"
    registry_dir = repo_root / "research" / "translation-knowledge-graph" / "registry"
    tkg001_path = registry_dir / "tkg-001-von-mangoldt-core.jsonl"
    tkg002_path = registry_dir / "tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl"
    rules_path = registry_dir / "executable" / "tkg-002-executable-rules-001.jsonl"

    executor = TKG002Executor([tkg001_path, tkg002_path], rules_path)
    projectors: dict[str, Projector] = {
        "mu": project_mu_from_factorization,
        "tau": project_tau_from_factorization,
        "lambda": project_lambda_from_factorization,
    }

    # Gate 1: one routed PRIME_FACTORIZATION intermediate fans out through the
    # common apply boundary to all three projectors. Direct and composed outputs
    # must be structurally equal and byte-identical over a broad deterministic
    # corpus. The exact byte representation is compact UTF-8 JSON without key
    # sorting, so structured Lambda output is tested as returned, not normalized.
    equivalence_inputs = list(range(1, 4097)) + [4099, 8192, 9973, 10000, 30030]
    comparison_count = 0
    per_projector_counts = {name: 0 for name in projectors}
    transcript = hashlib.sha256()

    for n in equivalence_inputs:
        factor_result = executor.execute(f"factorize({n})")
        assert factor_result.status == EXECUTED_FROM_REGISTRY_RULE
        shared_intermediate_before = deepcopy(factor_result.result)

        for query_name, projector in projectors.items():
            direct_result = executor.execute(f"{query_name}({n})")
            assert direct_result.status == EXECUTED_FROM_REGISTRY_RULE
            composed_result = apply_factorization_consumer(
                projector,
                factor_result.result,
            )

            assert composed_result == direct_result.result
            direct_bytes = execution_value_bytes(direct_result.result)
            composed_bytes = execution_value_bytes(composed_result)
            assert composed_bytes == direct_bytes

            transcript.update(query_name.encode("ascii"))
            transcript.update(b":")
            transcript.update(str(n).encode("ascii"))
            transcript.update(b":")
            transcript.update(direct_bytes)
            transcript.update(b"=")
            transcript.update(composed_bytes)
            transcript.update(b"\n")

            comparison_count += 1
            per_projector_counts[query_name] += 1

        # The same source intermediate must remain reusable after the three-way
        # fan-out; apply owns deep isolation and may not mutate the shared value.
        assert factor_result.result == shared_intermediate_before

    assert comparison_count == len(equivalence_inputs) * len(projectors)
    assert len(set(per_projector_counts.values())) == 1

    # Gate 2: removing or structurally corrupting the shared intermediate must
    # stop every composed path at the apply boundary. No projector is authorized
    # to fabricate or recover a missing factorization input.
    invalid_intermediates: dict[str, Any] = {
        "removed": None,
        "missing_factors": {"kind": "PRIME_FACTORIZATION"},
        "composite_prime_label": {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 4, "exponent": 1}],
        },
        "zero_exponent": {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 2, "exponent": 0}],
        },
    }
    rejection_count = 0
    for projector_name, projector in projectors.items():
        for corruption_name, invalid_intermediate in invalid_intermediates.items():
            expect_value_error(
                lambda projector=projector, value=invalid_intermediate: (
                    apply_factorization_consumer(projector, value)
                ),
                f"{projector_name} accepted {corruption_name}",
            )
            rejection_count += 1
    assert rejection_count == len(projectors) * len(invalid_intermediates)

    # Gate 3: legal but intentionally different intermediates must drive different
    # outputs according to each projector's declared fields. This proves that the
    # composed result tracks the supplied shared value rather than a hidden n.
    mu_base = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [
            {"prime": 2, "exponent": 1},
            {"prime": 3, "exponent": 1},
            {"prime": 5, "exponent": 1},
        ],
    }
    mu_altered = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [
            {"prime": 2, "exponent": 2},
            {"prime": 3, "exponent": 1},
            {"prime": 5, "exponent": 1},
        ],
    }
    tau_base = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [
            {"prime": 2, "exponent": 3},
            {"prime": 3, "exponent": 2},
        ],
    }
    tau_altered = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [
            {"prime": 2, "exponent": 4},
            {"prime": 3, "exponent": 2},
        ],
    }
    lambda_base = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [{"prime": 7, "exponent": 2}],
    }
    lambda_altered = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [{"prime": 11, "exponent": 9}],
    }
    lambda_multiaxis = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [
            {"prime": 7, "exponent": 2},
            {"prime": 11, "exponent": 9},
        ],
    }

    altered_intermediate_results = {
        "mu_base": apply_factorization_consumer(projectors["mu"], mu_base),
        "mu_altered": apply_factorization_consumer(projectors["mu"], mu_altered),
        "tau_base": apply_factorization_consumer(projectors["tau"], tau_base),
        "tau_altered": apply_factorization_consumer(projectors["tau"], tau_altered),
        "lambda_base": apply_factorization_consumer(projectors["lambda"], lambda_base),
        "lambda_altered": apply_factorization_consumer(
            projectors["lambda"],
            lambda_altered,
        ),
        "lambda_multiaxis": apply_factorization_consumer(
            projectors["lambda"],
            lambda_multiaxis,
        ),
    }
    assert altered_intermediate_results == {
        "mu_base": -1,
        "mu_altered": 0,
        "tau_base": 12,
        "tau_altered": 15,
        "lambda_base": {"kind": "LOG_PRIME", "prime": 7},
        "lambda_altered": {"kind": "LOG_PRIME", "prime": 11},
        "lambda_multiaxis": {"kind": "ZERO"},
    }

    # Gate 4: produce routed intermediates and direct reference outputs first,
    # then disable the project integer factorizer completely. All composed paths
    # must still reproduce their saved direct bytes from the existing values.
    no_refactor_cases = {"mu": 360, "tau": 360, "lambda": 49}
    saved_intermediates: dict[str, ExecutionValue] = {}
    saved_direct_bytes: dict[str, bytes] = {}
    for query_name, n in no_refactor_cases.items():
        factor_result = executor.execute(f"factorize({n})")
        direct_result = executor.execute(f"{query_name}({n})")
        assert factor_result.status == EXECUTED_FROM_REGISTRY_RULE
        assert direct_result.status == EXECUTED_FROM_REGISTRY_RULE
        saved_intermediates[query_name] = factor_result.result
        saved_direct_bytes[query_name] = execution_value_bytes(direct_result.result)

    original_factor_integer = execution_engine.factor_integer

    def forbidden_refactor(_n: int):
        raise AssertionError("composed execution attempted hidden integer factorization")

    execution_engine.factor_integer = forbidden_refactor
    try:
        no_refactor_results: dict[str, str] = {}
        for query_name, projector in projectors.items():
            composed_result = apply_factorization_consumer(
                projector,
                saved_intermediates[query_name],
            )
            composed_bytes = execution_value_bytes(composed_result)
            assert composed_bytes == saved_direct_bytes[query_name]
            no_refactor_results[query_name] = composed_bytes.decode("utf-8")
    finally:
        execution_engine.factor_integer = original_factor_integer

    # Gate 5: the equivalence certificate must be falsifiable. Inject one applied,
    # type-valid semantic defect into each projector and prove that byte equality
    # against the direct route breaks on a targeted witness.
    mu_mutant = load_mutated_projector(
        code_dir / "tkg_mu_factorization_projection_001.py",
        "project_mu_from_factorization",
        'if any(factor["exponent"] > 1 for factor in factors):',
        'if any(factor["exponent"] > 2 for factor in factors):',
    )
    tau_mutant = load_mutated_projector(
        code_dir / "tkg_tau_factorization_projection_001.py",
        "project_tau_from_factorization",
        'factor["exponent"] + 1',
        'factor["exponent"] + 2',
    )
    lambda_mutant = load_mutated_projector(
        code_dir / "tkg_lambda_factorization_projection_001.py",
        "project_lambda_from_factorization",
        'factors[0]["prime"]',
        'factors[0]["exponent"]',
    )
    mutation_witnesses = {
        "mu_exponent_threshold": assert_byte_mismatch(executor, "mu", mu_mutant, 4),
        "tau_exponent_shift": assert_byte_mismatch(executor, "tau", tau_mutant, 12),
        "lambda_prime_to_exponent": assert_byte_mismatch(
            executor,
            "lambda",
            lambda_mutant,
            49,
        ),
    }

    # Gate 6: PHASE-004-D and the recursively chained A/B/C verification remain
    # green. E adds no projector, operator, registry rule, or routing behavior.
    prior_exit_code = run_script(
        code_dir,
        "verify_tkg_lambda_factorization_projection_001.py",
    )

    report = {
        "phase": "PHASE-004-E",
        "scope": "DIRECT_VS_COMPOSED_BYTE_EXACT_EQUIVALENCE",
        "byte_encoding": "COMPACT_UTF8_JSON_PRESERVE_INSERTION_ORDER",
        "equivalence_input_count": len(equivalence_inputs),
        "comparison_count": comparison_count,
        "per_projector_counts": per_projector_counts,
        "equivalence_transcript_sha256": transcript.hexdigest(),
        "shared_intermediate_three_way_fanout": "PASS",
        "shared_intermediate_source_isolation": "PASS",
        "invalid_or_removed_intermediate_rejection_count": rejection_count,
        "altered_valid_intermediate_consumption": altered_intermediate_results,
        "factor_integer_disabled_after_intermediate_creation": "PASS",
        "no_refactor_results": no_refactor_results,
        "verifier_falsifiability": mutation_witnesses,
        "prior_non_regression_exit_code": prior_exit_code,
        "new_projection": "NONE",
        "new_operator": "NONE",
        "new_registry_rule": "NONE",
        "new_routing": "NONE",
        "composition_classification": "VERIFIED_TYPED_EXECUTION_COMPOSITION_CANDIDATE",
        "reasoning_composition": "NONE",
        "post_pinned_replay": "CLOSE_PHASE_004_PROJECTION_LINE",
        "fifth_projection": "PROHIBITED_BY_SCOPE",
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
