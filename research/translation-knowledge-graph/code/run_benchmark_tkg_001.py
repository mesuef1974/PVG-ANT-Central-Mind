#!/usr/bin/env python3
"""Structural runner for BENCHMARK-TKG-001.

This runner evaluates orchestrator routing and governance invariants. It does not
certify analytic theorems or promote MATH status.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from query_reasoning_orchestrator_001 import orchestrate


DEFAULT_REGISTRY = Path(__file__).resolve().parents[1] / "registry" / "benchmark-tkg-001.jsonl"


def load_cases(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            if "case_id" in row:
                rows.append(row)
    return rows


def normalize_units(payload: dict[str, Any]) -> set[str]:
    return set(payload.get("selected_units", []))


def evaluate_case(case: dict[str, Any]) -> dict[str, Any]:
    output = orchestrate(case["prompt"], supplied=[])
    selected = normalize_units(output)
    expected = set(case.get("expected_units", []))
    checks: dict[str, bool] = {
        "expected_units_subset": expected.issubset(selected),
        "math_ceiling_preserved": output.get("claim_ceiling", {}).get("MATH") == "MATH-M0",
        "automatic_promotion_blocked": output.get("automatic_math_promotion") is False,
    }

    blocked = case.get("blocked_edge")
    if blocked:
        triggered = " ".join(output.get("blocked_edges_triggered", []))
        checks["blocked_edge_detected"] = all(token.lower() in triggered.lower() for token in blocked.replace("->", " ").split())

    if case.get("authorization_expected") is False:
        checks["authorization_blocked"] = output.get("authorization", False) is False

    if case.get("expected_progress") == "NONE":
        ceiling = output.get("claim_ceiling", {})
        checks["progress_none"] = all(ceiling.get(key) == "NONE" for key in ("PNT", "PNT_AP", "Goldbach", "RH", "GRH"))

    if case.get("expected_behavior") == "unclassified_or_out_of_scope":
        checks["unclassified"] = not selected or "unclassified" in output.get("detected_intents", [])

    passed = all(checks.values())
    return {
        "case_id": case["case_id"],
        "class": case["class"],
        "passed": passed,
        "checks": checks,
        "selected_units": sorted(selected),
        "blocked_edges_triggered": output.get("blocked_edges_triggered", []),
        "claim_ceiling": output.get("claim_ceiling", {}),
    }


def run(path: Path) -> dict[str, Any]:
    results = [evaluate_case(case) for case in load_cases(path)]
    by_class: dict[str, dict[str, int]] = {}
    for result in results:
        bucket = by_class.setdefault(result["class"], {"passed": 0, "total": 0})
        bucket["total"] += 1
        bucket["passed"] += int(result["passed"])
    return {
        "benchmark_id": "BENCHMARK-TKG-001",
        "execution_scope": "structural routing and governance only",
        "passed": all(item["passed"] for item in results),
        "passed_cases": sum(int(item["passed"]) for item in results),
        "total_cases": len(results),
        "by_class": by_class,
        "results": results,
        "scientific_claims_certified": False,
        "math_status": "MATH-M0",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    parser.add_argument("--case-id")
    args = parser.parse_args()
    report = run(args.registry)
    if args.case_id:
        matches = [r for r in report["results"] if r["case_id"] == args.case_id]
        if not matches:
            raise SystemExit(f"unknown case id: {args.case_id}")
        report = matches[0]
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
