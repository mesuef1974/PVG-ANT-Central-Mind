import math, unittest
from pvg_lab_validation import factor,is_prime,dlog,build_grid,run,additive_fiber
class TestPVGLab(unittest.TestCase):
    def test_arithmetic(self):
        self.assertEqual(factor(360),{2:3,3:2,5:1}); self.assertTrue(is_prime(97)); self.assertFalse(is_prime(1)); self.assertAlmostEqual(dlog(60,72),math.log(30),places=12)
    def test_smooth_baselines(self):
        cases={(10,2):4,(100,5):34,(1000,3):40,(1000,7):141}
        for (x,y),expected in cases.items(): self.assertEqual(build_grid(x,[y],[x],1_000_000)[0]['exact'],expected)
    def test_additive(self):
        z=additive_fiber(10,5); self.assertEqual(z['goldbach'],3); self.assertEqual(z['ordered'],9)
    def test_validation_design(self):
        z=run(10000,1_000_000); self.assertTrue(z['design']['nonoverlap']); self.assertGreater(z['counts']['holdout'],20); self.assertTrue(math.isfinite(z['correlations']['partial_pi_max_share']))
if __name__=='__main__': unittest.main()
