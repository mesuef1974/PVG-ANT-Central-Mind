from __future__ import annotations

import unittest
from itertools import combinations
from pathlib import Path

try:
    from tools.pvg_deep_orbit_preimage_families import factor_support as support, successors
    from tools.pvg_local_additive_cell_atlas import factorint, is_prime, primes_up_to
except ModuleNotFoundError:
    from pvg_deep_orbit_preimage_families import factor_support as support, successors
    from pvg_local_additive_cell_atlas import factorint, is_prime, primes_up_to


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "research/pvg-space-deepening/synthesis-001-support-fiber-dynamics.md"


def unique_successor(face: tuple[int, ...]) -> tuple[int, ...]:
    targets = successors(face)
    if len(targets) != 1:
        raise AssertionError(f"expected one successor for {face}, found {targets}")
    return targets[0]


def orbit(start: tuple[int, ...], steps: int) -> list[tuple[int, ...]]:
    out = [start]
    current = start
    for _ in range(steps):
        current = unique_successor(current)
        out.append(current)
    return out


class PVGSupportFiberSynthesisTests(unittest.TestCase):
    def test_synthesis_document_exists(self) -> None:
        self.assertTrue(DOC.is_file())
        self.assertGreater(DOC.stat().st_size, 20_000)

    def test_document_has_required_sections(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        required = [
            "PVG الكامل وإسقاط الدعم",
            "مؤثر الانتقال",
            "قضايا دقيقة ناتجة من التعريف",
            "أمثلة عددية بسيطة",
            "ألياف المجموع والدعم",
            "خريطة PASS-013–024",
            "الترجمة العكسية إلى لغة ANT",
            "مصفوفة الادعاءات",
            "ما تعلمناه من النتائج السلبية",
            "بوابة PASS-025",
            "السقف العلمي",
        ]
        for token in required:
            self.assertIn(token, text)

    def test_support_projection_loses_exponents(self) -> None:
        self.assertEqual(support(10), (2, 5))
        self.assertEqual(support(20), (2, 5))
        self.assertNotEqual(factorint(10), factorint(20))

    def test_binary_face_has_unique_successor(self) -> None:
        for p, q in combinations(primes_up_to(100), 2):
            self.assertEqual(successors((p, q)), (support(p + q),))

    def test_source_destination_are_disjoint(self) -> None:
        for p, q in combinations(primes_up_to(100), 2):
            self.assertTrue(set((p, q)).isdisjoint(support(p + q)))

    def test_sum_fiber_24(self) -> None:
        representations = [(5, 19), (7, 17), (11, 13)]
        for p, q in representations:
            self.assertTrue(is_prime(p) and is_prime(q))
            self.assertEqual(p + q, 24)
            self.assertEqual(unique_successor((p, q)), (2, 3))
            self.assertEqual(unique_successor((2, 3)), (5,))

    def test_equal_support_different_sums(self) -> None:
        self.assertNotEqual(3 + 7, 7 + 13)
        self.assertEqual(support(3 + 7), support(7 + 13))
        self.assertEqual(
            orbit((3, 7), 2)[1:],
            orbit((7, 13), 2)[1:],
        )

    def test_706_orbit_certificate(self) -> None:
        expected = [
            (347, 359),
            (2, 353),
            (5, 71),
            (2, 19),
            (3, 7),
            (2, 5),
            (7,),
        ]
        self.assertEqual(sum(expected[0]), 706)
        self.assertEqual(orbit(expected[0], 6), expected)

    def test_all_registered_706_representations_share_tail(self) -> None:
        starts = [
            (227, 479),
            (239, 467),
            (257, 449),
            (263, 443),
            (317, 389),
            (347, 359),
        ]
        tails = []
        for start in starts:
            self.assertEqual(sum(start), 706)
            self.assertTrue(all(is_prime(value) for value in start))
            tails.append(orbit(start, 6)[1:])
        self.assertTrue(all(tail == tails[0] for tail in tails))

    def test_1774_depth_seven_certificate(self) -> None:
        expected = [
            (863, 911),
            (2, 887),
            (7, 127),
            (2, 67),
            (3, 23),
            (2, 13),
            (3, 5),
            (2,),
        ]
        self.assertEqual(sum(expected[0]), 1774)
        self.assertEqual(orbit(expected[0], 7), expected)

    def test_support_preimage_characterization_examples(self) -> None:
        for number in (10, 20, 40, 80):
            factors = factorint(number)
            self.assertEqual(set(factors), {2, 5})
            self.assertTrue(all(exponent >= 1 for exponent in factors.values()))

    def test_document_separates_exact_finite_and_open(self) -> None:
        text = DOC.read_text(encoding="utf-8")
        for token in (
            "Identity",
            "Finite-verified",
            "Reinterpretation / Diagnostic",
            "Candidate mechanism",
            "Missing literature certificate",
            "Open",
        ):
            self.assertIn(token, text)
        self.assertIn("لا تثبت هذه الوثيقة", text)
        self.assertIn("No original theorem certified", text)

    def test_all_pass_documents_exist(self) -> None:
        for number, slug in (
            (13, "local-additive-cell-atlas"),
            (14, "additive-face-transition-graph"),
            (15, "iterated-additive-face-dynamics"),
            (16, "additive-attraction-basins"),
            (17, "additive-basin-overlap-geometry"),
            (18, "additive-basin-depth-stability"),
            (19, "prime-bound-expansion-protocol"),
            (20, "pvg-visual-lab"),
            (21, "pvg-immersive-3d-visual-lab"),
            (22, "cross-bound-structural-stress-test"),
            (23, "minimum-closure-depth-growth"),
            (24, "deep-orbit-preimage-families"),
        ):
            path = ROOT / "research/pvg-space-deepening" / f"pass-{number:03d}-{slug}.md"
            self.assertTrue(path.is_file(), path)


if __name__ == "__main__":
    unittest.main()
