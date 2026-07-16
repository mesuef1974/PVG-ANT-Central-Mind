#!/usr/bin/env python3
"""RMG-001-D integration, query API, and public reasoning benchmark verifier."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from rmg_query import RMG, load_jsonl

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "benchmarks" / "rmg_001_d_public_reasoning_cases.jsonl"
LINKS = ROOT / "registry" / "integration-links.jsonl"
RESULT = ROOT / "results" / "rmg_001_d_verification.json"


def run() -> dict:
    graph = RMG.from_repo()
    cases = load_jsonl(CASES)
    links = load_jsonl(LINKS)
    checks: list[dict] = []

    def record(check_id: str, ok: bool, evidence: dict) -> None:
        checks.append({"check_id": check_id, "status": "PASS" if ok else "FAIL", "evidence": evidence})

    record("CHK-RMG-D-LOAD-001", len(graph.nodes) == 16 and len(graph.edges) == 20,
           {"nodes": len(graph.nodes), "edges": len(graph.edges)})
    prime_hits = graph.search("prime number")
    record("CHK-RMG-D-SEARCH-001", any(n["node_id"] == "ANT-PRIME-001" for n in prime_hits),
           {"hit_ids": [n["node_id"] for n in prime_hits]})
    exact_hits = graph.search(translation_type="EXACT_BIJECTION")
    record("CHK-RMG-D-FILTER-001", {n["node_id"] for n in exact_hits} == {
        "ANT-PRIME-001", "ANT-PRIME-POWER-001", "PVG-VALUATION-VECTOR-001"},
        {"hit_ids": [n["node_id"] for n in exact_hits]})
    lambda_neighbors = graph.neighbors("ANT-VON-MANGOLDT-001", "out")
    record("CHK-RMG-D-NEIGHBOR-001", {e["edge_id"] for e in lambda_neighbors} == {"RMG-E-0008", "RMG-E-0009"},
           {"edge_ids": [e["edge_id"] for e in lambda_neighbors]})
    path = graph.shortest_path("ANT-VON-MANGOLDT-001", "ANT-PSI-001")
    record("CHK-RMG-D-PATH-001", path == {"node_path":["ANT-VON-MANGOLDT-001","ANT-PSI-001"],"edge_path":["RMG-E-0009"]},
           {"path": path})
    rh_report = graph.translation_report("ANT-RH-001")
    record("CHK-RMG-D-CEILING-001", rh_report["translation_type"] == "COARSE_DIAGNOSTIC" and
           rh_report["scientific_ceiling"] == "no_claimed_progress" and rh_report["assimilation_level"].startswith("L2_"), rh_report)

    edge_by_id = {e["edge_id"]: e for e in graph.edges}
    for case in cases:
        ok = True
        evidence: dict = {"kind": case["kind"]}
        if case["kind"] == "positive_path":
            found = graph.shortest_path(case["source_id"], case["target_id"])
            ok = found is not None and found["edge_path"] == case["expected_edge_ids"]
            if ok:
                ok = all(edge_by_id[eid]["translation_class"] == case["expected_translation_class"] for eid in found["edge_path"])
            evidence["found"] = found
        else:
            if "node_id" in case:
                node = graph.get(case["node_id"])
                if "required_translation_type" in case:
                    ok = ok and node["translation_type"] == case["required_translation_type"]
                if "required_scientific_ceiling" in case:
                    ok = ok and node["scientific_ceiling"] == case["required_scientific_ceiling"]
                if "required_assimilation_level" in case:
                    ok = ok and node["assimilation_level"] == case["required_assimilation_level"]
                if "required_missing_information" in case:
                    phrase = case["required_missing_information"].casefold()
                    ok = ok and any(phrase in str(x).casefold() for x in node.get("lost_information", []) + node.get("certificate_missing", []))
                evidence["node_id"] = node["node_id"]
            if "expected_edge_ids" in case:
                ok = ok and all(eid in edge_by_id for eid in case["expected_edge_ids"])
                ok = ok and any(edge_by_id[eid]["edge_type"] == "DOES_NOT_IMPLY" for eid in case["expected_edge_ids"])
                evidence["edge_ids"] = case["expected_edge_ids"]
        record(f"CHK-{case['case_id']}", ok, evidence)

    required_link_fields = {"integration_id", "rmg_scope", "target_path", "relation", "status", "rule"}
    record("CHK-RMG-D-INTEGRATION-SCHEMA-001", len(links) == 8 and all(required_link_fields <= set(x) for x in links),
           {"links": len(links)})
    record("CHK-RMG-D-INTEGRATION-UNIQUE-001", len({x["integration_id"] for x in links}) == len(links),
           {"ids": [x["integration_id"] for x in links]})
    record("CHK-RMG-D-BENCHMARK-BALANCE-001",
           sum(c["kind"] == "positive_path" for c in cases) == 6 and sum(c["kind"] == "negative_claim" for c in cases) == 6,
           {"positive": sum(c["kind"] == "positive_path" for c in cases), "negative": sum(c["kind"] == "negative_claim" for c in cases)})

    passed = sum(c["status"] == "PASS" for c in checks)
    return {"unit":"RMG-001-D","status":"PASS" if passed == len(checks) else "FAIL",
            "summary":{"passed":passed,"total":len(checks)},
            "benchmark":{"public_cases":len(cases),"locked_hidden_cases":0,"training_authorized":False},
            "scientific_ceiling":"query and finite reasoning regression only; no new ANT theorem and no RH/GRH progress",
            "checks":checks}


def main() -> int:
    parser = argparse.ArgumentParser(); parser.add_argument("--write-result", action="store_true"); args = parser.parse_args()
    result = run(); text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True); print(text)
    if args.write_result:
        RESULT.parent.mkdir(parents=True, exist_ok=True); RESULT.write_text(text + "\n", encoding="utf-8")
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
