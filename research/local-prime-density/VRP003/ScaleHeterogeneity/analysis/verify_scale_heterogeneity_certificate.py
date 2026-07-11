from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
GENERATED = ROOT / "data" / "generated_scale_heterogeneity_certificate.json"
COMMITTED = ROOT / "certificates" / "SCALE_HETEROGENEITY_CERTIFICATE.json"
NUMBER_RTOL = 1e-11
NUMBER_ATOL = 1e-12


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def compare(expected: Any, observed: Any, path: str = "root") -> None:
    if isinstance(expected, bool) or expected is None or isinstance(expected, str):
        require(expected == observed, f"Mismatch at {path}: {expected!r} != {observed!r}")
        return
    if isinstance(expected, (int, float)) and not isinstance(expected, bool):
        require(isinstance(observed, (int, float)) and not isinstance(observed, bool), f"Type mismatch at {path}")
        require(
            math.isclose(float(expected), float(observed), rel_tol=NUMBER_RTOL, abs_tol=NUMBER_ATOL),
            f"Numeric mismatch at {path}: {expected!r} != {observed!r}",
        )
        return
    if isinstance(expected, list):
        require(isinstance(observed, list), f"Type mismatch at {path}")
        require(len(expected) == len(observed), f"Length mismatch at {path}")
        for index, (left, right) in enumerate(zip(expected, observed, strict=True)):
            compare(left, right, f"{path}[{index}]")
        return
    if isinstance(expected, dict):
        require(isinstance(observed, dict), f"Type mismatch at {path}")
        require(set(expected) == set(observed), f"Key mismatch at {path}")
        for key in expected:
            compare(expected[key], observed[key], f"{path}.{key}")
        return
    raise RuntimeError(f"Unsupported certificate type at {path}: {type(expected)}")


def main() -> None:
    require(GENERATED.exists(), f"Missing generated certificate: {GENERATED}")
    require(COMMITTED.exists(), f"Missing committed certificate: {COMMITTED}")
    expected = json.loads(COMMITTED.read_text(encoding="utf-8"))
    observed = json.loads(GENERATED.read_text(encoding="utf-8"))
    compare(expected, observed)
    require(
        expected["closure_decision"]
        == "CLOSE SCALE-HETEROGENEITY DIAGNOSTIC — PASS AS DIAGNOSTIC, NOT AS MECHANISM",
        "Unexpected closure decision",
    )
    require(expected["pvg_role"]["necessity_status"] == "not established", "PVG necessity was overclaimed")
    print("verify_scale_heterogeneity_certificate: PASS — regenerated certificate matches committed result")


if __name__ == "__main__":
    main()
