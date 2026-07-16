#!/usr/bin/env python3
"""Deterministic query harness for TKG-007.

Implements the real primitive character modulo 4 as a finite reasoning core.
This is symbolic infrastructure, not a proof engine for PNT-AP or GRH.
"""
from __future__ import annotations

import argparse
import json
import math


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


def chi4(n: int) -> int:
    r = n % 4
    if r % 2 == 0:
        return 0
    return 1 if r == 1 else -1


def von_mangoldt(n: int) -> float:
    fac = factorization(n)
    if len(fac) != 1:
        return 0.0
    return math.log(next(iter(fac)))


def twisted_coefficient(n: int) -> float:
    return von_mangoldt(n) * chi4(n)


def local_axis(p: int, max_k: int) -> dict:
    rows = []
    for k in range(max_k + 1):
        n = p**k
        rows.append({
            "k": k,
            "n": n,
            "chi4": chi4(n),
            "euler_coefficient": chi4(n),
            "log_derivative_coefficient": 0.0 if k == 0 else twisted_coefficient(n),
        })
    return {
        "prime": p,
        "bad_prime": p == 2,
        "local_factor": "1" if p == 2 else "(1-chi4(p)*p^(-s))^(-1)",
        "rows": rows,
    }


def explain(n: int) -> dict:
    fac = factorization(n)
    value = twisted_coefficient(n)
    return {
        "n": n,
        "factorization": fac,
        "chi4": chi4(n),
        "lambda": von_mangoldt(n),
        "twisted_log_derivative_coefficient": value,
        "single_axis": len(fac) == 1,
        "pvg_route": "decode labelled valuation point; if single-axis k e_p, attach log(p)*chi4(p)^k; otherwise coefficient zero",
        "asymptotic_inference_authorized": False,
        "missing_for_pnt_ap": ["analytic continuation/nonvanishing input", "zero-free or Tauberian control", "bounds for nonprincipal twisted sums"],
    }


def partial_l_series(s: float, limit: int) -> float:
    if s <= 1:
        raise ValueError("this finite harness requires s>1 for the governed absolute-convergence regime")
    return sum(chi4(n) / (n**s) for n in range(1, limit + 1))


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="kind", required=True)

    p_exp = sub.add_parser("coefficient")
    p_exp.add_argument("--n", type=int, required=True)

    p_loc = sub.add_parser("local")
    p_loc.add_argument("--p", type=int, required=True)
    p_loc.add_argument("--max-k", type=int, default=6)

    p_ser = sub.add_parser("partial-series")
    p_ser.add_argument("--s", type=float, default=2.0)
    p_ser.add_argument("--limit", type=int, default=1000)

    args = parser.parse_args()
    if args.kind == "coefficient":
        result = explain(args.n)
    elif args.kind == "local":
        result = local_axis(args.p, args.max_k)
    else:
        result = {"s": args.s, "limit": args.limit, "partial_L_chi4": partial_l_series(args.s, args.limit), "asymptotic_inference_authorized": False}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
