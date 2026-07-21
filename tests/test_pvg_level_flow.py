#!/usr/bin/env python3
import unittest
from tools.pvg_level_flow import analyze, adjacent

class PVGLevelFlowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.r=analyze([2,3,5],6)
    def test_scope(self):
        self.assertEqual(self.r['point_count'],28)
        self.assertEqual(set(self.r['fields']),{'n','tau','sigma_over_n','phi_over_n'})
    def test_all_strict_flows_are_acyclic(self):
        self.assertTrue(self.r['verification']['all_strict_flows_acyclic'])
    def test_plateau_condensations_are_acyclic(self):
        self.assertTrue(self.r['verification']['all_condensations_acyclic'])
    def test_size_has_expected_unique_extrema(self):
        f=self.r['fields']['n']
        self.assertEqual(f['global_minima'],[[6,0,0]])
        self.assertEqual(f['global_maxima'],[[0,0,6]])
    def test_tau_unique_global_peak(self):
        f=self.r['fields']['tau']
        self.assertEqual(f['global_maxima'],[[2,2,2]])
        self.assertIn([2,2,2],f['local_maxima'])
    def test_abundancy_unique_global_peak(self):
        self.assertEqual(self.r['fields']['sigma_over_n']['global_maxima'],[[3,2,1]])
    def test_phi_over_n_has_full_support_minimum_plateau(self):
        f=self.r['fields']['phi_over_n']
        self.assertEqual(len(f['global_minima']),10)
        self.assertTrue(all(all(x>0 for x in a) for a in f['global_minima']))
        self.assertGreater(f['equal_edge_count'],0)
    def test_strongest_paths_end_at_local_maxima(self):
        for f in self.r['fields'].values():
            maxima={tuple(x) for x in f['local_maxima']}
            for path in f['strongest_ascent_paths'].values():
                self.assertIn(tuple(path[-1]),maxima)
    def test_adjacency(self):
        self.assertTrue(adjacent((2,2,2),(3,1,2)))
        self.assertFalse(adjacent((2,2,2),(4,0,2)))

if __name__=='__main__': unittest.main()
