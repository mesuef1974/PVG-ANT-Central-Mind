from pathlib import Path

import numpy as np
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "pvg_lpd_dataset_001.csv"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    require(DATA_PATH.exists(), f"Dataset is missing: {DATA_PATH}")
    data = pd.read_csv(DATA_PATH)
    required = {
        "window_id",
        "family",
        "role",
        "analysis_split",
        "start",
        "end",
        "h",
        "prime_count",
        "li_expected",
        "li_std_residual",
        "r_d_2",
        "r_d_210",
    }
    missing = sorted(required.difference(data.columns))
    require(not missing, f"Missing required columns: {missing}")
    require(len(data) == 829, f"Expected 829 rows, found {len(data)}")
    require(data["window_id"].is_unique, "window_id values are not unique")
    require(not data[list(required)].isna().any().any(), "Required columns contain NA")
    require(
        np.isfinite(data[["start", "end", "h", "prime_count", "li_expected", "li_std_residual"]].to_numpy(dtype=float)).all(),
        "Required numeric columns contain non-finite values",
    )
    require((data["h"] == data["end"] - data["start"] + 1).all(), "Window-length identity failed")
    require((data["prime_count"] >= 0).all(), "Negative prime count found")
    require((data["r_d_210"].abs() < 1).all(), "Floor-remainder bound failed for d=210")

    research = data[data["role"] == "research"]
    counts = research["analysis_split"].value_counts().to_dict()
    expected = {"train": 319, "validation": 216, "test": 240}
    require(counts == expected, f"Unexpected split counts: {counts}")

    print("Dataset 001 structural checks: PASS")
    print(f"Rows: {len(data)}")
    print(f"Research split counts: {counts}")


if __name__ == "__main__":
    main()
