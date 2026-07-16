#!/usr/bin/env python3
"""Finite structural verifier for REASONING-ORCHESTRATOR-001."""
from __future__ import annotations

from query_reasoning_orchestrator_001 import detect_intents, reason


def main() -> None:
    convolution = reason("Use Möbius inversion on this divisor convolution")
    assert "arithmetic_identity" in convolution["detected_intents"]
    assert convolution["selected_units"] == ["TKG-001", "TKG-002"]
    assert convolution["claim_ceiling"]["MATH"] == "MATH-M0"

    pnt = reason("The Euler product proves the Prime Number Theorem")
    assert "pnt_claim" in pnt["detected_intents"]
    assert any(edge["target"] == "PNT" for edge in pnt["blocked_edges_triggered"])
    assert pnt["claim_ceiling"]["PNT"] == "NONE"
    assert pnt["authorization"] is False

    rh = reason("Functional equation symmetry proves RH")
    assert "rh_claim" in rh["detected_intents"]
    assert any(edge["target"] == "RH" for edge in rh["blocked_edges_triggered"])
    assert rh["claim_ceiling"]["RH"] == "NONE"

    explicit = reason("Build an explicit formula by Perron contour shift")
    assert "explicit_formula" in explicit["detected_intents"]
    for unit in ["TKG-011", "TKG-012", "TKG-013", "TKG-014"]:
        assert unit in explicit["selected_units"]
    assert "all contour bounds certified" in explicit["missing_certificates"]
    assert explicit["claim_ceiling"]["ASSIM"] == "ASSIM-L2"

    unknown = detect_intents("unrelated sentence")
    assert unknown.intents == ["unclassified"]
    assert unknown.units == []

    all_gates = [
        convolution["claim_ceiling"]["MATH"] == "MATH-M0",
        pnt["claim_ceiling"]["PNT"] == "NONE",
        rh["claim_ceiling"]["RH"] == "NONE",
        explicit["authorization"] is False,
    ]
    assert all(all_gates)
    print("REASONING-ORCHESTRATOR-001 structural verifier: PASS")
    print("Automatic theorem promotion: BLOCKED")


if __name__ == "__main__":
    main()
