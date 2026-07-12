from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "maps" / "translation-v2-pass002-example-results.json"


def main() -> None:
    primes = [2, 3, 5, 7, 11, 13, 17, 19]

    def chi4(p: int) -> int:
        if p % 2 == 0:
            return 0
        return 1 if p % 4 == 1 else -1

    distance_self = sum((1 - chi4(p) * chi4(p)) / p for p in primes if chi4(p) != 0)
    distance_one = sum((1 - chi4(p)) / p for p in primes if chi4(p) != 0)

    x = 4
    sharp = sum(1 for n in range(1, 10) if n <= x)
    triangular = sum(max(1 - n / x, 0) for n in range(1, 10))

    vector_a = [0, 0, 0, 2]
    vector_b = [1, 1, 1, 1]
    signs = [1, -1, 1, -1]
    diagonal = sum(value * value for value in signs)
    off_diagonal = sum(
        signs[i] * signs[j]
        for i in range(len(signs))
        for j in range(len(signs))
        if i != j
    )

    results = {
        "EX3-UNIFORMITY-EXPONENTIAL-CONSTANT": {
            "C_fixed_r3": 2**3,
            "C_growing_r10": 2**10,
            "ratio": 2**7,
            "uniform_without_bound": False,
        },
        "EX3-CONDUCTOR-PRINCIPAL-MOD4": {
            "s": 2,
            "L_mod4_over_zeta": 1 - 2 ** (-2),
            "correction_is_optional": False,
        },
        "EX3-SMOOTH-SHARP-BOUNDARY": {
            "x": x,
            "sharp": sharp,
            "triangular_smooth": triangular,
            "equal": sharp == triangular,
        },
        "EX3-TAUBERIAN-HYPOTHESIS-LEDGER": {
            "nonnegative_coefficients": True,
            "boundary_control_stated": False,
            "tauberian_transfer_certified": False,
        },
        "EX3-PRETENTIOUS-CHI4": {
            "prime_cutoff": 19,
            "distance_sq_chi4_to_self": round(distance_self, 12),
            "distance_sq_chi4_to_one": round(distance_one, 12),
        },
        "EX3-LOCAL-GLOBAL-DIVISIBILITY": {
            "x": 100,
            "p": 7,
            "empirical_probability": 14 / 100,
            "model_probability": 1 / 7,
            "absolute_error": abs(14 / 100 - 1 / 7),
        },
        "EX3-SHORT-INTERVAL-PARITY": {
            "global_even_density_first_100": 0.5,
            "interval_101_101_even_density": 0.0,
            "interval_102_102_even_density": 1.0,
        },
        "EX3-MOMENT-MAX-NONUNIQUENESS": {
            "vector_a_l2_sq": sum(value * value for value in vector_a),
            "vector_b_l2_sq": sum(value * value for value in vector_b),
            "vector_a_max": max(vector_a),
            "vector_b_max": max(vector_b),
        },
        "EX3-DISPERSION-OFFDIAGONAL": {
            "diagonal": diagonal,
            "off_diagonal": off_diagonal,
            "square_of_sum": sum(signs) ** 2,
            "identity_holds": diagonal + off_diagonal == sum(signs) ** 2,
        },
        "EX3-SUBSUMPTION-MATRIX": {
            "hypotheses_matched": 4,
            "hypotheses_required": 4,
            "new_analytic_method": False,
            "classification": "known framework application",
        },
        "EX3-VERTICAL-DECAY-BALANCE": {
            "growth_exponent_A": 3,
            "decay_order_N": 6,
            "integrable_tail_exponent": 3,
            "criterion_N_gt_A_plus_1": True,
        },
        "EX3-MATERIALITY-ABLATION": {
            "new_invariant": False,
            "shorter_proof": False,
            "tool_routing_gain": False,
            "improved_bound": False,
            "classification": "decorative reinterpretation",
        },
    }

    OUT.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {len(results)} Pass 002 examples to {OUT}")


if __name__ == "__main__":
    main()
