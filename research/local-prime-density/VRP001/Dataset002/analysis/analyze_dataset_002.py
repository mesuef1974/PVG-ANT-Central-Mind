from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

DATA = Path(__file__).resolve().parent.parent / "data" / "pvg_lpd_dataset_002.csv"
SEED = 20260711
ALPHAS = [0.01, 0.1, 1, 3, 10, 30, 100, 300, 1000, 3000]
TARGET = "li_std_residual"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def metrics(y: np.ndarray, prediction: np.ndarray) -> dict[str, float]:
    require(len(y) == len(prediction), "Metric vectors have different lengths")
    require(np.isfinite(y).all() and np.isfinite(prediction).all(), "Non-finite metric input")
    return {
        "rmse": float(mean_squared_error(y, prediction) ** 0.5),
        "mae": float(mean_absolute_error(y, prediction)),
        "r2": float(r2_score(y, prediction)),
    }


def tune(train: pd.DataFrame, validation: pd.DataFrame, features: list[str]):
    require(features, "Feature list is empty")
    best = None
    for alpha in ALPHAS:
        model = make_pipeline(StandardScaler(), Ridge(alpha=alpha))
        model.fit(train[features], train[TARGET])
        score = mean_squared_error(
            validation[TARGET], model.predict(validation[features])
        ) ** 0.5
        if best is None or score < best[0]:
            best = (score, alpha, model)
    require(best is not None, "Ridge tuning failed")
    return best[1], best[2]


def main() -> None:
    require(DATA.exists(), f"Dataset is missing: {DATA}")
    data = pd.read_csv(DATA)
    research = data[data["role"] == "research"]
    train = research[research["analysis_split"] == "train"]
    validation = research[research["analysis_split"] == "validation"]
    test = research[research["analysis_split"] == "test"]
    require((len(train), len(validation), len(test)) == (319, 216, 240), "Unexpected split")

    classical = ["log_x", "log_h", "theta_empirical"]
    lagged_lambda = [
        column
        for column in data.columns
        if column.startswith("pre_lambda_density")
        or column.startswith("pre_lambda_residual_per_sqrt")
    ]
    characters = [
        column
        for column in data.columns
        if column.startswith("pre_chi") or column.startswith("pre_character_energy")
    ]
    residue = [
        column
        for column in data.columns
        if column.startswith("pre_residue_energy") or column.startswith("pre_residue_max")
    ]
    vsds = [
        column
        for column in data.columns
        if column.startswith(("r_d_", "vsds_", "sift_residual_", "sift_ratio_"))
    ]
    for name, features in {
        "lagged_lambda": lagged_lambda,
        "characters": characters,
        "residue": residue,
        "vsds": vsds,
    }.items():
        require(features, f"Empty feature group: {name}")

    feature_sets = {
        "Classical Ridge": classical,
        "Classical + lagged Lambda": classical + lagged_lambda,
        "Classical + Lambda + characters": classical + lagged_lambda + characters,
        "Classical + Lambda + characters + residue energy": classical + lagged_lambda + characters + residue,
        "Full past-only + current VSDS": classical + lagged_lambda + characters + residue + vsds,
    }

    results = {}
    rows = []
    for name, features in feature_sets.items():
        alpha, model = tune(train, validation, features)
        prediction = model.predict(test[features])
        result_metrics = metrics(test[TARGET].to_numpy(), prediction)
        results[name] = {"alpha": alpha, "prediction": prediction, "metrics": result_metrics}
        rows.append({"model": name, "feature_count": len(features), "selected_alpha": alpha, **result_metrics})
    model_table = pd.DataFrame(rows)
    print(model_table.to_string(index=False))

    y = test[TARGET].to_numpy()
    classical_prediction = results["Classical Ridge"]["prediction"]
    classical_rmse = results["Classical Ridge"]["metrics"]["rmse"]
    candidate_names = list(feature_sets.keys())[1:]
    rng = np.random.default_rng(SEED)
    bootstrap_rows = []
    raw_p_values = []
    for name in candidate_names:
        prediction = results[name]["prediction"]
        delta = np.empty(3000)
        for index in range(3000):
            sample = rng.integers(0, len(y), len(y))
            rmse_classical = np.sqrt(np.mean((y[sample] - classical_prediction[sample]) ** 2))
            rmse_candidate = np.sqrt(np.mean((y[sample] - prediction[sample]) ** 2))
            delta[index] = rmse_classical - rmse_candidate
        probability_better = float(np.mean(delta > 0))
        p_one_sided = 1 - probability_better
        raw_p_values.append((name, p_one_sided))
        bootstrap_rows.append({
            "model": name,
            "improvement_vs_classical": classical_rmse - results[name]["metrics"]["rmse"],
            "bootstrap_ci_lower": float(np.quantile(delta, 0.025)),
            "bootstrap_median": float(np.quantile(delta, 0.5)),
            "bootstrap_ci_upper": float(np.quantile(delta, 0.975)),
            "probability_better": probability_better,
            "p_one_sided": p_one_sided,
            "p_bonferroni": min(1.0, p_one_sided * len(candidate_names)),
        })

    ordered = sorted(raw_p_values, key=lambda item: item[1])
    holm = {}
    running = 0.0
    total = len(ordered)
    for rank, (name, p_value) in enumerate(ordered):
        adjusted = min(1.0, p_value * (total - rank))
        running = max(running, adjusted)
        holm[name] = running
    for row in bootstrap_rows:
        row["p_holm"] = holm[row["model"]]
    bootstrap_table = pd.DataFrame(bootstrap_rows)
    print(bootstrap_table.to_string(index=False))

    exploratory = bootstrap_table[
        bootstrap_table["model"] == "Classical + Lambda + characters + residue energy"
    ].iloc[0]
    promoted = (
        exploratory["improvement_vs_classical"] > 0
        and exploratory["bootstrap_ci_lower"] > 0
        and exploratory["probability_better"] >= 0.95
        and exploratory["p_holm"] < 0.05
    )
    print("exploratory_signal_promoted", bool(promoted))


if __name__ == "__main__":
    main()
