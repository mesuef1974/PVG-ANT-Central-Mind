#!/usr/bin/env python3
"""Mechanically extract the TKG human-authorship pilot scaffold.

No canonical type or claim ceiling is inferred. Queue order is reproducible:
sort by (source_path, source_line), then random.Random(SEED).shuffle.
"""
from __future__ import annotations

import csv
import json
import random
from collections import Counter
from pathlib import Path
from typing import Any

SEED = 2026071701
SOURCE_REPOSITORY = "mesuef1974/PVG-ANT-Central-Mind"
SOURCE_BRANCH = "agent/pvg-axis-sum-continuation-002"
REGISTRY_SNAPSHOT_COMMIT = "9c69f1d7672cc378694d2e594b470c9e0583c894"
EXPECTED_RECORDS = 118
EXPECTED_DISTRIBUTION = {
    "TYPE_AND_CEILING": 12,
    "TYPE_ONLY": 15,
    "CEILING_ONLY": 10,
}
JUDGEMENT_COLUMNS = (
    "proposed_canonical_type",
    "proposed_claim_ceiling",
    "decision_evidence",
    "reviewer_id",
    "second_reviewer_id",
    "review_notes",
)


def accepted_governance_signal(record: dict[str, Any]) -> bool:
    # Nested status.MATH and math_status are evidence, not canonical aliases.
    return any(key in record for key in ("claim_ceiling", "math", "math_state"))


def governance_evidence(record: dict[str, Any]) -> dict[str, Any]:
    evidence: dict[str, Any] = {}
    for key in ("claim_ceiling", "math", "math_state", "math_status"):
        if key in record:
            evidence[key] = record[key]
    status = record.get("status")
    if isinstance(status, dict) and "MATH" in status:
        evidence["nested_status_MATH"] = status["MATH"]
    return evidence


def classify_missingness(record: dict[str, Any]) -> str | None:
    has_type = "record_type" in record or "kind" in record
    has_governance = accepted_governance_signal(record)
    if has_type and has_governance:
        return None
    if not has_type and not has_governance:
        return "TYPE_AND_CEILING"
    if not has_type:
        return "TYPE_ONLY"
    return "CEILING_ONLY"


def record_id(record: dict[str, Any]) -> str:
    value = record.get("record_id", record.get("id"))
    if not isinstance(value, str) or not value:
        raise ValueError("missing record_id/id")
    return value


def extract(repo_root: Path) -> list[dict[str, Any]]:
    registry = repo_root / "research" / "translation-knowledge-graph" / "registry"
    files = sorted(registry.glob("tkg-[0-9][0-9][0-9]-*.jsonl"))
    if len(files) != 15:
        raise ValueError(f"expected 15 registry files, found {len(files)}")

    rows: list[dict[str, Any]] = []
    total = 0
    for path in files:
        source_path = path.relative_to(repo_root).as_posix()
        for source_line, text in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not text.strip():
                continue
            source = json.loads(text)
            total += 1
            category = classify_missingness(source)
            if category is None:
                continue
            type_field = (
                "record_type" if "record_type" in source
                else "kind" if "kind" in source else ""
            )
            rows.append({
                "queue_id": "",
                "source_repository": SOURCE_REPOSITORY,
                "source_branch": SOURCE_BRANCH,
                "source_commit": REGISTRY_SNAPSHOT_COMMIT,
                "source_path": source_path,
                "source_line": source_line,
                "source_record_id": record_id(source),
                "source_keys": "|".join(source.keys()),
                "source_type_field": type_field,
                "source_type_value": source.get(type_field, "") if type_field else "",
                "authored_governance_signals": json.dumps(
                    governance_evidence(source), ensure_ascii=False, sort_keys=True
                ),
                "missing_category": category,
                "proposed_canonical_type": "",
                "proposed_claim_ceiling": "",
                "decision_evidence": "",
                "reviewer_id": "",
                "second_reviewer_id": "",
                "review_status": "UNREVIEWED",
                "review_notes": "",
            })

    if total != EXPECTED_RECORDS:
        raise ValueError(f"registry drift: expected {EXPECTED_RECORDS}, found {total}")

    # The pre-shuffle input order is part of the reproducibility contract.
    rows.sort(key=lambda row: (row["source_path"], int(row["source_line"])))
    distribution = dict(Counter(row["missing_category"] for row in rows))
    if distribution != EXPECTED_DISTRIBUTION:
        raise ValueError(
            f"queue drift: expected {EXPECTED_DISTRIBUTION}, found {distribution}"
        )

    random.Random(SEED).shuffle(rows)
    for index, row in enumerate(rows, 1):
        row["queue_id"] = f"TKG-PILOT-{index:03d}"
        if any(row[column] for column in JUDGEMENT_COLUMNS):
            raise AssertionError("extractor populated a human-judgement column")
        if row["review_status"] != "UNREVIEWED":
            raise AssertionError("extractor changed review status")
    return rows


def write_outputs(rows: list[dict[str, Any]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "scaffold.csv").open(
        "w", newline="", encoding="utf-8-sig"
    ) as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    with (output_dir / "scaffold.jsonl").open("w", encoding="utf-8") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def main() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    output_dir = (
        repo_root / "research" / "translation-knowledge-graph" / "pilots"
        / "TKG-HUMAN-AUTHORSHIP-PILOT-SCAFFOLD-001"
    )
    rows = extract(repo_root)
    write_outputs(rows, output_dir)
    print(json.dumps({
        "rows": len(rows),
        "distribution": dict(Counter(row["missing_category"] for row in rows)),
        "canonical_input_order": ["source_path ASC", "source_line ASC"],
        "shuffle_seed": SEED,
        "human_judgement_authored": False,
    }, indent=2))


if __name__ == "__main__":
    main()
