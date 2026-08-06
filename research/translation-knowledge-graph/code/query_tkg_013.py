#!/usr/bin/env python3
"""TKG-013 symbolic query harness.

Finite structural reasoning only. It does not certify analytic estimates.
"""
from __future__ import annotations

import argparse
import cmath
import json
from typing import Iterable

REQUIRED_CERT_FIELDS = [
    "integrand_definition", "meromorphic_region", "contour_geometry",
    "orientation", "singularity_ledger", "residue_values",
    "right_segment_bound", "left_segment_bound", "top_segment_bound",
    "bottom_segment_bound", "truncation_error", "endpoint_convention",
    "limit_order", "sign_audit", "source_or_proof",
]


def simple_residue_xs_over_s(x: float) -> complex:
    if x <= 0:
        raise ValueError("x must be positive")
    return 1.0 + 0.0j


def simple_pole_contribution(residue: complex, s0: complex, x: float) -> complex:
    if x <= 0:
        raise ValueError("x must be positive")
    return residue * cmath.exp(s0 * cmath.log(x))


def orientation_ledger() -> dict[str, object]:
    return {
        "closed_orientation": "counterclockwise",
        "segments": {
            "right": "up", "top": "left", "left": "down", "bottom": "right"
        },
        "shift_identity": (
            "right_up = left_up + 2*pi*i*sum(residues) - top_left - bottom_right"
        ),
        "warning": "left_down = -left_up",
    }


def certificate_status(provided: Iterable[str]) -> dict[str, object]:
    have = set(provided)
    missing = [field for field in REQUIRED_CERT_FIELDS if field not in have]
    return {
        "provided": sorted(have),
        "missing": missing,
        "syntactically_complete": not missing,
        "contour_shift_authorized": False,
        "reason": (
            "Even a complete field list needs proof-grade evidence; this harness never promotes MATH."
        ),
        "math_state": "MATH-M0",
    }


def error_ledger() -> dict[str, object]:
    return {
        "components": [
            "right truncation tail", "left vertical integral",
            "top horizontal integral", "bottom horizontal integral",
            "small indentation arcs", "endpoint half-weight",
            "zero-sum truncation", "limit interchange",
        ],
        "required_metadata": ["parameter", "domain", "bound", "norm", "limit_order", "source"],
        "explicit_formula_authorized": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="kind", required=True)

    residue = sub.add_parser("residue")
    residue.add_argument("--x", type=float, default=10.0)
    residue.add_argument("--real-residue", type=float, default=1.0)
    residue.add_argument("--imag-residue", type=float, default=0.0)
    residue.add_argument("--beta", type=float, default=1.0)
    residue.add_argument("--gamma", type=float, default=0.0)

    sub.add_parser("orientation")
    cert = sub.add_parser("certificate")
    cert.add_argument("--provided", nargs="*", default=[])
    sub.add_parser("errors")

    args = parser.parse_args()
    if args.kind == "residue":
        r = complex(args.real_residue, args.imag_residue)
        s0 = complex(args.beta, args.gamma)
        out = {
            "kernel_example": {"integrand": "x^s/s", "pole": "0", "residue": 1.0},
            "general_simple_pole": {
                "residue_of_F": [r.real, r.imag],
                "s0": [s0.real, s0.imag],
                "x": args.x,
                "contribution": [
                    simple_pole_contribution(r, s0, args.x).real,
                    simple_pole_contribution(r, s0, args.x).imag,
                ],
            },
            "claim_ceiling": "finite symbolic calculation",
        }
    elif args.kind == "orientation":
        out = orientation_ledger()
    elif args.kind == "certificate":
        out = certificate_status(args.provided)
    else:
        out = error_ledger()
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
