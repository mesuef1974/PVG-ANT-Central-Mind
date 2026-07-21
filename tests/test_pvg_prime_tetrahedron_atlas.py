#!/usr/bin/env python3

import csv
import io
import unittest

from tools.pvg_prime_tetrahedron_atlas import (
    build_atlas,
    generate_records,
    tetrahedron_record,
)


class PVGPrimeTetrahedronAtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.primes, cls.records = generate_records(100)
        cls.index = {p: i for i, p in enumerate(cls.primes)}
        cls.by_vertices = {tuple(row["vertices"]): row for row in cls.records}

    def test_preregistered_scope(self) -> None:
        self.assertEqual(len(self.primes), 25)
        self.assertEqual(len(self.records), 12650)
        self.assertEqual(self.records[0]["vertices"], [2, 3, 5, 7])
        self.assertEqual(self.records[-1]["vertices"], [79, 83, 89, 97])

    def test_path_independence_and_face_holonomy(self) -> None:
        row = self.by_vertices[(2, 3, 5, 7)]
        self.assertTrue(row["path_independence"]["verified"])
        self.assertEqual(row["path_independence"]["direct"], "7/2")
        self.assertTrue(all(face["verified"] for face in row["face_holonomies"]))
        self.assertEqual(len(row["face_holonomies"]), 4)

    def test_gap_composition(self) -> None:
        row = self.by_vertices[(11, 17, 29, 41)]
        self.assertEqual(row["consecutive_gaps"], [6, 12, 12])
        self.assertTrue(all(row["gap_composition"].values()))
        self.assertEqual(row["pair_differences"]["11_41"], 30)

    def test_vertex_recovery_from_six_pair_sums(self) -> None:
        row = self.by_vertices[(11, 17, 29, 41)]
        self.assertEqual(row["sum_transform"]["recovered_vertices"], [11, 17, 29, 41])
        self.assertEqual(row["sum_transform"]["vertex_sum"], 98)
        self.assertTrue(row["sum_transform"]["recovery_verified"])

    def test_pair_sum_gcd_rule(self) -> None:
        self.assertEqual(self.by_vertices[(2, 3, 5, 7)]["sum_transform"]["gcd"], 1)
        self.assertEqual(self.by_vertices[(3, 5, 7, 11)]["sum_transform"]["gcd"], 2)

    def test_axis_two_routing(self) -> None:
        for vertices in ((2, 3, 5, 7), (3, 5, 7, 11)):
            row = self.by_vertices[vertices]
            self.assertTrue(row["axis_two_routing"]["verified"])
            for check in row["axis_two_routing"]["checks"]:
                expected = check["edge"][0] != 2
                self.assertEqual(check["sum_contains_2"], expected)
                self.assertEqual(check["difference_contains_2"], expected)

    def test_exact_finite_distributions(self) -> None:
        _, _, summary = build_atlas(100)
        self.assertEqual(
            summary["finite_counts"]["sum_preserved_edge_count_distribution"],
            {"0": 11186, "1": 960, "2": 448, "3": 56},
        )
        self.assertEqual(
            summary["finite_counts"]["difference_preserved_edge_count_distribution"],
            {"0": 9386, "1": 2607, "2": 537, "3": 113, "4": 7},
        )
        self.assertEqual(summary["finite_counts"]["contains_axis_2"], 2024)
        self.assertEqual(summary["finite_counts"]["all_odd"], 10626)

    def test_maximum_difference_preservation(self) -> None:
        _, _, summary = build_atlas(100)
        self.assertEqual(summary["finite_counts"]["maximum_difference_preserved_edges_observed"], 4)
        self.assertEqual(
            summary["distinguished_tetrahedra"]["maximum_difference_preservation"],
            [
                [2, 3, 5, 7],
                [2, 5, 7, 13],
                [2, 5, 7, 19],
                [2, 5, 7, 31],
                [2, 5, 7, 43],
                [2, 5, 7, 61],
                [2, 5, 7, 73],
            ],
        )

    def test_maximum_sum_preservation(self) -> None:
        _, _, summary = build_atlas(100)
        self.assertEqual(summary["finite_counts"]["maximum_sum_preserved_edges"], 3)
        self.assertEqual(summary["distinguished_tetrahedra"]["maximum_sum_preservation_count"], 56)

    def test_all_verifications_pass(self) -> None:
        _, _, summary = build_atlas(100)
        self.assertTrue(all(summary["verification"].values()))

    def test_csv_is_deterministic(self) -> None:
        csv_one, summary_one, _ = build_atlas(100)
        csv_two, summary_two, _ = build_atlas(100)
        self.assertEqual(csv_one, csv_two)
        self.assertEqual(summary_one, summary_two)
        rows = list(csv.DictReader(io.StringIO(csv_one)))
        self.assertEqual(len(rows), 12650)
        self.assertEqual((rows[0]["p"], rows[0]["q"], rows[0]["r"], rows[0]["s"]), ("2", "3", "5", "7"))

    def test_invalid_tetrahedron_rejected(self) -> None:
        with self.assertRaises(ValueError):
            tetrahedron_record((2, 3, 5, 9), prime_indices={2: 0, 3: 1, 5: 2, 9: 3}, record_id=1)
        with self.assertRaises(ValueError):
            tetrahedron_record((2, 5, 3, 7), prime_indices={2: 0, 3: 1, 5: 2, 7: 3}, record_id=1)


if __name__ == "__main__":
    unittest.main()
