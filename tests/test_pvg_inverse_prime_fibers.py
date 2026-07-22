from __future__ import annotations

import unittest

try:
    from tools.pvg_inverse_integer_fibers import integer_fiber, support_universe
    from tools.pvg_inverse_prime_fibers import (
        independent_prime_pair_fiber,
        parity_route,
        prime_pair_fiber,
        registered_summary,
        representation_count,
    )
except ModuleNotFoundError:
    from pvg_inverse_integer_fibers import integer_fiber, support_universe
    from pvg_inverse_prime_fibers import (
        independent_prime_pair_fiber,
        parity_route,
        prime_pair_fiber,
        registered_summary,
        representation_count,
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

    def test_complete_registered_box(self) -> None:
        faces = support_universe(11, (1, 2, 3))
        checked = 0
        for face in faces:
            for value in integer_fiber(face, 100_000):
                self.assertEqual(prime_pair_fiber(value), independent_prime_pair_fiber(value))
                pairs = prime_pair_fiber(value)
                if value % 2:
                    self.assertLessEqual(len(pairs), 1)
                    self.assertTrue(all(left == 2 for left, _ in pairs))
                else:
                    self.assertTrue(all(left % 2 == right % 2 == 1 for left, right in pairs))
                checked += 1
        self.assertEqual(checked, 884)

    def test_registered_summary(self) -> None:
        data = registered_summary()
        self.assertEqual(data["scope"]["support_face_count"], 25)
        self.assertEqual(data["totals"]["integer_point_count"], 884)
        self.assertEqual(data["totals"]["representable_integer_count"], 745)
        self.assertEqual(data["totals"]["nonrepresentable_integer_count"], 139)
        self.assertEqual(data["totals"]["total_representation_count"], 218024)
        self.assertEqual(data["totals"]["independent_scan_mismatch_count"], 0)
        self.assertEqual(data["global_maximum"]["integer"], 97200)
        self.assertEqual(data["global_maximum"]["representation_count"], 1557)
        self.assertTrue(all(data["verification"].values()))
        self.assertFalse(data["claim_ceiling"]["phase_d_authorized"])
        self.assertFalse(data["claim_ceiling"]["goldbach_progress"])


if __name__ == "__main__":
    unittest.main()
