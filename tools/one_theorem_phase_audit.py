from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research" / "one-theorem" / "001"
P0 = BASE / "P0_PRIORITY_AUDIT.md"
P1 = BASE / "P1_SYMBOLIC_AUDIT.md"
P2 = BASE / "P2_LOCAL_FACTORIZATION_PROOF.md"
P3_P5 = BASE / "P3_P5_SMOOTHED_THEOREM_PROOF.md"
P4_INPUTS = BASE / "P4_ANALYTIC_PREREQUISITES.md"
P6_REVIEW = BASE / "P6_ADVERSARIAL_PROOF_REVIEW.md"
EXPECTED = BASE / "P1-symbolic-expected.json"
GENERATED = BASE / "P1-symbolic-results.json"
TARGET = ROOT / "research" / "original-lemma-selection" / "001" / "ONE-LEMMA-TARGET-001.md"
READINESS = ROOT / "governance" / "readiness" / "ONE-LEMMA-TARGET-001.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    paths = [P0, P1, P2, P3_P5, P4_INPUTS, P6_REVIEW, EXPECTED, GENERATED, TARGET, READINESS]
    for path in paths:
        require(path.exists(), f"Missing One-Theorem artifact: {path}")

    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    generated = json.loads(GENERATED.read_text(encoding="utf-8"))
    require(expected == generated, "Symbolic result differs from committed expected certificate")
    require(generated["decision"] == "P1_SYMBOLIC_PASS", "P1 symbolic decision changed")

    texts = {path.name: path.read_text(encoding="utf-8") for path in paths if path.suffix == ".md"}
    combined = "\n".join(texts.values())

    required_tokens = [
        "TARGET SURVIVES P0, WITH NARROWED ORIGINALITY CLAIM",
        "Squarefull numbers in arithmetic progression II",
        "chi^2 = chi_0",
        "chi^3 = chi_0",
        "P1 SYMBOLIC PASS",
        "No coefficient correction is required after P1",
        "Theorem P2-D — twisted Euler factorization",
        "Smoothed Theorem Proof",
        "This completes the manual proof candidate",
        "rapid Mellin decay",
        "polynomial vertical growth",
        "PASS MANUAL LOGIC / SOURCE AND PRIORITY GATES REMAIN",
        "No originality certificate",
        "No RH/GRH progress",
    ]
    for token in required_tokens:
        require(token in combined, f"Required phase token missing: {token}")

    formula_tokens = [
        "I_r(n)",
        "2r+2",
        "rho_q",
        "kappa_q",
        "ONE-LEMMA-TARGET-001",
        "L(2rs",
        "Q_\\chi'(\\beta_r)",
        "O_{q,r,W,\\varepsilon}",
    ]
    for token in formula_tokens:
        require(token in combined, f"Target formula token missing: {token}")

    p2_text = texts[P2.name]
    proof_text = texts[P3_P5.name]
    review_text = texts[P6_REVIEW.name]
    require("Geometric interpretation: proved" in p2_text, "P2 geometric proof status missing")
    require("Twisted Euler factorization: proved" in p2_text, "P2 factorization status missing")
    require("Full smoothed theorem: manual proof candidate complete" in proof_text, "Full proof status missing")
    require("Originality: plausible but unconfirmed" in review_text, "Review originality ceiling missing")

    forbidden = [
        "Original theorem: certified",
        "Original lemma: certified",
        "RH progress: positive",
        "GRH progress: positive",
    ]
    lowered = combined.lower()
    for phrase in forbidden:
        require(phrase.lower() not in lowered, f"Forbidden promotion found: {phrase}")

    # `"READY" in text` is satisfied by NOT_READY, which contains it. The check confirmed the
    # substring, not the decision -- so a target flipped to NOT_READY would have passed silently.
    readiness = texts[READINESS.name]
    require(
        bool(re.search(r"^\s*(?:Decision:\s*)?READY\b", readiness, re.M)),
        "Target readiness is not recorded as an affirmative READY decision",
    )
    require(
        not re.search(r"\bNOT[_\s]READY\b", readiness, re.I),
        "Target readiness records NOT_READY",
    )
    print(
        "one_theorem_phase_audit: PASS — P0-P6 artifacts include a complete manual proof candidate without originality promotion"
    )


if __name__ == "__main__":
    main()
