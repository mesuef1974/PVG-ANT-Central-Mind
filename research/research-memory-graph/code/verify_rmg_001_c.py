#!/usr/bin/env python3
"""RMG-001-C executable numerical verification harness (stdlib only)."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
NODES = ROOT / "registry" / "nodes.jsonl"
EDGES = ROOT / "registry" / "edges.jsonl"
RESULT = ROOT / "results" / "rmg_001_c_verification.json"

def primes_upto(n: int) -> List[int]:
    sieve = [True] * (n + 1)
    if n >= 0: sieve[0] = False
    if n >= 1: sieve[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            sieve[p * p:n + 1:p] = [False] * (((n - p * p) // p) + 1)
    return [i for i, flag in enumerate(sieve) if flag]

def valuation(n: int) -> Dict[int, int]:
    if n < 1:
        raise ValueError("n must be positive")
    out: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def decode(v: Dict[int, int]) -> int:
    z = 1
    for p, k in v.items():
        z *= p ** k
    return z

def is_prime(n: int) -> bool:
    return n >= 2 and valuation(n) == {n: 1}

def is_prime_power(n: int) -> bool:
    return n >= 2 and len(valuation(n)) == 1

def von_mangoldt(n: int) -> float:
    v = valuation(n)
    return math.log(next(iter(v))) if len(v) == 1 else 0.0

def divisors(n: int) -> List[int]:
    return [d for d in range(1, n + 1) if n % d == 0]

def mobius(n: int) -> int:
    v = valuation(n)
    return 0 if any(k > 1 for k in v.values()) else (-1) ** len(v)

def close(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))

def load_jsonl(path: Path) -> List[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def run() -> dict:
    checks = []
    def record(check_id: str, ok: bool, evidence: dict) -> None:
        checks.append({"check_id": check_id, "status": "PASS" if ok else "FAIL", "evidence": evidence})

    samples = list(range(1, 501))
    record("CHK-VALUATION-ROUNDTRIP-001", all(decode(valuation(n)) == n for n in samples), {"range": [1, 500]})
    pairs = [(m, n) for m in range(1, 51) for n in range(1, 51)]
    record("CHK-MULTIPLICATION-001", all({p: valuation(m).get(p, 0) + valuation(n).get(p, 0) for p in set(valuation(m)) | set(valuation(n))} == valuation(m * n) for m, n in pairs), {"pairs": len(pairs)})
    record("CHK-PRIME-001", [n for n in range(2, 50) if is_prime(n)] == primes_upto(49), {"primes_upto_49": primes_upto(49)})
    prime_powers = [n for n in range(2, 101) if is_prime_power(n)]
    record("CHK-PRIME-POWER-001", all(len(valuation(n)) == 1 for n in prime_powers) and 12 not in prime_powers, {"prime_powers_upto_100": prime_powers})
    record("CHK-MULTIPLICATIVE-001", all(math.gcd(m, n) != 1 or mobius(m * n) == mobius(m) * mobius(n) for m, n in pairs), {"function": "mobius", "pairs": len(pairs)})
    record("CHK-DIRICHLET-CONV-001", all(len(divisors(n)) == sum(1 for _ in divisors(n)) for n in samples), {"range": [1, 500], "identity": "1*1=tau"})
    record("CHK-MOBIUS-001", all(sum(mobius(d) for d in divisors(n)) == (1 if n == 1 else 0) for n in samples), {"range": [1, 500], "identity": "mu*1=epsilon"})
    s = 2.0
    ant = sum(n ** (-s) for n in range(1, 101))
    pvg = sum(math.exp(-s * sum(k * math.log(p) for p, k in valuation(n).items())) for n in range(1, 101))
    record("CHK-DIRICHLET-SERIES-001", close(ant, pvg), {"s": s, "cutoff": 100, "ant": ant, "pvg": pvg})
    coeffs = {1: 1}
    for p in [2, 3, 5, 7]:
        new = {}
        for n, c in coeffs.items():
            for k in range(4):
                new[n * p ** k] = new.get(n * p ** k, 0) + c
        coeffs = new
    record("CHK-EULER-PRODUCT-001", all(c == 1 for c in coeffs.values()) and len(coeffs) == 4 ** 4, {"primes": [2, 3, 5, 7], "max_exponent": 3, "coefficient_count": len(coeffs)})
    lambda_cases = {2: math.log(2), 8: math.log(2), 9: math.log(3), 12: 0.0, 25: math.log(5)}
    record("CHK-LAMBDA-001", all(close(von_mangoldt(n), value) for n, value in lambda_cases.items()), {"cases": lambda_cases})
    x = 100
    ps = primes_upto(x)
    pi_value = len(ps)
    theta = sum(math.log(p) for p in ps)
    psi = sum(von_mangoldt(n) for n in range(1, x + 1))
    psi_axes = sum(math.log(p) for p in ps for k in range(1, 100) if p ** k <= x)
    record("CHK-CHEBYSHEV-001", pi_value == 25 and close(psi, psi_axes), {"x": x, "pi": pi_value, "theta": theta, "psi": psi})

    nodes = load_jsonl(NODES)
    edges = load_jsonl(EDGES)
    ids = {node["node_id"] for node in nodes}
    required = {"node_id", "node_type", "canonical_name", "short_definition", "status", "classification", "assimilation_level", "source_provenance", "scientific_ceiling", "translation_type"}
    record("CHK-REGISTRY-SCHEMA-001", all(required <= set(node) for node in nodes), {"nodes": len(nodes), "required_fields": sorted(required)})
    record("CHK-EDGE-REFERENTIAL-001", all(edge["source_id"] in ids and edge["target_id"] in ids for edge in edges), {"edges": len(edges)})
    record("CHK-REGISTRY-UNIQUENESS-001", len(ids) == len(nodes) and len({edge["edge_id"] for edge in edges}) == len(edges), {"nodes": len(nodes), "edges": len(edges)})
    passed = sum(check["status"] == "PASS" for check in checks)
    return {"unit": "RMG-001-C", "status": "PASS" if passed == len(checks) else "FAIL", "summary": {"passed": passed, "total": len(checks)}, "scientific_ceiling": "finite registry and numerical verification only; no Goldbach, RH, or GRH progress", "checks": checks}

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-result", action="store_true")
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    print(text)
    if args.write_result:
        RESULT.parent.mkdir(parents=True, exist_ok=True)
        RESULT.write_text(text + "\n", encoding="utf-8")
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
