from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CERTIFICATE = ROOT / "certificates" / "SCALE_HETEROGENEITY_CERTIFICATE.json"
REPORT = ROOT / "SCALE_HETEROGENEITY_REPORT.md"
CLOSURE = ROOT / "CLOSURE_REVIEW.md"
GAIN = ROOT / "data" / "scale_gain_decomposition.csv"
GROUP = ROOT / "data" / "scale_group_alignment.csv"
ADJACENT = ROOT / "data" / "adjacent_lambda_covariance.csv"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def require_finite_tree(value: Any, path: str = "root") -> None:
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return
    if isinstance(value, (int, float)):
        require(np.isfinite(float(value)), f"Non-finite certificate value at {path}")
        return
    if isinstance(value, list):
        for index, item in enumerate(value):
            require_finite_tree(item, f"{path}[{index}]")
        return
    if isinstance(value, dict):
        for key, item in value.items():
            require_finite_tree(item, f"{path}.{key}")
        return
    raise RuntimeError(f"Unsupported certificate value at {path}: {type(value)}")


def main() -> None:
    for path in [CERTIFICATE, REPORT, CLOSURE, GAIN, GROUP, ADJACENT]:
        require(path.exists(), f"Missing scale closure artifact: {path}")

    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    require_finite_tree(certificate)
    require(certificate["status"] == "SCALE_HETEROGENEITY_DIAGNOSTIC_PASS", "Bad status")
    require(certificate["pvg_role"]["necessity_status"] == "not established", "PVG overclaim")
    require("No theorem about primes" in certificate["classification"], "Theorem ceiling missing")
    require("No RH/GRH progress" in certificate["classification"], "RH/GRH ceiling missing")

    gain = pd.read_csv(GAIN)
    groups = pd.read_csv(GROUP)
    adjacent = pd.read_csv(ADJACENT)
    require(len(gain) == 4, "Gain table row count changed")
    require(len(groups) == 16, "Group table row count changed")
    require(len(adjacent) == 4, "Adjacent table row count changed")

    numeric_frames = {
        "gain": gain.select_dtypes(include=["number"]),
        "groups": groups.select_dtypes(include=["number"]),
        "adjacent": adjacent.select_dtypes(include=["number"]),
    }
    for name, frame in numeric_frames.items():
        require(np.isfinite(frame.to_numpy(dtype=float)).all(), f"Non-finite values in {name} table")

    require((adjacent["covariance_past_future"] < 0).all(), "Adjacent covariance sign changed")

    closure_text = CLOSURE.read_text(encoding="utf-8")
    report_text = REPORT.read_text(encoding="utf-8")
    for token in [
        "PASS AS DIAGNOSTIC, NOT AS MECHANISM",
        "1.862645149230957e-09",
        "3.7473279654308245e-14",
        "PVG necessity is not established",
        "Dataset 004 remains unauthorized",
    ]:
        require(token in closure_text + report_text, f"Closure token missing: {token}")

    print("verify_scale_heterogeneity_closure: PASS")


if __name__ == "__main__":
    main()
