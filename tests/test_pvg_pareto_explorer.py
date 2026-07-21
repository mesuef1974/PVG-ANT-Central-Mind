from __future__ import annotations

import unittest
from pathlib import Path

from tools.pvg_multiobjective_geometry import analyze as multiobjective_analyze
from tools.pvg_pareto_frontier_geometry import analyze as frontier_analyze


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "web" / "pvg-pareto-explorer" / "index.html"
LAUNCHER = ROOT / "tools" / "open_pvg_pareto_explorer.ps1"


class PVGParetoExplorerTests(unittest.TestCase):
    def test_page_and_launcher_exist(self) -> None:
        self.assertTrue(PAGE.is_file())
        self.assertTrue(LAUNCHER.is_file())

    def test_page_is_self_contained(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        self.assertIn("<!doctype html>", text.lower())
        self.assertIn("<style>", text)
        self.assertIn("<script>", text)
        self.assertNotIn("<script src=", text.lower())
        self.assertNotIn("<link rel=\"stylesheet\"", text.lower())

    def test_registered_scope_is_visible(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        self.assertIn("const LEVEL=6", text)
        self.assertIn("28 نقطة", text)
        self.assertIn("جبهة باريتو", text)

    def test_3d_interaction_controls_are_present(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        for element_id in (
            "scene",
            "colorField",
            "heightField",
            "projection",
            "pointSize",
            "showAllEdges",
            "showFrontierEdges",
            "showLabels",
            "showStructure",
            "showFloor",
            "autoRotate",
            "resetCamera",
            "pointDetail",
        ):
            self.assertIn(f'id="{element_id}"', text)
        self.assertIn("pointermove", text)
        self.assertIn("wheel", text)
        self.assertIn("Shift + سحب", text)

    def test_high_contrast_number_labels(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        self.assertIn("rgba(2,7,13,.96)", text)
        self.assertIn("ctx.fillStyle='#fff'", text)
        self.assertIn("roundRect", text)

    def test_page_statistics_match_registered_analysis(self) -> None:
        mo = multiobjective_analyze([2, 3, 5], 6)
        fg = frontier_analyze([2, 3, 5], 6)
        self.assertEqual(mo["point_count"], 28)
        self.assertEqual(mo["global_pareto_frontier_size"], 19)
        self.assertEqual(fg["frontier_edge_count"], 27)
        self.assertEqual(fg["component_count"], 3)
        self.assertEqual(fg["cycle_rank"], 11)

    def test_launcher_targets_detached_worktree_page(self) -> None:
        text = LAUNCHER.read_text(encoding="utf-8")
        self.assertIn("D:\\PVG-ANT-Inverse-Geometry-001", text)
        self.assertIn("web\\pvg-pareto-explorer\\index.html", text)
        self.assertIn("Start-Process", text)


if __name__ == "__main__":
    unittest.main()
