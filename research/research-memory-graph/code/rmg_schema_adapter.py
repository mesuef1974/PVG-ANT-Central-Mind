#!/usr/bin/env python3
"""Non-destructive adapter from legacy RMG records to the RMG-GOV-001 schema.

The adapter never overwrites source records. Ambiguous values remain explicit.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

BARE_ASSIM = {
    "L0_MENTIONED": "ASSIM-L0",
    "L1_DEFINED_IN_ANT": "ASSIM-L1",
    "L2_TRANSLATED_TO_PVG": "ASSIM-L2",
    "L3_BIDIRECTIONALLY_ANALYZED": "ASSIM-L3",
    "L4_NUMERICALLY_VERIFIED": "ASSIM-L4",
    "L5_COMPUTATIONALLY_REGRESSION_TESTED": "ASSIM-L5",
    "L6_FORMALLY_VERIFIED": "ASSIM-L6",
    "L7_BENCHMARKED_FOR_REASONING": "ASSIM-L7",
}

REQUIRED = (
    "ant_standard_definition",
    "ant_to_pvg_map",
    "pvg_geometric_object",
    "pvg_to_ant_return_map",
    "translation_type",
    "injectivity_status",
    "kernel_or_information_loss",
    "assimilation_level",
    "math_contribution_level",
    "operational_maturity",
    "certificate_strength",
    "claim_ceiling",
)


def explicit_missing(reason: str = "NOT_YET_ANALYSED") -> dict[str, str]:
    return {"status": reason}


def adapt_record(record: dict[str, Any], source_path: str = "UNKNOWN") -> dict[str, Any]:
    src = copy.deepcopy(record)
    out: dict[str, Any] = {
        "source_path": source_path,
        "source_record": src,
        "migration_status": "MAPPED_WITH_EXPLICIT_ASSUMPTION",
        "mapping_notes": [],
    }

    out["ant_standard_definition"] = src.get("ant_standard_definition", src.get("ant_view", explicit_missing()))
    out["ant_to_pvg_map"] = src.get("ant_to_pvg_map", src.get("pvg_view", explicit_missing()))
    out["pvg_geometric_object"] = src.get("pvg_geometric_object", src.get("pvg_view", explicit_missing()))
    out["pvg_to_ant_return_map"] = src.get("pvg_to_ant_return_map", explicit_missing())
    out["translation_type"] = src.get("translation_type", "NOT_YET_ANALYSED")
    out["injectivity_status"] = src.get("injectivity_status", src.get("inverse_status", "NOT_YET_ANALYSED"))
    out["kernel_or_information_loss"] = src.get("kernel_or_information_loss", explicit_missing())

    legacy_level = src.get("assimilation_level", "NOT_YET_ANALYSED")
    out["assimilation_level"] = BARE_ASSIM.get(legacy_level, legacy_level)
    if legacy_level not in BARE_ASSIM and not str(legacy_level).startswith("ASSIM-"):
        out["mapping_notes"].append("assimilation level requires review")
        out["migration_status"] = "AMBIGUOUS_REQUIRES_REVIEW"

    out["math_contribution_level"] = src.get("math_contribution_level", "MATH-M0")
    out["operational_maturity"] = src.get("operational_maturity", "OPS-LEGACY-UNCLASSIFIED")
    out["certificate_strength"] = src.get("certificate_strength", "CERT-LEGACY-UNCLASSIFIED")
    out["claim_ceiling"] = src.get("claim_ceiling", explicit_missing())

    out["pvg_necessity_level"] = src.get("pvg_necessity_level", "NOT_AUDITED")
    out["removal_test_result"] = src.get("removal_test_result", "NOT_AUDITED")
    out["what_breaks_without_pvg"] = src.get("what_breaks_without_pvg", "NOT_AUDITED")
    out["classical_reduction"] = src.get("classical_reduction", "NOT_AUDITED")
    out["novelty_class"] = src.get("novelty_class", "NOT_AUDITED")
    out["prior_art_status"] = src.get("prior_art_status", "NOT_AUDITED")

    missing = [field for field in REQUIRED if field not in out]
    if missing:
        raise ValueError(f"adapter bug: missing canonical fields {missing}")
    return out


def adapt_jsonl(source: Path, destination: Path) -> int:
    rows = []
    for line_no, line in enumerate(source.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        record = json.loads(line)
        rows.append(adapt_record(record, f"{source}:{line_no}"))
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in rows) + "\n", encoding="utf-8")
    return len(rows)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    print(adapt_jsonl(args.source, args.destination))
