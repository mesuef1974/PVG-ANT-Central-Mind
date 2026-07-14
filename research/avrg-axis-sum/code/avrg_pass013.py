#!/usr/bin/env python3
"""PASS013: exact Dirichlet-character projections of residue Goldbach axes."""
import argparse, json, math
import numpy as np

PRIMES = (3, 5, 7, 11)

def sieve_theta(n):
    a = np.ones(n + 1, dtype=bool); a[:2] = False
    for p in range(2, math.isqrt(n) + 1):
        if a[p]: a[p*p:n+1:p] = False
    t = np.zeros(n + 1); idx = np.flatnonzero(a); t[idx] = np.log(idx)
    return t

def primitive_root(p):
    for g in range(2, p):
        if len({pow(g,j,p) for j in range(p-1)}) == p-1: return g
    raise ValueError(p)

def chars(p, n):
    g = primitive_root(p); log = {}; x = 1
    for j in range(p-1): log[x] = j; x = x*g % p
    residue = np.arange(n+1) % p
    out=[]
    for k in range(p-1):
        vals=np.zeros(n+1,dtype=complex)
        for a,j in log.items(): vals[residue==a]=np.exp(2j*np.pi*k*j/(p-1))
        out.append(vals)
    return g,out

def singular_main(N):
    # Hardy--Littlewood main term for even N, zero for odd N.
    m=np.zeros(N+1); C2=0.6601618158468696
    fac=np.ones(N+1)
    isp=np.ones(N+1,dtype=bool); isp[:2]=False
    for p in range(2,math.isqrt(N)+1):
        if isp[p]: isp[p*p:N+1:p]=False
    for p in np.flatnonzero(isp)[1:]: fac[p::p] *= (p-1)/(p-2)
    n=np.arange(N+1); z=(n>=4)&(n%2==0); m[z]=2*C2*n[z]*fac[z]
    return m

def conv_fft(a,b):
    L=1<<(len(a)+len(b)-2).bit_length()
    return np.fft.ifft(np.fft.fft(a,L)*np.fft.fft(b,L))[:len(a)+len(b)-1]

def run(exp):
    lo,hi=2**exp,2**(exp+1); theta=sieve_theta(hi); main=singular_main(hi)
    even=(np.arange(hi+1)>=lo)&(np.arange(hi+1)<hi)&(np.arange(hi+1)%2==0)
    rows=[]
    for p in PRIMES:
        g,cs=chars(p,hi)
        for k,c in enumerate(cs):
            T=conv_fft(c*theta,theta)[:hi+1]
            U=T-main if k==0 else T.copy()
            if k:
                off=np.arange(hi+1)%p!=0
                U[off] += c[off]*main[off]/(p-2)
            on=even&(np.arange(hi+1)%p==0); off=even&~on
            mse=lambda z: float(np.mean(np.abs(U[z]/main[z])**2)/(p-1))
            rows.append(dict(r=p,k=k,parity="even" if k%2==0 else "odd",
                on_mse=mse(on),off_mse=mse(off),on_max_abs=float(np.max(np.abs(T[on]))) if k%2 else None))
    return dict(exp=exp,window=[lo,hi],rows=rows)

if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--exp',type=int,default=19); ap.add_argument('--out'); args=ap.parse_args()
    z=run(args.exp); s=json.dumps(z,indent=2)
    if args.out: open(args.out,'w').write(s+'\n')
    else: print(s)
