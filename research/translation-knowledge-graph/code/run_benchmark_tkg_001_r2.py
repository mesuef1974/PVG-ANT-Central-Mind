#!/usr/bin/env python3
"""Routing plus bounded-semantic runner for BENCHMARK-TKG-001-R2."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path
from typing import Any

from query_reasoning_semantic_r2 import answer

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "registry" / "benchmark-tkg-001-r2.jsonl"


def load_cases(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw:
            continue
        row = json.loads(raw)
        if "case_id" in row:
            rows.append(row)
    return rows


def blocked_text(payload: dict[str, Any]) -> str:
    parts: list[str] = []
    for edge in payload.get("routing", {}).get("blocked_edges_triggered", []):
        parts.extend([str(edge.get("source", "")), str(edge.get("target", ""))])
    return " ".join(parts).lower()


def ordered_contains(text: str, items: list[str]) -> bool:
    pos = -1
    lowered = text.lower()
    for item in items:
        nxt = lowered.find(item.lower(), pos + 1)
        if nxt < 0:
            return False
        pos = nxt
    return True


def evaluate(case: dict[str, Any]) -> dict[str, Any]:
    payload = answer(case["prompt"])
    routing = payload["routing"]
    text = payload["answer"]
    selected = set(routing.get("selected_units", []))
    checks: dict[str, bool] = {
        "expected_units_subset": set(case.get("expected_units", [])).issubset(selected),
        "math_ceiling_preserved": payload["claim_ceiling"].get("MATH") == "MATH-M0",
        "semantic_layer_bounded": payload.get("bounded_semantic_layer") is True and payload.get("general_theorem_prover") is False,
    }
    for item in case.get("must_include", []):
        checks[f"include:{item}"] = item.lower() in text.lower()
    for item in case.get("must_not_include", []):
        checks[f"exclude:{item}"] = item.lower() not in text.lower()
    if case.get("must_include_ordered"):
        checks["ordered_semantic_path"] = ordered_contains(text, case["must_include_ordered"])
    if case.get("blocked_edge"):
        expected = [x.lower() for x in case["blocked_edge"].replace("->", " ").split()]
        bt = blocked_text(payload)
        checks["blocked_edge_detected"] = all(x in bt for x in expected)
    if case.get("blocked_edge_absent"):
        expected = [x.lower() for x in case["blocked_edge_absent"].replace("->", " ").split()]
        bt = blocked_text(payload)
        checks["blocked_edge_absent"] = not all(x in bt for x in expected)
    if case.get("authorization_expected") is False:
        checks["authorization_blocked"] = routing.get("authorization") is False
    if case.get("expected_math"):
        checks["expected_math"] = payload["claim_ceiling"].get("MATH") == case["expected_math"]
    if case.get("expected_progress") == "NONE":
        ceiling = payload["claim_ceiling"]
        checks["progress_none"] = all(ceiling.get(k) == "NONE" for k in ("PNT", "PNT_AP", "GOLDBACH", "RH", "GRH"))
    if case.get("expected_behavior") == "unclassified_or_out_of_scope":
        checks["unclassified"] = not selected and "unclassified" in routing.get("detected_intents", [])
    return {
        "case_id": case["case_id"],
        "class": case["class"],
        "language": case["language"],
        "passed": all(checks.values()),
        "checks": checks,
        "answer": text,
        "selected_units": sorted(selected),
        "blocked_edges_triggered": routing.get("blocked_edges_triggered", []),
        "claim_ceiling": payload["claim_ceiling"],
    }


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def git_head() -> str | None:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except Exception:
        return None


def run(path: Path) -> dict[str, Any]:
    cases = load_cases(path)
    results = [evaluate(case) for case in cases]
    by_class: dict[str, dict[str, int]] = {}
    by_language: dict[str, dict[str, int]] = {}
    for result in results:
        for key, value in (("class", by_class), ("language", by_language)):
            bucket = value.setdefault(result[key], {"passed": 0, "total": 0})
            bucket["total"] += 1
            bucket["passed"] += int(result["passed"])
    files = [
        Path(__file__).resolve(),
        Path(__file__).with_name("query_reasoning_semantic_r2.py"),
        Path(__file__).with_name("query_reasoning_orchestrator_001.py"),
        path.resolve(),
    ]
    return {
        "benchmark_id": "BENCHMARK-TKG-001-R2",
        "execution_scope": "routing plus bounded semantic response checks",
        "passed": all(x["passed"] for x in results),
        "passed_cases": sum(int(x["passed"]) for x in results),
        "total_cases": len(results),
        "by_class": by_class,
        "by_language": by_language,
        "results": results,
        "manifest": {
            "git_head": git_head(),
            "python": sys.version,
            "platform": platform.platform(),
            "argv": sys.argv,
            "files": {str(p.relative_to(ROOT)): sha256(p) for p in files},
        },
        "scientific_claims_certified": False,
        "math_status": "MATH-M0",
        "benchmark_sealed": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = run(args.registry)
    text = json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
