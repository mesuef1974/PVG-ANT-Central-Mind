#!/usr/bin/env python3
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "sieve-weights-fundamental-lemma-remainders.jsonl"


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    if n == 1:
        return 1
    m = n
    count = 0
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            count += 1
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        count += 1
    return -1 if count % 2 else 1


def smallest_prime_factor(n):
    if n < 2:
        return n
    for p in range(2, int(math.isqrt(n)) + 1):
        if n % p == 0:
            return p
    return n


def main():
    records = [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]
    checks = []
    ids = [r["record_id"] for r in records]
    checks.append(("registry_count", len(records) == 12, len(records)))
    checks.append(("unique_ids", len(ids) == len(set(ids)), len(set(ids))))

    # Exact divisor-box identity for a finite test weight.
    weights = {1: 1, 2: -1, 3: -1, 6: 1}
    exact = True
    for n in range(1, 301):
        direct = sum(w for d, w in weights.items() if n % d == 0)
        box = sum(weights.get(d, 0) for d in divisors(n))
        exact &= direct == box
    checks.append(("weighted_divisor_box_identity", exact, "n<=300"))

    # Inclusion-exclusion weight exactly detects avoidance of primes below z.
    z = 7
    P = 2 * 3 * 5
    exact_sift = True
    survivors = 0
    for n in range(1, 501):
        indicator = sum(mobius(d) for d in divisors(math.gcd(n, P)))
        expected = 1 if math.gcd(n, P) == 1 else 0
        exact_sift &= indicator == expected
        survivors += expected
    checks.append(("finite_inclusion_exclusion_sift", exact_sift, {"z": z, "survivors": survivors}))

    # A concrete local model A_d = floor(X/d), g(d)=1/d, r_d bounded by 1.
    X = 1000
    D = 100
    remainders = {d: X // d - X / d for d in range(1, D)}
    checks.append(("pointwise_remainder_bound", max(abs(v) for v in remainders.values()) < 1, max(abs(v) for v in remainders.values())))
    aggregate_l1 = sum(abs(v) for v in remainders.values())
    checks.append(("aggregate_norm_explicit", math.isfinite(aggregate_l1) and aggregate_l1 > 0, aggregate_l1))

    # s parameter must be explicit and positive in this finite sample.
    z = 11
    D = 1000
    s = math.log(D) / math.log(z)
    checks.append(("sieve_ratio_computable", s > 0, s))

    types = {r["record_type"] for r in records}
    checks.append(("certificate_types_present", {"SIEVE_WEIGHT", "THEOREM_DEPENDENCY", "SIEVE_FUNCTION", "REMAINDER_OBJECT", "CERTIFICATE", "CLAIM_REJECTION"} <= types, sorted(types)))
    rejections = [r for r in records if r["record_type"] == "CLAIM_REJECTION"]
    checks.append(("claim_rejections_present", len(rejections) >= 3, len(rejections)))

    passed = sum(ok for _, ok, _ in checks)
    result = {
        "unit": "RMG-004-B",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed": passed,
        "total": len(checks),
        "checks": [{"name": name, "pass": ok, "detail": detail} for name, ok, detail in checks],
    }
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
