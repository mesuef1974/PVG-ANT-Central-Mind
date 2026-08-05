from __future__ import annotations

import unittest

try:
    from tools.pvg_inverse_integer_fibers import integer_fiber, support_universe
    from tools.pvg_inverse_prime_fiber_parity import (
        odd_prime_fiber_formula,
        support_parity,
        support_parity_certificate,
        support_parity_route,
    )
    from tools.pvg_inverse_prime_fibers import prime_pair_fiber
except ModuleNotFoundError:
    from pvg_inverse_integer_fibers import integer_fiber, support_universe
    from pvg_inverse_prime_fiber_parity import (
        odd_prime_fiber_formula,
        support_parity,
        support_parity_certificate,
        support_parity_route,
    )
    from pvg_inverse_prime_fibers import prime_pair_fiber


class InversePrimeFiberParityTests(unittest.TestCase):
    def test_support_parity_identity(self) -> None:
        self.assertEqual(support_parity((2, 3, 5)), "even")
        self.assertEqual(support_parity((3, 5, 7)), "odd")
        self.assertEqual(support_parity_route((2, 11)), "odd_plus_odd")
        self.assertEqual(support_parity_route((3, 11)), "two_plus_odd")

    def test_odd_prime_fiber_formula(self) -> None:
        self.assertEqual(odd_prime_fiber_formula(9), ((2, 7),))
        self.assertEqual(odd_prime_fiber_formula(27), tuple())
        self.assertEqual(odd_prime_fiber_formula(24), tuple())
        for n in range(5, 500, 2):
            self.assertEqual(odd_prime_fiber_formula(n), prime_pair_fiber(n))

    def test_complete_registered_support_box(self) -> None:
        checked = 0
        for support in support_universe(11, (1, 2, 3)):
            expected_even = 2 in support
            for value in integer_fiber(support, 100_000):
                self.assertEqual(value % 2 == 0, expected_even)
                if not expected_even:
                    self.assertEqual(prime_pair_fiber(value), odd_prime_fiber_formula(value))
                checked += 1
        self.assertEqual(checked, 884)

    def test_certificates(self) -> None:
        for support in support_universe(11, (1, 2, 3)):
            certificate = support_parity_certificate(support, 100_000)
            self.assertTrue(all(certificate["verification"].values()))
            self.assertFalse(certificate["claim_ceiling"]["phase_d_authorized"])
            self.assertFalse(certificate["claim_ceiling"]["goldbach_progress"])


if __name__ == "__main__":
    unittest.main()
