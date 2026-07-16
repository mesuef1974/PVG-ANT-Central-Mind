#!/usr/bin/env python3
import cmath
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "weyl-vdc-exponential-sum-minor-arc.jsonl"


def load_records():
    return [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]


def exp_sum(alpha: float, degree: int, nmax: int) -> complex:
    return sum(cmath.exp(2j * math.pi * alpha * (n ** degree)) for n in range(1, nmax + 1))


def correlation(alpha: float, degree: int, nmax: int, h: int) -> complex:
    return sum(
        cmath.exp(2j * math.pi * alpha * (((n + h) ** degree) - (n ** degree)))
        for n in range(1, nmax - h + 1)
    )


def vdc_rhs(alpha: float, degree: int, nmax: int, hmax: int) -> float:
    # Standard finite van der Corput upper-bound form, deliberately non-optimized.
    weighted = 0.0
    for h in range(1, hmax + 1):
        weighted += (1 - h / (hmax + 1)) * abs(correlation(alpha, degree, nmax, h))
    return math.sqrt(((nmax + hmax) / (hmax + 1)) * (nmax + 2 * weighted))


def main():
    records = load_records()
    checks = []
    checks.append(("registry_count", len(records) == 12, len(records)))
    ids = [r["record_id"] for r in records]
    checks.append(("unique_ids", len(ids) == len(set(ids)), len(set(ids))))

    alpha = math.sqrt(2)
    nmax = 300
    linear = exp_sum(alpha, 1, nmax)
    quadratic = exp_sum(alpha, 2, nmax)
    checks.append(("trivial_bound_linear", abs(linear) <= nmax + 1e-10, abs(linear)))
    checks.append(("trivial_bound_quadratic", abs(quadratic) <= nmax + 1e-10, abs(quadratic)))

    rhs = vdc_rhs(alpha, 2, nmax, 20)
    checks.append(("finite_vdc_bound", abs(quadratic) <= rhs + 1e-10, {"lhs": abs(quadratic), "rhs": rhs}))

    # First difference of a quadratic phase has affine dependence on n.
    n, h = 17, 5
    direct_diff = (n + h) ** 2 - n ** 2
    affine_diff = 2 * h * n + h * h
    checks.append(("quadratic_difference_identity", direct_diff == affine_diff, direct_diff))

    ratio = abs(quadratic) / nmax
    checks.append(("finite_cancellation_ratio", 0 <= ratio <= 1, ratio))

    rejection_count = sum(r["record_type"] == "CLAIM_REJECTION" for r in records)
    checks.append(("claim_rejections_present", rejection_count >= 3, rejection_count))
    checks.append(("no_l6_promotion", any(r["record_type"] == "FORMALIZATION_BOUNDARY" for r in records), True))

    passed = sum(ok for _, ok, _ in checks)
    result = {
        "unit": "RMG-005-C",
        "status": "PASS" if passed == len(checks) else "FAIL",
        "passed": passed,
        "total": len(checks),
        "parameters": {"alpha": alpha, "N": nmax, "H": 20},
        "checks": [{"name": n, "pass": ok, "detail": d} for n, ok, d in checks],
    }
    print(json.dumps(result, indent=2, default=str))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
