from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research" / "one-theorem" / "001"
DOSSIER_001 = BASE / "P8_EXTERNAL_VALIDATION_001.md"
DOSSIER_002 = BASE / "P8_EXTERNAL_VALIDATION_002.md"
ROUTING = BASE / "P8_REFEREE_CANDIDATES.md"
LEDGER = BASE / "P8-external-source-ledger.json"
P8 = BASE / "P8_FINAL_CLASSIFICATION.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    for path in [DOSSIER_001, DOSSIER_002, ROUTING, LEDGER, P8]:
        require(path.exists(), f"Missing external-validation artifact: {path}")

    dossier_001 = DOSSIER_001.read_text(encoding="utf-8")
    dossier_002 = DOSSIER_002.read_text(encoding="utf-8")
    routing = ROUTING.read_text(encoding="utf-8")
    p8 = P8.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))

    require(isinstance(ledger, dict), "External source ledger must be a JSON object")
    require(ledger.get("target_id") == "ONE-LEMMA-TARGET-001", "Target ID drift")
    require(ledger.get("stage") == "P8-EXTERNAL-VALIDATION-001", "Stage drift")
    require(
        ledger.get("decision") == "ONLINE_PRIMARY_SOURCE_AUDIT_PARTIAL_PASS",
        "External-validation decision drift",
    )

    sources = ledger.get("sources")
    require(isinstance(sources, list) and len(sources) >= 6, "Source ledger is too small")
    source_ids = {str(source.get("id")) for source in sources if isinstance(source, dict)}
    require(len(source_ids) == len(sources), "Duplicate or invalid source IDs")

    required_source_ids = {
        "SRC-CHAN-2014-SQUAREFULL-AP-II",
        "SRC-MEEMARK-WONGCHAROENBHORN-2025",
        "SRC-MUNSCH-SHPARLINSKI-YAU-2018",
        "SRC-CAO-ZHAI-2013",
        "SRC-BALOG-GRANVILLE-SOUND-2007",
        "SRC-BRETECHE-TENENBAUM-2020",
    }
    require(required_source_ids <= source_ids, "Required primary-source coverage missing")

    for source in sources:
        require(isinstance(source, dict), "Invalid source record")
        for field in ["id", "title", "authors", "year", "locator", "role", "finding"]:
            require(bool(source.get(field)), f"Source {source.get('id')} missing {field}")
        require(source.get("direct_match_to_I_r") is False, "Direct match was promoted without review")

    require(ledger.get("exact_match_located") is False, "Exact match flag changed")
    gates = ledger.get("remaining_gates")
    require(isinstance(gates, list) and len(gates) == 2, "Remaining external gates changed")
    require("research-grade bibliographic database search" in gates, "Database gate missing")
    require("external human line-by-line referee review" in gates, "Referee gate missing")

    ceiling = ledger.get("scientific_ceiling")
    require(isinstance(ceiling, dict), "Scientific ceiling missing")
    require(ceiling.get("internally_proved_fixed_parameter_theorem") is True, "Internal proof status lost")
    require(ceiling.get("online_primary_source_audit_partial_pass") is True, "Online audit status lost")
    for key in [
        "certified_originality",
        "publication_ready",
        "new_method",
        "new_torsion_mechanism",
        "rh_progress",
        "grh_progress",
    ]:
        require(ceiling.get(key) is False, f"Forbidden promotion: {key}")

    required_001 = [
        "ONLINE PRIMARY-SOURCE AUDIT: PARTIAL PASS",
        "No primary source located in this audit stated",
        "New analytic method: no",
        "New torsion-character mechanism: no",
        "P8-EXTERNAL-REFEREE-001",
        "originality remains uncertified",
    ]
    lowered_001 = dossier_001.lower()
    for token in required_001:
        require(token.lower() in lowered_001, f"Required dossier-001 token missing: {token}")

    required_002 = [
        "POSSIBLY NEW PVG-DERIVED OBSERVABLE AND MODEST THEOREM",
        "ANALYTIC METHOD CLASSICAL",
        "Originality not certified",
        "Significance gate",
        "P8-EXTERNAL-VALIDATION-002 = COMPLETE AS AN INTERNAL ROUTING PASS",
        "Second theorem target = forbidden",
    ]
    lowered_002 = dossier_002.lower()
    for token in required_002:
        require(token.lower() in lowered_002, f"Required dossier-002 token missing: {token}")

    routing_required = [
        "No person listed below has reviewed or endorsed the result",
        "one priority/terminology review",
        "one independent line-by-line proof review",
        "No reviewer contacted by the project",
        "Originality remains uncertified",
    ]
    lowered_routing = routing.lower()
    for token in routing_required:
        require(token.lower() in lowered_routing, f"Required routing token missing: {token}")

    require("originality not certified" in p8.lower(), "P8 originality ceiling disappeared")

    forbidden_positive_promotions = [
        "Original theorem: certified",
        "Publication ready: yes",
        "External referee: pass",
        "Research database audit: complete",
        "Reviewer contacted: yes",
        "RH progress: positive",
        "GRH progress: positive",
    ]
    combined = "\n".join([dossier_001, dossier_002, routing, p8]).lower()
    for phrase in forbidden_positive_promotions:
        require(phrase.lower() not in combined, f"Forbidden external promotion: {phrase}")

    print(
        "one_theorem_external_validation_audit: PASS — online source and routing audits "
        "retained as partial evidence without originality promotion"
    )


if __name__ == "__main__":
    main()
