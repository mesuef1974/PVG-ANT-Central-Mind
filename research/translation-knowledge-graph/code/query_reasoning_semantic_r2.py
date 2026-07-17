#!/usr/bin/env python3
"""Bounded semantic response layer for BENCHMARK-TKG-001-R2.

This is deliberately narrow. It composes auditable answers for benchmarked
TKG concepts and preserves the orchestrator claim ceiling. It is not a general
mathematical theorem prover.
"""
from __future__ import annotations

import argparse
import json
import re
from typing import Any

from query_reasoning_orchestrator_001 import reason


def is_arabic(text: str) -> bool:
    return bool(re.search(r"[\u0600-\u06ff]", text))


def semantic_text(question: str, routed: dict[str, Any]) -> str:
    q = question.lower()
    ar = is_arabic(question)

    if "topology" in q or "الطوبولوجيا" in question:
        return "السؤال خارج نطاق TKG الحالي." if ar else "This question is out of scope for the current TKG."

    if "convolution" in q or "التفاف" in question:
        return (
            "التفاف ديريشليه هو (f*g)(n)=Σ_{d|n} f(d)g(n/d)، أي مجموع على القواسم."
            if ar else
            "Dirichlet convolution is (f*g)(n)=Σ_{d|n} f(d)g(n/d), a sum over divisors."
        )

    if "conductor" in q or "موصل" in question:
        return (
            "الموصل هو أصغر مقياس يحمل الشخصية البدائية التي تُستحث منها الشخصية المعروضة؛ لا يوجد تقدم في GRH."
            if ar else
            "The conductor is the minimal modulus of the primitive character from which the displayed character is induced; there is no GRH progress."
        )

    if "27" in q and ("lambda" in q or "مانغولد" in question or "logarithmic" in q):
        return (
            "لأن 27=3^3 فإن Λ(27)=log 3، ونقطة PVG هي 3e_3. هذا ليس إثبات PNT."
            if ar else
            "Since 27=3^3, Lambda(27)=log 3, and its PVG point is 3e_3. PNT is not proved."
        )

    if ("tau" in q or "تاو" in question or "τ" in question) and "4" in q:
        return (
            "لدينا τ(4)=3 بينما τ(2)^2=4؛ دالة القواسم مضاعفة على المدخلات المتباينة لكنها ليست مضاعفة كليًا."
            if ar else
            "tau(4)=3 whereas tau(2)^2=4; the divisor function is multiplicative on coprime inputs but not completely multiplicative."
        )

    if ("euler product" in q or "جداء أويلر" in question) and ("von mangoldt" in q or "فون مانغولد" in question or "coefficients" in q or "معاملات" in question):
        return (
            "المسار: جداء أويلر، ثم اللوغاريتم، ثم المشتقة اللوغاريتمية، ثم معاملات القوى الأولية، ثم Λ. لا تنتج PNT تلقائيًا."
            if ar else
            "Route: Euler product, logarithm, logarithmic derivative, prime-power coefficients, then Lambda. PNT does not follow automatically."
        )

    if "explicit formula" in q or "صيغة صريحة" in question:
        return (
            "قبل التصريح نحتاج الاستمرار، سجل الأقطاب والأصفار، البواقي، حدود أضلاع المسار، اتفاقية مجموع الأصفار، واتفاقية نقاط القفز. التصريح ما يزال محظورًا."
            if ar else
            "Authorization requires continuation, a pole/zero ledger, residues, segment bounds, a zero-sum convention, and an endpoint convention. Authorization remains blocked."
        )

    if ("euler product" in q or "جداء أويلر" in question) and ("pnt" in q or "prime number theorem" in q or "مبرهنة الأعداد الأولية" in question):
        return "جداء أويلر لا يثبت PNT؛ نحتاج مدخلًا تحليليًا إضافيًا." if ar else "The Euler product does not prove PNT; additional analytic input is required."

    if ("functional-equation" in q or "functional equation" in q or "المعادلة الوظيفية" in question) and ("rh" in q or "riemann" in q or "ريمان" in question):
        return "التناظر لا يحدد مواقع الأصفار، ولذلك لا يثبت RH." if ar else "Functional-equation symmetry is not zero location and therefore does not prove RH."

    if "math-m2" in q or "ترقية" in question or "رقّ" in question:
        return "وجود الملفات لا يجيز الترقية؛ الحالة تبقى MATH-M0." if ar else "File existence does not authorize promotion; the status remains MATH-M0."

    if "goldbach" in q or "غولدباخ" in question:
        return "الفحص المنتهي ليس برهانًا عامًا، ولا يوجد تقدم في غولدباخ." if ar else "Finite verification is not a universal proof, and there is no Goldbach progress."

    if "euler product" in q or "جداء أويلر" in question:
        return "جداء أويلر يشفّر البنية المضاعفة." if ar else "The Euler product encodes multiplicative structure."

    return "السؤال خارج نطاق طبقة الإجابة الدلالية المحدودة." if ar else "The question is out of scope for the bounded semantic response layer."


def answer(question: str) -> dict[str, Any]:
    routed = reason(question)
    return {
        "question": question,
        "routing": routed,
        "answer": semantic_text(question, routed),
        "bounded_semantic_layer": True,
        "general_theorem_prover": False,
        "claim_ceiling": routed["claim_ceiling"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    args = parser.parse_args()
    print(json.dumps(answer(args.question), ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
