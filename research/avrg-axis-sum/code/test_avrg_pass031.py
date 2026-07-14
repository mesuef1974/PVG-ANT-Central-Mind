import unittest

import numpy as np

import avrg_pass031 as p31


class Pass031Tests(unittest.TestCase):
    def test_locked_inputs(self):
        self.assertEqual(
            p31.sha256_file(p31.default_pass028_path()),
            p31.EXPECTED_PASS028_SHA256,
        )
        locked = p31.load_locked_pass030(p31.default_pass030_path())
        self.assertEqual(len(locked["folds"]), 35)

    def test_augmented_rank_is_exactly_d_plus_one(self):
        p30 = p31.load_pass030_module()
        rng = np.random.default_rng(310701)
        train = rng.normal(size=(24, 9))
        basis, _ = p30.sum_aware_basis(train, 5)
        self.assertEqual(basis.shape, (9, 5))
        np.testing.assert_allclose(basis.T @ basis, np.eye(5), atol=1e-12)

    def test_augmented_basis_preserves_sum(self):
        p30 = p31.load_pass030_module()
        p29 = p30.load_pass029_module()
        rng = np.random.default_rng(310702)
        train = rng.normal(size=(30, 8))
        test = rng.normal(size=(7, 8))
        basis, _ = p30.sum_aware_basis(train, 4)
        metrics = p29.projection_metrics(test, basis)
        self.assertAlmostEqual(metrics["scalar_skill"], 1.0, places=12)

    def test_free_rank_d_plus_one_cannot_capture_less_training_energy(self):
        rng = np.random.default_rng(310703)
        train = rng.normal(size=(20, 7))
        _, singular_values, _ = np.linalg.svd(train, full_matrices=False)
        energy = singular_values * singular_values
        self.assertGreaterEqual(np.sum(energy[:4]), np.sum(energy[:3]))

    def test_random_null_reproducible(self):
        p30 = p31.load_pass030_module()
        p29 = p30.load_pass029_module()
        rng = np.random.default_rng(310704)
        test = rng.normal(size=(4, 6))
        basis, direction = p30.sum_aware_basis(rng.normal(size=(12, 6)), 3)
        metrics = p29.projection_metrics(test, basis)
        fold = {
            "orbit_count": 6,
            "rank_augmented": 3,
            "_test": test,
            "augmented_metrics": metrics,
            "_sum_direction": direction,
        }
        first = p31.constrained_random_null(
            [fold], p30, iterations=50, seed=123
        )
        second = p31.constrained_random_null(
            [fold], p30, iterations=50, seed=123
        )
        self.assertEqual(first, second)

    def test_all_locked_folds_have_ambient_room(self):
        locked = p31.load_locked_pass030(p31.default_pass030_path())
        for fold in locked["folds"]:
            self.assertLessEqual(
                int(fold["selected_rank"]) + 1, int(fold["orbit_count"])
            )


if __name__ == "__main__":
    unittest.main()
