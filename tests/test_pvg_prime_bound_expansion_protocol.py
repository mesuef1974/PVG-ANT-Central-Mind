from __future__ import annotations

import unittest

from tools.pvg_prime_bound_expansion_protocol import (
    analyze,
    parse_limits,
    registered_summary,
)


class PVGPrimeBoundExpansionProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = analyze((100, 150, 200), 5, include_records=False)
        cls.snapshots = {
            row["prime_limit"]: row for row in cls.data["cumulative_snapshots"]
        }
        cls.cohorts = {
            (row["from_limit_exclusive"], row["to_limit_inclusive"]): row
            for row in cls.data["cohort_snapshots"]
        }
        cls.transitions = {
            (row["from_limit"], row["to_limit"]): row
            for row in cls.data["bound_transitions"]
        }

    def test_parse_limits_and_validation(self) -> None:
        self.assertEqual(parse_limits("100,150,200"), (100, 150, 200))
        for bad in ("100", "150,100", "100,100", "2,100", "100,x"):
            with self.assertRaises(ValueError):
                parse_limits(bad)

    def test_registered_scope_and_pair_counts(self) -> None:
        self.assertEqual(self.data["protocol"]["registered_limits"], [100, 150, 200])
        self.assertEqual(self.data["protocol"]["fixed_depth"], 5)
        self.assertEqual(
            [
                (self.snapshots[limit]["prime_count"], self.snapshots[limit]["start_face_count"])
                for limit in (100, 150, 200)
            ],
            [(25, 300), (35, 595), (46, 1035)],
        )

    def test_fixed_depth_closes_all_registered_starts(self) -> None:
        self.assertEqual(
            [self.snapshots[limit]["unresolved_start_count"] for limit in (100, 150, 200)],
            [0, 0, 0],
        )
        self.assertEqual(
            [
                (
                    self.snapshots[limit]["single_terminal_start_count"],
                    self.snapshots[limit]["multiple_terminal_start_count"],
                )
                for limit in (100, 150, 200)
            ],
            [(195, 105), (337, 258), (517, 518)],
        )

    def test_terminal_axis_growth(self) -> None:
        self.assertEqual(
            [self.snapshots[limit]["terminal_axis_count"] for limit in (100, 150, 200)],
            [10, 14, 17],
        )
        self.assertEqual(
            self.transitions[(100, 150)]["new_terminal_axes"],
            [103, 109, 139, 151],
        )
        self.assertEqual(
            self.transitions[(150, 200)]["new_terminal_axes"],
            [181, 193, 199],
        )

    def test_signature_growth_and_rank(self) -> None:
        self.assertEqual(
            [self.snapshots[limit]["endpoint_signature_count"] for limit in (100, 150, 200)],
            [19, 29, 38],
        )
        self.assertEqual(
            [self.snapshots[limit]["maximum_signature_rank"] for limit in (100, 150, 200)],
            [3, 4, 5],
        )
        self.assertEqual(
            self.snapshots[200]["signature_rank_distribution"],
            {"1": 17, "2": 3, "3": 16, "4": 1, "5": 1},
        )

    def test_overlap_component_growth(self) -> None:
        self.assertEqual(
            [self.snapshots[limit]["overlap_graph"]["edge_count"] for limit in (100, 150, 200)],
            [13, 18, 22],
        )
        self.assertEqual(
            [self.snapshots[limit]["overlap_graph"]["active_component"] for limit in (100, 150, 200)],
            [
                [2, 3, 5, 7, 13, 19],
                [2, 3, 5, 7, 13, 19, 31, 43],
                [2, 3, 5, 7, 13, 19, 31, 43, 61],
            ],
        )

    def test_axis_five_and_edge_five_seven_persist_as_leaders(self) -> None:
        candidates = self.data["cross_bound_candidates"]
        self.assertTrue(candidates["largest_basin_axis_is_constant"])
        self.assertTrue(candidates["strongest_overlap_edge_is_constant"])
        self.assertTrue(candidates["maximum_weighted_degree_axis_is_constant"])
        self.assertEqual(candidates["largest_basin_axis_series"], [[5], [5], [5]])
        self.assertEqual(candidates["strongest_overlap_edge_series"], [[5, 7], [5, 7], [5, 7]])

    def test_absent_signature_becomes_observed(self) -> None:
        first = self.data["first_appearance"]["endpoint_signatures"]
        self.assertEqual(first["{5,7}"], 150)
        count_100 = next(
            (
                row["start_face_count"]
                for row in self.snapshots[100]["endpoint_signatures"]
                if row["terminal_key"] == "{5,7}"
            ),
            0,
        )
        count_150 = next(
            row["start_face_count"]
            for row in self.snapshots[150]["endpoint_signatures"]
            if row["terminal_key"] == "{5,7}"
        )
        count_200 = next(
            row["start_face_count"]
            for row in self.snapshots[200]["endpoint_signatures"]
            if row["terminal_key"] == "{5,7}"
        )
        self.assertEqual((count_100, count_150, count_200), (0, 5, 15))

    def test_incremental_cohorts_are_reported_separately(self) -> None:
        first = self.cohorts[(100, 150)]
        second = self.cohorts[(150, 200)]
        self.assertEqual(
            (first["start_face_count"], second["start_face_count"]),
            (295, 440),
        )
        self.assertEqual(
            (first["multiple_terminal_start_count"], second["multiple_terminal_start_count"]),
            (153, 260),
        )
        self.assertGreater(
            second["multiplicity_shares"]["multiple"],
            first["multiplicity_shares"]["multiple"],
        )

    def test_new_edges_and_normalized_share_changes(self) -> None:
        self.assertEqual(
            [row["axes"] for row in self.transitions[(100, 150)]["new_overlap_edges"]],
            [[2, 3], [2, 31], [5, 31], [5, 43], [13, 43]],
        )
        self.assertEqual(
            [row["axes"] for row in self.transitions[(150, 200)]["new_overlap_edges"]],
            [[3, 61], [5, 61], [7, 31], [19, 31]],
        )
        self.assertLess(
            self.transitions[(100, 150)]["persistent_axis_basin_share_changes"]["43"],
            0,
        )
        self.assertLess(
            self.transitions[(150, 200)]["persistent_axis_basin_share_changes"]["73"],
            0,
        )

    def test_verification_and_registered_summary(self) -> None:
        self.assertTrue(all(self.data["verification"].values()))
        summary = registered_summary(self.data)
        self.assertEqual(summary["cumulative_table"][2]["prime_limit"], 200)
        self.assertEqual(summary["cumulative_table"][2]["largest_basin_axes"], [5])
        self.assertEqual(
            summary["bound_transitions"][0]["new_endpoint_signatures"][4]["terminal_key"],
            "{5,7}",
        )


if __name__ == "__main__":
    unittest.main()
