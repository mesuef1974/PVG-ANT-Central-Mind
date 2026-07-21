#!/usr/bin/env python3

import csv
import io
import unittest

from tools.pvg_prime_triangle_dynamics import (
    build_atlas,
    difference_chain,
    dynamics_record,
    generate_records,
    recover_from_sums,
)


class PVGPrimeTriangleDynamicsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.primes, cls.records = generate_records(100)
        cls.by_source = {tuple(row["source"]): row for row in cls.records}

    def test_registered_scope(self) -> None:
        self.assertEqual(len(self.primes), 25)
        self.assertEqual(len(self.records), 2300)

    def test_difference_relation(self) -> None:
        row = self.by_source[(11, 17, 29)]
        self.assertEqual(row["difference_transform"]["labeled"], [6, 12, 18])
        self.assertEqual(row["difference_transform"]["primitive_shape"], [1, 2, 3])
        self.assertTrue(row["difference_transform"]["relation_verified"])

    def test_difference_transform_loses_translation(self) -> None:
        self.assertEqual(
            self.by_source[(3, 5, 11)]["difference_transform"]["labeled"],
            self.by_source[(5, 7, 13)]["difference_transform"]["labeled"],
        )
        self.assertFalse(
            self.by_source[(3, 5, 11)]["difference_transform"][
                "absolute_position_recoverable_without_anchor"
            ]
        )

    def test_sum_transform_is_injective(self) -> None:
        row = self.by_source[(11, 17, 29)]
        self.assertEqual(row["sum_transform"]["labeled"], [28, 46, 40])
        self.assertEqual(row["sum_transform"]["recovered_source"], [11, 17, 29])
        self.assertTrue(row["sum_transform"]["recovery_verified"])
        self.assertEqual(recover_from_sums((28, 46, 40)), (11, 17, 29))

    def test_sum_gcd_routing(self) -> None:
        self.assertEqual(self.by_source[(3, 5, 7)]["sum_transform"]["gcd"], 2)
        self.assertEqual(self.by_source[(2, 5, 7)]["sum_transform"]["gcd"], 1)
        self.assertTrue(
            all(row["support_routing"]["sum_common_gcd_verified"] for row in self.records)
        )

    def test_unique_prime_difference_triangle(self) -> None:
        rows = [
            row
            for row in self.records
            if row["difference_transform"]["is_distinct_prime_triangle"]
        ]
        self.assertEqual([row["source"] for row in rows], [[2, 5, 7]])
        self.assertEqual(
            rows[0]["difference_transform"]["prime_triangle_target"], [2, 3, 5]
        )

    def test_unique_prime_chain_terminates(self) -> None:
        chain = difference_chain(2, 5, 7)
        self.assertEqual(chain[0]["prime_triangle_target"], [2, 3, 5])
        self.assertEqual(chain[1]["raw_difference_triple"], [1, 2, 3])
        self.assertIsNone(chain[1]["prime_triangle_target"])

    def test_no_sum_transform_is_prime_triangle(self) -> None:
        self.assertFalse(
            any(row["sum_transform"]["is_distinct_prime_triangle"] for row in self.records)
        )

    def test_exact_prime_count_distributions(self) -> None:
        _, _, summary = build_atlas(100)
        self.assertEqual(
            summary["finite_counts"]["difference_prime_count_distribution"],
            {"0": 1969, "1": 295, "2": 35, "3": 1},
        )
        self.assertEqual(
            summary["finite_counts"]["sum_prime_count_distribution"],
            {"0": 2144, "1": 128, "2": 28},
        )

    def test_exact_sum_gcd_distribution(self) -> None:
        _, _, summary = build_atlas(100)
        self.assertEqual(
            summary["finite_counts"]["sum_gcd_distribution"],
            {"1": 276, "2": 2024},
        )

    def test_all_verifications_pass(self) -> None:
        _, _, summary = build_atlas(100)
        self.assertTrue(all(summary["verification"].values()))
        self.assertEqual(summary["finite_counts"]["prime_difference_triangle_count"], 1)
        self.assertEqual(summary["finite_counts"]["detected_cycle_count"], 0)

    def test_csv_is_deterministic(self) -> None:
        csv_one, summary_one, _ = build_atlas(100)
        csv_two, summary_two, _ = build_atlas(100)
        self.assertEqual(csv_one, csv_two)
        self.assertEqual(summary_one, summary_two)
        rows = list(csv.DictReader(io.StringIO(csv_one)))
        self.assertEqual(len(rows), 2300)
        self.assertEqual((rows[0]["p"], rows[0]["q"], rows[0]["r"]), ("2", "3", "5"))

    def test_invalid_source_rejected(self) -> None:
        with self.assertRaises(ValueError):
            dynamics_record(2, 3, 9, 1)
        with self.assertRaises(ValueError):
            dynamics_record(5, 3, 7, 1)


if __name__ == "__main__":
    unittest.main()
