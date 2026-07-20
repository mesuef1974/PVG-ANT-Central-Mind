#!/usr/bin/env python3
"""Independent Python validation lane for PVG Structural Laboratory v6.

No third-party dependencies. Reimplements the finite smooth-number grid,
saddle diagnostics, calibration, partial correlations, and additive-fiber checks.
Scientific ceiling: finite diagnostics; no theorem or originality claim.
"""
from __future__ import annotations
from itertools import combinations
from math import exp, log, pi, sqrt
from statistics import mean, median
import json


def is_prime(n: int) -> bool:
    if n < 2: return False
    if n % 2 == 0: return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0: return False
        p += 2
    return True


def primes_up_to(y: int) -> list[int]: return [n for n in range(2, y + 1) if is_prime(n)]


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}; x = n; p = 2
    while p * p <= x:
        while x % p == 0: out[p] = out.get(p, 0) + 1; x //= p
        p += 1
    if x > 1: out[x] = out.get(x, 0) + 1
    return out


def dlog(a: int, b: int) -> float:
    fa, fb = factor(a), factor(b)
    return sum(abs(fa.get(p, 0) - fb.get(p, 0)) * log(p) for p in set(fa) | set(fb))


def geometric_abs_third(r: float) -> float:
    q = max(1e-15, 1-r); mu = r/q; var = r/(q*q); sd = sqrt(var)
    cutoff = max(80, int(mu + 32*(sd+1)) + 1); prob = q; total = 0.0
    for k in range(cutoff + 1):
        total += prob * abs(k-mu)**3; prob *= r
        if k > mu + 20*(sd+1) and prob < 1e-16: break
    return total


def saddle(x: int, primes: list[int]) -> dict[str, float]:
    L = log(x)
    def stats(a: float, full: bool=False):
        m=logz=phi2=phi3=third=v2=maxv=0.0
        for p in primes:
            lp=log(p); r=exp(-a*lp); q=max(1e-300,1-r); mu=r/q; v=r/(q*q); vp=lp*lp*v
            m += lp*mu; logz -= log(q); phi2 += vp; phi3 += lp**3*r*(1+r)/(q**3); v2 += vp*vp; maxv=max(maxv,vp)
            if full: third += lp**3*geometric_abs_third(r)
        return m,logz,phi2,phi3,third,v2,maxv
    lo,hi=1e-10,1.0
    while stats(hi)[0] > L and hi < 128: hi *= 2
    for _ in range(110):
        mid=(lo+hi)/2
        if stats(mid)[0] > L: lo=mid
        else: hi=mid
    alpha=(lo+hi)/2; m,logz,phi2,phi3,third,v2,maxv=stats(alpha,True); scale=phi2**1.5
    approx=exp(alpha*L+logz-log(alpha)-.5*(log(2*pi)+log(phi2)))
    return dict(alpha=alpha,approx=approx,phi2=phi2,berry=third/scale,skew=phi3/scale,max_share=maxv/phi2,effective_dim=phi2*phi2/v2)


def generate_smooth(limit: int, primes: list[int], budget: int) -> tuple[list[int], int, bool]:
    vals=[]; nodes=0; aborted=False
    def rec(i: int, current: int):
        nonlocal nodes, aborted
        if aborted: return
        nodes += 1
        if nodes > budget: aborted=True; return
        if i == len(primes): vals.append(current); return
        p=primes[i]; v=current
        while v <= limit:
            rec(i+1,v)
            if aborted: return
            if v > limit//p: break
            v *= p
    rec(0,1); vals.sort(); return vals,nodes,aborted


def upper_bound(a: list[int], x: int) -> int:
    lo,hi=0,len(a)
    while lo<hi:
        mid=(lo+hi)//2
        if a[mid] <= x: lo=mid+1
        else: hi=mid
    return lo


def geometric_points(min_x:int,max_x:int,count:int,offset:float=0.0)->list[int]:
    out=[]
    for i in range(count):
        t=(i+offset)/(count-1+2*offset); z=max(2,round(exp(log(min_x)+(log(max_x)-log(min_x))*t)))
        if z not in out: out.append(z)
    return out


def build_grid(max_x:int,ys:list[int],xs:list[int],budget:int)->list[dict]:
    cells=[]
    for y in ys:
        ps=primes_up_to(y); vals,_,aborted=generate_smooth(max_x,ps,budget)
        if aborted: continue
        for x in xs:
            exact=upper_bound(vals,x); s=saddle(x,ps); err=abs(s['approx']-exact)/exact
            cells.append(dict(x=x,y=y,pi_y=len(ps),exact=exact,error=err,**s))
    return cells


def pearson(x:list[float],y:list[float])->float:
    mx,my=mean(x),mean(y); num=sum((a-mx)*(b-my) for a,b in zip(x,y)); dx=sum((a-mx)**2 for a in x); dy=sum((b-my)**2 for b in y)
    return num/sqrt(dx*dy)


def ranks(a:list[float])->list[float]:
    order=sorted(range(len(a)),key=lambda i:a[i]); out=[0.0]*len(a); i=0
    while i<len(order):
        j=i+1
        while j<len(order) and a[order[j]]==a[order[i]]: j+=1
        r=(i+j-1)/2+1
        for k in range(i,j): out[order[k]]=r
        i=j
    return out


