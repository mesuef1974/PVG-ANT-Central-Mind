#!/usr/bin/env python3
"""PASS021: test amplitude law on r=13,17,19 and full-window defect ratios."""
import argparse,json,numpy as np
from avrg_pass013 import sieve_theta,singular_main,chars,conv_fft
from avrg_pass016 import choose,spectrum

MODULI=(13,17,19)

def leading(A):
    u,s,vh=np.linalg.svd(A,full_matrices=False);v=vh[0];a=s[0]*u[:,0]
    if v.sum()<0:v=-v;a=-a
    return a,v,float(np.linalg.norm(A-np.outer(a,v))/np.linalg.norm(A))

def sampled(exp,samples):
    lo,hi=2**exp,2**(exp+1);ns=np.arange(hi+1);theta=sieve_theta(hi);main=singular_main(hi)
    even=(ns>=lo)&(ns<hi)&(ns%2==0);out=[]
    for r in MODULI:
        _,cs=chars(r,hi);ks=[k for k in range(2,r-1,2)]; pon=choose(even&(ns%r==0),samples);poff=choose(even&(ns%r!=0),samples)
        mats=[]
        for k in ks:
            vo=np.zeros(r);vf=np.zeros(r);center=[]
            for N in pon:
                q,_=spectrum(int(N),cs[k],theta,r,main);vo+=np.bincount(np.arange(len(q))%r,weights=q,minlength=r)
            for N in poff:
                q,_=spectrum(int(N),cs[k],theta,r,main);vf+=np.bincount(np.arange(len(q))%r,weights=q,minlength=r)
                T=np.sum(cs[k][:N+1]*theta[:N+1]*theta[N::-1]);B=cs[k][N]*main[N]/(r-2)
                center.append(abs((T+B)/main[N])**2/(r-1))
            vo/=len(pon);vf/=len(poff);target=np.mean(center);vf += (target-vf.sum())/r
            mats.append((vo,vf))
        Aon=np.array([x[0] for x in mats]);Aoff=np.array([x[1] for x in mats]);ao,wo,eo=leading(Aon);af,wf,ef=leading(Aoff)
        ratios=ao/af
        out.append(dict(r=r,modes=ks,profile_cosine=float(abs(wo@wf)),amplitude_ratios=ratios.tolist(),
            amplitude_ratio_mean=float(np.mean(ratios)),candidate=(r-1)/r,
            relative_to_candidate=float(np.mean(ratios)/((r-1)/r)-1),on_rank1_error=eo,off_rank1_error=ef))
    return dict(exp=exp,window=[lo,hi],samples=samples,rows=out)

def full(exp):
    lo,hi=2**exp,2**(exp+1);ns=np.arange(hi+1);theta=sieve_theta(hi);main=singular_main(hi)
    even=(ns>=lo)&(ns<hi)&(ns%2==0);out=[]
    for r in MODULI:
        _,cs=chars(r,hi);on=even&(ns%r==0);off=even&~on
        for k in range(2,r-1,2):
            T=conv_fft(cs[k]*theta,theta)[:hi+1];U=T.copy();U[off]+=cs[k][off]*main[off]/(r-2)
            Eon=float(np.mean(abs(T[on]/main[on])**2)/(r-1));Eoff=float(np.mean(abs(U[off]/main[off])**2)/(r-1));ratio=Eon/Eoff
            out.append(dict(r=r,k=k,on_energy=Eon,off_energy=Eoff,energy_ratio=ratio,
                implied_defect_ratio=ratio/((r-1)/r)))
    return dict(exp=exp,window=[lo,hi],rows=out)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--mode',choices=['sampled','full'],required=True);p.add_argument('--exp',type=int,default=15);p.add_argument('--samples',type=int,default=64);p.add_argument('--out');a=p.parse_args()
 z=sampled(a.exp,a.samples) if a.mode=='sampled' else full(a.exp);s=json.dumps(z,indent=2)
 if a.out:open(a.out,'w').write(s+'\n')
 else:print(s)
