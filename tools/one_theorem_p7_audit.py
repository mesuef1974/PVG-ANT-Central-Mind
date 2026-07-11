from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research" / "one-theorem" / "001"
SOURCE_AUDIT = BASE / "P7_PRIORITY_SOURCE_AUDIT.md"
PROOF_REVIEW = BASE / "P7_SECOND_PASS_PROOF_REVIEW.md"
SOURCE_LEDGER = BASE / "P7-source-ledger.json"
P2 = BASE / "P2_LOCAL_FACTORIZATION_PROOF.md"
P3P5 = BASE / "P3_P5_SMOOTHED_THEOREM_PROOF.md"
P6 = BASE / "P6_ADVERSARIAL_PROOF_REVIEW.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    for path in [SOURCE_AUDIT, PROOF_REVIEW, SOURCE_LEDGER, P2, P3P5, P6]:
        require(path.exists(), f"Missing P7 artifact: {path}")

    source_text = SOURCE_AUDIT.read_text(encoding="utf-8")
    proof_text = PROOF_REVIEW.read_text(encoding="utf-8")
    proof_base = "\n".join(
        path.read_text(encoding="utf-8") for path in [P2, P3P5, P6]
    )
    ledger = json.loads(SOURCE_LEDGER.read_text(encoding="utf-8"))
    require(isinstance(ledger, dict), "P7 source ledger must be a JSON object")

    require(ledger["target_id"] == "ONE-LEMMA-TARGET-001", "P7 target drift")
    require(ledger["audit_stage"] == "P7", "Wrong audit stage")
    require(
        ledger["decision"]
        == "SURVIVES_AS_MODEST_WEIGHTED_EXTENSION_ORIGINALITY_UNCERTIFIED",
        "P7 decision drift",
    )
    require(len(ledger["primary_sources"]) >= 3, "P7 source ledger is too small")

    required_source_tokens = [
        "Chan and K. M. Tsang",
        "Srichan",
        "arXiv:1407.0054",
        "chi^2=chi_0",
        "chi^3=chi_0",
        "tau\\!\\left(\\frac{n}{\\operatorname{rad}(n)^{2r}}\\right)",
        "PLAUSIBLY NEW MODEST WEIGHTED STATEMENT, NOT A NEW METHOD",
    ]
    for token in required_source_tokens:
        require(token in source_text, f"Missing P7 priority token: {token}")

    required_proof_tokens = [
        "THE MANUAL PROOF IS MATHEMATICALLY COHERENT AT FIXED PARAMETERS",
        "no factor `1/s`",
        "PVG discovery contribution: material",
        "PVG proof necessity: weak",
        "External human referee review: not performed",
    ]
    for token in required_proof_tokens:
        require(token in proof_text, f"Missing P7 proof token: {token}")

    for token in [
        "D_{r,\\chi}(s)",
        "O_{q,r,W,\\varepsilon}",
        "Adversarial logical review: PASS",
    ]:
        require(token in proof_base, f"Missing pre-P7 proof token: {token}")

    ceiling = ledger["scientific_ceiling"]
    require(ceiling["method_novelty"] is False, "Method novelty was promoted")
    require(ceiling["torsion_mechanism_novelty"] is False, "Torsion novelty was promoted")
    require(ceiling["certified_theorem"] is False, "Theorem certified before P8")
    require(ceiling["rh_progress"] is False, "RH progress incorrectly recorded")
    require(ceiling["grh_progress"] is False, "GRH progress incorrectly recorded")

    forbidden = [
        "Original theorem: certified",
        "Original lemma: certified",
        "RH progress: positive",
        "GRH progress: positive",
    ]
    combined = (source_text + "\n" + proof_text).lower()
    for phrase in forbidden:
        require(phrase.lower() not in combined, f"Forbidden promotion found: {phrase}")

    print(
        "one_theorem_p7_audit: PASS — source correction, second-pass proof, and ceilings validated"
    )


if __name__ == "__main__":
    main()
