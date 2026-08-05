#!/usr/bin/env python3

import unittest

from tools.pvg_local_neighborhood import (
    analyze,
    geometric_triplet,
    horizontal_distance,
    local_geometry,
)


class PVGLocalNeighborhoodTests(unittest.TestCase):
    def test_two_three_face_at_six(self) -> None:
        report = local_geometry(6, {2: 1, 3: 1}, source="test", steps=3)
        self.assertEqual(report["horizontal_root_lattice"], "A_1")
        self.assertEqual(report["ordered_horizontal_degree"], 2)
        self.assertEqual(
            {row["neighbor"] for row in report["primitive_horizontal_neighbors"]},
            {4, 9},
        )
        line = report["pair_lines_through_point"][0]
        self.assertEqual([term["value"] for term in line["terms"]], [4, 6, 9])
        self.assertEqual(line["ratio"]["text"], "3/2")

    def test_two_five_face_at_ten(self) -> None:
        report = local_geometry(10, {2: 1, 5: 1}, source="test")
        line = report["pair_lines_through_point"][0]
        self.assertEqual([term["value"] for term in line["terms"]], [4, 10, 25])
        self.assertEqual(line["ratio"]["text"], "5/2")

    def test_three_seven_face_at_twenty_one(self) -> None:
        report = local_geometry(21, {3: 1, 7: 1}, source="test")
        line = report["pair_lines_through_point"][0]
        self.assertEqual([term["value"] for term in line["terms"]], [9, 21, 49])
        self.assertEqual(line["ratio"]["text"], "7/3")

    def test_three_axis_face_at_thirty(self) -> None:
        report = local_geometry(30, {2: 1, 3: 1, 5: 1}, source="test")
        self.assertEqual(report["horizontal_root_lattice"], "A_2")
        self.assertEqual(report["ordered_horizontal_degree"], 6)
        self.assertEqual(
            {row["neighbor"] for row in report["primitive_horizontal_neighbors"]},
            {12, 18, 20, 45, 50, 75},
        )
        self.assertEqual(
            {row["vertex"] for row in report["horizontal_simplex_vertices"]},
            {8, 27, 125},
        )

    def test_all_primitive_neighbors_preserve_Omega(self) -> None:
        report = local_geometry(360, {2: 3, 3: 2, 5: 1}, source="test")
        self.assertTrue(
            all(row["level_preserved"] for row in report["primitive_horizontal_neighbors"])
        )
        self.assertEqual(report["ordered_horizontal_degree"], 6)

    def test_adjacent_gcd_recovers_axis_pair(self) -> None:
        report = local_geometry(10403, {101: 1, 103: 1}, source="test")
        rows = {
            row["neighbor"]: row for row in report["primitive_horizontal_neighbors"]
        }
        left = rows[10201]["gcd_recovery"]
        right = rows[10609]["gcd_recovery"]
        self.assertEqual(
            {left["input_over_gcd"], left["neighbor_over_gcd"]}, {101, 103}
        )
        self.assertEqual(
            {right["input_over_gcd"], right["neighbor_over_gcd"]}, {101, 103}
        )

    def test_horizontal_distance_in_three_axis_face(self) -> None:
        self.assertEqual(
            horizontal_distance({2: 2, 3: 1}, {3: 1, 5: 2}),
            2,
        )
        with self.assertRaises(Exception):
            horizontal_distance({2: 1}, {3: 2})

    def test_geometric_midpoint_identity(self) -> None:
        report = geometric_triplet(10201, 10403, 10609)
        self.assertTrue(report["is_geometric"])
        self.assertEqual(report["ratio_left_to_middle"]["text"], "103/101")
        self.assertEqual(report["ratio_middle_to_right"]["text"], "103/101")
        self.assertFalse(geometric_triplet(4, 6, 10)["is_geometric"])

    def test_axis_ratio_cocycle(self) -> None:
        report = local_geometry(30, {2: 1, 3: 1, 5: 1}, source="test")
        ratios = {
            (row["donor_axis"], row["recipient_axis"]): (
                row["ratio"]["numerator"],
                row["ratio"]["denominator"],
            )
            for row in report["axis_ratio_matrix"]
        }
        self.assertEqual(ratios[(2, 3)], (3, 2))
        self.assertEqual(ratios[(3, 5)], (5, 3))
        self.assertEqual(ratios[(2, 5)], (5, 2))

    def test_automatic_analysis_of_10403(self) -> None:
        report = analyze(10403, steps=2)
        self.assertEqual(report["support"], [101, 103])
        self.assertEqual(report["Omega"], 2)
        self.assertEqual(
            [row["vertex"] for row in report["horizontal_simplex_vertices"]],
            [10201, 10609],
        )

    def test_primitive_ray_and_axis_sequences(self) -> None:
        report = local_geometry(36, {2: 2, 3: 2}, source="test", steps=3)
        ray = report["primitive_composite_ray"]
        self.assertEqual(ray["primitive_generator"], 6)
        self.assertEqual(ray["ray_index_of_input"], 2)
        self.assertEqual(ray["sequence"], [1, 6, 36, 216])
        sequences = {row["axis"]: row["sequence"] for row in report["axis_parallel_sequences"]}
        self.assertEqual(sequences[2], [36, 72, 144, 288])
        self.assertEqual(sequences[3], [36, 108, 324, 972])


if __name__ == "__main__":
    unittest.main()
