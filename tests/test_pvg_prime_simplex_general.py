#!/usr/bin/env python3

import unittest
from fractions import Fraction
from math import comb

from tools.pvg_prime_simplex import (
    SimplexInputError,
    all_pair_sums,
    analyze,
    compose_normalized_gaps,
    face_counts,
    normalized_gap,
    path_ratio,
    reconstruct_from_anchor,
    reconstruct_from_labeled_pair_sums,
    validate_vertices,
)


class PrimeSimplexGeneralTests(unittest.TestCase):
    def test_validate_vertices(self) -> None:
        self.assertEqual(validate_vertices([2, 3, 5]), (2, 3, 5))
        with self.assertRaises(SimplexInputError):
            validate_vertices([3])
        with self.assertRaises(SimplexInputError):
            validate_vertices([3, 2])
        with self.assertRaises(SimplexInputError):
            validate_vertices([2, 2, 3])
        with self.assertRaises(SimplexInputError):
            validate_vertices([2, 3, 9])

    def test_face_counts(self) -> None:
        self.assertEqual(face_counts(4), {"0": 4, "1": 6, "2": 4, "3": 1})
        for m in range(2, 9):
            counts = face_counts(m)
            self.assertEqual(sum(counts.values()), 2**m - 1)
            self.assertEqual(counts["1"], comb(m, 2))

    def test_anchor_and_gap_reconstruction(self) -> None:
        self.assertEqual(reconstruct_from_anchor(2, [1, 2, 2]), (2, 3, 5, 7))
        with self.assertRaises(SimplexInputError):
            reconstruct_from_anchor(2, [1, 0])

    def test_pair_sum_reconstruction_triangle(self) -> None:
        p = (11, 17, 29)
        self.assertEqual(reconstruct_from_labeled_pair_sums(3, all_pair_sums(p)), p)

    def test_pair_sum_reconstruction_tetrahedron(self) -> None:
        p = (2, 5, 7, 13)
        self.assertEqual(reconstruct_from_labeled_pair_sums(4, all_pair_sums(p)), p)

    def test_pair_sum_reconstruction_five_vertices(self) -> None:
        p = (3, 5, 11, 17, 29)
        self.assertEqual(reconstruct_from_labeled_pair_sums(5, all_pair_sums(p)), p)

    def test_pair_sum_reconstruction_not_available_for_edge(self) -> None:
        with self.assertRaises(SimplexInputError):
            reconstruct_from_labeled_pair_sums(2, {(0, 1): 5})

    def test_path_independence(self) -> None:
        p = (2, 3, 5, 7, 11)
        self.assertEqual(path_ratio(p, [0, 1, 2, 3, 4]), Fraction(11, 2))
        self.assertEqual(path_ratio(p, [0, 2, 4]), Fraction(11, 2))
        self.assertEqual(path_ratio(p, [0, 3, 1, 4]), Fraction(11, 2))

    def test_normalized_gap_composition(self) -> None:
        a, b, c = 3, 11, 29
        self.assertEqual(
            compose_normalized_gaps(normalized_gap(a, b), normalized_gap(b, c)),
            normalized_gap(a, c),
        )

    def test_pair_sum_gcd_rule(self) -> None:
        self.assertEqual(analyze([3, 5, 7, 11])["pair_sum_gcd"], 2)
        self.assertEqual(analyze([2, 3, 5, 7])["pair_sum_gcd"], 1)

    def test_pair_sum_gcd_rule_boundary_at_edge(self) -> None:
        report = analyze([2, 3])
        self.assertEqual(report["pair_sum_gcd"], 5)
        self.assertFalse(report["pair_sum_gcd_rule_available"])
        self.assertIsNone(report["expected_pair_sum_gcd"])
        self.assertTrue(report["verification"]["pair_sum_gcd_rule_for_m_ge_3"])

    def test_axis_two_routing(self) -> None:
        odd = analyze([3, 5, 7, 11, 13])
        self.assertEqual(odd["axis_2_transition_routing"]["containing_axis_2"], 20)
        self.assertEqual(odd["axis_2_transition_routing"]["excluding_axis_2"], 0)

        with_two = analyze([2, 3, 5, 7, 11])
        self.assertEqual(with_two["axis_2_transition_routing"]["containing_axis_2"], 12)
        self.assertEqual(with_two["axis_2_transition_routing"]["excluding_axis_2"], 8)

    def test_sum_preservation_upper_bound(self) -> None:
        report = analyze([2, 3, 5, 11, 17, 29])
        self.assertLessEqual(report["sum_preserved_edge_count"], 5)
        self.assertTrue(report["sum_bound_verified"])

    def test_dimensions_and_degrees(self) -> None:
        for vertices in ([2, 3], [2, 3, 5], [2, 3, 5, 7], [2, 3, 5, 7, 11]):
            report = analyze(vertices)
            m = len(vertices)
            self.assertEqual(report["dimension"], m - 1)
            self.assertEqual(report["root_lattice"], f"A_{m-1}")
            self.assertEqual(report["edge_count"], comb(m, 2))
            self.assertEqual(report["ordered_horizontal_neighbor_degree_at_interior"], m * (m - 1))
            self.assertTrue(all(report["verification"].values()))


if __name__ == "__main__":
    unittest.main()
