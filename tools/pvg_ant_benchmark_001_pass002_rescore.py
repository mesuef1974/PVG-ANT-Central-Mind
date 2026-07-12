from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "benchmarks" / "pvg-ant-001"
CASES_DIR = BASE / "cases"
EXPECTED = BASE / "post-pass002-expected.json"
GENERATED = BASE / "post-pass002-results.json"
REPORT = BASE / "post-pass002-report.md"
PASS2 = ROOT / "registries" / "pvg-ant-translation-kernel-v2-pass-002"

DIMS = [
    "forward_translation",
    "reverse_control",
    "information_loss",
    "tool_routing",
    "wall_certificate",
    "honest_classification",
]

UPGRADES: dict[str, dict[str, object]] = {
    "B001-GA-07": {"card": "TR-V2-PVG-MATERIALITY-GATE-001", "deltas": {"tool_routing": 1}},
    "B001-LA-06": {"card": "TR-V2-PRIMITIVE-IMPRIMITIVE-CONDUCTOR-001", "deltas": {"reverse_control": 1, "wall_certificate": 1}},
    "B001-LA-07": {"card": "TR-V2-GENERAL-THEOREM-SUBSUMPTION-001", "deltas": {"forward_translation": 1, "reverse_control": 1}},
    "B001-LA-09": {"card": "TR-V2-UNIFORMITY-PARAMETER-TRACKING-001", "deltas": {"reverse_control": 1, "tool_routing": 1, "wall_certificate": 1}},
    "B001-TR-03": {"card": "TR-V2-SMOOTH-TO-SHARP-DESMOOTHING-001", "deltas": {"reverse_control": 1, "tool_routing": 1, "wall_certificate": 1}},
    "B001-TR-04": {"card": "TR-V2-VERTICAL-STRIP-CERTIFICATE-001", "deltas": {"reverse_control": 1}},
    "B001-TR-05": {"card": "TR-V2-TAUBERIAN-BOUNDARY-001", "deltas": {"reverse_control": 1, "wall_certificate": 1}},
    "B001-TR-06": {"card": "TR-V2-UNIFORMITY-PARAMETER-TRACKING-001", "deltas": {"reverse_control": 1, "tool_routing": 1, "wall_certificate": 1}},
    "B001-TR-07": {"card": "TR-V2-TAUBERIAN-BOUNDARY-001", "deltas": {"reverse_control": 1}},
    "B001-RE-06": {"card": "TR-V2-PRIMITIVE-IMPRIMITIVE-CONDUCTOR-001", "deltas": {"forward_translation": 1, "reverse_control": 1, "tool_routing": 1}},
    "B001-RE-07": {"card": "TR-V2-MOMENT-TO-TAIL-MAX-001", "deltas": {"reverse_control": 1, "tool_routing": 1}},
    "B001-SI-06": {"card": "TR-V2-SIEVE-DISPERSION-001", "deltas": {"forward_translation": 1, "reverse_control": 1, "tool_routing": 1, "wall_certificate": 1}},
    "B001-PR-04": {"card": "TR-V2-LOCAL-GLOBAL-PROBABILISTIC-TRANSFER-001", "deltas": {"forward_translation": 1, "reverse_control": 1, "tool_routing": 1, "wall_certificate": 1}},
    "B001-PR-07": {"card": "TR-V2-SHORT-INTERVAL-ADDITIVE-ORDER-001", "deltas": {"reverse_control": 1, "tool_routing": 1, "wall_certificate": 1}},
    "B001-PR-08": {"card": "TR-V2-HALASZ-PRETENTIOUS-001", "deltas": {"forward_translation": 2, "reverse_control": 2, "tool_routing": 2}},
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def read_jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise RuntimeError(f"Invalid JSONL at {path}:{line_no}: {error}") from error
        require(isinstance(value, dict), f"Expected object at {path}:{line_no}")
        rows.append(value)
    return rows


def pass2_ids() -> set[str]:
    ids: set[str] = set()
    for path in sorted(PASS2.glob("*.jsonl")):
        ids.update(str(row["id"]) for row in read_jsonl(path))
    return ids


def main() -> None:
    cases: list[dict[str, object]] = []
    for path in sorted(CASES_DIR.glob("*.jsonl")):
        cases.extend(read_jsonl(path))
    require(len(cases) == 60, f"Expected 60 benchmark cases, found {len(cases)}")

    card_ids = pass2_ids()
    for case_id, upgrade in UPGRADES.items():
        require(str(upgrade["card"]) in card_ids, f"Upgrade card missing for {case_id}")
        deltas = upgrade["deltas"]
        require(isinstance(deltas, dict) and deltas, f"Invalid score deltas for {case_id}")
        require(all(dim in DIMS for dim in deltas), f"Invalid upgraded dimension for {case_id}")
        require(all(isinstance(delta, int) and delta > 0 for delta in deltas.values()), f"Invalid score delta for {case_id}")

    by_domain: dict[str, Counter[str]] = {}
    dimension_points = Counter()
    total = 0
    improvement = 0
    remaining_imperfect_cases = 0
    applied: list[dict[str, object]] = []

    for case in cases:
        case_id = str(case["id"])
        domain = str(case["domain"])
        baseline_scores = case["baseline_dimension_scores"]
        require(isinstance(baseline_scores, dict), f"Invalid baseline scores for {case_id}")
        scores = {dim: int(baseline_scores[dim]) for dim in DIMS}
        before = sum(scores.values())

        if case_id in UPGRADES:
            upgrade = UPGRADES[case_id]
            deltas = upgrade["deltas"]
            require(isinstance(deltas, dict), f"Invalid deltas for {case_id}")
            for dim, delta in deltas.items():
                require(dim in DIMS, f"Invalid upgraded dimension {dim} for {case_id}")
                require(isinstance(delta, int) and delta > 0, f"Invalid delta for {case_id}:{dim}")
                require(scores[dim] + delta <= 2, f"Upgrade would exceed the ceiling for {case_id}:{dim}")
                scores[dim] += delta
            after = sum(scores.values())
            applied.append({
                "case_id": case_id,
                "card": upgrade["card"],
                "points_added": after - before,
                "post_total": after,
            })
        else:
            after = before
            if before < 12:
                remaining_imperfect_cases += 1

        improvement += after - before
        total += after
        domain_counter = by_domain.setdefault(domain, Counter())
        domain_counter["points"] += after
        domain_counter["cases"] += 1
        for dim in DIMS:
            dimension_points[dim] += scores[dim]

    domain_scores = {
        domain: {
            "cases": counter["cases"],
            "points": counter["points"],
            "max": counter["cases"] * 12,
            "percent": round(100 * counter["points"] / (counter["cases"] * 12), 1),
        }
        for domain, counter in sorted(by_domain.items())
    }
    dimension_scores = {
        dim: {
            "points": dimension_points[dim],
            "max": 120,
            "percent": round(100 * dimension_points[dim] / 120, 1),
        }
        for dim in DIMS
    }

    result = {
        "benchmark_id": "PVG-ANT-BENCHMARK-001",
        "rescore_id": "TRANSLATION-KERNEL-V2-PASS-002-RESCORE",
        "rescore_type": "registry_coverage_improvement_not_model_performance",
        "case_count": 60,
        "baseline_points": 662,
        "post_pass002_points": total,
        "max_points": 720,
        "points_added": improvement,
        "post_pass002_percent": round(100 * total / 720, 1),
        "domain_scores": domain_scores,
        "dimension_scores": dimension_scores,
        "applied_upgrades": sorted(applied, key=lambda row: str(row["case_id"])),
        "remaining_imperfect_cases": remaining_imperfect_cases,
        "l3_promotion": False,
        "model_performance_claim": False,
    }
    GENERATED.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    require(result == expected, "Post-Pass-002 rescore differs from expected certificate")
    require(total == 702, f"Expected 702 points, found {total}")
    require(improvement == 40, f"Expected +40 points, found {improvement}")
    require(result["post_pass002_percent"] == 97.5, "Expected 97.5 percent coverage")
    require(dimension_scores["reverse_control"]["percent"] == 93.3, "Reverse-control rescore drift")
    require(dimension_scores["tool_routing"]["percent"] == 96.7, "Tool-routing rescore drift")
    require(result["model_performance_claim"] is False, "Rescore cannot be a model-performance claim")
    require(result["l3_promotion"] is False, "Rescore cannot promote L3")

    report = REPORT.read_text(encoding="utf-8")
    for token in [
        "702/720 = 97.5%",
        "coverage rescore, not a hidden-set model evaluation",
        "remaining gaps",
        "No RH/GRH progress",
    ]:
        require(token in report, f"Post-Pass-002 report token missing: {token}")

    print(
        "pvg_ant_benchmark_001_pass002_rescore: PASS — 702/720 coverage, +40 points, "
        "reverse/tool gaps reduced without model-performance or L3 claims"
    )


if __name__ == "__main__":
    main()
