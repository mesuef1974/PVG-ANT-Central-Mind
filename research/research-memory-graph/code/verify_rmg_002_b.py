#!/usr/bin/env python3
"""RMG-002-B finite Dirichlet-convolution algebra verifier (stdlib only)."""
from __future__ import annotations
import json, math
from pathlib import Path
from typing import Callable, Dict, List

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "dirichlet-convolution-algebra.jsonl"
RESULT = ROOT / "results" / "rmg_002_b_verification.json"
N = 300

Fn = Callable[[int], int | float]

def divisors(n: int) -> List[int]:
    return [d for d in range(1, n + 1) if n % d == 0]

def factor(n: int) -> Dict[int, int]:
    out: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1: out[n] = out.get(n, 0) + 1
    return out

def mobius(n: int) -> int:
    v = factor(n)
    return 0 if any(k > 1 for k in v.values()) else (-1) ** len(v)

def tau(n: int) -> int:
    z = 1
    for k in factor(n).values(): z *= k + 1
    return z

def phi(n: int) -> int:
    z = n
    for p in factor(n): z = z // p * (p - 1)
    return z

def von_mangoldt(n: int) -> float:
    v = factor(n)
    return math.log(next(iter(v))) if len(v) == 1 else 0.0

def conv(f: Fn, g: Fn, n: int) -> float:
    return sum(f(d) * g(n // d) for d in divisors(n))

def eps(n: int) -> int: return 1 if n == 1 else 0

def one(n: int) -> int: return 1

def ident(n: int) -> int: return n

def logf(n: int) -> float: return math.log(n)

def close(a: float, b: float, tol: float = 1e-11) -> bool:
    return abs(a-b) <= tol * max(1.0, abs(a), abs(b))

def run() -> dict:
    checks = []
    def record(cid: str, ok: bool, evidence: dict) -> None:
        checks.append({"check_id": cid, "status": "PASS" if ok else "FAIL", "evidence": evidence})

    samples = range(1, N + 1)
    record("CHK-DCA-IDENTITY-001", all(close(conv(eps, tau, n), tau(n)) and close(conv(tau, eps, n), tau(n)) for n in samples), {"range":[1,N],"function":"tau"})
    record("CHK-DCA-COMM-001", all(close(conv(mobius, one, n), conv(one, mobius, n)) for n in samples), {"range":[1,N],"functions":["mu","1"]})
    record("CHK-DCA-ASSOC-001", all(close(conv(lambda d: conv(one,mobius,d), tau, n), conv(one, lambda d: conv(mobius,tau,d), n)) for n in samples), {"range":[1,N],"functions":["1","mu","tau"]})
    record("CHK-DCA-DIST-001", all(close(conv(one, lambda k: mobius(k)+phi(k), n), conv(one,mobius,n)+conv(one,phi,n)) for n in samples), {"range":[1,N]})
    record("CHK-DCA-MOBIUS-001", all(close(conv(mobius, one, n), eps(n)) for n in samples), {"range":[1,N],"identity":"mu*1=epsilon"})
    record("CHK-DCA-TAU-001", all(close(conv(one, one, n), tau(n)) for n in samples), {"range":[1,N],"identity":"1*1=tau"})
    record("CHK-DCA-PHI-001", all(close(conv(phi, one, n), ident(n)) for n in samples), {"range":[1,N],"identity":"phi*1=id"})
    record("CHK-DCA-LAMBDA-001", all(close(conv(von_mangoldt, one, n), logf(n)) for n in samples), {"range":[1,N],"identity":"Lambda*1=log"})
    pairs = [(a,b) for a in range(1,61) for b in range(1,61) if math.gcd(a,b)==1]
    h = lambda n: conv(mobius, tau, n)
    record("CHK-DCA-MULT-PRES-001", all(close(h(a*b),h(a)*h(b)) for a,b in pairs), {"coprime_pairs":len(pairs),"functions":["mu","tau"]})
    record("CHK-DCA-COMPLETE-NOPRES-001", tau(4)==3 and tau(2)**2==4, {"counterexample":{"tau(4)":tau(4),"tau(2)^2":tau(2)**2}})

    records = [json.loads(line) for line in REGISTRY.read_text(encoding="utf-8").splitlines() if line.strip()]
    ids = [r["record_id"] for r in records]
    required = {"record_id","kind","statement","classification","translation_type","certificate_present","certificate_missing","scientific_ceiling"}
    record("CHK-DCA-SCHEMA-001", all(required <= set(r) for r in records), {"records":len(records),"required_fields":sorted(required)})
    record("CHK-DCA-UNIQUE-001", len(ids)==len(set(ids)), {"records":len(records)})
    record("CHK-DCA-NEGATIVE-RULE-001", any(r["kind"]=="negative_rule" and "does not preserve" in r["statement"] for r in records), {"required_negative_rule":"complete multiplicativity not preserved"})
    record("CHK-DCA-LEAN-CEILING-001", all("FORMAL_PROOF_CERTIFICATE" in r.get("certificate_missing",[]) or r["kind"]=="negative_rule" for r in records), {"l6_promotion":False})

    passed = sum(c["status"]=="PASS" for c in checks)
    return {"unit":"RMG-002-B","status":"PASS" if passed==len(checks) else "FAIL","summary":{"passed":passed,"total":len(checks)},"scientific_ceiling":"finite algebra regression and formalization candidates only; no new ANT theorem and no L6 promotion","checks":checks}

def main() -> int:
    result = run()
    text = json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)
    print(text)
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(text+"\n",encoding="utf-8")
    return 0 if result["status"]=="PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
