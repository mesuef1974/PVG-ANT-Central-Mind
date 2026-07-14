#!/usr/bin/env python3
"""PASS030: equal-rank orbit subspaces constrained to preserve the sum.

Each PASS029 rank budget is reused unchanged.  The constrained basis contains
the normalized all-ones direction and spends its remaining dimensions on the
leading training SVD directions inside the orthogonal complement.  This makes
sum preservation algebraic; the empirical question is the held-out vector
cost relative to unconstrained and equally constrained random subspaces.
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
EXPECTED_PASS029_SHA256 = (
    "0f0185811cd6b5ae50b98f1c96e61d18b8fb2864d9f1ecfa3f692eb870f1ab0f"
)
RANDOM_ITERATIONS = 5000
RANDOM_SEED = 300719
MAX_WEIGHTED_RANK_FRACTION = 0.50
MIN_VECTOR_SKILL = 0.60
MIN_SCALAR_SKILL = 0.99
MAX_VECTOR_SKILL_LOSS = 0.10
MAX_RANDOM_P_VALUE = 0.01
MIN_MODULUS_VECTOR_SKILL = 0.50
REQUIRED_MODULUS_COUNT = 5


def load_pass029_module():
    try:
        return importlib.import_module("avrg_pass029")
    except ModuleNotFoundError:
        sibling = Path(__file__).resolve().parents[1] / "pass029"
        sys.path.insert(0, str(sibling))
        return importlib.import_module("avrg_pass029")


def default_pass028_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass028_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass028" / "avrg_pass028_results.json"


def default_pass029_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass029_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass029" / "avrg_pass029_results.json"


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_results = here.parent / "results"
    if archive_results.is_dir():
        return archive_results / "avrg_pass030_results.json"
    return here / "avrg_pass030_results.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_locked_pass029(path: Path) -> dict:
    observed = sha256_file(path)
    if observed != EXPECTED_PASS029_SHA256:
        raise ValueError(f"PASS029 hash mismatch: {observed}")
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if data.get("pass") != "PASS029" or len(data.get("folds", [])) != 35:
        raise ValueError("Invalid PASS029 result")
    return data


def build_train_test(centered: Mapping, r: int, heldout_exp: int, p29) -> tuple[np.ndarray, np.ndarray]:
    modes = p29.representative_modes(r)
    train_exps = [exp for exp in p29.EXPS if exp != heldout_exp]
    character_means = {
        k: np.mean(
            np.vstack([centered[(exp, r, k)] for exp in train_exps]), axis=0
        )
        for k in modes
    }
    x_train = np.vstack(
        [
            centered[(exp, r, k)] - character_means[k]
            for exp in train_exps
            for k in modes
        ]
    )
    x_test = np.vstack(
        [centered[(heldout_exp, r, k)] - character_means[k] for k in modes]
    )
    return x_train, x_test


def sum_aware_basis(x_train: np.ndarray, rank: int) -> tuple[np.ndarray, np.ndarray]:
    if x_train.ndim != 2 or rank < 1 or rank > x_train.shape[1]:
        raise ValueError("Invalid constrained-basis inputs")
    q = x_train.shape[1]
    sum_direction = np.ones(q, dtype=float) / np.sqrt(q)
    if rank == 1:
        basis = sum_direction[:, None]
    else:
        perpendicular = x_train - (x_train @ sum_direction)[:, None] * sum_direction
        _, _, vt = np.linalg.svd(perpendicular, full_matrices=False)
        candidates = vt[: rank - 1].T
        candidates = candidates - sum_direction[:, None] * (
            sum_direction @ candidates
        )[None, :]
        candidate_basis, _ = np.linalg.qr(candidates, mode="reduced")
        basis = np.column_stack([sum_direction, candidate_basis[:, : rank - 1]])
    orthogonality_error = float(
        np.max(np.abs(basis.T @ basis - np.eye(rank)))
    )
    containment_error = float(
        np.max(np.abs(basis @ basis.T @ sum_direction - sum_direction))
    )
    if orthogonality_error > 1e-12 or containment_error > 1e-12:
        raise AssertionError("Constrained basis safety check failed")
    return basis, sum_direction


def analyze_fold(centered: Mapping, base_fold: Mapping, p29) -> dict:
    r = int(base_fold["r"])
    heldout_exp = int(base_fold["heldout_exp"])
    rank = int(base_fold["selected_rank"])
    x_train, x_test = build_train_test(centered, r, heldout_exp, p29)
    basis, sum_direction = sum_aware_basis(x_train, rank)
    constrained = p29.projection_metrics(x_test, basis)
    sum_only = p29.projection_metrics(x_test, sum_direction[:, None])
    unconstrained = base_fold["metrics"]
    if abs(unconstrained["vector_skill"] - base_fold["metrics"]["vector_skill"]) > 1e-15:
        raise AssertionError("PASS029 metric mismatch")
    ones = np.ones(x_test.shape[1])
    projector_sum_error = float(
        np.max(np.abs(basis @ basis.T @ ones - ones))
    )
    sum_direction_fraction = float(np.sum((x_test @ sum_direction) ** 2)) / float(
        np.sum(x_test * x_test)
    )
    return {
        "r": r,
        "heldout_exp": heldout_exp,
        "selected_rank": rank,
        "structural_rank_max": int(base_fold["structural_rank_max"]),
        "orbit_count": int(base_fold["orbit_count"]),
        "constrained_metrics": constrained,
        "unconstrained_metrics": unconstrained,
        "sum_only_metrics": sum_only,
        "vector_skill_loss_vs_unconstrained": unconstrained["vector_skill"]
        - constrained["vector_skill"],
        "heldout_vector_fraction_in_sum_direction": sum_direction_fraction,
        "projector_sum_error": projector_sum_error,
        "_basis": basis,
        "_sum_direction": sum_direction,
        "_test": x_test,
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


def random_constrained_basis(q: int, rank: int, rng: np.random.Generator) -> np.ndarray:
    sum_direction = np.ones(q, dtype=float) / np.sqrt(q)
    if rank == 1:
        return sum_direction[:, None]
    random_matrix = rng.normal(size=(q, rank - 1))
    random_matrix -= sum_direction[:, None] * (sum_direction @ random_matrix)[None, :]
    complement, _ = np.linalg.qr(random_matrix, mode="reduced")
    return np.column_stack([sum_direction, complement[:, : rank - 1]])


def random_constrained_null(
    folds: Sequence[dict], iterations: int = RANDOM_ITERATIONS, seed: int = RANDOM_SEED
) -> dict:
    rng = np.random.default_rng(seed)
    denominator = sum(float(np.sum(fold["_test"] ** 2)) for fold in folds)
    observed = sum(
        fold["constrained_metrics"]["vector_captured"] for fold in folds
    ) / denominator
    samples = np.empty(iterations, dtype=float)
    for iteration in range(iterations):
        captured = 0.0
        for fold in folds:
            basis = random_constrained_basis(
                fold["orbit_count"], fold["selected_rank"], rng
            )
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


def subspace_overlap(folds: Sequence[dict], moduli: Sequence[int]) -> list[dict]:
    output = []
    for r in moduli:
        local = [fold for fold in folds if fold["r"] == r]
        values = []
        for index, first in enumerate(local):
            for second in local[index + 1 :]:
                cross = first["_basis"].T @ second["_basis"]
                values.append(
                    float(np.sum(cross * cross))
                    / min(first["selected_rank"], second["selected_rank"])
                )
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


def decision_summary(
    folds: Sequence[dict], constrained: Mapping, unconstrained: Mapping, null: Mapping, p29
) -> dict:
    weighted_rank_fraction = sum(fold["selected_rank"] for fold in folds) / sum(
        fold["structural_rank_max"] for fold in folds
    )
    vector_skill_loss = unconstrained["vector_skill"] - constrained["vector_skill"]
    by_modulus = []
    for r in p29.PRIMARY_MODULI:
        local = [fold for fold in folds if fold["r"] == r]
        by_modulus.append(
            {
                "r": r,
                "constrained": aggregate_metrics(local, "constrained_metrics"),
                "unconstrained": aggregate_metrics(local, "unconstrained_metrics"),
                "sum_only": aggregate_metrics(local, "sum_only_metrics"),
            }
        )
    by_window = []
    for exp in p29.EXPS:
        local = [fold for fold in folds if fold["heldout_exp"] == exp]
        by_window.append(
            {
                "heldout_exp": exp,
                "constrained": aggregate_metrics(local, "constrained_metrics"),
                "unconstrained": aggregate_metrics(local, "unconstrained_metrics"),
            }
        )
    passing_moduli = sum(
        row["constrained"]["vector_skill"] >= MIN_MODULUS_VECTOR_SKILL
        for row in by_modulus
    )
    conditions = {
        "weighted_rank_fraction_at_most_0_50": weighted_rank_fraction
        <= MAX_WEIGHTED_RANK_FRACTION,
        "constrained_vector_skill_at_least_0_60": constrained["vector_skill"]
        >= MIN_VECTOR_SKILL,
        "scalar_skill_at_least_0_99_identity_check": constrained["scalar_skill"]
        >= MIN_SCALAR_SKILL,
        "vector_skill_loss_at_most_0_10": vector_skill_loss
        <= MAX_VECTOR_SKILL_LOSS,
        "constrained_random_p_at_most_0_01": null["one_sided_p_value"]
        <= MAX_RANDOM_P_VALUE,
        "at_least_five_moduli_vector_skill_at_least_0_50": passing_moduli
        >= REQUIRED_MODULUS_COUNT,
    }
    supported = all(conditions.values())
    return {
        "thresholds": {
            "maximum_weighted_rank_fraction": MAX_WEIGHTED_RANK_FRACTION,
            "minimum_constrained_vector_skill": MIN_VECTOR_SKILL,
            "minimum_scalar_skill_identity_check": MIN_SCALAR_SKILL,
            "maximum_vector_skill_loss": MAX_VECTOR_SKILL_LOSS,
            "maximum_constrained_random_p_value": MAX_RANDOM_P_VALUE,
            "minimum_modulus_vector_skill": MIN_MODULUS_VECTOR_SKILL,
            "required_modulus_count": REQUIRED_MODULUS_COUNT,
        },
        "weighted_rank_fraction": weighted_rank_fraction,
        "vector_skill_loss_vs_unconstrained": vector_skill_loss,
        "passing_modulus_count": passing_moduli,
        "conditions": conditions,
        "supported": supported,
        "decision": (
            "sum_preserving_low_dimensional_subspace_with_limited_vector_cost"
            if supported
            else "no_sum_preserving_low_dimensional_subspace_with_limited_vector_cost_support"
        ),
        "by_modulus": by_modulus,
        "by_heldout_window": by_window,
    }


def public_fold(fold: Mapping) -> dict:
    return {key: value for key, value in fold.items() if not key.startswith("_")}


def build_result(
    pass028_path: Path,
    pass029_path: Path,
    random_iterations: int = RANDOM_ITERATIONS,
) -> dict:
    if sha256_file(pass028_path) != EXPECTED_PASS028_SHA256:
        raise ValueError("PASS028 hash mismatch")
    locked = load_locked_pass029(pass029_path)
    p29 = load_pass029_module()
    vectors = p29.load_vectors(pass028_path)
    centered = p29.centered_vectors(vectors)
    locked_folds = {
        (int(row["r"]), int(row["heldout_exp"])): row for row in locked["folds"]
    }
    folds = [
        analyze_fold(centered, locked_folds[(r, exp)], p29)
        for r in p29.PRIMARY_MODULI
        for exp in p29.EXPS
    ]
    constrained = aggregate_metrics(folds, "constrained_metrics")
    unconstrained = aggregate_metrics(folds, "unconstrained_metrics")
    sum_only = aggregate_metrics(folds, "sum_only_metrics")
    if abs(unconstrained["vector_skill"] - locked["global_metrics"]["vector_skill"]) > 1e-12:
        raise AssertionError("PASS029 vector skill was not reproduced")
    if abs(unconstrained["scalar_skill"] - locked["global_metrics"]["scalar_skill"]) > 1e-12:
        raise AssertionError("PASS029 scalar skill was not reproduced")
    null = random_constrained_null(
        folds, iterations=random_iterations, seed=RANDOM_SEED
    )
    decision = decision_summary(folds, constrained, unconstrained, null, p29)
    return {
        "pass": "PASS030",
        "title": "Equal-rank sum-aware nonzero-orbit subspace",
        "classification": "finite held-out constrained-subspace diagnostic",
        "interpretation_guard": (
            "Scalar-sum preservation is exact by construction and is not empirical evidence. "
            "The empirical test is held-out vector retention under the same rank budget."
        ),
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "exps": list(p29.EXPS),
            "moduli": list(p29.PRIMARY_MODULI),
            "random_iterations": random_iterations,
            "random_seed": RANDOM_SEED,
            "input_sha256": {
                pass028_path.name: sha256_file(pass028_path),
                pass029_path.name: sha256_file(pass029_path),
            },
        },
        "constrained_global": constrained,
        "unconstrained_pass029_global": unconstrained,
        "sum_direction_only_secondary": sum_only,
        "constrained_random_null": null,
        "decision": decision,
        "subspace_overlap_secondary": subspace_overlap(folds, p29.PRIMARY_MODULI),
        "secondary": {
            "mean_heldout_vector_fraction_in_sum_direction": statistics.fmean(
                fold["heldout_vector_fraction_in_sum_direction"] for fold in folds
            ),
            "maximum_projector_sum_error": max(
                fold["projector_sum_error"] for fold in folds
            ),
            "folds_constrained_vector_skill_exceeds_unconstrained": sum(
                fold["constrained_metrics"]["vector_skill"]
                > fold["unconstrained_metrics"]["vector_skill"]
                for fold in folds
            ),
            "fold_count": len(folds),
        },
        "folds": [public_fold(fold) for fold in folds],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pass028", type=Path, default=default_pass028_path())
    parser.add_argument("--pass029", type=Path, default=default_pass029_path())
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument("--random-iterations", type=int, default=RANDOM_ITERATIONS)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(
        args.pass028, args.pass029, random_iterations=args.random_iterations
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"PASS030 result: {args.output}")
    print(
        "constrained vector skill=",
        f'{result["constrained_global"]["vector_skill"]:.6f}',
        "scalar skill=",
        f'{result["constrained_global"]["scalar_skill"]:.6f}',
        "loss=",
        f'{result["decision"]["vector_skill_loss_vs_unconstrained"]:.6f}',
    )
    print(
        "conditioned random p=",
        f'{result["constrained_random_null"]["one_sided_p_value"]:.6f}',
    )
    print("decision:", result["decision"]["decision"])


if __name__ == "__main__":
    main()
