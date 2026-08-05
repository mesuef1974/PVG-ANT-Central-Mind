#!/usr/bin/env python3

import csv
import io
import unittest

from tools.pvg_prime_triangle_atlas import (
    build_atlas,
    generate_records,
    triangle_record,
)


class PVGPrimeTriangleAtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.primes, cls.records = generate_records(100)
        cls.index = {p: i for i, p in enumerate(cls.primes)}
        cls.by_triangle = {
            (row["p"], row["q"], row["r"]): row for row in cls.records
        }

    def test_preregistered_scope(self) -> None:
        self.assertEqual(len(self.primes), 25)
        self.assertEqual(len(self.records), 2300)
        self.assertEqual((self.records[0]["p"], self.records[0]["q"], self.records[0]["r"]), (2, 3, 5))
        self.assertEqual((self.records[-1]["p"], self.records[-1]["q"], self.records[-1]["r"]), (83, 89, 97))

    def test_ratio_composition_and_holonomy(self) -> None:
        row = self.by_triangle[(2, 3, 5)]
        self.assertEqual(row["axis_ratios"]["pq"]["text"], "3/2")
        self.assertEqual(row["axis_ratios"]["qr"]["text"], "5/3")
        self.assertEqual(row["axis_ratios"]["pr"]["text"], "5/2")
        self.assertTrue(row["ratio_composition"]["verified"])
        self.assertEqual(row["ratio_composition"]["closed_loop_holonomy"]["text"], "1/1")

    def test_normalized_gap_composition(self) -> None:
        row = self.by_triangle[(2, 3, 5)]
        self.assertEqual(row["normalized_gaps"]["pq"]["text"], "1/5")
        self.assertEqual(row["normalized_gaps"]["qr"]["text"], "1/4")
        self.assertEqual(row["normalized_gaps"]["pr"]["text"], "3/7")
        self.assertEqual(row["normalized_gap_composition"]["composed"]["text"], "3/7")
        self.assertTrue(row["normalized_gap_composition"]["verified"])

    def test_additive_gap_and_vertex_recovery(self) -> None:
        row = self.by_triangle[(11, 17, 29)]
        self.assertEqual(row["additive_gap_composition"]["pq"], 6)
        self.assertEqual(row["additive_gap_composition"]["qr"], 12)
        self.assertEqual(row["additive_gap_composition"]["pr"], 18)
        self.assertTrue(row["additive_gap_composition"]["verified"])
        self.assertEqual(row["vertex_recovery_from_pair_sums"]["p"], 11)
        self.assertEqual(row["vertex_recovery_from_pair_sums"]["q"], 17)
        self.assertEqual(row["vertex_recovery_from_pair_sums"]["r"], 29)
        self.assertTrue(row["vertex_recovery_from_pair_sums"]["verified"])

    def test_axis_two_routing_when_triangle_contains_two(self) -> None:
        row = self.by_triangle[(2, 3, 5)]
        self.assertTrue(row["axis_two_routing"]["verified"])
        for edge_name in ("pq", "pr"):
            self.assertFalse(row["edges"][edge_name]["sum"]["contains_axis_2"])
            self.assertFalse(row["edges"][edge_name]["difference"]["contains_axis_2"])
        self.assertTrue(row["edges"]["qr"]["sum"]["contains_axis_2"])
        self.assertTrue(row["edges"]["qr"]["difference"]["contains_axis_2"])

    def test_axis_two_routing_for_all_odd_triangle(self) -> None:
        row = self.by_triangle[(3, 5, 7)]
        self.assertTrue(row["axis_two_routing"]["verified"])
        for edge_name in ("pq", "qr", "pr"):
            self.assertTrue(row["edges"][edge_name]["sum"]["contains_axis_2"])
            self.assertTrue(row["edges"][edge_name]["difference"]["contains_axis_2"])

    def test_unique_all_three_difference_preserved_triangle(self) -> None:
        rows = [
            row
            for row in self.records
            if row["preservation_profile"]["difference_preserved_edge_count"] == 3
        ]
        self.assertEqual([(row["p"], row["q"], row["r"]) for row in rows], [(2, 5, 7)])
        self.assertEqual(rows[0]["preservation_profile"]["code"], "S1_D3")

    def test_unique_all_odd_two_difference_preserved_triangle(self) -> None:
        rows = [
            row
            for row in self.records
            if row["parity_class"] == "all_odd"
            and row["preservation_profile"]["difference_preserved_edge_count"] == 2
        ]
        self.assertEqual([(row["p"], row["q"], row["r"]) for row in rows], [(3, 5, 7)])

    def test_no_triangle_has_three_sum_preserved_edges(self) -> None:
        self.assertEqual(
            max(row["preservation_profile"]["sum_preserved_edge_count"] for row in self.records),
            2,
        )

    def test_exact_preservation_distributions(self) -> None:
        _, _, summary = build_atlas(100)
        self.assertEqual(
            summary["finite_counts"]["sum_preserved_edge_count_distribution"],
            {"0": 2144, "1": 128, "2": 28},
        )
        self.assertEqual(
            summary["finite_counts"]["difference_preserved_edge_count_distribution"],
            {"0": 1969, "1": 295, "2": 35, "3": 1},
        )
        self.assertEqual(summary["finite_counts"]["triangles_with_two_sum_preserved_edges"], 28)
        self.assertEqual(
            summary["finite_counts"]["triangles_containing_the_unique_double_preserved_edge_2_5"],
            23,
        )

    def test_exact_profile_distribution(self) -> None:
        _, _, summary = build_atlas(100)
        self.assertEqual(
            summary["finite_counts"]["preservation_profile_distribution"],
            {
                "S0_D0": 1885,
                "S0_D1": 237,
                "S0_D2": 22,
                "S1_D0": 63,
                "S1_D1": 52,
                "S1_D2": 12,
                "S1_D3": 1,
                "S2_D0": 21,
                "S2_D1": 6,
                "S2_D2": 1,
            },
        )

    def test_all_global_verifications_pass(self) -> None:
        _, _, summary = build_atlas(100)
        self.assertTrue(all(summary["verification"].values()))
        self.assertEqual(
            summary["distinguished_triangles"]["all_three_difference_preserved"],
            [[2, 5, 7]],
        )
        self.assertEqual(
            summary["distinguished_triangles"]["all_odd_two_difference_preserved"],
            [[3, 5, 7]],
        )

    def test_csv_is_deterministic_and_complete(self) -> None:
        csv_one, summary_one, _ = build_atlas(100)
        csv_two, summary_two, _ = build_atlas(100)
        self.assertEqual(csv_one, csv_two)
        self.assertEqual(summary_one, summary_two)
        rows = list(csv.DictReader(io.StringIO(csv_one)))
        self.assertEqual(len(rows), 2300)
        self.assertEqual((rows[0]["p"], rows[0]["q"], rows[0]["r"]), ("2", "3", "5"))
        self.assertEqual(rows[0]["profile"], "S2_D2")

    def test_invalid_triangle_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            triangle_record(2, 3, 9, prime_indices={2: 0, 3: 1, 9: 2}, record_id=1)
        with self.assertRaises(ValueError):
            triangle_record(5, 3, 7, prime_indices={3: 0, 5: 1, 7: 2}, record_id=1)


if __name__ == "__main__":
    unittest.main()
