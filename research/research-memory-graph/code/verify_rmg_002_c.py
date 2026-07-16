#!/usr/bin/env python3
"""RMG-002-C convergence-certificate and Euler-product verifier (stdlib only)."""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "dirichlet-series-euler-product-dependencies.jsonl"
RESULT = ROOT / "results" / "rmg_002_c_verification.json"

def primes_upto(n):
    sieve=[True]*(n+1)
    if n>=0: sieve[0]=False
    if n>=1: sieve[1]=False
    for p in range(2,int(n**0.5)+1):
        if sieve[p]: sieve[p*p:n+1:p]=[False]*(((n-p*p)//p)+1)
    return [i for i,v in enumerate(sieve) if v]

def mobius(n):
    count=0; d=2
    while d*d<=n:
        if n%d==0:
            n//=d; count+=1
            if n%d==0: return 0
            while n%d==0: n//=d
        d+=1
    if n>1: count+=1
    return -1 if count%2 else 1

def close(a,b,tol=1e-10): return abs(a-b)<=tol*max(1.0,abs(a),abs(b))

def run():
    checks=[]
    def rec(cid,ok,evidence): checks.append({"check_id":cid,"status":"PASS" if ok else "FAIL","evidence":evidence})
    records=[json.loads(x) for x in REGISTRY.read_text(encoding="utf-8").splitlines() if x.strip()]
    ids=[r["record_id"] for r in records]
    rec("CHK-REGISTRY-SCHEMA-002C", all("kind" in r and "record_id" in r for r in records), {"records":len(records)})
    rec("CHK-REGISTRY-UNIQUE-002C", len(ids)==len(set(ids)), {"records":len(ids)})
    ps=[2,3,5,7]
    coeff={1:1}
    for p in ps:
        nxt={}
        for n,c in coeff.items():
            for k in range(5): nxt[n*p**k]=nxt.get(n*p**k,0)+c
        coeff=nxt
    rec("CHK-TRUNCATED-ZETA-COEFFICIENTS-002C", len(coeff)==5**4 and all(c==1 for c in coeff.values()), {"coefficient_count":len(coeff)})
    coeff_mu={1:1}
    for p in ps:
        nxt={}
        for n,c in coeff_mu.items():
            nxt[n]=nxt.get(n,0)+c; nxt[n*p]=nxt.get(n*p,0)-c
        coeff_mu=nxt
    rec("CHK-TRUNCATED-MOBIUS-COEFFICIENTS-002C", all(coeff_mu[n]==mobius(n) for n in coeff_mu), {"coefficient_count":len(coeff_mu)})
    for s,cid in [(2.0,"CHK-ZETA-S2-APPROX-002C"),(1.5,"CHK-ZETA-S15-APPROX-002C")]:
        partial=sum(n**(-s) for n in range(1,20001)); product=1.0
        for p in primes_upto(2000): product*=1.0/(1.0-p**(-s))
        rec(cid, abs(partial-product)<0.01, {"s":s,"partial_sum":partial,"prime_product":product,"difference":abs(partial-product)})
    h1=sum(1/n for n in range(1,1001)); h2=sum(1/n for n in range(1,10001))
    rec("CHK-ZETA-S1-DIVERGENCE-DIAGNOSTIC-002C", h2>h1 and h2-h1>2.0, {"H1000":h1,"H10000":h2})
    def valuation(n):
        out={}; d=2; m=n
        while d*d<=m:
            while m%d==0: out[d]=out.get(d,0)+1; m//=d
            d+=1
        if m>1: out[m]=out.get(m,0)+1
        return out
    s=2.25
    ant=sum(((-1)**(n%2))*n**(-s) for n in range(1,501))
    pvg=sum(((-1)**(n%2))*math.exp(-s*sum(k*math.log(p) for p,k in valuation(n).items())) for n in range(1,501))
    rec("CHK-PVG-LOG-HEIGHT-REINDEXING-002C", close(ant,pvg), {"ant":ant,"pvg":pvg})
    anti=[r for r in records if r["kind"]=="anti_collapse"]
    rec("CHK-ANTI-COLLAPSE-COVERAGE-002C", len(anti)>=2 and all("rejection_reason" in r for r in anti), {"anti_collapse_records":len(anti)})
    cert=next(r for r in records if r.get("certificate_id")=="CERT-ABS-CONV-001")
    rec("CHK-CERTIFICATE-SCOPE-002C", "analytic continuation" in cert["does_not_permit"] and "rearrangement" in cert["permits"], {"certificate":"CERT-ABS-CONV-001"})
    pvg_record=next(r for r in records if r["kind"]=="pvg_translation")
    rec("CHK-PVG-LOSS-PROFILE-002C", all(x in pvg_record["loses_or_does_not_supply"] for x in ["convergence","continuation","zeros"]), {"losses":pvg_record["loses_or_does_not_supply"]})
    rec("CHK-NO-RH-PROGRESS-002C", not any("RH proof" in json.dumps(r) or "RH progress" in json.dumps(r) for r in records), {"scientific_ceiling":"no RH/GRH progress"})
    passed=sum(c["status"]=="PASS" for c in checks)
    return {"unit":"RMG-002-C","status":"PASS" if passed==len(checks) else "FAIL","summary":{"passed":passed,"total":len(checks)},"scientific_ceiling":"finite coefficient and numerical convergence diagnostics; no analytic continuation, zero-free region, RH or GRH progress","checks":checks}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--write-result",action="store_true"); args=ap.parse_args()
    result=run(); text=json.dumps(result,indent=2,sort_keys=True); print(text)
    if args.write_result:
        RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(text+"\n",encoding="utf-8")
    return 0 if result["status"]=="PASS" else 1

if __name__=="__main__": raise SystemExit(main())
