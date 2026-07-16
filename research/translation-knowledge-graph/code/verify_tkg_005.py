#!/usr/bin/env python3
from __future__ import annotations
import math
from query_tkg_005 import pi, theta, psi, psi_terms, explain

def main()->None:
    assert pi(10)==4
    assert abs(theta(10)-math.log(210))<1e-12
    expected=3*math.log(2)+2*math.log(3)+math.log(5)+math.log(7)
    assert abs(psi(10)-expected)<1e-12
    assert [t['n'] for t in psi_terms(10)]==[2,3,4,5,7,8,9]
    for x in range(1,257):
        ts=psi_terms(x)
        assert abs(sum(t['weight'] for t in ts)-psi(x))<1e-12
        assert psi(x)+1e-12>=theta(x)
        assert pi(x)==sum(1 for p in range(2,x+1) if all(p%d for d in range(2,int(p**0.5)+1)))
        e=explain(x)
        assert e['asymptotic_inference_authorized'] is False
    # Exact finite prime-power correction.
    for x in range(2,129):
        corr=sum(t['weight'] for t in psi_terms(x) if t['k']>=2)
        assert abs((psi(x)-theta(x))-corr)<1e-12
    print('TKG-005 verifier: PASS (finite exact checks only)')
if __name__=='__main__': main()
