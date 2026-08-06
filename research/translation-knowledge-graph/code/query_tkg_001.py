#!/usr/bin/env python3
"""Minimal executable query harness for TKG-001.

This is a deterministic symbolic router, not a language model.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = ROOT / "translation-knowledge-graph/registry/tkg-001-von-mangoldt-core.jsonl"


def load_records() -> list[dict]:
    return [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]


def factorization(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("n must be positive")
    out: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def von_mangoldt(n: int) -> float:
    fac = factorization(n)
    if len(fac) != 1:
        return 0.0
    p = next(iter(fac))
    return math.log(p)


def explain(n: int) -> dict:
    fac = factorization(n)
    support = len(fac)
    value = von_mangoldt(n)
    return {
        "n": n,
        "factorization": fac,
        "valuation_support_cardinality": support,
        "lambda_value": value,
        "exact_pvg_decision": support == 1,
        "asymptotic_inference_authorized": False,
        "reason": "Pointwise valuation support decides Lambda(n), but asymptotics for psi require independent analytic input.",
    }


def main() -> None:
    records = load_records()
    result = explain(72)
    assert len(records) == 7
    assert result["valuation_support_cardinality"] == 2
    assert result["lambda_value"] == 0.0
    print(json.dumps({"registry_records": len(records), "example": result}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
