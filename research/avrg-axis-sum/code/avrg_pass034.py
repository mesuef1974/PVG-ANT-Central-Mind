#!/usr/bin/env python3
"""PASS034: independent early/late cancellation-functional stability test.

A new exact e=14 orbit window is computed with the PASS028 residue-fiber
algorithm.  The six windows are split into disjoint early (14,15,16) and late
(17,18,19) blocks.  Each block learns a no-intercept amplitude-to-cancellation
functional, which is mapped back to the common orbit space.  Signed functional
cosine and bidirectional cross-block scalar skill are compared with a locked
within-character six-window permutation null.

Finite computational diagnostic only; no asymptotic or Goldbach proof claim.
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
ALL_EXPS = (14, 15, 16, 17, 18, 19)
EARLY_EXPS = (14, 15, 16)
LATE_EXPS = (17, 18, 19)
PRIMARY_MODULI = (11, 13, 17, 19, 23, 29, 31)
TRAIN_EXPLAINED_THRESHOLD = 0.90
PERMUTATION_ITERATIONS = 5000
PERMUTATION_SEED = 340719
MIN_GLOBAL_SIGNED_COSINE = 0.50
MAX_COSINE_PERMUTATION_P = 0.01
MIN_MODULUS_SIGNED_COSINE = 0.30
MIN_GLOBAL_CROSS_SKILL = 0.10
MAX_SKILL_PERMUTATION_P = 0.01
REQUIRED_MODULUS_COUNT = 5
E14_CLOSURE_TOLERANCE = 1e-10
E14_ZERO_RANGE_TOLERANCE = 1e-12


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


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    results = here.parent / "results"
    if results.is_dir():
        return results / "avrg_pass034_results.json"
    return here / "avrg_pass034_results.json"


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


def scan_e14(p28, progress: bool = False) -> tuple[list[dict], dict]:
    """Compute the exact e=14 on-state orbit decomposition using PASS028 code."""
    exp = 14
    lo, hi = 1 << exp, 1 << (exp + 1)
    theta = p28.sieve_theta(hi)
    main = p28.singular_main(hi)
    fft_length = 1 << (2 * len(theta) - 2).bit_length()
    theta_fft = np.fft.rfft(theta, fft_length)
    rows: list[dict] = []
    candidate_counts = []
    maximum_pointwise_closure_error = 0.0
    maximum_averaged_closure_error = 0.0
    maximum_zero_range = 0.0

    for r in PRIMARY_MODULI:
        step = 2 * r
        first = ((lo + step - 1) // step) * step
        on_values = np.arange(first, hi, step, dtype=np.int64)
        if on_values.size == 0:
            raise ValueError(f"No e=14 on values for r={r}")
        if progress:
            print(f"PASS034 e14 r={r} on={len(on_values)}", flush=True)
        f_matrix = p28.residue_fiber_matrix(
            theta, theta_fft, fft_length, r, on_values, progress=progress
        )
        normalization = main[on_values] ** 2 * (r - 1)
        if np.any(normalization <= 0):
            raise ValueError(f"Nonpositive e=14 normalization for r={r}")
        zero_values = []
        for k in p28.representative_modes(r):
            parts = p28.decompose_f_matrix(
                f_matrix, p28.character_on_residues(r, k), normalization
            )
            maximum_pointwise_closure_error = max(
                maximum_pointwise_closure_error,
                float(parts["maximum_pointwise_closure_error"]),
            )
            total = float(np.mean(parts["total_values"]))
            zero = float(np.mean(parts["zero_values"]))
            orbits = [
                {"b": int(b), "energy": float(np.mean(values))}
                for b, values in sorted(parts["orbit_values"].items())
            ]
            reconstructed = zero + sum(item["energy"] for item in orbits)
            averaged_error = float(reconstructed - total)
            maximum_averaged_closure_error = max(
                maximum_averaged_closure_error, abs(averaged_error)
            )
            if not math.isfinite(total) or total <= 0:
                raise ValueError(f"Invalid e=14 energy at {(r, k)}")
            zero_values.append(zero)
            rows.append(
                {
                    "exp": exp,
                    "r": int(r),
                    "k": int(k),
                    "on_value_count": int(on_values.size),
                    "decomposed_on_energy": total,
                    "zero_residue_energy": zero,
                    "orbits": orbits,
                    "averaged_closure_error": averaged_error,
                }
            )
        maximum_zero_range = max(maximum_zero_range, max(zero_values) - min(zero_values))
        candidate_counts.append({"r": int(r), "count": int(on_values.size)})

    expected_count = sum(len(p28.representative_modes(r)) for r in PRIMARY_MODULI)
    if len(rows) != expected_count or expected_count != 32:
        raise AssertionError(f"Expected 32 e=14 rows, received {len(rows)}")
    keys = {(row["exp"], row["r"], row["k"]) for row in rows}
    if len(keys) != len(rows):
        raise AssertionError("Duplicate e=14 rows")
    passed = (
        maximum_pointwise_closure_error <= E14_CLOSURE_TOLERANCE
        and maximum_averaged_closure_error <= E14_CLOSURE_TOLERANCE
        and maximum_zero_range <= E14_ZERO_RANGE_TOLERANCE
    )
    diagnostics = {
        "exp": exp,
        "row_count": len(rows),
        "fft_length": int(fft_length),
        "candidate_counts": candidate_counts,
        "maximum_pointwise_closure_error": maximum_pointwise_closure_error,
        "maximum_averaged_closure_error": maximum_averaged_closure_error,
        "maximum_zero_residue_range_across_characters": maximum_zero_range,
        "thresholds": {
            "maximum_closure_error": E14_CLOSURE_TOLERANCE,
            "maximum_zero_residue_range": E14_ZERO_RANGE_TOLERANCE,
        },
        "passed": bool(passed),
    }
    if not passed:
        raise AssertionError(f"e=14 scan safety gate failed: {diagnostics}")
    return rows, diagnostics


def combine_vectors(pass028_path: Path, e14_rows: Sequence[Mapping], p29) -> dict:
    vectors = p29.load_vectors(pass028_path)
    for row in e14_rows:
        exp, r, k = int(row["exp"]), int(row["r"]), int(row["k"])
        expected_b = list(range(1, (r - 1) // 2 + 1))
        observed_b = [int(item["b"]) for item in row["orbits"]]
        if observed_b != expected_b:
            raise ValueError(f"e=14 orbit mismatch at {(r, k)}")
        vector = np.asarray([float(item["energy"]) for item in row["orbits"]])
        vectors[(exp, r, k)] = vector
    for exp in ALL_EXPS:
        for r in PRIMARY_MODULI:
            for k in p29.representative_modes(r):
                if (exp, r, k) not in vectors:
                    raise ValueError(f"Missing vector at {(exp, r, k)}")
    return vectors


def centered_vectors(vectors: Mapping, p29) -> dict:
    centered = {}
    for exp in ALL_EXPS:
        for r in PRIMARY_MODULI:
            modes = p29.representative_modes(r)
            matrix = np.vstack([vectors[(exp, r, k)] for k in modes])
            local = matrix - np.mean(matrix, axis=0, keepdims=True)
            if np.max(np.abs(np.sum(local, axis=0))) > 1e-13:
                raise AssertionError(f"Within-window centering failed at {(exp, r)}")
            for index, k in enumerate(modes):
                centered[(exp, r, k)] = local[index]
    return centered


def fit_block_model(
    centered: Mapping,
    r: int,
    block: Sequence[int],
    target_block: Sequence[int],
    p29,
    p32,
) -> dict:
    block = tuple(int(exp) for exp in block)
    target_block = tuple(int(exp) for exp in target_block)
    if set(block) & set(target_block):
        raise ValueError("Training and target blocks overlap")
    modes = p29.representative_modes(r)
    means = {
        k: np.mean(np.vstack([centered[(exp, r, k)] for exp in block]), axis=0)
        for k in modes
    }
    train_rows = [
        centered[(exp, r, k)] - means[k] for exp in block for k in modes
    ]
    target_rows = [
        centered[(exp, r, k)] - means[k] for exp in target_block for k in modes
    ]
    x_train = np.vstack(train_rows)
    x_target = np.vstack(target_rows)
    q = x_train.shape[1]
    sum_direction = np.ones(q, dtype=float) / math.sqrt(q)
    c_train = x_train @ sum_direction
    c_target = x_target @ sum_direction
    amplitude_train = x_train - c_train[:, None] * sum_direction
    _, singular_values, vt = np.linalg.svd(amplitude_train, full_matrices=False)
    rank_d, explained = p29.select_rank(
        singular_values, threshold=TRAIN_EXPLAINED_THRESHOLD
    )
    basis = vt[:rank_d].T
    orthogonality_error = float(
        np.max(np.abs(basis.T @ basis - np.eye(rank_d)))
    )
    perpendicular_error = float(np.max(np.abs(basis.T @ sum_direction)))
    if orthogonality_error > 1e-12 or perpendicular_error > 1e-12:
        raise AssertionError(f"Amplitude basis safety failure for {(r, block)}")
    z_train = x_train @ basis
    z_target = x_target @ basis
    beta, c_fitted, design_rank, condition_number = p32.least_squares_coupling(
        z_train, c_train, z_train
    )
    if design_rank != rank_d:
        raise AssertionError(f"Rank-deficient coupling design for {(r, block)}")
    functional = basis @ beta
    functional_norm = float(np.linalg.norm(functional))
    if functional_norm <= 1e-15:
        raise ValueError(f"Degenerate observed functional for {(r, block)}")
    return {
        "r": int(r),
        "block": list(block),
        "target_block": list(target_block),
        "modes": [int(k) for k in modes],
        "orbit_count": int(q),
        "training_row_count": int(x_train.shape[0]),
        "target_row_count": int(x_target.shape[0]),
        "selected_rank": int(rank_d),
        "training_explained_fraction": float(explained),
        "design_rank": int(design_rank),
        "design_condition_number": float(condition_number),
        "functional_norm": functional_norm,
        "basis_orthogonality_error": orthogonality_error,
        "basis_sum_perpendicular_error": perpendicular_error,
        "functional_sum_perpendicular_error": float(abs(functional @ sum_direction)),
        "training_scalar_skill": scalar_skill(c_train, c_fitted),
        "_basis": basis,
        "_beta": beta,
        "_functional": functional,
        "_unit": functional / functional_norm,
        "_z_train": z_train,
        "_z_target": z_target,
        "_c_train": c_train,
        "_c_target": c_target,
        "_sum_direction": sum_direction,
        "_character_means": means,
    }


def scalar_skill(actual: np.ndarray, predicted: np.ndarray) -> float:
    actual = np.asarray(actual, dtype=float)
    predicted = np.asarray(predicted, dtype=float)
    if actual.shape != predicted.shape:
        raise ValueError("Scalar prediction shape mismatch")
    ss = float(np.sum(actual * actual))
    if ss <= 0:
        raise ValueError("Degenerate scalar target")
    sse = float(np.sum((actual - predicted) ** 2))
    return 1.0 - sse / ss


def cross_metrics(model: Mapping) -> dict:
    q = int(model["orbit_count"])
    actual = math.sqrt(q) * np.asarray(model["_c_target"], dtype=float)
    predicted = math.sqrt(q) * (
        np.asarray(model["_z_target"], dtype=float)
        @ np.asarray(model["_beta"], dtype=float)
    )
    ss = float(np.sum(actual * actual))
    sse = float(np.sum((actual - predicted) ** 2))
    nonzero = actual != 0
    sign_accuracy = float(
        np.mean(np.sign(actual[nonzero]) == np.sign(predicted[nonzero]))
    )
    correlation = (
        float(np.corrcoef(actual, predicted)[0, 1])
        if actual.size >= 2 and np.std(actual) > 0 and np.std(predicted) > 0
        else float("nan")
    )
    return {
        "row_count": int(actual.size),
        "scalar_ss": ss,
        "scalar_sse": sse,
        "scalar_skill": 1.0 - sse / ss,
        "sign_accuracy": sign_accuracy,
        "pearson_correlation": correlation,
        "actual_rms": float(np.sqrt(np.mean(actual * actual))),
        "predicted_rms": float(np.sqrt(np.mean(predicted * predicted))),
        "_actual": actual,
        "_predicted": predicted,
    }


def public_mapping(mapping: Mapping) -> dict:
    return {key: value for key, value in mapping.items() if not key.startswith("_")}


def observed_analysis(centered: Mapping, p29, p32) -> tuple[list[dict], dict, list[dict]]:
    by_modulus = []
    models = []
    actual_all = []
    predicted_all = []
    total_ss = 0.0
    total_sse = 0.0
    for r in PRIMARY_MODULI:
        early = fit_block_model(centered, r, EARLY_EXPS, LATE_EXPS, p29, p32)
        late = fit_block_model(centered, r, LATE_EXPS, EARLY_EXPS, p29, p32)
        models.extend([early, late])
        signed_cosine = float(early["_unit"] @ late["_unit"])
        early_to_late = cross_metrics(early)
        late_to_early = cross_metrics(late)
        local_ss = early_to_late["scalar_ss"] + late_to_early["scalar_ss"]
        local_sse = early_to_late["scalar_sse"] + late_to_early["scalar_sse"]
        local_skill = 1.0 - local_sse / local_ss
        total_ss += local_ss
        total_sse += local_sse
        actual_all.extend([early_to_late["_actual"], late_to_early["_actual"]])
        predicted_all.extend(
            [early_to_late["_predicted"], late_to_early["_predicted"]]
        )
        by_modulus.append(
            {
                "r": int(r),
                "signed_functional_cosine": signed_cosine,
                "absolute_functional_cosine": abs(signed_cosine),
                "early_model": public_mapping(early),
                "late_model": public_mapping(late),
                "early_to_late": public_mapping(early_to_late),
                "late_to_early": public_mapping(late_to_early),
                "bidirectional_scalar_ss": local_ss,
                "bidirectional_scalar_sse": local_sse,
                "bidirectional_scalar_skill": local_skill,
            }
        )
    actual_vector = np.concatenate(actual_all)
    predicted_vector = np.concatenate(predicted_all)
    global_metrics = {
        "modulus_count": len(by_modulus),
        "mean_signed_functional_cosine": statistics.fmean(
            row["signed_functional_cosine"] for row in by_modulus
        ),
        "median_signed_functional_cosine": statistics.median(
            row["signed_functional_cosine"] for row in by_modulus
        ),
        "minimum_signed_functional_cosine": min(
            row["signed_functional_cosine"] for row in by_modulus
        ),
        "maximum_signed_functional_cosine": max(
            row["signed_functional_cosine"] for row in by_modulus
        ),
        "mean_absolute_functional_cosine": statistics.fmean(
            row["absolute_functional_cosine"] for row in by_modulus
        ),
        "bidirectional_scalar_ss": total_ss,
        "bidirectional_scalar_sse": total_sse,
        "bidirectional_scalar_skill": 1.0 - total_sse / total_ss,
        "bidirectional_sign_accuracy": float(
            np.mean(
                np.sign(actual_vector[actual_vector != 0])
                == np.sign(predicted_vector[actual_vector != 0])
            )
        ),
        "bidirectional_pearson_correlation": (
            float(np.corrcoef(actual_vector, predicted_vector)[0, 1])
            if np.std(actual_vector) > 0 and np.std(predicted_vector) > 0
            else float("nan")
        ),
        "row_count": int(actual_vector.size),
    }
    return by_modulus, global_metrics, models


def raw_cancellation_coefficients(centered: Mapping, p29) -> dict:
    output = {}
    for r in PRIMARY_MODULI:
        q = (r - 1) // 2
        direction = np.ones(q, dtype=float) / math.sqrt(q)
        for k in p29.representative_modes(r):
            output[(r, k)] = np.asarray(
                [centered[(exp, r, k)] @ direction for exp in ALL_EXPS],
                dtype=float,
            )
    return output


def coefficient_arrays_for_model(
    raw: Mapping,
    model: Mapping,
) -> tuple[np.ndarray, np.ndarray]:
    r = int(model["r"])
    modes = [int(k) for k in model["modes"]]
    block = [int(exp) for exp in model["block"]]
    target = [int(exp) for exp in model["target_block"]]
    exp_index = {exp: index for index, exp in enumerate(ALL_EXPS)}
    means = {
        k: float(np.mean([raw[(r, k)][exp_index[exp]] for exp in block]))
        for k in modes
    }
    train = np.asarray(
        [
            raw[(r, k)][exp_index[exp]] - means[k]
            for exp in block
            for k in modes
        ],
        dtype=float,
    )
    test = np.asarray(
        [
            raw[(r, k)][exp_index[exp]] - means[k]
            for exp in target
            for k in modes
        ],
        dtype=float,
    )
    return train, test


def null_iteration_metrics(raw: Mapping, models: Sequence[Mapping], p32) -> tuple[float, float, int]:
    by_r = {}
    total_ss = 0.0
    total_sse = 0.0
    degenerate_count = 0
    for model in models:
        c_train, c_target = coefficient_arrays_for_model(raw, model)
        beta, prediction, design_rank, _ = p32.least_squares_coupling(
            np.asarray(model["_z_train"]),
            c_train,
            np.asarray(model["_z_target"]),
        )
        if design_rank != int(model["selected_rank"]):
            raise AssertionError("Permutation changed fixed design rank")
        functional = np.asarray(model["_basis"]) @ beta
        norm = float(np.linalg.norm(functional))
        if norm <= 1e-15:
            unit = None
            degenerate_count += 1
        else:
            unit = functional / norm
        q = int(model["orbit_count"])
        actual = math.sqrt(q) * c_target
        predicted = math.sqrt(q) * prediction
        total_ss += float(np.sum(actual * actual))
        total_sse += float(np.sum((actual - predicted) ** 2))
        by_r.setdefault(int(model["r"]), []).append(unit)
    cosines = []
    for r in PRIMARY_MODULI:
        units = by_r[int(r)]
        if len(units) != 2:
            raise AssertionError(f"Expected two models for r={r}")
        cosine = 0.0 if any(unit is None for unit in units) else float(units[0] @ units[1])
        cosines.append(cosine)
    return statistics.fmean(cosines), 1.0 - total_sse / total_ss, degenerate_count


def describe_null(samples: np.ndarray, observed: float) -> dict:
    samples = np.asarray(samples, dtype=float)
    exceedances = int(np.count_nonzero(samples >= observed))
    return {
        "observed": float(observed),
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
        "one_sided_p_value": float((exceedances + 1) / (samples.size + 1)),
    }


def restricted_permutation_null(
    raw: Mapping,
    models: Sequence[Mapping],
    observed_global: Mapping,
    p32,
    iterations: int = PERMUTATION_ITERATIONS,
    seed: int = PERMUTATION_SEED,
) -> dict:
    rng = np.random.default_rng(seed)
    cosine_samples = np.empty(iterations, dtype=float)
    skill_samples = np.empty(iterations, dtype=float)
    total_degenerate = 0
    keys = sorted(raw)
    for iteration in range(iterations):
        permuted = {
            key: np.asarray(raw[key])[rng.permutation(len(ALL_EXPS))]
            for key in keys
        }
        cosine, skill, degenerates = null_iteration_metrics(permuted, models, p32)
        cosine_samples[iteration] = cosine
        skill_samples[iteration] = skill
        total_degenerate += degenerates
    return {
        "iterations": int(iterations),
        "seed": int(seed),
        "restriction": "permute six windows independently within each (r,k); amplitude designs fixed",
        "signed_functional_cosine_primary": describe_null(
            cosine_samples, observed_global["mean_signed_functional_cosine"]
        ),
        "bidirectional_scalar_skill_primary": describe_null(
            skill_samples, observed_global["bidirectional_scalar_skill"]
        ),
        "total_degenerate_functionals_assigned_zero_cosine": int(total_degenerate),
    }


def decision_summary(
    by_modulus: Sequence[Mapping],
    global_metrics: Mapping,
    permutation: Mapping,
) -> dict:
    cosine_moduli = sum(
        row["signed_functional_cosine"] >= MIN_MODULUS_SIGNED_COSINE
        for row in by_modulus
    )
    nonnegative_skill_moduli = sum(
        row["bidirectional_scalar_skill"] >= 0 for row in by_modulus
    )
    conditions = {
        "global_signed_cosine_at_least_0_50": global_metrics[
            "mean_signed_functional_cosine"
        ]
        >= MIN_GLOBAL_SIGNED_COSINE,
        "cosine_permutation_p_at_most_0_01": permutation[
            "signed_functional_cosine_primary"
        ]["one_sided_p_value"]
        <= MAX_COSINE_PERMUTATION_P,
        "at_least_five_moduli_signed_cosine_at_least_0_30": cosine_moduli
        >= REQUIRED_MODULUS_COUNT,
        "global_bidirectional_scalar_skill_at_least_0_10": global_metrics[
            "bidirectional_scalar_skill"
        ]
        >= MIN_GLOBAL_CROSS_SKILL,
        "skill_permutation_p_at_most_0_01": permutation[
            "bidirectional_scalar_skill_primary"
        ]["one_sided_p_value"]
        <= MAX_SKILL_PERMUTATION_P,
        "at_least_five_moduli_nonnegative_bidirectional_skill": nonnegative_skill_moduli
        >= REQUIRED_MODULUS_COUNT,
    }
    supported = all(conditions.values())
    return {
        "thresholds": {
            "minimum_global_signed_cosine": MIN_GLOBAL_SIGNED_COSINE,
            "maximum_cosine_permutation_p": MAX_COSINE_PERMUTATION_P,
            "minimum_modulus_signed_cosine": MIN_MODULUS_SIGNED_COSINE,
            "minimum_global_bidirectional_scalar_skill": MIN_GLOBAL_CROSS_SKILL,
            "maximum_skill_permutation_p": MAX_SKILL_PERMUTATION_P,
            "required_modulus_count": REQUIRED_MODULUS_COUNT,
        },
        "qualifying_cosine_modulus_count": int(cosine_moduli),
        "nonnegative_skill_modulus_count": int(nonnegative_skill_moduli),
        "conditions": conditions,
        "supported": bool(supported),
        "decision": (
            "stable_nonoverlapping_linear_cancellation_functional_on_finite_range"
            if supported
            else "no_stable_nonoverlapping_linear_cancellation_functional_under_locked_rule"
        ),
    }


def correlation(xs: Sequence[float], ys: Sequence[float]) -> float:
    x = np.asarray(xs, dtype=float)
    y = np.asarray(ys, dtype=float)
    if x.size != y.size or x.size < 2 or np.std(x) == 0 or np.std(y) == 0:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def build_result(
    pass028_path: Path,
    pass032_path: Path,
    pass033_path: Path,
    permutation_iterations: int = PERMUTATION_ITERATIONS,
    progress: bool = False,
) -> dict:
    locked032 = load_locked_json(pass032_path, EXPECTED_PASS032_SHA256, "PASS032")
    locked033 = load_locked_json(pass033_path, EXPECTED_PASS033_SHA256, "PASS033")
    if sha256_file(pass028_path) != EXPECTED_PASS028_SHA256:
        raise ValueError("PASS028 hash mismatch")
    p28 = load_module("avrg_pass028")
    p29 = load_module("avrg_pass029")
    p32 = load_module("avrg_pass032")
    e14_rows, e14_diagnostics = scan_e14(p28, progress=progress)
    vectors = combine_vectors(pass028_path, e14_rows, p29)
    centered = centered_vectors(vectors, p29)
    by_modulus, global_metrics, models = observed_analysis(centered, p29, p32)
    raw = raw_cancellation_coefficients(centered, p29)
    permutation = restricted_permutation_null(
        raw,
        models,
        global_metrics,
        p32,
        iterations=permutation_iterations,
        seed=PERMUTATION_SEED,
    )
    decision = decision_summary(by_modulus, global_metrics, permutation)
    pass032_skill_by_modulus = {
        int(row["r"]): float(row["predicted"]["scalar_skill"])
        for row in locked032["decision"]["by_modulus"]
    }
    return {
        "pass": "PASS034",
        "title": "Non-overlapping early/late cancellation-functional stability",
        "classification": "finite independent-block linear-functional and cross-prediction diagnostic",
        "interpretation_guard": (
            "The early and late training blocks share no windows, but there are only two "
            "adjacent three-window blocks. Stability here is finite and scale-local."
        ),
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "all_exps": list(ALL_EXPS),
            "early_exps": list(EARLY_EXPS),
            "late_exps": list(LATE_EXPS),
            "moduli": list(PRIMARY_MODULI),
            "training_explained_threshold": TRAIN_EXPLAINED_THRESHOLD,
            "permutation_iterations": int(permutation_iterations),
            "permutation_seed": PERMUTATION_SEED,
            "input_sha256": {
                pass028_path.name: sha256_file(pass028_path),
                pass032_path.name: sha256_file(pass032_path),
                pass033_path.name: sha256_file(pass033_path),
            },
        },
        "e14_full_scan": {
            "diagnostics": e14_diagnostics,
            "exact_rows": e14_rows,
        },
        "global": global_metrics,
        "by_modulus": by_modulus,
        "restricted_permutation_null": permutation,
        "decision": decision,
        "secondary": {
            "pass033_prior_mean_oriented_coherence": locked033["global_stability"][
                "mean_oriented_coherence"
            ],
            "pass033_prior_oriented_p_value": locked033[
                "restricted_permutation_null"
            ]["oriented_coherence_primary"]["one_sided_p_value"],
            "correlation_modulus_signed_cosine_with_pass032_scalar_skill": correlation(
                [row["signed_functional_cosine"] for row in by_modulus],
                [pass032_skill_by_modulus[int(row["r"])] for row in by_modulus],
            ),
            "pass032_scalar_skill_by_modulus": pass032_skill_by_modulus,
        },
        "safety": {
            "blocks_are_disjoint": not bool(set(EARLY_EXPS) & set(LATE_EXPS)),
            "e14_gate_passed": bool(e14_diagnostics["passed"]),
            "e14_row_count": len(e14_rows),
            "model_count": len(models),
            "maximum_basis_orthogonality_error": max(
                model["basis_orthogonality_error"] for model in models
            ),
            "maximum_basis_sum_perpendicular_error": max(
                model["basis_sum_perpendicular_error"] for model in models
            ),
            "maximum_functional_sum_perpendicular_error": max(
                model["functional_sum_perpendicular_error"] for model in models
            ),
            "minimum_functional_norm": min(model["functional_norm"] for model in models),
            "all_design_ranks_full": all(
                model["design_rank"] == model["selected_rank"] for model in models
            ),
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pass028", type=Path, default=default_pass028_path())
    parser.add_argument("--pass032", type=Path, default=default_pass032_path())
    parser.add_argument("--pass033", type=Path, default=default_pass033_path())
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument(
        "--permutation-iterations", type=int, default=PERMUTATION_ITERATIONS
    )
    parser.add_argument("--progress", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(
        args.pass028,
        args.pass032,
        args.pass033,
        permutation_iterations=args.permutation_iterations,
        progress=args.progress,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"PASS034 result: {args.output}")
    print(
        "cosine=",
        f'{result["global"]["mean_signed_functional_cosine"]:.6f}',
        "cosine p=",
        f'{result["restricted_permutation_null"]["signed_functional_cosine_primary"]["one_sided_p_value"]:.6f}',
        "cross skill=",
        f'{result["global"]["bidirectional_scalar_skill"]:.6f}',
        "skill p=",
        f'{result["restricted_permutation_null"]["bidirectional_scalar_skill_primary"]["one_sided_p_value"]:.6f}',
    )
    print("decision:", result["decision"]["decision"])


if __name__ == "__main__":
    main()