def solve(A:list[list[float]],b:list[float])->list[float]:
    n=len(A); M=[row[:] + [b[i]] for i,row in enumerate(A)]
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(M[i][k])); M[k],M[p]=M[p],M[k]
        if abs(M[k][k])<1e-12: continue
        d=M[k][k]; M[k]=[v/d for v in M[k]]
        for i in range(n):
            if i==k: continue
            q=M[i][k]; M[i]=[u-q*v for u,v in zip(M[i],M[k])]
    return [row[n] for row in M]


def residuals(y:list[float],controls:list[list[float]])->list[float]:
    X=[[1.0,*row] for row in controls]; p=len(X[0]); xtx=[[0.0]*p for _ in range(p)]; xty=[0.0]*p
    for row,target in zip(X,y):
        for i in range(p):
            xty[i]+=row[i]*target
            for j in range(p): xtx[i][j]+=row[i]*row[j]
    for i in range(p): xtx[i][i]+=1e-10
    beta=solve(xtx,xty)
    return [target-sum(v*b for v,b in zip(row,beta)) for row,target in zip(X,y)]


def partial_corr(x:list[float],y:list[float],controls:list[list[float]])->float: return pearson(residuals(x,controls),residuals(y,controls))


def quantile(a:list[float],q:float)->float:
    b=sorted(a); z=(len(b)-1)*q; i=int(z); t=z-i
    return b[i]*(1-t)+(b[min(i+1,len(b)-1)])*t


def calibration(cells:list[dict],edges:list[float])->list[dict]:
    groups=[[] for _ in range(4)]
    for c in cells:
        v=c['berry']; idx=0 if v<=edges[0] else 1 if v<=edges[1] else 2 if v<=edges[2] else 3; groups[idx].append(c['error'])
    return [dict(band=i+1,n=len(g),median=median(g) if g else None,mean=mean(g) if g else None) for i,g in enumerate(groups)]


def counterexamples(cells:list[dict])->dict:
    near=None; reversal=None
    for a,b in combinations(cells,2):
        db=abs(a['berry']-b['berry']); de=abs(a['error']-b['error'])
        if db<=.035 and (near is None or de>near['delta_error']): near=dict(a=a,b=b,delta_B=db,delta_error=de)
        low,high=(a,b) if a['berry']<b['berry'] else (b,a)
        gap=low['error']-high['error']
        if gap>.035 and (reversal is None or gap>reversal['gap']): reversal=dict(low=low,high=high,gap=gap)
    return dict(near_B=near,rank_reversal=reversal)


def additive_fiber(N:int,q:int)->dict:
    rows=[]; residues=[dict(a=a,all=0,goldbach=0,prime_power=0) for a in range(q)]
    for x in range(1,N):
        y=N-x; px=is_prime(x); py=is_prime(y); ppx=len(factor(x))==1 and x>1; ppy=len(factor(y))==1 and y>1
        kind='goldbach' if px and py else 'prime_power' if ppx or ppy else 'composite'; r=x%q
        residues[r]['all']+=1; residues[r]['goldbach']+=kind=='goldbach'; residues[r]['prime_power']+=kind=='prime_power'
        rows.append(dict(x=x,y=y,kind=kind,dlog=dlog(x,y)))
    return dict(N=N,q=q,ordered=len(rows),goldbach=sum(r['kind']=='goldbach' for r in rows),residues=residues)


def run(max_x:int=100000,budget:int=3_000_000)->dict:
    train_ys=[2,3,5,7,11,19]; hold_ys=[3,5,7,13,17,23]
    train_xs=geometric_points(10,max_x,10,0); hold_xs=geometric_points(14,int(max_x*.87),11,.45)
    train=build_grid(max_x,train_ys,train_xs,budget); hold=build_grid(max_x,hold_ys,hold_xs,budget)
    edges=[quantile([c['berry'] for c in train],q) for q in (.25,.5,.75)]
    B=[c['berry'] for c in hold]; E=[c['error'] for c in hold]
    controls=[[c['pi_y'],c['max_share']] for c in hold]; controls2=[[c['pi_y'],c['max_share'],c['alpha']] for c in hold]
    return dict(version='6.0',design=dict(train_ys=train_ys,holdout_ys=hold_ys,train_xs=train_xs,holdout_xs=hold_xs,nonoverlap=True),counts=dict(train=len(train),holdout=len(hold)),edges=edges,correlations=dict(pearson=pearson(B,E),spearman=pearson(ranks(B),ranks(E)),partial_pi_max_share=partial_corr(B,E,controls),partial_pi_max_share_alpha=partial_corr(B,E,controls2)),calibration=dict(train=calibration(train,edges),holdout=calibration(hold,edges)),counterexamples=counterexamples(hold),reference=dict(dlog_60_72=dlog(60,72),psi_100_5=next(c['exact'] for c in build_grid(100,[5],[100],100000))),additive_reference=additive_fiber(100,5),scientific_ceiling='finite computational diagnostics only; no theorem or Goldbach/RH/GRH claim')

if __name__=='__main__': print(json.dumps(run(),ensure_ascii=False,indent=2))
