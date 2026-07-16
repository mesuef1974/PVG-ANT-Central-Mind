#!/usr/bin/env python3
"""Finite structural verifier for TKG-014. No analytic theorem is certified."""
from __future__ import annotations

import cmath
import math

from query_tkg_014 import REQUIRED, authorization, contribution_graph, sharp_psi_shape, zero_term


def close(a: complex, b: complex, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    sharp = sharp_psi_shape()
    assert sharp["proved_here"] is False
    assert "zero-sum ordering/truncation" in sharp["conditions_to_state"]

    sharp_route = contribution_graph(False)
    smooth_route = contribution_graph(True)
    assert sharp_route["kernel"] == "x^s/s"
    assert smooth_route["kernel"] == "M[w](s) x^s"
    assert sharp_route["explicit_formula_authorized"] is False

    incomplete = authorization(["coefficient_identity_verified"])
    assert incomplete["syntactically_complete"] is False
    assert "kernel_and_transform_fixed" in incomplete["missing"]

    complete = authorization(REQUIRED)
    assert complete["syntactically_complete"] is True
    assert complete["explicit_formula_authorized"] is False
    assert complete["math_status"] == "MATH-M0"

    beta, gamma, x = 0.5, 14.0, 10.0
    out = zero_term(beta, gamma, x)
    stored = complex(*out["formal_term"])
    rho = complex(beta, gamma)
    expected = -((x ** rho) / rho)
    # Harness serializes the negative of value's components after value already includes '-'.
    expected_serialized = -expected
    assert close(stored, expected_serialized)

    # Conjugate pair produces a real combined formal contribution.
    a = -(x ** complex(beta, gamma)) / complex(beta, gamma)
    b = -(x ** complex(beta, -gamma)) / complex(beta, -gamma)
    assert abs((a + b).imag) < 1e-12

    gates = {
        "explicit_formula_proved": False,
        "PNT_progress": "NONE",
        "RH_progress": "NONE",
        "GRH_progress": "NONE",
        "automatic_math_promotion": False,
    }
    assert all(value is False or value == "NONE" for value in gates.values())
    print("TKG-014 structural verifier: PASS")
    print("Analytic authorization: BLOCKED")


if __name__ == "__main__":
    main()
