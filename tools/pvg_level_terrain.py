#!/usr/bin/env python3
"""Enumerate exact arithmetic-function terrain on a fixed PVG level."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb, prod
from typing import Iterable

try:
    from .pvg_inverse_geometry import GeometryInputError, is_prime_64
    from .pvg_arithmetic_terrain import arithmetic_values
except ImportError:
    from pvg_inverse_geometry import GeometryInputError, is_prime_64  # type: ignore
    from pvg_arithmetic_terrain import arithmetic_values  # type: ignore


def compositions(total: int, parts: int) -> Iterable[tuple[int, ...]]:
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def fraction_payload(x: Fraction) -> dict:
    return {"numerator": x.numerator, "denominator": x.denominator, "text": f"{x.numerator}/{x.denominator}"}


def parse_primes(text: str) -> list[int]:
    values = [int(x.strip()) for x in text.split(",") if x.strip()]
    if len(values) < 2 or len(set(values)) != len(values):
        raise GeometryInputError("provide at least two distinct prime axes")
    values.sort()
    if any(p < 2 or not is_prime_64(p) for p in values):
        raise GeometryInputError("all axes must be certified primes below 2^64")
    return values


def point_record(primes: list[int], exponents: tuple[int, ...]) -> dict:
    factors = {p: a for p, a in zip(primes, exponents) if a}
    v = arithmetic_values(factors)
    return {
        "exponents": list(exponents),
        **v,
        "sigma_over_n": fraction_payload(Fraction(v["sigma"], v["n"])),
        "phi_over_n": fraction_payload(Fraction(v["phi"], v["n"])),
    }


def extrema(points: list[dict], field: str, *, fraction_field: bool = False) -> dict:
    def key(row: dict):
        if fraction_field:
            x = row[field]
            return Fraction(x["numerator"], x["denominator"])
        return row[field]
    low = min(key(x) for x in points)
    high = max(key(x) for x in points)
    return {
        "minimum": fraction_payload(low) if isinstance(low, Fraction) else low,
        "minimum_points": [x["exponents"] for x in points if key(x) == low],
        "maximum": fraction_payload(high) if isinstance(high, Fraction) else high,
        "maximum_points": [x["exponents"] for x in points if key(x) == high],
    }


def analyze(primes: list[int], level: int) -> dict:
    if level < 1:
        raise GeometryInputError("level must be at least 1")
    points = [point_record(primes, a) for a in compositions(level, len(primes))]
    expected = comb(level + len(primes) - 1, len(primes) - 1)
    fields = {name: extrema(points, name) for name in ("n", "tau", "sigma", "phi", "omega")}
    fields["sigma_over_n"] = extrema(points, "sigma_over_n", fraction_field=True)
    fields["phi_over_n"] = extrema(points, "phi_over_n", fraction_field=True)
    balanced = sorted([level // len(primes) + (1 if i < level % len(primes) else 0) for i in range(len(primes))])
    tau_max_shapes = sorted(sorted(x) for x in fields["tau"]["maximum_points"])
    return {
        "schema": "PVG-LEVEL-TERRAIN-001",
        "axes": primes,
        "level": level,
        "dimension": len(primes) - 1,
        "point_count": len(points),
        "expected_point_count": expected,
        "points": points,
        "extrema": fields,
        "verification": {
            "point_count": len(points) == expected,
            "Omega_constant": all(x["Omega"] == level for x in points),
            "lambda_constant": len({x["lambda"] for x in points}) == 1,
            "size_vertices": fields["n"]["minimum_points"] == [[level] + [0] * (len(primes)-1)] and fields["n"]["maximum_points"] == [[0] * (len(primes)-1) + [level]],
            "tau_balanced_maximum": all(sorted(x) == balanced for x in fields["tau"]["maximum_points"]),
        },
        "classification": "exact finite terrain atlas on one fixed PVG simplex level; no asymptotic or novelty claim",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Enumerate arithmetic terrain on a fixed PVG level")
    ap.add_argument("axes", help="comma-separated prime axes, e.g. 2,3,5")
    ap.add_argument("level", type=int)
    ap.add_argument("--compact", action="store_true")
    args = ap.parse_args()
    try:
        report = analyze(parse_primes(args.axes), args.level)
    except (GeometryInputError, ValueError) as exc:
        print(json.dumps({"status": "invalid_level_terrain_input", "reason": str(exc)}, indent=2))
        return 2
    print(json.dumps(report, sort_keys=True, indent=None if args.compact else 2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
