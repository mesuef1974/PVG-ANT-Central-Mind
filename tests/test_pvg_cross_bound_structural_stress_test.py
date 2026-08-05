from __future__ import annotations

import unittest

from tools.pvg_cross_bound_structural_stress_test import (
    REGISTERED_DEPTH,
    REGISTERED_LIMITS,
    REGISTERED_REPAIR_DEPTH_CAP,
    analyze,
)


class PVGCrossBoundStructuralStressTestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = analyze(
            REGISTERED_LIMITS,
            REGISTERED_DEPTH,
            REGISTERED_REPAIR_DEPTH_CAP,
        )
        cls.cumulative = {
            row["prime_limit"]: row for row in cls.data["cumulative_table"]
        }
        cls.cohorts = {
            (row["from_limit_exclusive"], row["to_limit_inclusive"]): row
            for row in cls.data["cohort_table"]
        }
        cls.candidates = {
            row["candidate"]: row for row in cls.data["candidate_tests"]
        }

    def test_registered_scope(self) -> None:
        self.assertEqual(
            self.data["protocol"]["registered_limits"],
            [100, 150, 200, 250, 300, 400],
        )
        self.assertEqual(self.data["protocol"]["fixed_depth"], 5)
        self.assertEqual(self.data["protocol"]["repair_depth_cap"], 8)

    def test_start_counts_and_fixed_depth_wall(self) -> None:
        self.assertEqual(
            [self.cumulative[limit]["start_face_count"] for limit in REGISTERED_LIMITS],
            [300, 595, 1035, 1378, 1891, 3003],
        )
        self.assertEqual(
            [
                self.cumulative[limit]["unresolved_start_count"]
                for limit in REGISTERED_LIMITS
            ],
            [0, 0, 0, 0, 0, 2],
        )
        self.assertEqual(self.data["stress_summary"]["last_fully_closed_limit"], 300)
        self.assertEqual(
            self.data["stress_summary"]["first_fixed_depth_wall_limit"], 400
        )
        self.assertEqual(self.data["stress_summary"]["decisive_result"], "DEPTH-WALL")

    def test_unresolved_faces_are_exact(self) -> None:
        repair = self.data["depth_wall_repair"]
        self.assertEqual(
            repair["unresolved_start_keys"], ["{317,389}", "{347,359}"]
        )
        self.assertEqual(
            [row["unresolved_frontier_at_fixed_depth"] for row in repair["unresolved_start_details"]],
            [[[2, 5]], [[2, 5]]],
        )

    def test_local_depth_repair_closes_at_six(self) -> None:
        repair = self.data["depth_wall_repair"]
        self.assertTrue(repair["repair_succeeded_within_cap"])
        self.assertEqual(repair["first_closing_depth"], 6)
        self.assertEqual(
            [row["terminal_axes_after_repair"] for row in repair["unresolved_start_details"]],
            [[7], [7]],
        )
        self.assertEqual(repair["repaired_snapshot"]["unresolved_start_count"], 0)

    def test_axis_five_leads_all_fully_closed_cumulative_snapshots(self) -> None:
        for limit in (100, 150, 200, 250, 300):
            row = self.cumulative[limit]
            self.assertEqual(row["largest_basin_axes"], [5])
            self.assertEqual(row["maximum_weighted_degree_axes"], [5])

    def test_edge_five_seven_leads_all_fully_closed_cumulative_snapshots(self) -> None:
        for limit in (100, 150, 200, 250, 300):
            self.assertEqual(
                self.cumulative[limit]["strongest_overlap_edge"]["axes"], [5, 7]
            )

    def test_leaders_hold_in_all_fully_closed_cohorts(self) -> None:
        for transition in ((100, 150), (150, 200), (200, 250), (250, 300)):
            row = self.cohorts[transition]
            self.assertEqual(row["largest_basin_axes"], [5])
            self.assertEqual(row["maximum_weighted_degree_axes"], [5])
            self.assertEqual(row["strongest_overlap_edge"]["axes"], [5, 7])

    def test_rank_and_active_component_are_non_decreasing_before_wall(self) -> None:
        closed = [self.cumulative[limit] for limit in (100, 150, 200, 250, 300)]
        self.assertEqual(
            [row["maximum_nonempty_signature_rank"] for row in closed],
            [3, 4, 5, 5, 5],
        )
        self.assertEqual(
            [row["active_component_size"] for row in closed],
            [6, 8, 9, 10, 10],
        )

    def test_candidate_statuses_respect_censoring(self) -> None:
        self.assertEqual(
            self.candidates["fixed_depth_closure"]["status"],
            "COUNTEREXAMPLE_FOUND",
        )
        for key in (
            "largest_basin_axis_5",
            "maximum_weighted_degree_axis_5",
            "strongest_overlap_edge_5_7",
            "maximum_signature_rank_non_decreasing",
            "active_component_size_non_decreasing",
        ):
            self.assertEqual(
                self.candidates[key]["status"],
                "SURVIVES_FULLY_CLOSED_RANGE_PROVISIONAL_AT_DEPTH_WALL",
            )

    def test_first_counterexample_registry(self) -> None:
        counterexamples = self.data["first_counterexamples"]
        self.assertEqual(counterexamples["fixed_depth_closure"], 400)
        for key, value in counterexamples.items():
            if key != "fixed_depth_closure":
                self.assertIsNone(value)

    def test_repaired_snapshot_keeps_provisional_leaders(self) -> None:
        repaired = self.data["depth_wall_repair"]["repaired_snapshot"]
        self.assertEqual(repaired["largest_basin_axes"], [5])
        self.assertEqual(repaired["maximum_weighted_degree_axes"], [5])
        self.assertEqual(repaired["strongest_overlap_edge"]["axes"], [5, 7])
        self.assertEqual(repaired["maximum_nonempty_signature_rank"], 5)

    def test_verification(self) -> None:
        self.assertTrue(all(self.data["verification"].values()))
        self.assertFalse(
            self.data["underlying_expansion_verification"][
                "no_registered_bound_has_unresolved_starts"
            ]
        )
        for key, value in self.data["underlying_expansion_verification"].items():
            if key != "no_registered_bound_has_unresolved_starts":
                self.assertTrue(value, key)

    def test_validation_errors(self) -> None:
        with self.assertRaises(ValueError):
            analyze((100, 200), 5, 8)
        with self.assertRaises(ValueError):
            analyze((100, 200, 150), 5, 8)
        with self.assertRaises(ValueError):
            analyze((100, 150, 200), -1, 8)
        with self.assertRaises(ValueError):
            analyze((100, 150, 200), 5, 4)


if __name__ == "__main__":
    unittest.main()
