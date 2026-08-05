from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V1 = ROOT / "registries" / "pvg-ant-bridges.jsonl"
V2_DIR = ROOT / "registries" / "pvg-ant-translation-kernel-v2"
CATALOG = ROOT / "maps" / "pvg-ant-translation-kernel-v2-seed-catalog.md"
ONTOLOGY = ROOT / "maps" / "pvg-ant-translation-ontology-v2.md"
CHARTER = ROOT / "governance" / "programs" / "PVG-ANT-CENTRAL-MIND-MATURATION-002.md"
CHECKPOINT = ROOT / "governance" / "checkpoints" / "TRANSLATION-KERNEL-V2-PASS-001.md"
EXPECTED = ROOT / "maps" / "translation-v2-example-expected.json"
GENERATED = ROOT / "maps" / "translation-v2-example-results.json"
NEXT_ACTION = ROOT / "transition-memory" / "next-action.md"

REQUIRED_FIELDS = {
    "id", "title", "domain", "direction", "status", "maturity",
    "pvg_object", "ant_object", "forward_translation", "reverse_translation",
    "preserved_information", "lost_information", "trigger", "compatible_tools",
    "typical_output", "error_or_wall", "required_certificate", "positive_example",
    "counterexample", "anti_overclaim", "classification", "source_basis", "test_id",
}
ALLOWED_DOMAINS = {
    "geometry_arithmetic", "local_analytic", "transforms",
    "residues", "sieve", "probabilistic",
}
ALLOWED_DIRECTIONS = {"bidirectional", "pvg_to_ant", "ant_to_pvg"}
ALLOWED_MATURITY = {"L1", "L2"}
EXPECTED_DOMAIN_COUNTS = {
    "geometry_arithmetic": 9,
    "local_analytic": 4,
    "transforms": 2,
    "residues": 3,
    "sieve": 4,
    "probabilistic": 2,
}
FORBIDDEN_POSITIVE_PROMOTIONS = {
    "classification: original theorem",
    "classification: certified theorem",
    "publication-ready: yes",
    "certified-originality: yes",
    "breaks-parity-barrier: yes",
    "rh-progress: positive",
    "grh-progress: positive",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def read_jsonl(path: Path) -> list[dict[str, object]]:
    require(path.exists(), f"Missing JSONL file: {path}")
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


def main() -> None:
    v1 = read_jsonl(V1)
    require(V2_DIR.exists(), f"Missing v2 registry directory: {V2_DIR}")
    registry_files = sorted(V2_DIR.glob("*.jsonl"))
    require(len(registry_files) == 6, f"Expected 6 domain registry files, found {len(registry_files)}")
    v2: list[dict[str, object]] = []
    for registry_file in registry_files:
        v2.extend(read_jsonl(registry_file))

    require(len(v1) == 8, f"Closed v1 inventory drifted: {len(v1)}")
    require(len(v2) == 24, f"Pass 001 requires 24 new cards, found {len(v2)}")
    require(len(v1) + len(v2) == 32, "Combined translation inventory must be 32")

    ids = [str(row.get("id", "")) for row in v2]
    test_ids = [str(row.get("test_id", "")) for row in v2]
    require(len(ids) == len(set(ids)), "Duplicate v2 card ID")
    require(len(test_ids) == len(set(test_ids)), "Duplicate v2 test ID")
    require(set(ids).isdisjoint({str(row.get("id", "")) for row in v1}), "v1/v2 ID collision")

    counts = Counter(str(row.get("domain", "")) for row in v2)
    require(dict(counts) == EXPECTED_DOMAIN_COUNTS, f"Unexpected domain counts: {dict(counts)}")

    for row in v2:
        missing = REQUIRED_FIELDS - set(row)
        require(not missing, f"Missing fields for {row.get('id')}: {sorted(missing)}")
        for field in REQUIRED_FIELDS - {"compatible_tools"}:
            require(row[field] not in (None, "", []), f"Empty field {field} for {row['id']}")
        require(row["domain"] in ALLOWED_DOMAINS, f"Invalid domain for {row['id']}")
        require(row["direction"] in ALLOWED_DIRECTIONS, f"Invalid direction for {row['id']}")
        require(row["maturity"] in ALLOWED_MATURITY, f"Invalid maturity for {row['id']}")
        require(row["status"] == "validated_intake", f"Unexpected status for {row['id']}")

        tools = row["compatible_tools"]
        require(isinstance(tools, list) and len(tools) >= 2, f"Tool routing too weak for {row['id']}")
        require(all(isinstance(tool, str) and tool.strip() for tool in tools), f"Invalid tool in {row['id']}")
        require(len(str(row["lost_information"])) >= 25, f"Loss statement too weak for {row['id']}")
        require(len(str(row["required_certificate"])) >= 30, f"Certificate statement too weak for {row['id']}")
        require(len(str(row["counterexample"])) >= 20, f"Counterexample too weak for {row['id']}")
        require(len(str(row["anti_overclaim"])) >= 20, f"Anti-overclaim statement too weak for {row['id']}")

        combined = "\n".join(f"{key}: {value}" for key, value in row.items()).lower()
        for phrase in FORBIDDEN_POSITIVE_PROMOTIONS:
            require(phrase not in combined, f"Forbidden positive promotion in {row['id']}: {phrase}")

    require(EXPECTED.exists(), f"Expected examples missing: {EXPECTED}")
    require(GENERATED.exists(), f"Generated examples missing: {GENERATED}")
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    generated = json.loads(GENERATED.read_text(encoding="utf-8"))
    require(expected == generated, "Generated v2 examples differ from committed expected certificate")
    require(set(test_ids) == set(expected), "Registry/example test IDs do not match")

    for path in [CATALOG, ONTOLOGY, CHARTER, CHECKPOINT, NEXT_ACTION]:
        require(path.exists(), f"Required artifact missing: {path}")

    catalog = CATALOG.read_text(encoding="utf-8")
    for card_id in ids:
        require(card_id in catalog, f"Card absent from catalog: {card_id}")

    ontology = ONTOLOGY.read_text(encoding="utf-8")
    for token in [
        "LOSS-0 EXACT-LABELED", "LOSS-1 SUMMARY", "LOSS-2 AGGREGATION",
        "LOSS-3 PHASE-SIGN", "LOSS-4 ANALYTIC-CERTIFICATE",
        "Problem-translator procedure", "Research-front firewall",
        "Pass 002 should reach at least 50 cards",
    ]:
        require(token in ontology, f"Ontology token missing: {token}")

    charter = CHARTER.read_text(encoding="utf-8")
    for token in [
        "PVG-ANT-CENTRAL-MIND-MATURATION-002",
        "24 new translation cards",
        "no second theorem target",
        "Dataset 004: unauthorized",
    ]:
        require(token in charter, f"Charter token missing: {token}")

    checkpoint = CHECKPOINT.read_text(encoding="utf-8")
    require("CHECKPOINT PASS — TRANSLATION KERNEL v2 PASS 001" in checkpoint, "Checkpoint decision missing")
    require("Combined inventory = 32" in checkpoint, "Combined inventory checkpoint missing")
    require("L3 promotions = 0" in checkpoint, "L3 ceiling missing")

    next_action = NEXT_ACTION.read_text(encoding="utf-8")
    require("GOAL-OP-INVERSE-PRIME-FIBERS-001 = active_current" in next_action, "Current inverse goal missing")
    require("GOAL-OP-ONE-THEOREM-001 = superseded_with_reason" in next_action, "Archived theorem state missing")
    require("TRANSLATION-KERNEL-V2-PASS-001 = checkpoint_pass" in next_action, "Maturation state missing")
    require("a second theorem target" in next_action.lower(), "Second-theorem firewall missing")
    require("Dataset 004 remains unauthorized" in next_action, "Dataset 004 firewall missing")
    require("no RH/GRH progress" in next_action, "RH/GRH ceiling missing")

    print(
        "translation_kernel_v2_audit: PASS — 24 operational cards, 24 examples, "
        "32 combined translations, zero L3 or research-front promotion; "
        "ENGINE-004 is the current governed front"
    )


if __name__ == "__main__":
    main()
