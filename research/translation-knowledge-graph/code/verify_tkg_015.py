#!/usr/bin/env python3
"""Finite structural verifier for TKG-015. No Tauberian theorem is certified."""
from __future__ import annotations

from query_tkg_015 import REQUIRED, authorization, boundary, implication, route_pnt


def main() -> None:
    route = route_pnt()
    assert route["route"][0] == "Lambda coefficients"
    assert route["route"][-1] == "pi(x) ~ x/log(x)"
    assert "simple pole at s=1 => PNT" in route["blocked_edges"]
    assert route["PNT_progress"] == "NONE"

    incomplete = authorization(["summatory_object_fixed"])
    assert incomplete["syntactically_complete"] is False
    assert "transform_identity_verified" in incomplete["missing"]

    complete = authorization(REQUIRED)
    assert complete["syntactically_complete"] is True
    assert complete["tauberian_transfer_authorized"] is False
    assert complete["math_status"] == "MATH-M0"

    good = implication("theta~x", "pi~x/logx")
    assert good["verdict"] == "conditionally_valid"
    bad = implication("finite-pi-data", "PNT")
    assert bad["verdict"] == "rejected"
    pole_only = implication("simple-pole", "main-term-transfer")
    assert pole_only["verdict"] == "rejected"

    obstructed = boundary(True)
    assert obstructed["boundary_status"] == "obstructed"
    unproved = boundary(False)
    assert unproved["boundary_status"] == "not_certified"
    assert unproved["zero_free_region_proved"] is False

    gates = {
        "tauberian_theorem_proved": False,
        "PNT_progress": "NONE",
        "RH_progress": "NONE",
        "GRH_progress": "NONE",
        "automatic_math_promotion": False,
    }
    assert all(value is False or value == "NONE" for value in gates.values())
    print("TKG-015 structural verifier: PASS")
    print("Tauberian authorization: BLOCKED")


if __name__ == "__main__":
    main()
