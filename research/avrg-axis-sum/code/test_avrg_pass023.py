#!/usr/bin/env python3
"""Fast consistency checks for the saved PASS023 result."""

from __future__ import annotations

import json
import math
import statistics
import unittest
from pathlib import Path

import avrg_pass023


HERE = Path(__file__).resolve().parent
RESULT = HERE.parent / "results" / "avrg_pass023_results.json"


class Pass023ResultTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads(RESULT.read_text(encoding="utf-8"))

    def test_scope_and_claim_ceiling(self) -> None:
        self.assertEqual(self.data["pass"], "PASS023")
        self.assertEqual(self.data["configuration"]["exps"], [15, 16, 17, 18])
        self.assertEqual(
            self.data["configuration"]["moduli"],
            [5, 7, 11, 13, 17, 19, 23, 29, 31],
        )
        self.assertEqual([len(window["rows"]) for window in self.data["windows"]], [34] * 4)
        self.assertIn("No asymptotic proof", self.data["claim_ceiling"])
        self.assertIn("Goldbach", self.data["claim_ceiling"])

    def test_calibration(self) -> None:
        calibration = self.data["calibration"]
        self.assertTrue(calibration["passed"])
        self.assertEqual(calibration["shared_rows"], 15)
        self.assertLessEqual(
            calibration["max_absolute_difference"], calibration["tolerance"]
        )

    def test_saved_per_modulus_summaries(self) -> None:
        for window in self.data["windows"]:
            for summary in window["per_modulus"]:
                rows = [row for row in window["rows"] if row["r"] == summary["r"]]
                ratios = [row["energy_ratio"] for row in rows]
                self.assertEqual(len(rows), summary["representative_count"])
                self.assertAlmostEqual(statistics.fmean(ratios), summary["mean_ratio"], places=14)
                self.assertAlmostEqual(
                    avrg_pass023.population_sd(ratios), summary["population_sd"], places=14
                )
                self.assertAlmostEqual(min(ratios), summary["min_ratio"], places=14)
                self.assertAlmostEqual(max(ratios), summary["max_ratio"], places=14)
                self.assertTrue(all(row["on_energy"] > 0 for row in rows))
                self.assertTrue(all(row["off_energy"] > 0 for row in rows))

    def test_saved_model_comparisons(self) -> None:
        for window in self.data["windows"]:
            observed = avrg_pass023.compare_models(window["per_modulus"])
            saved = window["model_comparison"]
            self.assertAlmostEqual(
                observed["free_intercept"]["intercept"],
                saved["free_intercept"]["intercept"],
                places=14,
            )
            self.assertAlmostEqual(
                observed["fixed_sse_over_free_sse"],
                saved["fixed_sse_over_free_sse"],
                places=14,
            )
            self.assertEqual(
                observed["loocv"]["preferred_by_rmse"],
                saved["loocv"]["preferred_by_rmse"],
            )

    def test_larger_moduli_aggregate(self) -> None:
        rows = self.data["cross_window"]["larger_moduli_by_window"]
        self.assertEqual([row["exp"] for row in rows], [15, 16, 17, 18])
        for row in rows:
            self.assertEqual(row["moduli"], [23, 29, 31])
            self.assertLess(row["mean_absolute_deviation_from_two"], 0.032)
            self.assertLess(row["max_absolute_deviation_from_two"], 0.077)
            self.assertTrue(math.isfinite(row["mean_of_modulus_means"]))


if __name__ == "__main__":
    unittest.main()
