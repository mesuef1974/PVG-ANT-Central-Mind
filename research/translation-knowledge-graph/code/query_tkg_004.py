#!/usr/bin/env python3
"""Deterministic symbolic query harness for TKG-004."""
from __future__ import annotations
import argparse, json, math


def factorization(n:int)->dict[int,int]:
    if n<1: raise ValueError('n must be positive')
    out={}; d=2
    while d*d<=n:
        while n%d==0: out[d]=out.get(d,0)+1; n//=d
        d+=1
    if n>1: out[n]=out.get(n,0)+1
    return out


def mangoldt(n:int)->float:
    f=factorization(n)
    return math.log(next(iter(f))) if len(f)==1 else 0.0


def generalized(n:int,power:float)->float:
    return power*mangoldt(n)


def explain(n:int,power:float=1.0)->dict:
    f=factorization(n); support=len(f)
    return {'n':n,'factorization':f,'support_cardinality':support,
            'coefficient':generalized(n,power),'zeta_power':power,
            'prime_power_supported':support==1,
            'pvg_route':'single labelled prime axis' if support==1 else 'multi-axis point; coefficient vanishes',
            'asymptotic_inference_authorized':False}


def local(p:int,max_k:int,power:float)->dict:
    return {'prime':p,'zeta_power':power,
            'coefficients':[{'k':k,'n':p**k,'coefficient':power*math.log(p)} for k in range(1,max_k+1)]}


def main()->None:
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='kind',required=True)
    a=sub.add_parser('coefficient'); a.add_argument('--n',type=int,required=True); a.add_argument('--zeta-power',type=float,default=1.0)
    b=sub.add_parser('local'); b.add_argument('--p',type=int,required=True); b.add_argument('--max-k',type=int,default=5); b.add_argument('--zeta-power',type=float,default=1.0)
    args=ap.parse_args()
    out=explain(args.n,args.zeta_power) if args.kind=='coefficient' else local(args.p,args.max_k,args.zeta_power)
    print(json.dumps(out,ensure_ascii=False,indent=2))

if __name__=='__main__': main()
