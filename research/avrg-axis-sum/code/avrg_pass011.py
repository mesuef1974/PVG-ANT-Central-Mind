#!/usr/bin/env python3
"""AVRG Pass 011: exact centered residue-class energy decomposition."""

from __future__ import annotations

import json
import math
import os

import numpy as np

from avrg_pass003 import fft_self_convolution, prime_sieve, twin_prime_constant


LIMIT_EXPONENT = int(os.environ.get("AVRG_LIMIT_EXPONENT", "21"))
MAX_N = 2**LIMIT_EXPONENT - 1
AXIS_PRIMES = (3, 5, 7, 11)


def build_theta_and_singular(primes: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    theta = np.zeros(MAX_N + 1, dtype=np.float64)
    for p_raw in primes:
        p = int(p_raw)
        theta[p] = math.log(p)
    multiplier = np.ones(MAX_N + 1, dtype=np.float64)
    for p_raw in primes[primes > 2]:
        p = int(p_raw)
        multiplier[p::p] *= (p - 1.0) / (p - 2.0)
    singular = 2.0 * twin_prime_constant(primes) * multiplier
    return theta, singular


def group_mean(values: np.ndarray, mask: np.ndarray) -> float:
    return float(np.mean(values[mask]))


def fft_convolution(left: np.ndarray, right: np.ndarray, max_index: int) -> np.ndarray:
    size = 1
    while size < len(left) + len(right):
        size *= 2
    left_spectrum = np.fft.rfft(left, size)
    right_spectrum = np.fft.rfft(right, size)
    convolution = np.fft.irfft(left_spectrum * right_spectrum, size)
    return convolution[: max_index + 1]


def main() -> None:
    _, primes = prime_sieve(MAX_N)
    theta, singular = build_theta_and_singular(primes)
    total_convolution = fft_self_convolution(theta, MAX_N)

    lo, hi = 2 ** (LIMIT_EXPONENT - 1), 2**LIMIT_EXPONENT
    targets = np.arange(lo, hi, 2, dtype=np.int64)
    main_term = singular[targets] * targets
    prime_residual = total_convolution[targets] / main_term - 1.0

    axes = {}
    for prime in AXIS_PRIMES:
        target_residue = targets % prime
        allowed_count = np.where(target_residue == 0, prime - 1, prime - 2)
        sum_z = np.zeros(len(targets), dtype=np.float64)
        sum_z_squared = np.zeros(len(targets), dtype=np.float64)
        reconstructed_raw = np.zeros(len(targets), dtype=np.float64)

        integers = np.arange(MAX_N + 1, dtype=np.int64)
        for residue in range(prime):
            restricted = np.where(integers % prime == residue, theta, 0.0)
            class_convolution = fft_convolution(restricted, theta, MAX_N)[targets]
            allowed = (residue != 0) & ((target_residue - residue) % prime != 0)
            expected = np.where(allowed, main_term / allowed_count, 0.0)
            centered = class_convolution - expected
            reconstructed_raw += class_convolution
            sum_z += centered
            sum_z_squared += centered**2

        within = sum_z_squared / main_term**2
        total_from_vector = (sum_z / main_term) ** 2
        between = total_from_vector - within
        on = target_residue == 0
        off = ~on
        kappa_diagonal = (prime - 2.0) / (prime - 1.0)

        components = {}
        for name, values in (
            ("total", total_from_vector),
            ("within_classes", within),
            ("between_classes", between),
        ):
            mean_on = group_mean(values, on)
            mean_off = group_mean(values, off)
            components[name] = {
                "mean_on": mean_on,
                "mean_off": mean_off,
                "on_over_off": mean_on / mean_off,
                "axis_defect": mean_on - kappa_diagonal * mean_off,
            }

        total_defect = components["total"]["axis_defect"]
        components["within_classes"]["share_of_total_axis_defect"] = (
            components["within_classes"]["axis_defect"] / total_defect
        )
        components["between_classes"]["share_of_total_axis_defect"] = (
            components["between_classes"]["axis_defect"] / total_defect
        )

        axes[str(prime)] = {
            "kappa_diagonal": kappa_diagonal,
            "components": components,
            "checks": {
                "max_abs_raw_reconstruction_error": float(
                    np.max(np.abs(reconstructed_raw - total_convolution[targets]))
                ),
                "max_abs_residual_reconstruction_error": float(
                    np.max(np.abs(sum_z / main_term - prime_residual))
                ),
                "max_abs_energy_reconstruction_error": float(
                    np.max(np.abs(within + between - prime_residual**2))
                ),
                "defect_share_sum": (
                    components["within_classes"]["share_of_total_axis_defect"]
                    + components["between_classes"]["share_of_total_axis_defect"]
                ),
            },
        }

    result = {
        "parameters": {
            "limit_exponent": LIMIT_EXPONENT,
            "window": [lo, hi],
            "axis_primes": AXIS_PRIMES,
            "weight": "theta(n)=log(n) on primes",
        },
        "definitions": {
            "R_r_a": "sum_{m=a mod r} theta(m)theta(N-m)",
            "Z_r_a": "R_r_a-main(N)/A_r(N) on locally allowed classes",
            "within": "sum_a Z_r_a^2/main(N)^2",
            "between": "sum_{a!=b} Z_r_a Z_r_b/main(N)^2",
            "total": "within+between=(theta*theta/main-1)^2",
        },
        "axes": axes,
    }
    output_name = (
        "avrg_pass011_results.json"
        if LIMIT_EXPONENT == 21
        else f"avrg_pass011_results_to_2pow{LIMIT_EXPONENT}.json"
    )
    with open(output_name, "w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    print(json.dumps(axes, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
