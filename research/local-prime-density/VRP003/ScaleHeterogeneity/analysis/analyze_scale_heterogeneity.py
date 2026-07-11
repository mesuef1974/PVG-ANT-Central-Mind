from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
LOCAL_PRIME_ROOT = ROOT.parents[1]
DATASET003 = LOCAL_PRIME_ROOT / "VRP002" / "Dataset003" / "data"
SOURCE_DATA = DATASET003 / "pvg_lpd_dataset_003.csv"
PREDICTIONS = DATASET003 / "python_predictions_003.csv"
COEFFICIENTS = DATASET003 / "python_frozen_coefficients_003.csv"
OUTPUT_DIR = ROOT / "data"
GAIN_TABLE = OUTPUT_DIR / "scale_gain_decomposition.csv"
GROUP_TABLE = OUTPUT_DIR / "scale_group_alignment.csv"
ADJACENT_TABLE = OUTPUT_DIR / "adjacent_lambda_covariance.csv"
CERTIFICATE = ROOT / "certificates" / "SCALE_HETEROGENEITY_CERTIFICATE.json"
TOLERANCE = 1e-12


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def family_masks(data: pd.DataFrame) -> list[tuple[str, np.ndarray]]:
    result = [("overall", np.ones(len(data), dtype=bool))]
    for family in ["x^0.5", "x^0.666667", "x^0.75"]:
        mask = data["family"].to_numpy() == family
        require(int(mask.sum()) == 160, f"Unexpected row count for {family}")
        result.append((family, mask))
    return result


def group_contribution(
    data: pd.DataFrame,
    coefficient_table: pd.DataFrame,
    features: list[str],
) -> np.ndarray:
    contribution = np.zeros(len(data), dtype=np.float64)
    indexed = coefficient_table.set_index("feature")
    for feature in features:
        require(feature in indexed.index, f"Missing coefficient for {feature}")
        row = indexed.loc[feature]
        standardized = (
            data[feature].to_numpy(dtype=float) - float(row["training_mean"])
        ) / float(row["training_scale"])
        contribution += float(row["ridge_coefficient"]) * standardized
    return contribution


