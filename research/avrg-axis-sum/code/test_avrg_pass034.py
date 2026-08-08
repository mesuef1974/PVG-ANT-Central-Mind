#!/usr/bin/env python3
"""Safety and integration tests for PASS034."""

from __future__ import annotations

import unittest

import numpy as np

import avrg_pass034 as p34


class Pass034Tests(unittest.TestCase):
    def test_blocks_are_disjoint_and_complete(self):
        self.assertFalse(set(p34.EARLY_EXPS) & set(p34.LATE_EXPS))
        self.assertEqual(
            tuple(sorted(p34.EARLY_EXPS + p34.LATE_EXPS)), p34.ALL_EXPS
        )

    def test_scalar_skill_identity_and_zero_baseline(self):
        actual = np.asarray([1.0, -2.0, 3.0])
        self.assertAlmostEqual(p34.scalar_skill(actual, actual), 1.0)
        self.assertAlmostEqual(p34.scalar_skill(actual, np.zeros_like(actual)), 0.0)

    def test_null_description_uses_plus_one_correction(self):
        samples = np.asarray([0.1, 0.2, 0.3, 0.4])
        result = p34.describe_null(samples, 0.35)
        self.assertEqual(result["exceedance_count"], 1)
        self.assertAlmostEqual(result["one_sided_p_value"], 2 / 5)

    def test_coefficient_arrays_use_training_mean_only(self):
        raw = {(11, 2): np.asarray([1, 2, 3, 10, 20, 30], dtype=float)}
        model = {
            "r": 11,
            "modes": [2],
            "block": [14, 15, 16],
            "target_block": [17, 18, 19],
        }
        train, target = p34.coefficient_arrays_for_model(raw, model)
        np.testing.assert_allclose(train, [-1, 0, 1])
        np.testing.assert_allclose(target, [8, 18, 28])

    def test_decision_requires_all_six_conditions(self):
        by_modulus = [
            {
                "signed_functional_cosine": cosine,
                "bidirectional_scalar_skill": skill,
            }
            for cosine, skill in zip(
                [0.6, 0.6, 0.6, 0.6, 0.6, 0.1, 0.1],
                [0.2, 0.2, 0.2, 0.2, 0.2, -0.1, -0.1],
            )
        ]
        global_metrics = {
            "mean_signed_functional_cosine": 0.55,
            "bidirectional_scalar_skill": 0.15,
        }
        permutation = {
            "signed_functional_cosine_primary": {"one_sided_p_value": 0.005},
            "bidirectional_scalar_skill_primary": {"one_sided_p_value": 0.005},
        }
        passed = p34.decision_summary(by_modulus, global_metrics, permutation)
        self.assertTrue(passed["supported"])
        permutation["bidirectional_scalar_skill_primary"]["one_sided_p_value"] = 0.02
        failed = p34.decision_summary(by_modulus, global_metrics, permutation)
        self.assertFalse(failed["supported"])

    def test_exact_e14_scan_gate(self):
        p28 = p34.load_module("avrg_pass028")
        rows, diagnostics = p34.scan_e14(p28, progress=False)
        self.assertEqual(len(rows), 32)
        self.assertTrue(diagnostics["passed"])
        self.assertLessEqual(
            diagnostics["maximum_pointwise_closure_error"],
            p34.E14_CLOSURE_TOLERANCE,
        )
        self.assertLessEqual(
            diagnostics["maximum_zero_residue_range_across_characters"],
            p34.E14_ZERO_RANGE_TOLERANCE,
        )

    def test_locked_integration_smoke(self):
        result = p34.build_result(
            p34.default_pass028_path(),
            p34.default_pass032_path(),
            p34.default_pass033_path(),
            permutation_iterations=2,
            progress=False,
        )
        self.assertEqual(result["pass"], "PASS034")
        self.assertEqual(result["safety"]["e14_row_count"], 32)
        self.assertEqual(result["safety"]["model_count"], 14)
        self.assertTrue(result["safety"]["blocks_are_disjoint"])
        self.assertTrue(result["safety"]["e14_gate_passed"])
        self.assertTrue(result["safety"]["all_design_ranks_full"])
        self.assertLessEqual(
            result["safety"]["maximum_basis_sum_perpendicular_error"], 1e-12
        )
        self.assertGreater(result["safety"]["minimum_functional_norm"], 0)


if __name__ == "__main__":
    unittest.main()
