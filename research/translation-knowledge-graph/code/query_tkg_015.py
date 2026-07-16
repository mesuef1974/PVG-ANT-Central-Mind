#!/usr/bin/env python3
"""TKG-015 query harness: Tauberian routing with no theorem promotion."""
from __future__ import annotations

import argparse
import json
from typing import Iterable

REQUIRED = [
    "summatory_object_fixed",
    "transform_identity_verified",
    "boundary_point_fixed",
    "pole_main_part_verified",
    "remainder_boundary_hypothesis_verified",
    "positivity_or_monotonicity_verified",
    "theorem_variant_fixed",
    "normalization_verified",
    "conclusion_scope_fixed",
    "source_or_proof_attached",
]


def authorization(provided: Iterable[str]) -> dict:
    supplied = set(provided)
    missing = [item for item in REQUIRED if item not in supplied]
    return {
        "syntactically_complete": not missing,
        "missing": missing,
        "tauberian_transfer_authorized": False,
        "reason": "This harness checks structure only; it does not validate analytic hypotheses or proofs.",
        "math_status": "MATH-M0",
    }


def route_pnt() -> dict:
    return {
        "route": [
            "Lambda coefficients",
            "-zeta'/zeta transform identity",
            "zeta nonvanishing on Re(s)=1",
            "boundary regularity after main-part subtraction",
            "applicable Tauberian theorem",
            "psi(x) ~ x",
            "partial summation",
            "pi(x) ~ x/log(x)",
        ],
        "blocked_edges": [
            "Euler product => PNT",
            "simple pole at s=1 => PNT",
            "finite computation => asymptotic theorem",
        ],
        "PNT_progress": "NONE",
    }


def implication(source: str, target: str) -> dict:
    valid = {
        ("psi~x", "theta~x"): "valid with prime-power correction control",
        ("theta~x", "pi~x/logx"): "valid through partial summation",
        ("certified-tauberian-hypotheses", "main-term-transfer"): "valid theorem route",
    }
    invalid = {
        ("finite-pi-data", "PNT"): "finite evidence does not imply an asymptotic theorem",
        ("functional-equation-symmetry", "boundary-nonvanishing"): "symmetry does not prove nonvanishing",
        ("simple-pole", "main-term-transfer"): "pole data alone omit side conditions",
    }
    key = (source, target)
    if key in valid:
        verdict, reason = "conditionally_valid", valid[key]
    elif key in invalid:
        verdict, reason = "rejected", invalid[key]
    else:
        verdict, reason = "undetermined", "No governed implication is registered for this pair."
    return {
        "source": source,
        "target": target,
        "verdict": verdict,
        "reason": reason,
        "automatic_math_promotion": False,
    }


def boundary(zero_on_boundary: bool) -> dict:
    if zero_on_boundary:
        status = "obstructed"
        note = "A boundary zero creates a singularity in the logarithmic derivative."
    else:
        status = "not_certified"
        note = "Absence was supplied as a flag, not proved by this harness."
    return {
        "boundary_status": status,
        "note": note,
        "zero_free_region_proved": False,
        "PNT_progress": "NONE",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="kind", required=True)
    sub.add_parser("pnt-route")
    gate = sub.add_parser("authorize")
    gate.add_argument("--provided", nargs="*", default=[])
    imp = sub.add_parser("implication")
    imp.add_argument("--source", required=True)
    imp.add_argument("--target", required=True)
    bound = sub.add_parser("boundary")
    bound.add_argument("--zero-on-boundary", action="store_true")
    args = parser.parse_args()

    if args.kind == "pnt-route":
        payload = route_pnt()
    elif args.kind == "authorize":
        payload = authorization(args.provided)
    elif args.kind == "implication":
        payload = implication(args.source, args.target)
    else:
        payload = boundary(args.zero_on_boundary)
    payload.update({"RH_progress": "NONE", "GRH_progress": "NONE", "Goldbach_progress": "NONE"})
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
