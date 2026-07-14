#!/usr/bin/env python3
"""PASS034: disjoint-window-block transport of the cancellation functional.

An exact e=14 residue-orbit window is computed and joined to locked PASS028
e=15..19 vectors.  Separate linear cancellation functionals are learned from
the disjoint early (14,15,16) and late (17,18,19) blocks, then transported in
both directions.  Restricted permutations test scalar skill and signed
functional alignment without overlapping training windows.
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
E14_EXP = 14
ALL_EXPS = (14, 15, 16, 17, 18, 19)
EARLY_EXPS = (14, 15, 16)
LATE_EXPS = (17, 18, 19)
TRAIN_EXPLAINED_THRESHOLD = 0.90
SCAN_TOLERANCE = 1e-10
ZERO_RANGE_TOLERANCE = 1e-12
PERMUTATION_ITERATIONS = 5000
PERMUTATION_SEED = 340719
MIN_GLOBAL_SCALAR_SKILL = 0.10
MAX_SCALAR_PERMUTATION_P = 0.01
MIN_MEAN_SIGNED_COSINE = 0.40
MAX_COSINE_PERMUTATION_P = 0.01
REQUIRED_POSITIVE_MODULI = 5


def load_pass028_module():
    try:
        return importlib.import_module("avrg_pass028")
    except ModuleNotFoundError:
        sibling = Path(__file__).resolve().parents[1] / "pass028"
        sys.path.insert(0, str(sibling))
        return importlib.import_module("avrg_pass028")


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


def default_e14_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results"
    if archive.is_dir():
        return archive / "avrg_pass034_e14_orbits.json"
    return here / "avrg_pass034_e14_orbits.json"


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results"
    if archive.is_dir():
        return archive / "avrg_pass034_results.json"
    return here / "avrg_pass034_results.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def scan_e14(p28) -> dict:
    lo, hi = 1 << E14_EXP, 1 << (E14_EXP + 1)
    theta = p28.sieve_theta(hi)
    main = p28.singular_main(hi)
    fft_length = 1 << (2 * len(theta) - 2).bit_length()
    theta_fft = np.fft.rfft(theta, fft_length)
    rows = []
    candidate_counts = []
    maximum_pointwise_error = 0.0
    maximum_averaged_error = 0.0
    zero_ranges = []
    for r in p28.PRIMARY_MODULI:
        step = 2 * r
        first = ((lo + step - 1) // step) * step
        on_values = np.arange(first, hi, step, dtype=np.int64)
        f_matrix = p28.residue_fiber_matrix(
            theta, theta_fft, fft_length, r, on_values, progress=False
        )
        normalization = main[on_values] ** 2 * (r - 1)
        local_zero = []
        for k in p28.representative_modes(r):
            parts = p28.decompose_f_matrix(
                f_matrix, p28.character_on_residues(r, k), normalization
            )
            total = float(np.mean(parts["total_values"]))
            zero = float(np.mean(parts["zero_values"]))
            orbits = [
                {"b": int(b), "energy": float(np.mean(values))}
                for b, values in sorted(parts["orbit_values"].items())
            ]
            reconstructed = zero + sum(item["energy"] for item in orbits)
            maximum_pointwise_error = max(
                maximum_pointwise_error,
                float(parts["maximum_pointwise_closure_error"]),
            )
            maximum_averaged_error = max(
                maximum_averaged_error, abs(reconstructed - total)
            )
            local_zero.append(zero)
            rows.append(
                {
                    "exp": E14_EXP,
                    "r": int(r),
                    "k": int(k),
                    "on_value_count": int(on_values.size),
                    "decomposed_on_energy": total,
                    "zero_residue_energy": zero,
                    "orbits": orbits,
                    "averaged_closure_error": reconstructed - total,
                }
            )
        zero_ranges.append(max(local_zero) - min(local_zero))
        candidate_counts.append(
            {"exp": E14_EXP, "r": int(r), "count": int(on_values.size)}
        )
    conditions = {
        "exactly_32_character_rows": len(rows) == 32,
        "all_total_energies_positive_and_finite": all(
            math.isfinite(row["decomposed_on_energy"])
            and row["decomposed_on_energy"] > 0
            for row in rows
        ),
        "maximum_pointwise_closure_error_at_most_1e_10": maximum_pointwise_error
        <= SCAN_TOLERANCE,
        "maximum_averaged_closure_error_at_most_1e_10": maximum_averaged_error
        <= SCAN_TOLERANCE,
        "maximum_zero_residue_range_at_most_1e_12": max(zero_ranges)
        <= ZERO_RANGE_TOLERANCE,
    }
    payload = {
        "pass": "PASS034-E14",
        "title": "Exact e=14 nonzero residue-orbit window",
        "classification": "finite complete-window algebraic and computational input",
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "exp": E14_EXP,
            "moduli": list(p28.PRIMARY_MODULI),
            "character_selection": "one representative per conjugate pair of even nonprincipal characters",
            "fft_length": fft_length,
        },
        "gate": {
            "thresholds": {
                "maximum_closure_error": SCAN_TOLERANCE,
                "maximum_zero_residue_range": ZERO_RANGE_TOLERANCE,
            },
            "maximum_pointwise_closure_error": maximum_pointwise_error,
            "maximum_averaged_closure_error": maximum_averaged_error,
            "maximum_zero_residue_range_across_characters": max(zero_ranges),
            "conditions": conditions,
            "passed": all(conditions.values()),
        },
        "candidate_counts": candidate_counts,
        "exact_rows": rows,
    }
    validate_e14_payload(payload, p28)
    return payload


def validate_e14_payload(payload: Mapping, p28) -> None:
    if payload.get("pass") != "PASS034-E14" or not payload.get("gate", {}).get("passed"):
        raise ValueError("PASS034 e=14 gate failed")
    rows = payload.get("exact_rows", [])
    if len(rows) != 32:
        raise ValueError("PASS034 e=14 row count mismatch")
    keys = set()
    for row in rows:
        exp, r, k = int(row["exp"]), int(row["r"]), int(row["k"])
        if exp != E14_EXP or r not in p28.PRIMARY_MODULI:
            raise ValueError("Unexpected e=14 row key")
        expected_b = list(range(1, (r - 1) // 2 + 1))
        if [int(item["b"]) for item in row["orbits"]] != expected_b:
            raise ValueError("e=14 orbit ordering mismatch")
        if (exp, r, k) in keys:
            raise ValueError("Duplicate e=14 row")
        keys.add((exp, r, k))
    for r in p28.PRIMARY_MODULI:
        observed = sorted(k for exp, rr, k in keys if rr == r)
        if observed != p28.representative_modes(r):
            raise ValueError(f"e=14 representative mismatch for r={r}")


def load_six_window_vectors(
    pass028_path: Path, e14_payload: Mapping, p28, p29
) -> dict[tuple[int, int, int], np.ndarray]:
    if sha256_file(pass028_path) != EXPECTED_PASS028_SHA256:
        raise ValueError("PASS028 hash mismatch")
    validate_e14_payload(e14_payload, p28)
    with pass028_path.open("r", encoding="utf-8") as handle:
        old = json.load(handle)
    rows = list(e14_payload["exact_rows"]) + list(old.get("exact_rows", []))
    vectors = {}
    for row in rows:
        exp, r, k = int(row["exp"]), int(row["r"]), int(row["k"])
        if exp not in ALL_EXPS or r not in p29.PRIMARY_MODULI:
            continue
        expected_b = list(range(1, (r - 1) // 2 + 1))
        if [int(item["b"]) for item in row["orbits"]] != expected_b:
            raise ValueError("Six-window orbit mismatch")
        key = (exp, r, k)
        if key in vectors:
            raise ValueError(f"Duplicate six-window row {key}")
        vectors[key] = np.asarray(
            [float(item["energy"]) for item in row["orbits"]], dtype=float
        )
    expected_count = 6 * sum(
        len(p29.representative_modes(r)) for r in p29.PRIMARY_MODULI
    )
    if len(vectors) != expected_count:
        raise ValueError(f"Expected {expected_count} six-window vectors, got {len(vectors)}")
    return vectors


def centered_six_vectors(vectors: Mapping, p29) -> dict:
    centered = {}
    for exp in ALL_EXPS:
        for r in p29.PRIMARY_MODULI:
            modes = p29.representative_modes(r)
            matrix = np.vstack([vectors[(exp, r, k)] for k in modes])
            local = matrix - np.mean(matrix, axis=0, keepdims=True)
            if np.max(np.abs(np.sum(local, axis=0))) > 1e-14:
                raise AssertionError("Six-window centering failed")
            for index, k in enumerate(modes):
                centered[(exp, r, k)] = local[index]
    return centered


def structural_rank_max(r: int, character_count: int) -> int:
    q = (r - 1) // 2
    return min(q - 1, 2 * (character_count - 1))


def block_arrays(
    centered: Mapping,
    r: int,
    source_exps: Sequence[int],
    target_exps: Sequence[int],
    p29,
) -> tuple[np.ndarray, np.ndarray, dict[int, np.ndarray]]:
    if set(source_exps) & set(target_exps):
        raise ValueError("Source and target blocks overlap")
    modes = p29.representative_modes(r)
    means = {
        k: np.mean(np.vstack([centered[(exp, r, k)] for exp in source_exps]), axis=0)
        for k in modes
    }
    train = np.vstack(
        [centered[(exp, r, k)] - means[k] for exp in source_exps for k in modes]
    )
    target = np.vstack(
        [centered[(exp, r, k)] - means[k] for exp in target_exps for k in modes]
    )
    return train, target, means


def select_block_rank(x_train: np.ndarray, rank_max: int) -> tuple[int, float]:
    q = x_train.shape[1]
    direction = np.ones(q, dtype=float) / np.sqrt(q)
    perpendicular = x_train - (x_train @ direction)[:, None] * direction
    singular_values = np.linalg.svd(perpendicular, compute_uv=False)
    energy = singular_values * singular_values
    total = float(np.sum(energy))
    if total <= 0:
        raise ValueError("Degenerate block training spectrum")
    cumulative = np.cumsum(energy) / total
    rank = int(np.searchsorted(cumulative, TRAIN_EXPLAINED_THRESHOLD, side="left") + 1)
    if rank > rank_max:
        residual = float(np.sum(energy[rank_max:]) / total)
        if residual > 1e-12:
            raise AssertionError("Selected rank exceeds block structural maximum")
        rank = rank_max
    return rank, float(cumulative[rank - 1])


def analyze_transport(
    centered: Mapping,
    r: int,
    source_label: str,
    source_exps: Sequence[int],
    target_exps: Sequence[int],
    p32,
    p30,
    p29,
) -> dict:
    x_train, x_target, _ = block_arrays(
        centered, r, source_exps, target_exps, p29
    )
    modes = p29.representative_modes(r)
    rank_max = structural_rank_max(r, len(modes))
    rank, explained = select_block_rank(x_train, rank_max)
    basis, direction = p32.amplitude_basis(x_train, rank, p30)
    z_train = x_train @ basis
    z_target = x_target @ basis
    c_train = x_train @ direction
    c_target = x_target @ direction
    beta, c_prediction, design_rank, condition_number = p32.least_squares_coupling(
        z_train, c_train, z_target
    )
    functional = basis @ beta
    norm = float(np.linalg.norm(functional))
    if norm <= 1e-15:
        raise ValueError("Degenerate disjoint-block functional")
    q = x_target.shape[1]
    amplitude = z_target @ basis.T
    predicted_vector = amplitude + c_prediction[:, None] * direction
    oracle_vector = amplitude + c_target[:, None] * direction
    predicted_scalar = np.sqrt(q) * c_prediction
    actual_scalar = np.sqrt(q) * c_target
    predicted = p32.forecast_metrics(x_target, predicted_vector, predicted_scalar)
    oracle = p32.forecast_metrics(x_target, oracle_vector, actual_scalar)
    return {
        "r": int(r),
        "source_block": source_label,
        "source_exps": [int(exp) for exp in source_exps],
        "target_exps": [int(exp) for exp in target_exps],
        "modes": [int(k) for k in modes],
        "rank": rank,
        "structural_rank_max": rank_max,
        "training_explained_fraction": explained,
        "training_row_count": int(x_train.shape[0]),
        "target_row_count": int(x_target.shape[0]),
        "design_rank": design_rank,
        "design_condition_number": condition_number,
        "functional_norm": norm,
        "sum_perpendicular_error": float(abs(functional @ direction)),
        "predicted_metrics": predicted,
        "oracle_metrics": oracle,
        "vector_skill_loss_vs_oracle": oracle["vector_skill"] - predicted["vector_skill"],
        "actual_scalar": actual_scalar.tolist(),
        "predicted_scalar": predicted_scalar.tolist(),
        "sign_correct_count": int(
            np.count_nonzero(np.sign(actual_scalar) == np.sign(predicted_scalar))
        ),
        "_functional": functional,
        "_unit": functional / norm,
        "_basis": basis,
        "_z_train": z_train,
        "_z_target": z_target,
    }


def aggregate_metrics(folds: Sequence[Mapping], field: str) -> dict:
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


def cosine(first: np.ndarray, second: np.ndarray) -> float:
    denominator = float(np.linalg.norm(first) * np.linalg.norm(second))
    if denominator <= 0:
        raise ValueError("Cosine requires nonzero vectors")
    return float(first @ second / denominator)


def cosine_by_modulus(folds: Sequence[Mapping], moduli: Sequence[int]) -> list[dict]:
    rows = []
    for r in moduli:
        local = {fold["source_block"]: fold for fold in folds if fold["r"] == r}
        if set(local) != {"early", "late"}:
            raise ValueError("Missing block functional")
        signed = cosine(local["early"]["_functional"], local["late"]["_functional"])
        rows.append({"r": int(r), "signed_cosine": signed, "absolute_cosine": abs(signed)})
    return rows


def raw_six_coefficients(centered: Mapping, p29) -> dict:
    output = {}
    for r in p29.PRIMARY_MODULI:
        q = (r - 1) // 2
        direction = np.ones(q, dtype=float) / np.sqrt(q)
        for k in p29.representative_modes(r):
            output[(r, k)] = np.asarray(
                [centered[(exp, r, k)] @ direction for exp in ALL_EXPS], dtype=float
            )
    return output


def permuted_block_targets(
    permuted_raw: Mapping,
    fold: Mapping,
) -> tuple[np.ndarray, np.ndarray]:
    index = {exp: position for position, exp in enumerate(ALL_EXPS)}
    r = int(fold["r"])
    modes = [int(k) for k in fold["modes"]]
    source = [int(exp) for exp in fold["source_exps"]]
    target = [int(exp) for exp in fold["target_exps"]]
    means = {
        k: float(np.mean([permuted_raw[(r, k)][index[exp]] for exp in source]))
        for k in modes
    }
    c_train = np.asarray(
        [
            permuted_raw[(r, k)][index[exp]] - means[k]
            for exp in source
            for k in modes
        ],
        dtype=float,
    )
    c_target = np.asarray(
        [
            permuted_raw[(r, k)][index[exp]] - means[k]
            for exp in target
            for k in modes
        ],
        dtype=float,
    )
    return c_train, c_target


def restricted_permutation_null(
    folds: Sequence[dict],
    raw_coefficients: Mapping,
    moduli: Sequence[int],
    p32,
    iterations: int = PERMUTATION_ITERATIONS,
    seed: int = PERMUTATION_SEED,
) -> dict:
    rng = np.random.default_rng(seed)
    observed_metrics = aggregate_metrics(folds, "predicted_metrics")
    observed_skill = observed_metrics["scalar_skill"]
    observed_cosines = cosine_by_modulus(folds, moduli)
    observed_cosine = statistics.fmean(row["signed_cosine"] for row in observed_cosines)
    skill_samples = np.empty(iterations, dtype=float)
    cosine_samples = np.empty(iterations, dtype=float)
    keys = sorted(raw_coefficients)
    for iteration in range(iterations):
        permuted = {
            key: np.asarray(raw_coefficients[key])[rng.permutation(len(ALL_EXPS))]
            for key in keys
        }
        scalar_ss = 0.0
        scalar_sse = 0.0
        simulated_functionals = {}
        for fold in folds:
            c_train, c_target = permuted_block_targets(permuted, fold)
            beta, c_prediction, _, _ = p32.least_squares_coupling(
                fold["_z_train"], c_train, fold["_z_target"]
            )
            q = int(fold["orbit_count"] if "orbit_count" in fold else fold["_basis"].shape[0])
            scalar_ss += q * float(np.sum(c_target * c_target))
            scalar_sse += q * float(np.sum((c_target - c_prediction) ** 2))
            simulated_functionals[(fold["r"], fold["source_block"])] = (
                fold["_basis"] @ beta
            )
        skill_samples[iteration] = 1.0 - scalar_sse / scalar_ss
        cosine_samples[iteration] = statistics.fmean(
            cosine(
                simulated_functionals[(r, "early")],
                simulated_functionals[(r, "late")],
            )
            for r in moduli
        )

    def describe(samples: np.ndarray, observed: float) -> dict:
        exceedances = int(np.count_nonzero(samples >= observed))
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
        "restriction": "permute six windows independently within each (r,k)",
        "scalar_skill_primary": describe(skill_samples, observed_skill),
        "mean_signed_cosine_primary": describe(cosine_samples, observed_cosine),
    }


def grouped_results(folds: Sequence[dict], p29) -> tuple[list[dict], list[dict]]:
    by_modulus = []
    for r in p29.PRIMARY_MODULI:
        local = [fold for fold in folds if fold["r"] == r]
        by_modulus.append(
            {
                "r": int(r),
                "predicted": aggregate_metrics(local, "predicted_metrics"),
                "oracle": aggregate_metrics(local, "oracle_metrics"),
                "sign_accuracy": sum(fold["sign_correct_count"] for fold in local)
                / sum(fold["target_row_count"] for fold in local),
            }
        )
    by_direction = []
    for label in ("early", "late"):
        local = [fold for fold in folds if fold["source_block"] == label]
        by_direction.append(
            {
                "source_block": label,
                "target_block": "late" if label == "early" else "early",
                "predicted": aggregate_metrics(local, "predicted_metrics"),
                "oracle": aggregate_metrics(local, "oracle_metrics"),
            }
        )
    return by_modulus, by_direction


def decision_summary(
    predicted: Mapping,
    by_modulus: Sequence[Mapping],
    by_direction: Sequence[Mapping],
    cosines: Sequence[Mapping],
    permutation: Mapping,
) -> dict:
    mean_cosine = statistics.fmean(row["signed_cosine"] for row in cosines)
    positive_moduli = sum(row["predicted"]["scalar_skill"] > 0 for row in by_modulus)
    nonnegative_directions = sum(
        row["predicted"]["scalar_skill"] >= 0 for row in by_direction
    )
    conditions = {
        "global_scalar_skill_at_least_0_10": predicted["scalar_skill"]
        >= MIN_GLOBAL_SCALAR_SKILL,
        "scalar_skill_permutation_p_at_most_0_01": permutation[
            "scalar_skill_primary"
        ]["one_sided_p_value"]
        <= MAX_SCALAR_PERMUTATION_P,
        "mean_signed_cosine_at_least_0_40": mean_cosine
        >= MIN_MEAN_SIGNED_COSINE,
        "signed_cosine_permutation_p_at_most_0_01": permutation[
            "mean_signed_cosine_primary"
        ]["one_sided_p_value"]
        <= MAX_COSINE_PERMUTATION_P,
        "at_least_five_moduli_positive_scalar_skill": positive_moduli
        >= REQUIRED_POSITIVE_MODULI,
        "both_transport_directions_nonnegative_scalar_skill": nonnegative_directions
        == 2,
    }
    supported = all(conditions.values())
    return {
        "thresholds": {
            "minimum_global_scalar_skill": MIN_GLOBAL_SCALAR_SKILL,
            "maximum_scalar_skill_permutation_p": MAX_SCALAR_PERMUTATION_P,
            "minimum_mean_signed_cosine": MIN_MEAN_SIGNED_COSINE,
            "maximum_signed_cosine_permutation_p": MAX_COSINE_PERMUTATION_P,
            "required_positive_modulus_count": REQUIRED_POSITIVE_MODULI,
            "required_nonnegative_direction_count": 2,
        },
        "mean_signed_cosine": mean_cosine,
        "mean_absolute_cosine": statistics.fmean(
            row["absolute_cosine"] for row in cosines
        ),
        "positive_modulus_count": positive_moduli,
        "nonnegative_direction_count": nonnegative_directions,
        "conditions": conditions,
        "supported": supported,
        "decision": (
            "finite_disjoint_block_linear_cancellation_transport_supported"
            if supported
            else "no_disjoint_block_linear_cancellation_transport_under_locked_rule"
        ),
    }


def public_fold(fold: Mapping) -> dict:
    return {key: value for key, value in fold.items() if not key.startswith("_")}


def build_result(
    pass028_path: Path,
    e14_payload: Mapping,
    e14_sha256: str,
    permutation_iterations: int = PERMUTATION_ITERATIONS,
) -> dict:
    p28 = load_pass028_module()
    p32 = load_pass032_module()
    p31 = p32.load_pass031_module()
    p30 = p31.load_pass030_module()
    p29 = p30.load_pass029_module()
    vectors = load_six_window_vectors(pass028_path, e14_payload, p28, p29)
    centered = centered_six_vectors(vectors, p29)
    folds = []
    for r in p29.PRIMARY_MODULI:
        folds.append(
            analyze_transport(
                centered, r, "early", EARLY_EXPS, LATE_EXPS, p32, p30, p29
            )
        )
        folds.append(
            analyze_transport(
                centered, r, "late", LATE_EXPS, EARLY_EXPS, p32, p30, p29
            )
        )
    predicted = aggregate_metrics(folds, "predicted_metrics")
    oracle = aggregate_metrics(folds, "oracle_metrics")
    by_modulus, by_direction = grouped_results(folds, p29)
    cosines = cosine_by_modulus(folds, p29.PRIMARY_MODULI)
    raw_coefficients = raw_six_coefficients(centered, p29)
    permutation = restricted_permutation_null(
        folds,
        raw_coefficients,
        p29.PRIMARY_MODULI,
        p32,
        iterations=permutation_iterations,
        seed=PERMUTATION_SEED,
    )
    decision = decision_summary(
        predicted, by_modulus, by_direction, cosines, permutation
    )
    return {
        "pass": "PASS034",
        "title": "Disjoint early/late block transport of the linear cancellation functional",
        "classification": "finite disjoint-training-block conditional transport diagnostic",
        "interpretation_guard": (
            "Target amplitude coordinates still use observed target orbit vectors. "
            "The test removes training-window overlap but remains conditional."
        ),
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "exps": list(ALL_EXPS),
            "early_block": list(EARLY_EXPS),
            "late_block": list(LATE_EXPS),
            "moduli": list(p29.PRIMARY_MODULI),
            "training_explained_threshold": TRAIN_EXPLAINED_THRESHOLD,
            "permutation_iterations": permutation_iterations,
            "permutation_seed": PERMUTATION_SEED,
            "input_sha256": {
                pass028_path.name: sha256_file(pass028_path),
                "avrg_pass034_e14_orbits.json": e14_sha256,
            },
        },
        "e14_gate": e14_payload["gate"],
        "predicted_global": predicted,
        "oracle_global": oracle,
        "by_modulus": by_modulus,
        "by_direction": by_direction,
        "functional_cosine_by_modulus": cosines,
        "restricted_permutation_null": permutation,
        "decision": decision,
        "safety": {
            "fold_count": len(folds),
            "blocks_are_disjoint": set(EARLY_EXPS).isdisjoint(LATE_EXPS),
            "all_design_ranks_full": all(
                fold["design_rank"] == fold["rank"] for fold in folds
            ),
            "maximum_sum_perpendicular_error": max(
                fold["sum_perpendicular_error"] for fold in folds
            ),
            "maximum_design_condition_number": max(
                fold["design_condition_number"] for fold in folds
            ),
            "minimum_training_explained_fraction": min(
                fold["training_explained_fraction"] for fold in folds
            ),
        },
        "folds": [public_fold(fold) for fold in folds],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pass028", type=Path, default=default_pass028_path())
    parser.add_argument("--e14-output", type=Path, default=default_e14_output_path())
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument(
        "--permutation-iterations", type=int, default=PERMUTATION_ITERATIONS
    )
    return parser.parse_args()


def write_json(path: Path, payload: Mapping) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
        handle.write("\n")


def main() -> None:
    args = parse_args()
    if sha256_file(args.pass028) != EXPECTED_PASS028_SHA256:
        raise ValueError("PASS028 hash mismatch")
    p28 = load_pass028_module()
    e14_payload = scan_e14(p28)
    write_json(args.e14_output, e14_payload)
    e14_sha = sha256_file(args.e14_output)
    result = build_result(
        args.pass028,
        e14_payload,
        e14_sha,
        permutation_iterations=args.permutation_iterations,
    )
    write_json(args.output, result)
    print(f"PASS034 e=14 input: {args.e14_output}")
    print(f"PASS034 result: {args.output}")
    print(
        "scalar skill=",
        f'{result["predicted_global"]["scalar_skill"]:.6f}',
        "mean cosine=",
        f'{result["decision"]["mean_signed_cosine"]:.6f}',
        "skill p=",
        f'{result["restricted_permutation_null"]["scalar_skill_primary"]["one_sided_p_value"]:.6f}',
    )
    print("decision:", result["decision"]["decision"])


if __name__ == "__main__":
    main()
