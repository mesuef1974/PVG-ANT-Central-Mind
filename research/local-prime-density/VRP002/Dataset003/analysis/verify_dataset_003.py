from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
PROTOCOL = ROOT / "protocol.json"
DATA = ROOT / "data" / "pvg_lpd_dataset_003.csv"
METADATA = ROOT / "data" / "pvg_lpd_dataset_003_metadata.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def complete_windows(lower: int, upper_exclusive: int, theta: float) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    start = lower
    upper = upper_exclusive - 1
    while True:
        h = max(10, int(round(start**theta)))
        end = start + h - 1
        if end > upper:
            return result
        result.append((start, end, h))
        start = end + 1


def selected_windows(items: list[tuple[int, int, int]], count: int) -> list[tuple[int, int, int]]:
    indices = np.linspace(0, len(items) - 1, count, dtype=int)
    require(len(set(int(index) for index in indices)) == count, "Duplicate selection indices")
    return [items[int(index)] for index in indices]


def main() -> None:
    require(PROTOCOL.exists(), "protocol.json is missing")
    require(DATA.exists(), "Dataset 003 is missing; run build_dataset_003.py")
    require(METADATA.exists(), "Dataset 003 metadata is missing")

    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    metadata = json.loads(METADATA.read_text(encoding="utf-8"))
    data = pd.read_csv(DATA)

    require(protocol["protocol_id"] == metadata["protocol_id"], "Protocol/metadata ID mismatch")
    require(len(data) == 480, f"Expected 480 rows, found {len(data)}")
    require(data["window_id"].is_unique, "Window IDs are not unique")
    require(set(data["role"]) == {"confirmatory"}, "Unexpected role values")
    require(set(data["analysis_split"]) == {"independent_test"}, "Unexpected split values")
    require(data["start"].min() >= 10_000_000, "Dataset starts below frozen range")
    require(data["end"].max() < 100_000_000, "Dataset exceeds frozen range")
    require((data["h"] == data["end"] - data["start"] + 1).all(), "Window lengths are inconsistent")

    frozen_rows: list[tuple[str, int, int, int]] = []
    lower = int(protocol["numerical_range"]["start_inclusive"])
    upper = int(protocol["numerical_range"]["end_exclusive"])
    count = int(protocol["window_design"]["windows_per_family"])
    for theta in [float(value) for value in protocol["window_design"]["theta_families"]]:
        complete = complete_windows(lower, upper, theta)
        selected = selected_windows(complete, count)
        family = f"x^{theta:.6g}"
        frozen_rows.extend((family, start, end, h) for start, end, h in selected)

    actual_rows = list(
        data[["family", "start", "end", "h"]]
        .itertuples(index=False, name=None)
    )
    require(actual_rows == frozen_rows, "Dataset windows do not match the frozen protocol")

    family_counts = data.groupby("family").size().to_dict()
    require(set(family_counts.values()) == {160}, f"Family counts changed: {family_counts}")
    for family, group in data.groupby("family"):
        starts = group["start"].to_numpy()
        ends = group["end"].to_numpy()
        require(np.all(starts[1:] > ends[:-1]), f"Overlapping windows in {family}")

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
    primary_features = classical + lagged_lambda + characters + residue

    require(len(classical) == 3, "Classical feature count changed")
    require(len(lagged_lambda) == 6, f"Expected 6 lagged-Lambda features, found {len(lagged_lambda)}")
    require(len(characters) == 21, f"Expected 21 character features, found {len(characters)}")
    require(len(residue) == 36, f"Expected 36 residue features, found {len(residue)}")
    require(len(primary_features) == 66, f"Expected 66 primary features, found {len(primary_features)}")
    require(not any(column.startswith("target_") for column in primary_features), "Target leakage into primary feature list")
    require(not any(column in {"prime_count", "li_residual", "li_std_residual", "psi_interval"} for column in primary_features), "Response leakage into primary feature list")

    target_std = [column for column in data.columns if column.startswith("target_psi_std_q")]
    target_raw = [
        column
        for column in data.columns
        if column.startswith("target_psi_q") and not column.startswith("target_psi_std_q")
    ]
    require(len(target_std) == 28, f"Expected 28 standardized residue targets, found {len(target_std)}")
    require(len(target_raw) == 28, f"Expected 28 raw residue targets, found {len(target_raw)}")

    context_columns = [f"pre_context_actual_length_m{multiplier}" for multiplier in (1, 2, 4)]
    require((data[context_columns] > 0).all().all(), "Invalid past-context lengths")
    require((data["pre_context_actual_length_m1"] == data["h"]).all(), "m1 context mismatch")
    require((data["pre_context_actual_length_m2"] == 2 * data["h"]).all(), "m2 context mismatch")
    require((data["pre_context_actual_length_m4"] == 4 * data["h"]).all(), "m4 context mismatch")

    numeric = data.select_dtypes(include=[np.number]).to_numpy()
    require(np.isfinite(numeric).all(), "Dataset contains non-finite numeric values")
    require(not data.isna().any().any(), "Dataset contains missing values")
    require(metadata["rows"] == 480, "Metadata row count mismatch")
    require(metadata["selected_per_family"] == 160, "Metadata family count mismatch")

    print("Dataset 003 verification: PASS")
    print("Family counts:", family_counts)
    print("Primary feature count:", len(primary_features))
    print("Residue-class secondary targets:", len(target_std))


if __name__ == "__main__":
    main()
