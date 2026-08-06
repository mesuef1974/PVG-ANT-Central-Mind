#!/usr/bin/env python3
"""Static governance verifier for RMG-GOV-001.

This verifier is intentionally conservative. It checks the governance files added by
RMG-GOV-001 and scans RMG JSONL records for ambiguous bare L-level values and PVG
claim phrases lacking necessity fields. It does not rewrite files.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RMG = ROOT / "research" / "research-memory-graph"

REQUIRED_SCHEMA_FIELDS = {
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
}

PVG_CLAIM_RE = re.compile(r"PVG contribution|PVG-derived|new PVG theorem|PVG mechanism", re.I)
BARE_LEVEL_RE = re.compile(r"^L[0-7](?:_|$)")


def iter_jsonl(path: Path):
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            yield line_no, json.loads(line)


def main() -> int:
    failures: list[str] = []
    warnings: list[str] = []

    governance_files = [
        RMG / "governance" / "RMG-GOV-001-NAMESPACE-AND-SCHEMA.md",
        RMG / "governance" / "RMG-GOV-001-PVG-NECESSITY-GATE.md",
        RMG / "governance" / "rmg-governance-supersession.jsonl",
    ]
    for path in governance_files:
        if not path.exists():
            failures.append(f"missing governance file: {path.relative_to(ROOT)}")

    registry_paths = sorted((RMG / "registry").glob("*.jsonl"))
    for path in registry_paths:
        for line_no, record in iter_jsonl(path):
            level = record.get("assimilation_level")
            if isinstance(level, str) and BARE_LEVEL_RE.match(level):
                warnings.append(
                    f"legacy bare assimilation level: {path.relative_to(ROOT)}:{line_no}:{level}"
                )

            text = json.dumps(record, ensure_ascii=False)
            if PVG_CLAIM_RE.search(text):
                needed = {
                    "pvg_necessity_level",
                    "removal_test_result",
                    "what_breaks_without_pvg",
                    "classical_reduction",
                    "novelty_class",
                    "prior_art_status",
                }
                missing = sorted(needed - set(record))
                if missing:
                    warnings.append(
                        f"PVG claim pending necessity migration: {path.relative_to(ROOT)}:{line_no}:"
                        + ",".join(missing)
                    )

    status = "PASS_WITH_MIGRATION_WARNINGS" if not failures else "FAIL"
    report = {
        "unit": "RMG-GOV-001",
        "status": status,
        "failures": failures,
        "warnings": warnings,
        "warning_count": len(warnings),
        "note": "Warnings identify retrospective migration debt and do not certify migrated compliance.",
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
