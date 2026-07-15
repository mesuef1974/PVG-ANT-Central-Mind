#!/usr/bin/env python3
"""Verify exact von Mangoldt additive-fiber identities.

Checks:
1. total channel mass equals R_Lambda(N);
2. difference-channel reflection symmetry;
3. nonzero support occurs only on prime-power pairs;
4. exact decomposition Lambda = Lambda_pr + Lambda_hpp;
5. the same decomposition holds coordinatewise in each channel.
"""

from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path


def smallest_prime_factor(n: int) -> int:
    if n % 2 == 0:
        return 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return p
        p += 2
    return n


def prime_power_data(n: int) -> tuple[int, int] | None:
    if n < 2:
        return None
    p = smallest_prime_factor(n)
    m = n
    k = 0
    while m % p == 0:
        m //= p
        k += 1
    if m == 1:
        return p, k
    return None


def von_mangoldt(n: int) -> float:
    pp = prime_power_data(n)
    return math.log(pp[0]) if pp else 0.0


def lambda_prime(n: int) -> float:
    pp = prime_power_data(n)
    if pp and pp[1] == 1:
        return math.log(pp[0])
    return 0.0


def lambda_hpp(n: int) -> float:
    pp = prime_power_data(n)
    if pp and pp[1] >= 2:
        return math.log(pp[0])
    return 0.0


def channel(N: int, r: int, left, right) -> dict[int, float]:
    out: dict[int, float] = defaultdict(float)
    for a in range(1, N):
        out[(2 * a - N) % r] += left(a) * right(N - a)
    return {d: out[d] for d in range(r)}


def verify(N_max: int = 200, r_max: int = 40) -> dict:
    tol = 1e-11
    mass_checks = symmetry_checks = support_checks = decomposition_checks = 0
    mismatches: list[dict] = []

    for N in range(2, N_max + 1):
        weights = [von_mangoldt(a) * von_mangoldt(N - a) for a in range(1, N)]
        total = sum(weights)

        for a, w in enumerate(weights, start=1):
            if w != 0.0:
                support_checks += 1
                if prime_power_data(a) is None or prime_power_data(N - a) is None:
                    mismatches.append({"type": "support", "N": N, "a": a})

            lhs = von_mangoldt(a) * von_mangoldt(N - a)
            rhs = (
                lambda_prime(a) * lambda_prime(N - a)
                + lambda_prime(a) * lambda_hpp(N - a)
                + lambda_hpp(a) * lambda_prime(N - a)
                + lambda_hpp(a) * lambda_hpp(N - a)
            )
            decomposition_checks += 1
            if abs(lhs - rhs) > tol:
                mismatches.append({"type": "point_decomposition", "N": N, "a": a})

        for r in range(1, r_max + 1):
            y = channel(N, r, von_mangoldt, von_mangoldt)
            mass_checks += 1
            if abs(sum(y.values()) - total) > tol:
                mismatches.append({"type": "mass", "N": N, "r": r})

            for d in range(r):
                symmetry_checks += 1
                if abs(y[d] - y[(-d) % r]) > tol:
                    mismatches.append({"type": "symmetry", "N": N, "r": r, "d": d})

            y_pp = channel(N, r, lambda_prime, lambda_prime)
            y_ph = channel(N, r, lambda_prime, lambda_hpp)
            y_hp = channel(N, r, lambda_hpp, lambda_prime)
            y_hh = channel(N, r, lambda_hpp, lambda_hpp)
            for d in range(r):
                lhs = y[d]
                rhs = y_pp[d] + y_ph[d] + y_hp[d] + y_hh[d]
                decomposition_checks += 1
                if abs(lhs - rhs) > tol:
                    mismatches.append({"type": "channel_decomposition", "N": N, "r": r, "d": d})

    return {
        "schema": "pvg.von-mangoldt-additive-fiber-verification.v1",
        "status": "PASS" if not mismatches else "FAIL",
        "N_range": [2, N_max],
        "r_range": [1, r_max],
        "mass_checks": mass_checks,
        "symmetry_checks": symmetry_checks,
        "support_checks": support_checks,
        "decomposition_checks": decomposition_checks,
        "mismatch_count": len(mismatches),
        "first_mismatches": mismatches[:20],
    }


if __name__ == "__main__":
    result = verify()
    output = Path(__file__).resolve().parents[1] / "results" / "von_mangoldt_additive_fiber_verification_v1.2.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
