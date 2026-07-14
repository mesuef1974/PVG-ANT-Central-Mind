#!/usr/bin/env python3
"""PASS017: transition matrix character mode k <-> lag residue h mod r."""
import argparse,json,numpy as np
from avrg_pass013 import PRIMES,sieve_theta,singular_main,chars
from avrg_pass016 import choose,spectrum

def svd_stats(A):
    if not A.size:return dict(singular_values=[],energy_fractions=[],rank_tol=0,rank_99=0,leading_left=[],leading_right=[])
    u,s,vh=np.linalg.svd(A,full_matrices=False); e=s*s; cum=np.cumsum(e)/(e.sum() if e.sum() else 1)
    return dict(singular_values=s.tolist(),energy_fractions=(e/e.sum()).tolist() if e.sum() else e.tolist(),
        rank_tol=int(np.sum(s>s[0]*1e-10)) if len(s) and s[0] else 0,
        rank_99=int(np.searchsorted(cum,.99)+1) if len(s) and e.sum() else 0,
        leading_left=u[:,0].tolist() if len(s) else [],leading_right=vh[0].tolist() if len(s) else [])

def run(exp,samples):
    lo,hi=2**exp,2**(exp+1);ns=np.arange(hi+1)
    theta=sieve_theta(hi);main=singular_main(hi);even=(ns>=lo)&(ns<hi)&(ns%2==0);out=[]
    for r in PRIMES:
        _,cs=chars(r,hi); evenks=[k for k in range(1,r-1) if k%2==0]
        for state,mask in [('on',even&(ns%r==0)),('off',even&(ns%r!=0))]:
            picked=choose(mask,samples);A=np.zeros((len(evenks),r)); closure=0
            for i,k in enumerate(evenks):
                for N in picked:
                    q,total=spectrum(int(N),cs[k],theta,r,main);h=np.arange(len(q))
                    row=np.bincount(h%r,weights=q,minlength=r)
                    A[i]+=row;closure=max(closure,abs(row.sum()-total))
                A[i]/=len(picked)
            # Separate coherent column b=0 from phase-cancellation columns.
            phase=A[:,1:]
            phase_centered=phase-phase.mean(axis=1,keepdims=True) if phase.size else phase
            out.append(dict(r=r,state=state,samples=len(picked),even_modes=evenks,
                matrix=A.tolist(),row_sums=A.sum(axis=1).tolist(),
                coherent_column=A[:,0].tolist(),other_sum=A[:,1:].sum(axis=1).tolist(),
                full_svd=svd_stats(A),phase_svd=svd_stats(phase),
                phase_centered_svd=svd_stats(phase_centered),max_abs_closure=float(closure)))
    return dict(exp=exp,window=[lo,hi],definition='rows even nonprincipal characters k; columns lag residue b mod r',blocks=out)

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--exp',type=int,default=15);p.add_argument('--samples',type=int,default=32);p.add_argument('--out');a=p.parse_args()
 z=run(a.exp,a.samples);s=json.dumps(z,indent=2)
 if a.out:open(a.out,'w').write(s+'\n')
 else:print(s)
