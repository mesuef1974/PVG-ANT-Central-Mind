from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research" / "original-lemma-selection" / "001"
CANDIDATES = BASE / "candidates.jsonl"
LEDGER = BASE / "CANDIDATE_LEDGER.md"
LITERATURE = BASE / "PRELIMINARY_LITERATURE_AUDIT.md"
EXPECTED = BASE / "candidate-check-expected.json"
GENERATED = BASE / "candidate-check-results.json"

REQUIRED_FIELDS = {
    "id",
    "title",
    "bridge_ids",
    "statement",
    "preliminary_status",
    "pvg_necessity",
    "nearest_known",
    "main_risk",
    "claim_ceiling",
}
ALLOWED_STATUSES = {
    "survives_preliminary",
    "merge_corollary",
    "killed_trivial",
    "killed_known",
    "killed_known_pending_exact_citation",
}
EXPECTED_SHORTLIST = ["OLS-CAND-001", "OLS-CAND-002", "OLS-CAND-005"]
FORBIDDEN_POSITIVE_PROMOTIONS = [
    "original theorem: certified",
    "original lemma: certified",
    "candidate mechanism: certified",
    "rh progress: positive",
    "grh progress: positive",
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def read_jsonl(path: Path) -> list[dict[str, object]]:
    require(path.exists(), f"Missing candidate registry: {path}")
    rows: list[dict[str, object]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as error:
            raise RuntimeError(f"Invalid JSONL at {path}:{line_number}: {error}") from error
        require(isinstance(value, dict), f"Expected JSON object at {path}:{line_number}")
        rows.append(value)
    return rows


def main() -> None:
    rows = read_jsonl(CANDIDATES)
    require(len(rows) == 10, f"Expected exactly 10 candidates, found {len(rows)}")

    ids = [str(row.get("id", "")) for row in rows]
    require(ids == [f"OLS-CAND-{index:03d}" for index in range(1, 11)], "Candidate IDs/order changed")
    require(len(ids) == len(set(ids)), "Duplicate candidate IDs")

    for row in rows:
        missing = REQUIRED_FIELDS - set(row)
        require(not missing, f"Missing fields for {row.get('id')}: {sorted(missing)}")
        for field in REQUIRED_FIELDS:
            require(row[field] not in (None, "", []), f"Empty field {field} for {row['id']}")
        require(isinstance(row["bridge_ids"], list), f"bridge_ids must be a list for {row['id']}")
        require(str(row["preliminary_status"]) in ALLOWED_STATUSES, f"Invalid status for {row['id']}")

    counts = Counter(str(row["preliminary_status"]) for row in rows)
    require(counts["survives_preliminary"] == 5, "Expected five preliminary survivors")
    require(counts["merge_corollary"] == 1, "Expected one merged corollary")
    killed = sum(counts[status] for status in ["killed_trivial", "killed_known", "killed_known_pending_exact_citation"])
    require(killed == 4, "Expected four killed candidates")

    for path in [LEDGER, LITERATURE, EXPECTED, GENERATED]:
        require(path.exists(), f"Missing selection artifact: {path}")

    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    generated = json.loads(GENERATED.read_text(encoding="utf-8"))
    require(expected == generated, "Generated candidate checks differ from committed expected result")
    require(generated["preliminary_shortlist"] == EXPECTED_SHORTLIST, "Shortlist drift")

    ledger_text = LEDGER.read_text(encoding="utf-8")
    literature_text = LITERATURE.read_text(encoding="utf-8")
    combined = (ledger_text + "\n" + literature_text).lower()
    for candidate_id in ids:
        require(candidate_id in ledger_text, f"Candidate absent from ledger: {candidate_id}")
    for finalist in EXPECTED_SHORTLIST:
        require(finalist in literature_text, f"Finalist absent from literature audit: {finalist}")
    for phrase in FORBIDDEN_POSITIVE_PROMOTIONS:
        require(phrase not in combined, f"Forbidden positive promotion found: {phrase}")

    require("No candidate is certified original" in literature_text, "Originality ceiling missing")
    require("No proof has begun" in literature_text, "Proof-start ceiling missing")
    require("No RH/GRH progress" in literature_text, "RH/GRH negative ceiling missing")
    require("Phi_z" in ledger_text or "\\Phi_z" in ledger_text, "Face-enumerator family missing")
    require("zeta(2s)" in ledger_text or "\\zeta(2s)" in ledger_text, "Interior factorization missing")
    require("torsion" in literature_text.lower(), "Torsion-character audit missing")

    print("original_lemma_selection_audit: PASS — 10 candidates, 4 kills, 3 preliminary finalists, no originality promotion")


if __name__ == "__main__":
    main()
