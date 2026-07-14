#!/usr/bin/env python3
"""PASS034: held-out rank-two subspace test for cancellation functionals.

The five PASS033 functionals for each modulus are treated as signed unit vectors in
the common orbit space.  For each deleted window, a rank-one and a locked
rank-two subspace are learned from the other four functionals.  Held-out squared
projection is compared with the same overlap-aware restricted-permutation null
used by PASS033.
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
EXPECTED_PASS033_SHA256 = (
    "9d0641a61af4f9839ed210c6e4fdcac120935cf9d3f4699c1d56b1713f99c8c8"
)
PERMUTATION_ITERATIONS = 5000
PERMUTATION_SEED = 340719
MIN_GLOBAL_RANK2_SCORE = 0.75
MAX_RANK2_PERMUTATION_P = 0.01
MIN_GLOBAL_RANK2_GAIN = 0.10
MIN_MODULUS_RANK2_SCORE = 0.65
MIN_WINDOW_RANK2_SCORE = 0.60
REQUIRED_MODULUS_COUNT = 5
REQUIRED_WINDOW_COUNT = 4


def load_pass033_module():
    try:
        return importlib.import_module("avrg_pass033")
    except ModuleNotFoundError:
        sibling = Path(__file__).resolve().parents[1] / "pass033"
        sys.path.insert(0, str(sibling))
        return importlib.import_module("avrg_pass033")


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


def default_pass033_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass033_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass033" / "avrg_pass033_results.json"


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_results = here.parent / "results"
    if archive_results.is_dir():
        return archive_results / "avrg_pass034_results.json"
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


def reconstruct_functionals(pass028_path: Path, pass032_path: Path, p33):
    if sha256_file(pass028_path) != EXPECTED_PASS028_SHA256:
        raise ValueError("PASS028 hash mismatch")
    locked032 = load_locked_json(pass032_path, EXPECTED_PASS032_SHA256, "PASS032")
    if len(locked032.get("folds", [])) != 35:
        raise ValueError("PASS032 must contain 35 folds")
    p32 = p33.load_pass032_module()
    p31 = p32.load_pass031_module()
    p30 = p31.load_pass030_module()
    p29 = p30.load_pass029_module()
    vectors = p29.load_vectors(pass028_path)
    centered = p29.centered_vectors(vectors)
    folds = [
        p33.functional_from_fold(centered, locked_fold, p32, p30, p29)
        for locked_fold in locked032["folds"]
    ]
    expected_order = [
        (int(row["r"]), int(row["heldout_exp"])) for row in locked032["folds"]
    ]
    observed_order = [(row["r"], row["heldout_exp"]) for row in folds]
    if observed_order != expected_order:
        raise AssertionError("Fold order mismatch")
    return folds, centered, locked032, p32, p29


def projection_score(vector: np.ndarray, basis_rows: np.ndarray) -> float:
    score = float(np.sum((basis_rows @ vector) ** 2))
    tolerance = 1e-10
    if score < -tolerance or score > 1 + tolerance:
        raise AssertionError(f"Projection score outside [0,1]: {score}")
    return min(1.0, max(0.0, score))


def leave_one_out_subspace_scores(units: np.ndarray) -> list[dict]:
    units = np.asarray(units, dtype=float)
    if units.ndim != 2 or units.shape[0] != 5:
        raise ValueError("Exactly five unit functionals are required")
    norms = np.linalg.norm(units, axis=1)
    if np.max(np.abs(norms - 1.0)) > 1e-10:
        raise ValueError("Functionals must be unit vectors")
    output = []
    for heldout_index in range(units.shape[0]):
        train = np.delete(units, heldout_index, axis=0)
        _, singular_values, vh = np.linalg.svd(train, full_matrices=False)
        numerical_rank = int(np.count_nonzero(singular_values > 1e-12))
        if numerical_rank < 2:
            raise ValueError("Training functionals have numerical rank below two")
        target = units[heldout_index]
        rank1 = projection_score(target, vh[:1])
        rank2 = projection_score(target, vh[:2])
        if rank2 + 1e-12 < rank1:
            raise AssertionError("Rank-two score is below rank-one score")
        rank3 = projection_score(target, vh[:3]) if numerical_rank >= 3 else None
        output.append(
            {
                "heldout_index": heldout_index,
                "training_numerical_rank": numerical_rank,
                "rank1_projection_score": rank1,
                "rank2_projection_score": rank2,
                "rank2_gain_over_rank1": rank2 - rank1,
                "rank3_projection_score_secondary": rank3,
                "rank2_angle_degrees": float(
                    np.degrees(np.arccos(np.sqrt(min(1.0, max(0.0, rank2)))))
                ),
            }
        )
    return output


def score_functionals(folds: Sequence[dict], moduli: Sequence[int]) -> dict:
    rows = []
    by_modulus = []
    for r in moduli:
        local = sorted(
            (fold for fold in folds if int(fold["r"]) == int(r)),
            key=lambda fold: int(fold["heldout_exp"]),
        )
        if len(local) != 5:
            raise ValueError(f"Expected five functionals for r={r}")
        units = np.vstack([np.asarray(fold["_unit"], dtype=float) for fold in local])
        scores = leave_one_out_subspace_scores(units)
        local_rows = []
        for fold, score in zip(local, scores):
            row = {
                "r": int(r),
                "heldout_exp": int(fold["heldout_exp"]),
                "rank_d": int(fold["rank_d"]),
                **score,
            }
            rows.append(row)
            local_rows.append(row)
        by_modulus.append(
            {
                "r": int(r),
                "mean_rank1_projection_score": float(
                    np.mean([row["rank1_projection_score"] for row in local_rows])
                ),
                "mean_rank2_projection_score": float(
                    np.mean([row["rank2_projection_score"] for row in local_rows])
                ),
                "mean_rank2_gain_over_rank1": float(
                    np.mean([row["rank2_gain_over_rank1"] for row in local_rows])
                ),
                "minimum_rank2_projection_score": float(
                    min(row["rank2_projection_score"] for row in local_rows)
                ),
                "folds": local_rows,
            }
        )
    rank1 = np.asarray([row["rank1_projection_score"] for row in rows])
    rank2 = np.asarray([row["rank2_projection_score"] for row in rows])
    gains = rank2 - rank1
    by_window = []
    for exp in sorted({int(row["heldout_exp"]) for row in rows}):
        local = [row for row in rows if int(row["heldout_exp"]) == exp]
        by_window.append(
            {
                "heldout_exp": exp,
                "mean_rank1_projection_score": float(
                    np.mean([row["rank1_projection_score"] for row in local])
                ),
                "mean_rank2_projection_score": float(
                    np.mean([row["rank2_projection_score"] for row in local])
                ),
                "mean_rank2_gain_over_rank1": float(
                    np.mean([row["rank2_gain_over_rank1"] for row in local])
                ),
            }
        )
    return {
        "fold_count": len(rows),
        "global": {
            "mean_rank1_projection_score": float(np.mean(rank1)),
            "mean_rank2_projection_score": float(np.mean(rank2)),
            "mean_rank2_gain_over_rank1": float(np.mean(gains)),
            "median_rank2_projection_score": float(np.median(rank2)),
            "minimum_rank2_projection_score": float(np.min(rank2)),
            "maximum_rank2_projection_score": float(np.max(rank2)),
            "fraction_folds_rank2_at_least_0_60": float(np.mean(rank2 >= 0.60)),
            "mean_rank2_angle_degrees": float(
                np.mean([row["rank2_angle_degrees"] for row in rows])
            ),
        },
        "by_modulus": by_modulus,
        "by_heldout_window": by_window,
        "folds": rows,
    }


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
    folds: Sequence[dict],
    raw_coefficients: Mapping,
    exps: Sequence[int],
    moduli: Sequence[int],
    p32,
    observed: Mapping,
    iterations: int = PERMUTATION_ITERATIONS,
    seed: int = PERMUTATION_SEED,
) -> dict:
    rng = np.random.default_rng(seed)
    rank2_samples = np.empty(iterations, dtype=float)
    gain_samples = np.empty(iterations, dtype=float)
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
                    "_unit": functional / norm,
                }
            )
        scored = score_functionals(simulated, moduli)["global"]
        rank2_samples[iteration] = scored["mean_rank2_projection_score"]
        gain_samples[iteration] = scored["mean_rank2_gain_over_rank1"]
    return {
        "iterations": iterations,
        "seed": seed,
        "restriction": "permute five windows independently within each (r,k)",
        "rank2_projection_primary": describe_null(
            rank2_samples, observed["mean_rank2_projection_score"]
        ),
        "rank2_gain_secondary": describe_null(
            gain_samples, observed["mean_rank2_gain_over_rank1"]
        ),
    }


def decision_summary(scored: Mapping, permutation: Mapping) -> dict:
    global_metrics = scored["global"]
    modulus_count = sum(
        row["mean_rank2_projection_score"] >= MIN_MODULUS_RANK2_SCORE
        for row in scored["by_modulus"]
    )
    window_count = sum(
        row["mean_rank2_projection_score"] >= MIN_WINDOW_RANK2_SCORE
        for row in scored["by_heldout_window"]
    )
    conditions = {
        "global_rank2_score_at_least_0_75": global_metrics[
            "mean_rank2_projection_score"
        ]
        >= MIN_GLOBAL_RANK2_SCORE,
        "restricted_permutation_p_at_most_0_01": permutation[
            "rank2_projection_primary"
        ]["one_sided_p_value"]
        <= MAX_RANK2_PERMUTATION_P,
        "global_rank2_gain_at_least_0_10": global_metrics[
            "mean_rank2_gain_over_rank1"
        ]
        >= MIN_GLOBAL_RANK2_GAIN,
        "at_least_five_moduli_rank2_score_at_least_0_65": modulus_count
        >= REQUIRED_MODULUS_COUNT,
        "at_least_four_windows_rank2_score_at_least_0_60": window_count
        >= REQUIRED_WINDOW_COUNT,
    }
    supported = all(conditions.values())
    return {
        "thresholds": {
            "minimum_global_rank2_score": MIN_GLOBAL_RANK2_SCORE,
            "maximum_restricted_permutation_p": MAX_RANK2_PERMUTATION_P,
            "minimum_global_rank2_gain": MIN_GLOBAL_RANK2_GAIN,
            "minimum_modulus_rank2_score": MIN_MODULUS_RANK2_SCORE,
            "minimum_window_rank2_score": MIN_WINDOW_RANK2_SCORE,
            "required_modulus_count": REQUIRED_MODULUS_COUNT,
            "required_window_count": REQUIRED_WINDOW_COUNT,
        },
        "qualifying_modulus_count": int(modulus_count),
        "qualifying_window_count": int(window_count),
        "conditions": conditions,
        "supported": supported,
        "decision": (
            "stable_rank2_functional_plane_on_finite_range"
            if supported
            else "no_stable_rank2_functional_plane_under_locked_rule"
        ),
    }


def correlation(xs: Sequence[float], ys: Sequence[float]) -> float:
    x = np.asarray(xs, dtype=float)
    y = np.asarray(ys, dtype=float)
    if x.size != y.size or x.size < 2 or np.std(x) == 0 or np.std(y) == 0:
        return float("nan")
    return float(np.corrcoef(x, y)[0, 1])


def pass033_reproduction_error(folds: Sequence[dict], locked033: Mapping, p33, moduli):
    by_modulus, global_metrics = p33.stability_from_functionals(folds, moduli)
    errors = []
    for key in (
        "mean_oriented_coherence",
        "median_oriented_coherence",
        "minimum_oriented_coherence",
        "maximum_oriented_coherence",
        "mean_axis_coherence",
    ):
        errors.append(abs(global_metrics[key] - locked033["global_stability"][key]))
    locked_by_r = {int(row["r"]): row for row in locked033["by_modulus"]}
    for row in by_modulus:
        locked = locked_by_r[int(row["r"])]
        for key in ("oriented_coherence", "axis_coherence", "functional_norm_mean"):
            errors.append(abs(row[key] - locked[key]))
    return float(max(errors, default=0.0)), global_metrics


def build_result(
    pass028_path: Path,
    pass032_path: Path,
    pass033_path: Path,
    permutation_iterations: int = PERMUTATION_ITERATIONS,
) -> dict:
    locked033 = load_locked_json(pass033_path, EXPECTED_PASS033_SHA256, "PASS033")
    p33 = load_pass033_module()
    folds, centered, locked032, p32, p29 = reconstruct_functionals(
        pass028_path, pass032_path, p33
    )
    reproduction_error, reproduced_global = pass033_reproduction_error(
        folds, locked033, p33, p29.PRIMARY_MODULI
    )
    if reproduction_error > 1e-12:
        raise AssertionError(f"PASS033 reproduction error: {reproduction_error}")
    scored = score_functionals(folds, p29.PRIMARY_MODULI)
    raw_coefficients = p32.raw_cancellation_coefficients(centered, p29)
    permutation = restricted_permutation_null(
        folds,
        raw_coefficients,
        p29.EXPS,
        p29.PRIMARY_MODULI,
        p32,
        scored["global"],
        iterations=permutation_iterations,
        seed=PERMUTATION_SEED,
    )
    decision = decision_summary(scored, permutation)
    pass032_skill_by_modulus = {
        int(row["r"]): float(row["predicted"]["scalar_skill"])
        for row in locked032["decision"]["by_modulus"]
    }
    return {
        "pass": "PASS034",
        "title": "Held-out rank-two subspace containment of cancellation functionals",
        "classification": "finite leave-one-functional-out subspace-containment diagnostic",
        "interpretation_guard": (
            "The five functionals per modulus share overlapping training windows. "
            "The restricted null preserves that overlap; rank-two containment is not "
            "signed prediction of the cancellation coefficient."
        ),
        "claim_ceiling": "No asymptotic proof and no direct progress toward a proof of Goldbach.",
        "configuration": {
            "exps": list(p29.EXPS),
            "moduli": list(p29.PRIMARY_MODULI),
            "locked_subspace_rank": 2,
            "permutation_iterations": permutation_iterations,
            "permutation_seed": PERMUTATION_SEED,
            "input_sha256": {
                pass028_path.name: sha256_file(pass028_path),
                pass032_path.name: sha256_file(pass032_path),
                pass033_path.name: sha256_file(pass033_path),
            },
        },
        "subspace_containment": scored,
        "restricted_permutation_null": permutation,
        "decision": decision,
        "secondary": {
            "pass033_reproduced_global_stability": reproduced_global,
            "correlation_modulus_rank2_score_with_pass032_scalar_skill": correlation(
                [row["mean_rank2_projection_score"] for row in scored["by_modulus"]],
                [pass032_skill_by_modulus[int(row["r"])] for row in scored["by_modulus"]],
            ),
            "pass032_scalar_skill_by_modulus": pass032_skill_by_modulus,
        },
        "safety": {
            "fold_count": len(folds),
            "maximum_pass033_reproduction_error": reproduction_error,
            "maximum_unit_norm_error": float(
                max(abs(np.linalg.norm(fold["_unit"]) - 1.0) for fold in folds)
            ),
            "maximum_sum_perpendicular_error": float(
                max(fold["sum_perpendicular_error"] for fold in folds)
            ),
            "minimum_training_numerical_rank": int(
                min(
                    row["training_numerical_rank"]
                    for row in scored["folds"]
                )
            ),
            "all_rank2_scores_dominate_rank1": all(
                row["rank2_projection_score"] + 1e-12
                >= row["rank1_projection_score"]
                for row in scored["folds"]
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
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_result(
        args.pass028,
        args.pass032,
        args.pass033,
        permutation_iterations=args.permutation_iterations,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    global_metrics = result["subspace_containment"]["global"]
    print(f"PASS034 result: {args.output}")
    print(
        "rank1=",
        f'{global_metrics["mean_rank1_projection_score"]:.6f}',
        "rank2=",
        f'{global_metrics["mean_rank2_projection_score"]:.6f}',
        "gain=",
        f'{global_metrics["mean_rank2_gain_over_rank1"]:.6f}',
        "p=",
        f'{result["restricted_permutation_null"]["rank2_projection_primary"]["one_sided_p_value"]:.6f}',
    )
    print("decision:", result["decision"]["decision"])


if __name__ == "__main__":
    main()
