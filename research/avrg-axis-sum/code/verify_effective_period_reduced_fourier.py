#!/usr/bin/env python3
"""Verify the effective-period reduced Fourier theorem.

Checks:
- support on the admissible channel coset;
- exact full/reduced channel equivalence;
- reduced Fourier inversion;
- full/reduced Fourier coefficient relation;
- frequency redundancy for even moduli;
- Parseval on the effective period.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from collections import defaultdict
from pathlib import Path


def von_mangoldt(n: int) -> float:
    if n < 2:
        return 0.0
    p = None
    d = 2
    while d * d <= n:
        if n % d == 0:
            p = d
            break
        d += 1
    if p is None:
        return math.log(n)
    t = n
    while t % p == 0:
        t //= p
    return math.log(p) if t == 1 else 0.0


def run(max_n: int, max_r: int, tolerance: float) -> dict:
    counts: dict[str, int] = defaultdict(int)
    max_error: dict[str, float] = defaultdict(float)

    for n in range(2, max_n + 1):
        weights = [
            von_mangoldt(a) * von_mangoldt(n - a)
            for a in range(1, n)
        ]
        total_mass = sum(weights)

        for r in range(1, max_r + 1):
            g = math.gcd(2, r)
            q = r // g
            u = 2 // g

            full = [0.0] * r
            reduced = [0.0] * q
            for a, weight in enumerate(weights, start=1):
                full[(2 * a - n) % r] += weight
                reduced[(u * a) % q] += weight

            for d in range(r):
                admissible = (d + n) % g == 0
                expected = reduced[((d + n) // g) % q] if admissible else 0.0
                error = abs(full[d] - expected)
                max_error["channel_reduction"] = max(
                    max_error["channel_reduction"], error
                )
                counts["channel_checks"] += 1
                if error > tolerance:
                    counts["channel_reduction_mismatches"] += 1

            reduced_hat = [
                sum(
                    reduced[c] * cmath.exp(2j * math.pi * k * c / q)
                    for c in range(q)
                )
                for k in range(q)
            ]

            full_hat = []
            for h in range(r):
                value = sum(
                    full[d] * cmath.exp(2j * math.pi * h * d / r)
                    for d in range(r)
                )
                full_hat.append(value)
                expected = (
                    cmath.exp(-2j * math.pi * h * n / r)
                    * reduced_hat[h % q]
                )
                error = abs(value - expected)
                max_error["fourier_relation"] = max(
                    max_error["fourier_relation"], error
                )
                counts["frequency_checks"] += 1
                if error > tolerance:
                    counts["fourier_relation_mismatches"] += 1

            for c in range(q):
                reconstructed = sum(
                    reduced_hat[k] * cmath.exp(-2j * math.pi * k * c / q)
                    for k in range(q)
                ) / q
                error = abs(reconstructed - reduced[c])
                max_error["reduced_inversion"] = max(
                    max_error["reduced_inversion"], error
                )
                counts["inversion_checks"] += 1
                if error > tolerance:
                    counts["inversion_mismatches"] += 1

            if r > q:
                phase = cmath.exp(-2j * math.pi * n / g)
                for h in range(q):
                    error = abs(full_hat[h + q] - phase * full_hat[h])
                    max_error["frequency_redundancy"] = max(
                        max_error["frequency_redundancy"], error
                    )
                    counts["redundancy_checks"] += 1
                    if error > tolerance:
                        counts["redundancy_mismatches"] += 1

            lhs = sum(abs(value - total_mass / q) ** 2 for value in reduced)
            rhs = sum(abs(reduced_hat[k]) ** 2 for k in range(1, q)) / q
            error = abs(lhs - rhs)
            max_error["parseval"] = max(max_error["parseval"], error)
            counts["parseval_checks"] += 1
            if error > tolerance:
                counts["parseval_mismatches"] += 1

    mismatch_keys = [key for key in counts if key.endswith("mismatches")]
    total_mismatches = sum(counts[key] for key in mismatch_keys)

    return {
        "schema": "pvg.addition-fibers.effective-period-fourier-verification.v1",
        "status": "PASS" if total_mismatches == 0 else "FAIL",
        "N_range": [2, max_n],
        "r_range": [1, max_r],
        "tolerance": tolerance,
        "counts": dict(counts),
        "maximum_absolute_errors": dict(max_error),
        "total_mismatches": total_mismatches,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=500)
    parser.add_argument("--max-r", type=int, default=40)
    parser.add_argument("--tolerance", type=float, default=1e-8)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = run(args.max_n, args.max_r, args.tolerance)
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
