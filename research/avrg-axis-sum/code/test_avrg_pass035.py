#!/usr/bin/env python3
"""Safety and integration tests for PASS035."""

from __future__ import annotations

import unittest

import numpy as np

import avrg_pass035 as p35


class Pass035Tests(unittest.TestCase):
    def test_positive_scaling_is_pure_calibration(self):
        predicted = np.asarray([1.0, -2.0, 3.0, -4.0])
        actual = 2.5 * predicted
        result = p35.oracle_gain_metrics(actual, predicted)
        self.assertAlmostEqual(result["signed_cosine"], 1.0, places=12)
        self.assertAlmostEqual(result["signed_gain"], 2.5, places=12)
        self.assertAlmostEqual(result["positive_gain"], 2.5, places=12)
        self.assertAlmostEqual(result["signed_oracle_skill"], 1.0, places=12)
        self.assertAlmostEqual(result["positive_oracle_skill"], 1.0, places=12)

    def test_antialignment_requires_signed_gain(self):
        predicted = np.asarray([1.0, -2.0, 3.0, -4.0])
        actual = -predicted
        result = p35.oracle_gain_metrics(actual, predicted)
        self.assertAlmostEqual(result["signed_cosine"], -1.0, places=12)
        self.assertAlmostEqual(result["signed_gain"], -1.0, places=12)
        self.assertAlmostEqual(result["positive_gain"], 0.0, places=12)
        self.assertAlmostEqual(result["signed_oracle_skill"], 1.0, places=12)
        self.assertAlmostEqual(result["positive_oracle_skill"], 0.0, places=12)

    def test_leave_one_window_out_exact_constant_gain(self):
        predicted = np.asarray([1.0, 2.0, 2.0, 1.0, 3.0, 4.0])
        actual = 3.0 * predicted
        result = p35.leave_one_target_window_calibration(
            actual, predicted, [15, 16, 17], mode_count=2
        )
        self.assertAlmostEqual(result["signed_skill"], 1.0, places=12)
        self.assertAlmostEqual(result["positive_skill"], 1.0, places=12)
        for fold in result["folds"]:
            self.assertAlmostEqual(fold["signed_gain"], 3.0, places=12)
            self.assertNotIn(fold["heldout_exp"], fold["training_exps"])

    def test_heldout_window_does_not_fit_its_own_gain(self):
        predicted = np.ones(6)
        actual = np.asarray([1.0, 1.0, 1.0, 1.0, 10.0, 10.0])
        result = p35.leave_one_target_window_calibration(
            actual, predicted, [15, 16, 17], mode_count=2
        )
        heldout_last = next(
            row for row in result["folds"] if row["heldout_exp"] == 17
        )
        self.assertAlmostEqual(heldout_last["signed_gain"], 1.0, places=12)
        self.assertEqual(heldout_last["training_exps"], [15, 16])

    def test_calibration_dominated_classification(self):
        metrics = {
            "positive_oracle_skill": 0.80,
            "cv_positive_skill": 0.25,
            "positive_direction_count": 12,
            "nonnegative_modulus_cv_positive_skill_count": 6,
            "reciprocity_eligible_modulus_count": 5,
            "median_positive_gain_reciprocity_log_error": 0.20,
            "signed_oracle_skill": 0.82,
            "negative_signed_gain_count": 2,
            "cv_signed_skill": 0.26,
        }
        result = p35.classify_wall(metrics)
        self.assertEqual(
            result["decision"], "calibration_dominated_failure_on_finite_range"
        )

    def test_orientation_reversal_classification(self):
        metrics = {
            "positive_oracle_skill": 0.10,
            "cv_positive_skill": -0.10,
            "positive_direction_count": 5,
            "nonnegative_modulus_cv_positive_skill_count": 2,
            "reciprocity_eligible_modulus_count": 2,
            "median_positive_gain_reciprocity_log_error": 1.0,
            "signed_oracle_skill": 0.75,
            "negative_signed_gain_count": 8,
            "cv_signed_skill": 0.20,
        }
        result = p35.classify_wall(metrics)
        self.assertEqual(
            result["decision"],
            "orientation_reversal_dominated_failure_on_finite_range",
        )

    def test_mixed_classification(self):
        metrics = {
            "positive_oracle_skill": 0.30,
            "cv_positive_skill": -0.05,
            "positive_direction_count": 8,
            "nonnegative_modulus_cv_positive_skill_count": 3,
            "reciprocity_eligible_modulus_count": 3,
            "median_positive_gain_reciprocity_log_error": 0.9,
            "signed_oracle_skill": 0.40,
            "negative_signed_gain_count": 6,
            "cv_signed_skill": -0.02,
        }
        result = p35.classify_wall(metrics)
        self.assertEqual(
            result["decision"], "mixed_or_diffuse_direction_calibration_failure"
        )

    def test_locked_integration_smoke(self):
        result = p35.build_result(
            p35.default_pass028_path(),
            p35.default_pass032_path(),
            p35.default_pass033_path(),
            p35.default_pass034_path(),
            progress=False,
        )
        self.assertEqual(result["pass"], "PASS035")
        self.assertEqual(result["safety"]["direction_count"], 14)
        self.assertEqual(result["safety"]["modulus_count"], 7)
        self.assertTrue(result["safety"]["e14_gate_passed"])
        self.assertLessEqual(
            result["safety"]["pass034_reproduction_error"],
            p35.REPRODUCTION_TOLERANCE,
        )
        self.assertLessEqual(
            result["safety"]["maximum_signed_oracle_formula_error"],
            p35.FORMULA_TOLERANCE,
        )
        self.assertLessEqual(
            result["safety"]["maximum_positive_oracle_formula_error"],
            p35.FORMULA_TOLERANCE,
        )


if __name__ == "__main__":
    unittest.main()
