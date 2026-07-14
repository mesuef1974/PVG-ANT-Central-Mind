#!/usr/bin/env python3
"""Reproducibility and invariance checks for PASS022."""

from __future__ import annotations

import unittest
from pathlib import Path

import avrg_pass022


HERE = Path(__file__).resolve().parent
RESULTS = HERE.parent / "results"
SMALL = RESULTS / "avrg_pass015_e17.json"
LARGE = RESULTS / "avrg_pass021_full_e17.json"


class Pass022Tests(unittest.TestCase):
    def test_loader_uses_actual_ratio_fields(self) -> None:
        rows, metadata = avrg_pass022.load_rows(SMALL, LARGE)
        self.assertEqual(metadata["window"], [2**17, 2**18])
        self.assertEqual(len(rows), 27)
        self.assertEqual({row["ratio_field"] for row in rows}, {
            "on_off_ratio",
            "energy_ratio",
        })
        self.assertTrue(all(row["k"] % 2 == 0 for row in rows))

    def test_conjugacy_orbits_are_complete_and_numerically_equal(self) -> None:
        rows, _ = avrg_pass022.load_rows(SMALL, LARGE)
        representatives, checks = avrg_pass022.collapse_conjugates(rows)
        self.assertEqual(len(representatives), 15)
        self.assertTrue(all(check["passed"] for check in checks))
        self.assertLessEqual(
            max(check["max_ratio_spread"] for check in checks), 3e-15
        )

    def test_modulus_summary_regression_values(self) -> None:
        result = avrg_pass022.analyze(SMALL, LARGE)
        means = {row["r"]: row["mean_ratio"] for row in result["per_modulus"]}
        self.assertAlmostEqual(means[5], 2.6471378753211456, places=14)
        self.assertAlmostEqual(means[13], 2.1184837890135113, places=14)
        self.assertAlmostEqual(means[17], 1.993905262656738, places=14)
        self.assertAlmostEqual(means[19], 2.004415583064823, places=14)

    def test_analysis_is_deterministic_and_claim_limited(self) -> None:
        first = avrg_pass022.analyze(SMALL, LARGE)
        second = avrg_pass022.analyze(SMALL, LARGE)
        self.assertEqual(first, second)
        self.assertIn("No asymptotic proof", first["claim_ceiling"])
        self.assertEqual(
            first["trend_with_inverse_modulus"]["exact_permutation"][
                "permutations"
            ],
            720,
        )
        self.assertEqual(
            first["within_modulus_character_tests"]["frequency_linear"][
                "exact_within_modulus_permutations"
            ],
            6912,
        )


if __name__ == "__main__":
    unittest.main()
