#!/usr/bin/env python3
import cmath, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "circle-method-major-minor-singular-series.jsonl"


def load_records():
    return [json.loads(x) for x in REGISTRY.read_text(encoding="utf-8").splitlines() if x.strip()]


def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0: return False
        p += 2
    return True


def direct_binary(N):
    return sum(1 for x in range(2, N) if is_prime(x) and is_prime(N-x))


def fourier_binary(N, q=4096):
    vals = []
    for j in range(q):
        a = j / q
        s = sum(cmath.exp(2j*math.pi*a*n) for n in range(2, N) if is_prime(n))
        vals.append(s*s*cmath.exp(-2j*math.pi*a*N))
    return sum(vals)/q


def main():
    records = load_records(); checks=[]
    checks.append(("registry_count", len(records)==12, len(records)))
    ids=[r["record_id"] for r in records]
    checks.append(("unique_ids", len(ids)==len(set(ids)), len(set(ids))))
    samples={N:(direct_binary(N), fourier_binary(N)) for N in (20,30,50,100)}
    gap=max(abs(a-b.real) for a,b in samples.values())
    imag=max(abs(b.imag) for _,b in samples.values())
    checks.append(("binary_fourier_identity", gap < 1e-9 and imag < 1e-9, {"max_real_gap":gap,"max_imag":imag}))
    local_ok=all(direct_binary(N)>0 for N in (20,30,50,100))
    checks.append(("finite_positive_examples", local_ok, {N:direct_binary(N) for N in (20,30,50,100)}))
    ladder=[r for r in records if r["record_type"]=="CERTIFICATE_LADDER"]
    checks.append(("certificate_ladder_present", len(ladder)==1, len(ladder)))
    rejects=[r for r in records if r["record_type"]=="CLAIM_REJECTION"]
    checks.append(("claim_rejections_present", len(rejects)>=2, len(rejects)))
    no_goldbach=all("Goldbach" in r["claim_ceiling"] or "prime-producing" in r["claim_ceiling"] for r in rejects)
    checks.append(("no_goldbach_promotion", no_goldbach, len(rejects)))
    types={r["record_type"] for r in records}
    needed={"IDENTITY","DECOMPOSITION","DEPENDENCY","OBJECT","CERTIFICATE_LADDER","CLAIM_REJECTION","PROVENANCE"}
    checks.append(("required_types_present", needed <= types, sorted(types)))
    passed=sum(ok for _,ok,_ in checks)
    result={"unit":"RMG-005-B","status":"PASS" if passed==len(checks) else "FAIL","passed":passed,"total":len(checks),"checks":[{"name":n,"pass":ok,"detail":d} for n,ok,d in checks]}
    print(json.dumps(result,indent=2,default=str))
    raise SystemExit(0 if result["status"]=="PASS" else 1)

if __name__ == "__main__": main()
