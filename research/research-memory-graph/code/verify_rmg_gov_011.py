#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FILES = [
    ROOT / "research/research-memory-graph/registry/prime-distribution-ap-character-chebyshev.jsonl",
    ROOT / "research/research-memory-graph/registry/primitive-characters-conductors-gauss-functional-equation.jsonl",
]
REQUIRED = {
    "record_id", "record_type", "name", "ant_standard_definition",
    "ant_to_pvg_map", "pvg_geometric_object", "pvg_to_ant_return_map",
    "translation_type", "injectivity_status", "kernel_or_information_loss",
    "assimilation_level", "math_contribution_level", "operational_maturity",
    "certificate_strength", "claim_ceiling", "legacy_assimilation_level",
}
PLACEHOLDERS = {"NOT_YET_ANALYSED", "NOT_YET_ANALYZED", "UNMAPPED_LEGACY_VALUE", "AMBIGUOUS_REQUIRES_REVIEW"}

def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def contains_placeholder(value) -> bool:
    if isinstance(value, dict):
        return any(contains_placeholder(v) for v in value.values())
    if isinstance(value, list):
        return any(contains_placeholder(v) for v in value)
    return str(value) in PLACEHOLDERS

def main() -> int:
    rows = [row for path in FILES for row in load(path)]
    assert len(rows) == 24, len(rows)
    ids = [row["record_id"] for row in rows]
    assert len(ids) == len(set(ids))
    for row in rows:
        assert REQUIRED <= set(row), (row.get("record_id"), REQUIRED - set(row))
        assert row["assimilation_level"].startswith("ASSIM-L")
        assert row["math_contribution_level"] == "MATH-M0"
        assert not any(contains_placeholder(row[field]) for field in REQUIRED if field in row)
    by_id = {row["record_id"]: row for row in rows}
    assert by_id["RMG003B-PNTAP-001"]["assimilation_level"] == "ASSIM-L2"
    assert by_id["RMG-003-C-0001"]["assimilation_level"] == "ASSIM-L2"
    assert by_id["RMG-003-C-0009"]["assimilation_level"] == "ASSIM-L2"
    assert by_id["RMG003B-GRH-001"]["claim_ceiling"] == "No GRH progress."
    print("RMG-GOV-011 verification: PASS 24/24")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
