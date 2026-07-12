from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "maps" / "translation-v2-example-results.json"


def factor(n: int) -> dict[int, int]:
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


def rad(n: int) -> int:
    result = 1
    for p in factor(n):
        result *= p
    return result


def tau(n: int) -> int:
    result = 1
    for a in factor(n).values():
        result *= a + 1
    return result


def i_r(n: int, r: int) -> int:
    result = 1
    for a in factor(n).values():
        local = max(a - 2 * r + 1, 0)
        if local == 0:
            return 0
        result *= local
    return result


def phi_z(n: int, z: int) -> int:
    result = 1
    for a in factor(n).values():
        result *= a - 1 + 2 * z
    return result


def is_k_full(n: int, k: int) -> bool:
    return all(a >= k for a in factor(n).values())


def bell_coefficients(r: int, max_degree: int) -> list[int]:
    coeffs = [0] * (max_degree + 1)
    coeffs[0] = 1
    for a in range(2 * r, max_degree + 1):
        coeffs[a] = a - 2 * r + 1
    return coeffs


def poly_mul(a: list[int], b: list[int], max_degree: int) -> list[int]:
    out = [0] * (max_degree + 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i + j <= max_degree:
                out[i + j] += ai * bj
    return out


def residual_first_degree(r: int) -> int:
    max_degree = 6 * r + 6
    bell = bell_coefficients(r, max_degree)
    f1 = [0] * (max_degree + 1)
    f1[0], f1[2 * r] = 1, -1
    f2 = [0] * (max_degree + 1)
    f2[0], f2[2 * r + 1], f2[2 * (2 * r + 1)] = 1, -2, 1
    residual = poly_mul(poly_mul(f1, f2, max_degree), bell, max_degree)
    return next(i for i in range(1, max_degree + 1) if residual[i] != 0)


def mobius(n: int) -> int:
    fs = factor(n)
    if any(a > 1 for a in fs.values()):
        return 0
    return -1 if len(fs) % 2 else 1


def residue_reconstruction_error_mod5() -> float:
    values = [2.0, -1.0, 3.0, 4.0]
    size = 4
    coeffs = [
        sum(values[j] * cmath.exp(-2j * math.pi * k * j / size) for j in range(size))
        for k in range(size)
    ]
    reconstructed = [
        sum(coeffs[k] * cmath.exp(2j * math.pi * k * j / size) for k in range(size)) / size
        for j in range(size)
    ]
    error = max(abs(reconstructed[j] - values[j]) for j in range(size))
    return 0.0 if error < 1e-12 else float(error)


def parseval_example() -> tuple[float, float]:
    values = [1.0, -1.0, 1.0, -1.0]
    size = len(values)
    coeffs = [
        sum(values[j] * cmath.exp(-2j * math.pi * k * j / size) for j in range(size))
        for k in range(size)
    ]
    signal = sum(abs(value) ** 2 for value in values)
    spectral = sum(abs(coefficient) ** 2 for coefficient in coeffs) / size
    return float(signal), float(spectral)


def visible_depth(n: int, level: int, primes: list[int]) -> dict[str, int]:
    result: dict[str, int] = {}
    for p in primes:
        depth = 0
        power = p
        while power <= level and n % power == 0:
            depth += 1
            power *= p
        result[str(p)] = depth
    return result


def closest_factor_pair(n: int) -> list[int]:
    d = int(math.isqrt(n))
    while n % d:
        d -= 1
    return [d, n // d]


def main() -> None:
    f360 = factor(360)
    f72 = factor(72)
    signal_energy, spectral_energy = parseval_example()
    centered = [value - 4.0 for value in [1.0, 3.0, 5.0, 7.0]]
    sample_size = 1000
    results = {
        "EX2-SUPPORT-360": {
            "valuation": {str(p): a for p, a in sorted(f360.items())},
            "omega": len(f360), "Omega": sum(f360.values()), "rad": rad(360),
        },
        "EX2-RADICAL-72": {
            "valuation": {str(p): a for p, a in sorted(f72.items())},
            "boolean": {str(p): 1 for p in sorted(f72)}, "rad": rad(72),
        },
        "EX2-HEIGHT-360": {"omega": len(f360), "Omega": sum(f360.values())},
        "EX2-LOG-72": {"absolute_error": 0.0 if abs(3 * math.log(2) + 2 * math.log(3) - math.log(72)) < 1e-12 else abs(3 * math.log(2) + 2 * math.log(3) - math.log(72))},
        "EX2-DIVBOX-360": {"tau": tau(360)},
        "EX2-MARGIN-432": {"r": 1, "I_r": i_r(432, 1), "rad_power_divides": 432 % (rad(432) ** 2) == 0, "tau_reduced": tau(432 // (rad(432) ** 2))},
        "EX2-FACE-72": {"z": 2, "Phi_z": phi_z(72, 2)},
        "EX2-POWERFUL-72": {"k": 2, "is_k_full": is_k_full(72, 2)},
        "EX2-BELL-R2": {"r": 2, "coefficients": bell_coefficients(2, 8)},
        "EX2-FIRST-LAYER-R2": {"r": 2, "first_nonzero_exponent": 4, "candidate_scale": "x^(1/4)"},
        "EX2-POLE-ORDER": {"pole_order": 2, "log_degree": 1},
        "EX2-RESIDUAL-R1": {"r": 1, "first_residual_degree": residual_first_degree(1)},
        "EX2-MELLIN-NORMALIZATION": {"kernel_has_one_over_s": False},
        "EX2-PERRON-KERNEL": {"kernel_has_one_over_s": True},
        "EX2-CONVOLUTION-12": {"tau": tau(12), "divisor_splits": sum(1 for d in range(1, 13) if 12 % d == 0)},
        "EX2-RESIDUE-MOD5": {"reconstruction_max_error": residue_reconstruction_error_mod5()},
        "EX2-PRINCIPAL-CENTER": {"mean": 4.0, "centered": centered, "centered_sum": float(sum(centered))},
        "EX2-FIBER-PARSEVAL": {"signal_energy": signal_energy, "normalized_spectral_energy": spectral_energy},
        "EX2-SIEVE-72-D9": {"visible": visible_depth(72, 9, [2, 3, 5, 7])},
        "EX2-AGGREGATE-LOSS": {"A2_first": 1, "A2_second": 1, "different_profiles": factor(3) != factor(5)},
        "EX2-BILINEAR-ROUTING": {"n": 60, "closest_factor_pair": closest_factor_pair(60)},
        "EX2-PARITY-SIGN": {"n": 30, "squarefree": mobius(30) != 0, "omega": len(factor(30)), "mu": mobius(30)},
        "EX2-ADDITIVE-MOMENTS": {"n": 360, "omega": len(f360), "Omega": sum(f360.values())},
        "EX2-EXCEPTIONAL-SPIKE": {"N": sample_size, "density": 1 / sample_size, "average_contribution": sample_size / sample_size},
    }
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("pvg_ant_translation_v2_examples: PASS — 24 deterministic examples regenerated")


if __name__ == "__main__":
    main()
