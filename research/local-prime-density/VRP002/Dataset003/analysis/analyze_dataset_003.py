from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parent.parent
PROTOCOL_PATH = ROOT / "protocol.json"
TEST_DATA = ROOT / "data" / "pvg_lpd_dataset_003.csv"
TRAIN_DATA = (
    ROOT.parent.parent
    / "VRP001"
    / "Dataset002"
    / "data"
    / "pvg_lpd_dataset_002.csv"
)
OUTPUT_DIR = ROOT / "data"
RESULT_JSON = OUTPUT_DIR / "python_result_003.json"
MODEL_TABLE = OUTPUT_DIR / "python_model_results_003.csv"
FAMILY_TABLE = OUTPUT_DIR / "python_family_results_003.csv"
PREDICTIONS = OUTPUT_DIR / "python_predictions_003.csv"
COEFFICIENTS = OUTPUT_DIR / "python_frozen_coefficients_003.csv"
RESIDUE_SUMMARY = OUTPUT_DIR / "python_residue_secondary_003.csv"

PARK_MILLER_MODULUS = 2_147_483_647
PARK_MILLER_MULTIPLIER = 16_807
TARGET = "li_std_residual"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def metric_row(y: np.ndarray, prediction: np.ndarray) -> dict[str, float]:
    require(len(y) == len(prediction), "Metric vectors have different lengths")
    require(np.isfinite(y).all() and np.isfinite(prediction).all(), "Non-finite metric values")
    return {
        "rmse": float(mean_squared_error(y, prediction) ** 0.5),
        "mae": float(mean_absolute_error(y, prediction)),
        "r2": float(r2_score(y, prediction)),
    }


def fit_frozen(train: pd.DataFrame, features: list[str], alpha: float):
    require(features, "Frozen feature list is empty")
    missing = [feature for feature in features if feature not in train.columns]
    require(not missing, f"Training data is missing features: {missing}")
    model = make_pipeline(StandardScaler(), Ridge(alpha=alpha))
    model.fit(train[features], train[TARGET])
    return model


def park_miller_bootstrap(
    y: np.ndarray,
    classical: np.ndarray,
    candidate: np.ndarray,
    families: np.ndarray,
    ordered_families: list[str],
    replicates: int,
    seed: int,
) -> np.ndarray:
    family_indices = [np.flatnonzero(families == family) for family in ordered_families]
    require(all(len(indices) == 160 for indices in family_indices), "Unexpected family bootstrap size")
    state = seed
    delta = np.empty(replicates, dtype=np.float64)
    for replicate in range(replicates):
        sampled_parts: list[np.ndarray] = []
        for indices in family_indices:
            draws = np.empty(len(indices), dtype=np.int64)
            for position in range(len(indices)):
                state = (PARK_MILLER_MULTIPLIER * state) % PARK_MILLER_MODULUS
                draws[position] = indices[state % len(indices)]
            sampled_parts.append(draws)
        sample = np.concatenate(sampled_parts)
        rmse_classical = math.sqrt(float(np.mean((y[sample] - classical[sample]) ** 2)))
        rmse_candidate = math.sqrt(float(np.mean((y[sample] - candidate[sample]) ** 2)))
        delta[replicate] = rmse_classical - rmse_candidate
    return delta


def coefficient_rows(name: str, features: list[str], model) -> list[dict[str, object]]:
    scaler: StandardScaler = model.named_steps["standardscaler"]
    ridge: Ridge = model.named_steps["ridge"]
    rows: list[dict[str, object]] = []
    for index, feature in enumerate(features):
        rows.append(
            {
                "model": name,
                "feature": feature,
                "training_mean": float(scaler.mean_[index]),
                "training_scale": float(scaler.scale_[index]),
                "ridge_coefficient": float(ridge.coef_[index]),
                "ridge_intercept": float(ridge.intercept_),
                "alpha": float(ridge.alpha),
            }
        )
    return rows


