import unittest

import numpy as np

import avrg_pass027 as p27


class Pass027Tests(unittest.TestCase):
    def test_locked_full_rows(self):
        rows = p27.load_full_rows(
            p27.default_pass023_path(), p27.default_pass025_holdout_path()
        )
        self.assertEqual(len(rows), 160)
        self.assertEqual(sorted({row["exp"] for row in rows}), list(p27.EXPS))
        self.assertEqual(
            sorted({row["r"] for row in rows}), list(p27.PRIMARY_MODULI)
        )

    def test_on_selection_is_deterministic_and_valid(self):
        first = p27.choose_on_values(15, 31)
        second = p27.choose_on_values(15, 31)
        np.testing.assert_array_equal(first, second)
        self.assertEqual(len(first), p27.SAMPLE_COUNT)
        self.assertTrue(np.all(first % (2 * 31) == 0))
        self.assertTrue(np.all(first >= 2**15))
        self.assertTrue(np.all(first < 2**16))

    def test_residue_decomposition_closes(self):
        r = 11
        f = np.asarray([0.0, 2.0, 1.0, 3.0, 5.0, 0.5, 4.0, 1.5, 2.5, 3.5, 0.75])
        character = p27.character_on_residues(r, 2)
        parts = p27.residue_components(f, character)
        self.assertAlmostEqual(parts["closure_error"], 0.0, places=11)
        self.assertAlmostEqual(parts["zero_identity_error"], 0.0, places=11)
        self.assertAlmostEqual(
            parts["zero"] + sum(parts["orbits"].values()),
            parts["total"],
            places=11,
        )

    def test_zero_residue_is_character_independent(self):
        r = 13
        f = np.linspace(0.0, 3.0, r)
        zero_two = p27.residue_components(
            f, p27.character_on_residues(r, 2)
        )["zero"]
        zero_four = p27.residue_components(
            f, p27.character_on_residues(r, 4)
        )["zero"]
        self.assertAlmostEqual(zero_two, zero_four, places=12)
        self.assertAlmostEqual(zero_two, float(np.sum(f[1:] ** 2)), places=12)

    def test_linear_attribution_identity(self):
        components = {
            1: [-1.0, 0.0, 1.0, 0.5],
            2: [0.3, -0.2, 0.1, -0.4],
            3: [0.1, 0.2, -0.2, 0.3],
        }
        y = [sum(components[b][i] for b in components) for i in range(4)]
        result = p27.linear_attribution(y, components)
        self.assertAlmostEqual(result["signed_share_sum"], 1.0, places=12)
        self.assertAlmostEqual(
            sum(row["absolute_fraction"] for row in result["orbits"]),
            1.0,
            places=12,
        )

    def test_single_component_gets_all_attribution(self):
        y = [-1.0, -0.25, 0.5, 0.75]
        result = p27.linear_attribution(y, {4: y})
        self.assertEqual(result["top_orbit_b"], 4)
        self.assertAlmostEqual(result["top_absolute_fraction"], 1.0)
        self.assertAlmostEqual(result["signed_share_sum"], 1.0)


if __name__ == "__main__":
    unittest.main()
