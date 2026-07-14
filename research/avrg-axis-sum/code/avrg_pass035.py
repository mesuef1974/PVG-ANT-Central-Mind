#!/usr/bin/env python3
"""PASS035: separate orientation failure from gain/calibration failure.

PASS034 is reconstructed exactly without rerunning its permutation null.  For each
modulus and each disjoint-block transfer direction, this pass decomposes raw
prediction error into:

- signed direction alignment,
- signed and positive target-oracle gains,
- leave-one-target-window-out signed and positive gain calibration.

Target-oracle and target-window calibration are diagnostics, not source-only
held-out predictions.  Finite computation only; no asymptotic or Goldbach claim.
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
EXPECTED_PASS032_SHA256 = (
    "1168d02a0d8640a3371d15769b42daf67acf27843a4e67c27dbbec8219a2a787"
)
EXPECTED_PASS033_SHA256 = (
    "9d0641a61af4f9839ed210c6e4fdcac120935cf9d3f4699c1d56b1713f99c8c8"
)
EXPECTED_PASS034_SHA256 = (
    "fa92d9fa771740dd6083bf9bb6dbd530219e5c25bffee54991db4f50900196ce"
)
FORMULA_TOLERANCE = 1e-12
REPRODUCTION_TOLERANCE = 1e-12

MIN_CALIBRATION_ORACLE_POSITIVE_SKILL = 0.50
MIN_CALIBRATION_CV_POSITIVE_SKILL = 0.10
MIN_POSITIVE_DIRECTION_COUNT = 10
MIN_NONNEGATIVE_MODULUS_COUNT = 5
MAX_MEDIAN_LOG_RECIPROCITY = math.log(2.0)
MIN_RECIPROCITY_MODULUS_COUNT = 4

MIN_ORIENTATION_SIGNED_ORACLE_SKILL = 0.50
MAX_ORIENTATION_POSITIVE_ORACLE_SKILL = 0.20
MIN_NEGATIVE_GAIN_COUNT = 5
MIN_ORIENTATION_CV_SIGNED_SKILL = 0.10


def load_module(name: str):
    try:
        return importlib.import_module(name)
    except ModuleNotFoundError:
        here = Path(__file__).resolve().parent
        if str(here) not in sys.path:
            sys.path.insert(0, str(here))
        return importlib.import_module(name)


def default_result_path(filename: str) -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / filename
    if archive.exists():
        return archive
    return here / filename


def default_pass028_path() -> Path:
    return default_result_path("avrg_pass028_results.json")


def default_pass032_path() -> Path:
    return default_result_path("avrg_pass032_results.json")


def default_pass033_path() -> Path:
    return default_result_path("avrg_pass033_results.json")


def default_pass034_path() -> Path:
    return default_result_path("avrg_pass034_results.json")


def default_output_path() -> Path:
    return default_result_path("avrg_pass035_results.json")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_locked_json(path: Path, expected_sha256: str, expected_pass: str) -> dict:
    observed = sha256_file(path)
    if observed != expected_sha256:
        raise ValueError(f"{expected_pass} hash mismatch: {observed}")
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if data.get("pass") != expected_pass:
        raise ValueError(f"Invalid {expected_pass} result")
    return data


def scalar_components(actual: np.ndarray, predicted: np.ndarray) -> tuple[float, float]:
    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)
    if actual.shape != predicted.shape:
        raise ValueError("Actual and predicted arrays must have the same shape")
    ss = float(np.sum(actual * actual))
    sse = float(np.sum((actual - predicted) ** 2))
    if ss <= 0:
        raise ValueError("Degenerate target energy")
    return ss, sse


def gain_from_training(actual: np.ndarray, predicted: np.ndarray) -> float:
    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)
    denominator = float(np.sum(predicted * predicted))
    if denominator <= 1e-30:
        raise ValueError("Degenerate prediction energy for gain fit")
    return float(np.dot(actual, predicted) / denominator)


def oracle_gain_metrics(actual: np.ndarray, predicted: np.ndarray) -> dict:
    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)
    ss, raw_sse = scalar_components(actual, predicted)
    actual_norm = float(np.linalg.norm(actual))
    predicted_norm = float(np.linalg.norm(predicted))
    if predicted_norm <= 1e-15:
        raise ValueError("Degenerate prediction vector")
    signed_cosine = float(np.dot(actual, predicted) / (actual_norm * predicted_norm))
    signed_gain = gain_from_training(actual, predicted)
    positive_gain = max(0.0, signed_gain)
    signed_prediction = signed_gain * predicted
    positive_prediction = positive_gain * predicted
    _, signed_sse = scalar_components(actual, signed_prediction)
    _, positive_sse = scalar_components(actual, positive_prediction)
    raw_skill = 1.0 - raw_sse / ss
    signed_oracle_skill = 1.0 - signed_sse / ss
    positive_oracle_skill = 1.0 - positive_sse / ss
    expected_signed = signed_cosine * signed_cosine
    expected_positive = max(signed_cosine, 0.0) ** 2
    signed_formula_error = abs(signed_oracle_skill - expected_signed)
    positive_formula_error = abs(positive_oracle_skill - expected_positive)
    if signed_formula_error > FORMULA_TOLERANCE:
        raise AssertionError(f"Signed oracle identity failed: {signed_formula_error}")
    if positive_formula_error > FORMULA_TOLERANCE:
        raise AssertionError(f"Positive oracle identity failed: {positive_formula_error}")
    return {
        "row_count": int(actual.size),
        "target_ss": ss,
        "raw_sse": raw_sse,
        "raw_skill": raw_skill,
        "signed_cosine": signed_cosine,
        "absolute_cosine": abs(signed_cosine),
        "signed_gain": signed_gain,
        "positive_gain": positive_gain,
        "signed_oracle_sse": signed_sse,
        "signed_oracle_skill": signed_oracle_skill,
        "positive_oracle_sse": positive_sse,
        "positive_oracle_skill": positive_oracle_skill,
        "signed_formula_error": signed_formula_error,
        "positive_formula_error": positive_formula_error,
        "actual_rms": float(np.sqrt(np.mean(actual * actual))),
        "predicted_rms": float(np.sqrt(np.mean(predicted * predicted))),
    }


def target_window_slices(row_count: int, target_exps: Sequence[int], mode_count: int):
    target_exps = tuple(int(exp) for exp in target_exps)
    if len(target_exps) != 3:
        raise ValueError("PASS035 requires exactly three target windows")
    if row_count != len(target_exps) * mode_count:
        raise ValueError("Target row ordering is inconsistent with target windows")
    output = []
    for index, exp in enumerate(target_exps):
        start = index * mode_count
        stop = start + mode_count
        output.append((exp, slice(start, stop)))
    return output


def leave_one_target_window_calibration(
    actual: np.ndarray,
    predicted: np.ndarray,
    target_exps: Sequence[int],
    mode_count: int,
) -> dict:
    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)
    windows = target_window_slices(actual.size, target_exps, mode_count)
    total_ss = 0.0
    signed_sse = 0.0
    positive_sse = 0.0
    folds = []
    for heldout_exp, heldout_slice in windows:
        test_mask = np.zeros(actual.size, dtype=bool)
        test_mask[heldout_slice] = True
        train_mask = ~test_mask
        if np.any(train_mask & test_mask):
            raise AssertionError("Training and held-out target rows overlap")
        signed_gain = gain_from_training(actual[train_mask], predicted[train_mask])
        positive_gain = max(0.0, signed_gain)
        y_test = actual[test_mask]
        p_test = predicted[test_mask]
        ss, fold_signed_sse = scalar_components(y_test, signed_gain * p_test)
        _, fold_positive_sse = scalar_components(y_test, positive_gain * p_test)
        total_ss += ss
        signed_sse += fold_signed_sse
        positive_sse += fold_positive_sse
        folds.append(
            {
                "heldout_exp": int(heldout_exp),
                "training_exps": [int(exp) for exp, _ in windows if exp != heldout_exp],
                "training_row_count": int(np.count_nonzero(train_mask)),
                "heldout_row_count": int(np.count_nonzero(test_mask)),
                "signed_gain": signed_gain,
                "positive_gain": positive_gain,
                "target_ss": ss,
                "signed_sse": fold_signed_sse,
                "positive_sse": fold_positive_sse,
                "signed_skill": 1.0 - fold_signed_sse / ss,
                "positive_skill": 1.0 - fold_positive_sse / ss,
            }
        )
    signed_gains = [row["signed_gain"] for row in folds]
    positive_gains = [row["positive_gain"] for row in folds]
    return {
        "target_ss": total_ss,
        "signed_sse": signed_sse,
        "positive_sse": positive_sse,
        "signed_skill": 1.0 - signed_sse / total_ss,
        "positive_skill": 1.0 - positive_sse / total_ss,
        "signed_gain_population_sd": float(np.std(signed_gains)),
        "positive_gain_population_sd": float(np.std(positive_gains)),
        "folds": folds,
    }


def reproduce_pass034(
    pass028_path: Path,
    pass032_path: Path,
    pass033_path: Path,
    locked034: Mapping,
    progress: bool = False,
):
    p34 = load_module("avrg_pass034")
    if sha256_file(pass028_path) != EXPECTED_PASS028_SHA256:
        raise ValueError("PASS028 hash mismatch")
    if sha256_file(pass032_path) != EXPECTED_PASS032_SHA256:
        raise ValueError("PASS032 hash mismatch")
    if sha256_file(pass033_path) != EXPECTED_PASS033_SHA256:
        raise ValueError("PASS033 hash mismatch")
    p28 = p34.load_module("avrg_pass028")
    p29 = p34.load_module("avrg_pass029")
    p32 = p34.load_module("avrg_pass032")
    e14_rows, e14_diagnostics = p34.scan_e14(p28, progress=progress)
    vectors = p34.combine_vectors(pass028_path, e14_rows, p29)
    centered = p34.centered_vectors(vectors, p29)
    by_modulus, global_metrics, models = p34.observed_analysis(centered, p29, p32)

    errors = []
    for key in (
        "mean_signed_functional_cosine",
        "mean_absolute_functional_cosine",
        "bidirectional_scalar_ss",
        "bidirectional_scalar_sse",
        "bidirectional_scalar_skill",
        "bidirectional_sign_accuracy",
        "bidirectional_pearson_correlation",
    ):
        errors.append(abs(float(global_metrics[key]) - float(locked034["global"][key])))
    locked_by_r = {int(row["r"]): row for row in locked034["by_modulus"]}
    for row in by_modulus:
        locked = locked_by_r[int(row["r"])]
        for key in (
            "signed_functional_cosine",
            "absolute_functional_cosine",
            "bidirectional_scalar_ss",
            "bidirectional_scalar_sse",
            "bidirectional_scalar_skill",
        ):
            errors.append(abs(float(row[key]) - float(locked[key])))
    maximum_error = float(max(errors, default=0.0))
    if maximum_error > REPRODUCTION_TOLERANCE:
        raise AssertionError(f"PASS034 reproduction error: {maximum_error}")
    if not e14_diagnostics["passed"]:
        raise AssertionError("Reconstructed e=14 safety gate failed")
    return p34, p29, by_modulus, global_metrics, models, e14_diagnostics, maximum_error


def direction_label(model: Mapping) -> str:
    block = tuple(int(exp) for exp in model["block"])
    target = tuple(int(exp) for exp in model["target_block"])
    if block == (14, 15, 16) and target == (17, 18, 19):
        return "early_to_late"
    if block == (17, 18, 19) and target == (14, 15, 16):
        return "late_to_early"
    raise ValueError(f"Unexpected PASS034 block direction: {block} -> {target}")


def analyze_model(model: Mapping, p34) -> dict:
    cross = p34.cross_metrics(model)
    actual = np.asarray(cross["_actual"], dtype=float)
    predicted = np.asarray(cross["_predicted"], dtype=float)
    oracle = oracle_gain_metrics(actual, predicted)
    calibration = leave_one_target_window_calibration(
        actual,
        predicted,
        model["target_block"],
        len(model["modes"]),
    )
    return {
        "r": int(model["r"]),
        "direction": direction_label(model),
        "source_exps": [int(exp) for exp in model["block"]],
        "target_exps": [int(exp) for exp in model["target_block"]],
        "mode_count": len(model["modes"]),
        "selected_rank": int(model["selected_rank"]),
        "functional_norm": float(model["functional_norm"]),
        "oracle": oracle,
        "target_window_cross_calibration": calibration,
    }


def aggregate_skill(rows: Sequence[Mapping], sse_path: Sequence[str]) -> tuple[float, float, float]:
    total_ss = sum(float(row["oracle"]["target_ss"]) for row in rows)
    total_sse = 0.0
    for row in rows:
        current: Mapping = row
        for key in sse_path:
            current = current[key]  # type: ignore[assignment]
        total_sse += float(current)
    return total_ss, total_sse, 1.0 - total_sse / total_ss


def combine_direction_rows(direction_rows: Sequence[Mapping]) -> tuple[list[dict], dict]:
    by_r: dict[int, list[Mapping]] = {}
    for row in direction_rows:
        by_r.setdefault(int(row["r"]), []).append(row)
    by_modulus = []
    for r in sorted(by_r):
        local = sorted(by_r[r], key=lambda row: str(row["direction"]))
        if len(local) != 2:
            raise AssertionError(f"Expected two transfer directions for r={r}")
        total_ss = sum(float(row["oracle"]["target_ss"]) for row in local)
        raw_sse = sum(float(row["oracle"]["raw_sse"]) for row in local)
        signed_oracle_sse = sum(
            float(row["oracle"]["signed_oracle_sse"]) for row in local
        )
        positive_oracle_sse = sum(
            float(row["oracle"]["positive_oracle_sse"]) for row in local
        )
        cv_signed_sse = sum(
            float(row["target_window_cross_calibration"]["signed_sse"])
            for row in local
        )
        cv_positive_sse = sum(
            float(row["target_window_cross_calibration"]["positive_sse"])
            for row in local
        )
        gains = {str(row["direction"]): float(row["oracle"]["positive_gain"]) for row in local}
        reciprocity = None
        if gains["early_to_late"] > 0 and gains["late_to_early"] > 0:
            reciprocity = abs(
                math.log(gains["early_to_late"] * gains["late_to_early"])
            )
        norms = {str(row["direction"]): float(row["functional_norm"]) for row in local}
        by_modulus.append(
            {
                "r": int(r),
                "directions": local,
                "bidirectional_target_ss": total_ss,
                "raw_sse": raw_sse,
                "raw_skill": 1.0 - raw_sse / total_ss,
                "signed_oracle_sse": signed_oracle_sse,
                "signed_oracle_skill": 1.0 - signed_oracle_sse / total_ss,
                "positive_oracle_sse": positive_oracle_sse,
                "positive_oracle_skill": 1.0 - positive_oracle_sse / total_ss,
                "cv_signed_sse": cv_signed_sse,
                "cv_signed_skill": 1.0 - cv_signed_sse / total_ss,
                "cv_positive_sse": cv_positive_sse,
                "cv_positive_skill": 1.0 - cv_positive_sse / total_ss,
                "positive_gain_reciprocity_log_error": reciprocity,
                "late_over_early_functional_norm_ratio": (
                    norms["late_to_early"] / norms["early_to_late"]
                ),
            }
        )

    total_ss = sum(float(row["bidirectional_target_ss"]) for row in by_modulus)
    raw_sse = sum(float(row["raw_sse"]) for row in by_modulus)
    signed_oracle_sse = sum(float(row["signed_oracle_sse"]) for row in by_modulus)
    positive_oracle_sse = sum(float(row["positive_oracle_sse"]) for row in by_modulus)
    cv_signed_sse = sum(float(row["cv_signed_sse"]) for row in by_modulus)
    cv_positive_sse = sum(float(row["cv_positive_sse"]) for row in by_modulus)
    reciprocity_values = [
        float(row["positive_gain_reciprocity_log_error"])
        for row in by_modulus
        if row["positive_gain_reciprocity_log_error"] is not None
    ]
    global_metrics = {
        "direction_count": len(direction_rows),
        "modulus_count": len(by_modulus),
        "target_ss": total_ss,
        "raw_sse": raw_sse,
        "raw_skill": 1.0 - raw_sse / total_ss,
        "signed_oracle_sse": signed_oracle_sse,
        "signed_oracle_skill": 1.0 - signed_oracle_sse / total_ss,
        "positive_oracle_sse": positive_oracle_sse,
        "positive_oracle_skill": 1.0 - positive_oracle_sse / total_ss,
        "cv_signed_sse": cv_signed_sse,
        "cv_signed_skill": 1.0 - cv_signed_sse / total_ss,
        "cv_positive_sse": cv_positive_sse,
        "cv_positive_skill": 1.0 - cv_positive_sse / total_ss,
        "positive_direction_count": sum(
            float(row["oracle"]["signed_cosine"]) > 0 for row in direction_rows
        ),
        "negative_signed_gain_count": sum(
            float(row["oracle"]["signed_gain"]) < 0 for row in direction_rows
        ),
        "nonnegative_modulus_cv_positive_skill_count": sum(
            float(row["cv_positive_skill"]) >= 0 for row in by_modulus
        ),
        "reciprocity_eligible_modulus_count": len(reciprocity_values),
        "median_positive_gain_reciprocity_log_error": (
            float(statistics.median(reciprocity_values))
            if reciprocity_values
            else None
        ),
        "mean_signed_cosine": float(
            statistics.fmean(float(row["oracle"]["signed_cosine"]) for row in direction_rows)
        ),
        "mean_absolute_cosine": float(
            statistics.fmean(float(row["oracle"]["absolute_cosine"]) for row in direction_rows)
        ),
    }
    return by_modulus, global_metrics


def classify_wall(global_metrics: Mapping) -> dict:
    reciprocity_median = global_metrics["median_positive_gain_reciprocity_log_error"]
    calibration_conditions = {
        "positive_oracle_skill_at_least_0_50": float(
            global_metrics["positive_oracle_skill"]
        )
        >= MIN_CALIBRATION_ORACLE_POSITIVE_SKILL,
        "cv_positive_skill_at_least_0_10": float(global_metrics["cv_positive_skill"])
        >= MIN_CALIBRATION_CV_POSITIVE_SKILL,
        "at_least_ten_positive_directions": int(global_metrics["positive_direction_count"])
        >= MIN_POSITIVE_DIRECTION_COUNT,
        "at_least_five_nonnegative_modulus_cv_positive_skills": int(
            global_metrics["nonnegative_modulus_cv_positive_skill_count"]
        )
        >= MIN_NONNEGATIVE_MODULUS_COUNT,
        "reciprocity_median_at_most_log2_with_four_moduli": (
            int(global_metrics["reciprocity_eligible_modulus_count"])
            >= MIN_RECIPROCITY_MODULUS_COUNT
            and reciprocity_median is not None
            and float(reciprocity_median) <= MAX_MEDIAN_LOG_RECIPROCITY
        ),
    }
    orientation_conditions = {
        "signed_oracle_skill_at_least_0_50": float(
            global_metrics["signed_oracle_skill"]
        )
        >= MIN_ORIENTATION_SIGNED_ORACLE_SKILL,
        "positive_oracle_skill_at_most_0_20": float(
            global_metrics["positive_oracle_skill"]
        )
        <= MAX_ORIENTATION_POSITIVE_ORACLE_SKILL,
        "at_least_five_negative_signed_gains": int(
            global_metrics["negative_signed_gain_count"]
        )
        >= MIN_NEGATIVE_GAIN_COUNT,
        "cv_signed_skill_at_least_0_10": float(global_metrics["cv_signed_skill"])
        >= MIN_ORIENTATION_CV_SIGNED_SKILL,
    }
    calibration_supported = all(calibration_conditions.values())
    orientation_supported = all(orientation_conditions.values())
    if calibration_supported and orientation_supported:
        raise AssertionError("Mutually exclusive PASS035 wall classifications both passed")
    if calibration_supported:
        decision = "calibration_dominated_failure_on_finite_range"
    elif orientation_supported:
        decision = "orientation_reversal_dominated_failure_on_finite_range"
    else:
        decision = "mixed_or_diffuse_direction_calibration_failure"
    return {
        "thresholds": {
            "minimum_positive_oracle_skill_for_calibration": MIN_CALIBRATION_ORACLE_POSITIVE_SKILL,
            "minimum_cv_positive_skill_for_calibration": MIN_CALIBRATION_CV_POSITIVE_SKILL,
            "minimum_positive_direction_count": MIN_POSITIVE_DIRECTION_COUNT,
            "minimum_nonnegative_modulus_count": MIN_NONNEGATIVE_MODULUS_COUNT,
            "maximum_median_log_reciprocity": MAX_MEDIAN_LOG_RECIPROCITY,
            "minimum_reciprocity_modulus_count": MIN_RECIPROCITY_MODULUS_COUNT,
            "minimum_signed_oracle_skill_for_orientation": MIN_ORIENTATION_SIGNED_ORACLE_SKILL,
            "maximum_positive_oracle_skill_for_orientation": MAX_ORIENTATION_POSITIVE_ORACLE_SKILL,
            "minimum_negative_gain_count": MIN_NEGATIVE_GAIN_COUNT,
            "minimum_cv_signed_skill_for_orientation": MIN_ORIENTATION_CV_SIGNED_SKILL,
        },
        "calibration_conditions": calibration_conditions,
        "orientation_conditions": orientation_conditions,
        "calibration_supported": calibration_supported,
        "orientation_supported": orientation_supported,
        "decision": decision,
    }


def build_result(
    pass028_path: Path,
    pass032_path: Path,
    pass033_path: Path,
    pass034_path: Path,
    progress: bool = False,
) -> dict:
    locked034 = load_locked_json(pass034_path, EXPECTED_PASS034_SHA256, "PASS034")
    (
        p34,
        _p29,
        _reproduced_by_modulus,
        reproduced_global,
        models,
        e14_diagnostics,
        reproduction_error,
    ) = reproduce_pass034(
        pass028_path,
        pass032_path,
        pass033_path,
        locked034,
        progress=progress,
    )
    direction_rows = [analyze_model(model, p34) for model in models]
    direction_rows.sort(key=lambda row: (int(row["r"]), str(row["direction"])))
    by_modulus, global_metrics = combine_direction_rows(direction_rows)
    raw_skill_error = abs(
        float(global_metrics["raw_skill"])
        - float(locked034["global"]["bidirectional_scalar_skill"])
    )
    if raw_skill_error > REPRODUCTION_TOLERANCE:
        raise AssertionError(f"PASS034 raw skill mismatch: {raw_skill_error}")
    decision = classify_wall(global_metrics)
    max_signed_formula_error = max(
        float(row["oracle"]["signed_formula_error"]) for row in direction_rows
    )
    max_positive_formula_error = max(
        float(row["oracle"]["positive_formula_error"]) for row in direction_rows
    )
    return {
        "pass": "PASS035",
        "title": "Direction-versus-gain calibration decomposition after PASS034",
        "classification": "finite target-oracle and leave-one-target-window calibration diagnostic",
        "interpretation_guard": (
            "Oracle gains use the full target and cross-calibrated gains use two target "
            "windows. Neither is a source-only held-out prediction."
        ),
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "input_sha256": {
                pass028_path.name: sha256_file(pass028_path),
                pass032_path.name: sha256_file(pass032_path),
                pass033_path.name: sha256_file(pass033_path),
                pass034_path.name: sha256_file(pass034_path),
            },
            "formula_tolerance": FORMULA_TOLERANCE,
            "reproduction_tolerance": REPRODUCTION_TOLERANCE,
        },
        "global": global_metrics,
        "by_modulus": by_modulus,
        "decision": decision,
        "secondary": {
            "calibration_gap_positive_oracle_minus_raw": float(
                global_metrics["positive_oracle_skill"] - global_metrics["raw_skill"]
            ),
            "orientation_reversal_gap_signed_minus_positive_oracle": float(
                global_metrics["signed_oracle_skill"]
                - global_metrics["positive_oracle_skill"]
            ),
            "reproduced_pass034_global": reproduced_global,
        },
        "safety": {
            "pass034_reproduction_error": reproduction_error,
            "raw_skill_reproduction_error": raw_skill_error,
            "maximum_signed_oracle_formula_error": max_signed_formula_error,
            "maximum_positive_oracle_formula_error": max_positive_formula_error,
            "direction_count": len(direction_rows),
            "modulus_count": len(by_modulus),
            "e14_gate_passed": bool(e14_diagnostics["passed"]),
            "all_target_calibration_folds_have_disjoint_train_test_rows": True,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pass028", type=Path, default=default_pass028_path())
    parser.add_argument("--pass032", type=Path, default=default_pass032_path())
    parser.add_argument("--pass033", type=Path, default=default_pass033_path())
    parser.add_argument("--pass034", type=Path, default=default_pass034_path())
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument("--progress", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(
        args.pass028,
        args.pass032,
        args.pass033,
        args.pass034,
        progress=args.progress,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"PASS035 result: {args.output}")
    print(
        "raw=",
        f'{result["global"]["raw_skill"]:.6f}',
        "oracle+=",
        f'{result["global"]["positive_oracle_skill"]:.6f}',
        "cv+=",
        f'{result["global"]["cv_positive_skill"]:.6f}',
        "oracle±=",
        f'{result["global"]["signed_oracle_skill"]:.6f}',
        "cv±=",
        f'{result["global"]["cv_signed_skill"]:.6f}',
    )
    print("decision:", result["decision"]["decision"])


if __name__ == "__main__":
    main()
