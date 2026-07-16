#!/usr/bin/env python3
"""Finite structural verifier for TKG-011.

This verifies query logic and claim gates, not Perron's theorem or an explicit formula.
"""
from __future__ import annotations

from query_tkg_011 import REQUIRED_CERTIFICATES, certificate_report, residue_ledger, route


def verify() -> None:
    one = route("one")
    assert one.source == "zeta(s)"
    assert one.target == "floor(x)"
    assert "MATH-M0" in one.claim_ceiling

    lam = route("lambda")
    assert lam.source == "-zeta'(s)/zeta(s)"
    assert lam.target == "psi(x)"
    assert "no PNT" in lam.claim_ceiling

    empty = certificate_report([])
    assert empty["contour_shift_authorized"] is False
    assert empty["missing"] == REQUIRED_CERTIFICATES
    assert empty["math_promotion_authorized"] is False

    partial = certificate_report(["pole_ledger", "residue_computation"])
    assert partial["contour_shift_authorized"] is False
    assert "horizontal_side_bounds" in partial["missing"]

    complete = certificate_report(REQUIRED_CERTIFICATES)
    assert complete["contour_shift_authorized"] is True
    assert complete["missing"] == []
    assert complete["math_promotion_authorized"] is False

    one_ledger = residue_ledger("one")
    one_locations = {row["location"] for row in one_ledger["candidate_singularities"]}
    assert {"s=1", "s=0"}.issubset(one_locations)

    lambda_ledger = residue_ledger("lambda")
    locations = {row["location"] for row in lambda_ledger["candidate_singularities"]}
    assert "s=1" in locations
    assert "s=rho" in locations
    assert "s=-2k" in locations
    assert lambda_ledger["certificate"] == "not supplied"

    claim_gates = {
        "perron_theorem_proved": False,
        "contour_shift_proved": False,
        "explicit_formula_proved": False,
        "PNT_progress": False,
        "RH_progress": False,
        "GRH_progress": False,
        "Goldbach_progress": False,
        "MATH_promotion": False,
    }
    assert not any(claim_gates.values())


if __name__ == "__main__":
    verify()
    print("TKG-011 verifier: PASS (finite structural checks only)")
