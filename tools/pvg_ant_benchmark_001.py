from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "benchmarks" / "pvg-ant-001"
CASES_DIR = BASE / "cases"
EXPECTED = BASE / "baseline-expected.json"
GENERATED = BASE / "baseline-results.json"
RUBRIC = BASE / "rubric.md"
REPORT = BASE / "baseline-report.md"
TAXONOMY = BASE / "error-taxonomy.md"
MISSING = BASE / "missing-cards-ranked.md"
CHECKPOINT = ROOT / "governance" / "checkpoints" / "PVG-ANT-BENCHMARK-001.md"
NEXT_ACTION = ROOT / "transition-memory" / "next-action.md"

DOMAINS = {
    "geometry_arithmetic",
    "local_analytic",
    "transforms",
    "residues",
    "sieve",
    "probabilistic",
}
DIMS = [
    "forward_translation",
    "reverse_control",
    "information_loss",
    "tool_routing",
    "wall_certificate",
    "honest_classification",
]
REQUIRED_CASE_FIELDS = {
    "id", "domain", "case_class", "difficulty", "prompt", "expected_cards",
    "gold", "trap", "baseline_dimension_scores", "baseline_total", "gap_tags",
}
REQUIRED_GOLD_FIELDS = {
    "forward", "reverse", "preserved", "lost", "tool", "wall",
    "certificate", "classification",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def read_jsonl(path: Path) -> list[dict[str, object]]:
    require(path.exists(), f"Missing file: {path}")
    rows: list[dict[str, object]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise RuntimeError(f"Invalid JSONL at {path}:{line_number}: {error}") from error
        require(isinstance(value, dict), f"Expected object at {path}:{line_number}")
        rows.append(value)
    return rows


def compute(cases: list[dict[str, object]]) -> dict[str, object]:
    domain_scores: dict[str, dict[str, object]] = {}
    dimension_points = Counter()
    gap_counts = Counter()

    total_points = 0
    for case in cases:
        scores = case["baseline_dimension_scores"]
        assert isinstance(scores, dict)
        total = sum(int(scores[dim]) for dim in DIMS)
        require(total == case["baseline_total"], f"Total mismatch for {case['id']}")
        total_points += total
        for dim in DIMS:
            dimension_points[dim] += int(scores[dim])
        for gap in case["gap_tags"]:
            gap_counts[str(gap)] += 1

    for domain in sorted(DOMAINS):
        subset = [case for case in cases if case["domain"] == domain]
        points = sum(int(case["baseline_total"]) for case in subset)
        maximum = len(subset) * 12
        domain_scores[domain] = {
            "cases": len(subset),
            "points": points,
            "max": maximum,
            "percent": round(100 * points / maximum, 1),
        }

    dimension_scores = {
        dim: {
            "points": dimension_points[dim],
            "max": len(cases) * 2,
            "percent": round(100 * dimension_points[dim] / (len(cases) * 2), 1),
        }
        for dim in DIMS
    }

    originality_cases = [
        case for case in cases
        if (
            "originality" in str(case["case_class"])
            or "classification" in str(case["case_class"])
            or "decorative" in str(case["case_class"])
        )
    ]
    zero_false_originality = sum(
        1 for case in originality_cases
        if case["baseline_dimension_scores"]["honest_classification"] == 2
    )

    maximum = len(cases) * 12
    return {
        "benchmark_id": "PVG-ANT-BENCHMARK-001",
        "benchmark_type": "kernel_coverage_and_diagnostic_baseline",
        "not_a_model_performance_score": True,
        "case_count": len(cases),
        "max_points": maximum,
        "baseline_points": total_points,
        "baseline_percent": round(100 * total_points / maximum, 1),
        "domain_scores": domain_scores,
        "dimension_scores": dimension_scores,
        "zero_false_originality_cases": zero_false_originality,
        "gap_counts": dict(sorted(gap_counts.items())),
    }


def main() -> None:
    require(CASES_DIR.exists(), f"Missing cases directory: {CASES_DIR}")
    case_files = sorted(CASES_DIR.glob("*.jsonl"))
    require(len(case_files) == 6, f"Expected six domain case files, found {len(case_files)}")
    cases: list[dict[str, object]] = []
    for case_file in case_files:
        cases.extend(read_jsonl(case_file))
    require(len(cases) == 60, f"Benchmark must contain exactly 60 cases, found {len(cases)}")

    ids = [str(case.get("id", "")) for case in cases]
    require(len(ids) == len(set(ids)), "Duplicate benchmark case ID")

    counts = Counter(str(case.get("domain", "")) for case in cases)
    require(set(counts) == DOMAINS, f"Domain set drift: {set(counts)}")
    require(all(counts[domain] == 10 for domain in DOMAINS), f"Expected ten cases per domain: {dict(counts)}")

    classes = Counter(str(case.get("case_class", "")) for case in cases)
    require(len(classes) >= 12, "Benchmark lacks adversarial class diversity")

    for case in cases:
        missing = REQUIRED_CASE_FIELDS - set(case)
        require(not missing, f"Missing fields for {case.get('id')}: {sorted(missing)}")
        require(case["domain"] in DOMAINS, f"Invalid domain for {case['id']}")
        require(case["difficulty"] in {"easy", "medium", "hard"}, f"Invalid difficulty for {case['id']}")
        require(isinstance(case["expected_cards"], list) and case["expected_cards"], f"No card route for {case['id']}")
        require(isinstance(case["gap_tags"], list), f"Invalid gap tags for {case['id']}")

        gold = case["gold"]
        require(isinstance(gold, dict), f"Invalid gold answer for {case['id']}")
        require(REQUIRED_GOLD_FIELDS <= set(gold), f"Incomplete gold answer for {case['id']}")
        require(all(len(str(gold[field])) >= 2 for field in REQUIRED_GOLD_FIELDS), f"Weak gold field for {case['id']}")

        scores = case["baseline_dimension_scores"]
        require(isinstance(scores, dict) and set(scores) == set(DIMS), f"Score dimensions drift for {case['id']}")
        require(all(scores[dim] in {0, 1, 2} for dim in DIMS), f"Invalid score for {case['id']}")
        require(sum(scores.values()) == case["baseline_total"], f"Score sum mismatch for {case['id']}")

    result = compute(cases)
    GENERATED.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    require(EXPECTED.exists(), "Missing expected baseline certificate")
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    require(result == expected, "Generated benchmark baseline differs from committed expected certificate")

    require(result["not_a_model_performance_score"] is True, "Benchmark was misrepresented as model performance")
    require(result["case_count"] == 60, "Case count drift")
    require(result["baseline_points"] == 662, "Baseline points drift")
    require(result["max_points"] == 720, "Maximum points drift")
    require(result["baseline_percent"] == 91.9, "Baseline percentage drift")
    require(result["dimension_scores"]["reverse_control"]["percent"] == 80.8, "Reverse-control signal drift")
    require(result["dimension_scores"]["information_loss"]["percent"] == 100.0, "Loss-discipline signal drift")
    require(result["dimension_scores"]["honest_classification"]["percent"] == 100.0, "Classification ceiling drift")

    for path in [RUBRIC, REPORT, TAXONOMY, MISSING, CHECKPOINT, NEXT_ACTION]:
        require(path.exists(), f"Missing benchmark artifact: {path}")

    rubric = RUBRIC.read_text(encoding="utf-8")
    report = REPORT.read_text(encoding="utf-8")
    taxonomy = TAXONOMY.read_text(encoding="utf-8")
    missing = MISSING.read_text(encoding="utf-8")
    checkpoint = CHECKPOINT.read_text(encoding="utf-8")
    next_action = NEXT_ACTION.read_text(encoding="utf-8")

    for token in [
        "not an empirical score for a language model",
        "Maximum per case: **12**",
        "Pass 002 must be selected from benchmark failures",
    ]:
        require(token in rubric, f"Rubric token missing: {token}")

    for token in [
        "BASELINE TYPE = KERNEL COVERAGE / DIAGNOSTIC",
        "MODEL PERFORMANCE CLAIM = NONE",
        "662/720 = 91.9%",
        "No RH/GRH progress",
    ]:
        require(token in report, f"Report token missing: {token}")

    for token in ["E1 — Reverse-map overreach", "E10 — PVG decorative rather than material"]:
        require(token in taxonomy, f"Taxonomy token missing: {token}")

    for token in [
        "TR-V2-UNIFORMITY-PARAMETER-TRACKING-001",
        "TR-V2-PRIMITIVE-IMPRIMITIVE-CONDUCTOR-001",
        "TR-V2-SMOOTH-TO-SHARP-DESMOOTHING-001",
        "TR-V2-HALASZ-PRETENTIOUS-001",
    ]:
        require(token in missing, f"Missing-card priority absent: {token}")

    require("CHECKPOINT PASS — PVG–ANT BENCHMARK 001" in checkpoint, "Benchmark checkpoint decision missing")
    require("Cases = 60" in checkpoint, "Benchmark case count missing")
    require("Baseline = 662 / 720" in checkpoint, "Benchmark baseline missing")
    require("False originality promotion = 0" in checkpoint, "Originality guard missing")

    require("PVG-ANT-BENCHMARK-001 = checkpoint_pass" in next_action, "Next-action benchmark state missing")
    require("GOAL-OP-ONE-THEOREM-001 = active_external_validation_hold" in next_action, "Theorem hold lost")
    require("Dataset 004 remains unauthorized" in next_action, "Dataset firewall lost")
    require("no RH/GRH progress" in next_action, "Scientific ceiling lost")

    print(
        "pvg_ant_benchmark_001: PASS — 60 cases, 662/720 coverage baseline, "
        "reverse-control and tool-routing gaps identified without model-performance or originality claims"
    )


if __name__ == "__main__":
    main()
