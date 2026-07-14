import unittest

import numpy as np

import avrg_pass033 as p33


class Pass033Tests(unittest.TestCase):
    def test_locked_inputs(self):
        self.assertEqual(
            p33.sha256_file(p33.default_pass028_path()),
            p33.EXPECTED_PASS028_SHA256,
        )
        locked = p33.load_locked_pass032(p33.default_pass032_path())
        self.assertEqual(len(locked["folds"]), 35)

    def test_identical_functionals_have_unit_coherence(self):
        units = np.tile(np.asarray([[1.0, 0.0, 0.0]]), (5, 1))
        metrics = p33.stability_metrics(units, np.ones(5))
        self.assertAlmostEqual(metrics["oriented_coherence"], 1.0, places=12)
        self.assertAlmostEqual(metrics["axis_coherence"], 1.0, places=12)
        self.assertEqual(metrics["negative_pair_count"], 0)

    def test_sign_flips_preserve_axis_but_destroy_orientation(self):
        units = np.asarray(
            [[1.0, 0.0], [1.0, 0.0], [-1.0, 0.0], [-1.0, 0.0]]
        )
        metrics = p33.stability_metrics(units, np.ones(4))
        self.assertAlmostEqual(metrics["oriented_coherence"], 0.0, places=12)
        self.assertAlmostEqual(metrics["axis_coherence"], 1.0, places=12)
        self.assertEqual(metrics["negative_pair_count"], 4)

    def test_orthogonal_functionals_have_low_orientation(self):
        units = np.eye(4)
        metrics = p33.stability_metrics(units, np.ones(4))
        self.assertAlmostEqual(metrics["oriented_coherence"], 0.25, places=12)
        self.assertAlmostEqual(metrics["axis_coherence"], 0.25, places=12)

    def test_norm_cv_is_scale_sensitive(self):
        units = np.tile(np.asarray([[1.0, 0.0]]), (5, 1))
        stable = p33.stability_metrics(units, np.ones(5))
        variable = p33.stability_metrics(
            units, np.asarray([1.0, 2.0, 3.0, 4.0, 5.0])
        )
        self.assertAlmostEqual(stable["functional_norm_cv"], 0.0, places=12)
        self.assertGreater(variable["functional_norm_cv"], 0.0)

    def test_global_stability_uses_equal_modulus_weight(self):
        rows = [
            {
                "oriented_coherence": 0.2,
                "axis_coherence": 0.4,
                "mean_signed_cosine": 0.0,
                "negative_pair_count": 2,
                "pair_count": 10,
            },
            {
                "oriented_coherence": 0.8,
                "axis_coherence": 0.9,
                "mean_signed_cosine": 0.5,
                "negative_pair_count": 0,
                "pair_count": 10,
            },
        ]
        result = p33.global_stability(rows)
        self.assertAlmostEqual(result["mean_oriented_coherence"], 0.5, places=12)
        self.assertAlmostEqual(result["mean_axis_coherence"], 0.65, places=12)


if __name__ == "__main__":
    unittest.main()
