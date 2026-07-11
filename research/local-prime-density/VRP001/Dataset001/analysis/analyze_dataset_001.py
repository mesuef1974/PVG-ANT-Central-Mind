from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

DATA = Path(__file__).resolve().parent.parent / "data" / "pvg_lpd_dataset_001.csv"
SEED = 20260711
ALPHAS = [0.01, 0.1, 1, 3, 10, 30, 100, 300, 1000]
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
    vsds = [
        column
        for column in data.columns
        if column.startswith(("r_d_", "vsds_", "sift_residual_", "sift_ratio_"))
    ]
    require(vsds, "No VSDS features found")

    alpha_classical, classical_model = tune(train, validation, classical)
    alpha_full, full_model = tune(train, validation, classical + vsds)
    y = test[TARGET].to_numpy()
    pred_zero = np.zeros(len(test))
    pred_classical = classical_model.predict(test[classical])
    pred_full = full_model.predict(test[classical + vsds])

    result = pd.DataFrame([
        {"model": "Li zero-residual baseline", "selected_alpha": None, **metrics(y, pred_zero)},
        {"model": "Classical Ridge", "selected_alpha": alpha_classical, **metrics(y, pred_classical)},
        {"model": "Classical + VSDS Ridge", "selected_alpha": alpha_full, **metrics(y, pred_full)},
    ])
    print(result.to_string(index=False))

    rng = np.random.default_rng(SEED)
    delta = np.empty(5000)
    for index in range(5000):
        sample = rng.integers(0, len(y), len(y))
        rmse_classical = np.sqrt(np.mean((y[sample] - pred_classical[sample]) ** 2))
        rmse_full = np.sqrt(np.mean((y[sample] - pred_full[sample]) ** 2))
        delta[index] = rmse_classical - rmse_full
    print("bootstrap_ci_95", np.quantile(delta, [0.025, 0.975]))
    print("probability_full_better", float(np.mean(delta > 0)))


if __name__ == "__main__":
    main()
