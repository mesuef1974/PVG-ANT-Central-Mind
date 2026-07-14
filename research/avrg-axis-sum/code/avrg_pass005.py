#!/usr/bin/env python3
"""AVRG Research Pass 005: valuation-stratum residual diagnostics."""

from __future__ import annotations

import json
import math

import numpy as np

from avrg_pass003 import MAX_N, WINDOW_EXPONENTS, fft_self_convolution, prime_sieve, twin_prime_constant


def valuation_array(values: np.ndarray, prime: int) -> np.ndarray:
    """Return v_prime(n) elementwise for positive integer values."""
    work = values.copy()
    result = np.zeros(len(values), dtype=np.int16)
    divisible = work % prime == 0
    while np.any(divisible):
        result[divisible] += 1
        work[divisible] //= prime
        divisible = work % prime == 0
    return result


def stats(values: np.ndarray) -> dict[str, float | int]:
    return {
        "count": int(len(values)),
        "mean": float(np.mean(values)),
        "mean_square": float(np.mean(values**2)),
        "rms": float(math.sqrt(np.mean(values**2))),
        "std": float(np.std(values)),
        "q10": float(np.quantile(values, 0.10)),
        "q90": float(np.quantile(values, 0.90)),
    }


def grouped_stats(residual: np.ndarray, labels: np.ndarray, keep: list[int]) -> dict[str, dict]:
    return {str(label): stats(residual[labels == label]) for label in keep if np.any(labels == label)}


def main() -> None:
    _, primes = prime_sieve(MAX_N)
    c2 = twin_prime_constant(primes)

    von_mangoldt = np.zeros(MAX_N + 1, dtype=np.float64)
    chebyshev_theta = np.zeros(MAX_N + 1, dtype=np.float64)
    for p_raw in primes:
        p = int(p_raw)
        log_p = math.log(p)
        chebyshev_theta[p] = log_p
        power = p
        while power <= MAX_N:
            von_mangoldt[power] = log_p
            if power > MAX_N // p:
                break
            power *= p
    lambda_convolution = fft_self_convolution(von_mangoldt, MAX_N)
    theta_convolution = fft_self_convolution(chebyshev_theta, MAX_N)

    singular_multiplier = np.ones(MAX_N + 1, dtype=np.float64)
    for p_raw in primes[primes > 2]:
        p = int(p_raw)
        singular_multiplier[p::p] *= (p - 1.0) / (p - 2.0)
    singular_series = 2.0 * c2 * singular_multiplier

    windows = []
    for exponent in WINDOW_EXPONENTS:
        lo, hi = 2**exponent, 2 ** (exponent + 1)
        targets = np.arange(lo, hi, 2, dtype=np.int64)
        normalized = lambda_convolution[targets] / (singular_series[targets] * targets)
        residual = normalized - 1.0
        prime_only_residual = (
            theta_convolution[targets] / (singular_series[targets] * targets) - 1.0
        )

        v2 = valuation_array(targets, 2)
        v3 = valuation_array(targets, 3)
        v5 = valuation_array(targets, 5)
        v7 = valuation_array(targets, 7)
        v11 = valuation_array(targets, 11)
        joint_23 = 10 * np.minimum(v2, 5) + np.minimum(v3, 3)

        windows.append(
            {
                "exponent": exponent,
                "window": [lo, hi],
                "all_even": stats(residual),
                "prime_only_all_even": stats(prime_only_residual),
                "by_v2": grouped_stats(residual, v2, [1, 2, 3, 4, 5]),
                "by_v3": grouped_stats(residual, v3, [0, 1, 2, 3]),
                "prime_only_by_v3": grouped_stats(
                    prime_only_residual, v3, [0, 1, 2, 3]
                ),
                "by_v5": grouped_stats(residual, v5, [0, 1, 2, 3]),
                "prime_only_by_v5": grouped_stats(
                    prime_only_residual, v5, [0, 1, 2, 3]
                ),
                "by_v7": grouped_stats(residual, v7, [0, 1, 2]),
                "by_v11": grouped_stats(residual, v11, [0, 1, 2]),
                "by_joint_v2_v3": grouped_stats(
                    residual,
                    joint_23,
                    [10, 11, 12, 13, 20, 21, 22, 23, 30, 31, 32, 33],
                ),
            }
        )

    last = windows[-1]
    result = {
        "parameters": {
            "max_n": MAX_N,
            "window_exponents": WINDOW_EXPONENTS,
            "residual": "Lambda*Lambda(N)/(singular_series(N)*N)-1",
        },
        "exact_stratum_identity": {
            "v_r_equals_a": "union_{b=1}^{r-1} N congruent r^a*b (mod r^(a+1))",
            "multiple_axes_modulus": "product_i r_i^(a_i+1)",
        },
        "windows": windows,
        "first_to_last_all_even_rms": [
            windows[0]["all_even"]["rms"],
            windows[-1]["all_even"]["rms"],
        ],
        "last_window_digest": {
            "all_even": last["all_even"],
            "prime_only_all_even": last["prime_only_all_even"],
            "by_v2": last["by_v2"],
            "by_v3": last["by_v3"],
            "prime_only_by_v3": last["prime_only_by_v3"],
            "by_joint_v2_v3": last["by_joint_v2_v3"],
        },
    }

    with open("avrg_pass005_results.json", "w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    print(json.dumps(result["last_window_digest"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
