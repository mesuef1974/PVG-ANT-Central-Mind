#!/usr/bin/env python3
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "sieve-objects-levels-certificates.jsonl"


def load_records():
    return [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]


def primes_upto(n):
    out = []
    for x in range(2, n + 1):
        if all(x % p for p in range(2, int(math.isqrt(x)) + 1)):
            out.append(x)
    return out


def truncated_profile(n, D):
    return tuple((p, min(_vp(n, p), int(math.log(D, p)))) for p in primes_upto(D))


def _vp(n, p):
    k = 0
    while n % p == 0 and n:
        n //= p
        k += 1
    return k


def indicators(n, D):
    return tuple(d for d in range(1, D + 1) if n % d == 0)


def aggregate(weights, support, d):
    return sum(w for n, w in zip(support, weights) if n % d == 0)


def sifted_direct(A, z):
    ps = primes_upto(z - 1)
    return [n for n in A if all(n % p for p in ps)]


def sifted_pvg(A, z):
    ps = primes_upto(z - 1)
    return [n for n in A if all(_vp(n, p) == 0 for p in ps)]


def main():
    records = load_records()
    checks = []
    checks.append(("registry_count", len(records) == 12, len(records)))
    ids = [r["record_id"] for r in records]
    checks.append(("unique_ids", len(ids) == len(set(ids)), len(set(ids))))

    D = 12
    exact = True
    for n in range(1, 301):
        prof = truncated_profile(n, D)
        reconstructed = tuple(d for d in range(1, D + 1) if all(_vp(d, p) <= dict(prof).get(p, 0) for p in primes_upto(D)))
        if reconstructed != indicators(n, D):
            exact = False
            break
    checks.append(("truncated_profile_indicator_equivalence", exact, {"D": D, "n_max": 300}))

    support = [1, 2, 3, 6]
    weights = [1, -1, -1, 1]
    low = {d: aggregate(weights, support, d) for d in (1, 2, 3)}
    hidden = aggregate(weights, support, 6)
    checks.append(("aggregation_kernel_counterexample", all(v == 0 for v in low.values()) and hidden == 1, {"low": low, "d6": hidden}))

    A = list(range(1, 501))
    checks.append(("sifted_set_pvg_equivalence", sifted_direct(A, 11) == sifted_pvg(A, 11), len(sifted_direct(A, 11))))

    types = {r["record_type"] for r in records}
    required = {"OBJECT", "TRANSLATION", "LOSS_LEDGER", "CERTIFICATE", "SEPARATION_RULE", "BOUNDARY", "CLAIM_REJECTION"}
    checks.append(("certificate_types_present", required <= types, sorted(types)))

    separations = [r for r in records if r["record_type"] == "SEPARATION_RULE"]
    checks.append(("certificate_separation_present", len(separations) >= 2, len(separations)))

    rejections = [r for r in records if r["record_type"] == "CLAIM_REJECTION"]
    checks.append(("parity_and_prime_rejections", len(rejections) >= 2 and any("parity" in r["name"].lower() for r in rejections), [r["name"] for r in rejections]))

    passed = sum(ok for _, ok, _ in checks)
    result = {"unit": "RMG-004-A", "status": "PASS" if passed == len(checks) else "FAIL", "passed": passed, "total": len(checks), "checks": [{"name": n, "pass": ok, "detail": detail} for n, ok, detail in checks]}
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
