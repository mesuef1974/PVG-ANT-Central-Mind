#!/usr/bin/env python3
"""PASS015: full energy budget for off-residue centered character modes."""
import argparse, json, numpy as np
from avrg_pass013 import PRIMES, sieve_theta, singular_main, chars, conv_fft

def avg(z, mask, scale):
    return float(np.mean(z[mask]) / scale)

def ratio_sq(z, main, mask):
    return np.abs(z[mask]/main[mask])**2

def run(exp):
    lo,hi=2**exp,2**(exp+1); ns=np.arange(hi+1)
    theta=sieve_theta(hi); main=singular_main(hi)
    even=(ns>=lo)&(ns<hi)&(ns%2==0); rows=[]
    for r in PRIMES:
        _,cs=chars(r,hi); on=even&(ns%r==0); off=even&~on; scale=r-1
        unit=ns%r!=0
        D=conv_fft(theta**2*unit,theta**2)[:hi+1].real
        d_on=float(np.mean(D[on]/main[on]**2)/scale); d_off=float(np.mean(D[off]/main[off]**2)/scale)
        for k,c in enumerate(cs):
            if k==0 or k%2: continue
            T=conv_fft(c*theta,theta)[:hi+1]
            B=np.zeros(hi+1,dtype=complex); B[off]=c[off]*main[off]/(r-2)
            raw=float(np.mean(ratio_sq(T,main,off))/scale)
            center=float(np.mean(ratio_sq(B,main,off))/scale)
            cross=float(np.mean(2*np.real(T[off]*np.conj(B[off]))/main[off]**2)/scale)
            centered=float(np.mean(ratio_sq(T+B,main,off))/scale)
            on_total=float(np.mean(ratio_sq(T,main,on))/scale)
            rows.append(dict(r=r,k=k,on_total=on_total,
                off_raw_total=raw,off_raw_diagonal=d_off,
                off_raw_nondiagonal=raw-d_off,
                off_center_energy=center,off_cross=cross,
                off_centered_total=centered,
                closure_error=centered-(raw+center+cross),
                on_raw_diagonal=d_on,on_raw_nondiagonal=on_total-d_on,
                on_off_ratio=on_total/centered,
                cross_over_center=-cross/center,
                centering_net=center+cross))
    return dict(exp=exp,window=[lo,hi],normalization='mean divided by r-1; all amplitudes divided by M(N)',rows=rows)

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('--exp',type=int,default=18); p.add_argument('--out'); a=p.parse_args()
    z=run(a.exp); s=json.dumps(z,indent=2)
    if a.out: open(a.out,'w').write(s+'\n')
    else: print(s)
