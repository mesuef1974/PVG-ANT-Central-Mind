#!/usr/bin/env python3
"""Finite structural verifier for TKG-013."""
from __future__ import annotations

import cmath

from query_tkg_013 import (
    REQUIRED_CERT_FIELDS,
    certificate_status,
    orientation_ledger,
    simple_pole_contribution,
)


def close(a: complex, b: complex, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol


def run() -> None:
    # Residue of x^s/s at zero.
    for x in (0.5, 1.0, 2.0, 10.0, 100.0):
        assert close(simple_pole_contribution(1.0, 0.0, x), 1.0)

    # A simple pole r/(s-s0) contributes r*x^s0.
    r = 2.0 - 3.0j
    s0 = 0.25 + 4.0j
    x = 7.0
    expected = r * cmath.exp(s0 * cmath.log(x))
    assert close(simple_pole_contribution(r, s0, x), expected)

    orient = orientation_ledger()
    assert orient["segments"]["left"] == "down"
    assert "left_up" in orient["shift_identity"]

    empty = certificate_status([])
    assert not empty["syntactically_complete"]
    assert not empty["contour_shift_authorized"]
    assert set(empty["missing"]) == set(REQUIRED_CERT_FIELDS)

    complete = certificate_status(REQUIRED_CERT_FIELDS)
    assert complete["syntactically_complete"]
    assert not complete["contour_shift_authorized"]
    assert complete["math_state"] == "MATH-M0"

    # Claim gates remain closed.
    gates = {
        "explicit_formula_authorized": False,
        "PNT_progress": "NONE",
        "RH_progress": "NONE",
        "GRH_progress": "NONE",
        "MATH_promotion": False,
    }
    assert gates["explicit_formula_authorized"] is False
    assert gates["MATH_promotion"] is False

    print("TKG-013 finite structural verifier: PASS")


if __name__ == "__main__":
    run()
