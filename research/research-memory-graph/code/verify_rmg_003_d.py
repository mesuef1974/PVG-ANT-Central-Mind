#!/usr/bin/env python3
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "dirichlet-l-zeros-explicit-formula-grh-boundary.jsonl"


def load_records():
    return [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]


def chi4(n: int) -> int:
    r = n % 4
    if r == 1:
        return 1
    if r == 3:
        return -1
    return 0


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


def log_derivative_series(s: complex, cutoff: int) -> complex:
    return sum(mangoldt(n) * chi4(n) / (n ** s) for n in range(1, cutoff + 1))


def prime_power_series(s: complex, prime_cutoff: int, power_cutoff: int) -> complex:
    total = 0j
    for p in range(2, prime_cutoff + 1):
        if mangoldt(p) == 0:
            continue
        value = chi4(p)
        if value == 0:
            continue
        pk = p
        k = 1
        while pk <= power_cutoff:
            total += math.log(p) * (value ** k) / (pk ** s)
            pk *= p
            k += 1
    return total


def psi_character(x: int) -> complex:
    return sum(mangoldt(n) * chi4(n) for n in range(1, x + 1))


def main():
    records = load_records()
    checks = []

    checks.append(("registry_count", len(records) == 12, len(records)))
    ids = [r["record_id"] for r in records]
    checks.append(("unique_ids", len(ids) == len(set(ids)), len(set(ids))))

    s = 2.0 + 0.4j
    direct = log_derivative_series(s, 12000)
    prime_power = prime_power_series(s, 97, 12000)
    gap = abs(direct - prime_power)
    checks.append(("log_derivative_prime_power_agreement", gap < 2e-4, gap))

    samples = {x: psi_character(x) for x in (100, 1000, 10000)}
    checks.append(("finite_character_observables_computable", all(math.isfinite(v.real) for v in samples.values()), samples))

    required_types = {"EXPLICIT_FORMULA_DEPENDENCY", "BOUNDARY", "CONDITIONAL_THEOREM", "LOSS_LEDGER", "CLAIM_REJECTION"}
    present_types = {r["record_type"] for r in records}
    checks.append(("dependency_and_boundary_types_present", required_types <= present_types, sorted(present_types)))

    rejections = [r for r in records if r["record_type"] == "CLAIM_REJECTION"]
    checks.append(("claim_rejections_present", len(rejections) >= 2, len(rejections)))

    grh_records = [r for r in records if "GRH" in r["name"] or "GRH" in r["statement"]]
    no_promotion = all("no GRH progress" in r["claim_ceiling"] or "Reject GRH" in r["claim_ceiling"] for r in grh_records)
    checks.append(("no_grh_promotion", no_promotion, len(grh_records)))

    passed = sum(ok for _, ok, _ in checks)
    result = {
        "unit": "RMG-003-D",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed": passed,
        "total": len(checks),
        "checks": [{"name": name, "pass": ok, "detail": detail} for name, ok, detail in checks],
    }
    print(json.dumps(result, indent=2, default=str))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
