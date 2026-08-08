#!/usr/bin/env python3
"""Verify paired-frequency decomposition and compare K-pair selection rules."""

from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

N_MAX = 300
R_MAX = 20
K_VALUES = (0, 1, 2, 3)
TOL = 1e-8


def arithmetic_tables(limit: int):
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for n in range(p * p, limit + 1, p):
                is_prime[n] = False

    lam = [0.0] * (limit + 1)
    for p in range(2, limit + 1):
        if is_prime[p]:
            value = p
            lp = math.log(p)
            while value <= limit:
                lam[value] = lp
                if value > limit // p:
                    break
                value *= p
    return is_prime, lam


def channel_data(N: int, r: int, is_prime, lam):
    g = math.gcd(2, r)
    q = r // g
    u = 2 // g
    z = [0.0] * q
    pp = [0.0] * q
    hpp = [0.0] * q

    for a in range(1, N):
        c = (u * a) % q
        z[c] += lam[a] * lam[N - a]
        if is_prime[a] and is_prime[N - a]:
            pp[c] += math.log(a) * math.log(N - a)
        if lam[a] > 0.0 and not is_prime[a]:
            hpp[c] += lam[a]

    spectrum = []
    for k in range(q):
        spectrum.append(
            sum(z[c] * cmath.exp(2j * math.pi * k * c / q) for c in range(q))
        )
    return q, u, z, pp, hpp, spectrum


def main():
    is_prime, lam = arithmetic_tables(N_MAX)
    strategies = ("negative", "absolute_channel", "energy")
    certificates = {s: {str(k): 0 for k in K_VALUES} for s in strategies}
    false_certificates = {s: {str(k): 0 for k in K_VALUES} for s in strategies}

    reconstruction_mismatches = 0
    tail_bound_mismatches = 0
    prime_positive_channels = 0
    effective_channels = 0
    certificate_checks = 0

    for N in range(2, N_MAX + 1):
        for r in range(1, R_MAX + 1):
            q, u, z, pp, hpp, spectrum = channel_data(N, r, is_prime, lam)
            mean = sum(z) / q
            pair_reps = list(range(1, (q + 1) // 2))
            nyquist = q // 2 if q % 2 == 0 else None

            for c in range(q):
                effective_channels += 1
                if pp[c] > TOL:
                    prime_positive_channels += 1

                reflected = (u * N - c) % q
                contamination = math.log(N) * (hpp[c] + hpp[reflected])
                nyquist_term = 0.0
                if nyquist is not None:
                    nyquist_term = (
                        spectrum[nyquist]
                        * cmath.exp(-2j * math.pi * nyquist * c / q)
                    ).real / q

                pair_contribution = {
                    k: (2.0 / q)
                    * (
                        spectrum[k] * cmath.exp(-2j * math.pi * k * c / q)
                    ).real
                    for k in pair_reps
                }

                reconstructed = mean + nyquist_term + sum(pair_contribution.values())
                if abs(reconstructed - z[c]) > TOL:
                    reconstruction_mismatches += 1

                orders = {
                    "negative": sorted(pair_reps, key=lambda k: pair_contribution[k]),
                    "absolute_channel": sorted(
                        pair_reps, key=lambda k: abs(pair_contribution[k]), reverse=True
                    ),
                    "energy": sorted(
                        pair_reps, key=lambda k: abs(spectrum[k]), reverse=True
                    ),
                }

                for strategy, order in orders.items():
                    for K in K_VALUES:
                        selected = set(order[:K])
                        remaining = [k for k in pair_reps if k not in selected]
                        partial = mean + nyquist_term + sum(
                            pair_contribution[k] for k in selected
                        )
                        tail_bound = 0.0
                        if remaining:
                            tail_bound = (2.0 / q) * math.sqrt(
                                len(remaining)
                                * sum(abs(spectrum[k]) ** 2 for k in remaining)
                            )
                        actual_tail = sum(pair_contribution[k] for k in remaining)
                        if abs(actual_tail) > tail_bound + TOL:
                            tail_bound_mismatches += 1

                        if partial - tail_bound > contamination + TOL:
                            certificates[strategy][str(K)] += 1
                            if pp[c] <= TOL:
                                false_certificates[strategy][str(K)] += 1
                        certificate_checks += 1

    result = {
        "schema": "pvg.channel-paired-frequency-energy-selection.v1",
        "status": "PASS"
        if reconstruction_mismatches == 0
        and tail_bound_mismatches == 0
        and all(v == 0 for s in false_certificates.values() for v in s.values())
        else "FAIL",
        "N_range": [2, N_MAX],
        "r_range": [1, R_MAX],
        "K_values": list(K_VALUES),
        "effective_channels": effective_channels,
        "certificate_checks": certificate_checks,
        "prime_positive_channels": prime_positive_channels,
        "reconstruction_mismatches": reconstruction_mismatches,
        "tail_bound_mismatches": tail_bound_mismatches,
        "certificates": certificates,
        "false_certificates": false_certificates,
        "observations": [
            "Energy selection minimizes the declared uniform L2 tail bound for fixed K.",
            "Most-negative channel contributions are not optimal under that bound.",
            "All certificates are sufficient only; failure to certify does not imply absence of a prime-prime representation.",
        ],
    }

    out = Path(__file__).resolve().parents[1] / "results" / "channel_paired_frequency_energy_selection_verification_v1.2.json"
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
