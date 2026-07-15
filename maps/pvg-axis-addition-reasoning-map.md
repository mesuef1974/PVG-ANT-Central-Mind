# PVG Axis-Addition Reasoning Map

Status: active Central Mind route

## Routing trigger

Activate this route when a problem contains any of:

- ordinary sums `x+y=N` in PVG;
- Goldbach-type representations;
- addition of prime axes;
- residue classes of summands or differences;
- weighted additive convolution;
- reconstruction of fiber weights from modular channels;
- selection of Fourier frequencies under a certification budget.

## Geometry–Analysis–Certificate route

### Geometry

Start from the exact fiber

\[
\mathcal F_N=\{(a,N-a):1\le a<N\}
\]

and its injective valuation image. Record support, heights, prime-point membership, prime-power membership, symmetry under `a\leftrightarrow N-a`, and any modular partition.

### Analysis

Choose the observable:

\[
C_{f,g}(N)=\sum_{a=1}^{N-1}f(a)g(N-a).
\]

Typical choices include indicators, `\Lambda`, Dirichlet characters, residue weights, or experimentally defined fiber weights. Translate residue aggregation through `D_{N,r}` and Fourier analysis on the effective period.

### Certificate

Ask what is actually proved:

- an exact identity;
- injectivity or rank;
- a finite exhaustive verification;
- a lower bound exceeding an independently justified threshold;
- or only a geometric reinterpretation.

No arithmetic existence conclusion follows merely from a visualization, rank computation, or optimization optimum.

## Decision tree

1. **Is the requested operation multiplication?** Use ordinary valuation-vector addition.
2. **Is it integer addition?** Build an addition fiber; do not invent an internal vector sum.
3. **Is the goal counting representations?** Use additive convolution.
4. **Is the goal prime representations?** Intersect with the prime-point locus or use `\Lambda` weights.
5. **Is residue information requested?** Use `2a-N mod r` and reduce to `q(r)`.
6. **Is reconstruction claimed?** Compute rank and kernel first.
7. **Are several moduli used?** Distinguish marginal data from joint signatures and test factorization/information loss.
8. **Are frequencies selected?** Invoke COF with an explicit lower-bound functional, thresholds, budget, and admissible upper bounds.
9. **Is Goldbach mentioned?** State the exact missing positivity/asymptotic certificate.

## Canonical rank facts

For a single modulus:

\[
\operatorname{rank}D_{N,r}=\min\left(N-1,\frac r{\gcd(2,r)}\right).
\]

Thus odd `r\ge N-1` permits complete recovery of arbitrary ordered fiber weights from complete difference channels. Below rank `N-1`, unrestricted exact recovery is impossible without additional structure.

The full finite Fourier family has the same rank as the complete channel vector; the zero mode adds no rank.

## Failure modes the mind must catch

- confusing `\nu(x)+\nu(y)` with `\nu(x+y)`;
- suppressing ordered-pair multiplicity;
- treating the symmetric phase as nonconstant;
- calling marginal multi-modulus data joint data;
- inferring a prime pair from a positive von Mangoldt sum without controlling prime-power contamination;
- treating compatibility relaxations as actual simultaneous certification;
- treating finite benchmark success as an asymptotic theorem;
- calling dominance unconditional deletion rather than a feasibility-preserving exchange rule.

## Output contract

Every response using this route must contain, explicitly or implicitly:

`Object -> Fiber -> Valuation transport -> Observable -> Channel/transform -> Certificate -> Boundary -> Next test`.
