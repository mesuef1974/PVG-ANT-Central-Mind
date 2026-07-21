#!/usr/bin/env python3
import unittest
from tools.pvg_pareto_frontier_geometry import analyze


class PVGParetoFrontierGeometryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=analyze([2,3,5],6)

    def test_registered_scope(self):
        self.assertEqual(self.report['axes'],[2,3,5]); self.assertEqual(self.report['level'],6)

    def test_frontier_size_and_edges(self):
        self.assertEqual(self.report['frontier_size'],19)
        self.assertEqual(self.report['frontier_edge_count'],27)

    def test_components(self):
        self.assertEqual(self.report['component_count'],3)
        self.assertEqual(self.report['component_sizes'],[17,1,1])
        self.assertEqual({tuple(x) for x in self.report['isolated_points']},{(0,6,0),(6,0,0)})

    def test_cycle_rank(self):
        self.assertEqual(self.report['cycle_rank'],11)

    def test_leaves(self):
        self.assertEqual({tuple(x) for x in self.report['leaf_points']},{(0,4,2),(2,4,0),(4,0,2)})

    def test_articulation_points(self):
        self.assertEqual({tuple(x) for x in self.report['articulation_points']},{(0,3,3),(2,2,2),(3,0,3),(3,2,1),(3,3,0)})

    def test_bridges(self):
        got={frozenset((tuple(a),tuple(b))) for a,b in self.report['bridges']}
        expected={
          frozenset(((0,3,3),(0,4,2))),
          frozenset(((2,2,2),(3,2,1))),
          frozenset(((2,4,0),(3,3,0))),
          frozenset(((3,0,3),(4,0,2))),
        }
        self.assertEqual(got,expected)

    def test_objective_peaks(self):
        self.assertEqual(self.report['objective_peaks']['n'],[0,0,6])
        self.assertEqual(self.report['objective_peaks']['phi_over_n'],[0,0,6])
        self.assertEqual(self.report['objective_peaks']['tau'],[2,2,2])
        self.assertEqual(self.report['objective_peaks']['sigma_over_n'],[3,2,1])

    def test_peak_connectivity(self):
        self.assertIsNotNone(self.report['shortest_paths_between_objective_peaks']['n__tau'])
        self.assertIsNotNone(self.report['shortest_paths_between_objective_peaks']['sigma_over_n__tau'])

    def test_all_verifications(self):
        self.assertTrue(all(self.report['verification'].values()))


if __name__=='__main__': unittest.main()
