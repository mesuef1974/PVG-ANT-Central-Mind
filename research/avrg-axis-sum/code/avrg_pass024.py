#!/usr/bin/env python3
"""PASS024: separate modulus scale from cross-window character stability.

The input is the locked PASS023 result.  The primary statistic is the share of
within-modulus character energy explained by a persistent character signature
across the four windows.  Character labels are permuted independently inside
each window to test the no-persistent-signature null.

This is a finite computational diagnostic.  It is not an asymptotic proof and
does not constitute direct progress toward a proof of Goldbach.
"""

from __future__ import annotations

import argparse
import json
import math
from itertools import combinations
from pathlib import Path
from typing import Sequence

import numpy as np


LOCKED_EXPS = (15, 16, 17, 18)
LOCKED_MODULI = (5, 7, 11, 13, 17, 19, 23, 29, 31)
PRIMARY_MODULI = (11, 13, 17, 19, 23, 29, 31)
DEFAULT_SEED = 240724
DEFAULT_GLOBAL_PERMUTATIONS = 100_000
DEFAULT_PER_MODULUS_PERMUTATIONS = 50_000


def default_input_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_candidate = here.parent / "results" / "avrg_pass023_results.json"
    if archive_candidate.exists():
        return archive_candidate
    return here.parent / "pass023" / "avrg_pass023_results.json"


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_results = here.parent / "results"
    if archive_results.is_dir():
        return archive_results / "avrg_pass024_results.json"
    return here / "avrg_pass024_results.json"


