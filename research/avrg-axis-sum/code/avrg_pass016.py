#!/usr/bin/env python3
"""PASS016: sampled lag spectrum h=m1-m2 for twisted Goldbach modes."""
import argparse, json, math, numpy as np
from avrg_pass013 import sieve_theta, singular_main, chars

MODES=((5,2),(7,2),(11,2),(11,4))

def choose(mask, count):
    x=np.flatnonzero(mask)
    if len(x)<=count:return x
    return x[np.linspace(0,len(x)-1,count,dtype=int)]

def bins_for(n):
    e=np.arange(n+1); b=np.zeros(n+1,dtype=int)
    b[1:]=np.floor(np.log2(e[1:])).astype(int)+1
    return b, ['0']+[f'2^{j-1}..2^{j}-1' for j in range(1,int(math.log2(n))+2)]

def spectrum(N,c,theta,r,main):
    x=c[:N+1]*theta[:N+1]*theta[N::-1]
    L=1<<(2*len(x)-1).bit_length()
    ac=np.fft.ifft(np.abs(np.fft.fft(x,L))**2)[:len(x)]
    # C0 + 2 Re C_h (h>0) partitions |sum x|^2 into signed lag contributions.
    q=np.empty(len(x)); q[0]=ac[0].real; q[1:]=2*ac[1:].real
    q/=main[N]**2*(r-1)
    return q,abs(np.sum(x)/main[N])**2/(r-1)

def run(exp,samples):
    lo,hi=2**exp,2**(exp+1); ns=np.arange(hi+1)
    theta=sieve_theta(hi); main=singular_main(hi); even=(ns>=lo)&(ns<hi)&(ns%2==0)
    bidx,blabel=bins_for(hi); rows=[]
    for r,k in MODES:
        _,cs=chars(r,hi); c=cs[k]
        for state,mask in [('on',even&(ns%r==0)),('off',even&(ns%r!=0))]:
            picked=choose(mask,samples); byres=np.zeros(r); byscale=np.zeros(len(blabel)); totals=[]; closures=[]
            for N in picked:
                q,total=spectrum(int(N),c,theta,r,main)
                h=np.arange(len(q)); byres += np.bincount(h%r,weights=q,minlength=r)
                byscale += np.bincount(bidx[:len(q)],weights=q,minlength=len(blabel))
                totals.append(total); closures.append(float(q.sum()-total))
            byres/=len(picked); byscale/=len(picked)
            rows.append(dict(r=r,k=k,state=state,samples=len(picked),raw_energy=float(np.mean(totals)),
                lag0=float(byscale[0]),nonzero_lags=float(byscale[1:].sum()),
                residue_contributions=byres.tolist(),scale_contributions=byscale.tolist(),
                scale_labels=blabel,max_abs_closure=max(abs(x) for x in closures)))
    return dict(exp=exp,window=[lo,hi],method='deterministic equally spaced N sample; exact FFT autocorrelation per N',rows=rows)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--exp',type=int,default=15);p.add_argument('--samples',type=int,default=48);p.add_argument('--out');a=p.parse_args()
    z=run(a.exp,a.samples);s=json.dumps(z,indent=2)
    if a.out:open(a.out,'w').write(s+'\n')
    else:print(s)
