#!/usr/bin/env python3
"""Finite deterministic verifier for TKG-003."""
from __future__ import annotations

import json
from pathlib import Path

import query_tkg_003 as q

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "translation-knowledge-graph/registry/tkg-003-dirichlet-series-euler-products.jsonl"


def verify_registry() -> None:
    records = [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]
    assert len(records) == 7
    assert all(r["math_contribution_level"] == "MATH-M0" for r in records)
    assert any(r["record_type"] == "CLAIM_REJECTION" for r in records)


def verify_convolution_coefficients(limit: int = 256) -> None:
    for n in range(1, limit + 1):
        assert q.convolve(q.one, q.one, n) == q.tau(n)
        assert q.convolve(q.one, q.identity, n) == q.sigma(n)
        assert q.convolve(q.mobius, q.one, n) == q.epsilon(n)


def verify_multiplicativity(limit: int = 80) -> None:
    for name in ("one", "mu", "tau", "sigma", "id"):
        f = q.FUNCTIONS[name]
        assert f(1) == 1
        for m in range(1, limit + 1):
            for n in range(1, limit + 1):
                if q.math.gcd(m, n) == 1:
                    assert f(m * n) == f(m) * f(n), (name, m, n)


def verify_not_complete_multiplicativity() -> None:
    assert q.tau(4) == 3
    assert q.tau(2) * q.tau(2) == 4
    assert q.tau(4) != q.tau(2) ** 2
    assert q.sigma(4) == 7
    assert q.sigma(2) ** 2 == 9


def verify_local_axis_data() -> None:
    assert [x["coefficient"] for x in q.local_coefficients("one", 2, 4)] == [1, 1, 1, 1, 1]
    assert [x["coefficient"] for x in q.local_coefficients("mu", 3, 4)] == [1, -1, 0, 0, 0]
    assert [x["coefficient"] for x in q.local_coefficients("tau", 5, 4)] == [1, 2, 3, 4, 5]


def verify_pvg_examples() -> None:
    ex12 = q.explain_tau(12)
    assert ex12["valuation_vector"] == {2: 2, 3: 1}
    assert ex12["tau"] == 6
    assert ex12["divisor_box_cardinality"] == 6
    assert ex12["asymptotic_inference_authorized"] is False

    ex24 = q.explain_tau(24)
    assert ex24["valuation_vector"] == {2: 3, 3: 1}
    assert ex24["tau"] == 8

    ex30 = q.explain_tau(30)
    assert ex30["valuation_vector"] == {2: 1, 3: 1, 5: 1}
    assert ex30["tau"] == 8


def main() -> None:
    verify_registry()
    verify_convolution_coefficients()
    verify_multiplicativity()
    verify_not_complete_multiplicativity()
    verify_local_axis_data()
    verify_pvg_examples()
    print(json.dumps({
        "unit": "TKG-003",
        "status": "PASS",
        "verified": [
            "registry governance",
            "Dirichlet-series product coefficients through 256",
            "multiplicativity on coprime pairs through 80",
            "counterexamples to complete multiplicativity",
            "prime-axis local coefficients",
            "PVG examples 12, 24, 30",
            "asymptotic claim gate"
        ],
        "scientific_ceiling": {
            "math": "MATH-M0",
            "PNT_progress": "NONE",
            "RH_progress": "NONE",
            "GRH_progress": "NONE"
        }
    }, indent=2))


if __name__ == "__main__":
    main()
