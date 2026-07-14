import unittest

import numpy as np

import avrg_pass024 as p24


class Pass024Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.input_path = p24.default_input_path()
        cls.rows = p24.load_locked_rows(cls.input_path)

    def test_locked_input_and_centering(self):
        decomposition = p24.build_decomposition(self.rows)
        self.assertEqual(len(self.rows), 136)
        for matrix in decomposition["matrices"].values():
            np.testing.assert_allclose(matrix.sum(axis=1), 0.0, atol=1e-12)

    def test_persistent_identity(self):
        matrix = np.array(
            [
                [-1.0, 0.0, 1.0],
                [-0.8, -0.1, 0.9],
                [-1.1, 0.2, 0.9],
                [-0.9, -0.1, 1.0],
            ]
        )
        result = p24.persistent_components(matrix)
        self.assertAlmostEqual(
            result["total_ss"],
            result["persistent_ss"] + result["residual_ss"],
            places=13,
        )
        self.assertGreater(result["persistence_fraction"], 0.9)

    def test_holm_adjustment_is_monotone_in_sorted_order(self):
        adjusted = p24.holm_adjust([(11, 0.01), (13, 0.03), (17, 0.02)])
        self.assertAlmostEqual(adjusted[11], 0.03)
        self.assertAlmostEqual(adjusted[17], 0.04)
        self.assertAlmostEqual(adjusted[13], 0.04)

    def test_permutation_is_deterministic(self):
        matrix = np.array(
            [
                [-1.0, 0.0, 1.0],
                [-0.8, -0.1, 0.9],
                [-1.1, 0.2, 0.9],
                [-0.9, -0.1, 1.0],
            ]
        )
        left = p24.permutation_distribution(matrix, 100, np.random.default_rng(240724))
        right = p24.permutation_distribution(matrix, 100, np.random.default_rng(240724))
        np.testing.assert_array_equal(left, right)

    def test_real_analysis_reduced_permutations(self):
        result = p24.analyze(
            self.rows,
            global_permutations=300,
            per_modulus_permutations=200,
            seed=240724,
        )
        global_result = result["character_channel"]["global"]
        self.assertGreaterEqual(global_result["persistence_fraction"], 0.0)
        self.assertLessEqual(global_result["persistence_fraction"], 1.0)
        self.assertIn(global_result["decision_passed"], (True, False))
        channels = result["sum_of_squares_channels"]
        self.assertAlmostEqual(
            channels["total_ss"],
            channels["modulus_mean_ss"] + channels["within_modulus_character_ss"],
            places=11,
        )


if __name__ == "__main__":
    unittest.main()
