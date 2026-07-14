#!/usr/bin/env python3
"""PASS033: jackknife stability of the linear cancellation functional.

The no-intercept PASS032 regression is mapped back from fold-specific SVD
coordinates to the common orbit space.  Signed directional concentration
across the five leave-one-window-out functionals is compared with a restricted
within-character window-permutation null.  Axis concentration is reported
separately because sign flips are fatal for predicting signed cancellation.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import statistics
import sys
from pathlib import Path
from typing import Mapping, Sequence

import numpy as np


EXPECTED_PASS028_SHA256 = (
    "9088e373aa18fdef6cdc8a7a0b6b1fb8680f5dd08653a12699a787118f6f4eab"
)
EXPECTED_PASS032_SHA256 = (
    "1168d02a0d8640a3371d15769b42daf67acf27843a4e67c27dbbec8219a2a787"
)
PERMUTATION_ITERATIONS = 5000
PERMUTATION_SEED = 330719
MIN_GLOBAL_ORIENTED_COHERENCE = 0.50
MAX_PERMUTATION_P_VALUE = 0.01
MIN_MODULUS_ORIENTED_COHERENCE = 0.40
MIN_MODULUS_MEDIAN_SIGNED_COSINE = 0.25
MAX_MODULUS_NORM_CV = 0.50
REQUIRED_MODULUS_COUNT = 5


def load_pass032_module():
    try:
        return importlib.import_module("avrg_pass032")
    except ModuleNotFoundError:
        sibling = Path(__file__).resolve().parents[1] / "pass032"
        sys.path.insert(0, str(sibling))
        return importlib.import_module("avrg_pass032")


def default_pass028_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass028_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass028" / "avrg_pass028_results.json"


def default_pass032_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass032_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass032" / "avrg_pass032_results.json"


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_results = here.parent / "results"
    if archive_results.is_dir():
        return archive_results / "avrg_pass033_results.json"
    return here / "avrg_pass033_results.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_locked_pass032(path: Path) -> dict:
    observed = sha256_file(path)
    if observed != EXPECTED_PASS032_SHA256:
        raise ValueError(f"PASS032 hash mismatch: {observed}")
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if data.get("pass") != "PASS032" or len(data.get("folds", [])) != 35:
        raise ValueError("Invalid PASS032 result")
    return data


def functional_from_fold(centered: Mapping, locked_fold: Mapping, p32, p30, p29) -> dict:
    r = int(locked_fold["r"])
    heldout_exp = int(locked_fold["heldout_exp"])
    rank_d = int(locked_fold["rank_d"])
    x_train, x_test = p30.build_train_test(centered, r, heldout_exp, p29)
    basis, sum_direction = p32.amplitude_basis(x_train, rank_d, p30)
    z_train = x_train @ basis
    z_test = x_test @ basis
    c_train = x_train @ sum_direction
    beta, c_prediction, design_rank, condition_number = p32.least_squares_coupling(
        z_train, c_train, z_test
    )
    functional = basis @ beta
    norm = float(np.linalg.norm(functional))
    if norm <= 1e-15:
        raise ValueError(f"Degenerate functional at {(r, heldout_exp)}")
    unit = functional / norm
    predicted_scalar = np.sqrt(x_test.shape[1]) * c_prediction
    locked_prediction = np.asarray(locked_fold["predicted_scalar"], dtype=float)
    actual_scalar = np.sum(x_test, axis=1)
    locked_actual = np.asarray(locked_fold["actual_scalar"], dtype=float)
    return {
        "r": r,
        "heldout_exp": heldout_exp,
        "rank_d": rank_d,
        "orbit_count": int(x_test.shape[1]),
        "modes": [int(k) for k in locked_fold["modes"]],
        "functional_norm": norm,
        "design_rank": design_rank,
        "design_condition_number": condition_number,
        "sum_perpendicular_error": float(abs(functional @ sum_direction)),
        "maximum_prediction_error_vs_pass032": float(
            np.max(np.abs(predicted_scalar - locked_prediction))
        ),
        "maximum_actual_scalar_error_vs_pass032": float(
            np.max(np.abs(actual_scalar - locked_actual))
        ),
        "_functional": functional,
        "_unit": unit,
        "_basis": basis,
        "_z_train": z_train,
        "_z_test": z_test,
    }


def stability_metrics(units: np.ndarray, norms: np.ndarray) -> dict:
    if units.ndim != 2 or norms.ndim != 1 or units.shape[0] != norms.size:
        raise ValueError("Invalid stability arrays")
    if units.shape[0] < 2 or np.any(norms <= 0):
        raise ValueError("Stability requires nonzero repeated functionals")
    gram = units @ units.T
    pairwise = gram[np.triu_indices(units.shape[0], 1)]
    oriented = float(np.sum(np.mean(units, axis=0) ** 2))
    scatter = units.T @ units / units.shape[0]
    axis = float(np.linalg.eigvalsh(scatter)[-1])
    mean_norm = float(np.mean(norms))
    norm_cv = float(np.std(norms) / mean_norm)
    tolerance = 1e-12
    if oriented < -tolerance or oriented > 1 + tolerance:
        raise AssertionError("Oriented coherence outside [0,1]")
    if axis < -tolerance or axis > 1 + tolerance:
        raise AssertionError("Axis coherence outside [0,1]")
    return {
        "functional_count": int(units.shape[0]),
        "pair_count": int(pairwise.size),
        "oriented_coherence": min(1.0, max(0.0, oriented)),
        "axis_coherence": min(1.0, max(0.0, axis)),
        "mean_signed_cosine": float(np.mean(pairwise)),
        "median_signed_cosine": float(np.median(pairwise)),
        "minimum_signed_cosine": float(np.min(pairwise)),
        "maximum_signed_cosine": float(np.max(pairwise)),
        "mean_absolute_cosine": float(np.mean(np.abs(pairwise))),
        "negative_pair_count": int(np.count_nonzero(pairwise < 0)),
        "negative_pair_fraction": float(np.mean(pairwise < 0)),
        "functional_norm_mean": mean_norm,
        "functional_norm_population_sd": float(np.std(norms)),
        "functional_norm_cv": norm_cv,
        "functional_norm_minimum": float(np.min(norms)),
        "functional_norm_maximum": float(np.max(norms)),
    }


def metrics_by_modulus(folds: Sequence[dict], moduli: Sequence[int]) -> list[dict]:
    output = []
    for r in moduli:
        local = sorted(
            (fold for fold in folds if fold["r"] == r),
            key=lambda fold: fold["heldout_exp"],
        )
        units = np.vstack([fold["_unit"] for fold in local])
        norms = np.asarray([fold["functional_norm"] for fold in local])
        output.append(
            {
                "r": int(r),
                **stability_metrics(units, norms),
                "by_heldout_window": [
                    {
                        "heldout_exp": fold["heldout_exp"],
                        "rank_d": fold["rank_d"],
                        "functional_norm": fold["functional_norm"],
                    }
                    for fold in local
                ],
            }
        )
    return output


def global_stability(by_modulus: Sequence[Mapping]) -> dict:
    oriented = [float(row["oriented_coherence"]) for row in by_modulus]
    axis = [float(row["axis_coherence"]) for row in by_modulus]
    pairwise_signed = [float(row["mean_signed_cosine"]) for row in by_modulus]
    return {
        "modulus_count": len(by_modulus),
        "mean_oriented_coherence": statistics.fmean(oriented),
        "median_oriented_coherence": statistics.median(oriented),
        "minimum_oriented_coherence": min(oriented),
        "maximum_oriented_coherence": max(oriented),
        "mean_axis_coherence": statistics.fmean(axis),
        "mean_modulus_pairwise_signed_cosine": statistics.fmean(pairwise_signed),
        "total_negative_pair_count": sum(
            int(row["negative_pair_count"]) for row in by_modulus
        ),
        "total_pair_count": sum(int(row["pair_count"]) for row in by_modulus),
    }


def stability_from_functionals(functionals: Sequence[dict], moduli: Sequence[int]) -> tuple[list[dict], dict]:
    by_modulus = metrics_by_modulus(functionals, moduli)
    return by_modulus, global_stability(by_modulus)


def restricted_permutation_null(
    folds: Sequence[dict],
    raw_coefficients: Mapping,
    exps: Sequence[int],
    moduli: Sequence[int],
    p32,
    iterations: int = PERMUTATION_ITERATIONS,
    seed: int = PERMUTATION_SEED,
) -> dict:
    rng = np.random.default_rng(seed)
    observed_by_modulus, observed_global = stability_from_functionals(folds, moduli)
    observed_oriented = observed_global["mean_oriented_coherence"]
    observed_axis = observed_global["mean_axis_coherence"]
    oriented_samples = np.empty(iterations, dtype=float)
    axis_samples = np.empty(iterations, dtype=float)
    keys = sorted(raw_coefficients)
    for iteration in range(iterations):
        permuted = {
            key: np.asarray(raw_coefficients[key])[rng.permutation(len(exps))]
            for key in keys
        }
        simulated = []
        for fold in folds:
            c_train, _ = p32.permuted_targets_for_fold(permuted, fold, exps)
            beta, _, _, _ = p32.least_squares_coupling(
                fold["_z_train"], c_train, fold["_z_test"]
            )
            functional = fold["_basis"] @ beta
            norm = float(np.linalg.norm(functional))
            if norm <= 1e-15:
                raise ValueError("Degenerate permuted functional")
            simulated.append(
                {
                    "r": fold["r"],
                    "heldout_exp": fold["heldout_exp"],
                    "rank_d": fold["rank_d"],
                    "functional_norm": norm,
                    "_unit": functional / norm,
                }
            )
        _, global_metrics = stability_from_functionals(simulated, moduli)
        oriented_samples[iteration] = global_metrics["mean_oriented_coherence"]
        axis_samples[iteration] = global_metrics["mean_axis_coherence"]
    oriented_exceedances = int(np.count_nonzero(oriented_samples >= observed_oriented))
    axis_exceedances = int(np.count_nonzero(axis_samples >= observed_axis))

    def describe(samples: np.ndarray, observed: float, exceedances: int) -> dict:
        return {
            "observed": observed,
            "null_mean": float(np.mean(samples)),
            "null_population_sd": float(np.std(samples)),
            "null_quantiles": {
                "0.50": float(np.quantile(samples, 0.50)),
                "0.90": float(np.quantile(samples, 0.90)),
                "0.95": float(np.quantile(samples, 0.95)),
                "0.99": float(np.quantile(samples, 0.99)),
            },
            "null_minimum": float(np.min(samples)),
            "null_maximum": float(np.max(samples)),
            "exceedance_count": exceedances,
            "one_sided_p_value": (exceedances + 1) / (iterations + 1),
        }

    return {
        "iterations": iterations,
        "seed": seed,
        "restriction": "permute five windows independently within each (r,k)",
        "oriented_coherence_primary": describe(
            oriented_samples, observed_oriented, oriented_exceedances
        ),
        "axis_coherence_secondary": describe(
            axis_samples, observed_axis, axis_exceedances
        ),
        "observed_by_modulus_recomputed": observed_by_modulus,
    }


def correlation(xs: Sequence[float], ys: Sequence[float]) -> float:
    x = np.asarray(xs, dtype=float)
    y = np.asarray(ys, dtype=float)
    if x.size != y.size or x.size < 2 or np.std(x) == 0 or np.std(y) == 0:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def decision_summary(
    by_modulus: Sequence[Mapping],
    global_metrics: Mapping,
    permutation: Mapping,
) -> dict:
    coherent_moduli = sum(
        row["oriented_coherence"] >= MIN_MODULUS_ORIENTED_COHERENCE
        for row in by_modulus
    )
    positive_median_moduli = sum(
        row["median_signed_cosine"] >= MIN_MODULUS_MEDIAN_SIGNED_COSINE
        for row in by_modulus
    )
    norm_stable_moduli = sum(
        row["functional_norm_cv"] <= MAX_MODULUS_NORM_CV for row in by_modulus
    )
    conditions = {
        "global_oriented_coherence_at_least_0_50": global_metrics[
            "mean_oriented_coherence"
        ]
        >= MIN_GLOBAL_ORIENTED_COHERENCE,
        "restricted_permutation_p_at_most_0_01": permutation[
            "oriented_coherence_primary"
        ]["one_sided_p_value"]
        <= MAX_PERMUTATION_P_VALUE,
        "at_least_five_moduli_oriented_coherence_at_least_0_40": coherent_moduli
        >= REQUIRED_MODULUS_COUNT,
        "at_least_five_moduli_median_signed_cosine_at_least_0_25": positive_median_moduli
        >= REQUIRED_MODULUS_COUNT,
        "at_least_five_moduli_functional_norm_cv_at_most_0_50": norm_stable_moduli
        >= REQUIRED_MODULUS_COUNT,
    }
    supported = all(conditions.values())
    return {
        "thresholds": {
            "minimum_global_oriented_coherence": MIN_GLOBAL_ORIENTED_COHERENCE,
            "maximum_restricted_permutation_p_value": MAX_PERMUTATION_P_VALUE,
            "minimum_modulus_oriented_coherence": MIN_MODULUS_ORIENTED_COHERENCE,
            "minimum_modulus_median_signed_cosine": MIN_MODULUS_MEDIAN_SIGNED_COSINE,
            "maximum_modulus_functional_norm_cv": MAX_MODULUS_NORM_CV,
            "required_modulus_count": REQUIRED_MODULUS_COUNT,
        },
        "coherent_modulus_count": coherent_moduli,
        "positive_median_cosine_modulus_count": positive_median_moduli,
        "norm_stable_modulus_count": norm_stable_moduli,
        "conditions": conditions,
        "supported": supported,
        "decision": (
            "stable_oriented_linear_cancellation_functional_on_finite_range"
            if supported
            else "no_stable_oriented_linear_cancellation_functional_under_locked_rule"
        ),
    }


def public_fold(fold: Mapping) -> dict:
    return {key: value for key, value in fold.items() if not key.startswith("_")}


def build_result(
    pass028_path: Path,
    pass032_path: Path,
    permutation_iterations: int = PERMUTATION_ITERATIONS,
) -> dict:
    if sha256_file(pass028_path) != EXPECTED_PASS028_SHA256:
        raise ValueError("PASS028 hash mismatch")
    locked = load_locked_pass032(pass032_path)
    p32 = load_pass032_module()
    p31 = p32.load_pass031_module()
    p30 = p31.load_pass030_module()
    p29 = p30.load_pass029_module()
    vectors = p29.load_vectors(pass028_path)
    centered = p29.centered_vectors(vectors)
    folds = [
        functional_from_fold(centered, locked_fold, p32, p30, p29)
        for locked_fold in locked["folds"]
    ]
    if [(row["r"], row["heldout_exp"]) for row in folds] != [
        (int(row["r"]), int(row["heldout_exp"])) for row in locked["folds"]
    ]:
        raise AssertionError("Fold order mismatch")
    by_modulus, global_metrics = stability_from_functionals(
        folds, p29.PRIMARY_MODULI
    )
    raw_coefficients = p32.raw_cancellation_coefficients(centered, p29)
    permutation = restricted_permutation_null(
        folds,
        raw_coefficients,
        p29.EXPS,
        p29.PRIMARY_MODULI,
        p32,
        iterations=permutation_iterations,
        seed=PERMUTATION_SEED,
    )
    decision = decision_summary(by_modulus, global_metrics, permutation)
    pass032_skill_by_modulus = {
        int(row["r"]): float(row["predicted"]["scalar_skill"])
        for row in locked["decision"]["by_modulus"]
    }
    return {
        "pass": "PASS033",
        "title": "Jackknife stability of the oriented linear cancellation functional",
        "classification": "finite leave-one-window-out functional-stability diagnostic",
        "interpretation_guard": (
            "The five functionals per modulus have overlapping training windows. "
            "This measures deletion sensitivity, not independent replication."
        ),
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "exps": list(p29.EXPS),
            "moduli": list(p29.PRIMARY_MODULI),
            "permutation_iterations": permutation_iterations,
            "permutation_seed": PERMUTATION_SEED,
            "functional": "g_(r,e) = V_(r,e) beta_(r,e) in the common orbit space",
            "orientation_rule": "signed; no post-hoc sign alignment",
            "input_sha256": {
                pass028_path.name: sha256_file(pass028_path),
                pass032_path.name: sha256_file(pass032_path),
            },
        },
        "global_stability": global_metrics,
        "by_modulus": by_modulus,
        "restricted_permutation_null": permutation,
        "decision": decision,
        "secondary": {
            "pass032_global_scalar_skill": locked["predicted_global"]["scalar_skill"],
            "correlation_modulus_oriented_coherence_with_pass032_scalar_skill": correlation(
                [row["oriented_coherence"] for row in by_modulus],
                [pass032_skill_by_modulus[int(row["r"])] for row in by_modulus],
            ),
            "pass032_scalar_skill_by_modulus": pass032_skill_by_modulus,
        },
        "safety": {
            "fold_count": len(folds),
            "maximum_prediction_error_vs_pass032": max(
                fold["maximum_prediction_error_vs_pass032"] for fold in folds
            ),
            "maximum_actual_scalar_error_vs_pass032": max(
                fold["maximum_actual_scalar_error_vs_pass032"] for fold in folds
            ),
            "maximum_sum_perpendicular_error": max(
                fold["sum_perpendicular_error"] for fold in folds
            ),
            "minimum_functional_norm": min(
                fold["functional_norm"] for fold in folds
            ),
            "all_design_ranks_full": all(
                fold["design_rank"] == fold["rank_d"] for fold in folds
            ),
        },
        "folds": [public_fold(fold) for fold in folds],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pass028", type=Path, default=default_pass028_path())
    parser.add_argument("--pass032", type=Path, default=default_pass032_path())
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument(
        "--permutation-iterations", type=int, default=PERMUTATION_ITERATIONS
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(
        args.pass028,
        args.pass032,
        permutation_iterations=args.permutation_iterations,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"PASS033 result: {args.output}")
    print(
        "oriented coherence=",
        f'{result["global_stability"]["mean_oriented_coherence"]:.6f}',
        "axis coherence=",
        f'{result["global_stability"]["mean_axis_coherence"]:.6f}',
        "permutation p=",
        f'{result["restricted_permutation_null"]["oriented_coherence_primary"]["one_sided_p_value"]:.6f}',
    )
    print("decision:", result["decision"]["decision"])


if __name__ == "__main__":
    main()
