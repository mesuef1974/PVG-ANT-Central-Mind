from pathlib import Path

import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "pvg_lpd_dataset_002.csv"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    require(DATA_PATH.exists(), f"Dataset is missing: {DATA_PATH}")
    data = pd.read_csv(DATA_PATH)

    required_columns = {
        "window_id",
        "role",
        "analysis_split",
        "start",
        "end",
        "h",
        "li_std_residual",
        "pre_context_actual_length_m1",
        "pre_context_actual_length_m2",
        "pre_context_actual_length_m4",
    }
    missing = sorted(required_columns.difference(data.columns))
    require(not missing, f"Missing required columns: {missing}")

    require(len(data) == 829, f"Expected 829 rows, found {len(data)}")
    require(data["window_id"].is_unique, "window_id values are not unique")
    require(not data[list(required_columns)].isna().any().any(), "Required columns contain NA")

    numeric_columns = [
        "start",
        "end",
        "h",
        "li_std_residual",
        "pre_context_actual_length_m1",
        "pre_context_actual_length_m2",
        "pre_context_actual_length_m4",
    ]
    require(
        np.isfinite(data[numeric_columns].to_numpy(dtype=float)).all(),
        "Required numeric columns contain non-finite values",
    )

    for multiplier in (1, 2, 4):
        column = f"pre_context_actual_length_m{multiplier}"
        require((data[column] > 0).all(), f"Non-positive values in {column}")

    require(
        (data["h"] == data["end"] - data["start"] + 1).all(),
        "Window-length identity failed",
    )

    research = data[data["role"] == "research"]
    split_counts = research["analysis_split"].value_counts().to_dict()
    expected_counts = {"train": 319, "validation": 216, "test": 240}
    require(split_counts == expected_counts, f"Unexpected split counts: {split_counts}")

    past_feature_groups = {
        "lagged_lambda": [
            column
            for column in data.columns
            if column.startswith("pre_lambda_density")
            or column.startswith("pre_lambda_residual_per_sqrt")
        ],
        "characters": [
            column
            for column in data.columns
            if column.startswith("pre_chi")
            or column.startswith("pre_character_energy")
        ],
        "residue_energy": [
            column
            for column in data.columns
            if column.startswith("pre_residue_energy")
            or column.startswith("pre_residue_max")
        ],
    }
    empty_groups = [name for name, columns in past_feature_groups.items() if not columns]
    require(not empty_groups, f"Empty feature groups: {empty_groups}")

    print("Dataset 002 structural checks: PASS")
    print(f"Rows: {len(data)}")
    print(f"Research split counts: {split_counts}")
    print(
        "Feature groups:",
        {name: len(columns) for name, columns in past_feature_groups.items()},
    )


if __name__ == "__main__":
    main()
