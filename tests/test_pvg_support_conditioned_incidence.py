from __future__ import annotations

import unittest

from tools.pvg_support_conditioned_incidence import (
    bit_length_stratum,
    counterexamples,
    decimal_bin,
    matched_neighborhood_witnesses,
    registered_summary,
    route,
)


class SupportConditionedIncidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.summary = registered_summary()

    def test_strata_helpers(self) -> None:
        self.assertEqual(decimal_bin(1), "1-9")
        self.assertEqual(decimal_bin(99999), "10000-99999")
        self.assertEqual(decimal_bin(100000), "100000-100000")
        self.assertEqual(bit_length_stratum(1), 1)
        self.assertEqual(bit_length_stratum(8), 4)
        self.assertEqual(route(30), "even")
        self.assertEqual(route(45), "odd")
        for bad in (0, -1, 100001):
            with self.assertRaises(ValueError):
                decimal_bin(bad)

    def test_frozen_scope(self) -> None:
        scope = self.summary["scope"]
        self.assertEqual(scope["integer_point_count"], 884)
        self.assertEqual(scope["represented_point_count"], 745)
        self.assertEqual(scope["support_face_sizes"], [1, 2, 3])
        self.assertEqual(scope["integer_cap"], 100000)

    def test_group_partitions_reconstruct_scope(self) -> None:
        total = sum(row["summary"]["point_count"] for row in self.summary["conditioned_by_support_size"])
        self.assertEqual(total, 884)
        exact_total = sum(row["summary"]["point_count"] for row in self.summary["conditioned_by_exact_support"])
        self.assertEqual(exact_total, 884)

    def test_exact_arithmetic_fields(self) -> None:
        for collection_name in (
            "raw_by_support_size",
            "conditioned_by_support_size",
            "conditioned_by_exact_support",
            "bit_length_conditioned_by_support_size",
        ):
            for row in self.summary[collection_name]:
                block = row["summary"]
                self.assertEqual(block["represented_count"] + block["nonrepresented_count"], block["point_count"])
                self.assertIsInstance(block["multiplicity_mean"], str)
                self.assertIsInstance(block["represented_rate"], str)

    def test_preregistered_counterexamples_are_found(self) -> None:
        witnesses = self.summary["counterexamples"]
        self.assertIsNotNone(witnesses["same_exact_support_does_not_determine_multiplicity"])
        self.assertIsNotNone(witnesses["same_support_size_does_not_determine_multiplicity"])
        self.assertIsNotNone(witnesses["same_size_bin_does_not_determine_support"])

    def test_matched_witnesses_follow_rule(self) -> None:
        witnesses = self.summary["matched_neighborhood_witnesses"]
        self.assertTrue(witnesses)
        for witness in witnesses:
            left, right = witness["left"], witness["right"]
            self.assertEqual(int(left["integer"]) % 2, int(right["integer"]) % 2)
            self.assertNotEqual(left["support_size"], right["support_size"])
            self.assertGreaterEqual(witness["distance"], 0)

    def test_rank_tables_are_deterministic(self) -> None:
        for table in self.summary["conditioned_rank_tables"]:
            ranking = table["ranking"]
            self.assertEqual(
                ranking,
                sorted(ranking, key=lambda row: (-__import__("fractions").Fraction(row["multiplicity_mean"]), str(row["class"]))),
            )

    def test_verification_and_claim_ceiling(self) -> None:
        verification = self.summary["verification"]
        self.assertTrue(all(value is True for value in verification.values()))
        self.assertFalse(any(self.summary["claim_ceiling"].values()))
        certificate = self.summary["record_certificate"]
        self.assertEqual(certificate["row_count"], 884)
        self.assertEqual(len(certificate["sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
