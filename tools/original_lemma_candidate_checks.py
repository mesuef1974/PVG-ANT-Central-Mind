from __future__ import annotations

import cmath
import json
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = ROOT / "research" / "original-lemma-selection" / "001" / "candidate-check-expected.json"
GENERATED = ROOT / "research" / "original-lemma-selection" / "001" / "candidate-check-results.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def valuation_exponents(n: int) -> list[int]:
    require(n >= 1, "n must be positive")
    exponents: list[int] = []
    p = 2
    remaining = n
    while p * p <= remaining:
        exponent = 0
        while remaining % p == 0:
            exponent += 1
            remaining //= p
        if exponent:
            exponents.append(exponent)
        p += 1
    if remaining > 1:
        exponents.append(1)
    return exponents


def face_sum_by_enumeration(exponents: list[int], z: int) -> int:
    total = 0
    for beta in product(*(range(a + 1) for a in exponents)):
        boundary = sum(value in (0, a) for value, a in zip(beta, exponents))
        total += z**boundary
    return total


def face_product(exponents: list[int], z: int) -> int:
    value = 1
    for exponent in exponents:
        value *= exponent - 1 + 2 * z
    return value


def convolve(left: list[int], right: list[int], length: int) -> list[int]:
    result = [0] * length
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if i + j >= length:
                break
            result[i + j] += a * b
    return result


def factor_polynomial(r: int, length: int) -> list[int]:
    a = 2 * r
    b = 2 * r + 1
    # Multiply (1-x^a) by (1-2x^b+x^(2b)).
    first = [0] * length
    first[0] = 1
    if a < length:
        first[a] = -1
    second = [0] * length
    second[0] = 1
    if b < length:
        second[b] = -2
    if 2 * b < length:
        second[2 * b] = 1
    return convolve(first, second, length)


def margin_local_series(r: int, length: int) -> list[int]:
    return [1 if exponent == 0 else max(exponent - 2 * r + 1, 0) for exponent in range(length)]


def truncated_margin_series(r: int, y: complex, cutoff: int = 160) -> complex:
    return 1 + sum((exponent - 2 * r + 1) * y**exponent for exponent in range(2 * r, cutoff + 1))


def matrix_rank(matrix: list[list[int]]) -> int:
    rows = [[Fraction(value) for value in row] for row in matrix]
    if not rows:
        return 0
    n_rows = len(rows)
    n_cols = len(rows[0])
    rank = 0
    pivot_col = 0
    while rank < n_rows and pivot_col < n_cols:
        pivot = next((i for i in range(rank, n_rows) if rows[i][pivot_col] != 0), None)
        if pivot is None:
            pivot_col += 1
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        pivot_value = rows[rank][pivot_col]
        rows[rank] = [value / pivot_value for value in rows[rank]]
        for i in range(n_rows):
            if i == rank or rows[i][pivot_col] == 0:
                continue
            multiple = rows[i][pivot_col]
            rows[i] = [left - multiple * right for left, right in zip(rows[i], rows[rank])]
        rank += 1
        pivot_col += 1
    return rank


def mobius(n: int) -> int:
    exponents = valuation_exponents(n)
    if any(exponent > 1 for exponent in exponents):
        return 0
    return -1 if len(exponents) % 2 else 1


def main() -> None:
    require(EXPECTED.exists(), f"Missing expected checks: {EXPECTED}")

    for n in range(1, 201):
        exponents = valuation_exponents(n)
        for z in [0, 1, 2, 3]:
            require(
                face_sum_by_enumeration(exponents, z) == face_product(exponents, z),
                f"Face enumerator identity failed at n={n}, z={z}",
            )

    residual_orders: dict[str, int] = {}
    for r in range(1, 6):
        length = 4 * r + 12
        residual = convolve(factor_polynomial(r, length), margin_local_series(r, length), length)
        require(residual[0] == 1, f"Bad residual constant for r={r}")
        first = next(index for index, coefficient in enumerate(residual[1:], start=1) if coefficient != 0)
        require(first == 2 * r + 2, f"Unexpected residual order for r={r}: {first}")
        residual_orders[str(r)] = first

    # Independent numerical check: compare the closed Bell-series formula with
    # a direct truncated sum of its defining coefficients for several roots of unity.
    for r in [1, 2, 3]:
        for root_index in [0, 1, 2, 3, 4]:
            chi = cmath.exp(2j * cmath.pi * root_index / 5)
            y = chi * 0.07
            closed_form = 1 + y ** (2 * r) / (1 - y) ** 2
            direct_series = truncated_margin_series(r, y)
            require(
                abs(closed_form - direct_series) <= 1e-13,
                f"Twisted local series failed for r={r}, root={root_index}",
            )

    tested_pairs = [[8, 4], [12, 6], [20, 10]]
    for n_max, d_max in tested_pairs:
        matrix = [[1 if n % d == 0 else 0 for n in range(1, n_max + 1)] for d in range(1, d_max + 1)]
        require(matrix_rank(matrix) == d_max, f"Divisibility matrix rank failed for {(n_max, d_max)}")

    n_max = 30
    weights = {n: ((-1) ** n) * (n + 3) for n in range(1, n_max + 1)}
    aggregates = {d: sum(weights[n] for n in range(d, n_max + 1, d)) for d in range(1, n_max + 1)}
    recovered = {
        n: sum(mobius(k) * aggregates[n * k] for k in range(1, n_max // n + 1))
        for n in range(1, n_max + 1)
    }
    require(recovered == weights, "Finite Möbius aggregate recovery failed")

    results = {
        "face_enumerator": {"status": "PASS", "integers_checked": 200, "z_values": [0, 1, 2, 3]},
        "margin_local_factors": {
            "status": "PASS",
            "r_values": [1, 2, 3, 4, 5],
            "first_residual_orders": residual_orders,
        },
        "twisted_local_identity": {"status": "PASS", "r_values": [1, 2, 3]},
        "sieve_rank_candidate": {"status": "KILLED_TRIVIAL", "tested_pairs": tested_pairs},
        "aggregate_recovery_candidate": {"status": "KILLED_KNOWN", "N": n_max},
        "preliminary_shortlist": ["OLS-CAND-001", "OLS-CAND-002", "OLS-CAND-005"],
    }
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    require(results == expected, "Candidate check results differ from committed expected result")
    GENERATED.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("original_lemma_candidate_checks: PASS — candidate identities and kill tests verified")


if __name__ == "__main__":
    main()
