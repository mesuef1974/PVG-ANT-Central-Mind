#!/usr/bin/env python3
"""Verify the local higher-prime-power contamination bound.

Checks, for 2 <= N <= MAX_N and 1 <= r <= MAX_R, every residue channel d:

E_hpp(N,r,d) <= log(N) * (H(N,r,d) + H(N,r,-d)).

Also verifies that the sufficient local certificate never produces a false
prime-prime conclusion.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

MAX_N = 1000
MAX_R = 30
TOL = 1e-9


def build_tables(limit: int):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    von_mangoldt = [0.0] * (limit + 1)

    for p in range(2, limit + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False
            power = p
            while power <= limit:
                von_mangoldt[power] = math.log(p)
                power *= p

    is_higher_prime_power = [False] * (limit + 1)
    for n in range(2, limit + 1):
        is_higher_prime_power[n] = (
            von_mangoldt[n] > 0.0 and not is_prime[n]
        )

    return is_prime, von_mangoldt, is_higher_prime_power


def main() -> None:
    is_prime, lam, is_hpp = build_tables(MAX_N)

    channel_checks = 0
    bound_mismatches = 0
    certificate_successes = 0
    false_certificates = 0
    prime_positive_channels = 0
    maximum_ratio = 0.0
    maximum_ratio_case = None

    for N in range(2, MAX_N + 1):
        log_n = math.log(N)
        for r in range(1, MAX_R + 1):
            y_lambda = [0.0] * r
            y_pp = [0.0] * r
            h_local = [0.0] * r

            for a in range(1, N):
                b = N - a
                d = (2 * a - N) % r
                la = lam[a]
                lb = lam[b]

                y_lambda[d] += la * lb
                if is_prime[a] and is_prime[b]:
                    y_pp[d] += la * lb
                if is_hpp[a]:
                    h_local[d] += la

            for d in range(r):
                contamination = y_lambda[d] - y_pp[d]
                bound = log_n * (h_local[d] + h_local[(-d) % r])
                channel_checks += 1

                if contamination < -TOL or contamination > bound + TOL:
                    bound_mismatches += 1

                if bound > TOL:
                    ratio = contamination / bound
                    if ratio > maximum_ratio:
                        maximum_ratio = ratio
                        maximum_ratio_case = {
                            "N": N,
                            "r": r,
                            "d": d,
                            "contamination": contamination,
                            "bound": bound,
                            "von_mangoldt_channel_mass": y_lambda[d],
                            "prime_prime_channel_mass": y_pp[d],
                        }

                if y_pp[d] > TOL:
                    prime_positive_channels += 1

                if y_lambda[d] > bound + TOL:
                    certificate_successes += 1
                    if y_pp[d] <= TOL:
                        false_certificates += 1

    result = {
        "schema": "pvg.local-channel-hpp-contamination-verification.v1",
        "status": "PASS" if bound_mismatches == 0 and false_certificates == 0 else "FAIL",
        "N_range": [2, MAX_N],
        "modulus_range": [1, MAX_R],
        "channel_checks": channel_checks,
        "bound_mismatches": bound_mismatches,
        "certificate_successes": certificate_successes,
        "false_certificates": false_certificates,
        "prime_positive_channels": prime_positive_channels,
        "maximum_observed_contamination_to_bound_ratio": maximum_ratio,
        "maximum_ratio_case": maximum_ratio_case,
        "tolerance": TOL,
    }

    output = Path(__file__).resolve().parents[1] / "results" / "local_channel_hpp_contamination_bound_verification_v1.2.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
