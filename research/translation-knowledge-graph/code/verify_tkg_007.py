#!/usr/bin/env python3
"""Finite verifier for TKG-007."""
from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODULE_PATH = HERE / "query_tkg_007.py"
REGISTRY = HERE.parent / "registry/tkg-007-dirichlet-l-functions-log-derivatives.jsonl"

spec = importlib.util.spec_from_file_location("tkg007", MODULE_PATH)
assert spec and spec.loader
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def main() -> None:
    records = [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(records) == 6
    assert all(r["math_contribution_level"] == "MATH-M0" for r in records)

    # Character algebra and bad-prime deletion.
    for a in range(1, 81):
        for b in range(1, 81):
            assert m.chi4(a * b) == m.chi4(a) * m.chi4(b)
    assert m.local_axis(2, 5)["bad_prime"] is True
    assert all(row["chi4"] == 0 for row in m.local_axis(2, 5)["rows"][1:])

    # Twisted logarithmic-derivative coefficients.
    assert math.isclose(m.twisted_coefficient(9), math.log(3), rel_tol=0, abs_tol=1e-12)
    assert math.isclose(m.twisted_coefficient(27), -math.log(3), rel_tol=0, abs_tol=1e-12)
    assert m.twisted_coefficient(8) == 0.0
    assert m.twisted_coefficient(45) == 0.0

    for n in range(1, 513):
        fac = m.factorization(n)
        expected = 0.0
        if len(fac) == 1:
            p = next(iter(fac))
            expected = math.log(p) * m.chi4(n)
        assert math.isclose(m.twisted_coefficient(n), expected, rel_tol=0, abs_tol=1e-12)
        assert m.explain(n)["asymptotic_inference_authorized"] is False

    # Numerical sanity in the absolute-convergence region; finite check only.
    s2_100 = m.partial_l_series(2.0, 100)
    s2_1000 = m.partial_l_series(2.0, 1000)
    assert abs(s2_1000 - s2_100) < 0.011

    print(json.dumps({
        "status": "PASS",
        "registry_records": len(records),
        "coefficient_range": 512,
        "multiplicativity_box": 80,
        "scientific_ceiling": "MATH-M0; no PNT-AP/RH/GRH progress",
    }, indent=2))


if __name__ == "__main__":
    main()
