#!/usr/bin/env python3
"""TKG-014 query harness: explicit-formula assembly without theorem promotion."""
from __future__ import annotations

import argparse
import json
from typing import Iterable

REQUIRED = [
    "coefficient_identity_verified",
    "kernel_and_transform_fixed",
    "meromorphic_continuation_certificate",
    "functional_equation_certificate_if_used",
    "complete_pole_zero_ledger",
    "residue_values_verified",
    "contour_orientation_verified",
    "all_segment_bounds_verified",
    "truncation_and_limit_order_verified",
    "zero_sum_convention_fixed",
    "endpoint_convention_fixed",
    "archimedean_terms_verified",
    "source_or_proof_attached",
]


def authorization(provided: Iterable[str]) -> dict:
    supplied = set(provided)
    missing = [item for item in REQUIRED if item not in supplied]
    return {
        "syntactically_complete": not missing,
        "missing": missing,
        "explicit_formula_authorized": False,
        "reason": "Evidence values and proofs are not validated by this structural harness.",
        "math_status": "MATH-M0",
    }


def contribution_graph(weighted: bool) -> dict:
    kernel = "M[w](s) x^s" if weighted else "x^s/s"
    return {
        "kernel": kernel,
        "assembly": [
            "main pole contributions",
            "nontrivial-zero contributions",
            "trivial-zero contributions",
            "Gamma/archimedean terms",
            "endpoint convention",
            "certified remainder",
        ],
        "translation": "hybrid nonlocal ANT↔PVG",
        "explicit_formula_authorized": False,
    }


def sharp_psi_shape() -> dict:
    return {
        "observable": "psi(x)",
        "classical_target_shape": "x - sum_rho x^rho/rho - log(2*pi) - 1/2 log(1-x^-2)",
        "conditions_to_state": [
            "x > 1",
            "endpoint convention at prime powers",
            "zero-sum ordering/truncation",
            "normalization and branch conventions",
        ],
        "proved_here": False,
    }


def zero_term(beta: float, gamma: float, x: float) -> dict:
    rho = complex(beta, gamma)
    value = -(x ** rho) / rho
    return {
        "rho": [rho.real, rho.imag],
        "formal_term": [value.real, value.imag],
        "note": "A single formal contribution; no convergence or zero certification is implied.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="kind", required=True)
    sub.add_parser("sharp-psi")
    route = sub.add_parser("route")
    route.add_argument("--weighted", action="store_true")
    gate = sub.add_parser("authorize")
    gate.add_argument("--provided", nargs="*", default=[])
    zero = sub.add_parser("zero-term")
    zero.add_argument("--beta", type=float, required=True)
    zero.add_argument("--gamma", type=float, required=True)
    zero.add_argument("--x", type=float, required=True)
    args = parser.parse_args()

    if args.kind == "sharp-psi":
        payload = sharp_psi_shape()
    elif args.kind == "route":
        payload = contribution_graph(args.weighted)
    elif args.kind == "authorize":
        payload = authorization(args.provided)
    else:
        if args.x <= 0:
            raise SystemExit("x must be positive")
        payload = zero_term(args.beta, args.gamma, args.x)
    payload.update({"RH_progress": "NONE", "GRH_progress": "NONE", "PNT_progress": "NONE"})
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
