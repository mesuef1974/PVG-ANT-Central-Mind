from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "research" / "one-theorem" / "001"
P7_SOURCE = BASE / "P7_PRIORITY_SOURCE_AUDIT.md"
P7_PROOF = BASE / "P7_SECOND_PASS_PROOF_REVIEW.md"
P8 = BASE / "P8_FINAL_CLASSIFICATION.md"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    for path in [P7_SOURCE, P7_PROOF, P8]:
        require(path.exists(), f"Missing P8 dependency: {path}")

    source = P7_SOURCE.read_text(encoding="utf-8")
    proof = P7_PROOF.read_text(encoding="utf-8")
    p8 = P8.read_text(encoding="utf-8")
    combined = "\n".join([source, proof, p8])

    required = [
        "SURVIVES AS A MODEST WEIGHTED EXTENSION",
        "THE MANUAL PROOF IS MATHEMATICALLY COHERENT AT FIXED PARAMETERS",
        "INTERNALLY PROVED AT FIXED PARAMETERS",
        "PLAUSIBLY NEW MODEST WEIGHTED THEOREM, ORIGINALITY NOT CERTIFIED",
        "PVG role in discovering the observable: material",
        "P8-EXTERNAL-VALIDATION-001",
        "No RH progress",
        "No GRH progress",
    ]
    for token in required:
        require(token.lower() in combined.lower(), f"Missing P8 token: {token}")

    forbidden_positive_promotions = [
        "Original theorem: certified",
        "Original lemma: certified",
        "Publication ready: yes",
        "Torsion mechanism novelty: yes",
        "Contour method novelty: yes",
        "RH progress: positive",
        "GRH progress: positive",
    ]
    lowered = combined.lower()
    for phrase in forbidden_positive_promotions:
        require(phrase.lower() not in lowered, f"Forbidden P8 promotion: {phrase}")

    require("L3 proved transfer principle" in p8, "L3 internal transfer classification missing")
    require("not as an L5 certified original lemma" in p8, "L5 ceiling missing")
    require("not closed as a certified original-theorem success" in p8, "Program hold missing")
    require("originality not certified" in p8.lower(), "Originality ceiling missing")
    require("publication readiness: absent" in p8.lower(), "Publication ceiling missing")

    print("one_theorem_p8_audit: PASS — internally proved result retained without originality promotion")


if __name__ == "__main__":
    main()
