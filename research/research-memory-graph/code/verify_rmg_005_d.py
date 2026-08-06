#!/usr/bin/env python3
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "prime-weighted-exponential-vaughan-major-minor.jsonl"


def load_records():
    return [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]


def mobius(n: int) -> int:
    if n == 1:
        return 1
    count = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            n //= p
            count += 1
            if n % p == 0:
                return 0
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        count += 1
    return -1 if count % 2 else 1


def mangoldt(n: int) -> float:
    if n < 2:
        return 0.0
    for p in range(2, int(math.isqrt(n)) + 2):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return math.log(p) if m == 1 else 0.0
    return math.log(n)


def divisor_log_identity(n: int) -> float:
    return sum(mobius(d) * math.log(n // d) for d in range(1, n + 1) if n % d == 0)


def exp_sum(alpha: float, cutoff: int) -> complex:
    return sum(mangoldt(n) * cmath.exp(2j * math.pi * alpha * n) for n in range(1, cutoff + 1))


def factor_pairs(cutoff: int):
    return [(m, n) for m in range(1, cutoff + 1) for n in range(1, cutoff // m + 1)]


def main():
    records = load_records()
    checks = []
    checks.append(("registry_count", len(records) == 12, len(records)))
    ids = [r["record_id"] for r in records]
    checks.append(("unique_ids", len(ids) == len(set(ids)), len(set(ids))))

    max_gap = max(abs(mangoldt(n) - divisor_log_identity(n)) for n in range(1, 301))
    checks.append(("finite_vaughan_source_identity", max_gap < 1e-12, max_gap))

    pairs = factor_pairs(80)
    checks.append(("factor_pair_domain_nonempty", len(pairs) > 0, len(pairs)))

    alpha_samples = [math.sqrt(2) % 1, math.sqrt(3) % 1, 0.271828]
    values = [abs(exp_sum(a, 500)) for a in alpha_samples]
    trivial = sum(mangoldt(n) for n in range(1, 501))
    checks.append(("finite_prime_weighted_sums_computable", all(math.isfinite(v) for v in values), values))
    checks.append(("finite_values_below_trivial_bound", all(v <= trivial + 1e-9 for v in values), {"values": values, "trivial": trivial}))

    required = {"DECOMPOSITION", "CERTIFICATE", "TRANSFER", "BOUNDARY", "CLAIM_REJECTION"}
    present = {r["record_type"] for r in records}
    checks.append(("certificate_layers_present", required <= present, sorted(present)))

    rejections = [r for r in records if r["record_type"] == "CLAIM_REJECTION"]
    checks.append(("claim_rejections_present", len(rejections) == 3, len(rejections)))

    result = {
        "unit": "RMG-005-D",
        "status": "PASS" if all(ok for _, ok, _ in checks) else "FAIL",
        "passed": sum(ok for _, ok, _ in checks),
        "total": len(checks),
        "checks": [{"name": n, "pass": ok, "detail": d} for n, ok, d in checks],
    }
    print(json.dumps(result, indent=2, default=str))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
