# RMG-003-D — Dirichlet L-Function Zeros, Explicit Formula in Arithmetic Progressions, and GRH Boundary Graph

## Status

`COMPLETED`

## Purpose

This unit connects the finite character-weighted arithmetic observables already registered in `RMG-003-A..C` to the analytic objects governing prime distribution in arithmetic progressions:

- nontrivial zeros of Dirichlet L-functions;
- logarithmic derivatives;
- explicit formulas for character channels;
- reconstruction of residue channels;
- exceptional real-zero effects;
- the conditional GRH error-term layer.

The unit is a dependency and boundary map. It is not a zero-finding theorem, an explicit-formula proof, or progress on GRH.

## Core identities and dependencies

For a Dirichlet character `chi`, in the absolutely convergent half-plane,

\[
-\frac{L'(s,\chi)}{L(s,\chi)}
=
\sum_{n\ge1}\frac{\Lambda(n)\chi(n)}{n^s}.
\]

The finite weighted observable is

\[
\psi(x,\chi)=\sum_{n\le x}\Lambda(n)\chi(n).
\]

For `(a,q)=1`, finite character orthogonality gives the exact reconstruction

\[
\psi(x;q,a)
=
\frac1{\varphi(q)}
\sum_{\chi\bmod q}\overline{\chi(a)}\,\psi(x,\chi).
\]

The explicit formula for each character channel requires additional global analytic inputs:

1. continuation of the completed L-function;
2. its functional equation and gamma factors;
3. contour displacement;
4. residue calculations;
5. summation and tail control for the zero terms.

Only after those certificates are supplied can the zeros of `L(s,chi)` enter an explicit formula for `psi(x,chi)`, and hence for `psi(x;q,a)`.

## PVG translation

The finite arithmetic side has a precise PVG representation:

```text
valuation vector
→ decoded integer
→ residue class modulo q
→ character phase chi(n)
→ Lambda-weighted channel mass
```

Thus `psi(x,chi)` is an exact finite phase-weighted observable on single-axis prime-power points.

The analytic zero side is not encoded by the valuation vector alone. In this unit, zeros enter PVG only as externally certified oscillatory parameters attached through the explicit formula. This translation is partial and noninvertible.

## Preserved and lost information

### Preserved

- the integer represented by each valuation vector;
- the residue class modulo `q`;
- the character value;
- the von Mangoldt weight;
- finite character orthogonality;
- finite reconstruction of residue channels.

### Not preserved automatically

- meromorphic or entire continuation;
- gamma factors;
- zero locations and multiplicities;
- a zero-free region;
- exceptional-zero exclusion;
- explicit-formula remainder estimates;
- GRH.

A finite table of residue-channel values is therefore a many-to-one projection of the global analytic data.

## Principal and nonprincipal channels

The principal character channel carries the main term through the pole inherited from the zeta function. Primitive nonprincipal completed L-functions are entire. This distinction belongs to the analytic certificate layer; it is not inferred merely from visible finite balance among residue classes.

## Exceptional-zero boundary

A possible real zero close to `1` for a real character can produce a dominant secondary term and visible bias in arithmetic progressions. The governance rule is two-sided:

- a finite bias does not prove an exceptional zero;
- finite balance does not exclude one.

Any exceptional-zero claim requires an independent zero-location certificate.

## GRH boundary

GRH asserts that every nontrivial zero of every primitive Dirichlet L-function has real part `1/2`. Under GRH, square-root-scale error terms, up to logarithmic factors, become available for prime distribution in arithmetic progressions.

This dependency is recorded only as a conditional theorem interface:

```text
GRH assumption
→ critical-line zero location
→ square-root-scale character-channel error
→ arithmetic-progression error term
```

No reverse implication is claimed from finite computation, PVG translation, or observed channel balance.

## Numerical verification

The executable harness uses the primitive real character modulo `4`.

At

\[
s=2+0.4i
\]

and cutoff `12000`, it compares

\[
\sum_{n\le12000}\frac{\Lambda(n)\chi(n)}{n^s}
\]

with its exact finite prime-power regrouping. The recorded gap is

```text
6.938893903907228e-18
```

which is floating-point roundoff.

Finite character observables were also computed:

```text
psi(100, chi_4)   = -0.1125648875540417
psi(1000, chi_4)  = -8.713394532556894
psi(10000, chi_4) = 28.489906584357232
```

These values demonstrate finite cancellation and oscillation only. They do not locate zeros.

## Regression result

```text
PASS 7/7
```

Checks cover:

- registry cardinality;
- unique identifiers;
- logarithmic-derivative prime-power regrouping;
- finite character observables;
- presence of explicit-formula and boundary records;
- claim-rejection coverage;
- rejection of any GRH promotion.

## Assimilation state

```text
character logarithmic derivative in Re(s)>1 = L4_NUMERICALLY_VERIFIED
finite psi(x,chi) observable                 = L5_COMPUTATIONALLY_REGRESSION_TESTED
explicit-formula dependency                  = L2_TRANSLATED_TO_PVG
AP reconstruction with analytic inputs       = L3_BIDIRECTIONALLY_ANALYZED
exceptional-zero boundary                    = L2_TRANSLATED_TO_PVG
GRH conditional layer                        = L2_TRANSLATED_TO_PVG
Lean proof added                             = none
L6 promotion                                 = not authorized
GRH progress                                 = none
```

## Claim rejections

The unit rejects:

```text
zeros checked up to height T
⇒ GRH
```

and

```text
finite balance of residue channels
⇒ zero-free region or critical-line theorem
```

It also rejects:

```text
PVG encoding of character phases
⇒ recovery of all Dirichlet L-function zeros
```

## Scientific classification

- standard ANT identities: `KNOWN / LITERATURE-BACKED`;
- PVG representation of finite weighted channels: `EXACT REINTERPRETATION`;
- zero-driven PVG oscillation: `PARTIAL DIAGNOSTIC TRANSLATION`;
- explicit-formula graph: `DEPENDENCY MAP`;
- GRH layer: `CONDITIONAL OPEN-PROBLEM BOUNDARY`;
- new theorem: `NONE`.

## Files

```text
registry/dirichlet-l-zeros-explicit-formula-grh-boundary.jsonl
code/verify_rmg_003_d.py
results/rmg_003_d_verification.json
units/RMG-003-D.md
```

## Next unit

```text
RMG-004-A
Sieve Objects, Levels of Distribution,
and Certificate Separation Graph
```
