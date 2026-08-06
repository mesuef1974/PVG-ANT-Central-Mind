#!/usr/bin/env python3
"""Finite verifier for TKG-009.

This verifier checks parity, the chi4 Gauss sum, root number, and governance gates.
It does not claim analytic continuation or prove a functional equation.
"""
from __future__ import annotations

import cmath
import math

from query_tkg_009 import chi4, gauss_sum, parity, root_number


def close(a: complex, b: complex, tol: float = 1e-10) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    assert chi4(-1) == -1
    assert parity() == {"chi_minus_one": -1, "a": 1, "kind": "odd"}

    # Complete multiplicativity over a finite box.
    for m in range(1, 81):
        for n in range(1, 81):
            assert chi4(m * n) == chi4(m) * chi4(n)

    tau = gauss_sum()
    assert close(tau, 2j)
    assert abs(abs(tau) - math.sqrt(4)) <= 1e-10

    eps = root_number()
    assert close(eps, 1 + 0j)
    assert abs(abs(eps) - 1.0) <= 1e-10

    # Direct finite Fourier identity for units modulo 4.
    for n in range(1, 40, 2):
        lhs = sum(chi4(r) * cmath.exp(2j * math.pi * r * n / 4) for r in range(4))
        rhs = chi4(n) * tau
        assert close(lhs, rhs)

    # Governance: symmetry routing is not zero-location evidence.
    gates = {
        "analytic_continuation_proved": False,
        "functional_equation_proved_by_finite_test": False,
        "rh_progress": False,
        "grh_progress": False,
        "pnt_ap_progress": False,
    }
    assert not any(gates.values())

    print("TKG-009 finite verifier: PASS")
    print("Scope: parity, Gauss sum, root number, finite Fourier identity, claim gates")
    print("Analytic continuation / functional equation / RH / GRH: NOT CLAIMED")


if __name__ == "__main__":
    main()
