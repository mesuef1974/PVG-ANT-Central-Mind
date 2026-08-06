#!/usr/bin/env python3
"""Deterministic symbolic query harness for TKG-006.

This implements finite character calculations; it is not an asymptotic solver.
"""
from __future__ import annotations

import argparse
import cmath
import json
import math
from typing import Callable


def phi(q: int) -> int:
    return sum(1 for a in range(1, q + 1) if math.gcd(a, q) == 1)


def chi4(n: int) -> complex:
    r = n % 4
    if r % 2 == 0:
        return 0j
    return 1 + 0j if r == 1 else -1 + 0j


def principal(n: int, q: int) -> complex:
    return 1 + 0j if math.gcd(n, q) == 1 else 0j


def characters_mod_4() -> list[Callable[[int], complex]]:
    return [lambda n: principal(n, 4), chi4]


def residue_projector_mod4(n: int, a: int) -> complex:
    chars = characters_mod_4()
    return sum(c(n) * c(a).conjugate() for c in chars) / phi(4)


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


def factorization(n: int) -> dict[int, int]:
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


def von_mangoldt(n: int) -> float:
    fac = factorization(n)
    if len(fac) != 1:
        return 0.0
    return math.log(next(iter(fac)))


def psi_ap(x: int, q: int, a: int) -> float:
    return sum(von_mangoldt(n) for n in range(1, x + 1) if n % q == a % q)


def psi_twist_chi4(x: int) -> complex:
    return sum(von_mangoldt(n) * chi4(n) for n in range(1, x + 1))


def explain(n: int) -> dict:
    value = chi4(n)
    return {
        "n": n,
        "modulus": 4,
        "residue": n % 4,
        "gcd_with_modulus": math.gcd(n, 4),
        "chi4": value.real,
        "pvg_route": "decode labelled valuation vector -> reduce decoded integer modulo 4 -> evaluate character",
        "asymptotic_inference_authorized": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=["character", "projector", "psi-ap", "twist", "orthogonality"])
    parser.add_argument("--n", type=int, default=15)
    parser.add_argument("--a", type=int, default=1)
    parser.add_argument("--x", type=int, default=30)
    args = parser.parse_args()

    if args.kind == "character":
        result = explain(args.n)
    elif args.kind == "projector":
        result = {"n": args.n, "a": args.a, "q": 4, "projector": residue_projector_mod4(args.n, args.a).real}
    elif args.kind == "psi-ap":
        result = {"x": args.x, "q": 4, "a": args.a, "psi_ap": psi_ap(args.x, 4, args.a)}
    elif args.kind == "twist":
        z = psi_twist_chi4(args.x)
        result = {"x": args.x, "psi_chi4_real": z.real, "psi_chi4_imag": z.imag}
    else:
        chars = characters_mod_4()
        matrix = []
        units = [1, 3]
        for i, c1 in enumerate(chars):
            row = []
            for j, c2 in enumerate(chars):
                row.append(sum(c1(a) * c2(a).conjugate() for a in units).real)
            matrix.append(row)
        result = {"q": 4, "phi": 2, "orthogonality_matrix": matrix}
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
