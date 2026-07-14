#!/usr/bin/env python3
"""PASS029: held-out-window stability of the nonzero-orbit subspace.

For each modulus and held-out window, an SVD basis is learned only from the
other four windows after within-window centering and training-only character
mean removal.  The held-out orbit vectors are projected onto that basis and
compared with equal-rank random subspaces.

The projection is a subspace-containment diagnostic, not a forecast whose
coordinates are known without observing the held-out vector.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
from pathlib import Path
from typing import Mapping, Sequence

import numpy as np


EXPS = (15, 16, 17, 18, 19)
PRIMARY_MODULI = (11, 13, 17, 19, 23, 29, 31)
EXPECTED_PASS028_SHA256 = (
    "9088e373aa18fdef6cdc8a7a0b6b1fb8680f5dd08653a12699a787118f6f4eab"
)
TRAIN_EXPLAINED_THRESHOLD = 0.90
RANDOM_ITERATIONS = 5000
RANDOM_SEED = 290719
MAX_WEIGHTED_RANK_FRACTION = 0.50
MIN_VECTOR_SKILL = 0.60
MIN_SCALAR_SKILL = 0.30
MAX_RANDOM_P_VALUE = 0.01
MIN_MODULUS_VECTOR_SKILL = 0.50
REQUIRED_MODULUS_COUNT = 5


def default_pass028_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass028_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass028" / "avrg_pass028_results.json"


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_results = here.parent / "results"
    if archive_results.is_dir():
        return archive_results / "avrg_pass029_results.json"
    return here / "avrg_pass029_results.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def representative_modes(r: int) -> list[int]:
    return [k for k in range(2, r - 1, 2) if k <= r - 1 - k]


def load_vectors(path: Path) -> dict[tuple[int, int, int], np.ndarray]:
    observed_sha = sha256_file(path)
    if observed_sha != EXPECTED_PASS028_SHA256:
        raise ValueError(
            f"PASS028 hash mismatch: {observed_sha} != {EXPECTED_PASS028_SHA256}"
        )
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if data.get("pass") != "PASS028" or not data.get("full_scan_gate", {}).get("passed"):
        raise ValueError("PASS028 full scan is absent or did not pass")
    config = data.get("configuration", {})
    if tuple(config.get("exps", [])) != EXPS:
        raise ValueError("PASS028 windows differ from the lock")
    if tuple(config.get("moduli", [])) != PRIMARY_MODULI:
        raise ValueError("PASS028 moduli differ from the lock")
    rows = data.get("exact_rows", [])
    if len(rows) != 160:
        raise ValueError(f"Expected 160 rows, received {len(rows)}")
    vectors: dict[tuple[int, int, int], np.ndarray] = {}
    for row in rows:
        exp, r, k = int(row["exp"]), int(row["r"]), int(row["k"])
        expected_b = list(range(1, (r - 1) // 2 + 1))
        observed_b = [int(item["b"]) for item in row["orbits"]]
        if observed_b != expected_b:
            raise ValueError(f"Orbit mismatch at {(exp, r, k)}")
        vector = np.asarray([float(item["energy"]) for item in row["orbits"]])
        if not np.all(np.isfinite(vector)):
            raise ValueError(f"Nonfinite orbit vector at {(exp, r, k)}")
        key = (exp, r, k)
        if key in vectors:
            raise ValueError(f"Duplicate row: {key}")
        vectors[key] = vector
    for exp in EXPS:
        for r in PRIMARY_MODULI:
            modes = representative_modes(r)
            if any((exp, r, k) not in vectors for k in modes):
                raise ValueError(f"Incomplete representatives at {(exp, r)}")
    return vectors


def centered_vectors(
    vectors: Mapping[tuple[int, int, int], np.ndarray]
) -> dict[tuple[int, int, int], np.ndarray]:
    centered: dict[tuple[int, int, int], np.ndarray] = {}
    for exp in EXPS:
        for r in PRIMARY_MODULI:
            modes = representative_modes(r)
            matrix = np.vstack([vectors[(exp, r, k)] for k in modes])
            local = matrix - np.mean(matrix, axis=0, keepdims=True)
            if np.max(np.abs(np.sum(local, axis=0))) > 1e-14:
                raise AssertionError(f"Within-window centering failed at {(exp, r)}")
            for index, k in enumerate(modes):
                centered[(exp, r, k)] = local[index]
    return centered


def structural_rank_max(r: int, character_count: int) -> int:
    orbit_count = (r - 1) // 2
    return min(orbit_count, 3 * (character_count - 1))


def select_rank(singular_values: Sequence[float], threshold: float = TRAIN_EXPLAINED_THRESHOLD) -> tuple[int, float]:
    values = np.asarray(singular_values, dtype=float)
    energy = values * values
    total = float(np.sum(energy))
    if total <= 0:
        raise ValueError("Degenerate training spectrum")
    cumulative = np.cumsum(energy) / total
    rank = int(np.searchsorted(cumulative, threshold, side="left") + 1)
    return rank, float(cumulative[rank - 1])


def projection_metrics(matrix: np.ndarray, basis: np.ndarray) -> dict:
    if matrix.ndim != 2 or basis.ndim != 2 or matrix.shape[1] != basis.shape[0]:
        raise ValueError("Incompatible projection arrays")
    orthogonality_error = float(
        np.max(np.abs(basis.T @ basis - np.eye(basis.shape[1])))
    )
    projected = matrix @ basis @ basis.T
    vector_ss = float(np.sum(matrix * matrix))
    vector_sse = float(np.sum((matrix - projected) ** 2))
    if vector_ss <= 0:
        raise ValueError("Degenerate held-out orbit matrix")
    vector_skill = 1.0 - vector_sse / vector_ss
    target = np.sum(matrix, axis=1)
    prediction = np.sum(projected, axis=1)
    scalar_ss = float(np.sum(target * target))
    scalar_sse = float(np.sum((target - prediction) ** 2))
    scalar_skill = 1.0 - scalar_sse / scalar_ss if scalar_ss > 0 else float("nan")
    return {
        "vector_ss": vector_ss,
        "vector_sse": vector_sse,
        "vector_captured": vector_ss - vector_sse,
        "vector_skill": vector_skill,
        "scalar_ss": scalar_ss,
        "scalar_sse": scalar_sse,
        "scalar_skill": scalar_skill,
        "orthogonality_error": orthogonality_error,
    }


def analyze_fold(
    centered: Mapping[tuple[int, int, int], np.ndarray], r: int, heldout_exp: int
) -> dict:
    modes = representative_modes(r)
    train_exps = [exp for exp in EXPS if exp != heldout_exp]
    character_means = {
        k: np.mean(
            np.vstack([centered[(exp, r, k)] for exp in train_exps]), axis=0
        )
        for k in modes
    }
    train_rows = [
        centered[(exp, r, k)] - character_means[k]
        for exp in train_exps
        for k in modes
    ]
    test_rows = [
        centered[(heldout_exp, r, k)] - character_means[k] for k in modes
    ]
    x_train = np.vstack(train_rows)
    x_test = np.vstack(test_rows)
    if max(
        float(np.max(np.abs(np.sum(
            np.vstack([x_train[index * len(modes) + modes.index(k)] for index in range(len(train_exps))]),
            axis=0,
        ))))
        for k in modes
    ) > 1e-14:
        raise AssertionError("Training-only character mean removal failed")

    _, singular_values, vt = np.linalg.svd(x_train, full_matrices=False)
    rank, explained = select_rank(singular_values)
    rank_max = structural_rank_max(r, len(modes))
    if rank > rank_max:
        raise AssertionError(f"Selected rank exceeds structural maximum at {(r, heldout_exp)}")
    basis = vt[:rank].T
    metrics = projection_metrics(x_test, basis)
    rank_one_metrics = projection_metrics(x_test, vt[:1].T)
    return {
        "r": r,
        "heldout_exp": heldout_exp,
        "training_exps": train_exps,
        "character_count": len(modes),
        "orbit_count": x_train.shape[1],
        "training_row_count": x_train.shape[0],
        "test_row_count": x_test.shape[0],
        "structural_rank_max": rank_max,
        "selected_rank": rank,
        "selected_rank_fraction_of_structural_max": rank / rank_max,
        "training_explained_fraction": explained,
        "normalized_singular_energy": [
            float(value * value / np.sum(singular_values * singular_values))
            for value in singular_values[:rank_max]
        ],
        "metrics": metrics,
        "rank_one_metrics": rank_one_metrics,
        "_basis": basis,
        "_test": x_test,
    }


def aggregate_metrics(folds: Sequence[dict], rank_one: bool = False) -> dict:
    key = "rank_one_metrics" if rank_one else "metrics"
    vector_ss = sum(fold[key]["vector_ss"] for fold in folds)
    vector_sse = sum(fold[key]["vector_sse"] for fold in folds)
    scalar_ss = sum(fold[key]["scalar_ss"] for fold in folds)
    scalar_sse = sum(fold[key]["scalar_sse"] for fold in folds)
    return {
        "fold_count": len(folds),
        "vector_ss": vector_ss,
        "vector_sse": vector_sse,
        "vector_skill": 1.0 - vector_sse / vector_ss,
        "scalar_ss": scalar_ss,
        "scalar_sse": scalar_sse,
        "scalar_skill": 1.0 - scalar_sse / scalar_ss,
    }


def random_subspace_null(
    folds: Sequence[dict], iterations: int = RANDOM_ITERATIONS, seed: int = RANDOM_SEED
) -> dict:
    rng = np.random.default_rng(seed)
    denominator = sum(float(np.sum(fold["_test"] ** 2)) for fold in folds)
    observed = sum(fold["metrics"]["vector_captured"] for fold in folds) / denominator
    samples = np.empty(iterations, dtype=float)
    for iteration in range(iterations):
        captured = 0.0
        for fold in folds:
            q = fold["orbit_count"]
            d = fold["selected_rank"]
            random_matrix = rng.normal(size=(q, d))
            basis, _ = np.linalg.qr(random_matrix, mode="reduced")
            coordinates = fold["_test"] @ basis
            captured += float(np.sum(coordinates * coordinates))
        samples[iteration] = captured / denominator
    exceedances = int(np.count_nonzero(samples >= observed))
    return {
        "iterations": iterations,
        "seed": seed,
        "observed_vector_skill": observed,
        "null_mean": float(np.mean(samples)),
        "null_population_sd": float(np.std(samples)),
        "null_quantiles": {
            "0.50": float(np.quantile(samples, 0.50)),
            "0.90": float(np.quantile(samples, 0.90)),
            "0.95": float(np.quantile(samples, 0.95)),
            "0.99": float(np.quantile(samples, 0.99)),
        },
        "null_maximum": float(np.max(samples)),
        "exceedance_count": exceedances,
        "one_sided_p_value": (exceedances + 1) / (iterations + 1),
    }


def subspace_overlap(folds: Sequence[dict]) -> list[dict]:
    output = []
    for r in PRIMARY_MODULI:
        local = [fold for fold in folds if fold["r"] == r]
        values = []
        for first_index, first in enumerate(local):
            for second in local[first_index + 1 :]:
                cross = first["_basis"].T @ second["_basis"]
                overlap = float(np.sum(cross * cross)) / min(
                    first["selected_rank"], second["selected_rank"]
                )
                values.append(overlap)
        output.append(
            {
                "r": r,
                "pair_count": len(values),
                "mean_overlap": statistics.fmean(values),
                "minimum_overlap": min(values),
                "maximum_overlap": max(values),
            }
        )
    return output


def public_fold(fold: Mapping) -> dict:
    return {key: value for key, value in fold.items() if not key.startswith("_")}


def decision_summary(
    folds: Sequence[dict], global_metrics: Mapping, random_null: Mapping
) -> dict:
    weighted_rank_fraction = sum(fold["selected_rank"] for fold in folds) / sum(
        fold["structural_rank_max"] for fold in folds
    )
    by_modulus = []
    for r in PRIMARY_MODULI:
        local = [fold for fold in folds if fold["r"] == r]
        metrics = aggregate_metrics(local)
        by_modulus.append(
            {
                "r": r,
                "selected_ranks": [fold["selected_rank"] for fold in local],
                "structural_rank_max": local[0]["structural_rank_max"],
                "mean_selected_rank": statistics.fmean(
                    fold["selected_rank"] for fold in local
                ),
                "metrics": metrics,
            }
        )
    by_window = []
    for exp in EXPS:
        local = [fold for fold in folds if fold["heldout_exp"] == exp]
        by_window.append({"heldout_exp": exp, "metrics": aggregate_metrics(local)})
    passing_moduli = sum(
        row["metrics"]["vector_skill"] >= MIN_MODULUS_VECTOR_SKILL
        for row in by_modulus
    )
    conditions = {
        "weighted_rank_fraction_at_most_0_50": weighted_rank_fraction
        <= MAX_WEIGHTED_RANK_FRACTION,
        "global_vector_skill_at_least_0_60": global_metrics["vector_skill"]
        >= MIN_VECTOR_SKILL,
        "global_scalar_skill_at_least_0_30": global_metrics["scalar_skill"]
        >= MIN_SCALAR_SKILL,
        "random_subspace_p_at_most_0_01": random_null["one_sided_p_value"]
        <= MAX_RANDOM_P_VALUE,
        "at_least_five_moduli_vector_skill_at_least_0_50": passing_moduli
        >= REQUIRED_MODULUS_COUNT,
    }
    supported = all(conditions.values())
    return {
        "thresholds": {
            "maximum_weighted_rank_fraction": MAX_WEIGHTED_RANK_FRACTION,
            "minimum_global_vector_skill": MIN_VECTOR_SKILL,
            "minimum_global_scalar_skill": MIN_SCALAR_SKILL,
            "maximum_random_subspace_p_value": MAX_RANDOM_P_VALUE,
            "minimum_modulus_vector_skill": MIN_MODULUS_VECTOR_SKILL,
            "required_modulus_count": REQUIRED_MODULUS_COUNT,
        },
        "weighted_rank_fraction": weighted_rank_fraction,
        "passing_modulus_count": passing_moduli,
        "conditions": conditions,
        "supported": supported,
        "decision": (
            "stable_low_dimensional_collective_orbit_subspace"
            if supported
            else "no_stable_low_dimensional_collective_orbit_subspace_support"
        ),
        "by_modulus": by_modulus,
        "by_heldout_window": by_window,
    }


def build_result(path: Path, random_iterations: int = RANDOM_ITERATIONS) -> dict:
    vectors = load_vectors(path)
    centered = centered_vectors(vectors)
    folds = [
        analyze_fold(centered, r, heldout_exp)
        for r in PRIMARY_MODULI
        for heldout_exp in EXPS
    ]
    global_metrics = aggregate_metrics(folds)
    rank_one_metrics = aggregate_metrics(folds, rank_one=True)
    random_null = random_subspace_null(
        folds, iterations=random_iterations, seed=RANDOM_SEED
    )
    decision = decision_summary(folds, global_metrics, random_null)
    maximum_orthogonality_error = max(
        fold["metrics"]["orthogonality_error"] for fold in folds
    )
    minimum_vector_skill = min(fold["metrics"]["vector_skill"] for fold in folds)
    maximum_vector_skill = max(fold["metrics"]["vector_skill"] for fold in folds)
    if minimum_vector_skill < -1e-12 or maximum_vector_skill > 1.0 + 1e-12:
        raise AssertionError("Projection vector skill outside [0,1]")
    return {
        "pass": "PASS029",
        "title": "Held-out-window stability of the collective nonzero-orbit subspace",
        "classification": "finite held-out subspace-containment diagnostic",
        "interpretation_guard": (
            "Projection coordinates use the held-out vector. This tests subspace containment, "
            "not forecastability without observing that vector."
        ),
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "exps": list(EXPS),
            "moduli": list(PRIMARY_MODULI),
            "training_explained_threshold": TRAIN_EXPLAINED_THRESHOLD,
            "random_iterations": random_iterations,
            "random_seed": RANDOM_SEED,
            "input_file": path.name,
            "input_sha256": sha256_file(path),
        },
        "global_metrics": global_metrics,
        "rank_one_secondary": rank_one_metrics,
        "random_subspace_null": random_null,
        "decision": decision,
        "subspace_overlap_secondary": subspace_overlap(folds),
        "diagnostics": {
            "fold_count": len(folds),
            "maximum_orthogonality_error": maximum_orthogonality_error,
            "minimum_fold_vector_skill": minimum_vector_skill,
            "maximum_fold_vector_skill": maximum_vector_skill,
        },
        "folds": [public_fold(fold) for fold in folds],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pass028", type=Path, default=default_pass028_path())
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument("--random-iterations", type=int, default=RANDOM_ITERATIONS)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(args.pass028, random_iterations=args.random_iterations)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"PASS029 result: {args.output}")
    print(
        "vector skill=",
        f'{result["global_metrics"]["vector_skill"]:.6f}',
        "scalar skill=",
        f'{result["global_metrics"]["scalar_skill"]:.6f}',
        "random p=",
        f'{result["random_subspace_null"]["one_sided_p_value"]:.6f}',
    )
    print("decision:", result["decision"]["decision"])


if __name__ == "__main__":
    main()
