#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math

def primes_upto(n:int)->list[int]:
    ps=[]
    for m in range(2,n+1):
        if all(m%p for p in ps if p*p<=m): ps.append(m)
    return ps

def pi(x:int)->int: return len(primes_upto(x))
def theta(x:int)->float: return sum(math.log(p) for p in primes_upto(x))
def psi_terms(x:int)->list[dict]:
    out=[]
    for p in primes_upto(x):
        q=p; k=1
        while q<=x:
            out.append({'n':q,'p':p,'k':k,'weight':math.log(p),'valuation_point':f'{k}e_{p}'})
            q*=p; k+=1
    return sorted(out,key=lambda z:z['n'])
def psi(x:int)->float: return sum(t['weight'] for t in psi_terms(x))
def explain(x:int)->dict:
    return {'x':x,'primes':primes_upto(x),'pi':pi(x),'theta':theta(x),'psi':psi(x),'prime_power_terms':psi_terms(x),'psi_minus_theta':psi(x)-theta(x),'pvg_interpretation':{'pi':'count unit-height single-axis points','theta':'sum log-axis labels on unit-height points','psi':'sum log-axis labels on all positive-height single-axis points'},'asymptotic_inference_authorized':False}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--x',type=int,default=10); ap.add_argument('--kind',choices=['explain','pi','theta','psi','terms'],default='explain'); a=ap.parse_args()
    if a.x<1: raise SystemExit('x must be positive')
    data={'explain':explain(a.x),'pi':pi(a.x),'theta':theta(a.x),'psi':psi(a.x),'terms':psi_terms(a.x)}[a.kind]
    print(json.dumps(data,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
