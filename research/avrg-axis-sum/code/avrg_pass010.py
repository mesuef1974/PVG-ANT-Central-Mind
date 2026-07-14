#!/usr/bin/env python3
"""AVRG Pass 010: stratified dyadic sampling of the centered shift spectrum."""

from __future__ import annotations

import json
import math
import os

import numpy as np

from avrg_pass003 import fft_self_convolution, prime_sieve
from avrg_pass009 import (
    AXIS_PRIMES,
    MAX_N,
    build_data,
    mean,
    quadruple_singular_series,
    shift_energy,
)


LIMIT_EXPONENT = int(os.environ.get("AVRG_LIMIT_EXPONENT", "19"))
SAMPLES_PER_BIN = int(os.environ.get("AVRG_SAMPLES_PER_BIN", "24"))
MAX_H_FRACTION = float(os.environ.get("AVRG_MAX_H_FRACTION", "0.5"))
SEED = int(os.environ.get("AVRG_SEED", "20260714"))


def even_count(lo: int, hi: int) -> int:
    first = lo if lo % 2 == 0 else lo + 1
    if first >= hi:
        return 0
    return (hi - 1 - first) // 2 + 1


def category_count(lo: int, hi: int, prime: int, divisible: bool) -> int:
    total = even_count(lo, hi)
    modulus = 2 * prime
    first = ((lo + modulus - 1) // modulus) * modulus
    multiples = 0 if first >= hi else (hi - 1 - first) // modulus + 1
    return multiples if divisible else total - multiples


def make_bins(max_h: int, rng: np.random.Generator) -> list[dict]:
    bins = []
    lo = 2
    while lo <= max_h:
        hi = min(2 * lo, max_h + 1)
        candidates = np.arange(lo + lo % 2, hi, 2, dtype=np.int64)
        size = min(SAMPLES_PER_BIN, len(candidates))
        if size:
            chosen = np.sort(rng.choice(candidates, size=size, replace=False))
            bins.append(
                {
                    "lo": lo,
                    "hi": hi,
                    "population_even_shifts": int(len(candidates)),
                    "sampled_shifts": [int(value) for value in chosen],
                }
            )
        lo = hi
    return bins


def main() -> None:
    if MAX_N != 2**LIMIT_EXPONENT - 1:
        raise RuntimeError("AVRG_LIMIT_EXPONENT must be set before importing this script")

    rng = np.random.default_rng(SEED)
    lo_x, hi_x = 2 ** (LIMIT_EXPONENT - 1), 2**LIMIT_EXPONENT
    max_h = int(lo_x * MAX_H_FRACTION)
    max_h -= max_h % 2
    bins = make_bins(max_h, rng)

    _, primes = prime_sieve(MAX_N + max_h)
    theta, goldbach_singular, correction_stack = build_data(primes[primes <= MAX_N])
    correction_nu2, correction_nu3, base_array = correction_stack
    base_constant = float(base_array[0])

    targets = np.arange(lo_x, hi_x - max_h, 2, dtype=np.int64)
    denominator = goldbach_singular[targets] * targets
    denominator_squared = denominator**2
    theta_convolution = fft_self_convolution(theta, MAX_N)
    theta_residual = theta_convolution[targets] / denominator - 1.0

    full = {}
    for prime in AXIS_PRIMES:
        on = targets % prime == 0
        off = ~on
        kappa = (prime - 2.0) / (prime - 1.0)
        full[str(prime)] = {
            "kappa_diagonal": kappa,
            "mse_on": mean(theta_residual[on] ** 2),
            "mse_off": mean(theta_residual[off] ** 2),
        }
        full[str(prime)]["axis_defect"] = (
            full[str(prime)]["mse_on"] - kappa * full[str(prime)]["mse_off"]
        )

    rows = []
    for bin_index, bin_data in enumerate(bins):
        for shift in bin_data["sampled_shifts"]:
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
            centered = (energy - main_term) / denominator_squared
            admissible = singular4 > 0
            row = {
                "bin_index": bin_index,
                "shift": shift,
                "u_at_window_midpoint": shift / (0.5 * (lo_x + hi_x - max_h)),
                "mean_energy_over_main_admissible": mean(
                    energy[admissible] / main_term[admissible]
                ),
                "axes": {},
            }
            for prime in AXIS_PRIMES:
                on = targets % prime == 0
                off = ~on
                kappa = full[str(prime)]["kappa_diagonal"]
                defect = 2.0 * (mean(centered[on]) - kappa * mean(centered[off]))
                row["axes"][str(prime)] = {
                    "category": (
                        "r_divides_h" if shift % prime == 0 else "r_not_divide_h"
                    ),
                    "axis_defect": defect,
                }
            rows.append(row)

    bin_estimates = {str(prime): [] for prime in AXIS_PRIMES}
    totals = {}
    for prime in AXIS_PRIMES:
        estimated_total = 0.0
        estimated_total_variance = 0.0
        estimated_by_category = {"r_divides_h": 0.0, "r_not_divide_h": 0.0}
        variance_by_category = {"r_divides_h": 0.0, "r_not_divide_h": 0.0}
        missing_strata = []
        for bin_index, bin_data in enumerate(bins):
            sampled = [row for row in rows if row["bin_index"] == bin_index]
            category_rows = {
                category: [
                    row["axes"][str(prime)]["axis_defect"]
                    for row in sampled
                    if row["axes"][str(prime)]["category"] == category
                ]
                for category in ("r_divides_h", "r_not_divide_h")
            }
            category_estimates = {}
            for category, values in category_rows.items():
                population = category_count(
                    bin_data["lo"],
                    bin_data["hi"],
                    prime,
                    divisible=(category == "r_divides_h"),
                )
                estimate = float(np.mean(values) * population) if values else None
                if len(values) >= 2 and population > 1:
                    sample_variance = float(np.var(values, ddof=1))
                    finite_population = max(population - len(values), 0) / (
                        population - 1
                    )
                    estimate_variance = (
                        population**2
                        * sample_variance
                        / len(values)
                        * finite_population
                    )
                elif len(values) == population:
                    estimate_variance = 0.0
                else:
                    estimate_variance = None
                category_estimates[category] = {
                    "sample_count": len(values),
                    "population_count": population,
                    "estimated_defect": estimate,
                    "estimated_standard_error": (
                        math.sqrt(estimate_variance)
                        if estimate_variance is not None
                        else None
                    ),
                }
                if estimate is not None:
                    estimated_total += estimate
                    estimated_by_category[category] += estimate
                else:
                    missing_strata.append([bin_index, category])
                if estimate_variance is not None:
                    estimated_total_variance += estimate_variance
                    variance_by_category[category] += estimate_variance
            bin_estimates[str(prime)].append(
                {
                    "bin_index": bin_index,
                    "h_range": [bin_data["lo"], bin_data["hi"]],
                    "u_range_at_window_midpoint": [
                        bin_data["lo"] / (0.5 * (lo_x + hi_x - max_h)),
                        bin_data["hi"] / (0.5 * (lo_x + hi_x - max_h)),
                    ],
                    "categories": category_estimates,
                }
            )

        defect = full[str(prime)]["axis_defect"]
        totals[str(prime)] = {
            **full[str(prime)],
            "estimated_sampled_spectrum_defect": estimated_total,
            "estimated_standard_error": math.sqrt(estimated_total_variance),
            "estimated_share_of_full_defect": estimated_total / defect,
            "standard_error_over_abs_full_defect": (
                math.sqrt(estimated_total_variance) / abs(defect)
            ),
            "missing_strata": missing_strata,
            "estimated_by_category": {
                category: {
                    "defect": value,
                    "share_of_full_defect": value / defect,
                    "standard_error": math.sqrt(variance_by_category[category]),
                }
                for category, value in estimated_by_category.items()
            },
        }

    result = {
        "parameters": {
            "limit_exponent": LIMIT_EXPONENT,
            "target_window": [lo_x, hi_x - max_h],
            "max_h": max_h,
            "max_h_fraction_of_lower_X": MAX_H_FRACTION,
            "samples_per_bin": SAMPLES_PER_BIN,
            "seed": SEED,
            "sampled_shift_count": len(rows),
        },
        "bins": bins,
        "rows": rows,
        "bin_estimates": bin_estimates,
        "totals": totals,
    }
    output_name = (
        f"avrg_pass010_results_e{LIMIT_EXPONENT}"
        f"_s{SAMPLES_PER_BIN}_u{MAX_H_FRACTION:g}.json"
    )
    with open(output_name, "w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    print(json.dumps(totals, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
