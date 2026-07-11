from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registries" / "pvg-ant-bridges.jsonl"
RELEASE_INDEX = ROOT / "maps" / "pvg-ant-language-kernel-v1-release-index.md"
EXPECTED = ROOT / "maps" / "bridge-example-expected.json"
GENERATED = ROOT / "maps" / "bridge-example-results.json"

REQUIRED_FIELDS = {
    "id",
    "family",
    "title",
    "status",
    "maturity",
    "classical_object",
    "pvg_object",
    "forward_map",
    "reverse_map_or_loss",
    "preserved_structure",
    "lost_structure",
    "analytic_transform",
    "hypotheses",
    "simplification_gain",
    "finite_example_id",
    "literature_status",
    "classification",
    "card",
    "certificate",
}
ALLOWED_GAINS = {"none", "expository", "structural", "analytic", "proof-producing"}
ALLOWED_MATURITY = {"L1", "L2", "L3"}
FORBIDDEN_PROMOTIONS = {"New Theorem", "Original Theorem", "Candidate Mechanism", "RH progress", "GRH progress"}
CARD_TOKENS = [
    "## Classical object",
    "## PVG object",
    "## Reverse map",
    "## Simplification gain",
    "## Finite certificate",
    "## Research use",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def read_jsonl(path: Path) -> list[dict[str, object]]:
    require(path.exists(), f"Missing registry: {path}")
    rows: list[dict[str, object]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as error:
            raise RuntimeError(f"Invalid JSONL at {path}:{line_number}: {error}") from error
    return rows


def main() -> None:
    rows = read_jsonl(REGISTRY)
    require(len(rows) == 8, f"Kernel v1 requires exactly 8 canonical bridges, found {len(rows)}")

    ids = [str(row.get("id", "")) for row in rows]
    families = [str(row.get("family", "")) for row in rows]
    examples = [str(row.get("finite_example_id", "")) for row in rows]
    require(len(ids) == len(set(ids)), "Duplicate bridge ID")
    require(len(families) == len(set(families)), "Duplicate bridge family")
    require(len(examples) == len(set(examples)), "Duplicate finite example ID")

    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    generated = json.loads(GENERATED.read_text(encoding="utf-8"))
    require(expected == generated, "Generated bridge examples differ from expected certificate")
    require(set(examples) == set(expected), "Registry/example certificate mismatch")

    release_text = RELEASE_INDEX.read_text(encoding="utf-8")
    for row in rows:
        missing = REQUIRED_FIELDS - set(row)
        require(not missing, f"Missing fields for {row.get('id')}: {sorted(missing)}")
        for field in REQUIRED_FIELDS:
            value = row[field]
            require(value not in (None, "", []), f"Empty field {field} for {row['id']}")

        gain = str(row["simplification_gain"])
        maturity = str(row["maturity"])
        require(gain in ALLOWED_GAINS, f"Invalid gain {gain} for {row['id']}")
        require(maturity in ALLOWED_MATURITY, f"Invalid maturity {maturity} for {row['id']}")
        require(not (maturity == "L3" and gain != "proof-producing"), f"L3 bridge lacks proof-producing gain: {row['id']}")
        require(str(row["status"]) == "validated_intake", f"Unexpected bridge status for {row['id']}")

        combined = json.dumps(row, ensure_ascii=False)
        for phrase in FORBIDDEN_PROMOTIONS:
            require(phrase.lower() not in combined.lower(), f"Forbidden promotion in {row['id']}: {phrase}")

        card_path = ROOT / str(row["card"])
        require(card_path.exists(), f"Missing card for {row['id']}: {card_path}")
        card_text = card_path.read_text(encoding="utf-8")
        require(str(row["id"]) in card_text, f"Card ID mismatch for {row['id']}")
        require("## Exact forward map" in card_text or "## Forward map" in card_text, f"Forward map section missing for {row['id']}")
        for token in CARD_TOKENS:
            require(token in card_text, f"Card token {token!r} missing for {row['id']}")
        require(str(row["finite_example_id"]) in card_text, f"Example ID missing from card {row['id']}")
        require(str(row["id"]) in release_text, f"Bridge not indexed in release index: {row['id']}")

    require(sum(row["simplification_gain"] == "expository" for row in rows) >= 1, "Kernel must preserve an expository-only classification")
    require(sum(row["simplification_gain"] == "analytic" for row in rows) >= 3, "Kernel lacks analytic bridge coverage")
    require(all(row["maturity"] != "L3" for row in rows), "Kernel v1 cannot claim L3 without a proved transfer lemma")
    require("No family in v1 is L3" in release_text, "Release ceiling missing")

    print("language_kernel_audit: PASS — 8 canonical bridges, cards, examples, and ceilings validated")


if __name__ == "__main__":
    main()
