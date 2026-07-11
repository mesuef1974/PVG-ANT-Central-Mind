# P7 Source and Priority Audit — ONE-LEMMA-TARGET-001

**Target:** Smoothed torsion layers of margin-interior divisor boxes in arithmetic progressions  
**Date:** 2026-07-12  
**Status:** source-grounded priority audit in progress  
**Scientific ceiling:** no originality certificate; no theorem promotion

## 1. Object under audit

For fixed integer `r>=1`, define

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0).
\]

Geometrically, `I_r(n)` counts divisor-box lattice points whose coordinate distance from every facet is at least `r`.

The frozen smoothed target concerns

\[
S_{r;q,a,W}(x)=\sum_{n\equiv a\pmod q} I_r(n)W(n/x),
\qquad (a,q)=1,
\]

and the twisted Dirichlet series

\[
D_{r,\chi}(s)
=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s).
\]

## 2. Confirmed classical neighborhood

### 2.1 Squarefull numbers in arithmetic progressions

Tsz Ho Chan, **Squarefull numbers in arithmetic progression II**, arXiv:1407.0054 (2014), studies the unweighted squarefull counting problem in a fixed reduced residue class.

Confirmed from the source:

- squarefull numbers are represented through the classical `a^2 b^3` structure;
- the residue-class main terms separate quadratic and cubic root-counting layers;
- the proof explicitly uses

\[
G_2=\{\chi\pmod q:\chi^2=\chi_0\},
\qquad
G_3=\{\chi\pmod q:\chi^3=\chi_0\};
\]

- the article states that an earlier treatment by Srichan expressed the main terms using Dirichlet characters and Dirichlet `L`-functions;
- Chan's paper improves the error term for the unweighted squarefull progression problem by exponential-sum methods.

**Consequence for our claim:** quadratic/cubic torsion-character selection is classical and cannot be claimed as a new mechanism.

### 2.2 Powerful and k-full literature

The audited literature also includes modern work on:

- powerful numbers and arithmetic progressions;
- squarefull numbers in arithmetic progressions;
- powerful numbers in short intervals;
- `k`-full numbers and related distribution questions.

These works establish that support on exponents `>=2`, or more generally `>=k`, is classical. Therefore the support property of `I_r` is not original by itself.

## 3. Exact overlap with the target

The following components are **known or classical interfaces**:

1. character orthogonality for reduced residue classes;
2. torsion selection by `\chi^m=\chi_0` when an `L(ms,\chi^m)` factor has a pole;
3. Mellin inversion for smooth compactly supported weights;
4. contour shifting and residue extraction for fixed modulus;
5. the general squarefull `2/3`-layer phenomenon at `r=1`;
6. polynomial vertical growth of fixed-modulus Dirichlet `L`-functions.

They must be attributed and are not part of any originality claim.

## 4. Candidate contribution that survives the audit

The remaining potentially distinctive package is narrower:

### A. The PVG observable

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0)
\]

is not merely the indicator of `(2r)`-full integers. It weights each prime-power coordinate by the number of admissible interior coordinate positions.

### B. The divisor-box interpretation

The observable is derived canonically from margin geometry of the divisor box, rather than chosen as an arbitrary multiplicative weight.

### C. The exact local Bell series

For `y=\chi(p)p^{-s}`,

\[
\sum_{\alpha\ge0} I_r(p^\alpha)y^\alpha
=1+\frac{y^{2r}}{(1-y)^2}.
\]

### D. The general layer extraction

The factorization isolates the consecutive geometric layers `2r` and `2r+1`:

\[
D_{r,\chi}(s)
=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

with residual local order `2r+2`.

### E. The explicit smoothed weighted formula

The candidate theorem gives the fixed-modulus smoothed expansion with explicit simple- and double-pole constants for this weight and the remainder

\[
O_{q,r,W,\varepsilon}
\left(x^{1/(2r+2)+\varepsilon}\right).
\]

## 5. Priority search result

The directed search found **no exact textual or formula match** for any of the following:

- `prod max(a-2r+1,0)` as an arithmetic weight;
- “margin-interior divisor box” in the valuation-lattice sense;
- the complete general `2r,2r+1` twisted factorization attached to this weight;
- the exact smoothed residue-class expansion with the constants recorded in the frozen target.

This negative search result is **not** an originality certificate. Older papers may phrase the same object as a weighted `k`-full function, a Bell-series example, or a special case of a general theorem on multiplicative functions.

## 6. General-theorem subsumption risk

The main remaining priority risk is not a paper with the same title. It is a broad theorem that could imply the target immediately, for example:

- a general Selberg–Delange theorem for multiplicative functions whose first nonzero prime-power coefficients occur at prescribed exponents;
- a general theorem on weighted powerful or `k`-full numbers in progressions;
- a general smooth summation theorem for finite products of shifted Dirichlet `L`-functions with an absolutely convergent Euler product;
- an older Bell-series classification of weighted full numbers.

Even if such a theorem subsumes the analytic proof, the explicit PVG-derived observable and constants may still be a new application; that would be weaker than a new theorem or method.

## 7. Current originality classification

```text
Known:
  squarefull and k-full support;
  quadratic/cubic torsion selection at r=1;
  character and Mellin machinery;
  general contour method.

Potentially distinctive:
  margin-interior divisor-box observable I_r;
  general consecutive 2r / 2r+1 layer package;
  explicit weighted smooth fixed-q constants;
  PVG derivation and interpretation.

Not yet certified:
  historical priority of I_r;
  non-subsumption by a general multiplicative-function theorem;
  publication-level novelty.
```

## 8. P7 decision

\[
\boxed{\text{TARGET SURVIVES P7 PRIORITY AUDIT, WITH A NARROW CLAIM}}
\]

The target survives as a candidate theorem/application, but the allowable novelty claim is restricted to the PVG-derived weighted family and its explicit general formula.

It is forbidden to claim:

- discovery of quadratic/cubic torsion selection;
- a new contour method;
- a new theory of squarefull numbers;
- a certified original theorem before independent proof and broader-source review.

## 9. Remaining source actions

1. Obtain and inspect the earlier Chan–Tsang squarefull progression paper.
2. Obtain and inspect Srichan's character/`L`-function treatment and cubefull extension.
3. Search older weighted powerful and `k`-full literature by Bell-series/local-factor terminology.
4. Compare the statement against a precise general Selberg–Delange or smooth contour theorem.
5. Add exact theorem/page citations for Mellin inversion, vertical growth, and the contour shift.

## 10. Honest conclusion

P7 does not kill the target, but it substantially narrows the originality claim. The manual proof candidate remains mathematically relevant. Final classification must wait for independent line-by-line proof review and completion of the older-source audit.
