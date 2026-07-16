#!/usr/bin/env python3
"""Executable symbolic reasoning harness for TKG-002.

This module implements finite arithmetic-function reasoning. It is not a
language model and it does not authorize asymptotic conclusions.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Callable

ArithmeticFunction = Callable[[int], float]
ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "translation-knowledge-graph/registry/tkg-002-dirichlet-convolution-mobius-divisor-box.jsonl"


def load_records() -> list[dict]:
    return [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]


def factorization(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("n must be positive")
    out: dict[int, int] = {}
    d = 2
    m = n
    while d * d <= m:
        while m % d == 0:
            out[d] = out.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        out[m] = out.get(m, 0) + 1
    return out


def divisors(n: int) -> list[int]:
    fac = factorization(n)
    values = [1]
    for p, exponent in fac.items():
        values = [d * (p**e) for d in values for e in range(exponent + 1)]
    return sorted(values)


def valuation_vector(n: int) -> dict[int, int]:
    return factorization(n)


def divisor_box(n: int) -> list[dict]:
    alpha = valuation_vector(n)
    points: list[dict] = []
    for d in divisors(n):
        beta = valuation_vector(d)
        complement = {p: alpha[p] - beta.get(p, 0) for p in alpha if alpha[p] - beta.get(p, 0)}
        points.append({"d": d, "n_over_d": n // d, "beta": beta, "alpha_minus_beta": complement})
    return points


def epsilon(n: int) -> int:
    return 1 if n == 1 else 0


def one(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return 1


def identity(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return n


def mobius(n: int) -> int:
    fac = factorization(n)
    if any(exponent > 1 for exponent in fac.values()):
        return 0
    return -1 if len(fac) % 2 else 1


def log_function(n: int) -> float:
    return math.log(n)


def dirichlet_convolution(f: ArithmeticFunction, g: ArithmeticFunction, n: int) -> float:
    return sum(f(d) * g(n // d) for d in divisors(n))


def tau(n: int) -> int:
    return len(divisors(n))


def sigma(n: int) -> int:
    return sum(divisors(n))


def von_mangoldt(n: int) -> float:
    fac = factorization(n)
    if len(fac) != 1:
        return 0.0
    return math.log(next(iter(fac)))


def mobius_transform(F: ArithmeticFunction, n: int) -> float:
    return dirichlet_convolution(mobius, F, n)


def divisor_sum_transform(f: ArithmeticFunction, n: int) -> float:
    return dirichlet_convolution(one, f, n)


def named_function(name: str) -> ArithmeticFunction:
    table: dict[str, ArithmeticFunction] = {
        "epsilon": epsilon,
        "one": one,
        "mu": mobius,
        "id": identity,
        "log": log_function,
        "tau": tau,
        "sigma": sigma,
        "lambda": von_mangoldt,
    }
    try:
        return table[name.lower()]
    except KeyError as exc:
        raise ValueError(f"unknown arithmetic function: {name}") from exc


def explain_number(n: int) -> dict:
    fac = factorization(n)
    box = divisor_box(n)
    mu_one = dirichlet_convolution(mobius, one, n)
    mu_log = dirichlet_convolution(mobius, log_function, n)
    return {
        "n": n,
        "factorization": fac,
        "valuation_vector": fac,
        "divisor_box_cardinality": len(box),
        "divisor_box": box,
        "tau": tau(n),
        "sigma": sigma(n),
        "mu": mobius(n),
        "epsilon": epsilon(n),
        "mu_convolved_one": mu_one,
        "mu_convolved_log": mu_log,
        "lambda": von_mangoldt(n),
        "exact_checks": {
            "one_convolved_one_equals_tau": dirichlet_convolution(one, one, n) == tau(n),
            "one_convolved_id_equals_sigma": dirichlet_convolution(one, identity, n) == sigma(n),
            "mu_convolved_one_equals_epsilon": mu_one == epsilon(n),
            "mu_convolved_log_equals_lambda": math.isclose(mu_log, von_mangoldt(n), abs_tol=1e-12),
        },
        "translation": {
            "type": "EXACT_DIVISOR_BOX_REINDEXING",
            "preserves": ["divisor order", "complementary factor pairs", "finite convolution value"],
            "requires_for_exact_reverse": ["prime-labelled axes", "integer decoder"],
            "information_loss_if_only_box_shape_retained": ["prime labels", "integer magnitudes", "weighted sums such as sigma"],
        },
        "asymptotic_inference_authorized": False,
        "claim_ceiling": "Finite known identities and exact PVG reindexing only; no PNT, RH, or GRH progress.",
    }


def answer_query(kind: str, n: int, f_name: str | None = None, g_name: str | None = None) -> dict:
    if kind == "explain":
        return explain_number(n)
    if kind == "box":
        return {"n": n, "alpha": valuation_vector(n), "points": divisor_box(n)}
    if kind == "convolve":
        if not f_name or not g_name:
            raise ValueError("convolve requires --f and --g")
        f = named_function(f_name)
        g = named_function(g_name)
        return {
            "n": n,
            "f": f_name,
            "g": g_name,
            "value": dirichlet_convolution(f, g, n),
            "terms": [{"d": d, "n_over_d": n // d, "term": f(d) * g(n // d)} for d in divisors(n)],
        }
    raise ValueError(f"unknown query kind: {kind}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=["explain", "box", "convolve"], default="explain")
    parser.add_argument("--n", type=int, default=12)
    parser.add_argument("--f")
    parser.add_argument("--g")
    args = parser.parse_args()

    records = load_records()
    result = answer_query(args.kind, args.n, args.f, args.g)
    print(json.dumps({"registry_records": len(records), "result": result}, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
