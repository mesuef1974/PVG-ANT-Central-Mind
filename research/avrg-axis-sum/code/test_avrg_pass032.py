import unittest

import numpy as np

import avrg_pass032 as p32


class Pass032Tests(unittest.TestCase):
    def test_locked_inputs(self):
        self.assertEqual(
            p32.sha256_file(p32.default_pass028_path()),
            p32.EXPECTED_PASS028_SHA256,
        )
        locked = p32.load_locked_pass031(p32.default_pass031_path())
        self.assertEqual(len(locked["folds"]), 35)

    def test_least_squares_recovers_exact_linear_coupling(self):
        rng = np.random.default_rng(320701)
        z_train = rng.normal(size=(30, 4))
        beta_true = np.asarray([0.4, -0.2, 0.8, 0.1])
        c_train = z_train @ beta_true
        z_test = rng.normal(size=(8, 4))
        beta, prediction, rank, _ = p32.least_squares_coupling(
            z_train, c_train, z_test
        )
        np.testing.assert_allclose(beta, beta_true, atol=1e-12)
        np.testing.assert_allclose(prediction, z_test @ beta_true, atol=1e-12)
        self.assertEqual(rank, 4)

    def test_amplitude_basis_is_perpendicular_to_sum(self):
        p31 = p32.load_pass031_module()
        p30 = p31.load_pass030_module()
        rng = np.random.default_rng(320702)
        train = rng.normal(size=(24, 9))
        basis, direction = p32.amplitude_basis(train, 4, p30)
        np.testing.assert_allclose(basis.T @ basis, np.eye(4), atol=1e-12)
        np.testing.assert_allclose(basis.T @ direction, np.zeros(4), atol=1e-12)

    def test_zero_scalar_baseline_has_zero_skill(self):
        rng = np.random.default_rng(320703)
        test = rng.normal(size=(7, 6))
        vector_prediction = np.zeros_like(test)
        scalar_prediction = np.zeros(test.shape[0])
        metrics = p32.forecast_metrics(test, vector_prediction, scalar_prediction)
        self.assertAlmostEqual(metrics["scalar_skill"], 0.0, places=12)

    def test_permuted_target_order_matches_training_matrix_order(self):
        exps = (15, 16, 17, 18, 19)
        fold = {
            "r": 11,
            "heldout_exp": 17,
            "modes": [2, 4],
        }
        raw = {
            (11, 2): np.asarray([1.0, 2.0, 3.0, 4.0, 5.0]),
            (11, 4): np.asarray([10.0, 20.0, 30.0, 40.0, 50.0]),
        }
        train, test = p32.permuted_targets_for_fold(raw, fold, exps)
        np.testing.assert_allclose(
            train,
            np.asarray([-2.0, -20.0, -1.0, -10.0, 1.0, 10.0, 2.0, 20.0]),
        )
        np.testing.assert_allclose(test, np.asarray([0.0, 0.0]))

    def test_restricted_permutation_is_deterministic(self):
        rng = np.random.default_rng(320704)
        exps = (15, 16, 17, 18, 19)
        raw = {(11, 2): rng.normal(size=5), (11, 4): rng.normal(size=5)}
        folds = []
        for heldout_index, heldout in enumerate(exps):
            z_train = rng.normal(size=(8, 2))
            z_test = rng.normal(size=(2, 2))
            train, test = p32.permuted_targets_for_fold(raw, {
                "r": 11,
                "heldout_exp": heldout,
                "modes": [2, 4],
            }, exps)
            _, prediction, _, _ = p32.least_squares_coupling(z_train, train, z_test)
            q = 5
            folds.append({
                "r": 11,
                "heldout_exp": heldout,
                "modes": [2, 4],
                "orbit_count": q,
                "_z_train": z_train,
                "_z_test": z_test,
                "predicted_metrics": {
                    "scalar_ss": q * float(np.sum(test * test)),
                    "scalar_sse": q * float(np.sum((test - prediction) ** 2)),
                },
            })
        first = p32.restricted_permutation_null(
            folds, raw, exps, iterations=25, seed=123
        )
        second = p32.restricted_permutation_null(
            folds, raw, exps, iterations=25, seed=123
        )
        self.assertEqual(first, second)
        self.assertLess(first["maximum_denominator_invariance_error"], 1e-12)


if __name__ == "__main__":
    unittest.main()
