#!/usr/bin/env python3
"""PASS025: test a preregistered endpoint-character phase on held-out e=19.

Training uses PASS023 windows e=15..18.  The response in e=19 is read only
after all per-modulus phase coefficients have been fitted from training data.
The phase predictor is Re chi_k(2^e), centered within each modulus/window.

This is a finite computational diagnostic, not an asymptotic proof and not
direct progress toward a proof of Goldbach.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Sequence

import numpy as np


TRAIN_EXPS = (15, 16, 17, 18)
HOLDOUT_EXP = 19
ALL_MODULI = (5, 7, 11, 13, 17, 19, 23, 29, 31)
PRIMARY_MODULI = (11, 13, 17, 19, 23, 29, 31)
DEFAULT_SEED = 250719
DEFAULT_GLOBAL_PERMUTATIONS = 100_000
DEFAULT_PER_MODULUS_PERMUTATIONS = 50_000


def default_training_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass023_results.json"
    if archive.exists():
        return archive
    return here.parent / "pass023" / "avrg_pass023_results.json"


def default_holdout_path() -> Path:
    here = Path(__file__).resolve().parent
    archive = here.parent / "results" / "avrg_pass025_holdout_e19.json"
    if archive.exists():
        return archive
    return here / "avrg_pass025_holdout_e19.json"


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_results = here.parent / "results"
    if archive_results.is_dir():
        return archive_results / "avrg_pass025_results.json"
    return here / "avrg_pass025_results.json"


def validate_ratio_row(raw: dict, exp: int) -> dict:
    r, k = int(raw["r"]), int(raw["k"])
    ratio = float(raw["energy_ratio"])
    if r not in ALL_MODULI:
        raise ValueError(f"Unexpected modulus at e={exp}: {r}")
    if k <= 0 or k % 2 or k > r - 1 - k:
        raise ValueError(f"Invalid conjugacy representative: {(exp, r, k)}")
    if not math.isfinite(ratio) or ratio <= 0:
        raise ValueError(f"Invalid ratio: {(exp, r, k, ratio)}")
    return {"exp": exp, "r": r, "k": k, "rho": ratio}


def load_training(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    config = data.get("configuration", {})
    if tuple(config.get("exps", [])) != TRAIN_EXPS:
        raise ValueError("Training windows differ from preregistered e=15..18")
    if tuple(config.get("moduli", [])) != ALL_MODULI:
        raise ValueError("Training moduli differ from the preregistered set")
    windows = data.get("windows", [])
    if tuple(int(window["exp"]) for window in windows) != TRAIN_EXPS:
        raise ValueError("Training window order differs from the protocol")
    rows = [
        validate_ratio_row(raw, int(window["exp"]))
        for window in windows
        for raw in window.get("rows", [])
    ]
    if len(rows) != 136:
        raise ValueError(f"Expected 136 training rows, received {len(rows)}")
    return rows


def load_holdout(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    protocol = data.get("protocol", {})
    if int(protocol.get("holdout_exp", -1)) != HOLDOUT_EXP:
        raise ValueError("Holdout artifact is not e=19")
    if tuple(protocol.get("training_exps", [])) != TRAIN_EXPS:
        raise ValueError("Holdout artifact records the wrong training windows")
    if tuple(protocol.get("moduli", [])) != ALL_MODULI:
        raise ValueError("Holdout artifact records the wrong moduli")
    window = data.get("window", {})
    if int(window.get("exp", -1)) != HOLDOUT_EXP:
        raise ValueError("Holdout window payload is not e=19")
    rows = [validate_ratio_row(raw, HOLDOUT_EXP) for raw in window.get("rows", [])]
    if len(rows) != 34:
        raise ValueError(f"Expected 34 holdout rows, received {len(rows)}")
    return rows


def modes_by_modulus(rows: Sequence[dict]) -> dict[int, list[int]]:
    return {r: sorted({row["k"] for row in rows if row["r"] == r}) for r in ALL_MODULI}


def centered_response(rows: Sequence[dict], exp: int, r: int, modes: Sequence[int]) -> np.ndarray:
    lookup = {(row["exp"], row["r"], row["k"]): row["rho"] for row in rows}
    values = np.array([lookup[(exp, r, k)] for k in modes], dtype=float)
    centered = values - values.mean()
    if abs(float(centered.sum())) > 1e-12:
        raise AssertionError("Response centering failed")
    return centered


def primitive_root(p: int) -> int:
    for candidate in range(2, p):
        if len({pow(candidate, exponent, p) for exponent in range(p - 1)}) == p - 1:
            return candidate
    raise ValueError(f"No primitive root for {p}")


def discrete_log_two(p: int) -> int:
    generator = primitive_root(p)
    value = 1
    for exponent in range(p - 1):
        if value == 2:
            return exponent
        value = value * generator % p
    raise ValueError(f"Could not compute log_g(2) for {p}")


def raw_phase(r: int, k: int, exp: int) -> float:
    exponent = discrete_log_two(r)
    return math.cos(2.0 * math.pi * k * exp * exponent / (r - 1))


def centered_phase(r: int, modes: Sequence[int], exp: int) -> np.ndarray:
    values = np.array([raw_phase(r, k, exp) for k in modes], dtype=float)
    centered = values - values.mean()
    if abs(float(centered.sum())) > 1e-12:
        raise AssertionError("Phase centering failed")
    return centered


def fit_modulus(
    training_rows: Sequence[dict], holdout_rows: Sequence[dict], r: int, modes: Sequence[int]
) -> dict:
    train_y = np.vstack(
        [centered_response(training_rows, exp, r, modes) for exp in TRAIN_EXPS]
    )
    train_x = np.vstack([centered_phase(r, modes, exp) for exp in TRAIN_EXPS])
    denominator = float(np.sum(train_x**2))
    if denominator <= 1e-15:
        raise ValueError(f"Degenerate phase design for r={r}")
    beta = float(np.sum(train_x * train_y) / denominator)
    holdout_y = centered_response(holdout_rows, HOLDOUT_EXP, r, modes)
    holdout_x = centered_phase(r, modes, HOLDOUT_EXP)
    phase_prediction = beta * holdout_x
    static_prediction = train_y.mean(axis=0)
    zero_sse = float(np.sum(holdout_y**2))
    phase_sse = float(np.sum((holdout_y - phase_prediction) ** 2))
    static_sse = float(np.sum((holdout_y - static_prediction) ** 2))
    train_zero_sse = float(np.sum(train_y**2))
    train_phase_sse = float(np.sum((train_y - beta * train_x) ** 2))
    return {
        "r": r,
        "modes": list(modes),
        "discrete_log_two": discrete_log_two(r),
        "beta": beta,
        "training_zero_sse": train_zero_sse,
        "training_phase_sse": train_phase_sse,
        "training_skill": 1.0 - train_phase_sse / train_zero_sse if train_zero_sse else 0.0,
        "holdout_y": holdout_y,
        "holdout_x": holdout_x,
        "phase_prediction": phase_prediction,
        "static_prediction": static_prediction,
        "zero_sse": zero_sse,
        "phase_sse": phase_sse,
        "static_sse": static_sse,
        "phase_skill_vs_zero": 1.0 - phase_sse / zero_sse if zero_sse else 0.0,
        "static_skill_vs_zero": 1.0 - static_sse / zero_sse if zero_sse else 0.0,
    }


def improvement_distribution(
    target: np.ndarray,
    prediction: np.ndarray,
    permutations: int,
    rng: np.random.Generator,
) -> np.ndarray:
    scores = rng.random((permutations, len(target)))
    indices = np.argsort(scores, axis=1)
    permuted = target[indices]
    zero_sse = float(np.sum(target**2))
    phase_sse = np.sum((permuted - prediction[None, :]) ** 2, axis=1)
    return zero_sse - phase_sse


def permutation_pvalue(null_values: np.ndarray, observed: float) -> float:
    return float(
        (1 + np.count_nonzero(null_values >= observed - 1e-15))
        / (len(null_values) + 1)
    )


def holm_adjust(pairs: Sequence[tuple[int, float]]) -> dict[int, float]:
    ordered = sorted(pairs, key=lambda item: item[1])
    count = len(ordered)
    output: dict[int, float] = {}
    running = 0.0
    for index, (label, value) in enumerate(ordered):
        running = max(running, min(1.0, (count - index) * value))
        output[label] = running
    return output


def safe_correlation(left: np.ndarray, right: np.ndarray) -> float:
    denominator = float(np.linalg.norm(left) * np.linalg.norm(right))
    return float(np.dot(left, right) / denominator) if denominator else 0.0


def holdout_modulus_means(rows: Sequence[dict]) -> list[dict]:
    output = []
    for r in ALL_MODULI:
        values = [row["rho"] for row in rows if row["r"] == r]
        output.append(
            {
                "r": r,
                "representative_count": len(values),
                "mean_ratio": float(np.mean(values)),
                "population_sd": float(np.std(values, ddof=0)),
                "absolute_deviation_from_two": abs(float(np.mean(values)) - 2.0),
            }
        )
    return output


def analyze(
    training_rows: Sequence[dict],
    holdout_rows: Sequence[dict],
    global_permutations: int = DEFAULT_GLOBAL_PERMUTATIONS,
    per_modulus_permutations: int = DEFAULT_PER_MODULUS_PERMUTATIONS,
    seed: int = DEFAULT_SEED,
) -> dict:
    if global_permutations < 1:
        raise ValueError("global_permutations must be positive")
    if not 1 <= per_modulus_permutations <= global_permutations:
        raise ValueError("per_modulus_permutations must be in [1, global]")
    training_modes = modes_by_modulus(training_rows)
    holdout_modes = modes_by_modulus(holdout_rows)
    if training_modes != holdout_modes:
        raise ValueError("Character representatives differ between training and holdout")

    fitted = [
        fit_modulus(training_rows, holdout_rows, r, training_modes[r])
        for r in PRIMARY_MODULI
    ]
    rng = np.random.default_rng(seed)
    global_null = np.zeros(global_permutations, dtype=float)
    raw_pvalues: list[tuple[int, float]] = []
    per_modulus: list[dict] = []

    for row in fitted:
        null_values = improvement_distribution(
            row["holdout_y"], row["phase_prediction"], global_permutations, rng
        )
        global_null += null_values
        observed = row["zero_sse"] - row["phase_sse"]
        raw_p = permutation_pvalue(null_values[:per_modulus_permutations], observed)
        raw_pvalues.append((row["r"], raw_p))
        per_modulus.append(
            {
                "r": row["r"],
                "representative_k": row["modes"],
                "discrete_log_two": row["discrete_log_two"],
                "beta": row["beta"],
                "training_skill": row["training_skill"],
                "holdout_zero_sse": row["zero_sse"],
                "holdout_phase_sse": row["phase_sse"],
                "holdout_static_sse": row["static_sse"],
                "phase_skill_vs_zero": row["phase_skill_vs_zero"],
                "static_skill_vs_zero": row["static_skill_vs_zero"],
                "phase_target_correlation": safe_correlation(
                    row["phase_prediction"], row["holdout_y"]
                ),
                "permutation_p_raw": raw_p,
                "rows": [
                    {
                        "k": k,
                        "centered_phase": float(x),
                        "observed_g": float(y),
                        "phase_prediction": float(phase),
                        "static_prediction": float(static),
                    }
                    for k, x, y, phase, static in zip(
                        row["modes"],
                        row["holdout_x"],
                        row["holdout_y"],
                        row["phase_prediction"],
                        row["static_prediction"],
                    )
                ],
            }
        )

    adjusted = holm_adjust(raw_pvalues)
    for row in per_modulus:
        row["permutation_p_holm"] = adjusted[row["r"]]

    zero_sse = sum(row["zero_sse"] for row in fitted)
    phase_sse = sum(row["phase_sse"] for row in fitted)
    static_sse = sum(row["static_sse"] for row in fitted)
    observed_improvement = zero_sse - phase_sse
    global_p = permutation_pvalue(global_null, observed_improvement)
    skill = 1.0 - phase_sse / zero_sse
    static_skill = 1.0 - static_sse / zero_sse
    pooled_target = np.concatenate([row["holdout_y"] for row in fitted])
    pooled_prediction = np.concatenate([row["phase_prediction"] for row in fitted])
    passed = skill > 0.10 and phase_sse < static_sse and global_p <= 0.05

    return {
        "pass": "PASS025",
        "title": "Held-out endpoint-character phase test",
        "classification": "finite held-out computational diagnostic",
        "claim_ceiling": (
            "No asymptotic proof and no direct progress toward a proof of Goldbach."
        ),
        "locked_protocol": {
            "training_exps": list(TRAIN_EXPS),
            "holdout_exp": HOLDOUT_EXP,
            "all_moduli": list(ALL_MODULI),
            "primary_moduli": list(PRIMARY_MODULI),
            "predictor": "centered Re chi_k(2^e)",
            "seed": seed,
            "global_permutations": global_permutations,
            "per_modulus_permutations": per_modulus_permutations,
            "decision_rule": {
                "phase_skill_strictly_greater_than": 0.10,
                "phase_sse_less_than_static_sse": True,
                "global_permutation_p_at_most": 0.05,
            },
        },
        "holdout_modulus_summary": holdout_modulus_means(holdout_rows),
        "phase_test": {
            "global": {
                "zero_sse": zero_sse,
                "phase_sse": phase_sse,
                "static_sse": static_sse,
                "phase_skill_vs_zero": skill,
                "static_skill_vs_zero": static_skill,
                "phase_improvement_over_zero": observed_improvement,
                "phase_improvement_over_static": static_sse - phase_sse,
                "phase_target_correlation": safe_correlation(
                    pooled_prediction, pooled_target
                ),
                "permutation_p": global_p,
                "decision_passed": passed,
                "decision": (
                    "finite_heldout_support_for_endpoint_character_phase"
                    if passed
                    else "endpoint_character_phase_not_supported_on_holdout"
                ),
            },
            "per_modulus": per_modulus,
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--training", type=Path, default=default_training_path())
    parser.add_argument("--holdout", type=Path, default=default_holdout_path())
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
    training = load_training(args.training)
    holdout = load_holdout(args.holdout)
    result = analyze(
        training,
        holdout,
        global_permutations=args.global_permutations,
        per_modulus_permutations=args.per_modulus_permutations,
        seed=args.seed,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    global_result = result["phase_test"]["global"]
    print(f"PASS025 complete: {args.output}")
    print(
        f"phase_skill={global_result['phase_skill_vs_zero']:.6f} "
        f"static_skill={global_result['static_skill_vs_zero']:.6f} "
        f"permutation_p={global_result['permutation_p']:.6g}"
    )
    print(f"decision={global_result['decision']}")


if __name__ == "__main__":
    main()
