# ACTIVE-003-I — Blockwise Phase-Tail Status v1.2

Status: CLOSED / PASS

## Completed

- Proved the blockwise channel-dependent tail bound.
- Proved partition-refinement monotonicity.
- Implemented verification on 2 <= N <= 300 and 1 <= r <= 20.
- Compared one-block, equal-chunk, dyadic, and singleton partitions for K=0,1,2,3 energy-ranked principal frequency pairs.
- Recorded zero tail-bound mismatches and zero false prime-channel certificates.

## Finite benchmark

Effective channels: 46,345.
Prime-positive channels: 15,833.

At K=3:

- one block: 11,177 certificates;
- dyadic blocks: 11,384 certificates;
- singleton blocks: 11,521 certificates.

Singleton coverage among prime-positive channels is about 72.76 percent in the declared finite range.

## Corrections preserved

The effective channel coordinate is c=u*a mod q, where q=r/gcd(2,r) and u=2/gcd(2,r). The involution induced by a -> N-a is

c -> u*N-c mod q,

not c -> -c in general. All contamination and Fourier checks in this unit use the affine reflection.

## Honest classification

- Theorem: finite-dimensional proved inequality.
- Computation: finite verification only.
- No asymptotic distribution estimate.
- No proof of Goldbach.
- No RH/GRH progress.
- No literature-priority claim.

## Next target

ACTIVE-003-J: replace absolute addition across singleton or small blocks by signed interval/cluster enclosures that retain limited cancellation while remaining rigorous. A candidate route is exact evaluation of a small number of residual clusters plus certified bounds only on the final unresolved remainder.
