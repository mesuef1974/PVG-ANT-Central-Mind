#!/usr/bin/env python3
"""AVRG Pass 008: local four-point counts and the spectrum of shifts h."""

from __future__ import annotations

import json
import math
import os

import numpy as np

from avrg_pass003 import fft_self_convolution, prime_sieve, twin_prime_constant


LIMIT_EXPONENT = int(os.environ.get("AVRG_LIMIT_EXPONENT", "19"))
MAX_SHIFT = int(os.environ.get("AVRG_MAX_SHIFT", "48"))
MAX_N = 2**LIMIT_EXPONENT - 1
PRIMES_TESTED = (3, 5, 7, 11)


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


def local_four_point_count(prime: int, target: int, shift: int) -> int:
    return sum(
        1
        for x in range(prime)
        if all(
            value % prime
            for value in (x, x + shift, target - x, target - x - shift)
        )
    )


def local_count_table(prime: int) -> list[list[int]]:
    return [
        [local_four_point_count(prime, target, shift) for shift in range(prime)]
        for target in range(prime)
    ]


def predicted_normalized_factor(prime: int, shift_mod_prime: int) -> float | None:
    if shift_mod_prime == 0:
        return (prime - 2.0) / (prime - 1.0)
    if prime == 3:
        return None
    return (prime - 2.0) ** 2 / ((prime - 1.0) * (prime - 3.0))


def shift_energy(theta: np.ndarray, targets: np.ndarray, shift: int) -> np.ndarray:
    shifted_pair = np.zeros_like(theta)
    if shift == 0:
        shifted_pair = theta**2
    else:
        shifted_pair[:-shift] = theta[:-shift] * theta[shift:]
    convolution = fft_self_convolution(shifted_pair, MAX_N)
    return convolution[targets - shift]


def summarize(values: list[float]) -> dict:
    array = np.asarray(values, dtype=np.float64)
    return {
        "count": int(len(array)),
        "mean": float(np.mean(array)),
        "median": float(np.median(array)),
        "min": float(np.min(array)),
        "max": float(np.max(array)),
    }


def main() -> None:
    _, primes = prime_sieve(MAX_N)
    theta, singular = build_theta_and_singular(primes)
    lo, hi = 2 ** (LIMIT_EXPONENT - 1), 2**LIMIT_EXPONENT
    targets = np.arange(lo, hi, 2, dtype=np.int64)
    denominator_squared = (singular[targets] * targets) ** 2

    axis_rows = {str(prime): [] for prime in PRIMES_TESTED}
    for shift in range(MAX_SHIFT + 1):
        normalized_energy = shift_energy(theta, targets, shift) / denominator_squared
        for prime in PRIMES_TESTED:
            on_mask = targets % prime == 0
            off_mean = float(np.mean(normalized_energy[~on_mask]))
            on_mean = float(np.mean(normalized_energy[on_mask]))
            measured = on_mean / off_mean if off_mean > 0.0 else None
            predicted = predicted_normalized_factor(prime, shift % prime)
            axis_rows[str(prime)].append(
                {
                    "shift": shift,
                    "shift_mod_prime": shift % prime,
                    "category": (
                        "diagonal"
                        if shift == 0
                        else ("r_divides_h" if shift % prime == 0 else "r_not_divide_h")
                    ),
                    "off_mean_energy": off_mean,
                    "on_mean_energy": on_mean,
                    "measured_on_over_off": measured,
                    "predicted_local_factor": predicted,
                    "measured_over_predicted": (
                        measured / predicted
                        if measured is not None and predicted is not None
                        else None
                    ),
                }
            )

    category_summary = {}
    for prime in PRIMES_TESTED:
        rows = axis_rows[str(prime)]
        categories = {}
        for category in ("diagonal", "r_divides_h", "r_not_divide_h"):
            selected = [row for row in rows if row["category"] == category]
            if not selected:
                continue
            measured_values = [
                row["measured_on_over_off"]
                for row in selected
                if row["measured_on_over_off"] is not None
            ]
            ratio_values = [
                row["measured_over_predicted"]
                for row in selected
                if row["measured_over_predicted"] is not None
            ]
            pooled_off = sum(row["off_mean_energy"] for row in selected)
            pooled_on = sum(row["on_mean_energy"] for row in selected)
            categories[category] = {
                "shifts": [row["shift"] for row in selected],
                "selected_shift_count": len(selected),
                "even_shift_count": sum(row["shift"] % 2 == 0 for row in selected),
                "positive_off_shift_count": len(measured_values),
                "measured_factor_summary": summarize(measured_values),
                "measured_over_predicted_summary": (
                    summarize(ratio_values) if ratio_values else None
                ),
                "pooled_on_over_off": pooled_on / pooled_off if pooled_off > 0 else None,
                "predicted_factor": selected[0]["predicted_local_factor"],
            }
        category_summary[str(prime)] = categories

    local_tables = {}
    for prime in PRIMES_TESTED:
        table = local_count_table(prime)
        local_tables[str(prime)] = {
            "matrix_rows_target_columns_shift": table,
            "sum_over_shifts_by_target": [sum(row) for row in table],
            "expected_sum_identity": {
                "target_zero": (prime - 1) ** 2,
                "target_nonzero": (prime - 2) ** 2,
            },
            "predicted_normalized_factor_h_zero": predicted_normalized_factor(prime, 0),
            "predicted_normalized_factor_h_nonzero": predicted_normalized_factor(
                prime, 1
            ),
        }

    result = {
        "parameters": {
            "limit_exponent": LIMIT_EXPONENT,
            "max_n": MAX_N,
            "window": [lo, hi],
            "max_shift": MAX_SHIFT,
            "primes_tested": PRIMES_TESTED,
            "weight": "theta(n)=log(n) on primes and zero otherwise",
        },
        "definitions": {
            "four_point_shift_energy": "sum_m theta(m)theta(m+h)theta(N-m)theta(N-m-h)",
            "normalized_energy": "four_point_shift_energy/(singular_series(N)*N)^2",
        },
        "local_tables": local_tables,
        "shift_rows": axis_rows,
        "category_summary": category_summary,
    }
    output_name = (
        "avrg_pass008_results.json"
        if LIMIT_EXPONENT == 19 and MAX_SHIFT == 48
        else f"avrg_pass008_results_e{LIMIT_EXPONENT}_h{MAX_SHIFT}.json"
    )
    with open(output_name, "w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    print(json.dumps(category_summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
