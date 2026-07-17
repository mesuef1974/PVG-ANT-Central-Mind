from __future__ import annotations

import ast
import inspect
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

from sympy import factorint, mobius

import tkg_002_executable_rule_engine_001 as execution_engine
from tkg_002_executable_rule_engine_001 import (
    EXECUTED_FROM_REGISTRY_RULE,
    TKG002Executor,
)
from tkg_factorization_consumer_contract_001 import apply_factorization_consumer
from tkg_mu_factorization_projection_001 import project_mu_from_factorization


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


def expect_value_error(action, description: str) -> None:
    try:
        action()
    except ValueError:
        return
    raise AssertionError(f"expected ValueError: {description}")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    code_dir = repo_root / "research" / "translation-knowledge-graph" / "code"
    registry_dir = repo_root / "research" / "translation-knowledge-graph" / "registry"
    tkg001_path = registry_dir / "tkg-001-von-mangoldt-core.jsonl"
    tkg002_path = registry_dir / "tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl"
    rules_path = registry_dir / "executable" / "tkg-002-executable-rules-001.jsonl"

    # Gate 1: the projector receives the factorization only. It has no separate
    # integer parameter and cannot receive one through keyword injection.
    signature = inspect.signature(project_mu_from_factorization)
    parameters = list(signature.parameters.values())
    assert [parameter.name for parameter in parameters] == ["factorization"]
    assert parameters[0].kind is inspect.Parameter.POSITIONAL_ONLY

    # Gate 2: the implementation has no dependency on integer reconstruction or
    # factorization machinery. This is a durable local invariant, not a claim
    # that PRIME_FACTORIZATION is mathematically incapable of reconstructing n.
    projector_path = code_dir / "tkg_mu_factorization_projection_001.py"
    projector_tree = ast.parse(projector_path.read_text(encoding="utf-8"))
    forbidden_names = {
        "factor_integer",
        "reconstruct_n",
        "evaluate_factorize",
        "enumerate_divisors",
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
    assert observed_forbidden_names == set()
    assert observed_forbidden_modules == set()

    # Gate 3: exact branch behavior, including the factorization of 1.
    branch_cases = {
        1: 1,
        2: -1,
        6: 1,
        12: 0,
        30: -1,
        36: 0,
        210: 1,
    }
    branch_results: dict[int, int] = {}
    for n, expected in branch_cases.items():
        observed = apply_factorization_consumer(
            project_mu_from_factorization,
            canonical_factorization(n),
        )
        assert observed == expected
        assert isinstance(observed, int) and not isinstance(observed, bool)
        branch_results[n] = observed

    # Gate 4: malformed intermediates are rejected by apply before the projector
    # is invoked.
    invalid_inputs: list[Any] = [
        30,
        None,
        {"kind": "PRIME_FACTORIZATION"},
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 4, "exponent": 1}],
        },
        {
            "kind": "PRIME_FACTORIZATION",
            "factors": [{"prime": 2, "exponent": 0}],
        },
    ]
    projector_calls: list[dict[str, Any]] = []

    def recording_projector(factorization):
        projector_calls.append(factorization)
        return project_mu_from_factorization(factorization)

    for invalid in invalid_inputs:
        expect_value_error(
            lambda invalid=invalid: apply_factorization_consumer(
                recording_projector,
                invalid,
            ),
            f"invalid factorization {invalid!r}",
        )
    assert projector_calls == []

    # Gate 5: independent mathematical oracle over a broad finite range. The
    # input intermediate is built from SymPy, not from the project factorizer.
    oracle_count = 0
    for n in range(1, 3011):
        observed = apply_factorization_consumer(
            project_mu_from_factorization,
            canonical_factorization(n),
        )
        expected = int(mobius(n))
        assert observed == expected
        oracle_count += 1

    # Gate 6: actual consumption is falsifiable. Two legal changes to the
    # intermediate change the projected value exactly as the exponents and
    # support parity require.
    squarefree_three = canonical_factorization(30)
    square_mutation = {
        "kind": "PRIME_FACTORIZATION",
        "factors": [
            {"prime": 2, "exponent": 2},
            {"prime": 3, "exponent": 1},
            {"prime": 5, "exponent": 1},
        ],
    }
    parity_mutation = canonical_factorization(6)
    consumption_results = {
        "squarefree_three": apply_factorization_consumer(
            project_mu_from_factorization,
            squarefree_three,
        ),
        "square_mutation": apply_factorization_consumer(
            project_mu_from_factorization,
            square_mutation,
        ),
        "parity_mutation": apply_factorization_consumer(
            project_mu_from_factorization,
            parity_mutation,
        ),
    }
    assert consumption_results == {
        "squarefree_three": -1,
        "square_mutation": 0,
        "parity_mutation": 1,
    }

    # Gate 7: consume a genuinely routed factorization result, then disable the
    # project integer factorizer. Projection must still succeed from the already
    # produced intermediate, proving no hidden re-factorization dependency.
    executor = TKG002Executor([tkg001_path, tkg002_path], rules_path)
    routed_factorization = executor.execute("factorize(30)")
    assert routed_factorization.status == EXECUTED_FROM_REGISTRY_RULE
    assert routed_factorization.result == canonical_factorization(30)

    original_factor_integer = execution_engine.factor_integer

    def forbidden_refactor(_n: int):
        raise AssertionError("mu projection attempted hidden integer factorization")

    execution_engine.factor_integer = forbidden_refactor
    try:
        refactor_disabled_result = apply_factorization_consumer(
            project_mu_from_factorization,
            routed_factorization.result,
        )
    finally:
        execution_engine.factor_integer = original_factor_integer
    assert refactor_disabled_result == -1

    # Gate 8: selected routed factorize -> apply -> project_mu compositions agree
    # with the existing routed direct mu result. Full byte-exact equivalence is
    # reserved for PHASE-004-E; this gate verifies the first local bridge only.
    routed_bridge_cases = [1, 2, 6, 12, 30, 72, 210, 2310]
    routed_bridge_results: dict[int, int] = {}
    for n in routed_bridge_cases:
        factor_result = executor.execute(f"factorize({n})")
        direct_mu_result = executor.execute(f"mu({n})")
        assert factor_result.status == EXECUTED_FROM_REGISTRY_RULE
        assert direct_mu_result.status == EXECUTED_FROM_REGISTRY_RULE
        composed = apply_factorization_consumer(
            project_mu_from_factorization,
            factor_result.result,
        )
        assert composed == direct_mu_result.result
        routed_bridge_results[n] = composed

    # Gate 9: all PHASE-004-A and earlier permanent verification remains green.
    prior_exit_code = run_script(
        code_dir,
        "verify_tkg_factorization_consumer_contract_001.py",
    )

    report = {
        "phase": "PHASE-004-B",
        "scope": "MOBIUS_PROJECTION_FROM_FACTORIZATION",
        "projector_parameter": "factorization_only",
        "integer_parameter": "ABSENT",
        "hidden_refactor_dependency_audit": "PASS",
        "branch_results": branch_results,
        "invalid_input_count": len(invalid_inputs),
        "invalid_input_rejected_before_projector": "PASS",
        "sympy_mobius_oracle_count": oracle_count,
        "intermediate_consumption_mutations": consumption_results,
        "factor_integer_disabled_after_intermediate_creation": "PASS",
        "routed_local_bridge_results": routed_bridge_results,
        "prior_non_regression_exit_code": prior_exit_code,
        "tau_projection": "NOT_IN_THIS_PHASE",
        "lambda_projection": "NOT_IN_THIS_PHASE",
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
