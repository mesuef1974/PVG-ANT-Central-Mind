#!/usr/bin/env python3
"""Static verifier for RMG-GOV-004 pilot reclassification."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GOV = ROOT / "research/research-memory-graph/governance"
OVERLAY = GOV / "rmg-pilot-reclassification.jsonl"
REPORT = GOV / "RMG-GOV-004-PILOT-RECLASSIFICATION.md"
UNIT = ROOT / "research/research-memory-graph/units/RMG-GOV-004.md"

REQUIRED = {
    "id", "claim_pattern", "source_locator", "review_status",
    "assimilation_level", "math_contribution_level",
    "operational_maturity", "certificate_strength",
    "pvg_necessity_level", "removal_test_result",
    "what_breaks_without_pvg", "classical_reduction",
    "novelty_class", "prior_art_status", "claim_ceiling",
}


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            row = json.loads(line)
            missing = REQUIRED - row.keys()
            assert not missing, f"line {i} missing {sorted(missing)}"
            rows.append(row)
    return rows


def main() -> None:
    assert REPORT.exists()
    assert OVERLAY.exists()
    assert UNIT.exists()
    rows = load_jsonl(OVERLAY)
    assert len(rows) == 5
    assert len({r["id"] for r in rows}) == 5
    assert all(r["assimilation_level"].startswith("ASSIM-") for r in rows)
    assert all(r["math_contribution_level"].startswith("MATH-") for r in rows)
    assert all(r["pvg_necessity_level"].startswith("PVG-N") for r in rows)
    assert any("Goldbach" in r["claim_ceiling"] for r in rows)
    assert any("RH_PROGRESS=NONE" in r["claim_ceiling"] for r in rows)
    assert any(r["pvg_necessity_level"] == "PVG-N3" for r in rows)
    assert not any(r["math_contribution_level"] not in {"MATH-M0", "MATH-M1"} for r in rows)
    print("PASS 10/10")


if __name__ == "__main__":
    main()
