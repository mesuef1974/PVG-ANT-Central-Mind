#!/usr/bin/env python3
"""Finite verifier for TKG-004 identities and reasoning boundaries."""
from __future__ import annotations
import math
from query_tkg_004 import factorization, mangoldt, generalized, explain


def is_prime_power(n:int)->bool:
    return len(factorization(n))==1


def run()->None:
    for n in range(1,513):
        f=factorization(n)
        assert (mangoldt(n)!=0.0)==(len(f)==1 and n>1)
        if len(f)==1:
            p=next(iter(f)); assert abs(mangoldt(n)-math.log(p))<1e-12
        else:
            assert mangoldt(n)==0.0
        assert abs(generalized(n,2.0)-2.0*mangoldt(n))<1e-12
        assert explain(n)['asymptotic_inference_authorized'] is False
    assert mangoldt(72)==0.0
    assert abs(mangoldt(27)-math.log(3))<1e-12
    assert abs(generalized(27,2.0)-2*math.log(3))<1e-12
    # Distinguish Lambda from log n.
    assert abs(mangoldt(8)-math.log(8))>1e-6
    # Local coefficient constancy along one labelled axis.
    for p in (2,3,5,7,11):
        vals=[mangoldt(p**k) for k in range(1,7)]
        assert all(abs(v-math.log(p))<1e-12 for v in vals)
    print('TKG-004 verifier: PASS (finite exact checks; no asymptotic claim)')

if __name__=='__main__': run()