def main() -> None:
    require(PROTOCOL_PATH.exists(), "Frozen protocol is missing")
    require(TRAIN_DATA.exists(), "Dataset 002 is missing; build VRP001 Dataset 002 first")
    require(TEST_DATA.exists(), "Dataset 003 is missing; run build_dataset_003.py")

    protocol = json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))
    source = pd.read_csv(TRAIN_DATA)
    test = pd.read_csv(TEST_DATA)

    training = source[
        (source["role"] == "research")
        & (source["analysis_split"].isin(["train", "validation"]))
    ].copy()
    require(len(training) == 535, f"Expected 535 frozen training rows, found {len(training)}")
    require(len(test) == 480, f"Expected 480 independent rows, found {len(test)}")

    classical = ["log_x", "log_h", "theta_empirical"]
    lagged_lambda = [
        column
        for column in source.columns
        if column.startswith("pre_lambda_density")
        or column.startswith("pre_lambda_residual_per_sqrt")
    ]
    characters = [
        column
        for column in source.columns
        if column.startswith("pre_chi") or column.startswith("pre_character_energy")
    ]
    residue = [
        column
        for column in source.columns
        if column.startswith("pre_residue_energy") or column.startswith("pre_residue_max")
    ]
    require((len(classical), len(lagged_lambda), len(characters), len(residue)) == (3, 6, 21, 36), "Frozen feature schema changed")

    candidate = classical + lagged_lambda + characters + residue
    secondary = classical + lagged_lambda
    require(len(candidate) == 66, "Primary candidate feature count changed")
    require(all(feature in test.columns for feature in candidate), "Dataset 003 lacks frozen features")

    model_spec = protocol["models"]
    classical_alpha = float(model_spec["classical"]["alpha"])
    candidate_alpha = float(model_spec["primary_candidate"]["alpha"])
    secondary_alpha = float(model_spec["secondary_descriptive"]["alpha"])
    require((classical_alpha, candidate_alpha, secondary_alpha) == (300.0, 3000.0, 1000.0), "Frozen alphas changed")

    models = {
        "Classical Ridge": (classical, fit_frozen(training, classical, classical_alpha)),
        "Primary Lambda + characters + residue energy": (
            candidate,
            fit_frozen(training, candidate, candidate_alpha),
        ),
        "Secondary lagged Lambda": (
            secondary,
            fit_frozen(training, secondary, secondary_alpha),
        ),
    }

    y = test[TARGET].to_numpy(dtype=float)
    predictions: dict[str, np.ndarray] = {}
    model_rows: list[dict[str, object]] = []
    coefficient_table: list[dict[str, object]] = []
    for name, (features, model) in models.items():
        prediction = model.predict(test[features])
        predictions[name] = prediction
        model_rows.append(
            {
                "model": name,
                "feature_count": len(features),
                "alpha": float(model.named_steps["ridge"].alpha),
                **metric_row(y, prediction),
            }
        )
        coefficient_table.extend(coefficient_rows(name, features, model))

    classical_prediction = predictions["Classical Ridge"]
    primary_prediction = predictions["Primary Lambda + characters + residue energy"]
    secondary_prediction = predictions["Secondary lagged Lambda"]
    overall_delta = metric_row(y, classical_prediction)["rmse"] - metric_row(y, primary_prediction)["rmse"]

    ordered_families = [f"x^{theta:.6g}" for theta in protocol["window_design"]["theta_families"]]
    actual_families = test["family"].to_numpy()
    require(set(actual_families) == set(ordered_families), "Unexpected Dataset 003 families")

    family_rows: list[dict[str, object]] = []
    family_delta: dict[str, float] = {}
    for family in ordered_families:
        mask = actual_families == family
        family_y = y[mask]
        classical_metrics = metric_row(family_y, classical_prediction[mask])
        primary_metrics = metric_row(family_y, primary_prediction[mask])
        secondary_metrics = metric_row(family_y, secondary_prediction[mask])
        delta = classical_metrics["rmse"] - primary_metrics["rmse"]
        family_delta[family] = delta
        family_rows.append(
            {
                "family": family,
                "n": int(mask.sum()),
                "classical_rmse": classical_metrics["rmse"],
                "primary_rmse": primary_metrics["rmse"],
                "secondary_rmse": secondary_metrics["rmse"],
                "primary_delta": delta,
            }
        )

    bootstrap_spec = protocol["bootstrap"]
    delta = park_miller_bootstrap(
        y=y,
        classical=classical_prediction,
        candidate=primary_prediction,
        families=actual_families,
        ordered_families=ordered_families,
        replicates=int(bootstrap_spec["replicates"]),
        seed=int(bootstrap_spec["seed"]),
    )
    lower, median, upper = [float(value) for value in np.quantile(delta, [0.025, 0.5, 0.975])]
    probability_better = float(np.mean(delta > 0))

    family_stable = all(value > 0 for value in family_delta.values())
    if overall_delta > 0 and lower > 0 and family_stable:
        decision = "REPLICATED CANDIDATE SIGNAL"
    elif overall_delta > 0 and lower > 0 and not family_stable:
        decision = "HETEROGENEOUS EXPLORATORY REPLICATION — NOT PROMOTED"
    elif upper <= 0:
        decision = "NEGATIVE INDEPENDENT REPLICATION"
    else:
        decision = "UNRESOLVED IN INDEPENDENT REPLICATION"

    prediction_table = test[["window_id", "family", "start", "end", "h", TARGET]].copy()
    prediction_table["pred_classical"] = classical_prediction
    prediction_table["pred_primary"] = primary_prediction
    prediction_table["pred_secondary"] = secondary_prediction
    prediction_table.to_csv(PREDICTIONS, index=False)

    pd.DataFrame(model_rows).to_csv(MODEL_TABLE, index=False)
    pd.DataFrame(family_rows).to_csv(FAMILY_TABLE, index=False)
    pd.DataFrame(coefficient_table).to_csv(COEFFICIENTS, index=False)

    residue_rows: list[dict[str, object]] = []
    for column in sorted(c for c in test.columns if c.startswith("target_psi_std_q")):
        values = test[column].to_numpy(dtype=float)
        pieces = column.removeprefix("target_psi_std_q").split("_a")
        modulus = int(pieces[0])
        residue_class = int(pieces[1])
        residue_rows.append(
            {
                "target": column,
                "modulus": modulus,
                "residue": residue_class,
                "n": len(values),
                "mean": float(np.mean(values)),
                "sd_population": float(np.std(values, ddof=0)),
                "rmse_zero": float(math.sqrt(np.mean(values**2))),
                "min": float(np.min(values)),
                "max": float(np.max(values)),
            }
        )
    pd.DataFrame(residue_rows).to_csv(RESIDUE_SUMMARY, index=False)

    result = {
        "protocol_id": protocol["protocol_id"],
        "implementation": "python",
        "training_rows": len(training),
        "test_rows": len(test),
        "model_results": model_rows,
        "overall_delta": overall_delta,
        "family_delta": family_delta,
        "bootstrap": {
            "replicates": int(bootstrap_spec["replicates"]),
            "seed": int(bootstrap_spec["seed"]),
            "ci_lower": lower,
            "median": median,
            "ci_upper": upper,
            "probability_better": probability_better,
        },
        "family_stable": family_stable,
        "decision": decision,
        "secondary_residue_target_count": len(residue_rows),
        "scientific_ceiling": [
            "No theorem",
            "No RH/GRH progress",
            "Promotion only if the frozen rule passes",
        ],
    }
    RESULT_JSON.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print(pd.DataFrame(model_rows).to_string(index=False))
    print(pd.DataFrame(family_rows).to_string(index=False))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
