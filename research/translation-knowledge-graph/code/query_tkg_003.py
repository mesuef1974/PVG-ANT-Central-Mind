#!/usr/bin/env python3
"""Deterministic symbolic query harness for TKG-003.

This is an inspectable arithmetic engine, not a neural model.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "translation-knowledge-graph/registry/tkg-003-dirichlet-series-euler-products.jsonl"


def factorization(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("n must be positive")
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n: int) -> list[int]:
    out = [1]
    for p, a in factorization(n).items():
        out = [d * p**k for d in out for k in range(a + 1)]
    return sorted(out)


def mobius(n: int) -> int:
    fac = factorization(n)
    if any(a > 1 for a in fac.values()):
        return 0
    return -1 if len(fac) % 2 else 1


def tau(n: int) -> int:
    value = 1
    for a in factorization(n).values():
        value *= a + 1
    return value


def sigma(n: int) -> int:
    return sum(divisors(n))


def one(_: int) -> int:
    return 1


def epsilon(n: int) -> int:
    return int(n == 1)


def identity(n: int) -> int:
    return n


FUNCTIONS: dict[str, Callable[[int], float]] = {
    "one": one,
    "epsilon": epsilon,
    "mu": mobius,
    "tau": tau,
    "sigma": sigma,
    "id": identity,
}


def convolve(f: Callable[[int], float], g: Callable[[int], float], n: int) -> float:
    return sum(f(d) * g(n // d) for d in divisors(n))


def local_coefficients(name: str, p: int, max_k: int) -> list[dict]:
    f = FUNCTIONS[name]
    return [{"k": k, "n": p**k, "coefficient": f(p**k)} for k in range(max_k + 1)]


def multiplicativity_check(name: str, m: int, n: int) -> dict:
    f = FUNCTIONS[name]
    gcd = math.gcd(m, n)
    lhs = f(m * n)
    rhs = f(m) * f(n)
    return {
        "function": name,
        "m": m,
        "n": n,
        "gcd": gcd,
        "lhs": lhs,
        "rhs": rhs,
        "multiplicative_condition_applies": gcd == 1,
        "identity_holds": lhs == rhs,
    }


def convolution_product_check(f_name: str, g_name: str, limit: int) -> dict:
    f, g = FUNCTIONS[f_name], FUNCTIONS[g_name]
    coefficients = []
    for n in range(1, limit + 1):
        coefficients.append({"n": n, "convolution_coefficient": convolve(f, g, n)})
    return {
        "f": f_name,
        "g": g_name,
        "limit": limit,
        "coefficients": coefficients,
        "interpretation": "These are the coefficients obtained by multiplying the two formal Dirichlet series.",
        "analytic_warning": "Numerical coefficient agreement does not by itself establish convergence or justify infinite rearrangement outside a valid region.",
    }


def explain_tau(n: int) -> dict:
    fac = factorization(n)
    return {
        "n": n,
        "valuation_vector": fac,
        "tau": tau(n),
        "divisor_box_cardinality": math.prod(a + 1 for a in fac.values()),
        "identity": "tau = one * one",
        "dirichlet_series": "D_tau(s) = zeta(s)^2 for Re(s)>1",
        "local_factors": {str(p): f"sum_(k>=0) (k+1) {p}^(-ks) = (1-{p}^(-s))^(-2)" for p in fac},
        "asymptotic_inference_authorized": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="kind", required=True)

    p_tau = sub.add_parser("tau")
    p_tau.add_argument("--n", type=int, required=True)

    p_local = sub.add_parser("local")
    p_local.add_argument("--function", choices=sorted(FUNCTIONS), required=True)
    p_local.add_argument("--p", type=int, required=True)
    p_local.add_argument("--max-k", type=int, default=5)

    p_mult = sub.add_parser("multiplicative")
    p_mult.add_argument("--function", choices=sorted(FUNCTIONS), required=True)
    p_mult.add_argument("--m", type=int, required=True)
    p_mult.add_argument("--n", type=int, required=True)

    p_conv = sub.add_parser("convolution-product")
    p_conv.add_argument("--f", choices=sorted(FUNCTIONS), required=True)
    p_conv.add_argument("--g", choices=sorted(FUNCTIONS), required=True)
    p_conv.add_argument("--limit", type=int, default=12)

    args = parser.parse_args()
    if args.kind == "tau":
        result = explain_tau(args.n)
    elif args.kind == "local":
        result = local_coefficients(args.function, args.p, args.max_k)
    elif args.kind == "multiplicative":
        result = multiplicativity_check(args.function, args.m, args.n)
    else:
        result = convolution_product_check(args.f, args.g, args.limit)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
