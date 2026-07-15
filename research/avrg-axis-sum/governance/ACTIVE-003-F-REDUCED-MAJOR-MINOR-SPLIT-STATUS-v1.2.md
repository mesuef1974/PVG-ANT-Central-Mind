# ACTIVE-003-F — Reduced Major/Minor Frequency Split Status

Status: `CLOSED-PASS-v1.2`

## Completed

- Exact reduced Fourier split into zero, major, and minor frequencies — **proved**.
- Uniform minor-tail bound by Cauchy–Schwarz — **proved**.
- Prime-channel sufficient certificate with local higher-prime-power contamination — **proved**.
- Top-\(K\) largest-magnitude rule minimizing residual spectral energy — **proved for the declared L2 objective**.
- Independent finite verification for \(2\le N\le300\), \(1\le r\le20\), and \(K=0,1,2,3\) — **PASS**.

## Verification summary

```text
effective channels         = 46,345
certificate checks         = 185,380
minor-bound mismatches     = 0
false certificates         = 0
prime-positive channels    = 15,833
K=0 certificates           = 419
K=1 certificates           = 2,216
K=2 certificates           = 5,415
K=3 certificates           = 6,749
```

## Interpretation

Computing a few dominant frequencies exactly and controlling only the residual energy is substantially stronger than treating all nonzero frequencies uniformly. Three major frequencies produced more than sixteen times as many certificates as the zero-major-frequency L2 bound.

However, 6,749 certified channels remain far below the 15,833 channels with positive prime-prime mass. The remaining loss comes from using one channel-independent minor bound

\[
B_{\mathcal m}
=
\frac{\sqrt{|\mathcal m|}}q
\left(\sum_{k\in\mathcal m}|\widehat Z(k)|^2\right)^{1/2},
\]

which ignores the channel-dependent phases in the minor sum.

## Scientific ceiling

- No asymptotic major-arc estimate was proved.
- No asymptotic minor-arc estimate was proved.
- No Goldbach theorem was proved.
- The top-\(K\) rule is optimal only for residual L2 energy, not necessarily for channel certification count.
- Finite verification is evidence and regression protection, not proof of an asymptotic statement.

## Next target

`ACTIVE-003-G — Channel-adaptive paired-frequency bounds`

Exploit conjugate frequency pairs and cosine phases to replace the channel-independent minor-energy envelope by a channel-adaptive bound. Candidate directions:

1. pair \(k\) with \(-k\) and use real cosine contributions;
2. order frequency pairs by their channel-specific negative contribution rather than magnitude alone;
3. separate exactly computable adverse pairs from a residual L2 tail;
4. compare channel-adaptive certificates against the current 6,749 benchmark.
