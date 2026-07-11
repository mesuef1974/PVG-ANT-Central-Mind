from __future__ import annotations

import json
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
GENERATED_CERTIFICATE = OUTPUT_DIR / "generated_scale_heterogeneity_certificate.json"

ALGEBRA_ATOL = 1e-12
RECONSTRUCTION_ATOL = 1e-10
ADJACENT_ATOL = 1e-12
# The adjacent identity is evaluated as a cancellation-prone difference of
# three squares. 256 eps is a declared scale-aware float64 tolerance.
ADJACENT_RTOL = float(256 * np.finfo(np.float64).eps)


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
        scale = float(row["training_scale"])
        require(scale > 0 and np.isfinite(scale), f"Invalid training scale for {feature}")
        standardized = (
            data[feature].to_numpy(dtype=float) - float(row["training_mean"])
        ) / scale
        contribution += float(row["ridge_coefficient"]) * standardized
    return contribution


def row_dicts_by_family(frame: pd.DataFrame) -> dict[str, dict[str, object]]:
    result: dict[str, dict[str, object]] = {}
    for row in frame.to_dict("records"):
        family = str(row.pop("family"))
        result[family] = {
            key: int(value) if key == "n" else float(value)
            for key, value in row.items()
        }
    return result


def main() -> None:
    for path in [SOURCE_DATA, PREDICTIONS, COEFFICIENTS]:
        require(path.exists(), f"Missing Dataset 003 generated input: {path}")

    data = pd.read_csv(SOURCE_DATA)
    predictions = pd.read_csv(PREDICTIONS)
    coefficients = pd.read_csv(COEFFICIENTS)
    require(len(data) == len(predictions) == 480, "Unexpected Dataset 003 row count")
    require(
        data["window_id"].tolist() == predictions["window_id"].tolist(),
        "Data/prediction order mismatch",
    )

    y = predictions["li_std_residual"].to_numpy(dtype=float)
    classical = predictions["pred_classical"].to_numpy(dtype=float)
    primary = predictions["pred_primary"].to_numpy(dtype=float)
    require(np.isfinite(y).all(), "Non-finite target")
    require(np.isfinite(classical).all() and np.isfinite(primary).all(), "Non-finite prediction")

    classical_error = y - classical
    correction = primary - classical
    primary_error = y - primary

    gain_rows: list[dict[str, object]] = []
    for family, mask in family_masks(data):
        error = classical_error[mask]
        delta = correction[mask]
        rich_error = primary_error[mask]
        mse_classical = float(np.mean(error**2))
        mse_primary = float(np.mean(rich_error**2))
        gain = mse_classical - mse_primary
        alignment = float(2 * np.mean(error * delta))
        energy = float(np.mean(delta**2))
        identity_error = abs(gain - (alignment - energy))
        require(
            identity_error <= ALGEBRA_ATOL,
            f"Gain identity failed for {family}: {identity_error}",
        )
        covariance_term = float(2 * np.cov(error, delta, ddof=0)[0, 1])
        mean_term = float(2 * np.mean(error) * np.mean(delta))
        require(
            abs(alignment - covariance_term - mean_term) <= ALGEBRA_ATOL,
            f"Bias/covariance split failed for {family}",
        )
        gain_rows.append(
            {
                "family": family,
                "n": int(mask.sum()),
                "mse_classical": mse_classical,
                "mse_primary": mse_primary,
                "mse_gain": gain,
                "alignment": alignment,
                "correction_energy": energy,
                "alignment_to_energy_ratio": alignment / energy,
                "two_covariance": covariance_term,
                "two_mean_product": mean_term,
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
        if feature.startswith("pre_chi")
        or feature.startswith("pre_character_energy")
    ]
    residue_features = [
        feature
        for feature in primary_coefficients["feature"]
        if feature.startswith("pre_residue_energy")
        or feature.startswith("pre_residue_max")
    ]
    require(
        (len(lambda_features), len(character_features), len(residue_features))
        == (6, 21, 36),
        "Feature groups changed",
    )

    primary_index = primary_coefficients.set_index("feature")
    classical_index = classical_coefficients.set_index("feature")
    classical_shift = np.zeros(len(data), dtype=np.float64)
    for feature in classical_features:
        primary_row = primary_index.loc[feature]
        classical_row = classical_index.loc[feature]
        require(
            abs(float(primary_row["training_mean"]) - float(classical_row["training_mean"]))
            <= ALGEBRA_ATOL,
            "Classical training means differ",
        )
        require(
            abs(float(primary_row["training_scale"]) - float(classical_row["training_scale"]))
            <= ALGEBRA_ATOL,
            "Classical training scales differ",
        )
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
    reconstructed = np.sum(np.vstack(list(group_values.values())), axis=0)
    reconstruction_error = float(np.max(np.abs(reconstructed - correction)))
    require(
        reconstruction_error <= RECONSTRUCTION_ATOL,
        f"Correction reconstruction failed: {reconstruction_error}",
    )

    group_rows: list[dict[str, object]] = []
    for family, mask in family_masks(data):
        error = classical_error[mask]
        for group, values in group_values.items():
            value = values[mask]
            group_rows.append(
                {
                    "family": family,
                    "group": group,
                    "n": int(mask.sum()),
                    "mean_correction": float(np.mean(value)),
                    "sd_correction": float(np.std(value, ddof=0)),
                    "alignment_2E_error_group": float(2 * np.mean(error * value)),
                    "correlation_error_group": float(np.corrcoef(error, value)[0, 1]),
                    "self_energy_E_group_sq": float(np.mean(value**2)),
                }
            )

    past_lambda_residual = (
        data["pre_lambda_residual_per_sqrt_m1"].to_numpy(dtype=float)
        * np.sqrt(data["h"].to_numpy(dtype=float))
    )
    future_lambda_residual = data["lambda_residual"].to_numpy(dtype=float)
    adjacent_left = 2 * past_lambda_residual * future_lambda_residual
    adjacent_right = (
        (past_lambda_residual + future_lambda_residual) ** 2
        - past_lambda_residual**2
        - future_lambda_residual**2
    )
    adjacent_abs_error = np.abs(adjacent_left - adjacent_right)
    adjacent_scale = np.maximum(
        1.0, np.maximum(np.abs(adjacent_left), np.abs(adjacent_right))
    )
    adjacent_relative_error = adjacent_abs_error / adjacent_scale
    require(
        np.allclose(
            adjacent_left,
            adjacent_right,
            rtol=ADJACENT_RTOL,
            atol=ADJACENT_ATOL,
        ),
        "Adjacent-increment identity failed outside declared float64 tolerance",
    )

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
            }
        )

    gain_table = pd.DataFrame(gain_rows)
    group_table = pd.DataFrame(group_rows)
    adjacent_table = pd.DataFrame(adjacent_rows)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    gain_table.to_csv(GAIN_TABLE, index=False)
    group_table.to_csv(GROUP_TABLE, index=False)
    adjacent_table.to_csv(ADJACENT_TABLE, index=False)

    gain_decomposition = row_dicts_by_family(gain_table)
    lagged_lambda_group: dict[str, object] = {}
    for row in group_table[group_table["group"] == "lagged_lambda"].to_dict("records"):
        family = str(row["family"])
        lagged_lambda_group[family] = {
            "alignment": float(row["alignment_2E_error_group"]),
            "self_energy": float(row["self_energy_E_group_sq"]),
            "error_correlation": float(row["correlation_error_group"]),
            "mean_correction": float(row["mean_correction"]),
            "sd_correction": float(row["sd_correction"]),
        }
    frozen_lambda_coefficients = primary_coefficients[
        primary_coefficients["feature"].isin(lambda_features)
    ]["ridge_coefficient"].to_numpy(dtype=float)
    lagged_lambda_group["all_six_frozen_coefficients_negative"] = bool(
        np.all(frozen_lambda_coefficients < 0)
    )

    adjacent_lambda: dict[str, dict[str, object]] = {}
    for row in adjacent_table.to_dict("records"):
        family = str(row["family"])
        adjacent_lambda[family] = {
            "n": int(row["n"]),
            "covariance": float(row["covariance_past_future"]),
            "correlation": float(row["correlation_past_future"]),
            "mean_raw_product": float(row["mean_raw_product"]),
            "mean_product_over_h_log_x": float(row["mean_product_over_h_log_x"]),
            "median_product_over_h_log_x": float(row["median_product_over_h_log_x"]),
        }

    certificate = {
        "certificate_id": "CERT-PVG-LPD-SCALE-HETEROGENEITY-001",
        "status": "SCALE_HETEROGENEITY_DIAGNOSTIC_PASS",
        "parent_research_commit": "a0f93f46b01ba4743c2348e5ddbadf4522aed29a",
        "source_artifact": {
            "workflow_run_id": 29164273761,
            "artifact_id": 8251699912,
            "artifact_digest": "sha256:9fd56a0b99b198e44ebeaa73fb3bf36b69a5e3d40425e1d7c76cec23a493c889",
        },
        "numeric_tolerances": {
            "finite_gain_identity_atol": ALGEBRA_ATOL,
            "correction_reconstruction_atol": RECONSTRUCTION_ATOL,
            "adjacent_identity_atol": ADJACENT_ATOL,
            "adjacent_identity_rtol": ADJACENT_RTOL,
        },
        "exact_identities": {
            "correction_gain": "E[e_c^2]-E[(e_c-d)^2]=2E[e_c d]-E[d^2]",
            "positive_correction_criterion": "MSE_primary < MSE_classical iff 2E[e_c d] > E[d^2]",
            "bias_covariance": "2E[e_c d]=2Cov(e_c,d)+2E[e_c]E[d]",
            "adjacent_increment": "2AB=(A+B)^2-A^2-B^2",
            "maximum_gain_identity_abs_error": float(gain_table["identity_abs_error"].max()),
            "maximum_adjacent_identity_abs_error": float(adjacent_abs_error.max()),
            "maximum_adjacent_identity_relative_error": float(adjacent_relative_error.max()),
            "maximum_correction_reconstruction_error": reconstruction_error,
        },
        "gain_decomposition": gain_decomposition,
        "lagged_lambda_group": lagged_lambda_group,
        "adjacent_lambda": adjacent_lambda,
        "observed_pattern": {
            "shortest_family_gain_negative": gain_decomposition["x^0.5"]["mse_gain"] < 0,
            "longer_family_gains_positive": gain_decomposition["x^0.666667"]["mse_gain"] > 0
            and gain_decomposition["x^0.75"]["mse_gain"] > 0,
            "adjacent_lambda_covariance_negative_all_families": all(
                adjacent_lambda[family]["covariance"] < 0
                for family in ["x^0.5", "x^0.666667", "x^0.75"]
            ),
            "interpretation": "The frozen correction behaves as an anti-persistence correction. At x^0.5 its alignment is negative and its energy penalty is largest; at longer scales alignment is positive and exceeds correction energy.",
        },
        "analytic_bridge": {
            "exact_statement": "For E_h(x)=psi(x+h)-psi(x)-h, 2E_h(x)E_h(x+h)=E_2h(x)^2-E_h(x)^2-E_h(x+h)^2 pointwise.",
            "conditional_statement": "A sufficiently uniform variance asymptotic at h and 2h, together with common-domain shift and boundary control, would imply an adjacent covariance asymptotic of schematic size -h X log 2.",
            "status": "conditional proof strategy only",
            "missing_certificates": [
                "uniform short-interval variance asymptotic in the required h range",
                "shifted versus unshifted second-moment control",
                "boundary-domain control",
                "bridge from von Mangoldt covariance to the standardized prime-count residual",
            ],
        },
        "pvg_role": {
            "current_contribution": "organizes past-only valuation/residue observables and exposes the alignment-versus-energy criterion",
            "necessity_status": "not established",
            "originality_status": "no original PVG mechanism certified",
        },
        "classification": [
            "Exact known algebraic identities",
            "Computational scale-heterogeneity diagnostic",
            "Observed adjacent von Mangoldt anti-correlation",
            "Conditional Selberg-variance bridge",
            "Mechanism not proved",
            "No theorem about primes",
            "No RH/GRH progress",
        ],
        "closure_decision": "CLOSE SCALE-HETEROGENEITY DIAGNOSTIC — PASS AS DIAGNOSTIC, NOT AS MECHANISM",
        "next_action": "Complete targeted literature and assumption audit for the shifted Selberg covariance identity; do not start Dataset 004 or a new Lean pass.",
    }
    GENERATED_CERTIFICATE.write_text(
        json.dumps(certificate, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print(gain_table.to_string(index=False))
    print(group_table.to_string(index=False))
    print(adjacent_table.to_string(index=False))
    print(json.dumps(certificate, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
