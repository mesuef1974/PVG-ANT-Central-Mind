from __future__ import annotations

import unittest
from math import gcd

from tools.pvg_inverse_integer_fibers import integer_fiber, support_universe
from tools.pvg_inverse_prime_fibers import (
    centered_gap_record,
    independent_prime_pair_fiber,
    parity_route,
    prime_fiber_record,
    prime_gap_fiber,
    prime_pair_fiber,
    prime_pair_from_gap,
    registered_summary,
    representation_count,
    support_route_class,
)


class InversePrimeFiberTests(unittest.TestCase):
    def test_small_examples(self) -> None:
        self.assertEqual(prime_pair_fiber(10), ((3, 7),))
        self.assertEqual(prime_pair_fiber(24), ((5, 19), (7, 17), (11, 13)))
        self.assertEqual(prime_pair_fiber(9), ((2, 7),))
        self.assertEqual(prime_pair_fiber(27), tuple())

    def test_representation_count(self) -> None:
        self.assertEqual(representation_count(24), 3)
        self.assertEqual(representation_count(27), 0)

    def test_parity_route(self) -> None:
        self.assertEqual(parity_route(9), "two_plus_odd")
        self.assertEqual(parity_route(24), "odd_plus_odd")

    def test_centered_gap_examples(self) -> None:
        self.assertEqual(prime_gap_fiber(24), (14, 10, 2))
        self.assertEqual(
            tuple(prime_pair_from_gap(24, gap) for gap in prime_gap_fiber(24)),
            prime_pair_fiber(24),
        )
        record = centered_gap_record(24, (5, 19))
        self.assertEqual(record["square_difference"], record["four_prime_product"])
        self.assertEqual(record["gcd_n_gap"], 2)
        self.assertTrue(record["even_radius_coprime"])
        self.assertEqual(prime_gap_fiber(9), (5,))
        self.assertEqual(gcd(9, 5), 1)

    def test_support_route_and_membership(self) -> None:
        self.assertEqual(
            support_route_class((2, 3)),
            "contains_axis_2_even_route",
        )
        self.assertEqual(
            support_route_class((3, 5)),
            "excludes_axis_2_odd_route",
        )
        with self.assertRaises(ValueError):
            prime_fiber_record(24, (3, 5))

    def test_invalid_centered_gap_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            prime_pair_from_gap(24, 4)
        with self.assertRaises(ValueError):
            prime_pair_from_gap(24, 25)

    def test_complete_registered_box(self) -> None:
        faces = support_universe(11, (1, 2, 3))
        checked = 0
        checked_pairs = 0
        for face in faces:
            for value in integer_fiber(face, 100_000):
                self.assertEqual(
                    prime_pair_fiber(value),
                    independent_prime_pair_fiber(value),
                )
                pairs = prime_pair_fiber(value)
                gaps = prime_gap_fiber(value)
                self.assertEqual(
                    tuple(prime_pair_from_gap(value, gap) for gap in gaps),
                    pairs,
                )
                for gap, (left, right) in zip(gaps, pairs):
                    self.assertEqual(gap % 2, value % 2)
                    self.assertEqual(value * value - gap * gap, 4 * left * right)
                    self.assertEqual(gcd(value, gap), gcd(value, 2))
                    if value % 2 == 0:
                        self.assertEqual(gcd(value // 2, gap // 2), 1)
                    checked_pairs += 1
                if value % 2:
                    self.assertLessEqual(len(pairs), 1)
                    self.assertTrue(all(left == 2 for left, _ in pairs))
                else:
                    self.assertTrue(
                        all(left % 2 == right % 2 == 1 for left, right in pairs)
                    )
                checked += 1
        self.assertEqual(checked, 884)
        self.assertEqual(checked_pairs, 218_024)

    def test_registered_summary(self) -> None:
        data = registered_summary()
        self.assertEqual(data["scope"]["support_face_count"], 25)
        self.assertEqual(data["totals"]["integer_point_count"], 884)
        self.assertEqual(data["totals"]["representable_integer_count"], 745)
        self.assertEqual(data["totals"]["nonrepresentable_integer_count"], 139)
        self.assertEqual(data["totals"]["total_representation_count"], 218_024)
        self.assertEqual(data["totals"]["centered_gap_coordinate_count"], 218_024)
        self.assertEqual(data["totals"]["independent_scan_mismatch_count"], 0)

        contains_two = data["support_route_totals"]["contains_axis_2"]
        self.assertEqual(contains_two["integer_point_count"], 653)
        self.assertEqual(contains_two["representable_integer_count"], 650)
        self.assertEqual(contains_two["nonrepresentable_integer_count"], 3)
        self.assertEqual(contains_two["total_representation_count"], 217_929)

        excludes_two = data["support_route_totals"]["excludes_axis_2"]
        self.assertEqual(excludes_two["integer_point_count"], 231)
        self.assertEqual(excludes_two["representable_integer_count"], 95)
        self.assertEqual(excludes_two["nonrepresentable_integer_count"], 136)
        self.assertEqual(excludes_two["total_representation_count"], 95)

        self.assertEqual(
            data["frozen_box_exceptions"][
                "contains_axis_2_nonrepresentable_integers"
            ],
            [2, 4, 6],
        )
        self.assertEqual(data["global_maximum"]["integer"], 97_200)
        self.assertEqual(data["global_maximum"]["representation_count"], 1_557)
        self.assertTrue(all(data["verification"].values()))
        self.assertFalse(data["claim_ceiling"]["phase_d_authorized"])
        self.assertFalse(data["claim_ceiling"]["goldbach_progress"])


if __name__ == "__main__":
    unittest.main()
