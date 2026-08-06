#!/usr/bin/env python3
from __future__ import annotations
import cmath, json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'registry'/'dirichlet-characters-residue-phase-lfunctions.jsonl'
OUT=ROOT/'results'/'rmg_003_a_verification.json'

def chars_mod5():
    z=cmath.exp(2j*math.pi/4)
    log={1:0,2:1,4:2,3:3}
    return [lambda n,j=j: 0j if math.gcd(n,5)>1 else z**(j*log[n%5]) for j in range(4)]

def run():
    checks=[]
    def rec(i,ok,e): checks.append({'check_id':i,'status':'PASS' if ok else 'FAIL','evidence':e})
    cs=chars_mod5(); residues=[1,2,3,4]
    rec('CHK-CHAR-PERIODIC-001',all(abs(c(n)-c(n+5))<1e-12 for c in cs for n in range(1,30)),{})
    rec('CHK-CHAR-COMPLETE-MULT-001',all(abs(c(a*b)-c(a)*c(b))<1e-12 for c in cs for a in range(1,25) for b in range(1,25)),{})
    rec('CHK-CHAR-ORTHOGONALITY-001',all(abs(sum(c(a)*c(b).conjugate() for c in cs)-(4 if a==b else 0))<1e-10 for a in residues for b in residues),{'modulus':5})
    rec('CHK-RESIDUE-INDICATOR-001',all(abs(sum(c(n)*c(a).conjugate() for c in cs)/4-(1 if n%5==a else 0))<1e-10 for a in residues for n in range(1,50) if math.gcd(n,5)==1),{})
    s=2.0; chi=cs[1]
    ds=sum(chi(n)/(n**s) for n in range(1,5000))
    prod=1+0j
    for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]: prod/=1-chi(p)/(p**s)
    rec('CHK-L-SERIES-EULER-001',abs(ds-prod)<0.002,{'difference':abs(ds-prod)})
    records=[json.loads(x) for x in REG.read_text().splitlines() if x.strip()]
    rec('CHK-REGISTRY-001',len(records)==10 and len({r['record_id'] for r in records})==10,{'records':len(records)})
    rec('CHK-BOUNDARY-001',sum(r.get('decision')=='REJECT' for r in records)==2,{})
    passed=sum(c['status']=='PASS' for c in checks)
    return {'unit':'RMG-003-A','status':'PASS' if passed==len(checks) else 'FAIL','summary':{'passed':passed,'total':len(checks)},'scientific_ceiling':'finite character and L-series verification only; no PNT-AP, GRH, or new L-function theorem','checks':checks}

if __name__=='__main__':
    r=run(); OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(r,indent=2)+'\n'); print(json.dumps(r,indent=2)); raise SystemExit(0 if r['status']=='PASS' else 1)
