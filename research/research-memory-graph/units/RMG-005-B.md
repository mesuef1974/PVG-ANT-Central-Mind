# RMG-005-B — Circle Method, Major/Minor Arcs, Singular Series, and Certificate Separation

**Status:** COMPLETED  
**Verification:** PASS 8/8  
**Branch:** `agent/pvg-axis-sum-continuation-002`

## Purpose

Integrate the circle-method layer into the Research Memory Graph without duplicating the existing Montgomery `MNTII-006-H`, its closure audit, Addition Fibers, or `RMG-005-A`.

## Core finite identities

For a finite coefficient sequence `a_n`, define

\[
S(\alpha)=\sum_{n\le N} a_n e(\alpha n).
\]

Then the binary additive coefficient is

\[
r_2(M)=\int_0^1 S(\alpha)^2 e(-\alpha M)\,d\alpha,
\]

and the ternary coefficient is

\[
r_3(M)=\int_0^1 S(\alpha)^3 e(-\alpha M)\,d\alpha.
\]

These are exact coefficient-extraction identities. They are not positivity theorems.

## Addition-fiber interpretation

The Fourier phase enforces the additive fiber:

\[
\mathbf 1_{x+y=M}
=
\int_0^1 e(\alpha(x+y-M))\,d\alpha.
\]

Under PVG, each integer is decoded from its valuation vector before the additive phase is applied. This preserves the finite identity, but it does not make addition componentwise in valuation coordinates.

## Major/minor arc split

Write

\[
[0,1)=\mathfrak M\cup\mathfrak m.
\]

The major arcs require rational approximations that generate arithmetic local factors and an Archimedean model. The minor arcs require an independent cancellation estimate strong enough that

\[
\left|\int_{\mathfrak m} S(\alpha)^k e(-\alpha M)\,d\alpha\right|
<
\text{positive major-arc main term}.
\]

Merely naming the two regions proves nothing.

## Singular series and singular integral

The singular series records local congruence compatibility. Its PVG reading is a product of residue-channel compatibility factors. A truncated or formal product does not establish convergence, nonvanishing, or uniform lower bounds.

The singular integral is an Archimedean scaling factor. It is not intrinsic to the discrete valuation coordinates and must come from a separate continuous approximation.

## Certificate ladder

The logical order is:

1. exact Fourier coefficient identity;
2. major-arc approximation with a controlled tail;
3. definition and convergence of the singular factors;
4. minor-arc domination;
5. positive combined main term;
6. only then an existence or asymptotic conclusion.

No step may be inferred from a later label or from a finite numerical example.

## Numerical regression

The executable verifier compared direct ordered prime-pair counts against discrete Fourier coefficient extraction on a grid of size `4096`:

| N | ordered prime-pair count |
|---:|---:|
| 20 | 4 |
| 30 | 6 |
| 50 | 8 |
| 100 | 12 |

The agreement validates the finite projector and implementation. It is not evidence for all even integers.

## Negative reasoning cases

Rejected:

- exact integral identity `=>` binary Goldbach;
- positive finite examples `=>` asymptotic positivity;
- positive major-arc model `=>` positive full integral without minor-arc control;
- PVG additive-fiber encoding `=>` singular-series convergence;
- local congruence compatibility `=>` prime representation.

## Assimilation state

- finite coefficient extraction: `L5_COMPUTATIONALLY_REGRESSION_TESTED`;
- major/minor arc decomposition: `L3_BIDIRECTIONALLY_ANALYZED`;
- singular-series local interpretation: `L3_BIDIRECTIONALLY_ANALYZED`;
- singular integral: `L1_DEFINED_IN_ANT`;
- nontrivial minor-arc theory: not assimilated in this unit;
- Lean proof: none;
- L6 promotion: not authorized;
- Goldbach progress: none;
- RH/GRH progress: none.

## Provenance

Reuses:

- `ledgers/books/BOOK-ANT-MONTGOMERY-MNT-II-004/units/MNTII-006-H.md`;
- `audits/v0.6-h-closure.md`;
- Addition Fibers and Difference Channels;
- `RMG-005-A` additive Fourier registry.

## Next unit

`RMG-005-C — Weyl Differencing, van der Corput, Exponential-Sum Estimate Ladder, and Minor-Arc Certificate Graph`.
