#!/usr/bin/env python3
"""Finite symbolic query harness for TKG-010.

This tool classifies complex points and routes known zero symmetries. It does not
compute or certify zeros of any L-function.
"""
from __future__ import annotations

import argparse
import json


def classify(beta: float, tol: float = 1e-12) -> str:
    if abs(beta - 0.5) <= tol:
        return "critical_line"
    if 0.0 < beta < 1.0:
        return "critical_strip"
    if beta >= 1.0:
        return "right_of_or_on_one"
    if beta <= 0.0:
        return "left_of_or_on_zero"
    return "unclassified"


def partners(beta: float, gamma: float, real_coefficients: bool) -> list[dict[str, float]]:
    pts = {(beta, gamma), (1.0 - beta, gamma)}
    if real_coefficients:
        pts |= {(beta, -gamma), (1.0 - beta, -gamma)}
    return [{"real": x, "imag": y} for x, y in sorted(pts)]


def trivial_progression(parity: str, count: int) -> list[int]:
    if parity == "even":
        return [-2 * k for k in range(1, count + 1)]
    return [-(2 * k + 1) for k in range(count)]


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="kind", required=True)

    c = sub.add_parser("classify")
    c.add_argument("--beta", type=float, required=True)
    c.add_argument("--gamma", type=float, default=0.0)

    p = sub.add_parser("partners")
    p.add_argument("--beta", type=float, required=True)
    p.add_argument("--gamma", type=float, required=True)
    p.add_argument("--real-coefficients", action="store_true")

    t = sub.add_parser("trivial")
    t.add_argument("--parity", choices=["even", "odd"], required=True)
    t.add_argument("--count", type=int, default=6)

    sub.add_parser("prerequisites")
    args = parser.parse_args()

    if args.kind == "classify":
        out = {"point": [args.beta, args.gamma], "region": classify(args.beta)}
    elif args.kind == "partners":
        out = {
            "input": [args.beta, args.gamma],
            "partners": partners(args.beta, args.gamma, args.real_coefficients),
            "warning": "routing under functional-equation hypotheses; not zero certification",
        }
    elif args.kind == "trivial":
        out = {
            "parity": args.parity,
            "candidate_progression": trivial_progression(args.parity, args.count),
            "warning": "check exact character and completed-function convention",
        }
    else:
        out = {
            "explicit_formula_requires": [
                "continuation", "functional equation", "pole/trivial-zero ledger",
                "logarithmic derivative", "contour bounds", "zero-sum convention",
            ],
            "authorized": False,
        }
    out["RH_progress"] = "NONE"
    out["GRH_progress"] = "NONE"
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
