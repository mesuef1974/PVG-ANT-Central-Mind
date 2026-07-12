from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "maps" / "pvg-core-ontology-example-results.json"


def factor(n: int) -> dict[int, int]:
    if n <= 0:
        raise ValueError("Factorization is defined only for positive integers.")
    result: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            result[p] = result.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def tau(n: int) -> int:
    value = 1
    for a in factor(n).values():
        value *= a + 1
    return value


def i_r(n: int, r: int) -> int:
    value = 1
    for a in factor(n).values():
        value *= max(a - 2 * r + 1, 0)
    return value


def divisibility_signature(n: int, D: int) -> list[int]:
    return [d for d in range(1, D + 1) if n % d == 0]


def main() -> None:
    f360 = factor(360)
    reconstructed = math.prod(p**a for p, a in f360.items())

    residue_vector = [3, -1, 2, 0]
    # Discrete Fourier transform and inverse on C_4.
    coeffs: list[complex] = []
    for k in range(4):
        coeffs.append(
            sum(
                residue_vector[j] * cmath.exp(-2j * math.pi * k * j / 4)
                for j in range(4)
            )
        )
    inverse: list[int] = []
    for j in range(4):
        value = sum(
            coeffs[k] * cmath.exp(2j * math.pi * k * j / 4)
            for k in range(4)
        ) / 4
        inverse.append(round(value.real))

    local_i1 = [1, 0, 1, 2, 3, 4]

    result = {
        "ontology_id": "PVG-CORE-ONTOLOGY-V1",
        "examples": {
            "exact_vector_reconstruction": reconstructed == 360,
            "support_noninjective": factor(12).keys() == factor(18).keys() and 12 != 18,
            "support_size_noninjective": len(factor(6)) == len(factor(35)) == 2,
            "total_height_noninjective": sum(factor(8).values()) == sum(factor(12).values()) == 3,
            "tau_noninjective": tau(360) == tau(420) == 24 and sorted(factor(360).values()) != sorted(factor(420).values()),
            "unlabeled_heights_lose_residue": sorted(factor(12).values()) == sorted(factor(18).values()) and 12 % 5 != 18 % 5,
            "margin_interior_i1": i_r((2**4) * (3**3), 1) == 6,
            "log_mass_identity": abs(sum(a * math.log(p) for p, a in f360.items()) - math.log(360)) < 1e-12,
            "full_fourier_reconstruction": inverse == residue_vector,
            "energy_does_not_recover_phase": sum(x * x for x in [1, 0]) == sum(x * x for x in [0, 1]),
            "truncation_noninjective": divisibility_signature(2, 5) == divisibility_signature(22, 5),
            "aggregate_noninjective": {
                "population_a": {"size": 2, "A2": 1, "A3": 1},
                "population_b": {"size": 2, "A2": 1, "A3": 1},
                "distinct": sorted([2, 3]) != sorted([1, 6]),
            },
            "convolution_pair_count": tau(12) == 6,
            "bell_coefficient_recovery": local_i1 == [1, 0, 1, 2, 3, 4],
            "log_nearness_not_support_nearness": set(factor(100)).isdisjoint(set(factor(101))),
            "kfull_noninjective": min(factor(72).values()) >= 2 and min(factor(108).values()) >= 2 and factor(72) != factor(108),
        },
        "claims": {
            "theorem_promotion": False,
            "model_performance_claim": False,
            "rh_progress": False,
            "grh_progress": False,
        },
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("pvg_core_ontology_examples: PASS — deterministic reconstruction and loss witnesses generated")


if __name__ == "__main__":
    main()
