from __future__ import annotations

import unittest

from tools.pvg_additive_basin_overlap_geometry import analyze


class PVGAdditiveBasinOverlapGeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = analyze(
            100,
            5,
            include_records=False,
            include_unobserved_signatures=False,
        )

    def test_registered_scope(self) -> None:
        self.assertEqual(
            self.data["scope"],
            {
                "prime_limit": 100,
                "depth_bound": 5,
                "start_face_count": 300,
                "terminal_axis_count": 10,
                "endpoint_signature_count": 19,
            },
        )

    def test_overlap_graph_size_and_components(self) -> None:
        graph = self.data["axis_overlap_graph"]
        self.assertEqual(graph["node_count"], 10)
        self.assertEqual(graph["edge_count"], 13)
        self.assertEqual(graph["component_count"], 5)
        self.assertEqual(graph["component_sizes"], [6, 1, 1, 1, 1])
        self.assertEqual(graph["isolated_axes"], [31, 43, 61, 73])
        self.assertEqual(graph["cycle_rank"], 8)
        self.assertEqual(graph["articulation_axes"], [])
        self.assertEqual(graph["bridge_edges"], [])

    def test_strongest_pair_overlap(self) -> None:
        top = self.data["axis_overlap_graph"]["pair_overlaps"][0]
        self.assertEqual(top["axes"], [5, 7])
        self.assertEqual(top["intersection_size"], 75)
        self.assertEqual(top["union_size"], 196)
        self.assertEqual(top["exact_pair_signature_count"], 0)
        self.assertEqual(top["higher_order_mediated_count"], 75)

    def test_only_exact_pair_signature(self) -> None:
        observed = [
            item
            for item in self.data["axis_overlap_graph"]["pair_overlaps"]
            if item["exact_pair_signature_count"]
        ]
        self.assertEqual(len(observed), 1)
        self.assertEqual(observed[0]["axes"], [2, 5])
        self.assertEqual(observed[0]["intersection_size"], 46)
        self.assertEqual(observed[0]["exact_pair_signature_count"], 13)
        self.assertEqual(observed[0]["higher_order_mediated_count"], 33)

    def test_axis_five_weighted_centrality(self) -> None:
        ranking = self.data["axis_overlap_graph"][
            "weighted_overlap_degree_ranking"
        ]
        self.assertEqual(ranking[0]["axis"], 5)
        self.assertEqual(ranking[0]["basin_size"], 153)
        self.assertEqual(ranking[0]["overlap_degree"], 5)
        self.assertEqual(ranking[0]["weighted_overlap_degree"], 187)

    def test_triple_overlaps(self) -> None:
        self.assertEqual(
            [
                (item["axes"], item["intersection_size"])
                for item in self.data["triple_overlaps"]
            ],
            [
                ([2, 5, 7], 33),
                ([3, 5, 7], 28),
                ([3, 5, 13], 11),
                ([5, 7, 19], 8),
                ([5, 7, 13], 6),
                ([2, 7, 13], 4),
                ([3, 5, 19], 1),
                ([7, 13, 19], 1),
            ],
        )

    def test_signature_observation_counts(self) -> None:
        observation = self.data["signature_observation"]
        self.assertEqual(observation["possible_exact_pair_signature_count"], 45)
        self.assertEqual(observation["observed_exact_pair_signature_count"], 1)
        self.assertEqual(observation["unobserved_exact_pair_signature_count"], 44)
        self.assertEqual(observation["possible_exact_triple_signature_count"], 120)
        self.assertEqual(observation["observed_exact_triple_signature_count"], 8)
        self.assertEqual(observation["unobserved_exact_triple_signature_count"], 112)
        self.assertTrue(
            observation["all_terminal_axes_observed_as_exact_singletons"]
        )

    def test_signature_poset(self) -> None:
        poset = self.data["signature_poset"]
        self.assertEqual(poset["rank_distribution"], {"1": 10, "2": 1, "3": 8})
        self.assertEqual(poset["comparable_pair_count"], 27)
        self.assertEqual(poset["cover_edge_count"], 25)
        self.assertEqual(poset["component_count"], 5)
        self.assertEqual(poset["component_sizes"], [15, 1, 1, 1, 1])
        self.assertEqual(poset["cycle_rank"], 11)
        self.assertEqual(poset["longest_chain_node_count"], 3)
        self.assertEqual(
            poset["triple_signatures_with_observed_pair_predecessor"],
            [[2, 5, 7]],
        )

    def test_gateway_signatures(self) -> None:
        self.assertEqual(self.data["gateway_start_count"], 105)
        self.assertEqual(self.data["gateway_signature_count"], 9)
        top = self.data["gateway_signatures"][0]
        self.assertEqual(top["terminal_axes"], [2, 5, 7])
        self.assertEqual(top["start_face_count"], 33)
        self.assertEqual(top["routed_pair_memberships"], 99)

    def test_all_verifications(self) -> None:
        self.assertTrue(all(self.data["verification"].values()))

    def test_invalid_parameters(self) -> None:
        with self.assertRaises(ValueError):
            analyze(2, 5)
        with self.assertRaises(ValueError):
            analyze(100, -1)


if __name__ == "__main__":
    unittest.main()
