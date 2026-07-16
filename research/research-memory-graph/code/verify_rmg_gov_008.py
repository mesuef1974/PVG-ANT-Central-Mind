#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path

FILES = {
    "research/research-memory-graph/registry/weyl-vdc-exponential-sum-minor-arc.jsonl": 12,
    "research/research-memory-graph/registry/prime-weighted-exponential-vaughan-major-minor.jsonl": 12,
}
REQUIRED = {
    "record_id", "ant_standard_definition", "ant_to_pvg_map",
    "pvg_geometric_object", "pvg_to_ant_return_map", "translation_type",
    "injectivity_status", "kernel_or_information_loss", "assimilation_level",
    "math_contribution_level", "operational_maturity", "certificate_strength",
    "claim_ceiling",
}

def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def main() -> int:
    errors: list[str] = []
    ids: list[str] = []
    total = 0
    for raw, expected in FILES.items():
        rows = load(Path(raw))
        total += len(rows)
        if len(rows) != expected:
            errors.append(f"{raw}: expected {expected}, got {len(rows)}")
        for row in rows:
            ids.append(row.get("record_id", ""))
            missing = REQUIRED - row.keys()
            if missing:
                errors.append(f"{row.get('record_id')}: missing {sorted(missing)}")
            if not str(row.get("assimilation_level", "")).startswith("ASSIM-L"):
                errors.append(f"{row.get('record_id')}: bad assimilation namespace")
            if row.get("math_contribution_level") != "MATH-M0":
                errors.append(f"{row.get('record_id')}: unauthorized math promotion")
            if "legacy_assimilation_level" not in row:
                errors.append(f"{row.get('record_id')}: legacy level not preserved")
    if len(ids) != len(set(ids)):
        errors.append("duplicate record ids")
    if total != 24:
        errors.append(f"expected total 24, got {total}")
    if errors:
        for error in errors:
            print("FAIL", error)
        return 1
    print("PASS 24/24 canonical records; IDs preserved; MATH-M0 retained")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
