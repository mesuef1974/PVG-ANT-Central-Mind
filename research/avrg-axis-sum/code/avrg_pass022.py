#!/usr/bin/env python3
"""PASS022: separate modulus and character effects in the common e17 window.

This script uses only the Python standard library.  It merges the PASS015
results for r=5,7,11 with the PASS021 results for r=13,17,19, collapses each
complex-conjugate character pair, and performs finite-sample exploratory tests.

No asymptotic or Goldbach theorem claim is made by this program.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Callable, Iterable, Sequence


TOL = 1e-12


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_rows(small_path: Path, large_path: Path) -> tuple[list[dict], dict]:
    """Load both inputs without relying on a nonexistent ``parity`` key."""
    small = load_json(small_path)
    large = load_json(large_path)

    if small.get("exp") != large.get("exp"):
        raise ValueError("Input exponents differ")
    if small.get("window") != large.get("window"):
        raise ValueError("Input windows differ")

    rows: list[dict] = []

    # PASS015 rows are already restricted to the even nonprincipal characters.
    for item in small["rows"]:
        rows.append(
            {
                "r": int(item["r"]),
                "k": int(item["k"]),
                "rho": float(item["on_off_ratio"]),
                "source": small_path.name,
                "ratio_field": "on_off_ratio",
            }
        )

    # PASS021 calls the same on/off energy ratio ``energy_ratio``.
    for item in large["rows"]:
        rows.append(
            {
                "r": int(item["r"]),
                "k": int(item["k"]),
                "rho": float(item["energy_ratio"]),
                "source": large_path.name,
                "ratio_field": "energy_ratio",
            }
        )

    seen: set[tuple[int, int]] = set()
    for row in rows:
        key = (row["r"], row["k"])
        if key in seen:
            raise ValueError(f"Duplicate (r,k) row: {key}")
        seen.add(key)
        if row["k"] == 0 or row["k"] % 2:
            raise ValueError(f"Expected an even nonprincipal character: {key}")
        if not 0 < row["k"] < row["r"] - 1:
            raise ValueError(f"Character index outside 1..r-2: {key}")
        if not math.isfinite(row["rho"]) or row["rho"] <= 0:
            raise ValueError(f"Invalid ratio at {key}: {row['rho']}")

    metadata = {
        "exp": small["exp"],
        "window": small["window"],
        "input_files": [small_path.name, large_path.name],
        "raw_row_count": len(rows),
    }
    return rows, metadata


def collapse_conjugates(rows: Sequence[dict]) -> tuple[list[dict], list[dict]]:
    grouped: dict[tuple[int, int], list[dict]] = defaultdict(list)
    for row in rows:
        r, k = row["r"], row["k"]
        conjugate_k = (r - 1 - k) % (r - 1)
        representative_k = min(k, conjugate_k)
        grouped[(r, representative_k)].append(row)

    representatives: list[dict] = []
    checks: list[dict] = []
    for (r, k), members in sorted(grouped.items()):
        self_conjugate = (2 * k) % (r - 1) == 0
        expected_count = 1 if self_conjugate else 2
        if len(members) != expected_count:
            raise ValueError(
                f"Incomplete conjugacy orbit for (r,k_rep)=({r},{k}): "
                f"expected {expected_count}, found {len(members)}"
            )

        values = [member["rho"] for member in members]
        spread = max(values) - min(values)
        scale = max(1.0, max(abs(value) for value in values))
        if spread > TOL * scale:
            raise ValueError(
                f"Conjugate ratios disagree for (r,k_rep)=({r},{k}): {values}"
            )

        rho = statistics.fmean(values)
        representatives.append(
            {
                "r": r,
                "k": k,
                "conjugate_k": (r - 1 - k) % (r - 1),
                "self_conjugate": self_conjugate,
                "orbit_size": len(members),
                "rho": rho,
                "character_order": (r - 1) // math.gcd(k, r - 1),
                "normalized_frequency": k / (r - 1),
            }
        )
        checks.append(
            {
                "r": r,
                "k": k,
                "member_indices": sorted(member["k"] for member in members),
                "max_ratio_spread": spread,
                "passed": True,
            }
        )

    return representatives, checks


def population_sd(values: Sequence[float]) -> float:
    mean = statistics.fmean(values)
    return math.sqrt(statistics.fmean((value - mean) ** 2 for value in values))


def summarize_by_modulus(
    representatives: Sequence[dict], raw_rows: Sequence[dict]
) -> list[dict]:
    rep_by_r: dict[int, list[dict]] = defaultdict(list)
    raw_by_r: dict[int, list[dict]] = defaultdict(list)
    for row in representatives:
        rep_by_r[row["r"]].append(row)
    for row in raw_rows:
        raw_by_r[row["r"]].append(row)

    summaries: list[dict] = []
    for r in sorted(rep_by_r):
        rows = sorted(rep_by_r[r], key=lambda item: item["k"])
        values = [row["rho"] for row in rows]
        raw_mean = statistics.fmean(row["rho"] for row in raw_by_r[r])
        min_row = min(rows, key=lambda item: item["rho"])
        max_row = max(rows, key=lambda item: item["rho"])
        mean = statistics.fmean(values)
        summaries.append(
            {
                "r": r,
                "inverse_r": 1.0 / r,
                "representative_count": len(values),
                "representative_k": [row["k"] for row in rows],
                "mean_ratio": mean,
                "population_sd": population_sd(values),
                "sample_sd": statistics.stdev(values) if len(values) > 1 else None,
                "min_ratio": min_row["rho"],
                "min_k": min_row["k"],
                "max_ratio": max_row["rho"],
                "max_k": max_row["k"],
                "mean_minus_two": mean - 2.0,
                "all_rows_mean_for_sensitivity": raw_mean,
                "representative_minus_all_rows_mean": mean - raw_mean,
            }
        )
    return summaries


def pearson(xs: Sequence[float], ys: Sequence[float]) -> float:
    if len(xs) != len(ys) or len(xs) < 2:
        raise ValueError("Pearson correlation needs equal vectors of length >= 2")
    xbar, ybar = statistics.fmean(xs), statistics.fmean(ys)
    sxx = sum((x - xbar) ** 2 for x in xs)
    syy = sum((y - ybar) ** 2 for y in ys)
    if sxx == 0 or syy == 0:
        return 0.0
    return sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / math.sqrt(
        sxx * syy
    )


def average_ranks(values: Sequence[float]) -> list[float]:
    ordered = sorted(enumerate(values), key=lambda item: item[1])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(ordered):
        j = i + 1
        while j < len(ordered) and ordered[j][1] == ordered[i][1]:
            j += 1
        rank = ((i + 1) + j) / 2.0
        for position in range(i, j):
            ranks[ordered[position][0]] = rank
        i = j
    return ranks


def spearman(xs: Sequence[float], ys: Sequence[float]) -> float:
    return pearson(average_ranks(xs), average_ranks(ys))


def ols_simple(xs: Sequence[float], ys: Sequence[float]) -> dict:
    xbar, ybar = statistics.fmean(xs), statistics.fmean(ys)
    sxx = sum((x - xbar) ** 2 for x in xs)
    slope = sum((x - xbar) * (y - ybar) for x, y in zip(xs, ys)) / sxx
    intercept = ybar - slope * xbar
    predictions = [intercept + slope * x for x in xs]
    sst = sum((y - ybar) ** 2 for y in ys)
    sse = sum((y - prediction) ** 2 for y, prediction in zip(ys, predictions))
    return {
        "intercept": intercept,
        "slope": slope,
        "r_squared": 1.0 - sse / sst if sst else 0.0,
        "pearson_r": pearson(xs, ys),
        "spearman_rho": spearman(xs, ys),
    }


def exact_permutation_correlation(xs: Sequence[float], ys: Sequence[float]) -> dict:
    observed = pearson(xs, ys)
    total = 0
    two_sided = 0
    positive = 0
    for permuted in itertools.permutations(ys):
        statistic = pearson(xs, permuted)
        total += 1
        if abs(statistic) + 1e-15 >= abs(observed):
            two_sided += 1
        if statistic + 1e-15 >= observed:
            positive += 1
    return {
        "permutations": total,
        "two_sided_p": two_sided / total,
        "positive_direction_p": positive / total,
    }


def modulus_trend(summaries: Sequence[dict]) -> dict:
    xs = [row["inverse_r"] for row in summaries]
    ys = [row["mean_ratio"] for row in summaries]
    fit = ols_simple(xs, ys)
    fit["exact_permutation"] = exact_permutation_correlation(xs, ys)

    # Classical finite-sample uncertainty for the descriptive straight-line fit.
    # PASS022 has n=6 and therefore 4 residual degrees of freedom.
    predictions = [fit["intercept"] + fit["slope"] * x for x in xs]
    residuals = [y - prediction for y, prediction in zip(ys, predictions)]
    residual_df = len(xs) - 2
    xbar = statistics.fmean(xs)
    sxx = sum((x - xbar) ** 2 for x in xs)
    residual_variance = sum(value * value for value in residuals) / residual_df
    intercept_se = math.sqrt(
        residual_variance * (1.0 / len(xs) + xbar * xbar / sxx)
    )
    fit["residual_degrees_of_freedom"] = residual_df
    fit["intercept_standard_error"] = intercept_se
    if residual_df == 4:
        t_critical = 2.7764451051977987
        fit["intercept_classical_95_percent_ci"] = [
            fit["intercept"] - t_critical * intercept_se,
            fit["intercept"] + t_critical * intercept_se,
        ]

    # Directly inspect the empirical model with a fixed candidate limit of two.
    forced_slope = sum(x * (y - 2.0) for x, y in zip(xs, ys)) / sum(
        x * x for x in xs
    )
    forced_residuals = [
        y - (2.0 + forced_slope * x) for x, y in zip(xs, ys)
    ]
    unconstrained_sse = sum(value * value for value in residuals)
    forced_sse = sum(value * value for value in forced_residuals)
    fit["fixed_limit_two_model"] = {
        "formula": "mean_ratio = 2 + c/r",
        "c": forced_slope,
        "sse": forced_sse,
        "rmse": math.sqrt(forced_sse / len(xs)),
        "sse_over_unconstrained_sse": forced_sse / unconstrained_sse,
        "residuals_by_r": [
            {"r": row["r"], "residual": residual}
            for row, residual in zip(summaries, forced_residuals)
        ],
    }

    all_rows_fit = ols_simple(
        xs, [row["all_rows_mean_for_sensitivity"] for row in summaries]
    )
    fit["all_character_rows_weighting_sensitivity"] = all_rows_fit

    leave_one_out: list[dict] = []
    for omitted in range(len(summaries)):
        kept = [row for index, row in enumerate(summaries) if index != omitted]
        local_fit = ols_simple(
            [row["inverse_r"] for row in kept],
            [row["mean_ratio"] for row in kept],
        )
        leave_one_out.append(
            {
                "omitted_r": summaries[omitted]["r"],
                "slope": local_fit["slope"],
                "pearson_r": local_fit["pearson_r"],
                "r_squared": local_fit["r_squared"],
            }
        )
    fit["leave_one_modulus_out"] = leave_one_out
    fit["scope"] = "six finite modulus means; exploratory, not asymptotic"
    return fit


def group_center(
    rows: Sequence[dict], value: Callable[[dict], float]
) -> list[float]:
    by_r: dict[int, list[int]] = defaultdict(list)
    for index, row in enumerate(rows):
        by_r[row["r"]].append(index)
    result = [0.0] * len(rows)
    raw = [float(value(row)) for row in rows]
    for indices in by_r.values():
        local_mean = statistics.fmean(raw[index] for index in indices)
        for index in indices:
            result[index] = raw[index] - local_mean
    return result


def through_origin_r_squared(
    predictors: Sequence[Sequence[float]], response: Sequence[float]
) -> tuple[list[float], float]:
    if len(predictors) == 1:
        x = predictors[0]
        denominator = sum(value * value for value in x)
        beta = sum(value * y for value, y in zip(x, response)) / denominator
        fitted = [beta * value for value in x]
        coefficients = [beta]
    elif len(predictors) == 2:
        x1, x2 = predictors
        a = sum(value * value for value in x1)
        b = sum(v1 * v2 for v1, v2 in zip(x1, x2))
        d = sum(value * value for value in x2)
        c1 = sum(value * y for value, y in zip(x1, response))
        c2 = sum(value * y for value, y in zip(x2, response))
        determinant = a * d - b * b
        if abs(determinant) < 1e-18:
            raise ValueError("Singular two-predictor design")
        beta1 = (c1 * d - b * c2) / determinant
        beta2 = (a * c2 - b * c1) / determinant
        coefficients = [beta1, beta2]
        fitted = [beta1 * v1 + beta2 * v2 for v1, v2 in zip(x1, x2)]
    else:
        raise ValueError("Only one- and two-predictor fits are supported")

    sst = sum(y * y for y in response)
    sse = sum((y - fit) ** 2 for y, fit in zip(response, fitted))
    return coefficients, 1.0 - sse / sst if sst else 0.0


def within_group_permutations(rows: Sequence[dict]) -> Iterable[list[float]]:
    by_r: dict[int, list[float]] = defaultdict(list)
    for row in rows:
        by_r[row["r"]].append(row["rho"])
    ordered_groups = [by_r[r] for r in sorted(by_r)]
    group_permutations = [list(itertools.permutations(group)) for group in ordered_groups]
    for selection in itertools.product(*group_permutations):
        flattened: list[float] = []
        for group in selection:
            flattened.extend(group)
        yield flattened


def predictor_test(
    rows: Sequence[dict], predictor_functions: Sequence[Callable[[dict], float]]
) -> dict:
    response = group_center(rows, lambda row: row["rho"])
    predictors = [group_center(rows, function) for function in predictor_functions]
    coefficients, observed_r2 = through_origin_r_squared(predictors, response)

    total = 0
    at_least_observed = 0
    for permuted_raw in within_group_permutations(rows):
        # Permuting inside a modulus preserves its mean, so the same centering applies.
        pseudo_rows = [
            {"r": row["r"], "rho": rho}
            for row, rho in zip(rows, permuted_raw)
        ]
        permuted_response = group_center(pseudo_rows, lambda row: row["rho"])
        _, permuted_r2 = through_origin_r_squared(predictors, permuted_response)
        total += 1
        if permuted_r2 + 1e-15 >= observed_r2:
            at_least_observed += 1

    return {
        "coefficients": coefficients,
        "within_modulus_r_squared": observed_r2,
        "exact_within_modulus_permutations": total,
        "exact_permutation_p": at_least_observed / total,
    }


def within_modulus_character_tests(representatives: Sequence[dict]) -> dict:
    rows = sorted(representatives, key=lambda row: (row["r"], row["k"]))
    frequency = lambda row: row["normalized_frequency"]
    frequency_squared = lambda row: row["normalized_frequency"] ** 2
    order = lambda row: float(row["character_order"])

    per_modulus: list[dict] = []
    by_r: dict[int, list[dict]] = defaultdict(list)
    for row in rows:
        by_r[row["r"]].append(row)
    for r in sorted(by_r):
        local = by_r[r]
        if len(local) < 2:
            continue
        xs = [row["normalized_frequency"] for row in local]
        ys = [row["rho"] for row in local]
        per_modulus.append(
            {
                "r": r,
                "n": len(local),
                "frequency_slope": ols_simple(xs, ys)["slope"],
                "frequency_pearson_r": pearson(xs, ys),
            }
        )

    return {
        "frequency_linear": predictor_test(rows, [frequency]),
        "frequency_linear_quadratic": predictor_test(
            rows, [frequency, frequency_squared]
        ),
        "character_order_linear": predictor_test(rows, [order]),
        "per_modulus_frequency_direction": per_modulus,
        "method": (
            "Predictors and ratios are centered within each r; exact tests permute "
            "ratios only within r. Character order is (r-1)/gcd(k,r-1)."
        ),
    }


def proximity_to_two(summaries: Sequence[dict]) -> dict:
    all_deviations = [abs(row["mean_minus_two"]) for row in summaries]
    large = [row for row in summaries if row["r"] >= 13]
    large_deviations = [abs(row["mean_minus_two"]) for row in large]
    return {
        "all_moduli_mean_absolute_deviation": statistics.fmean(all_deviations),
        "all_moduli_max_absolute_deviation": max(all_deviations),
        "r_ge_13_moduli": [row["r"] for row in large],
        "r_ge_13_mean_absolute_deviation": statistics.fmean(large_deviations),
        "r_ge_13_max_absolute_deviation": max(large_deviations),
        "r_ge_13_mean_of_modulus_means": statistics.fmean(
            row["mean_ratio"] for row in large
        ),
        "interpretation_boundary": (
            "Finite-window descriptive support only; not evidence of a proved limit."
        ),
    }


def analyze(small_path: Path, large_path: Path) -> dict:
    raw_rows, metadata = load_rows(small_path, large_path)
    representatives, conjugacy_checks = collapse_conjugates(raw_rows)
    summaries = summarize_by_modulus(representatives, raw_rows)
    expected_moduli = [5, 7, 11, 13, 17, 19]
    actual_moduli = [row["r"] for row in summaries]
    if actual_moduli != expected_moduli:
        raise ValueError(f"Unexpected modulus set: {actual_moduli}")

    return {
        "pass": "PASS022",
        "title": "Modulus-character separation in the common e17 window",
        "classification": "finite computational diagnostic",
        "claim_ceiling": (
            "No asymptotic proof and no direct progress toward a proof of Goldbach."
        ),
        "metadata": {
            **metadata,
            "representative_row_count": len(representatives),
            "standard_deviation_convention": "population SD across orbit representatives",
        },
        "conjugacy_checks": conjugacy_checks,
        "representatives": representatives,
        "per_modulus": summaries,
        "trend_with_inverse_modulus": modulus_trend(summaries),
        "within_modulus_character_tests": within_modulus_character_tests(
            representatives
        ),
        "proximity_to_two": proximity_to_two(summaries),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--small",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "results" / "avrg_pass015_e17.json",
        help="PASS015 JSON for r=5,7,11",
    )
    parser.add_argument(
        "--large",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "results" / "avrg_pass021_full_e17.json",
        help="PASS021 JSON for r=13,17,19",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "results" / "avrg_pass022_results_e17.json",
        help="Output JSON path",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = analyze(args.small, args.large)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2, sort_keys=False)
        handle.write("\n")
    print(f"PASS022 complete: {args.output}")
    print(
        "modulus means:",
        ", ".join(
            f"r={row['r']}: {row['mean_ratio']:.9f}"
            for row in result["per_modulus"]
        ),
    )


if __name__ == "__main__":
    main()
