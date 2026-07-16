#!/usr/bin/env python3
"""Finite verifier for TKG-010 taxonomy and claim gates."""
from __future__ import annotations

from query_tkg_010 import classify, partners, trivial_progression


def main() -> None:
    assert classify(0.5) == "critical_line"
    assert classify(0.25) == "critical_strip"
    assert classify(0.75) == "critical_strip"
    assert classify(1.0) == "right_of_or_on_one"
    assert classify(0.0) == "left_of_or_on_zero"

    quartet = partners(0.3, 14.0, True)
    expected = [
        {"real": 0.3, "imag": -14.0},
        {"real": 0.3, "imag": 14.0},
        {"real": 0.7, "imag": -14.0},
        {"real": 0.7, "imag": 14.0},
    ]
    assert quartet == expected

    pair = partners(0.3, 14.0, False)
    assert pair == [
        {"real": 0.3, "imag": 14.0},
        {"real": 0.7, "imag": 14.0},
    ]

    assert trivial_progression("even", 5) == [-2, -4, -6, -8, -10]
    assert trivial_progression("odd", 5) == [-1, -3, -5, -7, -9]

    # A symmetric off-line pair is a direct counterexample to the inference
    # 'functional-equation symmetry => critical-line location'.
    assert classify(0.3) != "critical_line"
    assert classify(0.7) != "critical_line"
    assert abs((0.3 + 0.7) - 1.0) < 1e-12

    gates = {
        "zero_certified": False,
        "explicit_formula_authorized": False,
        "RH_progress": False,
        "GRH_progress": False,
        "MATH_promotion": False,
    }
    assert not any(gates.values())
    print("TKG-010 verifier: PASS (finite taxonomy only)")


if __name__ == "__main__":
    main()
