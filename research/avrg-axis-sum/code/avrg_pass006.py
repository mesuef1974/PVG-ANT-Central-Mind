#!/usr/bin/env python3
"""AVRG Research Pass 006: local support factors and axis interactions."""

from __future__ import annotations

import json
import math
import os

import numpy as np

from avrg_pass003 import fft_self_convolution, prime_sieve, twin_prime_constant
from avrg_pass005 import stats, valuation_array


LOCAL_PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
JOINT_PRIMES = (3, 5, 7, 11)
LIMIT_EXPONENT = int(os.environ.get("AVRG_LIMIT_EXPONENT", "21"))
MAX_N_RUN = 2**LIMIT_EXPONENT - 1
WINDOW_EXPONENTS_RUN = list(range(10, LIMIT_EXPONENT))


def mse(values: np.ndarray) -> float:
    return float(np.mean(values**2))


def safe_stats(values: np.ndarray) -> dict:
    if len(values) == 0:
        return {
            "count": 0,
            "mean": None,
            "mean_square": None,
            "rms": None,
            "std": None,
            "q10": None,
            "q90": None,
        }
    return stats(values)


def build_representation_data(primes: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    von_mangoldt = np.zeros(MAX_N_RUN + 1, dtype=np.float64)
    for p_raw in primes:
        p = int(p_raw)
        log_p = math.log(p)
        power = p
        while power <= MAX_N_RUN:
            von_mangoldt[power] = log_p
            if power > MAX_N_RUN // p:
                break
            power *= p
    convolution = fft_self_convolution(von_mangoldt, MAX_N_RUN)

    singular_multiplier = np.ones(MAX_N_RUN + 1, dtype=np.float64)
    for p_raw in primes[primes > 2]:
        p = int(p_raw)
        singular_multiplier[p::p] *= (p - 1.0) / (p - 2.0)
    singular_series = 2.0 * twin_prime_constant(primes) * singular_multiplier
    return convolution, singular_series


def local_axis_result(residual: np.ndarray, valuations: np.ndarray, prime: int) -> dict:
    off = residual[valuations == 0]
    on = residual[valuations >= 1]
    by_depth = {
        str(depth): stats(residual[valuations == depth])
        for depth in (0, 1, 2, 3)
        if np.any(valuations == depth)
    }
    empirical = mse(on) / mse(off)
    poisson = (prime - 2.0) / (prime - 1.0)
    return {
        "off": stats(off),
        "on": stats(on),
        "by_depth": by_depth,
        "kappa_empirical": empirical,
        "kappa_poisson_local": poisson,
        "empirical_over_poisson": empirical / poisson,
        "depth_2_over_depth_1": (
            by_depth["2"]["mean_square"] / by_depth["1"]["mean_square"]
            if "2" in by_depth
            else None
        ),
    }


def joint_result(residual: np.ndarray, valuation_map: dict[int, np.ndarray]) -> dict:
    masks = np.zeros(len(residual), dtype=np.int16)
    for bit, prime in enumerate(JOINT_PRIMES):
        masks |= ((valuation_map[prime] >= 1).astype(np.int16) << bit)

    raw = {}
    for mask in range(1 << len(JOINT_PRIMES)):
        values = residual[masks == mask]
        raw[str(mask)] = {
            "support": [
                prime for bit, prime in enumerate(JOINT_PRIMES) if mask & (1 << bit)
            ],
            **safe_stats(values),
        }

    base_mse = raw["0"]["mean_square"]
    single_factor = {
        str(prime): raw[str(1 << bit)]["mean_square"] / base_mse
        for bit, prime in enumerate(JOINT_PRIMES)
    }

    comparisons = {}
    for mask in range(1 << len(JOINT_PRIMES)):
        support = raw[str(mask)]["support"]
        actual_mse = raw[str(mask)]["mean_square"]
        actual = actual_mse / base_mse if actual_mse is not None else None
        predicted = math.prod(single_factor[str(prime)] for prime in support)
        comparisons[str(mask)] = {
            "support": support,
            "count": raw[str(mask)]["count"],
            "actual_ratio_to_empty": actual,
            "factorized_prediction": predicted,
            "interaction_quotient": actual / predicted if actual is not None else None,
            "relative_factorization_error": (
                actual / predicted - 1.0 if actual is not None else None
            ),
        }

    multi = [
        row
        for row in comparisons.values()
        if len(row["support"]) >= 2 and row["count"] >= 100
    ]
    return {
        "primes": JOINT_PRIMES,
        "raw": raw,
        "single_factors_conditional_on_other_axes_absent": single_factor,
        "comparisons": comparisons,
        "multi_axis_summary": {
            "eligible_patterns": len(multi),
            "max_abs_relative_error": (
                float(max(abs(row["relative_factorization_error"]) for row in multi))
                if multi
                else None
            ),
            "mean_abs_relative_error": (
                float(np.mean([abs(row["relative_factorization_error"]) for row in multi]))
                if multi
                else None
            ),
        },
    }


def main() -> None:
    _, primes = prime_sieve(MAX_N_RUN)
    convolution, singular_series = build_representation_data(primes)

    windows = []
    for exponent in WINDOW_EXPONENTS_RUN:
        lo, hi = 2**exponent, 2 ** (exponent + 1)
        targets = np.arange(lo, hi, 2, dtype=np.int64)
        residual = convolution[targets] / (singular_series[targets] * targets) - 1.0
        valuation_map = {
            prime: valuation_array(targets, prime) for prime in LOCAL_PRIMES
        }
        local = {
            str(prime): local_axis_result(residual, valuation_map[prime], prime)
            for prime in LOCAL_PRIMES
        }
        joint = joint_result(residual, valuation_map)
        windows.append(
            {
                "exponent": exponent,
                "window": [lo, hi],
                "all_even": stats(residual),
                "local_axes": local,
                "joint_axes": joint,
            }
        )

    last = windows[-1]
    last_local_digest = {
        prime: {
            "kappa_empirical": last["local_axes"][str(prime)]["kappa_empirical"],
            "kappa_poisson_local": last["local_axes"][str(prime)][
                "kappa_poisson_local"
            ],
            "empirical_over_poisson": last["local_axes"][str(prime)][
                "empirical_over_poisson"
            ],
            "depth_2_over_depth_1": last["local_axes"][str(prime)][
                "depth_2_over_depth_1"
            ],
        }
        for prime in LOCAL_PRIMES
    }
    result = {
        "parameters": {
            "max_n": MAX_N_RUN,
            "window_exponents": WINDOW_EXPONENTS_RUN,
            "local_primes": LOCAL_PRIMES,
            "joint_primes": JOINT_PRIMES,
            "residual": "Lambda*Lambda(N)/(singular_series(N)*N)-1",
        },
        "model": {
            "poisson_local_kappa": "(r-2)/(r-1)",
            "factorization_test": "V(S)/V(empty) versus product_r V({r})/V(empty), with all other tested axes absent",
        },
        "windows": windows,
        "last_window_local_digest": last_local_digest,
        "last_window_joint_digest": last["joint_axes"]["comparisons"],
        "last_window_joint_summary": last["joint_axes"]["multi_axis_summary"],
    }
    output_name = (
        "avrg_pass006_results.json"
        if LIMIT_EXPONENT == 21
        else f"avrg_pass006_results_to_2pow{LIMIT_EXPONENT}.json"
    )
    with open(output_name, "w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
    print(json.dumps({
        "local": last_local_digest,
        "joint_summary": result["last_window_joint_summary"],
        "joint": result["last_window_joint_digest"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
