#!/usr/bin/env python3
"""Deterministic queries for TKG-009.

Scope is intentionally finite and centered on the primitive real character chi4.
No analytic-continuation, zero-location, RH, or GRH claim is produced.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from typing import Any


def chi4(n: int) -> int:
    r = n % 4
    if r == 0 or r == 2:
        return 0
    return 1 if r == 1 else -1


def parity() -> dict[str, Any]:
    value = chi4(-1)
    a = 0 if value == 1 else 1
    return {"chi_minus_one": value, "a": a, "kind": "even" if a == 0 else "odd"}


def gauss_sum() -> complex:
    q = 4
    return sum(chi4(r) * cmath.exp(2j * math.pi * r / q) for r in range(q))


def root_number() -> complex:
    q = 4
    a = parity()["a"]
    return gauss_sum() / ((1j**a) * math.sqrt(q))


def l_partial(s: float, limit: int) -> float:
    if s <= 1:
        raise ValueError("This finite Dirichlet-series route is governed only for s>1.")
    return sum(chi4(n) / (n**s) for n in range(1, limit + 1))


def completed_partial(s: float, limit: int) -> float:
    a = parity()["a"]
    q = 4
    return ((q / math.pi) ** ((s + a) / 2)) * math.gamma((s + a) / 2) * l_partial(s, limit)


def explain() -> dict[str, Any]:
    tau = gauss_sum()
    eps = root_number()
    return {
        "character": "primitive chi4 modulo 4",
        "conductor": 4,
        "parity": parity(),
        "gauss_sum": {"real": tau.real, "imag": tau.imag, "abs": abs(tau)},
        "root_number": {"real": eps.real, "imag": eps.imag, "abs": abs(eps)},
        "completed_function": "Lambda(s,chi4)=(4/pi)^((s+1)/2) Gamma((s+1)/2)L(s,chi4)",
        "functional_equation_route": "Lambda(s,chi4)=Lambda(1-s,chi4), after analytic continuation",
        "pvg_boundary": "Residue Fourier phase and archimedean gamma data are not recoverable from an unlabeled valuation shape alone.",
        "rh_progress": "NONE",
        "grh_progress": "NONE",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="kind", required=True)
    sub.add_parser("explain")
    sub.add_parser("parity")
    sub.add_parser("gauss")
    sub.add_parser("root-number")
    p = sub.add_parser("partial-completed")
    p.add_argument("--s", type=float, required=True)
    p.add_argument("--limit", type=int, default=10000)
    args = parser.parse_args()

    if args.kind == "explain":
        out = explain()
    elif args.kind == "parity":
        out = parity()
    elif args.kind == "gauss":
        z = gauss_sum()
        out = {"real": z.real, "imag": z.imag, "abs": abs(z), "expected": "2i"}
    elif args.kind == "root-number":
        z = root_number()
        out = {"real": z.real, "imag": z.imag, "abs": abs(z), "expected": "1"}
    else:
        out = {
            "s": args.s,
            "limit": args.limit,
            "completed_partial": completed_partial(args.s, args.limit),
            "warning": "Finite truncation only; not a proof of the functional equation.",
        }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
