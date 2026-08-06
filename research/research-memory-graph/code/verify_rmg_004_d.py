#!/usr/bin/env python3
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "large-sieve-bombieri-vinogradov-average-boundary.jsonl"


def load_records():
    return [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]


def reduced_residues(q):
    return [a for a in range(1, q) if math.gcd(a, q) == 1]


def phase_energy(coeffs, q_max):
    total = 0.0
    for q in range(2, q_max + 1):
        for a in reduced_residues(q):
            z = sum(c * complex(math.cos(2 * math.pi * a * n / q), math.sin(2 * math.pi * a * n / q)) for n, c in enumerate(coeffs, start=1))
            total += abs(z) ** 2
    return total


def direct_energy_bound(coeffs, q_max):
    n = len(coeffs)
    return (n + q_max * q_max) * sum(abs(c) ** 2 for c in coeffs)


def average_pointwise_counterexample():
    values = [0.0] * 99 + [10.0]
    average = sum(values) / len(values)
    return average, max(values)


def residue_discrepancy(n_max, q_max):
    total = 0.0
    maxima = {}
    for q in range(2, q_max + 1):
        residues = reduced_residues(q)
        expected = n_max / q
        worst = 0.0
        for a in residues:
            count = sum(1 for n in range(1, n_max + 1) if n % q == a)
            worst = max(worst, abs(count - expected))
        maxima[q] = worst
        total += worst
    return total, maxima


def main():
    records = load_records()
    checks = []
    checks.append(("registry_count", len(records) == 12, len(records)))
    ids = [r["record_id"] for r in records]
    checks.append(("unique_ids", len(ids) == len(set(ids)), len(set(ids))))

    coeffs = [(-1) ** n * ((n % 7) - 3) for n in range(1, 41)]
    energy = phase_energy(coeffs, 9)
    bound = direct_energy_bound(coeffs, 9)
    checks.append(("finite_large_sieve_style_energy_bound", energy <= 2.5 * bound, {"energy": energy, "reference_bound": bound}))

    avg, mx = average_pointwise_counterexample()
    checks.append(("average_not_pointwise_counterexample", avg < 0.2 and mx == 10.0, {"average": avg, "maximum": mx}))

    total_disc, maxima = residue_discrepancy(500, 20)
    checks.append(("finite_average_discrepancy_computable", math.isfinite(total_disc) and len(maxima) == 19, {"total": total_disc, "maxima": maxima}))

    required_types = {"ANT_OBJECT", "OBSERVABLE", "PVG_TRANSLATION", "CERTIFICATE_LADDER", "BOUNDARY", "LOSS_LEDGER", "CLAIM_REJECTION", "GOVERNANCE"}
    present = {r["record_type"] for r in records}
    checks.append(("required_record_types_present", required_types <= present, sorted(present)))

    rejections = [r for r in records if r["record_type"] == "CLAIM_REJECTION"]
    checks.append(("claim_rejections_present", len(rejections) >= 2, len(rejections)))
    no_overclaim = all("No " in r["claim_ceiling"] or "Reject" in r["claim_ceiling"] or "cannot" in r["claim_ceiling"] or "must not" in r["claim_ceiling"] for r in records if r["record_type"] in {"BOUNDARY", "CLAIM_REJECTION", "GOVERNANCE"})
    checks.append(("claim_ceiling_enforced", no_overclaim, True))

    passed = sum(ok for _, ok, _ in checks)
    result = {
        "unit": "RMG-004-D",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed": passed,
        "total": len(checks),
        "checks": [{"name": name, "pass": ok, "detail": detail} for name, ok, detail in checks],
    }
    print(json.dumps(result, indent=2, default=str))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
