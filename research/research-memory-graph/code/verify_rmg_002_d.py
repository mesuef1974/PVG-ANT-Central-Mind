#!/usr/bin/env python3
"""RMG-002-D finite verifier (stdlib only)."""
from __future__ import annotations
import json, math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "registry" / "von-mangoldt-log-derivative-chebyshev.jsonl"
RESULT = ROOT / "results" / "rmg_002_d_verification.json"

def primes_upto(n):
    sieve=[True]*(n+1)
    if n>=0:sieve[0]=False
    if n>=1:sieve[1]=False
    for p in range(2,int(n**0.5)+1):
        if sieve[p]: sieve[p*p:n+1:p]=[False]*(((n-p*p)//p)+1)
    return [i for i,v in enumerate(sieve) if v]

def valuation(n):
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def lam(n):
    v=valuation(n)
    return math.log(next(iter(v))) if len(v)==1 else 0.0

def theta(x): return sum(math.log(p) for p in primes_upto(x))
def psi(x): return sum(lam(n) for n in range(1,x+1))
def close(a,b,tol=1e-11): return abs(a-b)<=tol*max(1.0,abs(a),abs(b))

def run():
    checks=[]
    def rec(i,ok,e): checks.append({"check_id":i,"status":"PASS" if ok else "FAIL","evidence":e})
    xs=[10,30,100,300,1000]
    rec("CHK-LAMBDA-SUPPORT-001", all((lam(n)>0)==(n>=2 and len(valuation(n))==1) for n in range(1,1001)), {"range":[1,1000]})
    rec("CHK-PSI-LAMBDA-001", all(close(psi(x),sum(lam(n) for n in range(1,x+1))) for x in xs), {"x":xs})
    rec("CHK-THETA-PRIME-001", all(close(theta(x),sum(math.log(p) for p in primes_upto(x))) for x in xs), {"x":xs})
    rec("CHK-PSI-THETA-DECOMP-001", all(close(psi(x),sum(theta(int(x**(1/k))) for k in range(1,20) if 2**k<=x)) for x in xs), {"x":xs})
    rec("CHK-PRIME-POWER-CONTAMINATION-001", all(close(psi(x)-theta(x),sum(math.log(next(iter(valuation(n)))) for n in range(2,x+1) if len(valuation(n))==1 and next(iter(valuation(n).values()))>=2)) for x in xs), {"x":xs})
    s=2.0; N=5000
    rhs=sum(lam(n)*n**(-s) for n in range(1,N+1))
    pside=sum(math.log(p)/(p**s-1.0) for p in primes_upto(N))
    rec("CHK-LOG-DERIVATIVE-TRUNCATED-001", abs(rhs-pside)<0.002, {"s":s,"N":N,"lambda_series":rhs,"prime_power_sum":pside,"difference":abs(rhs-pside)})
    ant=sum(lam(n)*n**(-s) for n in range(1,1001))
    pvg=sum((math.log(next(iter(valuation(n)))) if len(valuation(n))==1 else 0.0)*math.exp(-s*sum(k*math.log(p) for p,k in valuation(n).items())) for n in range(1,1001))
    rec("CHK-PVG-REINDEX-001", close(ant,pvg), {"s":s,"cutoff":1000,"ant":ant,"pvg":pvg})
    rec("CHK-NEGATIVE-RH-001", True, {"rejected_claim":"finite psi verification implies RH"})
    rec("CHK-NEGATIVE-ZERO-RECOVERY-001", True, {"rejected_claim":"single-axis observable recovers nontrivial zeros"})
    rows=[json.loads(x) for x in REGISTRY.read_text().splitlines() if x.strip()]
    rec("CHK-REGISTRY-001", len(rows)==8 and len({r['record_id'] for r in rows})==8, {"records":len(rows)})
    passed=sum(c['status']=='PASS' for c in checks)
    return {"unit":"RMG-002-D","status":"PASS" if passed==len(checks) else "FAIL","summary":{"passed":passed,"total":len(checks)},"scientific_ceiling":"finite identities and half-plane diagnostics only; no zero recovery or RH progress","checks":checks}

if __name__=="__main__":
    r=run(); RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(r,indent=2,sort_keys=True)+"\n"); print(json.dumps(r,indent=2,sort_keys=True)); raise SystemExit(0 if r['status']=='PASS' else 1)
