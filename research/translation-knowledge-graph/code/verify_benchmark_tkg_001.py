#!/usr/bin/env python3
"""Structural verifier for BENCHMARK-TKG-001.

Passing this verifier certifies only benchmark plumbing and governance invariants.
It does not certify mathematical theorems or analytic hypotheses.
"""
from __future__ import annotations

from run_benchmark_tkg_001 import DEFAULT_REGISTRY, load_cases, run


def main() -> None:
    cases = load_cases(DEFAULT_REGISTRY)
    assert len(cases) == 12
    classes = {case["class"] for case in cases}
    assert {"definitional", "computational", "multi_hop", "diagnostic", "adversarial", "coverage"}.issubset(classes)
    assert len({case["case_id"] for case in cases}) == len(cases)

    report = run(DEFAULT_REGISTRY)
    assert report["total_cases"] == 12
    assert report["math_status"] == "MATH-M0"
    assert report["scientific_claims_certified"] is False

    for result in report["results"]:
        assert result["claim_ceiling"]["MATH"] == "MATH-M0"
        assert result["claim_ceiling"]["PNT"] == "NONE"
        assert result["claim_ceiling"]["PNT_AP"] == "NONE"
        assert result["claim_ceiling"]["GOLDBACH"] == "NONE"
        assert result["claim_ceiling"]["RH"] == "NONE"
        assert result["claim_ceiling"]["GRH"] == "NONE"

    # This assertion checks routing behavior, not mathematical truth.
    assert report["passed"] is True, [item for item in report["results"] if not item["passed"]]
    print("BENCHMARK-TKG-001 structural verifier: PASS")
    print("Scientific theorem certification: NONE")
    print("MATH promotion: BLOCKED")


if __name__ == "__main__":
    main()
