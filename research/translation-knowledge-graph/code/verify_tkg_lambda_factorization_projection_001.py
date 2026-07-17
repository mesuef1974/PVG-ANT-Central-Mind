from __future__ import annotations

import ast
import inspect
import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Callable

from sympy import factorint

import tkg_002_executable_rule_engine_001 as execution_engine
from tkg_002_executable_rule_engine_001 import (
    EXECUTED_FROM_REGISTRY_RULE,
    TKG002Executor,
)
from tkg_execution_value_contract_001 import ExecutionValue, validate_execution_value
from tkg_factorization_consumer_contract_001 import apply_factorization_consumer
from tkg_lambda_factorization_projection_001 import project_lambda_from_factorization


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


def canonical_factorization(n: int) -> dict[str, Any]:
    return {
        "kind": "PRIME_FACTORIZATION",
        "factors": [
            {"prime": int(prime), "exponent": int(exponent)}
            for prime, exponent in sorted(factorint(n).items())
        ],
    }


def expected_lambda_value(n: int) -> ExecutionValue:
    factors = factorint(n)
    if len(factors) != 1:
        return {"kind": "ZERO"}
    prime = int(next(iter(factors)))
    return {"kind": "LOG_PRIME", "prime": prime}


def expect_value_error(action: Callable[[], Any], description: str) -> None:
    try:
        action()
    except ValueError:
        return
    raise AssertionError(f"expected ValueError: {description}")


def load_mutated_projector(
    projector_path: Path,
    old: str,
    new: str,
) -> Callable[[dict[str, Any]], ExecutionValue]:
    source = projector_path.read_text(encoding="utf-8")
    assert source.count(old) == 1, f"mutation target must occur exactly once: {old!r}"
    mutated_source = source.replace(old, new, 1)
    assert mutated_source != source
    namespace: dict[str, Any] = {}
    exec(compile(mutated_source, str(projector_path), "exec"), namespace)
    return namespace["project_lambda_from_factorization"]


def is_rooted_in_name(node: ast.AST, name: str) -> bool:
    current = node
    while isinstance(current, ast.Subscript):
        current = current.value
    return isinstance(current, ast.Name) and current.id == name


