#!/usr/bin/env python3
"""PASS023: multi-window and larger-modulus stability of AVRG energy ratios.

The computation uses one representative from each conjugate pair of even,
nonprincipal Dirichlet characters.  It compares

    mean_ratio(r) = 2 + c/r

with the free-intercept model

    mean_ratio(r) = a + c/r.

All conclusions are finite computational diagnostics, not asymptotic proofs.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
import time
from pathlib import Path
from typing import Sequence

import numpy as np


DEFAULT_EXPS = (15, 16, 17, 18)
DEFAULT_MODULI = (5, 7, 11, 13, 17, 19, 23, 29, 31)


def sieve_theta(n: int) -> np.ndarray:
    is_prime = np.ones(n + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if is_prime[p]:
            is_prime[p * p : n + 1 : p] = False
    theta = np.zeros(n + 1, dtype=float)
    primes = np.flatnonzero(is_prime)
    theta[primes] = np.log(primes)
    return theta


def singular_main(n_max: int) -> np.ndarray:
    """Hardy--Littlewood main term used unchanged in PASS013--PASS021."""
    c2 = 0.6601618158468696
    is_prime = np.ones(n_max + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, math.isqrt(n_max) + 1):
        if is_prime[p]:
            is_prime[p * p : n_max + 1 : p] = False
    factor = np.ones(n_max + 1, dtype=float)
    for p in np.flatnonzero(is_prime)[1:]:
        factor[p::p] *= (p - 1) / (p - 2)
    n = np.arange(n_max + 1)
    result = np.zeros(n_max + 1, dtype=float)
    even = (n >= 4) & (n % 2 == 0)
    result[even] = 2 * c2 * n[even] * factor[even]
    return result


def primitive_root(p: int) -> int:
    for g in range(2, p):
        if len({pow(g, exponent, p) for exponent in range(p - 1)}) == p - 1:
            return g
    raise ValueError(f"No primitive root found for {p}")


def discrete_log_table(p: int) -> np.ndarray:
    table = np.full(p, -1, dtype=np.int64)
    g = primitive_root(p)
    value = 1
    for exponent in range(p - 1):
        table[value] = exponent
        value = value * g % p
    return table


def character_values(
    p: int, k: int, residues: np.ndarray, log_table: np.ndarray
) -> np.ndarray:
    exponents = log_table[residues]
    unit = exponents >= 0
    values = np.zeros(residues.shape, dtype=np.complex128)
    values[unit] = np.exp(2j * np.pi * k * exponents[unit] / (p - 1))
    return values


def representative_modes(r: int) -> list[int]:
    """Even nonprincipal k, one from each k <-> r-1-k orbit."""
    return [k for k in range(2, r - 1, 2) if k <= r - 1 - k]


def population_sd(values: Sequence[float]) -> float:
    mean = statistics.fmean(values)
    return math.sqrt(statistics.fmean((value - mean) ** 2 for value in values))


def ols_free(xs: Sequence[float], ys: Sequence[float]) -> dict:
    xbar = statistics.fmean(xs)
    ybar = statistics.fmean(ys)
    sxx = sum((x - xbar) ** 2 for x in xs)
    slope = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / sxx
    intercept = ybar - slope * xbar
    predictions = [intercept + slope * x for x in xs]
    residuals = [y - prediction for y, prediction in zip(ys, predictions)]
    sse = sum(value * value for value in residuals)
    sst = sum((y - ybar) ** 2 for y in ys)
    df = len(xs) - 2
    result = {
        "intercept": intercept,
        "slope": slope,
        "sse": sse,
        "rmse": math.sqrt(sse / len(xs)),
        "r_squared": 1.0 - sse / sst if sst else 0.0,
        "residual_degrees_of_freedom": df,
    }
    if df > 0:
        residual_variance = sse / df
        intercept_se = math.sqrt(
            residual_variance * (1.0 / len(xs) + xbar * xbar / sxx)
        )
        result["intercept_standard_error"] = intercept_se
    # All default PASS023 fits use n=9 and residual df=7.
    if df == 7:
        critical = 2.3646242515927844
        result["intercept_classical_95_percent_ci"] = [
            intercept - critical * intercept_se,
            intercept + critical * intercept_se,
        ]
    return result


def threshold_sensitivity(per_modulus: Sequence[dict]) -> list[dict]:
    """Inspect how small moduli influence the candidate limit."""
    available = [row["r"] for row in per_modulus]
    thresholds = [value for value in (5, 7, 11, 13, 17, 19, 23) if value in available]
    output: list[dict] = []
    for minimum_r in thresholds:
        local = [row for row in per_modulus if row["r"] >= minimum_r]
        if len(local) < 3:
            continue
        xs = [1.0 / row["r"] for row in local]
        ys = [row["mean_ratio"] for row in local]
        free = ols_free(xs, ys)
        fixed = fit_fixed_two(xs, ys)
        output.append(
            {
                "minimum_r": minimum_r,
                "modulus_count": len(local),
                "moduli": [row["r"] for row in local],
                "mean_of_modulus_means": statistics.fmean(ys),
                "mean_absolute_deviation_from_two": statistics.fmean(
                    abs(value - 2.0) for value in ys
                ),
                "free_intercept": free["intercept"],
                "free_slope": free["slope"],
                "fixed_slope": fixed["slope"],
                "fixed_sse_over_free_sse": fixed["sse"] / free["sse"],
            }
        )
    return output


def fit_fixed_two(xs: Sequence[float], ys: Sequence[float]) -> dict:
    slope = sum(x * (y - 2.0) for x, y in zip(xs, ys)) / sum(
        x * x for x in xs
    )
    residuals = [y - (2.0 + slope * x) for x, y in zip(xs, ys)]
    sse = sum(value * value for value in residuals)
    return {
        "intercept": 2.0,
        "slope": slope,
        "sse": sse,
        "rmse": math.sqrt(sse / len(xs)),
    }


def aicc(sse: float, n: int, parameter_count: int) -> float:
    if sse <= 0 or n <= parameter_count + 1:
        return float("-inf")
    base = n * math.log(sse / n) + 2 * parameter_count
    correction = (
        2 * parameter_count * (parameter_count + 1)
        / (n - parameter_count - 1)
    )
    return base + correction


def loocv(xs: Sequence[float], ys: Sequence[float], fixed_two: bool) -> dict:
    residuals: list[float] = []
    for omitted in range(len(xs)):
        train_x = [x for index, x in enumerate(xs) if index != omitted]
        train_y = [y for index, y in enumerate(ys) if index != omitted]
        if fixed_two:
            fit = fit_fixed_two(train_x, train_y)
        else:
            fit = ols_free(train_x, train_y)
        prediction = fit["intercept"] + fit["slope"] * xs[omitted]
        residuals.append(ys[omitted] - prediction)
    mse = statistics.fmean(value * value for value in residuals)
    return {
        "rmse": math.sqrt(mse),
        "mae": statistics.fmean(abs(value) for value in residuals),
        "residuals": residuals,
    }


def compare_models(per_modulus: Sequence[dict]) -> dict:
    xs = [1.0 / row["r"] for row in per_modulus]
    ys = [row["mean_ratio"] for row in per_modulus]
    free = ols_free(xs, ys)
    fixed = fit_fixed_two(xs, ys)
    free_cv = loocv(xs, ys, fixed_two=False)
    fixed_cv = loocv(xs, ys, fixed_two=True)
    free_aicc = aicc(free["sse"], len(xs), 2)
    fixed_aicc = aicc(fixed["sse"], len(xs), 1)
    return {
        "free_intercept": free,
        "fixed_limit_two": fixed,
        "fixed_sse_over_free_sse": fixed["sse"] / free["sse"],
        "aicc": {
            "free_intercept": free_aicc,
            "fixed_limit_two": fixed_aicc,
            "fixed_minus_free": fixed_aicc - free_aicc,
            "parameter_count_convention": (
                "regression coefficients only; used as a descriptive comparison"
            ),
        },
        "loocv": {
            "free_intercept": free_cv,
            "fixed_limit_two": fixed_cv,
            "preferred_by_rmse": (
                "fixed_limit_two" if fixed_cv["rmse"] < free_cv["rmse"] else "free_intercept"
            ),
        },
    }


def run_window(exp: int, moduli: Sequence[int], progress: bool = False) -> dict:
    started = time.perf_counter()
    lo, hi = 2**exp, 2 ** (exp + 1)
    n = np.arange(hi + 1)
    theta = sieve_theta(hi)
    main = singular_main(hi)
    even = (n >= lo) & (n < hi) & (n % 2 == 0)
    fft_length = 1 << (2 * len(theta) - 2).bit_length()
    theta_fft = np.fft.fft(theta, fft_length)
    rows: list[dict] = []

    for r in moduli:
        residues = n % r
        log_table = discrete_log_table(r)
        on = even & (residues == 0)
        off = even & (residues != 0)
        modes = representative_modes(r)
        if progress:
            print(f"e={exp} r={r} representatives={len(modes)}", flush=True)
        for k in modes:
            character = character_values(r, k, residues, log_table)
            twisted_fft = np.fft.fft(character * theta, fft_length)
            convolution = np.fft.ifft(twisted_fft * theta_fft)[: hi + 1]
            on_normalized = convolution[on] / main[on]
            off_normalized = (
                convolution[off] / main[off] + character[off] / (r - 2)
            )
            on_energy = float(np.mean(np.abs(on_normalized) ** 2) / (r - 1))
            off_energy = float(np.mean(np.abs(off_normalized) ** 2) / (r - 1))
            ratio = on_energy / off_energy
            rows.append(
                {
                    "exp": exp,
                    "r": r,
                    "k": k,
                    "conjugate_k": r - 1 - k,
                    "self_conjugate": 2 * k == r - 1,
                    "character_order": (r - 1) // math.gcd(k, r - 1),
                    "normalized_frequency": k / (r - 1),
                    "on_energy": on_energy,
                    "off_energy": off_energy,
                    "energy_ratio": ratio,
                }
            )

    per_modulus: list[dict] = []
    for r in moduli:
        local = [row for row in rows if row["r"] == r]
        ratios = [row["energy_ratio"] for row in local]
        minimum = min(local, key=lambda row: row["energy_ratio"])
        maximum = max(local, key=lambda row: row["energy_ratio"])
        per_modulus.append(
            {
                "r": r,
                "representative_count": len(local),
                "representative_k": [row["k"] for row in local],
                "mean_ratio": statistics.fmean(ratios),
                "population_sd": population_sd(ratios),
                "min_ratio": minimum["energy_ratio"],
                "min_k": minimum["k"],
                "max_ratio": maximum["energy_ratio"],
                "max_k": maximum["k"],
            }
        )

    return {
        "exp": exp,
        "window": [lo, hi],
        "fft_length": fft_length,
        "elapsed_seconds": time.perf_counter() - started,
        "rows": rows,
        "per_modulus": per_modulus,
        "model_comparison": compare_models(per_modulus),
        "threshold_sensitivity": threshold_sensitivity(per_modulus),
    }


def load_reference_ratios(paths: Sequence[Path]) -> dict[tuple[int, int], float]:
    reference: dict[tuple[int, int], float] = {}
    for path in paths:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
        for row in data["rows"]:
            r, k = int(row["r"]), int(row["k"])
            if k > r - 1 - k:
                continue
            ratio = row.get("on_off_ratio", row.get("energy_ratio"))
            if ratio is None:
                raise ValueError(f"No ratio field in {path}: {(r, k)}")
            reference[(r, k)] = float(ratio)
    return reference


def calibration(window: dict, reference_paths: Sequence[Path]) -> dict:
    reference = load_reference_ratios(reference_paths)
    observed = {
        (row["r"], row["k"]): row["energy_ratio"] for row in window["rows"]
    }
    shared = sorted(set(reference) & set(observed))
    if not shared:
        raise ValueError("Calibration has no shared (r,k) rows")
    differences = [abs(observed[key] - reference[key]) for key in shared]
    return {
        "exp": window["exp"],
        "reference_files": [path.name for path in reference_paths],
        "shared_rows": len(shared),
        "max_absolute_difference": max(differences),
        "mean_absolute_difference": statistics.fmean(differences),
        "tolerance": 1e-10,
        "passed": max(differences) <= 1e-10,
    }


def cross_window_summary(windows: Sequence[dict], moduli: Sequence[int]) -> dict:
    per_modulus: list[dict] = []
    for r in moduli:
        values = [
            next(row for row in window["per_modulus"] if row["r"] == r)[
                "mean_ratio"
            ]
            for window in windows
        ]
        within_modulus_sds = [
            next(row for row in window["per_modulus"] if row["r"] == r)[
                "population_sd"
            ]
            for window in windows
        ]
        per_modulus.append(
            {
                "r": r,
                "window_means": [
                    {"exp": window["exp"], "mean_ratio": value}
                    for window, value in zip(windows, values)
                ],
                "cross_window_mean": statistics.fmean(values),
                "cross_window_population_sd": population_sd(values),
                "cross_window_range": max(values) - min(values),
                "mean_absolute_deviation_from_two": statistics.fmean(
                    abs(value - 2.0) for value in values
                ),
                "mean_within_modulus_population_sd": statistics.fmean(
                    within_modulus_sds
                ),
                "within_modulus_population_sd_range": [
                    min(within_modulus_sds),
                    max(within_modulus_sds),
                ],
            }
        )

    large_moduli = [r for r in moduli if r >= 23]
    large_by_window: list[dict] = []
    if large_moduli:
        for window in windows:
            values = [
                row["mean_ratio"]
                for row in window["per_modulus"]
                if row["r"] in large_moduli
            ]
            large_by_window.append(
                {
                    "exp": window["exp"],
                    "moduli": large_moduli,
                    "mean_of_modulus_means": statistics.fmean(values),
                    "mean_absolute_deviation_from_two": statistics.fmean(
                        abs(value - 2.0) for value in values
                    ),
                    "max_absolute_deviation_from_two": max(
                        abs(value - 2.0) for value in values
                    ),
                }
            )

    aggregate_rows = [
        {"r": row["r"], "mean_ratio": row["cross_window_mean"]}
        for row in per_modulus
    ]
    return {
        "per_modulus": per_modulus,
        "aggregate_threshold_sensitivity": threshold_sensitivity(aggregate_rows),
        "free_intercepts_by_window": [
            {
                "exp": window["exp"],
                "intercept": window["model_comparison"]["free_intercept"][
                    "intercept"
                ],
                "ci95": window["model_comparison"]["free_intercept"].get(
                    "intercept_classical_95_percent_ci"
                ),
            }
            for window in windows
        ],
        "model_preference_by_window": [
            {
                "exp": window["exp"],
                "fixed_sse_over_free_sse": window["model_comparison"][
                    "fixed_sse_over_free_sse"
                ],
                "aicc_fixed_minus_free": window["model_comparison"]["aicc"][
                    "fixed_minus_free"
                ],
                "loocv_preferred": window["model_comparison"]["loocv"][
                    "preferred_by_rmse"
                ],
                "loocv_free_rmse": window["model_comparison"]["loocv"][
                    "free_intercept"
                ]["rmse"],
                "loocv_fixed_rmse": window["model_comparison"]["loocv"][
                    "fixed_limit_two"
                ]["rmse"],
            }
            for window in windows
        ],
        "larger_moduli_by_window": large_by_window,
    }


def validate_moduli(moduli: Sequence[int]) -> None:
    for value in moduli:
        if value < 5 or any(value % divisor == 0 for divisor in range(2, math.isqrt(value) + 1)):
            raise ValueError(f"Expected an odd prime modulus >=5, got {value}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exps", nargs="+", type=int, default=list(DEFAULT_EXPS))
    parser.add_argument(
        "--moduli", nargs="+", type=int, default=list(DEFAULT_MODULI)
    )
    parser.add_argument(
        "--calibration-reference", nargs="*", type=Path, default=[]
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "results" / "avrg_pass023_results.json",
    )
    parser.add_argument("--progress", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    validate_moduli(args.moduli)
    windows = [
        run_window(exp, args.moduli, progress=args.progress) for exp in args.exps
    ]
    result = {
        "pass": "PASS023",
        "title": "Multi-window and larger-modulus stability",
        "classification": "finite computational diagnostic",
        "claim_ceiling": (
            "No asymptotic proof and no direct progress toward a proof of Goldbach."
        ),
        "configuration": {
            "exps": args.exps,
            "moduli": args.moduli,
            "character_selection": (
                "one representative per conjugate pair of even nonprincipal characters"
            ),
        },
        "windows": windows,
        "cross_window": cross_window_summary(windows, args.moduli),
    }
    if args.calibration_reference:
        e17 = next((window for window in windows if window["exp"] == 17), None)
        if e17 is None:
            raise ValueError("Calibration references require exp=17")
        result["calibration"] = calibration(e17, args.calibration_reference)
        if not result["calibration"]["passed"]:
            raise RuntimeError(f"Calibration failed: {result['calibration']}")

    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"PASS023 complete: {args.output}")
    for window in windows:
        model = window["model_comparison"]
        print(
            f"e={window['exp']} seconds={window['elapsed_seconds']:.2f} "
            f"a={model['free_intercept']['intercept']:.6f} "
            f"fixed/free SSE={model['fixed_sse_over_free_sse']:.3f} "
            f"LOOCV={model['loocv']['preferred_by_rmse']}"
        )


if __name__ == "__main__":
    main()
