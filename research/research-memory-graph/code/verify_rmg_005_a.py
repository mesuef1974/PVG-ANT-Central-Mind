#!/usr/bin/env python3
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "additive-characters-exponential-sums-fourier-cancellation.jsonl"


def load_records():
    return [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]


def e_q(a: int, n: int, q: int) -> complex:
    return cmath.exp(2j * math.pi * a * n / q)


def dft(values):
    q = len(values)
    return [sum(values[r] * e_q(-a, r, q) for r in range(q)) for a in range(q)]


def idft(values_hat):
    q = len(values_hat)
    return [sum(values_hat[a] * e_q(a, r, q) for a in range(q)) / q for r in range(q)]


def factor_vector(n: int):
    result = []
    p = 2
    while p * p <= n:
        v = 0
        while n % p == 0:
            n //= p
            v += 1
        if v:
            result.append((p, v))
        p += 1
    if n > 1:
        result.append((n, 1))
    return result


def decode(vector):
    n = 1
    for p, v in vector:
        n *= p ** v
    return n


def main():
    records = load_records()
    checks = []
    checks.append(("registry_count", len(records) == 12, len(records)))
    ids = [r["record_id"] for r in records]
    checks.append(("unique_ids", len(ids) == len(set(ids)), len(set(ids))))

    q = 7
    orth_gap = 0.0
    for n in range(q):
        for m in range(q):
            value = sum(e_q(a, n - m, q) for a in range(q))
            expected = q if n == m else 0
            orth_gap = max(orth_gap, abs(value - expected))
    checks.append(("additive_orthogonality", orth_gap < 1e-10, orth_gap))

    values = [3, -1, 2, 0, 4, -2, 1]
    transformed = dft(values)
    recovered = idft(transformed)
    inversion_gap = max(abs(recovered[i] - values[i]) for i in range(q))
    checks.append(("fourier_inversion", inversion_gap < 1e-10, inversion_gap))

    lhs = sum(abs(z) ** 2 for z in transformed)
    rhs = q * sum(abs(x) ** 2 for x in values)
    checks.append(("parseval", abs(lhs - rhs) < 1e-9, {"lhs": lhs, "rhs": rhs}))

    projector_gap = 0.0
    for x in range(q):
        for y in range(q):
            for N in range(q):
                value = sum(e_q(a, x + y - N, q) for a in range(q)) / q
                expected = 1 if (x + y - N) % q == 0 else 0
                projector_gap = max(projector_gap, abs(value - expected))
    checks.append(("addition_fiber_projector", projector_gap < 1e-10, projector_gap))

    reindex_gap = 0.0
    alpha = 3 / 11
    for n in range(1, 301):
        direct = cmath.exp(2j * math.pi * alpha * n)
        pvg = cmath.exp(2j * math.pi * alpha * decode(factor_vector(n)))
        reindex_gap = max(reindex_gap, abs(direct - pvg))
    checks.append(("pvg_additive_phase_reindexing", reindex_gap < 1e-12, reindex_gap))

    trivial = sum(abs((-1) ** n) for n in range(1, 101))
    complete = abs(sum(e_q(1, n, 10) for n in range(10)))
    checks.append(("cancellation_certificate_distinction", complete < 1e-10 and trivial == 100, {"complete_period_sum": complete, "trivial_l1_bound": trivial}))

    rejections = [r for r in records if r["record_type"] == "CLAIM_REJECTION"]
    checks.append(("claim_rejections_present", len(rejections) >= 2, len(rejections)))

    passed = sum(ok for _, ok, _ in checks)
    result = {
        "unit": "RMG-005-A",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed": passed,
        "total": len(checks),
        "checks": [{"name": name, "pass": ok, "detail": detail} for name, ok, detail in checks],
    }
    print(json.dumps(result, indent=2, default=str))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
