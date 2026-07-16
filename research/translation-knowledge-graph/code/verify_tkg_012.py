#!/usr/bin/env python3
"""Finite structural verifier for TKG-012.

Passing this file certifies only the encoded finite identities and governance gates.
"""
from __future__ import annotations

import math

from query_tkg_012 import mellin_descriptor, weight, weighted_sum, von_mangoldt


def close(a: float, b: float, tol: float = 1e-10) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def main() -> None:
    # Kernel values and support.
    assert close(weight("exp", 0.0), 1.0)
    assert 0.0 < weight("exp", 1.0) < 1.0
    assert close(weight("triangle", 0.25), 0.75)
    assert close(weight("triangle", 1.0), 0.0)
    assert close(weight("triangle", 2.0), 0.0)
    assert close(weight("sharp", 0.5), 1.0)
    assert close(weight("sharp", 2.0), 0.0)

    # Mellin descriptors and the regularity/decay distinction.
    assert mellin_descriptor("exp")["mellin_transform"] == "Gamma(s)"
    assert mellin_descriptor("triangle")["mellin_transform"] == "1/(s(s+1))"
    assert mellin_descriptor("sharp")["mellin_transform"] == "1/s"
    assert "jump" in mellin_descriptor("sharp")["regularity"]

    # Exact finite weighted sums for the constant coefficients.
    x = 10.0
    limit = 50
    direct_exp = sum(math.exp(-n / x) for n in range(1, limit + 1))
    assert close(weighted_sum("one", "exp", x, limit), direct_exp)
    direct_triangle = sum(max(1.0 - n / x, 0.0) for n in range(1, limit + 1))
    assert close(weighted_sum("one", "triangle", x, limit), direct_triangle)

    # Von Mangoldt support examples.
    assert close(von_mangoldt(8), math.log(2))
    assert close(von_mangoldt(9), math.log(3))
    assert close(von_mangoldt(12), 0.0)
    lambda_exp = sum(von_mangoldt(n) * math.exp(-n / x) for n in range(1, limit + 1))
    assert close(weighted_sum("lambda", "exp", x, limit), lambda_exp)

    # Gamma recurrence at safe positive arguments: structural numerical check only.
    for s in (0.5, 1.0, 1.5, 2.0, 3.25):
        assert close(math.gamma(s + 1.0), s * math.gamma(s), 1e-12)

    # Scientific gates remain closed.
    gates = {
        "mellin_inversion_proved": False,
        "contour_shift_authorized": False,
        "pnt_progress": False,
        "rh_progress": False,
        "grh_progress": False,
        "math_promotion": False,
    }
    assert not any(gates.values())
    print("TKG-012 finite structural checks: PASS")
    print("Scientific theorem promotion: BLOCKED")


if __name__ == "__main__":
    main()
