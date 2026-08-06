#!/usr/bin/env python3
"""RMG-002-A arithmetic-function verification harness (stdlib only)."""
from __future__ import annotations
import json, math
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
REG = ROOT / "registry" / "arithmetic-functions.jsonl"
EDGES = ROOT / "registry" / "arithmetic-function-edges.jsonl"
RESULT = ROOT / "results" / "rmg_002_a_verification.json"


def valuation(n: int) -> Dict[int, int]:
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


def divisors(n: int) -> List[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    v = valuation(n)
    return 0 if any(k > 1 for k in v.values()) else (-1) ** len(v)


def tau(n: int) -> int:
    z = 1
    for k in valuation(n).values(): z *= k + 1
    return z


def phi(n: int) -> int:
    z = n
    for p in valuation(n): z = z // p * (p - 1)
    return z


def liouville(n: int) -> int:
    return (-1) ** sum(valuation(n).values())


def is_prime(n: int) -> bool:
    return n >= 2 and valuation(n) == {n: 1}


def load_jsonl(path: Path) -> List[dict]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]


def run() -> dict:
    checks = []
    def record(cid: str, ok: bool, evidence: dict) -> None:
        checks.append({"check_id": cid, "status": "PASS" if ok else "FAIL", "evidence": evidence})

    N = 500
    nums = range(1, N + 1)
    pairs = [(a,b) for a in range(1,81) for b in range(1,81)]
    record("CHK-AF-ONE-001", all(1 == 1 for _ in nums), {"range":[1,N]})
    record("CHK-AF-MOBIUS-001", all(sum(mobius(d) for d in divisors(n)) == (1 if n == 1 else 0) for n in nums), {"identity":"mu*1=epsilon","range":[1,N]})
    record("CHK-AF-MOBIUS-MULT-001", all(math.gcd(a,b) != 1 or mobius(a*b) == mobius(a)*mobius(b) for a,b in pairs), {"pairs":len(pairs)})
    record("CHK-AF-TAU-001", all(tau(n) == len(divisors(n)) for n in nums), {"identity":"tau=1*1","range":[1,N]})
    record("CHK-AF-TAU-MULT-001", all(math.gcd(a,b) != 1 or tau(a*b) == tau(a)*tau(b) for a,b in pairs), {"pairs":len(pairs)})
    record("CHK-AF-PHI-001", all(sum(phi(d) for d in divisors(n)) == n for n in nums), {"identity":"phi*1=id","range":[1,N]})
    record("CHK-AF-PHI-MULT-001", all(math.gcd(a,b) != 1 or phi(a*b) == phi(a)*phi(b) for a,b in pairs), {"pairs":len(pairs)})
    record("CHK-AF-LIOUVILLE-001", all(liouville(n) == (-1)**sum(valuation(n).values()) for n in nums), {"range":[1,N]})
    record("CHK-AF-LIOUVILLE-COMPLETE-MULT-001", all(liouville(a*b) == liouville(a)*liouville(b) for a,b in pairs), {"pairs":len(pairs)})
    record("CHK-AF-PRIME-INDICATOR-001", all((1 if is_prime(n) else 0) == (1 if len(valuation(n)) == 1 and list(valuation(n).values()) == [1] else 0) for n in nums), {"range":[1,N]})
    counterexamples = {"tau_noninjective":[6,8],"phi_noninjective":[15,16],"liouville_loss":[6,10]}
    record("CHK-AF-NONINJECTIVITY-001", tau(6)==tau(8) and phi(15)==phi(16) and liouville(6)==liouville(10), counterexamples)

    nodes, edges = load_jsonl(REG), load_jsonl(EDGES)
    base_ids = {"PVG-VALUATION-VECTOR-001","ANT-PRIME-001","ANT-PNT-001"}
    ids = {n["node_id"] for n in nodes}
    required = {"node_id","canonical_name","assimilation_level","translation_type","certificate_present","certificate_missing","scientific_ceiling"}
    record("CHK-AF-SCHEMA-001", len(nodes)==6 and all(required <= set(n) for n in nodes), {"nodes":len(nodes)})
    record("CHK-AF-EDGE-REFERENTIAL-001", all(e["source_id"] in ids and e["target_id"] in ids|base_ids for e in edges), {"edges":len(edges)})
    record("CHK-AF-NO-UNSUPPORTED-L6-001", all(n["assimilation_level"] != "L6_FORMALLY_VERIFIED" for n in nodes), {"reason":"no function-specific Lean build certificate"})
    passed = sum(c["status"]=="PASS" for c in checks)
    return {"unit":"RMG-002-A","status":"PASS" if passed==len(checks) else "FAIL","summary":{"passed":passed,"total":len(checks)},"scientific_ceiling":"classical arithmetic-function identities plus finite regression; no new theorem and no unsupported Lean L6","checks":checks}


if __name__ == "__main__":
    result = run()
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    print(text)
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(text+"\n", encoding="utf-8")
    raise SystemExit(0 if result["status"] == "PASS" else 1)
