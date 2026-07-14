#!/usr/bin/env python3
"""PASS018: geometry relative to the cancellation hyperplane 1^perp."""
import argparse,json,numpy as np
from avrg_pass013 import PRIMES,sieve_theta,singular_main,chars
from avrg_pass016 import choose,spectrum

def geom(v):
    r=len(v); s=float(np.sum(v)); n=float(np.linalg.norm(v)); par=abs(s)/np.sqrt(r)
    return dict(sum=s,norm=n,distance_to_cancellation=par,
        cosine_to_ones=(s/(np.sqrt(r)*n) if n else 0.0),
        angle_degrees=float(np.degrees(np.arccos(np.clip(abs(s)/(np.sqrt(r)*n),0,1)))) if n else 90.0,
        cancellation_condition=(float(np.sum(np.abs(v)))/abs(s) if s else float('inf')))

def run(exp,samples):
    lo,hi=2**exp,2**(exp+1);ns=np.arange(hi+1)
    theta=sieve_theta(hi);main=singular_main(hi);even=(ns>=lo)&(ns<hi)&(ns%2==0);blocks=[]
    for r in PRIMES:
        _,cs=chars(r,hi);ks=[k for k in range(1,r-1) if k%2==0]
        if not ks:continue
        pon=choose(even&(ns%r==0),samples);poff=choose(even&(ns%r!=0),samples)
        for k in ks:
            rows={}; centered_off=[]
            for state,picked in [('on',pon),('off_raw',poff)]:
                v=np.zeros(r)
                for N in picked:
                    q,_=spectrum(int(N),cs[k],theta,r,main);h=np.arange(len(q))
                    v += np.bincount(h%r,weights=q,minlength=r)
                    if state=='off_raw':
                        T=np.sum(cs[k][:N+1]*theta[:N+1]*theta[N::-1])
                        B=cs[k][N]*main[N]/(r-2)
                        centered_off.append(abs((T+B)/main[N])**2/(r-1))
                rows[state]=v/len(picked)
            target=float(np.mean(centered_off)); raw=rows['off_raw']
            # Unique minimum-Euclidean-norm adjustment with prescribed new row sum.
            canonical=raw+(target-raw.sum())/r*np.ones(r)
            gon=geom(rows['on']); gro=geom(raw); gc=geom(canonical)
            blocks.append(dict(r=r,k=k,samples=samples,on_vector=rows['on'].tolist(),
                off_raw_vector=raw.tolist(),off_centered_canonical_vector=canonical.tolist(),
                on=gon,off_raw=gro,off_centered_canonical=gc,
                on_off_centered_sum_ratio=gon['sum']/gc['sum'],
                perpendicular_change_norm=float(np.linalg.norm((canonical-canonical.mean())-(raw-raw.mean()))),
                warning='canonical centered vector is a geometric convention, not a unique arithmetic lag decomposition'))
    return dict(exp=exp,window=[lo,hi],construction='minimum-norm centering parallel to ones',blocks=blocks)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--exp',type=int,default=15);p.add_argument('--samples',type=int,default=32);p.add_argument('--out');a=p.parse_args()
 z=run(a.exp,a.samples);s=json.dumps(z,indent=2)
 if a.out:open(a.out,'w').write(s+'\n')
 else:print(s)
