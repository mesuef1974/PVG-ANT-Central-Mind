#!/usr/bin/env python3

import unittest

from tools.pvg_prime_pair_edge_atlas import (
    build_atlas,
    edge_record,
    generate_records,
    is_prime,
    summarize,
)


class PVGPrimePairEdgeAtlasTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.primes, cls.records = generate_records(100)
        cls.by_pair = {(row["p"], row["q"]): row for row in cls.records}
        cls.summary = summarize(100, cls.primes, cls.records)

    def test_preregistered_scope(self) -> None:
        self.assertEqual(len(self.primes), 25)
        self.assertEqual(self.primes[0], 2)
        self.assertEqual(self.primes[-1], 97)
        self.assertEqual(len(self.records), 300)

    def test_two_three_edge(self) -> None:
        row = self.by_pair[(2, 3)]
        self.assertEqual(row["axis_ratio"]["text"], "3/2")
        self.assertEqual(row["sum_transition"]["factorization_text"], "5")
        self.assertEqual(row["sum_transition"]["kappa"], 0)
        self.assertEqual(row["difference_transition"]["factorization_text"], "1")
        self.assertEqual(row["difference_transition"]["kappa"], -1)

    def test_two_five_unique_double_preservation(self) -> None:
        row = self.by_pair[(2, 5)]
        self.assertTrue(row["both_level_preserved"])
        self.assertEqual(row["sum_transition"]["value"], 7)
        self.assertEqual(row["difference_transition"]["value"], 3)
        self.assertEqual(
            self.summary["distinguished_pairs"]["both_level_preserved"], [[2, 5]]
        )

    def test_three_seven_transition(self) -> None:
        row = self.by_pair[(3, 7)]
        self.assertEqual(row["sum_transition"]["factorization_text"], "2*5")
        self.assertEqual(row["sum_transition"]["kappa"], 1)
        self.assertEqual(row["difference_transition"]["factorization_text"], "2^2")
        self.assertEqual(row["difference_transition"]["kappa"], 1)
        self.assertEqual(row["transition_coupling"]["gcd_sum_difference"], 2)
        self.assertEqual(row["transition_coupling"]["support_intersection"], [2])

    def test_axis_ratio_additive_bridge(self) -> None:
        self.assertTrue(
            all(row["ratio_gap_bridge"]["verified"] for row in self.records)
        )

    def test_transition_support_avoids_original_edge_axes(self) -> None:
        self.assertTrue(
            all(
                row["reduced_transition_support_disjoint_from_edge_axes"]
                for row in self.records
            )
        )

    def test_sum_difference_gcd_law(self) -> None:
        for row in self.records:
            expected = 1 if row["p"] == 2 else 2
            self.assertEqual(
                row["transition_coupling"]["gcd_sum_difference"], expected
            )
            self.assertTrue(row["transition_coupling"]["gcd_law_verified"])

    def test_axis_two_parity_routing(self) -> None:
        for row in self.records:
            plus_has_two = row["sum_transition"]["contains_axis_2"]
            minus_has_two = row["difference_transition"]["contains_axis_2"]
            if row["p"] == 2:
                self.assertFalse(plus_has_two)
                self.assertFalse(minus_has_two)
            else:
                self.assertTrue(plus_has_two)
                self.assertTrue(minus_has_two)

    def test_sum_level_preservation_rigidity(self) -> None:
        for row in self.records:
            expected = row["p"] == 2 and is_prime(row["q"] + 2)
            self.assertEqual(row["sum_level_preserved"], expected)

    def test_difference_level_preservation_rigidity(self) -> None:
        for row in self.records:
            expected = is_prime(row["q"] - row["p"])
            self.assertEqual(row["difference_level_preserved"], expected)
            if row["p"] > 2:
                self.assertEqual(row["difference_level_preserved"], row["gap"] == 2)

    def test_exact_finite_distributions(self) -> None:
        counts = self.summary["finite_counts"]
        self.assertEqual(counts["parity_class"], {"contains_axis_2": 24, "odd_odd": 276})
        self.assertEqual(counts["sum_level_relation"], {"preserved": 8, "up": 292})
        self.assertEqual(
            counts["difference_level_relation"],
            {"down": 1, "preserved": 16, "up": 283},
        )
        self.assertEqual(
            counts["kappa_plus_distribution"],
            {"0": 8, "1": 57, "2": 96, "3": 81, "4": 40, "5": 16, "6": 2},
        )
        self.assertEqual(
            counts["kappa_minus_distribution"],
            {"-1": 1, "0": 16, "1": 95, "2": 107, "3": 61, "4": 17, "5": 3},
        )

    def test_maximum_observed_defects(self) -> None:
        maxima = self.summary["maximum_observed_defects"]
        self.assertEqual(maxima["sum"]["maximum"], 6)
        self.assertEqual(
            {(x["p"], x["q"], x["value"]) for x in maxima["sum"]["examples"]},
            {(31, 97, 128), (61, 67, 128)},
        )
        self.assertEqual(maxima["difference"]["maximum"], 5)
        self.assertEqual(
            {(x["p"], x["q"], x["value"]) for x in maxima["difference"]["examples"]},
            {(3, 67, 64), (7, 71, 64), (19, 83, 64)},
        )

    def test_csv_is_deterministic_and_complete(self) -> None:
        csv_payload, summary_payload, summary = build_atlas(100)
        self.assertEqual(csv_payload.count("\n") - 1, 300)
        self.assertTrue(csv_payload.startswith("id,p,q,ratio,normalized_gap"))
        self.assertIn("PP-001,2,3,3/2,1/5", csv_payload)
        self.assertEqual(summary["scope"]["unordered_pair_count"], 300)
        self.assertTrue(summary_payload.endswith("\n"))

    def test_invalid_edge_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            edge_record(3, 9, prime_index_gap=1, record_id=1)


if __name__ == "__main__":
    unittest.main()
