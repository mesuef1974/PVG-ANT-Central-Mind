#!/usr/bin/env python3
"""Governed multi-hop router over TKG-001..TKG-015.

This is a structural reasoning harness. It does not prove analytic theorems and
never promotes MATH automatically.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from typing import Iterable

INTENT_RULES = {
    "arithmetic_identity": (r"mobius|möbius|convolution|التفاف|موبيوس|lambda|فون مانغولد|مانغولد|tau|تاو|sigma|divisor|قواسم|سيغما", ["TKG-001", "TKG-002"]),
    "multiplicative_structure": (r"multiplicative|completely multiplicative|tau|تاو|sigma|divisor function|مضاعف|دالة القواسم", ["TKG-002", "TKG-003"]),
    "euler_product": (r"euler product|dirichlet series|جداء أويلر|متسلسلة ديريشليه|logarithmic[- ]derivative|prime-power coefficient|قوة أولية|معامل فون مانغولد|معامل مانغولد", ["TKG-003", "TKG-004"]),
    "summatory_observable": (r"psi|theta|pi\(|تشيبيشيف|دالة عد|summatory|partial summation", ["TKG-005"]),
    "residue_class": (r"character|dirichlet l|residue class|شخصية|فئة باقية|متتالية حسابية|conductor|موصل", ["TKG-006", "TKG-007", "TKG-008"]),
    "functional_equation": (r"gauss sum|functional[- ]equation|completed l|root number|مجموع غاوس|معادلة وظيفية|عدد الجذر", ["TKG-009", "TKG-010"]),
    "explicit_formula": (r"perron|mellin|contour|residue|explicit formula|بيرون|ميلين|مسار|باقي|صيغة صريحة", ["TKG-011", "TKG-012", "TKG-013", "TKG-014"]),
    "asymptotic_transfer": (r"tauberian|ikehara|asymptotic|تاوبري|أسيمبتوطي|حد رئيسي|main term", ["TKG-015"]),
    "pnt_claim": (r"prime number theorem|pnt|مبرهنة الأعداد الأولية", ["TKG-001", "TKG-003", "TKG-004", "TKG-005", "TKG-011", "TKG-013", "TKG-014", "TKG-015"]),
    "goldbach_claim": (r"goldbach|غولدباخ", ["REASONING-ORCHESTRATOR-001"]),
    "rh_claim": (r"riemann hypothesis|rh\b|grh\b|فرضية ريمان", ["TKG-009", "TKG-010", "TKG-014"]),
    "governance_claim": (r"promote|promotion|math-m[1-9]|verifier files exist|all verifier files|ترقية|رقّ|ملفات التحقق|جميع ملفات التحقق", ["REASONING-ORCHESTRATOR-001"]),
    "discovery_claim": (r"pvg reinterpretation|pvg.*new theorem|هندسة التقييمات.*مبرهنة جديدة|إعادة تفسير.*مبرهنة", ["REASONING-ORCHESTRATOR-001"]),
}

BLOCKED_EDGES = [
    ("Euler product", "PNT", r"euler product.*(pnt|prime number theorem)|جداء أويلر.*مبرهنة الأعداد الأولية"),
    ("finite computation", "universal or asymptotic theorem", r"(?:finite|computed|checked|million|مليون|فحصنا|فحص).*?(?:prove|proof|يثبت|برهان).*?(?:asymptotic|universal|all|every|pnt|goldbach|أسيمبتوطي|جميع|كل|غولدباخ)"),
    ("functional-equation symmetry", "RH", r"functional[- ]equation.*(?:rh|riemann hypothesis)|المعادلة الوظيفية.*فرضية ريمان"),
    ("character orthogonality", "PNT-AP", r"orthogonality.*arithmetic progression|تعامد الشخصيات.*المتتاليات الحسابية"),
    ("formal contour shift", "explicit formula", r"contour shift.*explicit formula|تحريك المسار.*الصيغة الصريحة"),
    ("simple pole", "Tauberian conclusion", r"simple pole.*asymptotic|قطب بسيط.*أسيمبتوطي"),
    ("PVG reinterpretation", "new theorem", r"pvg.*new theorem|ترجمة.*هندسة التقييمات.*مبرهنة جديدة|pvg reinterpretation.*new theorem"),
    ("syntactic completeness", "MATH promotion", r"(?:verifier files exist|all verifier files|syntactically complete|وجود ملفات التحقق|جميع ملفات التحقق).*?(?:promote|promotion|math-m[1-9]|ترقية|رقّ)"),
]

HYPOTHESES = {
    "arithmetic_identity": ["object definitions fixed", "finite-domain conventions fixed"],
    "multiplicative_structure": ["coprimality conditions checked", "complete multiplicativity not assumed"],
    "euler_product": ["multiplicativity where required", "absolute-convergence region fixed"],
    "summatory_observable": ["endpoint convention fixed", "coefficient definition verified"],
    "residue_class": ["modulus fixed", "reduced-residue conditions checked", "character convention fixed"],
    "functional_equation": ["primitive source fixed", "parity and conductor fixed", "analytic continuation theorem supplied"],
    "explicit_formula": ["kernel fixed", "continuation region certified", "pole/zero ledger complete", "all contour bounds certified", "limit order fixed"],
    "asymptotic_transfer": ["exact Tauberian theorem fixed", "positivity/monotonicity checked", "boundary regularity certified", "normalization fixed"],
    "pnt_claim": ["zeta nonvanishing on Re(s)=1 certified", "valid transfer theorem supplied"],
    "goldbach_claim": ["finite verification is not a universal proof", "additive theorem certificate required"],
    "rh_claim": ["no finite or symmetry-only argument accepted"],
    "governance_claim": ["executed verifier evidence required", "independent MATH promotion review required"],
    "discovery_claim": ["novel mathematical content must be separated from reinterpretation", "independent theorem certificate required"],
}

@dataclass(frozen=True)
class Route:
    intents: list[str]
    units: list[str]

def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())

def detect_intents(question: str) -> Route:
    text = normalize(question)
    intents: list[str] = []
    units: list[str] = []
    for name, (pattern, linked_units) in INTENT_RULES.items():
        if re.search(pattern, text, flags=re.IGNORECASE):
            intents.append(name)
            for unit in linked_units:
                if unit not in units:
                    units.append(unit)
    if not intents:
        intents = ["unclassified"]
    return Route(intents, units)

def blocked_edges(question: str) -> list[dict]:
    text = normalize(question)
    hits = []
    for source, target, pattern in BLOCKED_EDGES:
        if re.search(pattern, text, flags=re.IGNORECASE):
            hits.append({"source": source, "target": target, "status": "BLOCKED"})
    return hits

def reason(question: str, supplied: Iterable[str] = ()) -> dict:
    route = detect_intents(question)
    required: list[str] = []
    for intent in route.intents:
        for item in HYPOTHESES.get(intent, []):
            if item not in required:
                required.append(item)
    supplied_set = set(supplied)
    missing = [item for item in required if item not in supplied_set]
    blocked = blocked_edges(question)
    analytic_intents = {"explicit_formula", "asymptotic_transfer", "pnt_claim", "rh_claim", "goldbach_claim"}
    ceiling = "ASSIM-L2" if analytic_intents.intersection(route.intents) else "ASSIM-L3"
    return {
        "normalized_question": normalize(question),
        "detected_intents": route.intents,
        "selected_units": route.units,
        "reasoning_path": [f"route:{intent}" for intent in route.intents],
        "required_hypotheses": required,
        "missing_certificates": missing,
        "blocked_edges_triggered": blocked,
        "pvg_translation": "Use labelled valuation geometry where available; preserve a hybrid/nonlocal label for analytic steps.",
        "preserved_information": ["selected TKG provenance", "hypothesis ledger", "claim ceiling"],
        "lost_information": ["no theorem proof is reconstructed from routing alone"],
        "claim_ceiling": {"ASSIM": ceiling, "MATH": "MATH-M0", "PNT": "NONE", "PNT_AP": "NONE", "GOLDBACH": "NONE", "RH": "NONE", "GRH": "NONE"},
        "authorization": False,
        "automatic_math_promotion": False,
        "next_valid_action": "Supply and independently verify missing certificates; then run the relevant unit verifiers and benchmark cases.",
    }

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    parser.add_argument("--supplied", nargs="*", default=[])
    args = parser.parse_args()
    print(json.dumps(reason(args.question, args.supplied), ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