def main() -> None:
    for path in [SOURCE_DATA, PREDICTIONS, COEFFICIENTS]:
        require(path.exists(), f"Missing Dataset 003 generated input: {path}")

    data = pd.read_csv(SOURCE_DATA)
    predictions = pd.read_csv(PREDICTIONS)
    coefficients = pd.read_csv(COEFFICIENTS)
    require(len(data) == len(predictions) == 480, "Unexpected Dataset 003 row count")
    require(data["window_id"].tolist() == predictions["window_id"].tolist(), "Data/prediction order mismatch")

    y = predictions["li_std_residual"].to_numpy(dtype=float)
    classical = predictions["pred_classical"].to_numpy(dtype=float)
    primary = predictions["pred_primary"].to_numpy(dtype=float)
    classical_error = y - classical
    correction = primary - classical
    primary_error = y - primary

    gain_rows: list[dict[str, object]] = []
    for family, mask in family_masks(data):
        e = classical_error[mask]
        d = correction[mask]
        ep = primary_error[mask]
        mse_classical = float(np.mean(e**2))
        mse_primary = float(np.mean(ep**2))
        gain = mse_classical - mse_primary
        alignment = float(2 * np.mean(e * d))
        energy = float(np.mean(d**2))
        identity_error = abs(gain - (alignment - energy))
        require(identity_error <= TOLERANCE, f"Gain identity failed for {family}: {identity_error}")

        covariance_term = float(2 * np.cov(e, d, ddof=0)[0, 1])
        mean_term = float(2 * np.mean(e) * np.mean(d))
        require(abs(alignment - covariance_term - mean_term) <= TOLERANCE, f"Bias-covariance split failed for {family}")

        gain_rows.append(
            {
                "family": family,
                "n": int(mask.sum()),
                "mse_classical": mse_classical,
                "mse_primary": mse_primary,
                "mse_gain": gain,
                "alignment_2E_error_correction": alignment,
                "correction_energy_E_correction_sq": energy,
                "alignment_to_energy_ratio": alignment / energy,
                "two_covariance": covariance_term,
                "two_mean_product": mean_term,
                "correction_variance": float(np.var(d, ddof=0)),
                "correction_mean_square": float(np.mean(d) ** 2),
                "correlation_error_correction": float(np.corrcoef(e, d)[0, 1]),
                "identity_abs_error": identity_error,
            }
        )

    primary_coefficients = coefficients[
        coefficients["model"] == "Primary Lambda + characters + residue energy"
    ].copy()
    classical_coefficients = coefficients[
        coefficients["model"] == "Classical Ridge"
    ].copy()
    require(len(primary_coefficients) == 66, "Primary coefficient count changed")
    require(len(classical_coefficients) == 3, "Classical coefficient count changed")

    classical_features = ["log_x", "log_h", "theta_empirical"]
    lambda_features = [
        feature
        for feature in primary_coefficients["feature"]
        if feature.startswith("pre_lambda_density")
        or feature.startswith("pre_lambda_residual_per_sqrt")
    ]
    character_features = [
        feature
        for feature in primary_coefficients["feature"]
        if feature.startswith("pre_chi") or feature.startswith("pre_character_energy")
    ]
    residue_features = [
        feature
        for feature in primary_coefficients["feature"]
        if feature.startswith("pre_residue_energy") or feature.startswith("pre_residue_max")
    ]
    require((len(lambda_features), len(character_features), len(residue_features)) == (6, 21, 36), "Feature groups changed")

    primary_index = primary_coefficients.set_index("feature")
    classical_index = classical_coefficients.set_index("feature")
    classical_shift = np.zeros(len(data), dtype=np.float64)
    for feature in classical_features:
        primary_row = primary_index.loc[feature]
        classical_row = classical_index.loc[feature]
        require(abs(float(primary_row["training_mean"]) - float(classical_row["training_mean"])) <= TOLERANCE, "Classical training means differ")
        require(abs(float(primary_row["training_scale"]) - float(classical_row["training_scale"])) <= TOLERANCE, "Classical training scales differ")
        standardized = (
            data[feature].to_numpy(dtype=float) - float(primary_row["training_mean"])
        ) / float(primary_row["training_scale"])
        classical_shift += (
            float(primary_row["ridge_coefficient"])
            - float(classical_row["ridge_coefficient"])
        ) * standardized

    group_values = {
        "classical_shift": classical_shift,
        "lagged_lambda": group_contribution(data, primary_coefficients, lambda_features),
        "characters": group_contribution(data, primary_coefficients, character_features),
        "residue_energy": group_contribution(data, primary_coefficients, residue_features),
    }
    reconstructed = sum(group_values.values())
    reconstruction_error = float(np.max(np.abs(reconstructed - correction)))
    require(reconstruction_error <= 1e-10, f"Correction reconstruction failed: {reconstruction_error}")

    group_rows: list[dict[str, object]] = []
    for family, mask in family_masks(data):
        e = classical_error[mask]
        for group, values in group_values.items():
            value = values[mask]
            group_rows.append(
                {
                    "family": family,
                    "group": group,
                    "n": int(mask.sum()),
                    "mean_correction": float(np.mean(value)),
                    "sd_correction": float(np.std(value, ddof=0)),
                    "alignment_2E_error_group": float(2 * np.mean(e * value)),
                    "correlation_error_group": float(np.corrcoef(e, value)[0, 1]),
                    "self_energy_E_group_sq": float(np.mean(value**2)),
                }
            )

    past_lambda_residual = (
        data["pre_lambda_residual_per_sqrt_m1"].to_numpy(dtype=float)
        * np.sqrt(data["h"].to_numpy(dtype=float))
    )
    future_lambda_residual = data["lambda_residual"].to_numpy(dtype=float)
    adjacent_identity_error = float(
        np.max(
            np.abs(
                2 * past_lambda_residual * future_lambda_residual
                - (
                    (past_lambda_residual + future_lambda_residual) ** 2
                    - past_lambda_residual**2
                    - future_lambda_residual**2
                )
            )
        )
    )
    require(adjacent_identity_error <= TOLERANCE, "Adjacent-increment square identity failed")

    adjacent_rows: list[dict[str, object]] = []
    h_values = data["h"].to_numpy(dtype=float)
    log_x_values = np.log(data["start"].to_numpy(dtype=float))
    for family, mask in family_masks(data):
        past = past_lambda_residual[mask]
        future = future_lambda_residual[mask]
        normalized_product = past * future / (h_values[mask] * log_x_values[mask])
        adjacent_rows.append(
            {
                "family": family,
                "n": int(mask.sum()),
                "past_mean": float(np.mean(past)),
                "future_mean": float(np.mean(future)),
                "covariance_past_future": float(np.cov(past, future, ddof=0)[0, 1]),
                "correlation_past_future": float(np.corrcoef(past, future)[0, 1]),
                "mean_raw_product": float(np.mean(past * future)),
                "mean_product_over_h_log_x": float(np.mean(normalized_product)),
                "median_product_over_h_log_x": float(np.median(normalized_product)),
                "pointwise_identity_max_error": adjacent_identity_error,
            }
        )

    gain_table = pd.DataFrame(gain_rows)
    group_table = pd.DataFrame(group_rows)
    adjacent_table = pd.DataFrame(adjacent_rows)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    gain_table.to_csv(GAIN_TABLE, index=False)
    group_table.to_csv(GROUP_TABLE, index=False)
    adjacent_table.to_csv(ADJACENT_TABLE, index=False)

    family_gain = {
        row["family"]: row["mse_gain"]
        for row in gain_rows
        if row["family"] != "overall"
    }
    adjacent_covariance = {
        row["family"]: row["covariance_past_future"]
        for row in adjacent_rows
        if row["family"] != "overall"
    }
    certificate = {
        "certificate_id": "CERT-PVG-LPD-SCALE-HETEROGENEITY-001",
        "status": "SCALE_HETEROGENEITY_DIAGNOSTIC_PASS",
        "dataset003_parent_commit": "a0f93f46b01ba4743c2348e5ddbadf4522aed29a",
        "exact_identities": {
            "correction_gain": "E[e_c^2]-E[(e_c-d)^2]=2E[e_c d]-E[d^2]",
            "bias_covariance": "2E[e_c d]=2Cov(e_c,d)+2E[e_c]E[d]",
            "adjacent_increment": "2AB=(A+B)^2-A^2-B^2",
            "maximum_gain_identity_error": float(gain_table["identity_abs_error"].max()),
            "maximum_adjacent_identity_error": adjacent_identity_error,
            "maximum_correction_reconstruction_error": reconstruction_error,
        },
        "family_mse_gain": family_gain,
        "family_adjacent_lambda_covariance": adjacent_covariance,
        "observed_pattern": {
            "shortest_family_gain_negative": family_gain["x^0.5"] < 0,
            "longer_family_gains_positive": family_gain["x^0.666667"] > 0 and family_gain["x^0.75"] > 0,
            "adjacent_lambda_covariance_negative_all_families": all(
                value < 0 for value in adjacent_covariance.values()
            ),
            "interpretation": "The fitted correction exploits anti-persistence rather than positive persistence; at x^0.5 correction energy exceeds alignment.",
        },
        "classification": [
            "Exact algebraic diagnostic",
            "Empirical scale heterogeneity",
            "Adjacent Lambda anti-correlation observed",
            "Mechanism not proved",
            "No theorem about primes",
            "No RH/GRH progress",
        ],
        "next_proof_objects": [
            "Finite correction-gain identity",
            "Adjacent von Mangoldt increment square identity",
            "Shifted Selberg-integral covariance identity",
            "Conditional variance-to-anticorrelation transfer",
        ],
    }
    CERTIFICATE.parent.mkdir(parents=True, exist_ok=True)
    CERTIFICATE.write_text(json.dumps(certificate, indent=2, ensure_ascii=False), encoding="utf-8")

    print(gain_table.to_string(index=False))
    print(group_table.to_string(index=False))
    print(adjacent_table.to_string(index=False))
    print(json.dumps(certificate, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
