from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROTOCOL_PATH = ROOT / "protocol.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def complete_window_count(lower: int, upper_exclusive: int, theta: float) -> int:
    count = 0
    start = lower
    upper = upper_exclusive - 1
    while True:
        h = max(10, int(round(start**theta)))
        end = start + h - 1
        if end > upper:
            return count
        count += 1
        start = end + 1


def main() -> None:
    require(PROTOCOL_PATH.exists(), "protocol.json is missing")
    protocol = json.loads(PROTOCOL_PATH.read_text(encoding="utf-8"))

    require(protocol["protocol_id"] == "PVG-LPD-DATASET-003-PROTOCOL-001", "Unexpected protocol ID")
    require(protocol["status"] == "FROZEN_BEFORE_DATA", "Protocol is not frozen")
    require(protocol["data_generation_allowed_before_protocol_merge"] is False, "Pre-merge data generation is not blocked")

    lower = int(protocol["numerical_range"]["start_inclusive"])
    upper = int(protocol["numerical_range"]["end_exclusive"])
    require((lower, upper) == (10_000_000, 100_000_000), "Unexpected numerical range")

    design = protocol["window_design"]
    theta_families = [float(value) for value in design["theta_families"]]
    windows_per_family = int(design["windows_per_family"])
    expected_total = int(design["expected_total_windows"])

    require(theta_families == [0.5, 2 / 3, 0.75], "Unexpected theta families")
    require(windows_per_family == 160, "Unexpected windows-per-family freeze")
    require(expected_total == 480, "Unexpected total sample size")

    counts = {
        str(theta): complete_window_count(lower, upper, theta)
        for theta in theta_families
    }
    require(all(count >= windows_per_family for count in counts.values()), f"Insufficient windows: {counts}")
    require(min(counts.values()) == 175, f"Unexpected limiting complete-list size: {counts}")

    models = protocol["models"]
    require(float(models["classical"]["alpha"]) == 300.0, "Classical alpha changed")
    require(float(models["primary_candidate"]["alpha"]) == 3000.0, "Primary alpha changed")
    require(float(models["secondary_descriptive"]["alpha"]) == 1000.0, "Secondary alpha changed")
    require(models["primary_candidate"]["current_window_vsds_included"] is False, "Current-window VSDS leaked into primary model")

    bootstrap = protocol["bootstrap"]
    require(int(bootstrap["replicates"]) == 10_000, "Bootstrap replicate count changed")
    require(int(bootstrap["seed"]) == 20_260_712, "Bootstrap seed changed")
    require(int(bootstrap["resample_count_per_family"]) == 160, "Bootstrap stratum size changed")

    forbidden_extensions = {".csv", ".parquet", ".feather", ".xlsx", ".zip"}
    generated_files = [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and path.suffix.lower() in forbidden_extensions
    ]
    require(not generated_files, f"Pre-freeze generated artifacts are forbidden: {generated_files}")

    print("Dataset 003 protocol validation: PASS")
    print("Complete non-overlapping window counts:", counts)
    print("Frozen selected windows:", windows_per_family, "per family;", expected_total, "total")


if __name__ == "__main__":
    main()
