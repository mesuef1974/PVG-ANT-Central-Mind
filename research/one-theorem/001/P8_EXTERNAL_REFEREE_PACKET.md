# External Referee Packet — ONE-LEMMA-TARGET-001

**Packet ID:** `P8-EXTERNAL-REFEREE-001`  
**Date:** 2026-07-12  
**Requested review:** mathematical correctness, priority, and significance  
**Current claim ceiling:** internally proved; originality not certified

## 1. Proposed theorem

Fix integers `q>=1`, `r>=1`, a reduced residue class `(a,q)=1`, and
`W in C_c^infinity(0,infinity)`. Define

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0),
\qquad I_r(1)=1.
\]

Equivalently,

\[
I_r(n)=\mathbf1_{\operatorname{rad}(n)^{2r}\mid n}
\tau\!\left(\frac{n}{\operatorname{rad}(n)^{2r}}\right).
\]

For

\[
S_{r;q,a,W}(x)=
\sum_{\substack{n\ge1\\n\equiv a\pmod q}}I_r(n)W(n/x),
\]

the project proves a fixed-parameter smooth expansion obtained from

\[
D_{r,\chi}(s)=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

where `H_{r,chi}` is holomorphic for

\[
\Re(s)>\frac1{2r+2}.
\]

The expansion has:

- a simple-pole `x^(1/(2r))` layer for `chi^(2r)=chi_0`;
- a double-pole `x^(1/(2r+1)) log x` layer for
  `chi^(2r+1)=chi_0`;
- explicit simple- and double-pole constants;
- remainder
  \[
  O_{q,r,W,\varepsilon}
  \left(x^{1/(2r+2)+\varepsilon}\right).
  \]

The exact statement and constants are in
`P3_P5_SMOOTHED_THEOREM_PROOF.md`.

## 2. Geometric origin

For `n=prod p^alpha`, the divisor set is the lattice box

\[
\prod_{p\mid n}\{0,1,\ldots,\alpha\}.
\]

`I_r(n)` counts lattice points whose coordinate in every active prime direction
lies at distance at least `r` from both facets. Thus it is the margin-interior
lattice-point count of the divisor box.

The geometric construction predicts the local values

\[
I_r(p^\alpha)=
\begin{cases}
0,&1\le\alpha<2r,\\
\alpha-2r+1,&\alpha\ge2r,
\end{cases}
\]

and hence the Bell series

\[
1+\frac{y^{2r}}{(1-y)^2}.
\]

## 3. Proof route

1. Prove the geometric formula and multiplicativity.
2. Derive the Bell series.
3. Cancel the first local terms with
   `(1-y^(2r))(1-y^(2r+1))^2`.
4. Obtain a residual local factor `1+O(y^(2r+2))`.
5. Form the twisted Euler product and continue meromorphically.
6. Use character orthogonality for the reduced residue class.
7. Apply smooth Mellin inversion.
8. Shift to `Re(s)=1/(2r+2)+epsilon`.
9. Compute the simple and double residues.

## 4. Internal verification already completed

- independent reconstruction of the geometric count;
- exact Bell-series derivation;
- symbolic residual-order checks for `r=1,...,8`;
- independent Laurent calculations for both pole types;
- numerical verification of the principal-character finite part at
  `q=1,2,6,30`;
- internal adversarial review;
- second independent proof reconstruction;
- CI checks of all committed certificates.

These checks do not replace expert peer review.

## 5. Prior art already excluded from novelty

The following are not claimed as new:

- squarefull and k-full support;
- the classical `x^(1/2)` and `x^(1/3)` squarefull layers;
- quadratic and cubic torsion-character selection;
- character decomposition in arithmetic progressions;
- Dirichlet `L`-function factorization;
- Mellin inversion, contour shifting, or Selberg–Delange-type transfer.

## 6. Possible distinctive package

Only the following combination remains under originality review:

1. the margin-interior divisor-box weight `I_r`;
2. its exact weighted `2r`-full interpretation;
3. the all-`r` consecutive layer hierarchy `2r`, `2r+1`;
4. the explicit smooth fixed-modulus constants;
5. the residual `2r+2` threshold and error.

## 7. Questions for the mathematical referee

### Correctness

1. Is the local factorization correct at every prime, including `p|q`?
2. Does the residual Euler product justify holomorphy and vertical boundedness in
   the claimed half-plane?
3. Are all singularities crossed in the contour shift identified correctly?
4. Are the simple- and double-pole constants correct, including the finite part
   of the principal character?
5. Is the error term valid for fixed `q,r,W`, uniformly in reduced `a`, as
   `x->infinity`?

### Priority and subsumption

6. Is `I_r` known under another name or notation?
7. Is the theorem an explicit special case of a published general theorem on
   weighted k-full integers or multiplicative functions in progressions?
8. If it is subsumed, does the explicit geometric construction or constant
   calculation still merit a proposition or worked application?
9. Does the smooth fixed-parameter statement have enough mathematical content
   for publication, or is an unsmoothed/uniform strengthening needed?

### PVG contribution

10. Is the divisor-box formulation a materially useful discovery language, or
    merely an expository relabeling once the classical weight is written down?

## 8. Allowed referee outcomes

- `A — ORIGINAL MODEST THEOREM`: proof correct; no prior theorem located;
  contribution sufficient.
- `B — NEW APPLICATION OF KNOWN GENERAL THEOREM`: statement is not method-new,
  but the observable/application is distinctive.
- `C — KNOWN RESULT IN DIFFERENT NOTATION`: exact result already exists.
- `D — CORRECTED THEOREM`: proof or statement needs a specified repair.
- `E — INSUFFICIENT SIGNIFICANCE`: correct but too routine without a stronger
  consequence.

## 9. Source dossier

The external source matrix is in:

- `P8_EXTERNAL_VALIDATION_001.md`;
- `P8-external-source-ledger.json`.

The online audit found no exact match but is explicitly incomplete without a
research-grade database search and human expert review.

## 10. Scientific ceiling

```text
Internal fixed-parameter proof: complete.
Online primary-source audit: partial pass.
External referee decision: absent.
Research-grade priority certification: absent.
Certified originality: absent.
Publication readiness: absent.
New analytic method: no.
RH progress: none.
GRH progress: none.
```
