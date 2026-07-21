from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "web" / "pvg-pareto-explorer" / "visual-lab-3d.html"
LAUNCHER = ROOT / "tools" / "open_pvg_visual_lab_3d.ps1"
STYLE = ROOT / "web" / "pvg-pareto-explorer" / "assets" / "pvg-3d-style.css"
ENGINE = ROOT / "web" / "pvg-pareto-explorer" / "assets" / "pvg-3d-engine.js"
SCENES = ROOT / "web" / "pvg-pareto-explorer" / "assets" / "pvg-3d-scenes.js"


class PVGVisualLab3DTests(unittest.TestCase):
    def page_text(self) -> str:
        return PAGE.read_text(encoding="utf-8")

    def engine_text(self) -> str:
        return ENGINE.read_text(encoding="utf-8")

    def scenes_text(self) -> str:
        return SCENES.read_text(encoding="utf-8")

    def all_text(self) -> str:
        return "\n".join((self.page_text(), self.engine_text(), self.scenes_text()))

    def run_node(self, javascript: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "check.js"
            path.write_text(javascript, encoding="utf-8")
            return subprocess.run(
                ["node", str(path)], capture_output=True, text=True, timeout=35
            )

    def test_page_and_launcher_exist(self) -> None:
        for path in (PAGE, STYLE, ENGINE, SCENES, LAUNCHER):
            self.assertTrue(path.is_file(), path)
        total = sum(path.stat().st_size for path in (PAGE, STYLE, ENGINE, SCENES))
        self.assertGreater(total, 30000)

    def test_page_is_self_contained(self) -> None:
        text = self.page_text().lower()
        self.assertIn("<canvas id=\"scene\"", text)
        self.assertIn('href="./assets/pvg-3d-style.css"', text)
        self.assertIn('src="./assets/pvg-3d-engine.js"', text)
        self.assertIn('src="./assets/pvg-3d-scenes.js"', text)
        for content in (text, STYLE.read_text(encoding="utf-8").lower(), self.all_text().lower()):
            self.assertNotIn("http://", content)
            self.assertNotIn("https://", content)

    def test_seven_immersive_scenes_are_registered(self) -> None:
        text = self.all_text()
        for scene in (
            "space",
            "pascal",
            "basins",
            "overlap",
            "stability",
            "expansion",
            "trace",
        ):
            self.assertIn(f'data-scene="{scene}"', text)
            self.assertIn(f"{scene}:", text)
        self.assertIn("فضاء PVG", text)
        self.assertIn("الهوية الباسكالية", text)
        self.assertIn("كوكبة تداخل الأحواض", text)

    def test_true_3d_camera_and_interaction_controls_exist(self) -> None:
        text = self.all_text()
        for token in (
            "function rotate3",
            "function project",
            "function line3",
            "function poly3",
            "function point3",
            "pointermove",
            "wheel",
            "Shift + سحب",
            "autoRotate",
            "resetCamera",
            "zoomIn",
            "zoomOut",
        ):
            self.assertIn(token, text)

    def test_live_finite_engine_is_embedded(self) -> None:
        text = self.all_text()
        for name in (
            "primesUpTo",
            "factorSupport",
            "successors",
            "traceFace",
            "startFaces",
            "components",
            "analyze",
        ):
            self.assertIn(f"function {name}", text)
        self.assertIn("SELF-CONTAINED 3D", text)
        self.assertIn("NO GENERAL THEOREM", text)

    def test_javascript_syntax(self) -> None:
        for source in (ENGINE, SCENES):
            run = subprocess.run(
                ["node", "--check", str(source)],
                capture_output=True,
                text=True,
            )
            self.assertEqual(run.returncode, 0, f"{source}: {run.stderr}")

    def test_engine_reproduces_registered_bound_results(self) -> None:
        expected = {
            100: [300, 195, 105, 10, 19, 3, 13, 6, 153, 75],
            150: [595, 337, 258, 14, 29, 4, 18, 8, 325, 157],
            200: [1035, 517, 518, 17, 38, 5, 22, 9, 594, 306],
        }
        javascript = self.engine_text() + """
console.log(JSON.stringify(Object.fromEntries([100,150,200].map(L=>{
  const a=analyze(L,5,'cumulative');
  return [L,[a.startCount,a.single,a.multiple,a.axisCount,a.signatureCount,
    a.maximumRank,a.edgeCount,a.activeComponent.length,a.largest.size,
    a.strongest.weight]];
}))));
"""
        run = self.run_node(javascript)
        self.assertEqual(run.returncode, 0, run.stderr)
        actual = {int(k): v for k, v in json.loads(run.stdout).items()}
        self.assertEqual(actual, expected)

    def test_special_depth_five_faces_end_at_axis_two(self) -> None:
        javascript = self.engine_text() + """
const a=traceFace([37,97],5), b=traceFace([61,73],5);
console.log(JSON.stringify([
  [a.terminalAxes,a.unresolved,a.levels.length],
  [b.terminalAxes,b.unresolved,b.levels.length]
]));
"""
        run = self.run_node(javascript)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(
            json.loads(run.stdout),
            [[[2], False, 6], [[2], False, 6]],
        )

    def test_registered_visual_findings_are_explicit(self) -> None:
        text = self.all_text()
        self.assertIn("{5,7}: <b>0 → 5 → 15</b>", text)
        self.assertIn("3 → 4 → 5", text)
        self.assertIn("6 → 8 → 9", text)
        self.assertIn("300,single:195,multiple:105", text)
        self.assertIn("1035,single:517,multiple:518", text)

    def test_launcher_targets_detached_worktree(self) -> None:
        text = LAUNCHER.read_text(encoding="utf-8")
        self.assertIn("D:\\PVG-ANT-Inverse-Geometry-001", text)
        self.assertIn("visual-lab-3d.html", text)
        self.assertIn("Start-Process", text)


if __name__ == "__main__":
    unittest.main()
