#!/usr/bin/env python3
"""Exact arithmetic-function changes under one horizontal PVG transfer.

For N=prod p^a and a move p->q, replace a_p by a_p-1 and a_q by a_q+1.
The move preserves Omega.  The tool reports exact values and ratios for tau,
sigma, phi, mu, Liouville lambda, omega, radical, and n.
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import prod
from typing import Mapping

try:
    from .pvg_inverse_geometry import GeometryInputError, parse_factorization, validate_complete_factorization
except ImportError:
    from pvg_inverse_geometry import GeometryInputError, parse_factorization, validate_complete_factorization  # type: ignore


def normalize(f: Mapping[int, int]) -> dict[int, int]:
    return dict(sorted((int(p), int(a)) for p, a in f.items() if int(a) > 0))


def value(f: Mapping[int, int]) -> int:
    return prod(p**a for p, a in f.items())


def tau(f: Mapping[int, int]) -> int:
    return prod(a + 1 for a in f.values())


def sigma(f: Mapping[int, int]) -> int:
    return prod((p ** (a + 1) - 1) // (p - 1) for p, a in f.items())


def phi(f: Mapping[int, int]) -> int:
    return prod((p - 1) * p ** (a - 1) for p, a in f.items())


def mobius(f: Mapping[int, int]) -> int:
    if any(a > 1 for a in f.values()):
        return 0
    return -1 if len(f) % 2 else 1


def liouville(f: Mapping[int, int]) -> int:
    return -1 if sum(f.values()) % 2 else 1


def radical(f: Mapping[int, int]) -> int:
    return prod(f.keys()) if f else 1


def arithmetic_values(f: Mapping[int, int]) -> dict[str, int]:
    f = normalize(f)
    return {
        "n": value(f),
        "omega": len(f),
        "Omega": sum(f.values()),
        "tau": tau(f),
        "sigma": sigma(f),
        "phi": phi(f),
        "mu": mobius(f),
        "lambda": liouville(f),
        "radical": radical(f),
    }


def ratio_payload(after: int, before: int) -> dict:
    if before == 0:
        return {"defined": False, "reason": "before value is zero"}
    r = Fraction(after, before)
    return {"defined": True, "numerator": r.numerator, "denominator": r.denominator, "text": f"{r.numerator}/{r.denominator}"}


def transfer(factors: Mapping[int, int], donor: int, recipient: int) -> dict[int, int]:
    f = normalize(factors)
    if donor == recipient:
        raise GeometryInputError("donor and recipient axes must be distinct")
    if f.get(donor, 0) <= 0:
        raise GeometryInputError("donor axis must have positive valuation")
    f[donor] -= 1
    if f[donor] == 0:
        del f[donor]
    f[recipient] = f.get(recipient, 0) + 1
    return normalize(f)


def classify_move(before_f: Mapping[int, int], after_f: Mapping[int, int], donor: int, recipient: int) -> dict:
    a = before_f.get(donor, 0)
    b = before_f.get(recipient, 0)
    return {
        "donor_exponent_before": a,
        "recipient_exponent_before": b,
        "donor_disappears": a == 1,
        "recipient_is_new_axis": b == 0,
        "support_change": len(after_f) - len(before_f),
        "position_class": (
            "support_swap" if a == 1 and b == 0 else
            "boundary_contraction" if a == 1 and b > 0 else
            "boundary_expansion" if a > 1 and b == 0 else
            "interior_transfer"
        ),
    }


def analyze_transfer(factors: Mapping[int, int], donor: int, recipient: int) -> dict:
    before_f = normalize(factors)
    after_f = transfer(before_f, donor, recipient)
    before = arithmetic_values(before_f)
    after = arithmetic_values(after_f)
    delta = {k: after[k] - before[k] for k in before}
    ratios = {k: ratio_payload(after[k], before[k]) for k in ("n", "tau", "sigma", "phi", "radical")}
    a, b = before_f[donor], before_f.get(recipient, 0)
    expected_tau = Fraction(a, a + 1) * Fraction(b + 2, b + 1)
    exact_laws = {
        "Omega": "invariant",
        "lambda": "invariant because lambda(n)=(-1)^Omega",
        "n_ratio": f"{recipient}/{donor}",
        "tau_ratio": f"({a}/{a+1})*({b+2}/{b+1})",
        "sigma_ratio": f"((donor^{a}-1)/(donor^{a+1}-1))*((recipient^{b+2}-1)/(recipient^{b+1}-1))",
        "phi_ratio": (
            f"{recipient}/{donor}" if a > 1 and b > 0 else
            f"{recipient}/({donor}-1)" if a == 1 and b > 0 else
            f"({recipient}-1)/{donor}" if a > 1 and b == 0 else
            f"({recipient}-1)/({donor}-1)"
        ),
    }
    return {
        "schema": "PVG-ARITHMETIC-TERRAIN-001",
        "before_factorization": [{"prime": p, "valuation": e} for p, e in before_f.items()],
        "after_factorization": [{"prime": p, "valuation": e} for p, e in after_f.items()],
        "move": {"donor": donor, "recipient": recipient, **classify_move(before_f, after_f, donor, recipient)},
        "before": before,
        "after": after,
        "delta": delta,
        "ratios": ratios,
        "exact_laws": exact_laws,
        "verification": {
            "Omega_preserved": before["Omega"] == after["Omega"],
            "lambda_preserved": before["lambda"] == after["lambda"],
            "integer_move": after["n"] * donor == before["n"] * recipient,
            "tau_formula": (
                ratios["tau"]["numerator"] == expected_tau.numerator
                and ratios["tau"]["denominator"] == expected_tau.denominator
            ),
        },
        "classification": "exact arithmetic identities on one PVG horizontal edge; no novelty or asymptotic claim",
    }


def parse_axis(text: str) -> int:
    x = int(text)
    if x < 2:
        raise GeometryInputError("axis must be an integer >=2")
    return x


def main() -> int:
    ap = argparse.ArgumentParser(description="Analyze arithmetic-function terrain under a PVG transfer.")
    ap.add_argument("n", type=int)
    ap.add_argument("donor")
    ap.add_argument("recipient")
    ap.add_argument("--factors", required=True, help="complete factorization, e.g. 2^2,3,5")
    ap.add_argument("--compact", action="store_true")
    args = ap.parse_args()
    try:
        factors = parse_factorization(args.factors)
        validate_complete_factorization(args.n, factors)
        report = analyze_transfer(factors, parse_axis(args.donor), parse_axis(args.recipient))
    except (GeometryInputError, ValueError) as exc:
        print(json.dumps({"status": "invalid_arithmetic_terrain_input", "reason": str(exc)}, indent=2))
        return 2
    print(json.dumps(report, sort_keys=True, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
