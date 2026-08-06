#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "translation-knowledge-graph/registry/tkg-001-von-mangoldt-core.jsonl"
REQUIRED = {
    "record_id", "record_type", "assimilation_level",
    "math_contribution_level", "operational_maturity",
    "certificate_strength", "claim_ceiling",
}


def main() -> None:
    records = [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]
    ids = [r["record_id"] for r in records]
    assert len(records) == 7
    assert len(ids) == len(set(ids))
    for record in records:
        missing = REQUIRED - set(record)
        assert not missing, (record.get("record_id"), sorted(missing))
        assert str(record["assimilation_level"]).startswith("ASSIM-")
        assert record["math_contribution_level"] == "MATH-M0"
    core = next(r for r in records if r["record_id"] == "TKG001-NODE-LAMBDA")
    assert core["translation_type"] == "BIJECTIVE_ON_ENCODED_INTEGER_POINTS"
    rejection = next(r for r in records if r["record_id"] == "TKG001-REJECT-SINGLE-AXIS-PNT")
    assert rejection["decision"] == "REJECT"
    print("TKG-001 verification: PASS 7/7")


if __name__ == "__main__":
    main()
