# ACTIVE-003-G — Paired-Frequency Energy Selection Status v1.2

Status: CLOSED / PASS

## Scope

Convert conjugate reduced Fourier frequencies into real channel-dependent pair contributions and compare three K-pair selection rules under a uniform L2 tail certificate.

## Proved

- conjugate-pair real decomposition;
- separate Nyquist treatment when q is even;
- uniform pair-tail Cauchy-Schwarz bound;
- fixed-K energy-optimal selection for the declared tail bound;
- local prime-prime certificate after subtracting the higher-prime-power contamination bound.

## Computation

Range:

- 2 <= N <= 300;
- 1 <= r <= 20;
- K in {0,1,2,3}.

Results:

- effective channels: 46,345;
- certificate checks: 556,140;
- prime-positive channels: 15,833;
- reconstruction mismatches: 0;
- tail-bound mismatches: 0;
- false certificates: 0.

K=3 certificates:

- most-negative selection: 5,269;
- largest absolute channel contribution: 9,663;
- largest Fourier energy: 10,319.

## Negative result retained

The initial channel-adaptive idea of selecting the most negative pair contributions is not optimal under the uniform L2 tail bound. It leaves high-energy frequencies in the remainder and underperforms the energy selection rule.

## Scientific classification

- finite Fourier theorem: PROVED;
- verifier: PASS;
- energy-selection advantage: COMPUTATIONAL OBSERVATION consistent with the proved fixed-K tail optimization;
- analytic estimates for nonzero Fourier coefficients: OPEN;
- Goldbach progress: NONE CLAIMED.

## Next target

Replace the channel-uniform tail bound by a channel-dependent bound that uses pair phases or blockwise cancellation, while preserving a rigorous no-false-certificate guarantee.
