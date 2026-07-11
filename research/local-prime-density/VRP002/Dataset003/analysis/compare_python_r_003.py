from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PYTHON_RESULT = DATA / "python_result_003.json"
PYTHON_PREDICTIONS = DATA / "python_predictions_003.csv"
PYTHON_MODELS = DATA / "python_model_results_003.csv"
PYTHON_FAMILIES = DATA / "python_family_results_003.csv"
R_PREDICTIONS = DATA / "r_predictions_003.csv"
R_MODELS = DATA / "r_model_results_003.csv"
R_FAMILIES = DATA / "r_family_results_003.csv"
R_BOOTSTRAP = DATA / "r_bootstrap_003.csv"
CERTIFICATE = ROOT / "certificates" / "DATASET003_CROSS_LANGUAGE_CERTIFICATE.json"
TOLERANCE = 1e-7


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def maximum_difference(left: np.ndarray, right: np.ndarray) -> float:
    require(left.shape == right.shape, f"Shape mismatch: {left.shape} vs {right.shape}")
    require(np.isfinite(left).all() and np.isfinite(right).all(), "Non-finite comparison values")
    return float(np.max(np.abs(left - right))) if left.size else 0.0


def main() -> None:
    required = [
        PYTHON_RESULT,
        PYTHON_PREDICTIONS,
        PYTHON_MODELS,
        PYTHON_FAMILIES,
        R_PREDICTIONS,
        R_MODELS,
        R_FAMILIES,
        R_BOOTSTRAP,
    ]
    missing = [str(path) for path in required if not path.exists()]
    require(not missing, f"Missing cross-language inputs: {missing}")

    python_result = json.loads(PYTHON_RESULT.read_text(encoding="utf-8"))
    python_predictions = pd.read_csv(PYTHON_PREDICTIONS)
    r_predictions = pd.read_csv(R_PREDICTIONS)

    require(
        python_predictions["window_id"].tolist() == r_predictions["window_id"].tolist(),
        "Python/R window order differs",
    )
    require(
        python_predictions["family"].tolist() == r_predictions["family"].tolist(),
        "Python/R family order differs",
    )

    prediction_differences = {}
    for column in ["li_std_residual", "pred_classical", "pred_primary", "pred_secondary"]:
        difference = maximum_difference(
            python_predictions[column].to_numpy(dtype=float),
            r_predictions[column].to_numpy(dtype=float),
        )
        prediction_differences[column] = difference
        require(difference <= TOLERANCE, f"Python/R {column} difference {difference} exceeds {TOLERANCE}")

    python_models = pd.read_csv(PYTHON_MODELS).sort_values("model").reset_index(drop=True)
    r_models = pd.read_csv(R_MODELS).sort_values("model").reset_index(drop=True)
    require(python_models["model"].tolist() == r_models["model"].tolist(), "Model names differ")
    model_differences = {}
    for column in ["rmse", "mae", "r2"]:
        difference = maximum_difference(
            python_models[column].to_numpy(dtype=float),
            r_models[column].to_numpy(dtype=float),
        )
        model_differences[column] = difference
        require(difference <= TOLERANCE, f"Python/R model {column} difference exceeds tolerance")

    python_families = pd.read_csv(PYTHON_FAMILIES).sort_values("family").reset_index(drop=True)
    r_families = pd.read_csv(R_FAMILIES).sort_values("family").reset_index(drop=True)
    require(python_families["family"].tolist() == r_families["family"].tolist(), "Family names differ")
    family_differences = {}
    for column in ["classical_rmse", "primary_rmse", "secondary_rmse", "primary_delta"]:
        difference = maximum_difference(
            python_families[column].to_numpy(dtype=float),
            r_families[column].to_numpy(dtype=float),
        )
        family_differences[column] = difference
        require(difference <= TOLERANCE, f"Python/R family {column} difference exceeds tolerance")

    r_bootstrap = pd.read_csv(R_BOOTSTRAP).iloc[0]
    bootstrap_differences = {
        "overall_delta": abs(float(python_result["overall_delta"]) - float(r_bootstrap["overall_delta"])),
        "ci_lower": abs(float(python_result["bootstrap"]["ci_lower"]) - float(r_bootstrap["bootstrap_ci_lower"])),
        "median": abs(float(python_result["bootstrap"]["median"]) - float(r_bootstrap["bootstrap_median"])),
        "ci_upper": abs(float(python_result["bootstrap"]["ci_upper"]) - float(r_bootstrap["bootstrap_ci_upper"])),
        "probability_better": abs(
            float(python_result["bootstrap"]["probability_better"])
            - float(r_bootstrap["probability_better"])
        ),
    }
    require(max(bootstrap_differences.values()) <= TOLERANCE, f"Bootstrap outputs differ: {bootstrap_differences}")

    r_decision = str(r_bootstrap["decision"])
    require(python_result["decision"] == r_decision, "Python/R scientific decisions differ")
    require(bool(python_result["family_stable"]) == bool(r_bootstrap["family_stable"]), "Python/R family-stability flags differ")

    certificate = {
        "certificate_id": "CERT-PVG-LPD-DATASET003-CROSS-LANGUAGE-001",
        "protocol_id": python_result["protocol_id"],
        "status": "PASS",
        "tolerance": TOLERANCE,
        "rows": len(python_predictions),
        "prediction_max_abs_differences": prediction_differences,
        "model_metric_max_abs_differences": model_differences,
        "family_metric_max_abs_differences": family_differences,
        "bootstrap_abs_differences": bootstrap_differences,
        "decision": python_result["decision"],
        "family_stable": bool(python_result["family_stable"]),
        "scientific_ceiling": [
            "Cross-language agreement is a computational certificate, not a theorem",
            "No RH/GRH progress",
        ],
    }
    CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE.write_text(json.dumps(certificate, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(certificate, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
