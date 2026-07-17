#!/usr/bin/env python3
"""Verifier for BENCHMARK-TKG-001-R2.

A pass certifies only routing and bounded semantic expectations in the declared
cases. It does not certify mathematical theorems or authorize MATH promotion.
"""
from __future__ import annotations

import json

from run_benchmark_tkg_001_r2 import DEFAULT_REGISTRY, load_cases, run


def main() -> None:
    cases = load_cases(DEFAULT_REGISTRY)
    assert len(cases) == 24
    assert len({x["case_id"] for x in cases}) == 24
    assert {x["language"] for x in cases} == {"ar", "en"}
    assert {
        "definitional",
        "computational",
        "multi_hop",
        "diagnostic",
        "adversarial",
        "minimal_pair",
        "coverage",
    }.issubset({x["class"] for x in cases})
    assert all("must_include" in x or "must_include_ordered" in x for x in cases)

    expected_by_language: dict[str, dict[str, int]] = {}
    for case in cases:
        bucket = expected_by_language.setdefault(case["language"], {"passed": 0, "total": 0})
        bucket["total"] += 1
        bucket["passed"] += 1

    report = run(DEFAULT_REGISTRY)
    failed = [x for x in report["results"] if not x["passed"]]
    if failed:
        raise AssertionError(
            "BENCHMARK-TKG-001-R2 failing cases:\n"
            + json.dumps(failed, ensure_ascii=False, indent=2, sort_keys=True)
        )

    assert report["total_cases"] == 24
    assert report["passed"] is True
    assert report["passed_cases"] == 24
    assert report["math_status"] == "MATH-M0"
    assert report["scientific_claims_certified"] is False
    assert report["benchmark_sealed"] is False
    assert report["by_language"] == expected_by_language
    assert sum(x["total"] for x in report["by_language"].values()) == 24
    assert report["manifest"]["files"]

    for result in report["results"]:
        assert result["claim_ceiling"]["MATH"] == "MATH-M0"
        assert all(result["claim_ceiling"][k] == "NONE" for k in ("PNT", "PNT_AP", "GOLDBACH", "RH", "GRH"))

    print("BENCHMARK-TKG-001-R2 verifier: PASS")
    print("Routing plus bounded semantic cases: 24/24")
    print(f"Language distribution: {report['by_language']}")
    print("Scientific theorem certification: NONE")
    print("Benchmark sealed: NO")


if __name__ == "__main__":
    main()
