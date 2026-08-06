#!/usr/bin/env python3
"""Static verification for RMG-GOV-002 artifacts.

This verifier checks the adapter contract and migration registry. It does not claim
that a repository-wide migration has already been executed.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADAPTER = ROOT / "code" / "rmg_schema_adapter.py"
REGISTRY = ROOT / "governance" / "rmg-migration-registry.jsonl"


def load_adapter():
    spec = importlib.util.spec_from_file_location("rmg_schema_adapter", ADAPTER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load adapter")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    checks = []
    adapter = load_adapter()

    sample = {
        "id": "SAMPLE",
        "ant_view": "standard ANT object",
        "pvg_view": "PVG diagnostic",
        "inverse_status": "DIAGNOSTIC_ONLY",
        "assimilation_level": "L5_COMPUTATIONALLY_REGRESSION_TESTED",
        "claim_ceiling": "finite regression only",
    }
    adapted = adapter.adapt_record(sample, "sample.jsonl:1")

    required = set(adapter.REQUIRED)
    checks.append(("canonical_required_fields", required.issubset(adapted)))
    checks.append(("assimilation_namespace", adapted["assimilation_level"] == "ASSIM-L5"))
    checks.append(("math_not_auto_promoted", adapted["math_contribution_level"] == "MATH-M0"))
    checks.append(("source_preserved", adapted["source_record"] == sample))
    checks.append(("pvg_gate_explicit", adapted["pvg_necessity_level"] == "NOT_AUDITED"))

    rows = [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]
    ids = [row["id"] for row in rows]
    checks.append(("migration_registry_nonempty", len(rows) >= 5))
    checks.append(("migration_ids_unique", len(ids) == len(set(ids))))
    checks.append(("source_preservation_required", all(row.get("preserve_source") is True for row in rows)))
    checks.append(("review_not_bypassed", all(row.get("review_required") is True for row in rows)))

    failed = [name for name, ok in checks if not ok]
    print(json.dumps({"checks": [{"name": n, "pass": ok} for n, ok in checks], "passed": len(checks)-len(failed), "total": len(checks), "failed": failed}, indent=2))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
