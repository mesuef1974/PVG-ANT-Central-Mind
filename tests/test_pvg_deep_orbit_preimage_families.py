from __future__ import annotations

import unittest

from tools.pvg_deep_orbit_preimage_families import (
    analyze,
    analyze_support_orbit,
    closest_distinct_prime_pair,
    face_key,
    factor_support,
    sieve_tables,
    successors,
)


class PVGDeepOrbitPreimageFamiliesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = analyze(400_000, 12, 7)
        cls.ladder = [
            (
                row["prime_limit_threshold"],
                row["new_minimum_closure_depth"],
            )
            for row in cls.data["exact_prime_limit_threshold_ladder_through_sum_cap"]
        ]
        cls.deep_rows = {
            row["new_minimum_closure_depth"]: row
            for row in cls.data["deep_prime_limit_threshold_ladder"]
        }
        cls.families = {
            row["initial_support_key"]: row
            for row in cls.data["deep_threshold_support_families"]
        }

    def test_validation(self) -> None:
        for args in ((9, 12, 7), (100, 0, 7), (100, 12, 1)):
            with self.assertRaises(ValueError):
                analyze(*args)

    def test_pair_successor_identity_examples(self) -> None:
        self.assertEqual(successors((347, 359)), ((2, 353),))
        self.assertEqual(successors((863, 911)), ((2, 887),))
        self.assertEqual(successors((5107, 5227)), ((2, 5167),))
        self.assertEqual(factor_support(1774), (2, 887))
        self.assertEqual(face_key((2, 887)), "{2,887}")

    def test_exact_threshold_ladder(self) -> None:
        self.assertEqual(
            self.ladder,
            [
                (3, 1),
                (7, 2),
                (19, 3),
                (31, 4),
                (73, 5),
                (359, 6),
                (911, 7),
                (5227, 8),
                (23251, 9),
                (63103, 10),
                (167119, 11),
            ],
        )

    def test_pass023_prefix_is_reproduced(self) -> None:
        self.assertEqual(
            self.ladder[:6],
            [(3, 1), (7, 2), (19, 3), (31, 4), (73, 5), (359, 6)],
        )

    def test_deep_witness_sums_and_pairs(self) -> None:
        expected = {
            7: (1774, [863, 911], [2, 887], 26),
            8: (10334, [5107, 5227], [2, 5167], 96),
            9: (46418, [23167, 23251], [2, 23209], 320),
            10: (126134, [63031, 63103], [2, 63067], 713),
            11: (334142, [167023, 167119], [2, 167071], 1596),
        }
        for depth, values in expected.items():
            witness = self.deep_rows[depth]["witnesses"][0]
            self.assertEqual(
                (
                    witness["sum"],
                    witness["closest_prime_pair"],
                    witness["initial_support"],
                    witness["distinct_prime_pair_representation_count"],
                ),
                values,
            )

    def test_depth_seven_orbit_certificate(self) -> None:
        witness = self.deep_rows[7]["witnesses"][0]
        self.assertEqual(
            witness["orbit_layers_from_prime_pair_depth_1"],
            [
                [[2, 887]],
                [[7, 127]],
                [[2, 67]],
                [[3, 23]],
                [[2, 13]],
                [[3, 5]],
                [[2]],
            ],
        )
        self.assertEqual(witness["final_terminal_axes"], [2])

    def test_depth_eleven_orbit_certificate(self) -> None:
        witness = self.deep_rows[11]["witnesses"][0]
        self.assertEqual(
            witness["orbit_layers_from_prime_pair_depth_1"],
            [
                [[2, 167071]],
                [[3, 55691]],
                [[2, 27847]],
                [[3, 9283]],
                [[2, 4643]],
                [[5, 929]],
                [[2, 467]],
                [[7, 67]],
                [[2, 37]],
                [[3, 13]],
                [[2]],
            ],
        )

    def test_support_fiber_powers_and_counts(self) -> None:
        expected = {
            "{2,887}": ([1774, 3548, 7096, 14192, 28384, 56768, 113536, 227072], 2719),
            "{2,5167}": ([10334, 20668, 41336, 82672, 165344, 330688], 3611),
            "{2,23209}": ([46418, 92836, 185672, 371344], 3695),
            "{2,63067}": ([126134, 252268], 1991),
            "{2,167071}": ([334142], 1596),
        }
        for key, (sums, total_representations) in expected.items():
            family = self.families[key]
            self.assertEqual(
                [row["sum"] for row in family["represented_sums_under_cap"]],
                sums,
            )
            self.assertEqual(
                family["total_distinct_prime_pair_representations_under_cap"],
                total_representations,
            )
            self.assertTrue(family["all_sums_have_same_support"])

    def test_support_fiber_orbit_invariance(self) -> None:
        first = analyze_support_orbit((2, 887), 12)
        second = analyze_support_orbit(factor_support(3548), 12)
        self.assertEqual(first, second)
        family = self.families["{2,887}"]
        self.assertEqual(family["prime_pair_closure_depth"], 7)
        self.assertEqual(family["final_terminal_key"], "{2}")

    def test_depth_distribution_and_ceiling(self) -> None:
        self.assertEqual(
            self.data["represented_sum_depth_distribution"],
            {
                "1": 3870,
                "2": 6131,
                "3": 18590,
                "4": 77864,
                "5": 79824,
                "6": 37190,
                "7": 8798,
                "8": 1435,
                "9": 143,
                "10": 10,
                "11": 1,
            },
        )
        self.assertEqual(self.data["maximum_observed_prime_pair_closure_depth"], 11)
        self.assertIsNone(self.data["first_depth_twelve_threshold"])

    def test_closest_pair_helper(self) -> None:
        _, is_prime, primes = sieve_tables(2000)
        self.assertEqual(
            closest_distinct_prime_pair(1774, is_prime, primes),
            (863, 911),
        )
        self.assertEqual(
            closest_distinct_prime_pair(5, is_prime, primes),
            (2, 3),
        )

    def test_verification(self) -> None:
        self.assertTrue(all(self.data["verification"].values()))
        self.assertEqual(self.data["first_depth_seven_threshold"], 911)
        self.assertEqual(self.data["first_depth_eight_threshold"], 5227)
        self.assertEqual(self.data["first_depth_nine_threshold"], 23251)
        self.assertEqual(self.data["first_depth_ten_threshold"], 63103)
        self.assertEqual(self.data["first_depth_eleven_threshold"], 167119)


if __name__ == "__main__":
    unittest.main()
