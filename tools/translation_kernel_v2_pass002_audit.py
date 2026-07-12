from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V1 = ROOT / "registries" / "pvg-ant-bridges.jsonl"
PASS1 = ROOT / "registries" / "pvg-ant-translation-kernel-v2"
PASS2 = ROOT / "registries" / "pvg-ant-translation-kernel-v2-pass-002"
EXPECTED = ROOT / "maps" / "translation-v2-pass002-example-expected.json"
GENERATED = ROOT / "maps" / "translation-v2-pass002-example-results.json"
MISSING = ROOT / "benchmarks" / "pvg-ant-001" / "missing-cards-ranked.md"
CATALOG = ROOT / "maps" / "pvg-ant-translation-kernel-v2-pass002-catalog.md"
CHECKPOINT = ROOT / "governance" / "checkpoints" / "TRANSLATION-KERNEL-V2-PASS-002.md"
NEXT_ACTION = ROOT / "transition-memory" / "next-action.md"

REQUIRED_FIELDS = {
    "id", "title", "domain", "direction", "status", "maturity",
    "pvg_object", "ant_object", "forward_translation", "reverse_translation",
    "preserved_information", "lost_information", "trigger", "compatible_tools",
    "typical_output", "error_or_wall", "required_certificate", "positive_example",
    "counterexample", "anti_overclaim", "classification", "source_basis", "test_id",
}
EXPECTED_COUNTS = {
    "geometry_arithmetic": 1,
    "local_analytic": 2,
    "transforms": 3,
    "residues": 2,
    "sieve": 1,
    "probabilistic": 3,
}
FORBIDDEN_POSITIVE_PROMOTIONS = {
    "classification: original theorem",
    "classification: certified theorem",
    "publication-ready: yes",
    "certified-originality: yes",
    "rh-progress: positive",
    "grh-progress: positive",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def read_jsonl(path: Path) -> list[dict[str, object]]:
    require(path.exists(), f"Missing JSONL: {path}")
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


def read_directory(path: Path) -> list[dict[str, object]]:
    files = sorted(path.glob("*.jsonl"))
    require(len(files) == 6, f"Expected six registry files in {path}, found {len(files)}")
    rows: list[dict[str, object]] = []
    for file in files:
        rows.extend(read_jsonl(file))
    return rows


def main() -> None:
    v1 = read_jsonl(V1)
    pass1 = read_directory(PASS1)
    pass2 = read_directory(PASS2)

    require(len(v1) == 8, f"v1 inventory drift: {len(v1)}")
    require(len(pass1) == 24, f"Pass 001 inventory drift: {len(pass1)}")
    require(len(pass2) == 12, f"Pass 002 requires 12 cards, found {len(pass2)}")
    require(len(v1) + len(pass1) + len(pass2) == 44, "Combined inventory must be 44")

    all_prior_ids = {str(row.get("id", "")) for row in v1 + pass1}
    ids = [str(row.get("id", "")) for row in pass2]
    test_ids = [str(row.get("test_id", "")) for row in pass2]
    duplicates = [item for item, count in Counter(ids).items() if count > 1]
    require(not duplicates, f"Duplicate Pass 002 IDs: {duplicates}")
    require(len(test_ids) == len(set(test_ids)), "Duplicate Pass 002 test ID")
    require(set(ids).isdisjoint(all_prior_ids), "Pass 002 ID collides with prior registry")

    counts = Counter(str(row.get("domain", "")) for row in pass2)
    require(dict(counts) == EXPECTED_COUNTS, f"Unexpected Pass 002 domain counts: {dict(counts)}")

    for row in pass2:
        missing = REQUIRED_FIELDS - set(row)
        require(not missing, f"Missing fields for {row.get('id')}: {sorted(missing)}")
        require(row["status"] == "validated_intake", f"Invalid status for {row['id']}")
        require(row["maturity"] == "L2", f"Pass 002 may not promote {row['id']} beyond L2")
        require(row["direction"] in {"bidirectional", "pvg_to_ant", "ant_to_pvg"}, f"Bad direction for {row['id']}")
        tools = row["compatible_tools"]
        require(isinstance(tools, list) and len(tools) >= 3, f"Tool route too weak for {row['id']}")
        require(len(str(row["lost_information"])) >= 25, f"Loss statement too weak for {row['id']}")
        require(len(str(row["required_certificate"])) >= 35, f"Certificate too weak for {row['id']}")
        require(len(str(row["counterexample"])) >= 25, f"Counterexample too weak for {row['id']}")
        combined = "\n".join(f"{key}: {value}" for key, value in row.items()).lower()
        for phrase in FORBIDDEN_POSITIVE_PROMOTIONS:
            require(phrase not in combined, f"Forbidden promotion in {row['id']}: {phrase}")

    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    generated = json.loads(GENERATED.read_text(encoding="utf-8"))
    require(expected == generated, "Pass 002 generated examples differ from expected")
    require(set(test_ids) == set(expected), "Pass 002 registry/example test IDs differ")

    missing_text = MISSING.read_text(encoding="utf-8")
    catalog_text = CATALOG.read_text(encoding="utf-8")
    for card_id in ids:
        require(card_id in missing_text, f"Card was not benchmark-justified: {card_id}")
        require(card_id in catalog_text, f"Card missing from Pass 002 catalog: {card_id}")

    checkpoint = CHECKPOINT.read_text(encoding="utf-8")
    require("CHECKPOINT PASS — TRANSLATION KERNEL v2 PASS 002" in checkpoint, "Pass 002 checkpoint missing")
    require("Combined inventory = 44" in checkpoint, "Combined inventory checkpoint missing")
    require("L3 promotions = 0" in checkpoint, "L3 ceiling missing")

    next_action = NEXT_ACTION.read_text(encoding="utf-8")
    require("TRANSLATION-KERNEL-V2-PASS-002 = checkpoint_pass" in next_action, "Pass 002 state missing")
    require("GOAL-OP-ONE-THEOREM-001 = active_external_validation_hold" in next_action, "Theorem hold lost")
    require("Dataset 004 remains unauthorized" in next_action, "Dataset firewall lost")
    require("no RH/GRH progress" in next_action, "Scientific ceiling lost")

    print(
        "translation_kernel_v2_pass002_audit: PASS — 12 benchmark-justified cards, "
        "44 combined translations, 12 deterministic examples, zero L3 promotion"
    )


if __name__ == "__main__":
    main()
