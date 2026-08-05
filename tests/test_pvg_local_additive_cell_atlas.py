from __future__ import annotations

import unittest

from tools.pvg_local_additive_cell_atlas import analyze, analyze_pair


class PVGLocalAdditiveCellAtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.atlas = analyze(100)

    def test_registered_scope(self) -> None:
        self.assertEqual(self.atlas["prime_count"], 25)
        self.assertEqual(self.atlas["cell_count"], 300)

    def test_two_three_pascal_cell(self) -> None:
        cell = analyze_pair(2, 3)
        self.assertTrue(cell["pascal_cell_closed"])
        self.assertEqual(cell["sum"], 5)
        self.assertEqual(cell["sum_identity"], "2g + 3g = 5g")

    def test_three_five_sum_leaves_prime_axis_class(self) -> None:
        cell = analyze_pair(3, 5)
        self.assertFalse(cell["pascal_cell_closed"])
        self.assertEqual(cell["sum"], 8)
        self.assertEqual(cell["sum_destination_axes"], [2])
        self.assertEqual(cell["sum_Omega"], 3)

    def test_closed_cells_are_exactly_registered_twin_prime_triples(self) -> None:
        self.assertEqual(
            self.atlas["closed_pascal_triples"],
            [[2, 3, 5], [2, 5, 7], [2, 11, 13], [2, 17, 19], [2, 29, 31], [2, 41, 43], [2, 59, 61], [2, 71, 73]],
        )
        self.assertEqual(self.atlas["closed_pascal_cell_count"], 8)

    def test_difference_prime_count(self) -> None:
        self.assertEqual(self.atlas["difference_prime_cell_count"], 16)

    def test_unique_double_preservation_pair(self) -> None:
        self.assertEqual(self.atlas["double_preservation_count"], 1)
        self.assertEqual(self.atlas["double_preservation_pairs"], [[2, 5]])

    def test_exact_Omega_distributions(self) -> None:
        self.assertEqual(self.atlas["sum_Omega_distribution"], {1: 8, 2: 57, 3: 96, 4: 81, 5: 40, 6: 16, 7: 2})
        self.assertEqual(self.atlas["difference_Omega_distribution"], {0: 1, 1: 16, 2: 95, 3: 107, 4: 61, 5: 17, 6: 3})

    def test_exact_support_distributions(self) -> None:
        self.assertEqual(self.atlas["sum_support_size_distribution"], {1: 24, 2: 171, 3: 105})
        self.assertEqual(self.atlas["difference_support_size_distribution"], {0: 1, 1: 52, 2: 203, 3: 44})

    def test_all_verifications(self) -> None:
        self.assertTrue(all(self.atlas["verification"].values()))

    def test_invalid_pair_rejected(self) -> None:
        with self.assertRaises(ValueError):
            analyze_pair(3, 3)
        with self.assertRaises(ValueError):
            analyze_pair(4, 5)


if __name__ == "__main__":
    unittest.main()
