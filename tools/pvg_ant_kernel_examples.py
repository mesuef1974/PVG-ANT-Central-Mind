from __future__ import annotations

import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "maps" / "bridge-example-results.json"
EXPECTED = ROOT / "maps" / "bridge-example-expected.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def valuation(n: int) -> dict[int, int]:
    require(n >= 1, "valuation input must be positive")
    result: dict[int, int] = {}
    p = 2
    remaining = n
    while p * p <= remaining:
        while remaining % p == 0:
            result[p] = result.get(p, 0) + 1
            remaining //= p
        p += 1
    if remaining > 1:
        result[remaining] = result.get(remaining, 0) + 1
    return result


def add_vectors(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    primes = set(left) | set(right)
    return {p: left.get(p, 0) + right.get(p, 0) for p in primes if left.get(p, 0) + right.get(p, 0)}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    vector = valuation(n)
    if any(exponent > 1 for exponent in vector.values()):
        return 0
    return -1 if len(vector) % 2 else 1


def divisor_count(n: int) -> int:
    value = 1
    for exponent in valuation(n).values():
        value *= exponent + 1
    return value


def reduced_character(modulus: int, index: int, value: int) -> complex:
    require(modulus == 5, "finite example fixes modulus 5")
    if math.gcd(value, modulus) != 1:
        return 0j
    discrete_log = {1: 0, 2: 1, 4: 2, 3: 3}[value % modulus]
    return cmath.exp(2j * math.pi * index * discrete_log / 4)


def close_complex(left: complex, right: complex, tolerance: float = 1e-12) -> bool:
    return abs(left - right) <= tolerance


def main() -> None:
    require(EXPECTED.exists(), f"Missing expected certificate: {EXPECTED}")
    results: dict[str, dict[str, object]] = {}

    v12 = valuation(12)
    v18 = valuation(18)
    require(add_vectors(v12, v18) == valuation(216), "multiplicative linearization failed")
    require(valuation(math.gcd(12, 18)) == {2: 1, 3: 1}, "gcd/min example failed")
    require(valuation(math.lcm(12, 18)) == {2: 2, 3: 2}, "lcm/max example failed")
    results["EX-MULT-001"] = {"status": "PASS", "objects": [12, 18, 216]}

    ds = divisors(12)
    require(ds == [1, 2, 3, 4, 6, 12], "divisor box enumeration failed")
    require(len(ds) == divisor_count(12) == 6, "box cardinality failed")
    require(sum(1 for _ in ds) == divisor_count(12), "1*1=tau example failed")
    results["EX-BOX-001"] = {"status": "PASS", "n": 12, "divisors": ds}

    require(mobius(30) ** 2 == 1, "squarefree Euler coefficient failed")
    require(mobius(12) ** 2 == 0, "non-squarefree Euler coefficient failed")
    require(all(mobius(p) ** 2 == 1 for p in [2, 3, 5, 7]), "prime local coefficients failed")
    results["EX-EULER-001"] = {
        "status": "PASS",
        "formal_identity": "sum mu(n)^2 n^-s = product_p (1+p^-s)",
        "analytic_gate": "Re(s)>1 for absolute convergence",
    }

    x = 12
    tolerance = 1e-12
    for n in range(1, 20):
        log_weight = sum(exponent * math.log(p) for p, exponent in valuation(n).items())
        require(abs(log_weight - math.log(n)) <= tolerance, f"log weight failed at {n}")
        require((n <= x) == (log_weight <= math.log(x) + tolerance), f"half-space failed at {n}")
    results["EX-HALFSPACE-001"] = {
        "status": "PASS",
        "x": x,
        "warning": "coarse slabs do not encode additive order",
    }

    require(mobius(30) == -1, "Boolean support parity failed")
    require(mobius(12) == 0, "off-Boolean Möbius zero failed")
    results["EX-MOBIUS-001"] = {"status": "PASS", "mu30": -1, "mu12": 0}

    for target in [1, 2, 3, 4]:
        for value in [1, 2, 3, 4]:
            reconstructed = sum(
                reduced_character(5, k, value) * reduced_character(5, k, target).conjugate()
                for k in range(4)
            ) / 4
            expected_value = 1 + 0j if value == target else 0j
            require(close_complex(reconstructed, expected_value), f"character reconstruction failed for {value},{target}")
    results["EX-RESIDUE-001"] = {"status": "PASS", "modulus": 5, "characters": 4}

    universe = [1, 2, 3, 6]
    weights = {1: 1, 2: -1, 3: -1, 6: 1}
    aggregates = {d: sum(weights[n] for n in universe if n % d == 0) for d in [1, 2, 3, 6]}
    require(aggregates[1] == aggregates[2] == aggregates[3] == 0, "aggregate kernel example failed")
    require(aggregates[6] == 1, "lost divisibility moment was not detected")
    results["EX-SIEVE-LOSS-001"] = {"status": "PASS", "aggregates": aggregates}

    coefficients = {n: divisor_count(n) for n in range(1, 21)}
    require(all(coefficients[n] == sum(1 for d in range(1, n + 1) if n % d == 0) for n in coefficients), "zeta-square coefficient identity failed")
    results["EX-TRANSFER-001"] = {
        "status": "PASS",
        "finite_coefficients": coefficients,
        "warning": "summatory asymptotics require Perron/Tauberian/contour hypotheses",
    }

    require(len(results) == 8, "expected exactly eight bridge examples")
    normalized = json.loads(json.dumps(results))
    expected = json.loads(EXPECTED.read_text(encoding="utf-8"))
    require(normalized == expected, "generated bridge examples differ from committed expected certificate")
    OUTPUT.write_text(json.dumps(normalized, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("pvg_ant_kernel_examples: PASS — 8 deterministic examples match committed certificate")


if __name__ == "__main__":
    main()
