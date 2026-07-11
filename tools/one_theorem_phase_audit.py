from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research" / "one-theorem" / "001"
P0 = BASE / "P0_PRIORITY_AUDIT.md"
P1 = BASE / "P1_SYMBOLIC_AUDIT.md"
EXPECTED = BASE / "P1-symbolic-expected.json"
GENERATED = BASE / "P1-symbolic-results.json"
TARGET = ROOT / "research" / "original-lemma-selection" / "001" / "ONE-LEMMA-TARGET-001.md"
READINESS = ROOT / "governance" / "readiness" / "ONE-LEMMA-TARGET-001.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    for path in [P0, P1, EXPECTED, GENERATED, TARGET, READINESS]:
        require(path.exists(), f"Missing One-Theorem artifact: {path}")

    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    generated = json.loads(GENERATED.read_text(encoding="utf-8"))
    require(expected == generated, "Symbolic result differs from committed expected certificate")
    require(generated["decision"] == "P1_SYMBOLIC_PASS", "P1 symbolic decision changed")

    p0 = P0.read_text(encoding="utf-8")
    p1 = P1.read_text(encoding="utf-8")
    target = TARGET.read_text(encoding="utf-8")
    readiness = READINESS.read_text(encoding="utf-8")
    combined = "\n".join([p0, p1, target, readiness])

    for token in [
        "TARGET SURVIVES P0, WITH NARROWED ORIGINALITY CLAIM",
        "Squarefull numbers in arithmetic progression II",
        "chi^2 = chi_0",
        "chi^3 = chi_0",
        "P1 SYMBOLIC PASS",
        "No coefficient correction is required after P1",
        "No originality certificate",
        "No RH/GRH progress",
    ]:
        require(token in combined, f"Required phase token missing: {token}")

    for formula_token in [
        "I_r(n)",
        "2r+2",
        "rho_q",
        "kappa_q",
        "ONE-LEMMA-TARGET-001",
    ]:
        require(formula_token in combined, f"Target formula token missing: {formula_token}")

    forbidden = [
        "Original theorem: certified",
        "Original lemma: certified",
        "RH progress: positive",
        "GRH progress: positive",
    ]
    lowered = combined.lower()
    for phrase in forbidden:
        require(phrase.lower() not in lowered, f"Forbidden promotion found: {phrase}")

    require("READY" in readiness, "Target readiness is not recorded")
    print("one_theorem_phase_audit: PASS — P0/P1 complete without theorem or originality promotion")


if __name__ == "__main__":
    main()