def load_locked_rows(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    configuration = data.get("configuration", {})
    exps = tuple(int(value) for value in configuration.get("exps", []))
    moduli = tuple(int(value) for value in configuration.get("moduli", []))
    if exps != LOCKED_EXPS:
        raise ValueError(f"PASS024 locked exps are {LOCKED_EXPS}, received {exps}")
    if moduli != LOCKED_MODULI:
        raise ValueError(
            f"PASS024 locked moduli are {LOCKED_MODULI}, received {moduli}"
        )

    windows = data.get("windows", [])
    if tuple(int(window["exp"]) for window in windows) != LOCKED_EXPS:
        raise ValueError("Window order or membership differs from the locked protocol")

    rows: list[dict] = []
    seen: set[tuple[int, int, int]] = set()
    modes_by_r: dict[int, tuple[int, ...]] = {}
    for window in windows:
        exp = int(window["exp"])
        local_by_r: dict[int, list[int]] = {r: [] for r in LOCKED_MODULI}
        for raw in window.get("rows", []):
            r, k = int(raw["r"]), int(raw["k"])
            key = (exp, r, k)
            if key in seen:
                raise ValueError(f"Duplicate PASS023 row: {key}")
            seen.add(key)
            ratio = float(raw["energy_ratio"])
            if not math.isfinite(ratio) or ratio <= 0:
                raise ValueError(f"Invalid energy ratio at {key}: {ratio}")
            if k <= 0 or k % 2 or k > r - 1 - k:
                raise ValueError(f"Row is not a valid conjugacy representative: {key}")
            local_by_r[r].append(k)
            rows.append({"exp": exp, "r": r, "k": k, "rho": ratio})

        for r in LOCKED_MODULI:
            modes = tuple(sorted(local_by_r[r]))
            if not modes:
                raise ValueError(f"No character representatives for e={exp}, r={r}")
            previous = modes_by_r.setdefault(r, modes)
            if modes != previous:
                raise ValueError(f"Character list changes across windows for r={r}")

    expected = sum(len(modes_by_r[r]) for r in LOCKED_MODULI) * len(LOCKED_EXPS)
    if len(rows) != expected:
        raise ValueError(f"Expected {expected} locked rows, received {len(rows)}")
    return rows


def build_decomposition(rows: Sequence[dict]) -> dict:
    indexed = {(row["exp"], row["r"], row["k"]): row["rho"] for row in rows}
    modes_by_r = {
        r: sorted({row["k"] for row in rows if row["r"] == r})
        for r in LOCKED_MODULI
    }
    scale_rows: list[dict] = []
    centered_rows: list[dict] = []
    matrices: dict[int, np.ndarray] = {}

    for r in LOCKED_MODULI:
        modes = modes_by_r[r]
        matrix = np.array(
            [[indexed[(exp, r, k)] for k in modes] for exp in LOCKED_EXPS],
            dtype=float,
        )
        means = matrix.mean(axis=1)
        centered = matrix - means[:, None]
        if float(np.max(np.abs(centered.sum(axis=1)))) > 1e-12:
            raise AssertionError(f"Within-modulus centering failed for r={r}")
        matrices[r] = centered
        for exp_index, exp in enumerate(LOCKED_EXPS):
            scale_rows.append(
                {
                    "exp": exp,
                    "r": r,
                    "representative_count": len(modes),
                    "mean_ratio": float(means[exp_index]),
                }
            )
            for k_index, k in enumerate(modes):
                centered_rows.append(
                    {
                        "exp": exp,
                        "r": r,
                        "k": k,
                        "rho": float(matrix[exp_index, k_index]),
                        "modulus_mean": float(means[exp_index]),
                        "g": float(centered[exp_index, k_index]),
                    }
                )

    return {
        "modes_by_r": modes_by_r,
        "scale_rows": scale_rows,
        "centered_rows": centered_rows,
        "matrices": matrices,
    }


def fit_scale(scale_rows: Sequence[dict]) -> dict:
    by_window: list[dict] = []
    for exp in LOCKED_EXPS:
        local = [row for row in scale_rows if row["exp"] == exp]
        xs = np.array([1.0 / row["r"] for row in local], dtype=float)
        ys = np.array([row["mean_ratio"] for row in local], dtype=float)
        slope = float(np.dot(xs, ys - 2.0) / np.dot(xs, xs))
        residuals = ys - (2.0 + slope * xs)
        by_window.append(
            {
                "exp": exp,
                "A_e": slope,
                "rmse_over_modulus_means": float(np.sqrt(np.mean(residuals**2))),
                "max_absolute_residual": float(np.max(np.abs(residuals))),
                "residuals": [
                    {"r": row["r"], "delta": float(value)}
                    for row, value in zip(local, residuals)
                ],
            }
        )
    coefficients = [row["A_e"] for row in by_window]
    return {
        "model": "m[e,r] = 2 + A[e]/r + delta[e,r]",
        "by_window": by_window,
        "A_e_mean": float(np.mean(coefficients)),
        "A_e_population_sd": float(np.std(coefficients, ddof=0)),
        "A_e_range": [float(min(coefficients)), float(max(coefficients))],
    }


def persistent_components(matrix: np.ndarray) -> dict:
    signature = matrix.mean(axis=0)
    residual = matrix - signature[None, :]
    total_ss = float(np.sum(matrix**2))
    persistent_ss = float(matrix.shape[0] * np.sum(signature**2))
    residual_ss = float(np.sum(residual**2))
    tolerance = 1e-12 * max(1.0, total_ss)
    if abs(total_ss - persistent_ss - residual_ss) > tolerance:
        raise AssertionError("Persistent/residual sum-of-squares identity failed")
    return {
        "signature": signature,
        "residual": residual,
        "total_ss": total_ss,
        "persistent_ss": persistent_ss,
        "residual_ss": residual_ss,
        "persistence_fraction": persistent_ss / total_ss if total_ss else 0.0,
    }


def permutation_pvalue(null_values: np.ndarray, observed: float) -> float:
    return float((1 + np.count_nonzero(null_values >= observed - 1e-15)) / (len(null_values) + 1))


def permutation_distribution(
    matrix: np.ndarray, permutations: int, rng: np.random.Generator
) -> np.ndarray:
    """Persistent SS under independent within-window label permutations.

    The first window is fixed because a common relabeling of every window
    leaves the statistic unchanged.
    """
    window_count, character_count = matrix.shape
    totals = np.broadcast_to(matrix[0], (permutations, character_count)).copy()
    for window_index in range(1, window_count):
        random_scores = rng.random((permutations, character_count))
        indices = np.argsort(random_scores, axis=1)
        totals += matrix[window_index][indices]
    means = totals / window_count
    return window_count * np.sum(means**2, axis=1)


def holm_adjust(pairs: Sequence[tuple[int, float]]) -> dict[int, float]:
    ordered = sorted(pairs, key=lambda item: item[1])
    count = len(ordered)
    adjusted: dict[int, float] = {}
    running = 0.0
    for index, (label, value) in enumerate(ordered):
        candidate = min(1.0, (count - index) * value)
        running = max(running, candidate)
        adjusted[label] = running
    return adjusted


def loo_skill(matrix: np.ndarray) -> dict:
    signature_sse = 0.0
    zero_sse = 0.0
    by_window: list[dict] = []
    for held_out in range(matrix.shape[0]):
        training = np.delete(matrix, held_out, axis=0)
        prediction = training.mean(axis=0)
        target = matrix[held_out]
        local_signature_sse = float(np.sum((target - prediction) ** 2))
        local_zero_sse = float(np.sum(target**2))
        signature_sse += local_signature_sse
        zero_sse += local_zero_sse
        by_window.append(
            {
                "exp": LOCKED_EXPS[held_out],
                "signature_sse": local_signature_sse,
                "zero_sse": local_zero_sse,
            }
        )
    return {
        "signature_sse": signature_sse,
        "zero_sse": zero_sse,
        "skill_vs_zero": 1.0 - signature_sse / zero_sse if zero_sse else 0.0,
        "by_held_out_window": by_window,
    }


def pairwise_correlations(matrix: np.ndarray) -> list[dict]:
    output: list[dict] = []
    for left, right in combinations(range(matrix.shape[0]), 2):
        x, y = matrix[left], matrix[right]
        denominator = float(np.linalg.norm(x) * np.linalg.norm(y))
        correlation = float(np.dot(x, y) / denominator) if denominator else 0.0
        output.append(
            {
                "exp_left": LOCKED_EXPS[left],
                "exp_right": LOCKED_EXPS[right],
                "correlation": correlation,
            }
        )
    return output


def sign_agreement(matrix: np.ndarray, signature: np.ndarray) -> dict:
    signature_sign = np.sign(signature)
    comparable = signature_sign != 0
    if not np.any(comparable):
        return {"agreements": 0, "comparisons": 0, "fraction": 0.0}
    observed = np.sign(matrix[:, comparable])
    expected = signature_sign[comparable][None, :]
    comparisons = int(observed.size)
    agreements = int(np.count_nonzero(observed == expected))
    return {
        "agreements": agreements,
        "comparisons": comparisons,
        "fraction": agreements / comparisons,
    }


def sum_of_squares_channels(rows: Sequence[dict], centered_rows: Sequence[dict]) -> dict:
    total = sum((row["rho"] - 2.0) ** 2 for row in rows)
    within = sum(row["g"] ** 2 for row in centered_rows)
    between = sum(
        row["representative_count"] * (row["mean_ratio"] - 2.0) ** 2
        for row in build_scale_lookup(centered_rows)
    )
    tolerance = 1e-11 * max(1.0, total)
    if abs(total - between - within) > tolerance:
        raise AssertionError("Modulus-mean/character sum-of-squares identity failed")
    return {
        "reference": 2.0,
        "total_ss": total,
        "modulus_mean_ss": between,
        "within_modulus_character_ss": within,
        "modulus_mean_fraction": between / total if total else 0.0,
        "character_fraction": within / total if total else 0.0,
        "weighting": "each character representative row has equal weight",
    }


def build_scale_lookup(centered_rows: Sequence[dict]) -> list[dict]:
    grouped: dict[tuple[int, int], list[dict]] = {}
    for row in centered_rows:
        grouped.setdefault((row["exp"], row["r"]), []).append(row)
    return [
        {
            "exp": key[0],
            "r": key[1],
            "representative_count": len(local),
            "mean_ratio": local[0]["modulus_mean"],
        }
        for key, local in sorted(grouped.items())
    ]


def analyze(
    rows: Sequence[dict],
    global_permutations: int = DEFAULT_GLOBAL_PERMUTATIONS,
    per_modulus_permutations: int = DEFAULT_PER_MODULUS_PERMUTATIONS,
    seed: int = DEFAULT_SEED,
) -> dict:
    if global_permutations < 1:
        raise ValueError("global_permutations must be positive")
    if not 1 <= per_modulus_permutations <= global_permutations:
        raise ValueError("per_modulus_permutations must be in [1, global]")

    decomposition = build_decomposition(rows)
    matrices = decomposition["matrices"]
    rng = np.random.default_rng(seed)
    global_null = np.zeros(global_permutations, dtype=float)
    per_modulus: list[dict] = []
    raw_pvalues: list[tuple[int, float]] = []

    for r in PRIMARY_MODULI:
        matrix = matrices[r]
        components = persistent_components(matrix)
        null_values = permutation_distribution(matrix, global_permutations, rng)
        global_null += null_values
        local_null = null_values[:per_modulus_permutations]
        pvalue = permutation_pvalue(local_null, components["persistent_ss"])
        raw_pvalues.append((r, pvalue))
        skill = loo_skill(matrix)
        correlations = pairwise_correlations(matrix)
        per_modulus.append(
            {
                "r": r,
                "representative_k": decomposition["modes_by_r"][r],
                "representative_count": matrix.shape[1],
                "G_by_k": [
                    {"k": k, "G": float(value)}
                    for k, value in zip(
                        decomposition["modes_by_r"][r], components["signature"]
                    )
                ],
                "total_character_ss": components["total_ss"],
                "persistent_ss": components["persistent_ss"],
                "residual_ss": components["residual_ss"],
                "persistence_fraction": components["persistence_fraction"],
                "permutation_p_raw": pvalue,
                "loo": skill,
                "pairwise_correlations": correlations,
                "mean_pairwise_correlation": float(
                    np.mean([row["correlation"] for row in correlations])
                ),
                "sign_agreement": sign_agreement(matrix, components["signature"]),
            }
        )

    adjusted = holm_adjust(raw_pvalues)
    for row in per_modulus:
        row["permutation_p_holm"] = adjusted[row["r"]]

    observed_persistent = sum(row["persistent_ss"] for row in per_modulus)
    observed_total = sum(row["total_character_ss"] for row in per_modulus)
    observed_residual = sum(row["residual_ss"] for row in per_modulus)
    global_loo_signature_sse = sum(row["loo"]["signature_sse"] for row in per_modulus)
    global_loo_zero_sse = sum(row["loo"]["zero_sse"] for row in per_modulus)
    global_persistence_fraction = observed_persistent / observed_total
    global_pvalue = permutation_pvalue(global_null, observed_persistent)
    global_loo_skill = 1.0 - global_loo_signature_sse / global_loo_zero_sse
    stable = (
        global_persistence_fraction > 0.50
        and global_pvalue <= 0.05
        and global_loo_skill > 0.0
    )

    return {
        "pass": "PASS024",
        "title": "Modulus-scale and cross-window character-signature separation",
        "classification": "finite computational diagnostic",
        "claim_ceiling": (
            "No asymptotic proof and no direct progress toward a proof of Goldbach."
        ),
        "locked_protocol": {
            "exps": list(LOCKED_EXPS),
            "moduli": list(LOCKED_MODULI),
            "primary_character_moduli": list(PRIMARY_MODULI),
            "seed": seed,
            "global_permutations": global_permutations,
            "per_modulus_permutations": per_modulus_permutations,
            "decision_rule": {
                "persistence_fraction_strictly_greater_than": 0.50,
                "global_permutation_p_at_most": 0.05,
                "loo_skill_strictly_greater_than": 0.0,
            },
        },
        "scale_channel": fit_scale(decomposition["scale_rows"]),
        "sum_of_squares_channels": sum_of_squares_channels(
            rows, decomposition["centered_rows"]
        ),
        "character_channel": {
            "uninformative_single_representative_moduli": [5, 7],
            "global": {
                "total_character_ss": observed_total,
                "persistent_ss": observed_persistent,
                "residual_ss": observed_residual,
                "persistence_fraction": global_persistence_fraction,
                "permutation_p": global_pvalue,
                "loo_signature_sse": global_loo_signature_sse,
                "loo_zero_sse": global_loo_zero_sse,
                "loo_skill_vs_zero": global_loo_skill,
                "decision": (
                    "stable_finite_window_character_signature"
                    if stable
                    else "insufficient_evidence_for_stable_character_signature"
                ),
                "decision_passed": stable,
            },
            "per_modulus": per_modulus,
        },
        "decomposition": {
            "scale_rows": decomposition["scale_rows"],
            "centered_rows": decomposition["centered_rows"],
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=default_input_path())
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument(
        "--global-permutations", type=int, default=DEFAULT_GLOBAL_PERMUTATIONS
    )
    parser.add_argument(
        "--per-modulus-permutations",
        type=int,
        default=DEFAULT_PER_MODULUS_PERMUTATIONS,
    )
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = load_locked_rows(args.input)
    result = analyze(
        rows,
        global_permutations=args.global_permutations,
        per_modulus_permutations=args.per_modulus_permutations,
        seed=args.seed,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    global_result = result["character_channel"]["global"]
    print(f"PASS024 complete: {args.output}")
    print(
        "persistence_fraction="
        f"{global_result['persistence_fraction']:.6f} "
        f"permutation_p={global_result['permutation_p']:.6g} "
        f"loo_skill={global_result['loo_skill_vs_zero']:.6f}"
    )
    print(f"decision={global_result['decision']}")


if __name__ == "__main__":
    main()
