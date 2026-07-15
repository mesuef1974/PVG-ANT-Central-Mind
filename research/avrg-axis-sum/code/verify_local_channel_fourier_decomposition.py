#!/usr/bin/env python3
"""Verify local-channel Fourier decomposition for von Mangoldt addition fibers.

Checks finite Fourier inversion, reality, reflection, Parseval, the exact local
prime certificate, and a conservative certificate obtained from the l1 bound
on nonzero Fourier coefficients.
"""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

MAX_N = 500
MAX_R = 25
TOL = 1e-8


def smallest_prime_factors(limit: int) -> list[int]:
    spf = list(range(limit + 1))
    for p in range(2, math.isqrt(limit) + 1):
        if spf[p] == p:
            for n in range(p * p, limit + 1, p):
                if spf[n] == n:
                    spf[n] = p
    return spf


SPF = smallest_prime_factors(MAX_N)


def is_prime(n: int) -> bool:
    return n >= 2 and SPF[n] == n


def von_mangoldt(n: int) -> float:
    if n < 2:
        return 0.0
    p = SPF[n]
    m = n
    while m % p == 0:
        m //= p
    return math.log(p) if m == 1 else 0.0


def is_higher_prime_power(n: int) -> bool:
    return n >= 4 and von_mangoldt(n) > 0.0 and not is_prime(n)


def run() -> dict[str, object]:
    counts = {
        "channel_checks": 0,
        "inversion_mismatches": 0,
        "reality_mismatches": 0,
        "reflection_mismatches": 0,
        "parseval_mismatches": 0,
        "exact_certificate_count": 0,
        "exact_false_certificates": 0,
        "uniform_certificate_count": 0,
        "uniform_false_certificates": 0,
        "prime_positive_channels": 0,
    }
    max_inversion_error = 0.0
    max_imaginary_part = 0.0
    max_parseval_error = 0.0

    for N in range(2, MAX_N + 1):
        indices = list(range(1, N))
        weights = [von_mangoldt(a) * von_mangoldt(N - a) for a in indices]
        total_mass = sum(weights)

        for r in range(1, MAX_R + 1):
            channel = [0.0] * r
            prime_channel = [0.0] * r
            higher_power_mass = [0.0] * r

            for a, weight in zip(indices, weights):
                d = (2 * a - N) % r
                channel[d] += weight
                if is_prime(a) and is_prime(N - a):
                    prime_channel[d] += math.log(a) * math.log(N - a)
                if is_higher_prime_power(a):
                    higher_power_mass[d] += von_mangoldt(a)

            fourier = []
            for h in range(r):
                coefficient = sum(
                    weight
                    * cmath.exp(2j * math.pi * h * ((2 * a - N) % r) / r)
                    for a, weight in zip(indices, weights)
                )
                fourier.append(coefficient)
                max_imaginary_part = max(max_imaginary_part, abs(coefficient.imag))
                if abs(coefficient.imag) > TOL:
                    counts["reality_mismatches"] += 1

            parseval_left = sum(value * value for value in channel)
            parseval_right = sum(abs(value) ** 2 for value in fourier) / r
            parseval_error = abs(parseval_left - parseval_right)
            max_parseval_error = max(max_parseval_error, parseval_error)
            if parseval_error > 1e-6:
                counts["parseval_mismatches"] += 1

            nonzero_l1_bound = (
                sum(abs(fourier[h]) for h in range(1, r)) / r if r > 1 else 0.0
            )

            for d in range(r):
                reconstructed = sum(
                    fourier[h] * cmath.exp(-2j * math.pi * h * d / r)
                    for h in range(r)
                ) / r
                inversion_error = abs(reconstructed.real - channel[d]) + abs(
                    reconstructed.imag
                )
                max_inversion_error = max(max_inversion_error, inversion_error)
                counts["channel_checks"] += 1
                if inversion_error > 1e-6:
                    counts["inversion_mismatches"] += 1

                if abs(channel[d] - channel[(-d) % r]) > TOL:
                    counts["reflection_mismatches"] += 1

                contamination_bound = math.log(N) * (
                    higher_power_mass[d] + higher_power_mass[(-d) % r]
                )
                deviation = channel[d] - total_mass / r

                if prime_channel[d] > TOL:
                    counts["prime_positive_channels"] += 1

                if total_mass / r + deviation > contamination_bound + TOL:
                    counts["exact_certificate_count"] += 1
                    if prime_channel[d] <= TOL:
                        counts["exact_false_certificates"] += 1

                if total_mass / r > nonzero_l1_bound + contamination_bound + TOL:
                    counts["uniform_certificate_count"] += 1
                    if prime_channel[d] <= TOL:
                        counts["uniform_false_certificates"] += 1

    return {
        "schema": "pvg.local-channel-fourier-verification.v1",
        "status": "PASS"
        if not any(
            counts[key]
            for key in (
                "inversion_mismatches",
                "reality_mismatches",
                "reflection_mismatches",
                "parseval_mismatches",
                "exact_false_certificates",
                "uniform_false_certificates",
            )
        )
        else "FAIL",
        "N_range": [2, MAX_N],
        "modulus_range": [1, MAX_R],
        **counts,
        "max_inversion_error": max_inversion_error,
        "max_fourier_imaginary_part": max_imaginary_part,
        "max_parseval_error": max_parseval_error,
        "uniform_bound": "B=(1/r) sum_{h != 0} |Yhat(h)|",
    }


if __name__ == "__main__":
    result = run()
    output = Path(__file__).resolve().parents[1] / "results" / (
        "local_channel_fourier_decomposition_verification_v1.2.json"
    )
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
