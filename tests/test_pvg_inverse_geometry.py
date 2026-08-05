import unittest

from tools.pvg_inverse_geometry import (
    GeometryInputError,
    UINT64_LIMIT,
    factorint_64,
    inverse_geometry,
    parse_factorization,
)


class PVGInverseGeometryTests(unittest.TestCase):
    def test_origin(self):
        p = inverse_geometry(1)
        self.assertEqual(p["point_class"], "origin")
        self.assertEqual(p["omega"], 0)
        self.assertEqual(p["Omega"], 0)

    def test_prime_axis_generator(self):
        p = inverse_geometry(2)
        self.assertEqual(p["point_class"], "prime_axis_generator")
        self.assertEqual(p["support"], [2])
        self.assertEqual(p["primitive_ray"]["primitive_generator"], 2)

    def test_two_prime_floor_point(self):
        p = inverse_geometry(6)
        self.assertEqual(p["point_class"], "relative_interior_of_two_prime_face")
        self.assertEqual(p["valuation_vector"], {"2": 1, "3": 1})
        self.assertEqual(p["repeat_depth"], 0)
        self.assertTrue(p["primitive_ray"]["balanced_support_diagonal"])

    def test_misaligned_two_prime_point(self):
        p = inverse_geometry(12)
        self.assertEqual(p["omega"], 2)
        self.assertEqual(p["Omega"], 3)
        self.assertEqual(p["shape_partition"], [2, 1])
        self.assertEqual(p["primitive_ray"]["primitive_generator"], 12)
        self.assertEqual(p["primitive_ray"]["ray_index"], 1)

    def test_composite_balanced_ray(self):
        p = inverse_geometry(36)
        self.assertEqual(p["primitive_ray"]["primitive_generator"], 6)
        self.assertEqual(p["primitive_ray"]["ray_index"], 2)
        self.assertEqual(p["primitive_ray"]["power_identity"], "36 = 6^2")

    def test_three_prime_balanced_point(self):
        p = inverse_geometry(900)
        self.assertEqual(p["support"], [2, 3, 5])
        self.assertEqual(p["omega"], 3)
        self.assertEqual(p["Omega"], 6)
        self.assertEqual(p["radical"], 30)
        self.assertEqual(p["repeat_depth"], 3)
        self.assertEqual(p["shape_partition"], [2, 2, 2])
        self.assertEqual(p["primitive_ray"]["primitive_generator"], 30)
        self.assertEqual(p["primitive_ray"]["ray_index"], 2)
        self.assertEqual(p["divisibility_geometry"]["divisor_count"], 27)

    def test_known_64bit_composite(self):
        n = (1 << 63) - 1
        self.assertEqual(
            factorint_64(n),
            {7: 2, 73: 1, 127: 1, 337: 1, 92737: 1, 649657: 1},
        )

    def test_large_input_with_supplied_certified_factorization(self):
        n = 2**80 * 3**40
        p = inverse_geometry(n, "2^80,3^40")
        self.assertEqual(p["Omega"], 120)
        self.assertEqual(p["primitive_ray"]["primitive_generator"], 12)
        self.assertEqual(p["primitive_ray"]["ray_index"], 40)

    def test_large_input_without_factorization_is_refused(self):
        with self.assertRaises(GeometryInputError):
            inverse_geometry(UINT64_LIMIT)

    def test_supplied_factorization_must_match(self):
        with self.assertRaises(GeometryInputError):
            inverse_geometry(12, "2^2,3^2")

    def test_supplied_bases_must_be_prime(self):
        with self.assertRaises(GeometryInputError):
            parse_factorization("4^2,3")


if __name__ == "__main__":
    unittest.main()
