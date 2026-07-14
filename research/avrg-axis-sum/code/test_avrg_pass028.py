import unittest

import numpy as np

import avrg_pass028 as p28


class Pass028Tests(unittest.TestCase):
    def test_locked_full_rows(self):
        rows = p28.load_full_rows(
            p28.default_pass023_path(), p28.default_pass025_holdout_path()
        )
        self.assertEqual(len(rows), 160)
        self.assertEqual(sorted({row["exp"] for row in rows}), list(p28.EXPS))
        self.assertEqual(
            sorted({row["r"] for row in rows}), list(p28.PRIMARY_MODULI)
        )

    def test_splitmix_order_is_deterministic_permutation(self):
        values = np.arange(100, 300, 2, dtype=np.int64)
        first = p28.splitmix64_order(values, 17, 13)
        second = p28.splitmix64_order(values, 17, 13)
        np.testing.assert_array_equal(first, second)
        np.testing.assert_array_equal(np.sort(first), np.arange(len(values)))

    def test_coverage_prefixes_are_nested(self):
        values = np.arange(1000, 3000, 2, dtype=np.int64)
        order = p28.splitmix64_order(values, 18, 19)
        previous = set()
        for numerator, denominator in p28.COVERAGE_LADDER:
            count = p28.coverage_count(len(values), numerator, denominator)
            current = set(int(index) for index in order[:count])
            self.assertTrue(previous <= current)
            previous = current
        self.assertEqual(len(previous), len(values))

    def test_matrix_decomposition_closes_pointwise(self):
        r = 11
        rng = np.random.default_rng(280711)
        f_matrix = rng.uniform(0.0, 4.0, size=(r, 23))
        f_matrix[0] = 0.0
        character = p28.character_on_residues(r, 2)
        normalization = rng.uniform(1.0, 3.0, size=23)
        parts = p28.decompose_f_matrix(f_matrix, character, normalization)
        reconstructed = parts["zero_values"] + sum(parts["orbit_values"].values())
        np.testing.assert_allclose(
            reconstructed, parts["total_values"], atol=1e-12, rtol=1e-12
        )
        self.assertLess(parts["maximum_pointwise_closure_error"], 1e-12)

    def test_zero_channel_is_character_independent(self):
        r = 13
        rng = np.random.default_rng(280712)
        f_matrix = rng.uniform(0.0, 2.0, size=(r, 17))
        f_matrix[0] = 0.0
        normalization = np.ones(17)
        first = p28.decompose_f_matrix(
            f_matrix, p28.character_on_residues(r, 2), normalization
        )
        second = p28.decompose_f_matrix(
            f_matrix, p28.character_on_residues(r, 4), normalization
        )
        np.testing.assert_allclose(first["zero_values"], second["zero_values"])

    def test_linear_attribution_identity(self):
        components = {
            1: [-1.0, 0.0, 1.0, 0.5],
            2: [0.3, -0.2, 0.1, -0.4],
            3: [0.1, 0.2, -0.2, 0.3],
        }
        y = [sum(components[b][i] for b in components) for i in range(4)]
        result = p28.linear_attribution(y, components)
        self.assertAlmostEqual(result["signed_share_sum"], 1.0, places=12)
        self.assertAlmostEqual(
            sum(row["absolute_fraction"] for row in result["orbits"]),
            1.0,
            places=12,
        )


if __name__ == "__main__":
    unittest.main()
