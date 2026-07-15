"""Verify blockwise channel-dependent Fourier tail bounds.

Finite benchmark only; no asymptotic or Goldbach claim.
"""
from __future__ import annotations

import cmath
import json
import math
from collections import defaultdict
from pathlib import Path

TOL = 1e-9


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def von_mangoldt(n: int) -> float:
    if n < 2:
        return 0.0
    if is_prime(n):
        return math.log(n)
    for p in range(2, int(math.isqrt(n)) + 1):
        if not is_prime(p):
            continue
        x = n
        while x % p == 0:
            x //= p
        if x == 1:
            return math.log(p)
    return 0.0


def data(N: int, r: int):
    g = math.gcd(2, r)
    q = r // g
    u = 2 // g
    z = [0.0] * q
    zpp = [0.0] * q
    h = [0.0] * q
    for a in range(1, N):
        b = N - a
        la, lb = von_mangoldt(a), von_mangoldt(b)
        c = (u * a) % q
        z[c] += la * lb
        if is_prime(a) and is_prime(b):
            zpp[c] += math.log(a) * math.log(b)
        if la > 0.0 and not is_prime(a):
            h[c] += la
    hat = [
        sum(z[c] * cmath.exp(2j * math.pi * k * c / q) for c in range(q))
        for k in range(q)
    ]
    return q, u, z, zpp, h, hat


def pair_indices(q: int):
    return list(range(1, (q - 1) // 2 + 1)), (q // 2 if q % 2 == 0 else None)


def blocks(indices, mode: str):
    indices = list(indices)
    if not indices:
        return []
    if mode == "one":
        return [indices]
    if mode == "singleton":
        return [[k] for k in indices]
    if mode.startswith("chunks"):
        count = int(mode[6:])
        width = math.ceil(len(indices) / count)
        return [indices[i : i + width] for i in range(0, len(indices), width)]
    if mode == "dyadic":
        out = []
        start, maximum = 1, max(indices)
        while start <= maximum:
            end = min(maximum, 2 * start - 1)
            block = [k for k in indices if start <= k <= end]
            if block:
                out.append(block)
            start *= 2
        return out
    raise ValueError(mode)


def tail_bound(hat, q: int, c: int, partition) -> float:
    answer = 0.0
    for block in partition:
        energy = sum(abs(hat[k]) ** 2 for k in block)
        phase_mass = 0.0
        for k in block:
            phase = cmath.phase(hat[k]) if abs(hat[k]) > TOL else 0.0
            phase_mass += math.cos(phase - 2 * math.pi * k * c / q) ** 2
        answer += (2.0 / q) * math.sqrt(max(0.0, energy * phase_mass))
    return answer


def run(max_N: int = 300, max_r: int = 20):
    modes = ["one", "chunks2", "chunks3", "dyadic", "singleton"]
    certificates = {K: defaultdict(int) for K in range(4)}
    false_certificates = {K: defaultdict(int) for K in range(4)}
    bound_mismatches = 0
    refinement_mismatches = 0
    effective_channels = 0
    prime_positive_channels = 0

    for N in range(2, max_N + 1):
        for r in range(1, max_r + 1):
            q, u, z, zpp, h, hat = data(N, r)
            pairs, nyquist = pair_indices(q)
            effective_channels += q
            prime_positive_channels += sum(value > TOL for value in zpp)

            for K in range(4):
                selected = set(sorted(pairs, key=lambda k: abs(hat[k]) ** 2, reverse=True)[:K])
                remaining = [k for k in pairs if k not in selected]
                partitions = {mode: blocks(remaining, mode) for mode in modes}

                for c in range(q):
                    main = sum(z) / q
                    main += sum(
                        (2.0 / q)
                        * (hat[k] * cmath.exp(-2j * math.pi * k * c / q)).real
                        for k in selected
                    )
                    if nyquist is not None:
                        main += (
                            hat[nyquist]
                            * cmath.exp(-2j * math.pi * nyquist * c / q)
                        ).real / q

                    actual_tail = sum(
                        (2.0 / q)
                        * (hat[k] * cmath.exp(-2j * math.pi * k * c / q)).real
                        for k in remaining
                    )
                    contamination = math.log(N) * (h[c] + h[(u * N - c) % q])
                    previous = None
                    for mode in modes:
                        bound = tail_bound(hat, q, c, partitions[mode])
                        if abs(actual_tail) > bound + 1e-7:
                            bound_mismatches += 1
                        if previous is not None and mode in {"chunks2", "chunks3", "singleton"}:
                            # The listed chunk partitions are not necessarily nested; only endpoints are universal.
                            pass
                        if main > bound + contamination + TOL:
                            certificates[K][mode] += 1
                            if zpp[c] <= TOL:
                                false_certificates[K][mode] += 1

                    if tail_bound(hat, q, c, partitions["singleton"]) > tail_bound(
                        hat, q, c, partitions["one"]
                    ) + 1e-7:
                        refinement_mismatches += 1

    return {
        "schema": "pvg.additive-fiber.blockwise-channel-phase-tail.v1",
        "status": "PASS" if not bound_mismatches and not refinement_mismatches and all(
            not any(v.values()) for v in false_certificates.values()
        ) else "FAIL",
        "range": {"N": [2, max_N], "r": [1, max_r], "K": [0, 1, 2, 3]},
        "effective_channels": effective_channels,
        "prime_positive_channels": prime_positive_channels,
        "bound_mismatches": bound_mismatches,
        "endpoint_refinement_mismatches": refinement_mismatches,
        "certificates": {str(K): dict(certificates[K]) for K in range(4)},
        "false_certificates": {str(K): dict(false_certificates[K]) for K in range(4)},
        "notes": [
            "Energy-ranked principal pairs are used.",
            "The channel coordinate is c=(2/gcd(2,r))*a mod q.",
            "Reflection for contamination is c -> u*N-c mod q.",
            "Singleton blocks remove within-block Cauchy-Schwarz loss but still take absolute values across frequencies.",
        ],
    }


if __name__ == "__main__":
    result = run()
    output = Path(__file__).resolve().parents[1] / "results" / "blockwise_channel_phase_tail_bound_verification_v1.2.json"
    output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
