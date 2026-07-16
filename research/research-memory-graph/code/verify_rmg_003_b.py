#!/usr/bin/env python3
"""RMG-003-B finite verifier: residue Chebyshev observables and claim boundaries."""
from __future__ import annotations
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'registry'/'prime-distribution-ap-character-chebyshev.jsonl'
OUT=ROOT/'results'/'rmg_003_b_verification.json'

def valuation(n:int):
    out={};d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out

def lam(n:int)->float:
    v=valuation(n)
    return math.log(next(iter(v))) if len(v)==1 else 0.0

def units(q:int): return [a for a in range(q) if math.gcd(a,q)==1]
def phi(q:int): return len(units(q))
def psi_ap(x:int,q:int,a:int)->float:
    return sum(lam(n) for n in range(1,x+1) if n%q==a%q)

def chars_cyclic_prime(q:int):
    g=2
    order=[];x=1
    for _ in range(q-1): order.append(x);x=x*g%q
    pos={a:i for i,a in enumerate(order)}
    return [lambda n,j=j: 0j if math.gcd(n,q)>1 else cmath.exp(2j*math.pi*j*pos[n%q]/(q-1)) for j in range(q-1)]

import cmath

def run():
    checks=[]
    def rec(i,ok,e): checks.append({'check_id':i,'status':'PASS' if ok else 'FAIL','evidence':e})
    records=[json.loads(x) for x in REG.read_text(encoding='utf-8').splitlines() if x.strip()]
    rec('CHK-RMG003B-SCHEMA-001',len(records)==12 and len({r['record_id'] for r in records})==12,{'records':len(records)})
    q=5;chs=chars_cyclic_prime(q);x=500
    direct={a:psi_ap(x,q,a) for a in units(q)}
    twisted=[sum(ch(n)*lam(n) for n in range(1,x+1)) for ch in chs]
    recon={a:sum(ch(a).conjugate()*twisted[j] for j,ch in enumerate(chs))/phi(q) for a in units(q)}
    rec('CHK-RMG003B-ORTH-RECON-001',all(abs(recon[a].real-direct[a])<1e-9 and abs(recon[a].imag)<1e-9 for a in units(q)),{'q':q,'x':x,'direct':direct})
    mods=[3,4,5,8];snap={}
    for mod in mods:
        target=10000/phi(mod)
        snap[str(mod)]={str(a):{'psi':psi_ap(10000,mod,a),'ratio_to_x_over_phi':psi_ap(10000,mod,a)/target} for a in units(mod)}
    rec('CHK-RMG003B-FINITE-SNAPSHOT-001',all(v['psi']>0 for m in snap.values() for v in m.values()),{'x':10000,'moduli':snap})
    neg=[r for r in records if r['kind']=='claim_rejection']
    rec('CHK-RMG003B-NEGATIVE-BOUNDARY-001',len(neg)==3 and all(r['decision']=='REJECT' for r in neg),{'rejections':[r['claim'] for r in neg]})
    levels={r.get('level') for r in records if r['kind'] in {'certificate_ladder','boundary','conditional_certificate'}}
    rec('CHK-RMG003B-CERTIFICATE-LADDER-001',levels=={1,2,3},{'levels':sorted(levels)})
    rec('CHK-RMG003B-NO-GRH-PROMOTION-001',all('no GRH' in r.get('scientific_ceiling','') or r.get('kind')!='conditional_certificate' for r in records),{'scientific_ceiling':'no GRH progress'})
    passed=sum(c['status']=='PASS' for c in checks)
    return {'unit':'RMG-003-B','status':'PASS' if passed==len(checks) else 'FAIL','summary':{'passed':passed,'total':len(checks)},'scientific_ceiling':'finite AP observables and certificate discipline only; no new PNT-AP, zero-free-region, Siegel-zero, or GRH result','checks':checks}

def main():
    result=run(); text=json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True); print(text)
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(text+'\n',encoding='utf-8')
    return 0 if result['status']=='PASS' else 1
if __name__=='__main__': raise SystemExit(main())
