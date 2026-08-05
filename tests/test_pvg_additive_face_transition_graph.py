from __future__ import annotations

import unittest

from tools.pvg_additive_face_transition_graph import analyze


class PVGAdditiveFaceTransitionGraphTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = analyze(100)

    def test_registered_scope(self) -> None:
        self.assertEqual(self.data["source_face_count"], 300)
        self.assertEqual(self.data["unique_destination_face_count"], 52)

    def test_transition_type_distribution(self) -> None:
        self.assertEqual(
            self.data["transition_type_distribution"],
            {"composite_face": 276, "prime_axis": 8, "prime_power_axis": 16},
        )

    def test_destination_dimension_distribution(self) -> None:
        self.assertEqual(self.data["destination_face_dimension_distribution"], {1: 24, 2: 171, 3: 105})

    def test_axis_two_routing(self) -> None:
        self.assertEqual(self.data["odd_odd_source_count"], 276)
        self.assertEqual(self.data["axis_2_destination_count"], 276)

    def test_most_frequent_destination_face(self) -> None:
        first = self.data["destination_faces_ranked"][0]
        self.assertEqual(first["face"], [2, 3])
        self.assertEqual(first["indegree"], 44)

    def test_top_destination_axes(self) -> None:
        top = self.data["destination_axes_ranked"][:3]
        self.assertEqual(top, [
            {"axis": 2, "weighted_indegree": 276},
            {"axis": 3, "weighted_indegree": 143},
            {"axis": 5, "weighted_indegree": 74},
        ])

    def test_source_and_destination_are_disjoint(self) -> None:
        self.assertTrue(self.data["verification"]["all_source_destination_faces_are_disjoint"])

    def test_bipartite_graph_is_typed_acyclic(self) -> None:
        graph = self.data["bipartite_structure"]
        self.assertTrue(graph["acyclic_by_typing"])
        self.assertEqual(graph["directed_edge_count"], 300)

    def test_all_verifications(self) -> None:
        self.assertTrue(all(self.data["verification"].values()))


if __name__ == "__main__":
    unittest.main()