def count_factor_component_field_reads(tree: ast.AST, field: str) -> int:
    """Count actual factor-component subscripts rooted in the local factors list.

    This distinguishes a read such as factors[0]["prime"] from an unrelated
    string occurrence such as the output mapping key {"prime": ...}.
    """

    count = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.Subscript):
            continue
        if not isinstance(node.slice, ast.Constant) or node.slice.value != field:
            continue
        if is_rooted_in_name(node.value, "factors"):
            count += 1
    return count


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    code_dir = repo_root / "research" / "translation-knowledge-graph" / "code"
    registry_dir = repo_root / "research" / "translation-knowledge-graph" / "registry"
    tkg001_path = registry_dir / "tkg-001-von-mangoldt-core.jsonl"
    tkg002_path = registry_dir / "tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl"
    rules_path = registry_dir / "executable" / "tkg-002-executable-rules-001.jsonl"

    # Gate 1: one positional-only factorization input; no separate integer channel.
    signature = inspect.signature(project_lambda_from_factorization)
    parameters = list(signature.parameters.values())
    assert [parameter.name for parameter in parameters] == ["factorization"]
    assert parameters[0].kind is inspect.Parameter.POSITIONAL_ONLY

    # Gate 2: no integer reconstruction/refactor dependency. Unlike tau, Lambda
    # must read one prime label when support cardinality is exactly one, while it
    # must remain independent of exponent magnitude.
    projector_path = code_dir / "tkg_lambda_factorization_projection_001.py"
    projector_source = projector_path.read_text(encoding="utf-8")
    projector_tree = ast.parse(projector_source)
    forbidden_names = {
        "factor_integer",
        "reconstruct_n",
        "evaluate_factorize",
        "enumerate_divisors",
        "evaluate_von_mangoldt",
    }
    forbidden_modules = {
        "tkg_002_executable_rule_engine_001",
        "tkg_composite_value_contract_001",
    }
    observed_forbidden_names: set[str] = set()
    observed_forbidden_modules: set[str] = set()
    for node in ast.walk(projector_tree):
        if isinstance(node, ast.Name) and node.id in forbidden_names:
            observed_forbidden_names.add(node.id)
        if isinstance(node, ast.Attribute) and node.attr in forbidden_names:
            observed_forbidden_names.add(node.attr)
        if isinstance(node, ast.ImportFrom) and node.module in forbidden_modules:
            observed_forbidden_modules.add(str(node.module))
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in forbidden_modules:
                    observed_forbidden_modules.add(alias.name)

    prime_field_reads = count_factor_component_field_reads(projector_tree, "prime")
    exponent_field_reads = count_factor_component_field_reads(projector_tree, "exponent")
    assert observed_forbidden_names == set()
    assert observed_forbidden_modules == set()
    assert prime_field_reads == 1
    assert exponent_field_reads == 0

    # Gate 2A: the audit itself distinguishes an output key from a component read.
    output_key_only_tree = ast.parse('value = {"kind": "LOG_PRIME", "prime": 2}')
    assert count_factor_component_field_reads(output_key_only_tree, "prime") == 0

    # Gate 2B: positive audit injection. Removing the actual prime read and adding
    # an exponent read must be detected by the structural measurement itself.
    prime_read_target = 'factors[0]["prime"]'
    exponent_read_replacement = 'factors[0]["exponent"]'
    assert projector_source.count(prime_read_target) == 1
    audit_mutant_source = projector_source.replace(
        prime_read_target,
        exponent_read_replacement,
        1,
    )
    assert audit_mutant_source != projector_source
    audit_mutant_tree = ast.parse(audit_mutant_source)
    assert count_factor_component_field_reads(audit_mutant_tree, "prime") == 0
    assert count_factor_component_field_reads(audit_mutant_tree, "exponent") == 1

    # Gate 3: exact branch behavior, including n=1, prime powers, and composite
    # support. Results are structured ExecutionValue objects, not numeric logs.
    branch_cases = [1, 2, 4, 8, 6, 12, 49, 72, 121, 9973]
    branch_results: dict[int, ExecutionValue] = {}
    for n in branch_cases:
        expected = expected_lambda_value(n)
        observed = apply_factorization_consumer(
            project_lambda_from_factorization,
            canonical_factorization(n),
        )
        assert observed == expected
        assert validate_execution_value(observed) == observed
        branch_results[n] = observed

    # Gate 4: malformed intermediates are rejected before the projector is called.
    invalid_inputs: list[Any] = [
        49,
        None,
        {"kind": "PRIME_FACTORIZATION"},
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 4, "exponent": 1}],
        },
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 7, "exponent": 0}],
        },
    ]
    projector_calls: list[dict[str, Any]] = []

    def recording_projector(factorization):
        projector_calls.append(factorization)
        return project_lambda_from_factorization(factorization)

    for invalid in invalid_inputs:
        expect_value_error(
            lambda invalid=invalid: apply_factorization_consumer(
                recording_projector,
                invalid,
            ),
            f"invalid factorization {invalid!r}",
        )
    assert projector_calls == []

    # Gate 5: independent structured oracle over a broad finite range. Both the
    # input and expected symbolic value are derived from SymPy factorint, not the
    # project factorizer or direct project Lambda operator.
    oracle_count = 0
    for n in range(1, 3011):
        observed = apply_factorization_consumer(
            project_lambda_from_factorization,
            canonical_factorization(n),
        )
        expected = expected_lambda_value(n)
        assert observed == expected
        oracle_count += 1

    # Gate 6: actual field consumption is falsifiable. Prime labels matter on
    # one-axis support; exponent magnitude does not; support cardinality does.
    prime_2_power_1 = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [{"prime": 2, "exponent": 1}],
    }
    prime_2_power_9 = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [{"prime": 2, "exponent": 9}],
    }
    prime_5_power_9 = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [{"prime": 5, "exponent": 9}],
    }
    two_axis_support = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [
            {"prime": 2, "exponent": 1},
            {"prime": 5, "exponent": 9},
        ],
    }
    consumption_results = {
        "prime_2_power_1": apply_factorization_consumer(
            project_lambda_from_factorization,
            prime_2_power_1,
        ),
        "prime_2_power_9": apply_factorization_consumer(
            project_lambda_from_factorization,
            prime_2_power_9,
        ),
        "prime_5_power_9": apply_factorization_consumer(
            project_lambda_from_factorization,
            prime_5_power_9,
        ),
        "two_axis_support": apply_factorization_consumer(
            project_lambda_from_factorization,
            two_axis_support,
        ),
        "empty_support": apply_factorization_consumer(
            project_lambda_from_factorization,
            canonical_factorization(1),
        ),
    }
    assert consumption_results == {
        "prime_2_power_1": {"kind": "LOG_PRIME", "prime": 2},
        "prime_2_power_9": {"kind": "LOG_PRIME", "prime": 2},
        "prime_5_power_9": {"kind": "LOG_PRIME", "prime": 5},
        "two_axis_support": {"kind": "ZERO"},
        "empty_support": {"kind": "ZERO"},
    }

    # Gate 7: consume a genuinely routed factorization result, then disable the
    # project integer factorizer. Projection must succeed from the existing
    # intermediate with no hidden re-factorization.
    executor = TKG002Executor([tkg001_path, tkg002_path], rules_path)
    routed_factorization = executor.execute("factorize(49)")
    assert routed_factorization.status == EXECUTED_FROM_REGISTRY_RULE
    assert routed_factorization.result == canonical_factorization(49)

    original_factor_integer = execution_engine.factor_integer

    def forbidden_refactor(_n: int):
        raise AssertionError("Lambda projection attempted hidden integer factorization")

    execution_engine.factor_integer = forbidden_refactor
    try:
        refactor_disabled_result = apply_factorization_consumer(
            project_lambda_from_factorization,
            routed_factorization.result,
        )
    finally:
        execution_engine.factor_integer = original_factor_integer
    assert refactor_disabled_result == {"kind": "LOG_PRIME", "prime": 7}

    # Gate 8: selected routed factorize -> apply -> project_lambda compositions
    # agree structurally with the existing routed direct Lambda result. Full
    # broad-range byte-exact equivalence remains reserved for PHASE-004-E.
    routed_bridge_cases = [1, 2, 4, 6, 8, 12, 49, 72, 121, 9973]
    routed_bridge_results: dict[int, ExecutionValue] = {}
    for n in routed_bridge_cases:
        factor_result = executor.execute(f"factorize({n})")
        direct_lambda_result = executor.execute(f"lambda({n})")
        assert factor_result.status == EXECUTED_FROM_REGISTRY_RULE
        assert direct_lambda_result.status == EXECUTED_FROM_REGISTRY_RULE
        composed = apply_factorization_consumer(
            project_lambda_from_factorization,
            factor_result.result,
        )
        assert composed == direct_lambda_result.result
        routed_bridge_results[n] = composed

    # Gate 9: verifier falsifiability with two applied semantic mutations.
    support_mutant = load_mutated_projector(
        projector_path,
        "if len(factors) != 1:",
        "if len(factors) == 1:",
    )
    support_mutant_result = apply_factorization_consumer(
        support_mutant,
        canonical_factorization(49),
    )
    assert support_mutant_result != expected_lambda_value(49)

    prime_field_mutant = load_mutated_projector(
        projector_path,
        prime_read_target,
        exponent_read_replacement,
    )
    prime_field_mutant_result = apply_factorization_consumer(
        prime_field_mutant,
        canonical_factorization(49),
    )
    assert prime_field_mutant_result != expected_lambda_value(49)

    # Gate 10: PHASE-004-C and all earlier permanent verification remain green.
    prior_exit_code = run_script(
        code_dir,
        "verify_tkg_tau_factorization_projection_001.py",
    )

    report = {
        "phase": "PHASE-004-D",
        "scope": "VON_MANGOLDT_PROJECTION_FROM_FACTORIZATION",
        "projector_parameter": "factorization_only",
        "integer_parameter": "ABSENT",
        "structured_output_family": ["ZERO", "LOG_PRIME"],
        "hidden_refactor_dependency_audit": "PASS",
        "prime_field_dependency": "REQUIRED_AND_VERIFIED",
        "exponent_magnitude_independence": "PASS",
        "field_read_audit": {
            "actual_prime_component_reads": prime_field_reads,
            "actual_exponent_component_reads": exponent_field_reads,
            "output_key_not_counted_as_read": "PASS",
            "prime_to_exponent_injection_detected": "PASS",
        },
        "branch_results": branch_results,
        "invalid_input_count": len(invalid_inputs),
        "invalid_input_rejected_before_projector": "PASS",
        "sympy_factorint_structured_oracle_count": oracle_count,
        "intermediate_consumption_mutations": consumption_results,
        "factor_integer_disabled_after_intermediate_creation": "PASS",
        "routed_local_bridge_results": routed_bridge_results,
        "verifier_falsifiability": {
            "support_condition_mutation": "DETECTED",
            "prime_field_to_exponent_mutation": "DETECTED",
        },
        "prior_non_regression_exit_code": prior_exit_code,
        "byte_exact_equivalence": "RESERVED_FOR_PHASE_004_E",
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
