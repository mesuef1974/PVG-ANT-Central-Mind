#!/usr/bin/env python3
"""PASS032: predict the cancellation coefficient from amplitude coordinates.

For each held-out window and modulus, keep the locked PASS031 amplitude rank,
learn the amplitude basis and a no-intercept least-squares coupling only from
the other four windows, and predict the coefficient in the normalized sum
direction.  A restricted within-character window permutation tests whether
the held-out scalar skill exceeds accidental amplitude/cancellation alignment.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import math
import statistics
import sys
from pathlib import Path
from typing import Mapping, Sequence

import numpy as np


EXPECTED_PASS028_SHA256 = (
    "9088e373aa18fdef6cdc8a7a0b6b1fb8680f5dd08653a12699a787118f6f4eab"
)
EXPECTED_PASS031_SHA256 = (
    "65664dbd37fa3b2cee4b87d659b2899fabe80045cc579445510fba6e1476b272"
)
PERMUTATION_ITERATIONS = 5000
PERMUTATION_SEED = 320719
MIN_GLOBAL_SCALAR_SKILL = 0.25
MIN_GLOBAL_CORRELATION = 0.50
MAX_PERMUTATION_P_VALUE = 0.01
REQUIRED_POSITIVE_MODULI = 5
REQUIRED_NONNEGATIVE_WINDOWS = 4


def load_pass031_module():
    try:
        return importlib.import_module("avrg_pass031")
    except ModuleNotFoundError:
        sibling = Path(__file__).resolve().parents[1] / "pass031"
        sys.path.insert(0, str(sibling))
        return importlib.import_module("avrg_pass031")


def default_pass028_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass028_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass028" / "avrg_pass028_results.json"


def default_pass031_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass031_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass031" / "avrg_pass031_results.json"


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_results = here.parent / "results"
    if archive_results.is_dir():
        return archive_results / "avrg_pass032_results.json"
    return here / "avrg_pass032_results.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_locked_pass031(path: Path) -> dict:
    observed = sha256_file(path)
    if observed != EXPECTED_PASS031_SHA256:
        raise ValueError(f"PASS031 hash mismatch: {observed}")
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if data.get("pass") != "PASS031" or len(data.get("folds", [])) != 35:
        raise ValueError("Invalid PASS031 result")
    return data


def least_squares_coupling(
    z_train: np.ndarray, c_train: np.ndarray, z_test: np.ndarray
) -> tuple[np.ndarray, np.ndarray, int, float]:
    """Fit the locked no-intercept minimum-norm linear coupling."""
    if z_train.ndim != 2 or z_test.ndim != 2 or c_train.ndim != 1:
        raise ValueError("Invalid coupling arrays")
    if z_train.shape[0] != c_train.size or z_train.shape[1] != z_test.shape[1]:
        raise ValueError("Incompatible coupling arrays")
    beta, _, rank, singular_values = np.linalg.lstsq(z_train, c_train, rcond=None)
    prediction = z_test @ beta
    if singular_values.size == 0 or singular_values[-1] == 0:
        condition_number = float("inf")
    else:
        condition_number = float(singular_values[0] / singular_values[-1])
    return beta, prediction, int(rank), condition_number


def forecast_metrics(
    x_test: np.ndarray,
    vector_prediction: np.ndarray,
    scalar_prediction: np.ndarray,
) -> dict:
    if x_test.shape != vector_prediction.shape:
        raise ValueError("Vector prediction shape mismatch")
    target_scalar = np.sum(x_test, axis=1)
    if scalar_prediction.shape != target_scalar.shape:
        raise ValueError("Scalar prediction shape mismatch")
    vector_ss = float(np.sum(x_test * x_test))
    vector_sse = float(np.sum((x_test - vector_prediction) ** 2))
    scalar_ss = float(np.sum(target_scalar * target_scalar))
    scalar_sse = float(np.sum((target_scalar - scalar_prediction) ** 2))
    if vector_ss <= 0 or scalar_ss <= 0:
        raise ValueError("Degenerate forecast target")
    return {
        "vector_ss": vector_ss,
        "vector_sse": vector_sse,
        "vector_skill": 1.0 - vector_sse / vector_ss,
        "scalar_ss": scalar_ss,
        "scalar_sse": scalar_sse,
        "scalar_skill": 1.0 - scalar_sse / scalar_ss,
    }


def amplitude_basis(x_train: np.ndarray, rank_d: int, p30) -> tuple[np.ndarray, np.ndarray]:
    augmented, sum_direction = p30.sum_aware_basis(x_train, rank_d + 1)
    basis = augmented[:, 1:]
    orthogonality_error = float(np.max(np.abs(basis.T @ basis - np.eye(rank_d))))
    perpendicular_error = float(np.max(np.abs(basis.T @ sum_direction)))
    if orthogonality_error > 1e-12 or perpendicular_error > 1e-12:
        raise AssertionError("Amplitude basis safety check failed")
    return basis, sum_direction


def analyze_fold(
    centered: Mapping,
    locked_fold: Mapping,
    p30,
    p29,
) -> dict:
    r = int(locked_fold["r"])
    heldout_exp = int(locked_fold["heldout_exp"])
    rank_d = int(locked_fold["rank_d"])
    modes = p29.representative_modes(r)
    training_exps = [exp for exp in p29.EXPS if exp != heldout_exp]
    x_train, x_test = p30.build_train_test(centered, r, heldout_exp, p29)
    basis, sum_direction = amplitude_basis(x_train, rank_d, p30)
    z_train = x_train @ basis
    z_test = x_test @ basis
    c_train = x_train @ sum_direction
    c_test = x_test @ sum_direction
    beta, c_prediction, design_rank, condition_number = least_squares_coupling(
        z_train, c_train, z_test
    )
    q = x_test.shape[1]
    amplitude_prediction = z_test @ basis.T
    predicted_vector = amplitude_prediction + c_prediction[:, None] * sum_direction
    oracle_vector = amplitude_prediction + c_test[:, None] * sum_direction
    predicted_scalar = math.sqrt(q) * c_prediction
    actual_scalar = math.sqrt(q) * c_test
    zero_scalar = np.zeros_like(actual_scalar)
    predicted = forecast_metrics(x_test, predicted_vector, predicted_scalar)
    amplitude_only = forecast_metrics(x_test, amplitude_prediction, zero_scalar)
    oracle = forecast_metrics(x_test, oracle_vector, actual_scalar)
    locked_oracle = locked_fold["augmented_metrics"]
    if abs(oracle["vector_skill"] - locked_oracle["vector_skill"]) > 1e-12:
        raise AssertionError(f"PASS031 oracle mismatch at {(r, heldout_exp)}")
    if abs(amplitude_only["scalar_skill"]) > 1e-12:
        raise AssertionError("Zero baseline scalar skill is not zero")
    return {
        "r": r,
        "heldout_exp": heldout_exp,
        "training_exps": training_exps,
        "modes": modes,
        "rank_d": rank_d,
        "orbit_count": q,
        "training_row_count": int(x_train.shape[0]),
        "test_row_count": int(x_test.shape[0]),
        "design_rank": design_rank,
        "design_condition_number": condition_number,
        "coefficient_l2_norm": float(np.linalg.norm(beta)),
        "predicted_metrics": predicted,
        "amplitude_only_metrics": amplitude_only,
        "oracle_metrics": oracle,
        "vector_skill_loss_vs_oracle": oracle["vector_skill"] - predicted["vector_skill"],
        "actual_scalar": actual_scalar.tolist(),
        "predicted_scalar": predicted_scalar.tolist(),
        "sign_correct_count": int(
            np.count_nonzero(np.sign(actual_scalar) == np.sign(predicted_scalar))
        ),
        "_z_train": z_train,
        "_z_test": z_test,
        "_raw_sum_direction": sum_direction,
    }


def aggregate_metrics(folds: Sequence[dict], field: str) -> dict:
    vector_ss = sum(fold[field]["vector_ss"] for fold in folds)
    vector_sse = sum(fold[field]["vector_sse"] for fold in folds)
    scalar_ss = sum(fold[field]["scalar_ss"] for fold in folds)
    scalar_sse = sum(fold[field]["scalar_sse"] for fold in folds)
    return {
        "fold_count": len(folds),
        "vector_ss": vector_ss,
        "vector_sse": vector_sse,
        "vector_skill": 1.0 - vector_sse / vector_ss,
        "scalar_ss": scalar_ss,
        "scalar_sse": scalar_sse,
        "scalar_skill": 1.0 - scalar_sse / scalar_ss,
    }


def prediction_diagnostics(folds: Sequence[dict]) -> dict:
    actual = np.asarray(
        [value for fold in folds for value in fold["actual_scalar"]], dtype=float
    )
    predicted = np.asarray(
        [value for fold in folds for value in fold["predicted_scalar"]], dtype=float
    )
    if actual.size < 2 or np.std(actual) == 0 or np.std(predicted) == 0:
        correlation = float("nan")
    else:
        correlation = float(np.corrcoef(actual, predicted)[0, 1])
    nonzero = actual != 0
    sign_accuracy = float(np.mean(np.sign(actual[nonzero]) == np.sign(predicted[nonzero])))
    calibration = np.linalg.lstsq(
        np.column_stack([np.ones(predicted.size), predicted]), actual, rcond=None
    )[0]
    return {
        "row_count": int(actual.size),
        "pearson_correlation": correlation,
        "sign_accuracy": sign_accuracy,
        "calibration_intercept_actual_on_predicted": float(calibration[0]),
        "calibration_slope_actual_on_predicted": float(calibration[1]),
        "actual_rms": float(np.sqrt(np.mean(actual * actual))),
        "predicted_rms": float(np.sqrt(np.mean(predicted * predicted))),
    }


def raw_cancellation_coefficients(centered: Mapping, p29) -> dict:
    output = {}
    for r in p29.PRIMARY_MODULI:
        q = (r - 1) // 2
        direction = np.ones(q, dtype=float) / math.sqrt(q)
        for k in p29.representative_modes(r):
            output[(r, k)] = np.asarray(
                [centered[(exp, r, k)] @ direction for exp in p29.EXPS],
                dtype=float,
            )
    return output


def permuted_targets_for_fold(
    permuted_raw: Mapping,
    fold: Mapping,
    exps: Sequence[int],
) -> tuple[np.ndarray, np.ndarray]:
    r = int(fold["r"])
    heldout = int(fold["heldout_exp"])
    modes = [int(k) for k in fold["modes"]]
    exp_to_index = {int(exp): index for index, exp in enumerate(exps)}
    train_exps = [int(exp) for exp in exps if int(exp) != heldout]
    means = {
        k: float(
            np.mean([permuted_raw[(r, k)][exp_to_index[exp]] for exp in train_exps])
        )
        for k in modes
    }
    c_train = np.asarray(
        [
            permuted_raw[(r, k)][exp_to_index[exp]] - means[k]
            for exp in train_exps
            for k in modes
        ],
        dtype=float,
    )
    c_test = np.asarray(
        [permuted_raw[(r, k)][exp_to_index[heldout]] - means[k] for k in modes],
        dtype=float,
    )
    return c_train, c_test


def restricted_permutation_null(
    folds: Sequence[dict],
    raw_coefficients: Mapping,
    exps: Sequence[int],
    iterations: int = PERMUTATION_ITERATIONS,
    seed: int = PERMUTATION_SEED,
) -> dict:
    rng = np.random.default_rng(seed)
    observed_ss = sum(fold["predicted_metrics"]["scalar_ss"] for fold in folds)
    observed_sse = sum(fold["predicted_metrics"]["scalar_sse"] for fold in folds)
    observed_skill = 1.0 - observed_sse / observed_ss
    samples = np.empty(iterations, dtype=float)
    maximum_denominator_error = 0.0
    keys = sorted(raw_coefficients)
    for iteration in range(iterations):
        permuted = {
            key: np.asarray(raw_coefficients[key])[rng.permutation(len(exps))]
            for key in keys
        }
        scalar_ss = 0.0
        scalar_sse = 0.0
        for fold in folds:
            c_train, c_test = permuted_targets_for_fold(permuted, fold, exps)
            _, c_prediction, _, _ = least_squares_coupling(
                fold["_z_train"], c_train, fold["_z_test"]
            )
            q = int(fold["orbit_count"])
            scalar_ss += q * float(np.sum(c_test * c_test))
            scalar_sse += q * float(np.sum((c_test - c_prediction) ** 2))
        maximum_denominator_error = max(
            maximum_denominator_error, abs(scalar_ss - observed_ss)
        )
        samples[iteration] = 1.0 - scalar_sse / scalar_ss
    exceedances = int(np.count_nonzero(samples >= observed_skill))
    return {
        "iterations": iterations,
        "seed": seed,
        "restriction": "permute five windows independently within each (r,k)",
        "observed_scalar_skill": observed_skill,
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
        "maximum_denominator_invariance_error": maximum_denominator_error,
    }


def grouped_results(folds: Sequence[dict], key: str, values: Sequence[int]) -> list[dict]:
    output = []
    for value in values:
        local = [fold for fold in folds if int(fold[key]) == int(value)]
        diagnostics = prediction_diagnostics(local)
        output.append(
            {
                key: int(value),
                "predicted": aggregate_metrics(local, "predicted_metrics"),
                "amplitude_only": aggregate_metrics(local, "amplitude_only_metrics"),
                "oracle": aggregate_metrics(local, "oracle_metrics"),
                "pearson_correlation": diagnostics["pearson_correlation"],
                "sign_accuracy": diagnostics["sign_accuracy"],
            }
        )
    return output


def decision_summary(
    folds: Sequence[dict],
    predicted: Mapping,
    oracle: Mapping,
    diagnostics: Mapping,
    permutation: Mapping,
    p29,
) -> dict:
    by_modulus = grouped_results(folds, "r", p29.PRIMARY_MODULI)
    by_window = grouped_results(folds, "heldout_exp", p29.EXPS)
    positive_moduli = sum(row["predicted"]["scalar_skill"] > 0 for row in by_modulus)
    nonnegative_windows = sum(
        row["predicted"]["scalar_skill"] >= 0 for row in by_window
    )
    conditions = {
        "global_scalar_skill_at_least_0_25": predicted["scalar_skill"]
        >= MIN_GLOBAL_SCALAR_SKILL,
        "global_pearson_correlation_at_least_0_50": diagnostics[
            "pearson_correlation"
        ]
        >= MIN_GLOBAL_CORRELATION,
        "restricted_permutation_p_at_most_0_01": permutation["one_sided_p_value"]
        <= MAX_PERMUTATION_P_VALUE,
        "at_least_five_moduli_positive_scalar_skill": positive_moduli
        >= REQUIRED_POSITIVE_MODULI,
        "at_least_four_windows_nonnegative_scalar_skill": nonnegative_windows
        >= REQUIRED_NONNEGATIVE_WINDOWS,
    }
    supported = all(conditions.values())
    return {
        "thresholds": {
            "minimum_global_scalar_skill": MIN_GLOBAL_SCALAR_SKILL,
            "minimum_global_pearson_correlation": MIN_GLOBAL_CORRELATION,
            "maximum_restricted_permutation_p_value": MAX_PERMUTATION_P_VALUE,
            "required_positive_modulus_count": REQUIRED_POSITIVE_MODULI,
            "required_nonnegative_window_count": REQUIRED_NONNEGATIVE_WINDOWS,
        },
        "positive_modulus_count": positive_moduli,
        "nonnegative_window_count": nonnegative_windows,
        "vector_skill_loss_vs_oracle": oracle["vector_skill"]
        - predicted["vector_skill"],
        "positive_scalar_skill_fold_count": sum(
            fold["predicted_metrics"]["scalar_skill"] > 0 for fold in folds
        ),
        "conditions": conditions,
        "supported": supported,
        "decision": (
            "finite_conditional_linear_cancellation_coupling_supported"
            if supported
            else "no_stable_linear_coupling_support_under_locked_rule"
        ),
        "by_modulus": by_modulus,
        "by_heldout_window": by_window,
    }


def public_fold(fold: Mapping) -> dict:
    return {key: value for key, value in fold.items() if not key.startswith("_")}


def build_result(
    pass028_path: Path,
    pass031_path: Path,
    permutation_iterations: int = PERMUTATION_ITERATIONS,
) -> dict:
    if sha256_file(pass028_path) != EXPECTED_PASS028_SHA256:
        raise ValueError("PASS028 hash mismatch")
    locked = load_locked_pass031(pass031_path)
    p31 = load_pass031_module()
    p30 = p31.load_pass030_module()
    p29 = p30.load_pass029_module()
    vectors = p29.load_vectors(pass028_path)
    centered = p29.centered_vectors(vectors)
    locked_folds = {
        (int(row["r"]), int(row["heldout_exp"])): row for row in locked["folds"]
    }
    folds = [
        analyze_fold(centered, locked_folds[(r, exp)], p30, p29)
        for r in p29.PRIMARY_MODULI
        for exp in p29.EXPS
    ]
    predicted = aggregate_metrics(folds, "predicted_metrics")
    amplitude_only = aggregate_metrics(folds, "amplitude_only_metrics")
    oracle = aggregate_metrics(folds, "oracle_metrics")
    if abs(oracle["vector_skill"] - locked["augmented_global"]["vector_skill"]) > 1e-12:
        raise AssertionError("Global PASS031 oracle mismatch")
    if abs(oracle["scalar_skill"] - 1.0) > 1e-12:
        raise AssertionError("Oracle scalar skill is not one")
    if abs(amplitude_only["scalar_skill"]) > 1e-12:
        raise AssertionError("Amplitude-only scalar skill is not zero")
    diagnostics = prediction_diagnostics(folds)
    raw_coefficients = raw_cancellation_coefficients(centered, p29)
    permutation = restricted_permutation_null(
        folds,
        raw_coefficients,
        p29.EXPS,
        iterations=permutation_iterations,
        seed=PERMUTATION_SEED,
    )
    decision = decision_summary(
        folds, predicted, oracle, diagnostics, permutation, p29
    )
    return {
        "pass": "PASS032",
        "title": "Held-out prediction of the cancellation coefficient from amplitude coordinates",
        "classification": "finite conditional held-out linear-coupling diagnostic",
        "interpretation_guard": (
            "Held-out amplitude coordinates still require observing the held-out orbit vector. "
            "This predicts only its cancellation coefficient conditionally on those coordinates."
        ),
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "exps": list(p29.EXPS),
            "moduli": list(p29.PRIMARY_MODULI),
            "permutation_iterations": permutation_iterations,
            "permutation_seed": PERMUTATION_SEED,
            "model": "per-modulus outer-fold no-intercept minimum-norm least squares",
            "rank_rule": "locked PASS031 amplitude rank d",
            "input_sha256": {
                pass028_path.name: sha256_file(pass028_path),
                pass031_path.name: sha256_file(pass031_path),
            },
        },
        "predicted_global": predicted,
        "amplitude_only_global": amplitude_only,
        "oracle_pass031_global": oracle,
        "prediction_diagnostics": diagnostics,
        "restricted_permutation_null": permutation,
        "decision": decision,
        "safety": {
            "fold_count": len(folds),
            "all_design_ranks_full": all(
                fold["design_rank"] == fold["rank_d"] for fold in folds
            ),
            "minimum_design_rank_fraction": min(
                fold["design_rank"] / fold["rank_d"] for fold in folds
            ),
            "maximum_design_condition_number": max(
                fold["design_condition_number"] for fold in folds
            ),
            "maximum_oracle_fold_vector_skill_error_vs_pass031": max(
                abs(
                    fold["oracle_metrics"]["vector_skill"]
                    - locked_folds[(fold["r"], fold["heldout_exp"])][
                        "augmented_metrics"
                    ]["vector_skill"]
                )
                for fold in folds
            ),
        },
        "folds": [public_fold(fold) for fold in folds],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pass028", type=Path, default=default_pass028_path())
    parser.add_argument("--pass031", type=Path, default=default_pass031_path())
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument(
        "--permutation-iterations",
        type=int,
        default=PERMUTATION_ITERATIONS,
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(
        args.pass028,
        args.pass031,
        permutation_iterations=args.permutation_iterations,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"PASS032 result: {args.output}")
    print(
        "scalar skill=",
        f'{result["predicted_global"]["scalar_skill"]:.6f}',
        "correlation=",
        f'{result["prediction_diagnostics"]["pearson_correlation"]:.6f}',
        "permutation p=",
        f'{result["restricted_permutation_null"]["one_sided_p_value"]:.6f}',
    )
    print("decision:", result["decision"]["decision"])


if __name__ == "__main__":
    main()
