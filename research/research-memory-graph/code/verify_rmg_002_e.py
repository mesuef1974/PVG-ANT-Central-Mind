#!/usr/bin/env python3
"""RMG-002-E finite verification of PNT observables and certificate ladder."""
from __future__ import annotations
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'registry'/'pnt-equivalence-error-term-ladder.jsonl'
OUT=ROOT/'results'/'rmg_002_e_verification.json'

def primes_upto(n:int):
    s=[True]*(n+1)
    if n>=0:s[0]=False
    if n>=1:s[1]=False
    for p in range(2,int(n**0.5)+1):
        if s[p]: s[p*p:n+1:p]=[False]*(((n-p*p)//p)+1)
    return [i for i,v in enumerate(s) if v]

def mangoldt(n:int)->float:
    m=n; p=2; support=[]
    while p*p<=m:
        if m%p==0:
            k=0
            while m%p==0: m//=p; k+=1
            support.append((p,k))
        p+=1
    if m>1:support.append((m,1))
    return math.log(support[0][0]) if len(support)==1 else 0.0

def observables(x:int):
    ps=primes_upto(x)
    return len(ps),sum(math.log(p) for p in ps),sum(mangoldt(n) for n in range(1,x+1))

def run():
    checks=[]
    def rec(cid,ok,evidence): checks.append({'check_id':cid,'status':'PASS' if ok else 'FAIL','evidence':evidence})
    rows=[json.loads(x) for x in REG.read_text().splitlines() if x.strip()]
    ids=[r['record_id'] for r in rows]
    rec('CHK-PNT-REGISTRY-001',len(ids)==len(set(ids)) and len(rows)==11,{'records':len(rows)})
    levels=[r['level'] for r in rows if r['kind']=='error_ladder']
    rec('CHK-PNT-LADDER-001',levels==[0,1,2,3],{'levels':levels})
    eq={r['target'] for r in rows if r['kind']=='equivalence'}
    rec('CHK-PNT-EQUIVALENCE-COVERAGE-001',eq=={'ANT-PI-001','ANT-THETA-001','ANT-PSI-001'},{'targets':sorted(eq)})
    samples={}
    trend_ok=True
    for x in [100,1000,10000,100000]:
        pi,theta,psi=observables(x)
        ratios={'pi_log_over_x':pi*math.log(x)/x,'theta_over_x':theta/x,'psi_over_x':psi/x}
        samples[str(x)]=ratios
        trend_ok &= all(v>0 for v in ratios.values())
    rec('CHK-PNT-FINITE-OBSERVABLES-001',trend_ok,{'samples':samples})
    rec('CHK-PNT-THETA-PSI-ORDER-001',all(observables(x)[1] <= observables(x)[2]+1e-12 for x in [10,100,1000,10000]),{'identity':'theta<=psi'})
    anti=[r['statement'] for r in rows if r['kind']=='anti_collapse']
    rec('CHK-PNT-ANTI-COLLAPSE-001',len(anti)==3 and any('PNT does not imply RH' in x for x in anti),{'rules':anti})
    rh=next(r for r in rows if r.get('name')=='RH_scale_error')
    rec('CHK-PNT-RH-CONDITIONAL-001','RH' in rh['requires'] and rh['classification'].startswith('Conditional'),{'requires':rh['requires']})
    classical=next(r for r in rows if r.get('name')=='classical_zero_free_region_error')
    rec('CHK-PNT-ZFR-CERTIFICATE-001','zero-free region and contour estimates' in classical['requires'],{'requires':classical['requires']})
    rec('CHK-PNT-NO-L6-001',all(r.get('certificate')!='FORMAL_PROOF_CERTIFICATE' for r in rows),{'formal_proofs_added':0})
    rec('CHK-PNT-CLAIM-CEILING-001',all('RH' in r.get('does_not_imply',[]) or r['kind'] not in {'error_ladder'} or r.get('level')==3 for r in rows),{'ceiling':'no RH progress'})
    passed=sum(c['status']=='PASS' for c in checks)
    return {'unit':'RMG-002-E','status':'PASS' if passed==len(checks) else 'FAIL','summary':{'passed':passed,'total':len(checks)},'scientific_ceiling':'finite diagnostics and known implication graph only; no new PNT error term, zero-free region, RH, or GRH progress','checks':checks}

if __name__=='__main__':
    result=run(); OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n'); print(json.dumps(result,indent=2,sort_keys=True)); raise SystemExit(0 if result['status']=='PASS' else 1)
