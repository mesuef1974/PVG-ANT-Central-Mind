#!/usr/bin/env python3
"""TKG-012 query harness: Mellin transforms, smoothing, and weighted sums.

Finite numerical outputs are illustrations only. No analytic theorem is certified.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from typing import Callable


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def prime_power_base(n: int) -> int | None:
    if n < 2:
        return None
    for p in range(2, n + 1):
        if not is_prime(p):
            continue
        m = p
        while m < n:
            m *= p
        if m == n:
            return p
    return None


def von_mangoldt(n: int) -> float:
    p = prime_power_base(n)
    return math.log(p) if p is not None else 0.0


def weight(name: str, u: float) -> float:
    if name == "exp":
        return math.exp(-u)
    if name == "triangle":
        return max(1.0 - u, 0.0)
    if name == "sharp":
        return 1.0 if u <= 1.0 else 0.0
    raise ValueError(f"unsupported weight: {name}")


def coefficient(name: str, n: int) -> float:
    if name == "one":
        return 1.0
    if name == "lambda":
        return von_mangoldt(n)
    raise ValueError(f"unsupported coefficient: {name}")


def weighted_sum(coeff: str, kernel: str, x: float, limit: int) -> float:
    return sum(coefficient(coeff, n) * weight(kernel, n / x) for n in range(1, limit + 1))


def mellin_descriptor(kernel: str) -> dict:
    if kernel == "exp":
        return {
            "weight": "w(u)=exp(-u)",
            "mellin_transform": "Gamma(s)",
            "fundamental_strip": "Re(s)>0",
            "vertical_decay": "exponential after Stirling, subject to using the known Gamma theory",
            "regularity": "smooth; rapid decay at infinity",
        }
    if kernel == "triangle":
        return {
            "weight": "w(u)=max(1-u,0)",
            "mellin_transform": "1/(s(s+1))",
            "fundamental_strip": "Re(s)>0",
            "vertical_decay": "quadratic in |t| away from poles",
            "regularity": "continuous, piecewise C1, compact support",
        }
    if kernel == "sharp":
        return {
            "weight": "w(u)=1_{0<u<=1}",
            "mellin_transform": "1/s",
            "fundamental_strip": "Re(s)>0",
            "vertical_decay": "only first order in |t|",
            "regularity": "jump discontinuity at u=1",
        }
    raise ValueError(kernel)


def route(coeff: str, kernel: str) -> dict:
    source = {
        "one": "zeta(s)",
        "lambda": "-zeta'(s)/zeta(s)",
    }[coeff]
    m = mellin_descriptor(kernel)
    return {
        "coefficient": coeff,
        "dirichlet_series": source,
        "weight": m["weight"],
        "mellin_transform": m["mellin_transform"],
        "formal_integrand": f"({source}) * ({m['mellin_transform']}) * x^s",
        "required": [
            "common strip of validity",
            "justified interchange of sum and integral",
            "Mellin inversion hypotheses",
            "vertical integrability",
            "separate contour-shift certificate if the line is moved",
        ],
        "authorized": False,
        "math_promotion": False,
    }


def regularity(kernel: str) -> dict:
    m = mellin_descriptor(kernel)
    return {
        **m,
        "rule": "Decay must be derived from actual smoothness, endpoint vanishing, and integration-by-parts hypotheses.",
        "claim_ceiling": "ASSIM only",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="kind", required=True)

    p = sub.add_parser("mellin")
    p.add_argument("--weight", choices=["exp", "triangle", "sharp"], required=True)

    p = sub.add_parser("weighted-sum")
    p.add_argument("--coeff", choices=["one", "lambda"], required=True)
    p.add_argument("--weight", choices=["exp", "triangle", "sharp"], required=True)
    p.add_argument("--x", type=float, required=True)
    p.add_argument("--limit", type=int, default=1000)

    p = sub.add_parser("route")
    p.add_argument("--coeff", choices=["one", "lambda"], required=True)
    p.add_argument("--weight", choices=["exp", "triangle", "sharp"], required=True)

    p = sub.add_parser("regularity")
    p.add_argument("--weight", choices=["exp", "triangle", "sharp"], required=True)

    args = parser.parse_args()
    if args.kind == "mellin":
        out = mellin_descriptor(args.weight)
    elif args.kind == "weighted-sum":
        if args.x <= 0 or args.limit < 1:
            raise SystemExit("x>0 and limit>=1 required")
        out = {
            "coeff": args.coeff,
            "weight": args.weight,
            "x": args.x,
            "limit": args.limit,
            "finite_weighted_sum": weighted_sum(args.coeff, args.weight, args.x, args.limit),
            "finite_illustration_only": True,
            "asymptotic_inference_authorized": False,
        }
    elif args.kind == "route":
        out = route(args.coeff, args.weight)
    else:
        out = regularity(args.weight)
    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
