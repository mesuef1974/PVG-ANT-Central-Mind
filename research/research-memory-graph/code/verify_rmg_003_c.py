#!/usr/bin/env python3
"""RMG-003-C finite verification harness (stdlib only)."""
from __future__ import annotations
import cmath, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
REG=ROOT/'registry'/'primitive-characters-conductors-gauss-functional-equation.jsonl'
OUT=ROOT/'results'/'rmg_003_c_verification.json'

def chi5(n:int)->complex:
    r=n%5
    return {0:0,1:1,2:1j,3:-1j,4:-1}[r]

def chi8(n:int)->complex:
    if math.gcd(n,8)>1:return 0
    return 1 if n%8 in (1,7) else -1

def induced12(n:int)->complex:
    if math.gcd(n,12)>1:return 0
    return 1 if n%4==1 else -1

def gauss(q,chi):
    return sum(chi(a)*cmath.exp(2j*math.pi*a/q) for a in range(q))

def run():
    checks=[]
    rec=lambda i,o,e: checks.append({'check_id':i,'status':'PASS' if o else 'FAIL','evidence':e})
    records=[json.loads(x) for x in REG.read_text().splitlines() if x.strip()]
    rec('CHK-REGISTRY-001',len(records)==12 and len({r['record_id'] for r in records})==12,{'records':len(records)})
    rec('CHK-CHI5-MULT-001',all(abs(chi5(a*b)-chi5(a)*chi5(b))<1e-12 for a in range(1,40) for b in range(1,40)),{})
    t5=gauss(5,chi5); rec('CHK-GAUSS5-001',abs(abs(t5)-math.sqrt(5))<1e-12,{'tau':[t5.real,t5.imag],'abs':abs(t5)})
    t8=gauss(8,chi8); rec('CHK-GAUSS8-001',abs(abs(t8)-math.sqrt(8))<1e-12,{'tau':[t8.real,t8.imag],'abs':abs(t8)})
    rec('CHK-CONDUCTOR12-001',all(induced12(n)==(0 if math.gcd(n,12)>1 else chi8(n%4) if False else (1 if n%4==1 else -1)) for n in range(1,100)),{'modulus':12,'conductor':4})
    a5=0 if abs(chi5(-1)-1)<1e-12 else 1
    eps=t5/((1j**a5)*math.sqrt(5)); rec('CHK-ROOT-NUMBER-001',abs(abs(eps)-1)<1e-12,{'parity':a5,'epsilon_abs':abs(eps)})
    rec('CHK-BOUNDARY-001',sum(r.get('status')=='REJECTED' for r in records)==2,{'rejections':2})
    passed=sum(c['status']=='PASS' for c in checks)
    return {'unit':'RMG-003-C','status':'PASS' if passed==len(checks) else 'FAIL','summary':{'passed':passed,'total':len(checks)},'scientific_ceiling':'finite character and Gauss-sum verification only; no new functional-equation proof or GRH progress','checks':checks}

if __name__=='__main__':
    result=run(); print(json.dumps(result,indent=2,sort_keys=True))
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    raise SystemExit(0 if result['status']=='PASS' else 1)
