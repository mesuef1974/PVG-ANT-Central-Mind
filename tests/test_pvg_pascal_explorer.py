from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "web" / "pvg-pareto-explorer" / "pascal.html"
LAUNCHER = ROOT / "tools" / "open_pvg_pascal_explorer.ps1"


class PVGPascalExplorerTests(unittest.TestCase):
    def test_page_and_launcher_exist(self) -> None:
        self.assertTrue(PAGE.is_file())
        self.assertTrue(LAUNCHER.is_file())

    def test_page_is_self_contained(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        self.assertIn("<!doctype html>", text.lower())
        self.assertIn("<style>", text)
        self.assertIn("<script>", text)
        self.assertNotIn("<script src=", text.lower())

    def test_registered_scope_and_identity_are_visible(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        self.assertIn("const LEVEL=6", text)
        self.assertIn("2g + 3g = 5g", text)
        self.assertIn("المحاور 2، 3، 5", text)

    def test_interaction_controls_exist(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        for element_id in (
            "scene",
            "slice",
            "pair",
            "prev",
            "next",
            "play",
            "reset",
            "showAll",
            "showEdges",
            "showLabels",
            "showWeights",
            "formula",
            "weight",
        ):
            self.assertIn(f'id="{element_id}"', text)

    def test_exact_cell_formula_is_encoded(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        self.assertIn("left:byKey.get(`${a+1},${b},${c}`)", text)
        self.assertIn("right:byKey.get(`${a},${b+1},${c}`)", text)
        self.assertIn("top:byKey.get(`${a},${b},${c+1}`)", text)
        self.assertIn("2**a*3**b*5**c", text)

    def test_multinomial_weight_is_separate(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        self.assertIn("multinomial", text)
        self.assertIn("القيمة العددية والوزن المساري ليسا الشيء نفسه", text)

    def test_launcher_targets_pascal_page(self) -> None:
        text = LAUNCHER.read_text(encoding="utf-8")
        self.assertIn("D:\\PVG-ANT-Inverse-Geometry-001", text)
        self.assertIn("web\\pvg-pareto-explorer\\pascal.html", text)
        self.assertIn("Start-Process", text)


if __name__ == "__main__":
    unittest.main()
