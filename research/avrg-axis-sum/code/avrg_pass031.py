#!/usr/bin/env python3
"""PASS031: add one cancellation coordinate above the locked amplitude rank.

Every PASS029 rank d is retained for amplitude directions in the sum-orthogonal
complement, while the normalized all-ones direction is added as coordinate
d+1.  The held-out vector skill is compared with rank-d and rank-(d+1)
unconstrained SVD bases and with rank-(d+1) random sum-constrained subspaces.
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
EXPECTED_PASS030_SHA256 = (
    "8737913d3f4c24f7e29cae8eea19ab2b796819b7f1a022f3b27af16db60e46d9"
)
RANDOM_ITERATIONS = 5000
RANDOM_SEED = 310719
MIN_AUGMENTED_VECTOR_SKILL = 0.65
MIN_SCALAR_SKILL = 0.99
MAX_LOSS_VS_RANK_D = 0.03
MAX_LOSS_VS_FREE_RANK_D_PLUS_ONE = 0.10
MAX_RANDOM_P_VALUE = 0.01
MIN_MODULUS_VECTOR_SKILL = 0.60
REQUIRED_MODULUS_COUNT = 5


def load_pass030_module():
    try:
        return importlib.import_module("avrg_pass030")
    except ModuleNotFoundError:
        sibling = Path(__file__).resolve().parents[1] / "pass030"
        sys.path.insert(0, str(sibling))
        return importlib.import_module("avrg_pass030")


def default_pass028_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass028_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass028" / "avrg_pass028_results.json"


def default_pass030_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass030_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass030" / "avrg_pass030_results.json"


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_results = here.parent / "results"
    if archive_results.is_dir():
        return archive_results / "avrg_pass031_results.json"
    return here / "avrg_pass031_results.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_locked_pass030(path: Path) -> dict:
    observed = sha256_file(path)
    if observed != EXPECTED_PASS030_SHA256:
        raise ValueError(f"PASS030 hash mismatch: {observed}")
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if data.get("pass") != "PASS030" or len(data.get("folds", [])) != 35:
        raise ValueError("Invalid PASS030 result")
    return data


def analyze_fold(centered: Mapping, locked_fold: Mapping, p30, p29) -> dict:
    r = int(locked_fold["r"])
    heldout_exp = int(locked_fold["heldout_exp"])
    rank_d = int(locked_fold["selected_rank"])
    rank_augmented = rank_d + 1
    orbit_count = int(locked_fold["orbit_count"])
    if rank_augmented > orbit_count:
        raise ValueError(f"No ambient room for extra coordinate at {(r, heldout_exp)}")
    x_train, x_test = p30.build_train_test(centered, r, heldout_exp, p29)
    augmented_basis, sum_direction = p30.sum_aware_basis(x_train, rank_augmented)
    augmented = p29.projection_metrics(x_test, augmented_basis)
    _, _, vt = np.linalg.svd(x_train, full_matrices=False)
    free_d_plus_one_basis = vt[:rank_augmented].T
    free_d_plus_one = p29.projection_metrics(x_test, free_d_plus_one_basis)
    base_rank_d = locked_fold["unconstrained_metrics"]
    equal_rank_constrained = locked_fold["constrained_metrics"]
    ones = np.ones(orbit_count)
    return {
        "r": r,
        "heldout_exp": heldout_exp,
        "rank_d": rank_d,
        "rank_augmented": rank_augmented,
        "orbit_count": orbit_count,
        "augmented_metrics": augmented,
        "base_rank_d_unconstrained_metrics": base_rank_d,
        "equal_rank_d_constrained_metrics": equal_rank_constrained,
        "free_rank_d_plus_one_metrics": free_d_plus_one,
        "loss_vs_base_rank_d": base_rank_d["vector_skill"]
        - augmented["vector_skill"],
        "loss_vs_free_rank_d_plus_one": free_d_plus_one["vector_skill"]
        - augmented["vector_skill"],
        "projector_sum_error": float(
            np.max(np.abs(augmented_basis @ augmented_basis.T @ ones - ones))
        ),
        "_basis": augmented_basis,
        "_test": x_test,
        "_sum_direction": sum_direction,
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


def constrained_random_null(
    folds: Sequence[dict], p30, iterations: int = RANDOM_ITERATIONS, seed: int = RANDOM_SEED
) -> dict:
    adapted = [
        {
            "orbit_count": fold["orbit_count"],
            "selected_rank": fold["rank_augmented"],
            "_test": fold["_test"],
            "constrained_metrics": fold["augmented_metrics"],
        }
        for fold in folds
    ]
    return p30.random_constrained_null(adapted, iterations=iterations, seed=seed)


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
                    / min(first["rank_augmented"], second["rank_augmented"])
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
    folds: Sequence[dict],
    augmented: Mapping,
    base_d: Mapping,
    free_d_plus_one: Mapping,
    null: Mapping,
    p29,
) -> dict:
    loss_vs_d = base_d["vector_skill"] - augmented["vector_skill"]
    loss_vs_free_plus = free_d_plus_one["vector_skill"] - augmented["vector_skill"]
    rank_overhead = (
        sum(fold["rank_augmented"] for fold in folds)
        - sum(fold["rank_d"] for fold in folds)
    ) / sum(fold["rank_d"] for fold in folds)
    by_modulus = []
    for r in p29.PRIMARY_MODULI:
        local = [fold for fold in folds if fold["r"] == r]
        by_modulus.append(
            {
                "r": r,
                "augmented": aggregate_metrics(local, "augmented_metrics"),
                "base_rank_d": aggregate_metrics(
                    local, "base_rank_d_unconstrained_metrics"
                ),
                "equal_rank_d_constrained": aggregate_metrics(
                    local, "equal_rank_d_constrained_metrics"
                ),
                "free_rank_d_plus_one": aggregate_metrics(
                    local, "free_rank_d_plus_one_metrics"
                ),
            }
        )
    by_window = []
    for exp in p29.EXPS:
        local = [fold for fold in folds if fold["heldout_exp"] == exp]
        by_window.append(
            {
                "heldout_exp": exp,
                "augmented": aggregate_metrics(local, "augmented_metrics"),
                "base_rank_d": aggregate_metrics(
                    local, "base_rank_d_unconstrained_metrics"
                ),
                "free_rank_d_plus_one": aggregate_metrics(
                    local, "free_rank_d_plus_one_metrics"
                ),
            }
        )
    passing_moduli = sum(
        row["augmented"]["vector_skill"] >= MIN_MODULUS_VECTOR_SKILL
        for row in by_modulus
    )
    conditions = {
        "augmented_vector_skill_at_least_0_65": augmented["vector_skill"]
        >= MIN_AUGMENTED_VECTOR_SKILL,
        "scalar_skill_at_least_0_99_identity_check": augmented["scalar_skill"]
        >= MIN_SCALAR_SKILL,
        "loss_vs_rank_d_at_most_0_03": loss_vs_d <= MAX_LOSS_VS_RANK_D,
        "loss_vs_free_rank_d_plus_one_at_most_0_10": loss_vs_free_plus
        <= MAX_LOSS_VS_FREE_RANK_D_PLUS_ONE,
        "constrained_random_p_at_most_0_01": null["one_sided_p_value"]
        <= MAX_RANDOM_P_VALUE,
        "at_least_five_moduli_vector_skill_at_least_0_60": passing_moduli
        >= REQUIRED_MODULUS_COUNT,
    }
    supported = all(conditions.values())
    return {
        "thresholds": {
            "minimum_augmented_vector_skill": MIN_AUGMENTED_VECTOR_SKILL,
            "minimum_scalar_skill_identity_check": MIN_SCALAR_SKILL,
            "maximum_loss_vs_rank_d": MAX_LOSS_VS_RANK_D,
            "maximum_loss_vs_free_rank_d_plus_one": MAX_LOSS_VS_FREE_RANK_D_PLUS_ONE,
            "maximum_constrained_random_p_value": MAX_RANDOM_P_VALUE,
            "minimum_modulus_vector_skill": MIN_MODULUS_VECTOR_SKILL,
            "required_modulus_count": REQUIRED_MODULUS_COUNT,
        },
        "rank_overhead_fraction_vs_rank_d": rank_overhead,
        "loss_vs_base_rank_d": loss_vs_d,
        "loss_vs_free_rank_d_plus_one": loss_vs_free_plus,
        "passing_modulus_count": passing_moduli,
        "conditions": conditions,
        "supported": supported,
        "decision": (
            "one_extra_cancellation_coordinate_sufficient_on_finite_range"
            if supported
            else "one_extra_cancellation_coordinate_not_sufficient_under_locked_rule"
        ),
        "by_modulus": by_modulus,
        "by_heldout_window": by_window,
    }


def public_fold(fold: Mapping) -> dict:
    return {key: value for key, value in fold.items() if not key.startswith("_")}


def build_result(
    pass028_path: Path,
    pass030_path: Path,
    random_iterations: int = RANDOM_ITERATIONS,
) -> dict:
    if sha256_file(pass028_path) != EXPECTED_PASS028_SHA256:
        raise ValueError("PASS028 hash mismatch")
    locked = load_locked_pass030(pass030_path)
    p30 = load_pass030_module()
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
    augmented = aggregate_metrics(folds, "augmented_metrics")
    base_d = aggregate_metrics(folds, "base_rank_d_unconstrained_metrics")
    equal_d = aggregate_metrics(folds, "equal_rank_d_constrained_metrics")
    free_plus = aggregate_metrics(folds, "free_rank_d_plus_one_metrics")
    if abs(base_d["vector_skill"] - locked["unconstrained_pass029_global"]["vector_skill"]) > 1e-12:
        raise AssertionError("PASS030 base metric mismatch")
    if abs(equal_d["vector_skill"] - locked["constrained_global"]["vector_skill"]) > 1e-12:
        raise AssertionError("PASS030 constrained metric mismatch")
    null = constrained_random_null(
        folds, p30, iterations=random_iterations, seed=RANDOM_SEED
    )
    decision = decision_summary(
        folds, augmented, base_d, free_plus, null, p29
    )
    return {
        "pass": "PASS031",
        "title": "One extra cancellation coordinate above the amplitude rank",
        "classification": "finite held-out augmented-subspace diagnostic",
        "interpretation_guard": (
            "The added sum coordinate preserves the scalar exactly by construction. "
            "Evidence concerns held-out vector recovery under one explicit extra dimension."
        ),
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "exps": list(p29.EXPS),
            "moduli": list(p29.PRIMARY_MODULI),
            "random_iterations": random_iterations,
            "random_seed": RANDOM_SEED,
            "rank_rule": "locked PASS029 d plus exactly one sum coordinate",
            "input_sha256": {
                pass028_path.name: sha256_file(pass028_path),
                pass030_path.name: sha256_file(pass030_path),
            },
        },
        "augmented_global": augmented,
        "base_rank_d_global": base_d,
        "equal_rank_d_constrained_global": equal_d,
        "free_rank_d_plus_one_global": free_plus,
        "constrained_random_null": null,
        "decision": decision,
        "subspace_overlap_secondary": subspace_overlap(folds, p29.PRIMARY_MODULI),
        "secondary": {
            "fold_count": len(folds),
            "folds_augmented_at_least_base_rank_d_vector_skill": sum(
                fold["augmented_metrics"]["vector_skill"]
                >= fold["base_rank_d_unconstrained_metrics"]["vector_skill"]
                for fold in folds
            ),
            "folds_augmented_above_equal_rank_d_constrained": sum(
                fold["augmented_metrics"]["vector_skill"]
                > fold["equal_rank_d_constrained_metrics"]["vector_skill"]
                for fold in folds
            ),
            "maximum_projector_sum_error": max(
                fold["projector_sum_error"] for fold in folds
            ),
        },
        "folds": [public_fold(fold) for fold in folds],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pass028", type=Path, default=default_pass028_path())
    parser.add_argument("--pass030", type=Path, default=default_pass030_path())
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument("--random-iterations", type=int, default=RANDOM_ITERATIONS)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(
        args.pass028, args.pass030, random_iterations=args.random_iterations
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"PASS031 result: {args.output}")
    print(
        "augmented vector skill=",
        f'{result["augmented_global"]["vector_skill"]:.6f}',
        "scalar skill=",
        f'{result["augmented_global"]["scalar_skill"]:.6f}',
        "loss vs d=",
        f'{result["decision"]["loss_vs_base_rank_d"]:.6f}',
    )
    print(
        "loss vs free d+1=",
        f'{result["decision"]["loss_vs_free_rank_d_plus_one"]:.6f}',
        "random p=",
        f'{result["constrained_random_null"]["one_sided_p_value"]:.6f}',
    )
    print("decision:", result["decision"]["decision"])


if __name__ == "__main__":
    main()
