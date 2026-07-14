import unittest

import numpy as np

import avrg_pass030 as p30


class Pass030Tests(unittest.TestCase):
    def test_locked_inputs(self):
        self.assertEqual(
            p30.sha256_file(p30.default_pass028_path()),
            p30.EXPECTED_PASS028_SHA256,
        )
        locked = p30.load_locked_pass029(p30.default_pass029_path())
        self.assertEqual(len(locked["folds"]), 35)

    def test_sum_aware_basis_has_requested_rank(self):
        rng = np.random.default_rng(300701)
        matrix = rng.normal(size=(20, 7))
        basis, direction = p30.sum_aware_basis(matrix, 4)
        self.assertEqual(basis.shape, (7, 4))
        np.testing.assert_allclose(basis.T @ basis, np.eye(4), atol=1e-12)
        np.testing.assert_allclose(basis @ basis.T @ direction, direction, atol=1e-12)

    def test_sum_is_preserved_exactly(self):
        p29 = p30.load_pass029_module()
        rng = np.random.default_rng(300702)
        train = rng.normal(size=(24, 9))
        test = rng.normal(size=(6, 9))
        basis, _ = p30.sum_aware_basis(train, 4)
        metrics = p29.projection_metrics(test, basis)
        self.assertAlmostEqual(metrics["scalar_skill"], 1.0, places=12)
        projected = test @ basis @ basis.T
        np.testing.assert_allclose(
            np.sum(projected, axis=1), np.sum(test, axis=1), atol=1e-12
        )

    def test_rank_one_is_sum_direction(self):
        rng = np.random.default_rng(300703)
        matrix = rng.normal(size=(10, 5))
        basis, direction = p30.sum_aware_basis(matrix, 1)
        np.testing.assert_allclose(basis[:, 0], direction)

    def test_random_constrained_basis_preserves_sum(self):
        rng = np.random.default_rng(300704)
        basis = p30.random_constrained_basis(8, 3, rng)
        ones = np.ones(8)
        np.testing.assert_allclose(basis @ basis.T @ ones, ones, atol=1e-12)
        np.testing.assert_allclose(basis.T @ basis, np.eye(3), atol=1e-12)

    def test_random_constrained_null_is_reproducible(self):
        p29 = p30.load_pass029_module()
        rng = np.random.default_rng(300705)
        test = rng.normal(size=(4, 6))
        basis, direction = p30.sum_aware_basis(rng.normal(size=(12, 6)), 2)
        metrics = p29.projection_metrics(test, basis)
        fold = {
            "orbit_count": 6,
            "selected_rank": 2,
            "_test": test,
            "constrained_metrics": metrics,
            "_sum_direction": direction,
        }
        first = p30.random_constrained_null([fold], iterations=50, seed=123)
        second = p30.random_constrained_null([fold], iterations=50, seed=123)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
