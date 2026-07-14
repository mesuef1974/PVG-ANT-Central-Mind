#!/usr/bin/env python3
"""PASS014: diagonal/non-diagonal decomposition of on-residue character energy."""
import argparse, json, numpy as np
from avrg_pass013 import PRIMES, sieve_theta, singular_main, chars, conv_fft

def run(exp):
    lo,hi=2**exp,2**(exp+1)
    theta=sieve_theta(hi); main=singular_main(hi)
    ns=np.arange(hi+1); base=(ns>=lo)&(ns<hi)&(ns%2==0)
    # The diagonal m1=m2 in |T_chi|^2.  |chi(m)|^2 removes m divisible by r.
    rows=[]
    for r in PRIMES:
        _,cs=chars(r,hi)
        unit=(ns%r!=0)
        diagonal=conv_fft(theta**2*unit,theta**2)[:hi+1].real
        on=base&(ns%r==0)
        off=base&~on
        diag_energy=float(np.mean(diagonal[on]/main[on]**2)/(r-1))
        diag_off=float(np.mean(diagonal[off]/main[off]**2)/(r-1))
        for k,c in enumerate(cs):
            if k==0 or k%2: continue
            T=conv_fft(c*theta,theta)[:hi+1]
            total=float(np.mean(np.abs(T[on]/main[on])**2)/(r-1))
            U=T.copy(); U[off] += c[off]*main[off]/(r-2)
            total_off=float(np.mean(np.abs(U[off]/main[off])**2)/(r-1))
            non=total-diag_energy
            rows.append(dict(r=r,k=k,parity='even',total=total,
                diagonal=diag_energy,non_diagonal=non,
                diagonal_share=diag_energy/total,
                total_over_diagonal=total/diag_energy,
                off_total=total_off,off_raw_diagonal=diag_off,
                on_off_total_ratio=total/total_off,
                on_off_raw_diagonal_ratio=diag_energy/diag_off))
    return dict(exp=exp,window=[lo,hi],normalization='character energy divided by r-1',rows=rows)

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--exp',type=int,default=18); ap.add_argument('--out'); a=ap.parse_args()
    z=run(a.exp); s=json.dumps(z,indent=2)
    if a.out: open(a.out,'w').write(s+'\n')
    else: print(s)
