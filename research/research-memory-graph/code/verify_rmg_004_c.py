#!/usr/bin/env python3
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "type-i-type-ii-bilinear-level-distribution.jsonl"


def load_records():
    return [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]


def valuation(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def addv(a, b):
    out = dict(a)
    for p, e in b.items():
        out[p] = out.get(p, 0) + e
    return out


def main():
    records = load_records()
    checks = []
    ids = [r["record_id"] for r in records]
    checks.append(("registry_count", len(records) == 12, len(records)))
    checks.append(("unique_ids", len(ids) == len(set(ids)), len(set(ids))))

    # Exact finite bilinear bookkeeping.
    alpha = {m: (-1) ** m * (m % 5 + 1) for m in range(1, 31)}
    beta = {n: (n % 7) - 3 for n in range(1, 41)}
    direct = sum(alpha[m] * beta[n] for m in alpha for n in beta if m * n <= 300)
    by_product = 0
    for k in range(1, 301):
        by_product += sum(alpha[m] * beta[k // m] for m in alpha if k % m == 0 and k // m in beta)
    checks.append(("finite_bilinear_identity", direct == by_product, {"direct": direct, "by_product": by_product}))

    # PVG factor splitting nu(mn)=nu(m)+nu(n).
    split_ok = all(addv(valuation(m), valuation(n)) == valuation(m * n) for m in range(1, 51) for n in range(1, 51))
    checks.append(("valuation_factor_split", split_ok, "2500 pairs"))

    # Finite residue discrepancy for a toy sequence; diagnostic only.
    N, Q = 2000, 25
    seq = [1 if math.gcd(n, 30) == 1 else 0 for n in range(1, N + 1)]
    discrepancies = {}
    for q in range(2, Q + 1):
        counts = [0] * q
        for n, a in enumerate(seq, start=1):
            if a:
                counts[n % q] += 1
        mean = sum(counts) / q
        discrepancies[q] = sum(abs(c - mean) for c in counts)
    finite_norm = sum(discrepancies.values())
    checks.append(("finite_distribution_norm_computable", math.isfinite(finite_norm) and finite_norm > 0, finite_norm))

    required = {"OBJECT", "IDENTITY", "CERTIFICATE", "DEPENDENCY", "INTEGRATION_LINK", "LOSS_LEDGER", "CLAIM_REJECTION", "BOUNDARY"}
    types = {r["record_type"] for r in records}
    checks.append(("required_record_types", required <= types, sorted(types)))
    checks.append(("claim_rejections", sum(r["record_type"] == "CLAIM_REJECTION" for r in records) >= 2, None))
    checks.append(("no_parity_claim", all("parity-barrier progress" in r.get("claim_ceiling", "") or r["record_type"] != "BOUNDARY" for r in records), None))

    passed = sum(ok for _, ok, _ in checks)
    result = {
        "unit": "RMG-004-C",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed": passed,
        "total": len(checks),
        "checks": [{"name": n, "pass": ok, "detail": d} for n, ok, d in checks],
    }
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
