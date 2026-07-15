"""Verify frequency-dominance precedence constraints.

Benchmark:
  4 <= N <= 120, 3 <= r <= 30, budgets B <= 4.

The verifier reconstructs von Mangoldt channel data, paired-frequency gains,
channelwise dominance, exhaustive optima, and canonical optima satisfying
selected precedence constraints. It also checks the N=15,r=12,B=2
counterexample to naive dominated-candidate deletion.
"""

from __future__ import annotations

import cmath
import itertools
import json
import math
from pathlib import Path

EPS = 1e-10


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
    for p in range(2, int(math.isqrt(n)) + 1):
        if n % p == 0:
            x = n
            while x % p == 0:
                x //= p
            return math.log(p) if x == 1 else 0.0
    return math.log(n)


def build_instance(N: int, r: int):
    g = math.gcd(2, r)
    q = r // g
    u = 2 // g
    z = [0.0] * q
    h = [0.0] * q
    for a in range(1, N):
        la = von_mangoldt(a)
        lb = von_mangoldt(N - a)
        c = (u * a) % q
        z[c] += la * lb
        if la > 0.0 and not is_prime(a):
            h[c] += la
    contamination = [
        math.log(N) * (h[c] + h[(u * N - c) % q]) for c in range(q)
    ]
    hat = [
        sum(z[c] * cmath.exp(2j * math.pi * k * c / q) for c in range(q))
        for k in range(q)
    ]
    frequencies = list(range(1, (q - 1) // 2 + 1))
    base = [sum(z) / q for _ in range(q)]
    if q % 2 == 0:
        nyquist = hat[q // 2].real / q
        base = [base[c] + nyquist * ((-1) ** c) for c in range(q)]
    contributions = {
        k: [
            (2.0 / q)
            * (hat[k] * cmath.exp(-2j * math.pi * k * c / q)).real
            for c in range(q)
        ]
        for k in frequencies
    }
    gains = {
        k: [x + abs(x) for x in contributions[k]] for k in frequencies
    }
    lower0 = [
        base[c] - sum(abs(contributions[k][c]) for k in frequencies)
        for c in range(q)
    ]
    return q, frequencies, contamination, lower0, gains


def objective(selected, lower0, gains, contamination) -> int:
    return sum(
        lower0[c] + sum(gains[k][c] for k in selected)
        > contamination[c] + EPS
        for c in range(len(contamination))
    )


def precedence_map(frequencies, gains, q):
    parents = {}
    for j in frequencies:
        equals = [
            k
            for k in frequencies
            if k < j
            and all(abs(gains[k][c] - gains[j][c]) <= EPS for c in range(q))
        ]
        if equals:
            parents[j] = min(equals)
            continue
        dominators = [
            k
            for k in frequencies
            if k != j
            and all(gains[k][c] >= gains[j][c] - EPS for c in range(q))
            and any(gains[k][c] > gains[j][c] + 1e-8 for c in range(q))
        ]
        if dominators:
            parents[j] = max(dominators, key=lambda k: (sum(gains[k]), -k))
    return parents


def canonical(selected, parents) -> bool:
    selected = set(selected)
    return all(j not in selected or parent in selected for j, parent in parents.items())


def main() -> None:
    total_subsets = 0
    canonical_subsets = 0
    optimization_cases = 0
    optimum_mismatches = 0
    constrained_instances = 0

    for N in range(4, 121):
        for r in range(3, 31):
            q, frequencies, contamination, lower0, gains = build_instance(N, r)
            if len(frequencies) < 2:
                continue
            parents = precedence_map(frequencies, gains, q)
            constrained_instances += bool(parents)
            for budget in range(0, min(4, len(frequencies)) + 1):
                optimization_cases += 1
                unrestricted_values = []
                canonical_values = []
                for size in range(budget + 1):
                    for selected in itertools.combinations(frequencies, size):
                        total_subsets += 1
                        value = objective(selected, lower0, gains, contamination)
                        unrestricted_values.append(value)
                        if canonical(selected, parents):
                            canonical_subsets += 1
                            canonical_values.append(value)
                if max(unrestricted_values, default=0) != max(canonical_values, default=0):
                    optimum_mismatches += 1

    q, frequencies, contamination, lower0, gains = build_instance(15, 12)
    deletion_counterexample = {
        "N": 15,
        "r": 12,
        "q": q,
        "dominant_frequency": 2,
        "dominated_frequency": 1,
        "F_empty": objective((), lower0, gains, contamination),
        "F_1": objective((1,), lower0, gains, contamination),
        "F_2": objective((2,), lower0, gains, contamination),
        "F_1_2": objective((1, 2), lower0, gains, contamination),
    }

    summary = {
        "schema": "pvg.frequency-dominance-precedence.v1",
        "status": "PASS" if optimum_mismatches == 0 else "FAIL",
        "benchmark": {"N": [4, 120], "r": [3, 30], "max_budget": 4},
        "optimization_cases": optimization_cases,
        "instances_with_precedence_constraints": constrained_instances,
        "unrestricted_subsets_evaluated": total_subsets,
        "canonical_subsets_evaluated": canonical_subsets,
        "subsets_removed_by_precedence": total_subsets - canonical_subsets,
        "optimum_mismatches": optimum_mismatches,
        "naive_deletion_counterexample": deletion_counterexample,
    }
    out = Path(__file__).resolve().parents[1] / "results" / "frequency_dominance_precedence_verification_v1.2.json"
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
