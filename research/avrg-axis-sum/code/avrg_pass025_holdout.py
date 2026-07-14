#!/usr/bin/env python3
"""Compute the locked PASS025 holdout window e=19 without analyzing it."""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from pathlib import Path


HOLDOUT_EXP = 19
LOCKED_MODULI = (5, 7, 11, 13, 17, 19, 23, 29, 31)


def load_pass023_module():
    try:
        return importlib.import_module("avrg_pass023")
    except ModuleNotFoundError:
        sibling = Path(__file__).resolve().parents[1] / "pass023"
        sys.path.insert(0, str(sibling))
        return importlib.import_module("avrg_pass023")


def default_output_path() -> Path:
    here = Path(__file__).resolve().parent
    archive_results = here.parent / "results"
    if archive_results.is_dir():
        return archive_results / "avrg_pass025_holdout_e19.json"
    return here / "avrg_pass025_holdout_e19.json"


def build_holdout(progress: bool = False) -> dict:
    pass023 = load_pass023_module()
    window = pass023.run_window(HOLDOUT_EXP, LOCKED_MODULI, progress=progress)
    return {
        "pass": "PASS025",
        "artifact": "locked held-out window",
        "classification": "finite computational diagnostic input",
        "claim_ceiling": (
            "No asymptotic proof and no direct progress toward a proof of Goldbach."
        ),
        "protocol": {
            "training_exps": [15, 16, 17, 18],
            "holdout_exp": HOLDOUT_EXP,
            "moduli": list(LOCKED_MODULI),
            "computed_after_protocol_commit": True,
        },
        "window": window,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=default_output_path())
    parser.add_argument("--progress", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = build_holdout(progress=args.progress)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"PASS025 holdout computed without phase analysis: {args.output}")


if __name__ == "__main__":
    main()
