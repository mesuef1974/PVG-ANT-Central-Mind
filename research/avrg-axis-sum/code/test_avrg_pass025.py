import unittest

import numpy as np

import avrg_pass025 as p25


class Pass025Tests(unittest.TestCase):
    def test_phase_is_conjugacy_invariant(self):
        for r in p25.PRIMARY_MODULI:
            for k in range(2, r - 1, 2):
                left = p25.raw_phase(r, k, 19)
                right = p25.raw_phase(r, r - 1 - k, 19)
                self.assertAlmostEqual(left, right, places=12)

    def test_centered_phase_sums_to_zero(self):
        for r in p25.PRIMARY_MODULI:
            modes = [k for k in range(2, r - 1, 2) if k <= r - 1 - k]
            for exp in (*p25.TRAIN_EXPS, p25.HOLDOUT_EXP):
                self.assertAlmostEqual(
                    float(p25.centered_phase(r, modes, exp).sum()), 0.0, places=12
                )

    def test_training_input_is_locked(self):
        rows = p25.load_training(p25.default_training_path())
        self.assertEqual(len(rows), 136)
        self.assertEqual(sorted({row["exp"] for row in rows}), list(p25.TRAIN_EXPS))

    def test_permutation_is_deterministic(self):
        target = np.array([-1.0, 0.2, 0.8])
        prediction = np.array([-0.8, 0.1, 0.7])
        left = p25.improvement_distribution(
            target, prediction, 200, np.random.default_rng(250719)
        )
        right = p25.improvement_distribution(
            target, prediction, 200, np.random.default_rng(250719)
        )
        np.testing.assert_array_equal(left, right)

    def test_synthetic_phase_fit_recovers_coefficient(self):
        r = 13
        modes = [2, 4, 6]
        beta = 0.75
        training_rows = []
        for exp in p25.TRAIN_EXPS:
            centered = beta * p25.centered_phase(r, modes, exp)
            for k, value in zip(modes, centered):
                training_rows.append(
                    {"exp": exp, "r": r, "k": k, "rho": 2.0 + float(value)}
                )
        holdout_centered = beta * p25.centered_phase(r, modes, p25.HOLDOUT_EXP)
        holdout_rows = [
            {"exp": p25.HOLDOUT_EXP, "r": r, "k": k, "rho": 2.0 + float(value)}
            for k, value in zip(modes, holdout_centered)
        ]
        fitted = p25.fit_modulus(training_rows, holdout_rows, r, modes)
        self.assertAlmostEqual(fitted["beta"], beta, places=12)
        self.assertAlmostEqual(fitted["phase_sse"], 0.0, places=12)
        self.assertGreater(fitted["phase_skill_vs_zero"], 0.999999)

    def test_holm_adjustment(self):
        adjusted = p25.holm_adjust([(11, 0.01), (13, 0.03), (17, 0.02)])
        self.assertAlmostEqual(adjusted[11], 0.03)
        self.assertAlmostEqual(adjusted[17], 0.04)
        self.assertAlmostEqual(adjusted[13], 0.04)


if __name__ == "__main__":
    unittest.main()
