# RMG-005-C — Weyl Differencing, van der Corput, Exponential-Sum Estimate Ladder, and Minor-Arc Certificate Graph

**Status:** COMPLETED

## Purpose

Integrate the standard exponential-sum estimate ladder into the Research Memory Graph while preserving the distinction between:

1. exact finite identities;
2. finite inequalities;
3. observed numerical cancellation;
4. uniform asymptotic estimates;
5. minor-arc domination sufficient for an additive theorem.

This unit reuses the additive-character and circle-method layers from `RMG-005-A/B`. It does not create a parallel Fourier ontology.

## Core objects

For

\[
S_f(N)=\sum_{n\le N} a_n e(f(n)),
\]

the trivial certificate is

\[
|S_f(N)|\le \sum_{n\le N}|a_n|.
\]

A van der Corput step replaces direct control of `S_f` by shifted correlations of the form

\[
\sum_n a_{n+h}\overline{a_n}
 e\bigl(f(n+h)-f(n)\bigr).
\]

For a quadratic phase,

\[
(n+h)^2-n^2=2hn+h^2,
\]

so one differencing step lowers the degree from two to one.

Repeated Weyl differencing extends this degree-lowering mechanism, but a usable theorem still requires explicit hypotheses, constants, approximation data, and a uniform range.

## ANT ↔ PVG translation

For a valuation vector `v=ν(n)`, the phase is represented by decoding `n` and assigning

\[
v\longmapsto e(f(\operatorname{decode}(v))).
\]

This is an exact reindexing when coefficients are preserved.

Shifted correlations require care. The displacement `n -> n+h` is additive in the decoded integers. It is not componentwise addition in valuation space:

\[
\nu(n+h)\ne \nu(n)+\nu(h)
\]

in general.

Therefore the reverse translation is classified as:

```text
exact after integer decoding
not intrinsic valuation-vector addition
```

## Certificate ladder

```text
L0  exact exponential-sum definition
L1  trivial L1 bound
L2  finite shift-correlation identity
L3  finite van der Corput inequality
L4  Weyl / exponent-pair estimate under named hypotheses
L5  uniform bound over the declared minor arcs
L6  minor-arc contribution dominated by a certified major-arc main term
L7  positive representation theorem after every remaining condition is closed
```

No layer may be skipped.

## Numerical regression

The verifier uses

```text
alpha = sqrt(2)
N = 300
H = 20
```

and records:

```text
|sum exp(2πi alpha n)|       = 0.7652836834395833
|sum exp(2πi alpha n^2)|     = 17.754660682154544
trivial bound                = 300
finite van der Corput bound  = 71.0438763472784
cancellation ratio           = 0.05918220227384848
```

It also verifies the quadratic-difference identity at `n=17`, `h=5`:

\[
(22)^2-(17)^2=195=2(5)(17)+5^2.
\]

Result:

```text
PASS 9/9
```

These computations show finite cancellation and validate the implemented finite inequality. They do not establish a uniform Weyl estimate.

## Negative benchmarks

The unit rejects:

```text
finite cancellation at sampled alpha
⇒ uniform exponential-sum estimate
```

```text
exact ANT ↔ PVG reindexing
⇒ cancellation
```

```text
small values on a finite minor-arc grid
⇒ continuum minor-arc domination
```

```text
sample minor-arc domination
⇒ binary Goldbach
```

## Honest classification

```text
finite sum definition and trivial bound       = L5
quadratic difference regression               = L5
finite van der Corput implementation           = L5
Weyl differencing dependency graph             = L3
exponent-pair interface                        = L2
uniform minor-arc certificate                  = not established
Lean proof added                               = none
L6 promotion                                   = not authorized
Goldbach progress                              = none
RH / GRH progress                              = none
```

## Files

- `registry/weyl-vdc-exponential-sum-minor-arc.jsonl`
- `code/verify_rmg_005_c.py`
- `results/rmg_005_c_verification.json`
- `units/RMG-005-C.md`

## Next unit

```text
RMG-005-D
Prime-Weighted Exponential Sums,
Vaughan Decomposition,
and Major/Minor-Arc Transfer Graph
```
