#!/usr/bin/env python3
"""Safety and integration tests for PASS034."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import numpy as np

import avrg_pass034 as p34


class Pass034Tests(unittest.TestCase):
    def test_exact_plane_has_unit_rank2_score(self):
        angles = np.asarray([0.0, 0.5, 1.1, 1.9, 2.7])
        units = np.column_stack(
            [np.cos(angles), np.sin(angles), np.zeros_like(angles), np.zeros_like(angles)]
        )
        rows = p34.leave_one_out_subspace_scores(units)
        self.assertTrue(all(abs(row["rank2_projection_score"] - 1.0) < 1e-12 for row in rows))
        self.assertLess(
            np.mean([row["rank1_projection_score"] for row in rows]), 0.95
        )

    def test_row_sign_flips_do_not_change_subspace_scores(self):
        angles = np.asarray([0.1, 0.7, 1.4, 2.0, 2.8])
        units = np.column_stack(
            [np.cos(angles), np.sin(angles), np.zeros_like(angles)]
        )
        baseline = p34.leave_one_out_subspace_scores(units)
        flipped = units * np.asarray([1, -1, 1, -1, 1])[:, None]
        changed = p34.leave_one_out_subspace_scores(flipped)
        for left, right in zip(baseline, changed):
            self.assertAlmostEqual(
                left["rank1_projection_score"], right["rank1_projection_score"], places=12
            )
            self.assertAlmostEqual(
                left["rank2_projection_score"], right["rank2_projection_score"], places=12
            )

    def test_off_plane_heldout_vector_is_rejected(self):
        units = np.asarray(
            [
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [2 ** -0.5, 2 ** -0.5, 0.0],
                [2 ** -0.5, -2 ** -0.5, 0.0],
                [0.0, 0.0, 1.0],
            ]
        )
        rows = p34.leave_one_out_subspace_scores(units)
        self.assertAlmostEqual(rows[4]["rank2_projection_score"], 0.0, places=12)

    def test_rank2_never_below_rank1(self):
        rng = np.random.default_rng(34)
        units = rng.normal(size=(5, 8))
        units /= np.linalg.norm(units, axis=1, keepdims=True)
        rows = p34.leave_one_out_subspace_scores(units)
        self.assertTrue(
            all(
                row["rank2_projection_score"] + 1e-12
                >= row["rank1_projection_score"]
                for row in rows
            )
        )

    def test_null_description_uses_plus_one_correction(self):
        samples = np.asarray([0.1, 0.2, 0.3, 0.4])
        result = p34.describe_null(samples, 0.35)
        self.assertEqual(result["exceedance_count"], 1)
        self.assertAlmostEqual(result["one_sided_p_value"], 2 / 5)

    def test_decision_requires_every_condition(self):
        scored = {
            "global": {
                "mean_rank2_projection_score": 0.80,
                "mean_rank2_gain_over_rank1": 0.12,
            },
            "by_modulus": [
                {"mean_rank2_projection_score": value}
                for value in [0.8, 0.8, 0.8, 0.8, 0.8, 0.4, 0.4]
            ],
            "by_heldout_window": [
                {"mean_rank2_projection_score": value}
                for value in [0.7, 0.7, 0.7, 0.7, 0.4]
            ],
        }
        permutation = {
            "rank2_projection_primary": {"one_sided_p_value": 0.005}
        }
        passed = p34.decision_summary(scored, permutation)
        self.assertTrue(passed["supported"])
        scored["global"]["mean_rank2_gain_over_rank1"] = 0.09
        failed = p34.decision_summary(scored, permutation)
        self.assertFalse(failed["supported"])

    def test_locked_integration_smoke(self):
        with tempfile.TemporaryDirectory() as directory:
            result = p34.build_result(
                p34.default_pass028_path(),
                p34.default_pass032_path(),
                p34.default_pass033_path(),
                permutation_iterations=2,
            )
            self.assertEqual(result["pass"], "PASS034")
            self.assertEqual(result["safety"]["fold_count"], 35)
            self.assertLessEqual(
                result["safety"]["maximum_pass033_reproduction_error"], 1e-12
            )
            self.assertGreaterEqual(
                result["safety"]["minimum_training_numerical_rank"], 2
            )
            self.assertTrue(result["safety"]["all_rank2_scores_dominate_rank1"])


if __name__ == "__main__":
    unittest.main()
