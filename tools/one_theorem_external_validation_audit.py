from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research" / "one-theorem" / "001"
DOSSIER_001 = BASE / "P8_EXTERNAL_VALIDATION_001.md"
DOSSIER_002 = BASE / "P8_EXTERNAL_VALIDATION_002.md"
ROUTING = BASE / "P8_REFEREE_CANDIDATES.md"
OUTREACH_PROTOCOL = BASE / "P8_OUTREACH_PROTOCOL.md"
PRIORITY_REQUEST = BASE / "P8_PRIORITY_REVIEW_REQUEST.md"
PROOF_REQUEST = BASE / "P8_PROOF_REFEREE_REQUEST.md"
OUTREACH_TRACKER = BASE / "P8-outreach-tracker.json"
LEDGER = BASE / "P8-external-source-ledger.json"
P8 = BASE / "P8_FINAL_CLASSIFICATION.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def audit_review_record(record: dict, role: str) -> None:
    require(record.get("role") == role, f"Outreach role drift: {role}")
    allowed = record.get("allowed_outcomes")
    require(isinstance(allowed, list) and allowed, f"Allowed outcomes missing: {role}")

    sent = record.get("request_sent")
    received = record.get("response_received")
    verified = record.get("official_contact_verified")
    candidate = record.get("candidate")
    sent_date = record.get("sent_date")
    outcome = record.get("outcome")

    require(isinstance(sent, bool), f"request_sent must be boolean: {role}")
    require(isinstance(received, bool), f"response_received must be boolean: {role}")
    require(isinstance(verified, bool), f"official_contact_verified must be boolean: {role}")

    if sent:
        require(verified is True, f"Official contact must be verified before sending: {role}")
        require(isinstance(candidate, str) and candidate.strip(), f"Candidate missing after send: {role}")
        require(isinstance(sent_date, str) and sent_date.strip(), f"Sent date missing: {role}")
    else:
        require(received is False, f"Response cannot precede request: {role}")
        require(outcome is None, f"Outcome cannot precede request: {role}")

    if received:
        require(sent is True, f"Response cannot precede send: {role}")
        require(outcome in allowed, f"Invalid reviewer outcome: {role}")
    else:
        require(outcome is None, f"Outcome requires a response: {role}")


def main() -> None:
    paths = [
        DOSSIER_001,
        DOSSIER_002,
        ROUTING,
        OUTREACH_PROTOCOL,
        PRIORITY_REQUEST,
        PROOF_REQUEST,
        OUTREACH_TRACKER,
        LEDGER,
        P8,
    ]
    for path in paths:
        require(path.exists(), f"Missing external-validation artifact: {path}")

    dossier_001 = DOSSIER_001.read_text(encoding="utf-8")
    dossier_002 = DOSSIER_002.read_text(encoding="utf-8")
    routing = ROUTING.read_text(encoding="utf-8")
    protocol = OUTREACH_PROTOCOL.read_text(encoding="utf-8")
    priority_request = PRIORITY_REQUEST.read_text(encoding="utf-8")
    proof_request = PROOF_REQUEST.read_text(encoding="utf-8")
    p8 = P8.read_text(encoding="utf-8")
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    tracker = json.loads(OUTREACH_TRACKER.read_text(encoding="utf-8"))

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

    protocol_required = [
        "Separate the two roles",
        "Do not interpret silence as approval",
        "Because the repository is private",
        "Certified originality: absent",
    ]
    lowered_protocol = protocol.lower()
    for token in protocol_required:
        require(token.lower() in lowered_protocol, f"Required outreach protocol token missing: {token}")

    priority_required = [
        "Priority check for a weighted k-full / divisor-box counting result",
        "We are not claiming that the analytic method or the torsion-character mechanism is new",
        "withholding any originality or publication claim",
    ]
    lowered_priority = priority_request.lower()
    for token in priority_required:
        require(token.lower() in lowered_priority, f"Required priority-request token missing: {token}")

    proof_required = [
        "Request for an independent proof check",
        "I am asking only whether the argument is mathematically correct as stated",
        "no claim related to RH or GRH",
    ]
    lowered_proof = proof_request.lower()
    for token in proof_required:
        require(token.lower() in lowered_proof, f"Required proof-request token missing: {token}")

    require(isinstance(tracker, dict), "Outreach tracker must be a JSON object")
    require(tracker.get("stage") == "P8-EXTERNAL-REFEREE-001", "Outreach stage drift")
    require(tracker.get("target_id") == "ONE-LEMMA-TARGET-001", "Outreach target drift")
    # Outreach may be "prepared but unsent" or, once the CEO authorizes and the packets
    # are actually emailed, "sent, awaiting response". The scientific-ceiling locks below
    # (review incomplete, originality not certified, RH/GRH no progress) remain enforced in
    # BOTH states, so relaxing this single status lock records the real send without
    # weakening any overclaim protection. (Line-195 relax authorized by CEO 2026-07-13.)
    require(
        tracker.get("status") in ("PREPARED_NOT_SENT", "SENT_AWAITING_RESPONSE"),
        "Unverified outreach status change",
    )
    audit_review_record(tracker.get("priority_review", {}), "priority_and_significance")
    audit_review_record(tracker.get("proof_review", {}), "independent_proof_referee")

    outreach_ceiling = tracker.get("scientific_ceiling")
    require(isinstance(outreach_ceiling, dict), "Outreach scientific ceiling missing")
    require(outreach_ceiling.get("internal_proof_complete") is True, "Internal proof status lost")
    require(outreach_ceiling.get("online_source_audit_partial_pass") is True, "Online audit status lost")
    for key in [
        "priority_review_complete",
        "external_proof_review_complete",
        "certified_originality",
        "publication_ready",
        "rh_progress",
        "grh_progress",
    ]:
        require(outreach_ceiling.get(key) is False, f"Forbidden outreach promotion: {key}")

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
    combined = "\n".join(
        [dossier_001, dossier_002, routing, protocol, priority_request, proof_request, p8]
    ).lower()
    for phrase in forbidden_positive_promotions:
        require(phrase.lower() not in combined, f"Forbidden external promotion: {phrase}")

    print(
        "one_theorem_external_validation_audit: PASS — outreach status "
        f"'{tracker.get('status')}'; external review incomplete and originality not certified"
    )


if __name__ == "__main__":
    main()
