#!/usr/bin/env python3
"""Deterministic verifier for TKG-002."""
from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "query_tkg_002.py"
SPEC = importlib.util.spec_from_file_location("query_tkg_002", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("cannot load query_tkg_002")
TKG = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TKG)

REQUIRED_FIELDS = {
    "record_id",
    "record_type",
    "assimilation_level",
    "math_contribution_level",
    "operational_maturity",
    "certificate_strength",
    "claim_ceiling",
}


def verify_registry() -> dict:
    records = TKG.load_records()
    ids = [record["record_id"] for record in records]
    assert len(records) >= 16
    assert len(ids) == len(set(ids))
    for record in records:
        missing = REQUIRED_FIELDS - record.keys()
        assert not missing, (record.get("record_id"), sorted(missing))
        assert record["math_contribution_level"] == "MATH-M0"
        assert "RH" not in record["claim_ceiling"] or "no" in record["claim_ceiling"].lower()
    expected = {
        "TKG002-NODE-DIRICHLET-CONVOLUTION",
        "TKG002-NODE-MOBIUS-INVERSION",
        "TKG002-NODE-DIVISOR-BOX",
        "TKG002-EDGE-MU-LOG-TO-LAMBDA",
        "TKG002-REJECT-CONVOLUTION-TO-ASYMPTOTIC",
    }
    assert expected.issubset(ids)
    return {"records": len(records), "unique_ids": len(ids)}


def verify_known_identities(limit: int = 256) -> dict:
    max_mu_log_error = 0.0
    for n in range(1, limit + 1):
        assert TKG.dirichlet_convolution(TKG.epsilon, TKG.one, n) == TKG.one(n)
        assert TKG.dirichlet_convolution(TKG.one, TKG.one, n) == TKG.tau(n)
        assert TKG.dirichlet_convolution(TKG.one, TKG.identity, n) == TKG.sigma(n)
        assert TKG.dirichlet_convolution(TKG.mobius, TKG.one, n) == TKG.epsilon(n)
        error = abs(TKG.dirichlet_convolution(TKG.mobius, TKG.log_function, n) - TKG.von_mangoldt(n))
        max_mu_log_error = max(max_mu_log_error, error)
        assert error < 1e-10
    return {"checked_n": limit, "max_mu_log_error": max_mu_log_error}


def verify_mobius_inversion(limit: int = 128) -> dict:
    test_functions = {
        "id": TKG.identity,
        "tau": TKG.tau,
        "square": lambda n: n * n,
        "support_parity": lambda n: -1 if len(TKG.factorization(n)) % 2 else 1,
    }
    checks = 0
    for name, f in test_functions.items():
        F = lambda n, f=f: TKG.divisor_sum_transform(f, n)
        for n in range(1, limit + 1):
            recovered = TKG.mobius_transform(F, n)
            assert math.isclose(recovered, f(n), abs_tol=1e-10), (name, n, recovered, f(n))
            checks += 1
    return {"functions": list(test_functions), "checks": checks}


def verify_divisor_box() -> dict:
    expected = {
        1: (1, 1, 1),
        12: (6, 6, 28),
        24: (8, 8, 60),
        30: (8, 8, 72),
    }
    for n, (box_size, tau_value, sigma_value) in expected.items():
        box = TKG.divisor_box(n)
        assert len(box) == box_size
        assert TKG.tau(n) == tau_value
        assert TKG.sigma(n) == sigma_value
        for point in box:
            assert point["d"] * point["n_over_d"] == n
    assert sorted(TKG.factorization(12).values()) == sorted(TKG.factorization(18).values())
    assert TKG.sigma(12) == 28
    assert TKG.sigma(18) == 39
    return {"examples": sorted(expected), "anonymized_shape_counterexample": "sigma(12)=28 != sigma(18)=39"}


def verify_reasoning_response() -> dict:
    result = TKG.explain_number(12)
    assert result["divisor_box_cardinality"] == 6
    assert result["tau"] == 6
    assert result["sigma"] == 28
    assert result["mu_convolved_one"] == 0
    assert abs(result["mu_convolved_log"]) < 1e-12
    assert all(result["exact_checks"].values())
    assert result["asymptotic_inference_authorized"] is False
    return {"n": 12, "all_exact_checks": True, "asymptotic_gate": "closed"}


def main() -> None:
    report = {
        "unit": "TKG-002",
        "status": "PASS",
        "registry": verify_registry(),
        "known_identities": verify_known_identities(),
        "mobius_inversion": verify_mobius_inversion(),
        "divisor_box": verify_divisor_box(),
        "reasoning_response": verify_reasoning_response(),
        "scientific_ceiling": {
            "math_contribution": "MATH-M0",
            "pnt_progress": "NONE",
            "rh_progress": "NONE",
            "grh_progress": "NONE",
            "trained_network": False,
        },
    }
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
