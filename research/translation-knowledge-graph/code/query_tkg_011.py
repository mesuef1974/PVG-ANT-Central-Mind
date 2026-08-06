#!/usr/bin/env python3
"""TKG-011 query harness: Perron routing and contour-shift certificates.

Finite symbolic diagnostics only. This file does not prove an explicit formula.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from typing import List


REQUIRED_CERTIFICATES = [
    "meromorphic_continuation_region",
    "pole_ledger",
    "vertical_side_bound",
    "horizontal_side_bounds",
    "truncation_error",
    "residue_computation",
    "orientation_and_sign",
    "boundary_convention",
]


@dataclass(frozen=True)
class Route:
    source: str
    coefficients: str
    target: str
    integrand: str
    status: str
    claim_ceiling: str


def route(name: str) -> Route:
    if name == "one":
        return Route(
            source="zeta(s)",
            coefficients="a(n)=1",
            target="floor(x)",
            integrand="zeta(s) x^s / s",
            status="formal Perron route; rigorous use needs theorem and error control",
            claim_ceiling="ASSIM only / MATH-M0",
        )
    if name == "lambda":
        return Route(
            source="-zeta'(s)/zeta(s)",
            coefficients="a(n)=Lambda(n)",
            target="psi(x)",
            integrand="(-zeta'/zeta)(s) x^s / s",
            status="explicit-formula prerequisite route only",
            claim_ceiling="no PNT, RH, or explicit-formula proof",
        )
    raise ValueError(f"unsupported route: {name}")


def certificate_report(provided: List[str]) -> dict:
    supplied = set(provided)
    missing = [x for x in REQUIRED_CERTIFICATES if x not in supplied]
    return {
        "required": REQUIRED_CERTIFICATES,
        "provided": sorted(supplied),
        "missing": missing,
        "contour_shift_authorized": not missing,
        "warning": "Authorization records structural completeness only; mathematical validity still requires proofs of every supplied certificate.",
        "math_promotion_authorized": False,
    }


def residue_ledger(name: str) -> dict:
    if name == "one":
        return {
            "integrand": "zeta(s)x^s/s",
            "candidate_singularities": [
                {"location": "s=1", "source": "pole of zeta", "candidate_contribution": "x"},
                {"location": "s=0", "source": "Perron kernel", "candidate_contribution": "depends on formulation"},
            ],
            "certificate": "not supplied",
        }
    if name == "lambda":
        return {
            "integrand": "(-zeta'/zeta)(s)x^s/s",
            "candidate_singularities": [
                {"location": "s=1", "source": "pole of -zeta'/zeta", "role": "main term"},
                {"location": "s=rho", "source": "nontrivial zero of zeta", "role": "zero contribution"},
                {"location": "s=-2k", "source": "trivial zeros", "role": "archimedean/trivial-zero correction"},
                {"location": "s=0", "source": "kernel and local behavior", "role": "formulation-dependent correction"},
            ],
            "certificate": "not supplied",
        }
    raise ValueError(f"unsupported ledger: {name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="kind", required=True)

    p_route = sub.add_parser("route")
    p_route.add_argument("--source", choices=["one", "lambda"], required=True)

    p_cert = sub.add_parser("certificate")
    p_cert.add_argument("--provided", nargs="*", default=[])

    p_res = sub.add_parser("residues")
    p_res.add_argument("--source", choices=["one", "lambda"], required=True)

    sub.add_parser("prerequisites")
    args = parser.parse_args()

    if args.kind == "route":
        out = asdict(route(args.source))
    elif args.kind == "certificate":
        out = certificate_report(args.provided)
    elif args.kind == "residues":
        out = residue_ledger(args.source)
    else:
        out = {
            "perron": ["Dirichlet series on the starting line", "valid truncation/interchange", "cutoff convention"],
            "contour_shift": REQUIRED_CERTIFICATES,
            "explicit_formula": [
                "analytic or meromorphic continuation",
                "functional equation when used",
                "complete pole and zero ledger",
                "logarithmic derivative identity",
                "contour bounds",
                "zero-sum convergence convention",
                "endpoint or smoothing protocol",
            ],
            "explicit_formula_authorized": False,
        }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
