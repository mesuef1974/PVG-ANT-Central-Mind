#!/usr/bin/env python3
"""Verify the reduced major/minor frequency split and its channel certificate."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d for d in range(2, math.isqrt(n) + 1))


def von_mangoldt(n: int) -> float:
    if n < 2:
        return 0.0
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0:
            if not is_prime(p):
                continue
            t = n
            while t % p == 0:
                t //= p
            return math.log(p) if t == 1 else 0.0
    return math.log(n)


def higher_prime_power_weight(n: int) -> float:
    if n < 4:
        return 0.0
    for p in range(2, math.isqrt(n) + 1):
        if not is_prime(p):
            continue
        t = p * p
        while t < n:
            t *= p
        if t == n:
            return math.log(p)
    return 0.0


def build_case(N: int, r: int):
    g = math.gcd(2, r)
    q = r // g
    u = 2 // g
    weights = [von_mangoldt(a) * von_mangoldt(N - a) for a in range(1, N)]

    channels = [0.0] * q
    hpp = [0.0] * q
    prime_prime = [0.0] * q

    for a, weight in enumerate(weights, 1):
        c = (u * a) % q
        channels[c] += weight
        hpp[c] += higher_prime_power_weight(a)
        if is_prime(a) and is_prime(N - a):
            prime_prime[c] += math.log(a) * math.log(N - a)

    spectrum = [
        sum(
            weights[a - 1] * cmath.exp(2j * math.pi * k * u * a / q)
            for a in range(1, N)
        )
        for k in range(q)
    ]
    contamination = [
        math.log(N) * (hpp[c] + hpp[(u * N - c) % q]) for c in range(q)
    ]
    return q, channels, spectrum, contamination, prime_prime


def main() -> None:
    tolerance = 1e-8
    K_values = (0, 1, 2, 3)
    summary = {
        "schema": "pvg.reduced-major-minor-frequency.verification.v1",
        "status": "PASS",
        "N_range": [2, 300],
        "r_range": [1, 20],
        "K_values": list(K_values),
        "channel_checks": 0,
        "bound_mismatches": 0,
        "certificate_counts": {str(k): 0 for k in K_values},
        "false_certificate_counts": {str(k): 0 for k in K_values},
        "prime_positive_channels": 0,
    }

    for N in range(2, 301):
        for r in range(1, 21):
            q, channels, spectrum, contamination, prime_prime = build_case(N, r)
            nonzero = list(range(1, q))
            ranked = sorted(nonzero, key=lambda k: abs(spectrum[k]), reverse=True)

            for c in range(q):
                if prime_prime[c] > tolerance:
                    summary["prime_positive_channels"] += 1

                for K in K_values:
                    major = set(ranked[: min(K, len(ranked))])
                    minor = [k for k in nonzero if k not in major]
                    major_term = sum(
                        spectrum[k] * cmath.exp(-2j * math.pi * k * c / q)
                        for k in major
                    ) / q
                    minor_exact = sum(
                        spectrum[k] * cmath.exp(-2j * math.pi * k * c / q)
                        for k in minor
                    ) / q
                    minor_bound = (
                        math.sqrt(len(minor))
                        * math.sqrt(sum(abs(spectrum[k]) ** 2 for k in minor))
                        / q
                        if minor
                        else 0.0
                    )
                    if abs(minor_exact) > minor_bound + tolerance:
                        summary["bound_mismatches"] += 1

                    lower = (
                        spectrum[0].real / q
                        + major_term.real
                        - minor_bound
                        - contamination[c]
                    )
                    if lower > tolerance:
                        summary["certificate_counts"][str(K)] += 1
                        if prime_prime[c] <= tolerance:
                            summary["false_certificate_counts"][str(K)] += 1
                    summary["channel_checks"] += 1

    if summary["bound_mismatches"]:
        summary["status"] = "FAIL"
    if any(summary["false_certificate_counts"].values()):
        summary["status"] = "FAIL"

    output = Path(__file__).resolve().parents[1] / "results" / "reduced_major_minor_frequency_split_verification_v1.2.json"
    output.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
