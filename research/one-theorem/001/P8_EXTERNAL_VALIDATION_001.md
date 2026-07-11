# P8 External Validation 001 — Source-Grounded Dossier

**Date:** 2026-07-12  
**Target:** `ONE-LEMMA-TARGET-001`  
**Scope:** online primary-source priority and subsumption audit; not an external referee report

## 1. Object under validation

For fixed `r>=1`,

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0)
=\mathbf 1_{\operatorname{rad}(n)^{2r}\mid n}
\tau\!\left(\frac{n}{\operatorname{rad}(n)^{2r}}\right).
\]

The internally proved theorem gives, for fixed `q,r`, reduced `a mod q`, fixed
`W in C_c^infinity(0,infinity)`, and `x->infinity`, a smooth residue-class
expansion whose singular layers arise from

\[
D_{r,\chi}(s)=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

with `H` holomorphic for `Re(s)>1/(2r+2)` and remainder

\[
O_{q,r,W,\varepsilon}\!\left(x^{1/(2r+2)+\varepsilon}\right).
\]

## 2. Search protocol

The audit searched exact and near-exact forms of:

- `prod max(alpha_p-2r+1,0)`;
- `tau(n/rad(n)^(2r))` on `2r`-full support;
- `1+y^(2r)/(1-y)^2`;
- weighted powerful / squarefull / k-full numbers in arithmetic progressions;
- divisor weights on powerful integers;
- general multiplicative-function theorems in arithmetic progressions;
- Selberg–Delange and meromorphic Dirichlet-series transfer results;
- recent squarefull arithmetic-progression and variance literature.

The search used primary paper pages and full texts where available. Search-engine
absence is not treated as proof of originality.

## 3. Prior art confirmed

### 3.1 Chan, squarefull numbers in arithmetic progressions

T. H. Chan, *Squarefull numbers in arithmetic progression II*, arXiv:1407.0054.

This paper confirms that:

- unweighted squarefull numbers in reduced arithmetic progressions already have
  `x^(1/2)` and `x^(1/3)` layers;
- the quadratic layer uses characters with `chi^2=chi_0`;
- the cubic layer uses characters with `chi^3=chi_0`;
- Chan–Tsang and Srichan are earlier sources for the same squarefull progression
  problem, with Srichan using Dirichlet characters and `L`-functions.

**Effect on our claim:** torsion-character selection and classical squarefull
progression asymptotics are prior art.

### 3.2 Meemark–Wongcharoenbhorn, current squarefull variance literature

Y. Meemark and W. Wongcharoenbhorn,
*Variance of square-full integers in short intervals and arithmetic progressions*,
arXiv:2504.14511.

The paper surveys the classical squarefull counting formula, Chan's arithmetic-
progression result, generalized squarefull integers, and recent variance questions.
It treats the unweighted characteristic function of squarefull integers and does
not state the margin-interior weight `I_r` or its Bell series.

**Effect on our claim:** the current adjacent literature remains centered on
unweighted squarefull counts and variances; no direct match to `I_r` was located.

### 3.3 Munsch–Shparlinski–Yau, smooth squarefull integers in progressions

M. Munsch, I. E. Shparlinski, and K. H. Yau,
*Smooth squarefree and square-full integers in arithmetic progressions*,
arXiv:1810.02573.

This work studies smoothness restrictions and least squarefull representatives
in residue classes. It is adjacent but has a different observable and goal.

**Effect on our claim:** not a direct subsumption.

### 3.4 Cao–Zhai, generalized squarefull arithmetic functions

X. Cao and W. Zhai,
*Conditional Results for a Class of Arithmetic Functions: a variant of H. L.
Montgomery and R. C. Vaughan's method*, arXiv:1301.4530.

Their class is defined by Dirichlet series of the form

\[
\frac{\zeta(as)\zeta(bs)}{\zeta(cs)^k},
\]

and includes generalized squarefull-related examples. The target `I_r` instead
has a character-twisted two-layer factorization with a nontrivial residual Euler
product `H_{r,chi}`. The located statement does not give the exact fixed-residue,
smooth weighted theorem or constants proved here.

**Effect on our claim:** strong general-method adjacency, but no direct match
located.

### 3.5 General multiplicative-function and Selberg–Delange frameworks

- A. Balog, A. Granville, and K. Soundararajan,
  *Multiplicative functions in arithmetic progressions*, arXiv:math/0702389,
  develops a theory for multiplicative functions valued in or on the unit disk.
  The sparse unbounded weight `I_r` is not directly in that stated class.
- R. de la Bretèche and G. Tenenbaum,
  *Remarks on the Selberg–Delange method*, arXiv:2010.12929,
  treats broad mean-value transfer from zeta-type factorizations. This confirms
  that the analytic machinery is classical, but the located framework does not
  state our exact multi-scale, character-twisted, fixed-residue formula.

**Effect on our claim:** method novelty is excluded; statement-level novelty is
not resolved by these general frameworks.

## 4. Exact-match result

No primary source located in this audit stated any of the following exact objects:

\[
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0),
\]

\[
1+\frac{y^{2r}}{(1-y)^2},
\]

or the full fixed-`q`, smooth residue-class theorem with explicit `2r`, `2r+1`,
and residual `2r+2` layers.

This is positive evidence for continued originality review, but it is not a
proof that the statement is absent from all literature.

## 5. Subsumption analysis

### 5.1 What is clearly classical

- support on `2r`-full integers;
- squarefull / k-full parametrizations;
- character decomposition of reduced residue classes;
- torsion-character selection;
- Euler products, Mellin inversion, and contour shifting;
- deriving asymptotics from poles of Dirichlet series.

### 5.2 What appears specific to the project

- selecting `I_r` from divisor-box margin geometry;
- identifying its exact Bell series;
- the consecutive `2r` and `2r+1` layer hierarchy for all `r`;
- the explicit weighted constants in fixed progressions;
- the residual `2r+2` threshold in the smooth theorem.

### 5.3 Method-versus-statement classification

```text
New analytic method: no.
New torsion-character mechanism: no.
New support class: no.
PVG-derived observable: plausibly distinctive.
Exact theorem statement: no match located.
General-theorem subsumption: possible in principle, not identified explicitly.
```

## 6. External-validation decision

\[
\boxed{
\text{ONLINE PRIMARY-SOURCE AUDIT: PARTIAL PASS}
}
\]

The theorem survives as a **plausibly new, modest, PVG-derived weighted
application of classical analytic machinery**.

It is not promoted to a certified original theorem because two gates remain:

1. a research-grade bibliographic database / cited-by audit with full coverage;
2. an external human line-by-line referee review.

## 7. Final allowed wording

Allowed:

> We prove internally a fixed-parameter smooth weighted theorem generated by
> divisor-box margin geometry. An online primary-source audit found no exact
> match, while confirming that the analytic method and torsion mechanism are
> classical. Statement originality remains unverified externally.

Forbidden:

- `certified original theorem`;
- `publication-ready result`;
- `new Selberg–Delange method`;
- `new torsion-character phenomenon`;
- any RH or GRH progress claim.

## 8. Next controlled action

`P8-EXTERNAL-REFEREE-001`:

- prepare a compact referee packet containing theorem, proof, constants, and
  source matrix;
- obtain independent expert review;
- run a research-grade bibliographic database search;
- issue one of:
  - original modest theorem;
  - new application of a known general theorem;
  - known result in different notation;
  - corrected theorem.

**Classification:** external online source audit; originality remains uncertified.
