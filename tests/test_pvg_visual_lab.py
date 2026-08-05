from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "web" / "pvg-pareto-explorer" / "visual-lab.html"
LAUNCHER = ROOT / "tools" / "open_pvg_visual_lab.ps1"


class PVGVisualLabTests(unittest.TestCase):
    def test_page_and_launcher_exist(self) -> None:
        self.assertTrue(PAGE.is_file())
        self.assertTrue(LAUNCHER.is_file())
        self.assertGreater(PAGE.stat().st_size, 25000)

    def test_page_is_self_contained(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        self.assertIn("<style>", text)
        self.assertIn("<script>", text)
        self.assertNotIn("<script src=", text.lower())
        self.assertNotIn("http://", text.lower())
        self.assertNotIn("https://", text.lower())

    def test_controls_and_views_exist(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        for element_id in (
            "bound",
            "depth",
            "mode",
            "axisFilter",
            "edgeMin",
            "view-overview",
            "view-basins",
            "view-overlap",
            "view-signatures",
            "view-stability",
            "view-expansion",
            "view-trace",
            "view-audit",
            "graph",
            "traceInput",
        ):
            self.assertIn(f'id="{element_id}"', text)

    def test_live_engine_is_embedded(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
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
        self.assertIn("LIVE FINITE COMPUTATION", text)
        self.assertIn("NO GENERAL THEOREM", text)

    def test_registered_reference_values_are_visible(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        self.assertIn("start:300,single:195,multiple:105", text)
        self.assertIn("start:595,single:337,multiple:258", text)
        self.assertIn("start:1035,single:517,multiple:518", text)
        self.assertIn('"{5,7}":150', text)

    def test_javascript_syntax(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        script = text.split("<script>", 1)[1].rsplit("</script>", 1)[0]
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "visual-lab.js"
            path.write_text(script, encoding="utf-8")
            run = subprocess.run(
                ["node", "--check", str(path)], capture_output=True, text=True
            )
        self.assertEqual(run.returncode, 0, run.stderr)

    def test_engine_reproduces_registered_cumulative_rows(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        engine = text.split("/*ENGINE_START*/", 1)[1].split("/*ENGINE_END*/", 1)[0]
        expected = {
            100: [300, 195, 105, 10, 19, 3, 13, 6, 153, 75],
            150: [595, 337, 258, 14, 29, 4, 18, 8, 325, 157],
            200: [1035, 517, 518, 17, 38, 5, 22, 9, 594, 306],
        }
        javascript = engine + """
console.log(JSON.stringify(Object.fromEntries([100,150,200].map(l=>{
  const a=analyze(l,5,'cumulative');
  return [l,[a.startCount,a.single,a.multiple,a.axisCount,a.signatureCount,
    a.maximumRank,a.edgeCount,a.activeComponent.length,a.largest.size,
    a.strongest.weight]];
}))));
"""
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "engine.js"
            path.write_text(javascript, encoding="utf-8")
            run = subprocess.run(
                ["node", str(path)], capture_output=True, text=True, timeout=30
            )
        self.assertEqual(run.returncode, 0, run.stderr)
        actual = {int(key): value for key, value in json.loads(run.stdout).items()}
        self.assertEqual(actual, expected)

    def test_cohort_counts_are_reproduced(self) -> None:
        text = PAGE.read_text(encoding="utf-8")
        engine = text.split("/*ENGINE_START*/", 1)[1].split("/*ENGINE_END*/", 1)[0]
        javascript = engine + """
console.log(JSON.stringify([analyze(150,5,'cohort'),analyze(200,5,'cohort')]
  .map(a=>[a.startCount,a.single,a.multiple,a.largest.axis,a.largest.size,
    a.strongest.weight])));
"""
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "engine.js"
            path.write_text(javascript, encoding="utf-8")
            run = subprocess.run(
                ["node", str(path)], capture_output=True, text=True, timeout=30
            )
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(
            json.loads(run.stdout),
            [[295, 142, 153, 5, 172, 82], [440, 180, 260, 5, 269, 149]],
        )

    def test_launcher_targets_visual_lab(self) -> None:
        text = LAUNCHER.read_text(encoding="utf-8")
        self.assertIn("D:\\PVG-ANT-Inverse-Geometry-001", text)
        self.assertIn("visual-lab.html", text)
        self.assertIn("Start-Process", text)


if __name__ == "__main__":
    unittest.main()
