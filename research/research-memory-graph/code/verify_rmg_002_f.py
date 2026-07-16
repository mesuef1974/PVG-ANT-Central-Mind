#!/usr/bin/env python3
"""RMG-002-F registry and scientific-boundary verifier (stdlib only)."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "zeta-zero-explicit-formula-boundary.jsonl"
RESULT = ROOT / "results" / "rmg_002_f_verification.json"

def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def run() -> dict:
    records = load_jsonl(REGISTRY)
    checks: list[dict] = []
    def record(check_id: str, ok: bool, evidence: dict) -> None:
        checks.append({"check_id": check_id, "status": "PASS" if ok else "FAIL", "evidence": evidence})
    ids = [r["record_id"] for r in records]
    record("CHK-F-REGISTRY-COUNT", len(records) == 12, {"records": len(records)})
    record("CHK-F-UNIQUE", len(set(ids)) == len(ids), {"unique": len(set(ids))})
    record("CHK-F-COMPONENTS", sum(r.get("kind") == "explicit_formula_component" for r in records) == 3, {})
    record("CHK-F-NEGATIVE", sum(r.get("kind") == "claim_rejection" for r in records) == 2, {})
    record("CHK-F-BOUNDARY", sum(r.get("kind") == "boundary" for r in records) >= 2, {})
    record("CHK-F-TRANSLATION", sum(r.get("kind") == "translation" for r in records) == 2, {})
    passed = sum(c["status"] == "PASS" for c in checks)
    return {"unit":"RMG-002-F","status":"PASS" if passed == len(checks) else "FAIL","summary":{"passed":passed,"total":len(checks)},"checks":checks,"scientific_ceiling":"dependency and boundary registry only; no zero recovery and no RH progress"}

def main() -> int:
    result = run()
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    print(text)
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(text + "\n", encoding="utf-8")
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
