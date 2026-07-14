#!/usr/bin/env python3
"""AVRG Pass 009: center each four-prime shift by its local singular series."""

from __future__ import annotations

import json
import math
import os

import numpy as np

from avrg_pass003 import fft_self_convolution, prime_sieve, twin_prime_constant
from avrg_pass008 import local_four_point_count


LIMIT_EXPONENT = int(os.environ.get("AVRG_LIMIT_EXPONENT", "19"))
MAX_SHIFT = int(os.environ.get("AVRG_MAX_SHIFT", "48"))
MAX_N = 2**LIMIT_EXPONENT - 1
AXIS_PRIMES = (3, 5, 7, 11)


def local_factor(prime: int, forbidden_count: np.ndarray | int) -> np.ndarray:
    return (1.0 - np.asarray(forbidden_count) / prime) / (1.0 - 1.0 / prime) ** 4


def build_data(primes: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    theta = np.zeros(MAX_N + 1, dtype=np.float64)
    for p_raw in primes:
        p = int(p_raw)
        theta[p] = math.log(p)

    goldbach_multiplier = np.ones(MAX_N + 1, dtype=np.float64)
    for p_raw in primes[primes > 2]:
        p = int(p_raw)
        goldbach_multiplier[p::p] *= (p - 1.0) / (p - 2.0)
    goldbach_singular = (
        2.0 * twin_prime_constant(primes) * goldbach_multiplier
    )

    correction_nu2 = np.ones(MAX_N + 1, dtype=np.float64)
    correction_nu3 = np.ones(MAX_N + 1, dtype=np.float64)
    log_base = 0.0
    for p_raw in primes[primes >= 5]:
        p = int(p_raw)
        g4 = float(local_factor(p, 4))
        g3 = float(local_factor(p, 3))
        g2 = float(local_factor(p, 2))
        log_base += math.log(g4)
        correction_nu2[p::p] *= g2 / g4
        correction_nu3[p::p] *= g3 / g4
    return (
        theta,
        goldbach_singular,
        np.stack(
            (
                correction_nu2,
                correction_nu3,
                np.full(MAX_N + 1, math.exp(log_base), dtype=np.float64),
            )
        ),
    )


def unique_prime_factors(number: int, primes: np.ndarray) -> list[int]:
    factors = []
    remaining = number
    for p_raw in primes:
        p = int(p_raw)
        if p * p > remaining:
            break
        if remaining % p == 0:
            factors.append(p)
            while remaining % p == 0:
                remaining //= p
        if remaining == 1:
            break
    if remaining > 1:
        factors.append(remaining)
    return factors


def small_prime_factor(targets: np.ndarray, shift: int, prime: int) -> np.ndarray:
    target_residue = targets % prime
    shift_residue = shift % prime
    forbidden_counts = np.empty(len(targets), dtype=np.int8)
    for residue in range(prime):
        count = prime - local_four_point_count(prime, residue, shift_residue)
        forbidden_counts[target_residue == residue] = count
    return local_factor(prime, forbidden_counts)


def quadruple_singular_series(
    targets: np.ndarray,
    shift: int,
    primes: np.ndarray,
    correction_nu2: np.ndarray,
    correction_nu3: np.ndarray,
    base_constant: float,
) -> np.ndarray:
    result = (
        base_constant
        * correction_nu2[targets]
        * correction_nu3[targets - shift]
        * correction_nu3[targets + shift]
    )

    for prime in unique_prime_factors(shift, primes):
        if prime < 5:
            continue
        g4 = float(local_factor(prime, 4))
        g3 = float(local_factor(prime, 3))
        g2 = float(local_factor(prime, 2))
        g1 = float(local_factor(prime, 1))
        divisible = targets % prime == 0
        current_when_divisible = g2 * g3 * g3 / (g4 * g4)
        result[divisible] *= g1 / current_when_divisible
        result[~divisible] *= g2 / g4

    result *= small_prime_factor(targets, shift, 2)
    result *= small_prime_factor(targets, shift, 3)
    return result


def shift_energy(theta: np.ndarray, targets: np.ndarray, shift: int) -> np.ndarray:
    pair = np.zeros_like(theta)
    pair[:-shift] = theta[:-shift] * theta[shift:]
    return fft_self_convolution(pair, MAX_N)[targets - shift]


def mean(values: np.ndarray) -> float:
    return float(np.mean(values))


def main() -> None:
    _, primes = prime_sieve(MAX_N + MAX_SHIFT)
    theta, goldbach_singular, correction_stack = build_data(primes[primes <= MAX_N])
    correction_nu2, correction_nu3, base_array = correction_stack
    base_constant = float(base_array[0])

    lo, hi = 2 ** (LIMIT_EXPONENT - 1), 2**LIMIT_EXPONENT
    # Keep N+h inside the precomputed multiplicative tables for every h tested.
    targets = np.arange(lo, hi - MAX_SHIFT, 2, dtype=np.int64)
    denominator = goldbach_singular[targets] * targets
    denominator_squared = denominator**2
    theta_convolution = fft_self_convolution(theta, MAX_N)
    theta_residual = theta_convolution[targets] / denominator - 1.0

    rows = {str(prime): [] for prime in AXIS_PRIMES}
    reconstruction_partial = {str(prime): {"on": 0.0, "off": 0.0} for prime in AXIS_PRIMES}

    for shift in range(2, MAX_SHIFT + 1, 2):
        energy = shift_energy(theta, targets, shift)
        singular4 = quadruple_singular_series(
            targets,
            shift,
            primes,
            correction_nu2,
            correction_nu3,
            base_constant,
        )
        main_term = singular4 * (targets - shift)
        admissible = singular4 > 0.0
        ratio_to_main = np.zeros(len(targets), dtype=np.float64)
        ratio_to_main[admissible] = energy[admissible] / main_term[admissible]
        centered_normalized = (energy - main_term) / denominator_squared

        for prime in AXIS_PRIMES:
            on = targets % prime == 0
            off = ~on
            kappa_diag = (prime - 2.0) / (prime - 1.0)
            on_centered = mean(centered_normalized[on])
            off_centered = mean(centered_normalized[off])
            axis_defect = 2.0 * (on_centered - kappa_diag * off_centered)
            reconstruction_partial[str(prime)]["on"] += 2.0 * on_centered
            reconstruction_partial[str(prime)]["off"] += 2.0 * off_centered
            rows[str(prime)].append(
                {
                    "shift": shift,
                    "shift_mod_prime": shift % prime,
                    "category": (
                        "r_divides_h" if shift % prime == 0 else "r_not_divide_h"
                    ),
                    "mean_ratio_energy_to_main_admissible": mean(
                        ratio_to_main[admissible]
                    ),
                    "mean_centered_normalized_on": on_centered,
                    "mean_centered_normalized_off": off_centered,
                    "axis_defect_contribution": axis_defect,
                }
            )

    summaries = {}
    for prime in AXIS_PRIMES:
        axis_rows = rows[str(prime)]
        on = targets % prime == 0
        off = ~on
        kappa_diag = (prime - 2.0) / (prime - 1.0)
        full_on = mean(theta_residual[on] ** 2)
        full_off = mean(theta_residual[off] ** 2)
        full_defect = full_on - kappa_diag * full_off
        categories = {}
        for category in ("r_divides_h", "r_not_divide_h"):
            selected = [row for row in axis_rows if row["category"] == category]
            defect_sum = sum(row["axis_defect_contribution"] for row in selected)
            categories[category] = {
                "shift_count": len(selected),
                "axis_defect_sum": defect_sum,
                "share_of_full_axis_defect": defect_sum / full_defect,
                "mean_energy_to_main": float(
                    np.mean(
                        [
                            row["mean_ratio_energy_to_main_admissible"]
                            for row in selected
                        ]
                    )
                ),
            }
        partial_on = reconstruction_partial[str(prime)]["on"]
        partial_off = reconstruction_partial[str(prime)]["off"]
        summaries[str(prime)] = {
            "kappa_diagonal": kappa_diag,
            "full_prime_only_mse_on": full_on,
            "full_prime_only_mse_off": full_off,
            "full_axis_defect": full_defect,
            "partial_centered_shift_sum_on": partial_on,
            "partial_centered_shift_sum_off": partial_off,
            "partial_axis_defect": partial_on - kappa_diag * partial_off,
            "partial_share_of_full_axis_defect": (
                (partial_on - kappa_diag * partial_off) / full_defect
            ),
            "categories": categories,
        }

    result = {
        "parameters": {
            "limit_exponent": LIMIT_EXPONENT,
            "window": [lo, hi - MAX_SHIFT],
            "max_shift": MAX_SHIFT,
            "even_shifts": [2, MAX_SHIFT],
            "axis_primes": AXIS_PRIMES,
        },
        "definitions": {
            "singular4": "product_p (1-nu_p(N,h)/p)/(1-1/p)^4",
            "shift_main": "singular4(N,h)*(N-h)",
            "centered_shift": "(C_h-shift_main)/(Goldbach_singular(N)*N)^2",
            "axis_defect": "2*(mean_on(centered_shift)-kappa_diag*mean_off(centered_shift))",
        },
        "base_constant_p_ge_5": base_constant,
        "rows": rows,
        "summaries": summaries,
    }
    output_name = (
        "avrg_pass009_results.json"
        if LIMIT_EXPONENT == 19 and MAX_SHIFT == 48
        else f"avrg_pass009_results_e{LIMIT_EXPONENT}_h{MAX_SHIFT}.json"
    )
    with open(output_name, "w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    print(json.dumps(summaries, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
