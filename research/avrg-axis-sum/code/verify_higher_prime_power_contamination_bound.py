#!/usr/bin/env python3
"""Verify elementary higher-prime-power contamination bounds.

Checks, for 2 <= N <= max_n:
  S_hpp(N) <= sqrt(N) log N,
  E_hpp(N) <= 2 log N S_hpp(N),
  E_hpp(N) <= 2 sqrt(N) (log N)^2.

Also records how often the computable certificate
  R_Lambda(N) > 2 log N S_hpp(N)
implies positive prime-prime mass on the tested even range.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path


def prime_sieve(limit: int) -> list[bool]:
    is_prime = [True] * (limit + 1)
    if limit >= 0:
        is_prime[0] = False
    if limit >= 1:
        is_prime[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
    return is_prime


def von_mangoldt_components(limit: int) -> tuple[list[float], list[float], list[float]]:
    is_prime = prime_sieve(limit)
    lam = [0.0] * (limit + 1)
    lam_pr = [0.0] * (limit + 1)
    lam_hpp = [0.0] * (limit + 1)

    for p in range(2, limit + 1):
        if not is_prime[p]:
            continue
        log_p = math.log(p)
        lam[p] = log_p
        lam_pr[p] = log_p
        power = p * p
        while power <= limit:
            lam[power] = log_p
            lam_hpp[power] = log_p
            power *= p
    return lam, lam_pr, lam_hpp


def additive_mass(values_left: list[float], values_right: list[float], n: int) -> float:
    return sum(values_left[a] * values_right[n - a] for a in range(1, n))


def run(max_n: int, tolerance: float) -> dict:
    lam, lam_pr, lam_hpp = von_mangoldt_components(max_n)
    cumulative_hpp = [0.0] * (max_n + 1)
    for n in range(1, max_n + 1):
        cumulative_hpp[n] = cumulative_hpp[n - 1] + lam_hpp[n]

    cumulative_bound_mismatches = 0
    sharp_bound_mismatches = 0
    explicit_bound_mismatches = 0
    decomposition_mismatches = 0

    max_sharp_ratio = 0.0
    max_explicit_ratio = 0.0
    worst_sharp = None
    worst_explicit = None

    even_cases = 0
    certificate_successes = 0
    certificate_failures = []

    for n in range(2, max_n + 1):
        r_lambda = additive_mass(lam, lam, n)
        r_pp = additive_mass(lam_pr, lam_pr, n)
        contamination = r_lambda - r_pp

        r_ph = additive_mass(lam_pr, lam_hpp, n)
        r_hp = additive_mass(lam_hpp, lam_pr, n)
        r_hh = additive_mass(lam_hpp, lam_hpp, n)
        if abs(contamination - (r_ph + r_hp + r_hh)) > tolerance:
            decomposition_mismatches += 1

        s_hpp = cumulative_hpp[n]
        cumulative_bound = math.sqrt(n) * math.log(n)
        sharp_bound = 2.0 * math.log(n) * s_hpp
        explicit_bound = 2.0 * math.sqrt(n) * math.log(n) ** 2

        if s_hpp > cumulative_bound + tolerance:
            cumulative_bound_mismatches += 1
        if contamination > sharp_bound + tolerance:
            sharp_bound_mismatches += 1
        if contamination > explicit_bound + tolerance:
            explicit_bound_mismatches += 1

        if sharp_bound > 0.0:
            ratio = contamination / sharp_bound
            if ratio > max_sharp_ratio:
                max_sharp_ratio = ratio
                worst_sharp = {
                    "N": n,
                    "contamination": contamination,
                    "bound": sharp_bound,
                    "R_Lambda": r_lambda,
                    "R_pp": r_pp,
                }

        ratio = contamination / explicit_bound
        if ratio > max_explicit_ratio:
            max_explicit_ratio = ratio
            worst_explicit = {
                "N": n,
                "contamination": contamination,
                "bound": explicit_bound,
                "R_Lambda": r_lambda,
                "R_pp": r_pp,
            }

        if n % 2 == 0:
            even_cases += 1
            if r_lambda > sharp_bound + tolerance:
                certificate_successes += 1
                if r_pp <= tolerance:
                    raise AssertionError("Certificate succeeded but prime-prime mass was nonpositive")
            else:
                certificate_failures.append({"N": n, "R_Lambda": r_lambda, "bound": sharp_bound})

    total_mismatches = (
        cumulative_bound_mismatches
        + sharp_bound_mismatches
        + explicit_bound_mismatches
        + decomposition_mismatches
    )

    return {
        "schema": "pvg.von-mangoldt.hpp-contamination-bound-verification.v1",
        "status": "PASS" if total_mismatches == 0 else "FAIL",
        "N_range": [2, max_n],
        "tolerance": tolerance,
        "checks": {
            "decomposition_mismatches": decomposition_mismatches,
            "S_hpp_bound_mismatches": cumulative_bound_mismatches,
            "sharp_contamination_bound_mismatches": sharp_bound_mismatches,
            "explicit_contamination_bound_mismatches": explicit_bound_mismatches,
            "total_mismatches": total_mismatches,
        },
        "sharpness": {
            "maximum_E_over_2logN_S_hpp": max_sharp_ratio,
            "worst_sharp_case": worst_sharp,
            "maximum_E_over_2sqrtN_logN_squared": max_explicit_ratio,
            "worst_explicit_case": worst_explicit,
        },
        "computed_even_certificate": {
            "even_cases": even_cases,
            "successes": certificate_successes,
            "failures": len(certificate_failures),
            "failure_cases": certificate_failures,
            "classification": "finite computation only; not a proof for untested N",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=5000)
    parser.add_argument("--tolerance", type=float, default=1e-9)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = run(args.max_n, args.tolerance)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
