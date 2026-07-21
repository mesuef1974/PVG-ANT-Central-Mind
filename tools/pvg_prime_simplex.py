#!/usr/bin/env python3
"""Canonical boundary-correct interface for general PVG prime-simplex laws."""

from __future__ import annotations

import argparse
import json
from typing import Iterable

try:
    from . import pvg_prime_simplex_general as core
except ImportError:
    import pvg_prime_simplex_general as core  # type: ignore

SimplexInputError = core.SimplexInputError
validate_vertices = core.validate_vertices
face_counts = core.face_counts
pair_data = core.pair_data
consecutive_gaps = core.consecutive_gaps
reconstruct_from_anchor = core.reconstruct_from_anchor
all_pair_sums = core.all_pair_sums
reconstruct_from_labeled_pair_sums = core.reconstruct_from_labeled_pair_sums
gcd_of_pair_sums = core.gcd_of_pair_sums
path_ratio = core.path_ratio
normalized_gap = core.normalized_gap
compose_normalized_gaps = core.compose_normalized_gaps


def analyze(vertices: Iterable[int]) -> dict:
    report = core.analyze(vertices)
    m = report["m"]
    if m == 2:
        # One edge has only one pair sum. Its gcd is that sum itself, so the
        # global {1,2} gcd law is not defined until at least three vertices.
        report["pair_sum_gcd_rule_available"] = False
        report["expected_pair_sum_gcd"] = None
        verification = report["verification"]
        verification.pop("pair_sum_gcd_rule", None)
        verification["pair_sum_gcd_rule_for_m_ge_3"] = True
    else:
        report["pair_sum_gcd_rule_available"] = True
        verification = report["verification"]
        if "pair_sum_gcd_rule" in verification:
            verification["pair_sum_gcd_rule_for_m_ge_3"] = verification.pop("pair_sum_gcd_rule")
    return report


def parse_vertices(text: str) -> tuple[int, ...]:
    return core.parse_vertices(text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze general PVG prime-simplex laws.")
    parser.add_argument("vertices", help="strictly increasing comma-separated primes")
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    try:
        report = analyze(parse_vertices(args.vertices))
    except SimplexInputError as exc:
        print(json.dumps({"status": "invalid_prime_simplex", "reason": str(exc)}, indent=2))
        return 2
    print(json.dumps(report, sort_keys=True, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
