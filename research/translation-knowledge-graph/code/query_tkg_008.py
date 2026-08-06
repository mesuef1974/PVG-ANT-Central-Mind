#!/usr/bin/env python3
"""Deterministic TKG-008 conductor/induction query harness.

This is a symbolic finite model for selected characters, not a theorem prover.
"""
from __future__ import annotations

import argparse
import json
import math


def chi_trivial_mod1(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return 1


def chi_principal_mod4(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return 1 if n % 2 else 0


def chi4(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    if n % 2 == 0:
        return 0
    return 1 if n % 4 == 1 else -1


def induced_chi4_mod8(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    if math.gcd(n, 8) != 1:
        return 0
    return chi4(n)


def prime_factorization(n: int) -> dict[int, int]:
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


def von_mangoldt(n: int) -> float:
    fac = prime_factorization(n)
    return math.log(next(iter(fac))) if len(fac) == 1 else 0.0


def character_spec(name: str) -> dict:
    specs = {
        "principal4": {"modulus": 4, "conductor": 1, "primitive": "trivial1", "fn": chi_principal_mod4},
        "chi4": {"modulus": 4, "conductor": 4, "primitive": "chi4", "fn": chi4},
        "chi4mod8": {"modulus": 8, "conductor": 4, "primitive": "chi4", "fn": induced_chi4_mod8},
    }
    if name not in specs:
        raise ValueError(f"unknown character: {name}")
    return specs[name]


def extra_bad_primes(modulus: int, conductor: int) -> list[int]:
    q_primes = set(prime_factorization(modulus))
    f_primes = set(prime_factorization(conductor)) if conductor > 1 else set()
    return sorted(q_primes - f_primes)


def explain_character(name: str) -> dict:
    spec = character_spec(name)
    extra = extra_bad_primes(spec["modulus"], spec["conductor"])
    return {
        "character": name,
        "modulus": spec["modulus"],
        "conductor": spec["conductor"],
        "primitive_source": spec["primitive"],
        "extra_bad_primes": extra,
        "translation": "primitive residue phase plus finite axis masks",
        "claim_ceiling": "No PNT-AP, RH, or GRH inference is authorized.",
    }


def coefficient(name: str, n: int) -> dict:
    spec = character_spec(name)
    value = spec["fn"](n)
    lam = von_mangoldt(n)
    return {
        "character": name,
        "n": n,
        "factorization": prime_factorization(n),
        "chi": value,
        "lambda": lam,
        "twisted_mangoldt": lam * value,
        "masked_by_induced_modulus": bool(lam and value == 0),
        "asymptotic_inference_authorized": False,
    }


def compare(name: str, limit: int) -> dict:
    spec = character_spec(name)
    if name == "principal4":
        primitive_fn = chi_trivial_mod1
    else:
        primitive_fn = chi4
    diffs = []
    for n in range(1, limit + 1):
        induced = spec["fn"](n)
        primitive = primitive_fn(n)
        if induced != primitive:
            diffs.append({"n": n, "primitive": primitive, "induced": induced, "factorization": prime_factorization(n)})
    return {"character": name, "limit": limit, "differences": diffs, "extra_bad_primes": extra_bad_primes(spec["modulus"], spec["conductor"])}


def partial_l_series(name: str, s: float, limit: int) -> dict:
    if s <= 1:
        raise ValueError("this governed finite approximation requires s>1")
    spec = character_spec(name)
    value = sum(spec["fn"](n) / (n**s) for n in range(1, limit + 1))
    return {"character": name, "s": s, "limit": limit, "partial_sum": value, "analytic_continuation_claimed": False}


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="kind", required=True)
    p = sub.add_parser("explain")
    p.add_argument("--character", choices=["principal4", "chi4", "chi4mod8"], required=True)
    p = sub.add_parser("coefficient")
    p.add_argument("--character", choices=["principal4", "chi4", "chi4mod8"], required=True)
    p.add_argument("--n", type=int, required=True)
    p = sub.add_parser("compare")
    p.add_argument("--character", choices=["principal4", "chi4mod8"], required=True)
    p.add_argument("--limit", type=int, default=40)
    p = sub.add_parser("partial-series")
    p.add_argument("--character", choices=["principal4", "chi4", "chi4mod8"], required=True)
    p.add_argument("--s", type=float, default=2.0)
    p.add_argument("--limit", type=int, default=1000)
    args = parser.parse_args()

    if args.kind == "explain":
        result = explain_character(args.character)
    elif args.kind == "coefficient":
        result = coefficient(args.character, args.n)
    elif args.kind == "compare":
        result = compare(args.character, args.limit)
    else:
        result = partial_l_series(args.character, args.s, args.limit)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
