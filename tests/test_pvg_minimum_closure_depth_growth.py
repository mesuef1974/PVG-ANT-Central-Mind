from __future__ import annotations

import unittest

from tools.pvg_minimum_closure_depth_growth import (
    REGISTERED_LIMITS,
    analyze,
    analyze_start_profile,
    parse_limits,
    registered_summary,
    support,
    successors,
)


class PVGMinimumClosureDepthGrowthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = analyze(REGISTERED_LIMITS, 0, 8, include_profiles=False)
        cls.snapshots = {
            row["prime_limit"]: row for row in cls.data["limit_snapshots"]
        }

    def test_parse_limits_and_validation(self) -> None:
        self.assertEqual(parse_limits("100,150,200"), (100, 150, 200))
        for bad in ("", "150,100", "100,100", "2,100", "100,x"):
            with self.assertRaises(ValueError):
                parse_limits(bad)
        with self.assertRaises(ValueError):
            analyze((100,), 1, 8, include_profiles=False)
        with self.assertRaises(ValueError):
            analyze((100,), 0, -1, include_profiles=False)

    def test_support_and_successor_rule(self) -> None:
        self.assertEqual(support(706), (2, 353))
        self.assertEqual(successors((347, 359)), ((2, 353),))
        self.assertEqual(successors((2, 5)), ((7,),))
        self.assertEqual(successors((7,)), tuple())

    def test_registered_scope_and_pair_counts(self) -> None:
        self.assertEqual(
            self.data["scope"]["registered_limits"], list(REGISTERED_LIMITS)
        )
        self.assertEqual(self.data["scope"]["depth_values"], list(range(9)))
        self.assertEqual(
            [self.snapshots[limit]["start_face_count"] for limit in REGISTERED_LIMITS],
            [300, 595, 1035, 1378, 1891, 2415, 3003, 3741, 4465],
        )

    def test_minimum_closure_depth_series(self) -> None:
        self.assertEqual(
            self.data["minimum_closure_depth_series"],
            [5, 5, 5, 5, 5, 5, 6, 6, 6],
        )
        self.assertTrue(
            all(
                self.snapshots[limit]["all_starts_closed_through_max_depth"]
                for limit in REGISTERED_LIMITS
            )
        )

    def test_exact_threshold_ladder(self) -> None:
        ladder = self.data["exact_threshold_ladder_through_maximum_limit"]
        self.assertEqual(
            [
                (row["prime_limit_threshold"], row["new_minimum_closure_depth"])
                for row in ladder
            ],
            [(3, 1), (7, 2), (19, 3), (31, 4), (73, 5), (359, 6)],
        )
        self.assertEqual(ladder[-1]["witness_start_faces"], [[347, 359]])
        self.assertEqual(ladder[-1]["witness_final_terminal_keys"], ["{7}"])

    def test_first_depth_six_and_absence_of_depth_seven(self) -> None:
        self.assertEqual(self.data["first_depth_six_threshold"], 359)
        self.assertIsNone(self.data["first_depth_seven_threshold"])
        self.assertTrue(
            self.data["no_depth_seven_required_through_maximum_limit"]
        )

    def test_closure_depth_distributions(self) -> None:
        self.assertEqual(
            self.snapshots[100]["closure_depth_distribution"],
            {"0": 0, "1": 24, "2": 161, "3": 90, "4": 23, "5": 2, "6": 0, "7": 0, "8": 0},
        )
        self.assertEqual(
            self.snapshots[400]["closure_depth_distribution"],
            {"0": 0, "1": 55, "2": 971, "3": 1196, "4": 648, "5": 131, "6": 2, "7": 0, "8": 0},
        )
        self.assertEqual(
            self.snapshots[500]["closure_depth_distribution"],
            {"0": 0, "1": 62, "2": 1296, "3": 1797, "4": 1082, "5": 222, "6": 6, "7": 0, "8": 0},
        )

    def test_depth_six_extremal_faces_grow_by_bound(self) -> None:
        self.assertEqual(
            self.snapshots[400]["maximum_depth_start_faces"],
            [[317, 389], [347, 359]],
        )
        self.assertEqual(
            self.snapshots[450]["maximum_depth_start_faces"],
            [[257, 449], [263, 443], [317, 389], [347, 359]],
        )
        self.assertEqual(
            self.snapshots[500]["maximum_depth_start_faces"],
            [[227, 479], [239, 467], [257, 449], [263, 443], [317, 389], [347, 359]],
        )

    def test_depth_six_faces_share_sum_and_orbit(self) -> None:
        snapshot = self.snapshots[500]
        self.assertEqual(snapshot["maximum_depth_start_sums"], [706])
        self.assertEqual(
            snapshot["maximum_depth_terminal_signature_distribution"],
            {"{7}": 6},
        )
        group = snapshot["maximum_depth_orbit_groups"][0]
        self.assertEqual(group["start_face_count"], 6)
        self.assertTrue(group["all_start_sums_equal"])
        self.assertEqual(group["start_sums"], [706])
        self.assertEqual(
            group["orbit_tail_from_depth_1"],
            [
                [[2, 353]],
                [[5, 71]],
                [[2, 19]],
                [[3, 7]],
                [[2, 5]],
                [[7]],
            ],
        )

    def test_explicit_depth_six_orbit_certificate(self) -> None:
        profile = analyze_start_profile((347, 359), 8)
        self.assertEqual(profile["first_bounded_closure_depth"], 6)
        self.assertEqual(profile["final_terminal_axes"], [7])
        self.assertEqual(
            profile["layer_faces"][:7],
            [
                [[347, 359]],
                [[2, 353]],
                [[5, 71]],
                [[2, 19]],
                [[3, 7]],
                [[2, 5]],
                [[7]],
            ],
        )

    def test_signature_stabilization_can_precede_closure(self) -> None:
        self.assertEqual(
            self.snapshots[100]["signature_stabilization_depth_distribution"],
            {"0": 0, "1": 24, "2": 171, "3": 80, "4": 23, "5": 2, "6": 0, "7": 0, "8": 0},
        )
        self.assertEqual(
            [
                self.snapshots[limit]["maximum_closure_minus_stabilization_gap"]
                for limit in REGISTERED_LIMITS
            ],
            [1, 1, 1, 1, 1, 1, 3, 3, 3],
        )

    def test_maximum_stabilization_gap_examples(self) -> None:
        self.assertEqual(
            self.snapshots[500]["maximum_gap_start_faces"],
            [[211, 499], [223, 487], [271, 439], [277, 433], [313, 397], [331, 379], [337, 373]],
        )
        self.assertEqual(
            self.snapshots[500]["maximum_gap_final_signatures"],
            ["{7,73}"],
        )

    def test_verification_and_registered_summary(self) -> None:
        self.assertTrue(all(self.data["verification"].values()))
        summary = registered_summary(self.data)
        self.assertEqual(summary["limit_table"][-1]["prime_limit"], 500)
        self.assertEqual(summary["first_depth_six_threshold"], 359)
        self.assertTrue(summary["no_depth_seven_required_through_maximum_limit"])


if __name__ == "__main__":
    unittest.main()
