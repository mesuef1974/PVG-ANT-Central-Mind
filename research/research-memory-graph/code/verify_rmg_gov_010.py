#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FILES = {
    "research/research-memory-graph/registry/additive-characters-exponential-sums-fourier-cancellation.jsonl": 12,
    "research/research-memory-graph/registry/circle-method-major-minor-singular-series.jsonl": 12,
}
REQUIRED = {
    "record_id", "ant_standard_definition", "ant_to_pvg_map", "pvg_geometric_object",
    "pvg_to_ant_return_map", "translation_type", "injectivity_status",
    "kernel_or_information_loss", "assimilation_level", "math_contribution_level",
    "operational_maturity", "certificate_strength", "claim_ceiling",
    "legacy_assimilation_level",
}
PLACEHOLDERS = {"NOT_YET_ANALYSED", "NOT_YET_ANALYZED", "UNMAPPED_LEGACY_VALUE", "AMBIGUOUS_REQUIRES_REVIEW"}


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def nested_values(value):
    if isinstance(value, dict):
        for item in value.values():
            yield from nested_values(item)
    elif isinstance(value, list):
        for item in value:
            yield from nested_values(item)
    else:
        yield str(value)


def main() -> int:
    all_rows: list[dict] = []
    for rel, expected in FILES.items():
        rows = load(ROOT / rel)
        assert len(rows) == expected, (rel, len(rows), expected)
        all_rows.extend(rows)
    ids = [row["record_id"] for row in all_rows]
    assert len(ids) == 24
    assert len(ids) == len(set(ids))
    for row in all_rows:
        assert not (REQUIRED - set(row)), (row.get("record_id"), sorted(REQUIRED - set(row)))
        assert str(row["assimilation_level"]).startswith("ASSIM-L")
        assert row["math_contribution_level"] == "MATH-M0"
        assert str(row["operational_maturity"]).startswith("OPS-")
        assert str(row["certificate_strength"]).startswith("CERT-")
        values = set(nested_values({field: row[field] for field in REQUIRED if field in row}))
        assert not (values & PLACEHOLDERS), (row["record_id"], values & PLACEHOLDERS)
    assert next(r for r in all_rows if r["record_id"] == "RMG005A-LEAN")["assimilation_level"] == "ASSIM-L2"
    assert next(r for r in all_rows if r["record_id"] == "RMG-005-B-012")["assimilation_level"] == "ASSIM-L2"
    print("RMG-GOV-010: PASS 24/24 canonical records; no mathematical promotion; honest downgrades preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
