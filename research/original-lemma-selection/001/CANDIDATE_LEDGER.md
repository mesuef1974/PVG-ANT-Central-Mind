# Original Lemma Selection 001 — Candidate Ledger

**Stage:** `GOAL-OP-ORIGINAL-LEMMA-SELECTION-001`  
**Status:** preliminary intake; no originality certification.

## Governing geometric object

For

\[
n=\prod_{p^a\parallel n}p^a,
\]

let the divisor box be

\[
\mathcal B(n)=\prod_{p^a\parallel n}\{0,1,\ldots,a\}.
\]

For a divisor point `β=ν(d)`, define its number of boundary coordinates

\[
b_n(d)=\#\{p\mid n:\beta_p\in\{0,a_p\}\}.
\]

The face enumerator is

\[
\Phi_z(n)=\sum_{d\mid n}z^{b_n(d)}
=\prod_{p^a\parallel n}(a-1+2z).
\]

This identity is exact: each coordinate offers `a-1` interior choices of weight `1` and two endpoints of weight `z`.

Specializations:

\[
\Phi_1(n)=\tau(n),
\qquad
\Phi_0(n)=I(n)=\prod_{p^a\parallel n}(a-1).
\]

`I(n)` counts strict interior lattice points and vanishes unless `n` is powerful.

---

## OLS-CAND-001 — Mean of the face enumerator

### Candidate statement

For `z` in a compact subset of `Re(z)>0`, prove uniformly that

\[
\sum_{n\le x}\Phi_z(n)
=
\frac{G_z(1)}{\Gamma(2z)}x(\log x)^{2z-1}
+
O_K\bigl(x(\log x)^{2\Re z-2}\bigr),
\]

with

\[
G_z(s)=
\prod_p(1-p^{-s})^{2z}
\left(
1+\frac{2z p^{-s}}{1-p^{-s}}
+\frac{p^{-2s}}{(1-p^{-s})^2}
\right).
\]

The local factor of `G_z` is `1+O_K(p^{-2\sigma})`, so the natural analytic gate is `σ>1/2`.

### Initial assessment

- exactness: high;
- PVG necessity: high for discovering and interpreting `Phi_z`;
- proof novelty: probably low-to-medium because Selberg–Delange is classical;
- research value: a unified theorem for all face strata and a clear phase transition at `z=0`.

**Preliminary status:** survives.

---

## OLS-CAND-002 — Interior divisor-box two-scale asymptotic

### Exact Euler factorization target

For `I(n)=Phi_0(n)`,

\[
\sum_{a\ge0}I(p^a)p^{-as}
=
1+\frac{p^{-2s}}{(1-p^{-s})^2}.
\]

Set

\[
H(s)=\prod_p
(1-p^{-2s})(1-p^{-3s})^2
\left(1+\frac{p^{-2s}}{(1-p^{-s})^2}\right).
\]

The local factor is `1+O(p^{-4σ})`, suggesting

\[
D_I(s)=\zeta(2s)\zeta(3s)^2H(s),
\qquad
H(s)\text{ absolutely convergent for }\Re s>1/4.
\]

### Candidate asymptotic

Prove

\[
\sum_{n\le x}I(n)
=
C_2x^{1/2}
+x^{1/3}(C_{31}\log x+C_{30})
+R(x),
\]

where

\[
C_2=\zeta(3/2)^2H(1/2),
\qquad
C_{31}=\frac{\zeta(2/3)H(1/3)}{3},
\]

and determine a valid explicit power-saving bound for `R(x)`. The hoped-for `O_epsilon(x^{1/4+epsilon})` is a proof target, not yet certified.

### Initial assessment

This is the sharpest concrete first-theorem candidate. The observable is directly geometric and the two scales correspond to square and cube layers of powerful numbers.

**Preliminary status:** survives; likely finalist.

---

## OLS-CAND-003 — r-margin interior hierarchy

For fixed `r>=1`, define

\[
I_r(n)=\prod_{p^a\parallel n}\max(a-2r+1,0).
\]

It counts divisor points satisfying

\[
r\le v_p(d)\le a_p-r
\]

for every active coordinate.

The proposed factorization is

\[
D_r(s)=\zeta(2rs)\zeta((2r+1)s)^2H_r(s),
\]

where

\[
H_r(s)=\prod_p
(1-p^{-2rs})(1-p^{-(2r+1)s})^2
\left(1+\frac{p^{-2rs}}{(1-p^{-s})^2}\right)
\]

should converge absolutely for `Re(s)>1/(2r+2)`.

### Initial assessment

- strongest geometric generality;
- likely too broad for the first theorem;
- may be best presented as a generalization after `r=1` is proved.

**Preliminary status:** survives but not presently preferred over OLS-CAND-002.

---

## OLS-CAND-004 — Twisted interior Euler factorization

For a Dirichlet character `chi mod q`, propose

\[
\sum_{n\ge1}\frac{I_r(n)\chi(n)}{n^s}
=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

with

\[
H_{r,\chi}(s)=
\prod_p
(1-y_p^{2r})(1-y_p^{2r+1})^2
\left(1+\frac{y_p^{2r}}{(1-y_p)^2}\right),
\qquad
y_p=\chi(p)p^{-s}.
\]

At primes dividing `q`, `chi(p)=0` and the local factor is `1`.

### Initial assessment

This is exact, bounded, and tractable. Alone it may be too routine, but it is the load-bearing lemma for the residue-class candidate.

**Preliminary status:** survives as a prerequisite lemma.

---

## OLS-CAND-005 — Torsion-character bias in residue classes

For fixed `q,r` and `(a,q)=1`, define

\[
S_{r;q,a}(x)=\sum_{\substack{n\le x\\n\equiv a\pmod q}}I_r(n).
\]

Character decomposition plus OLS-CAND-004 predicts:

- `x^{1/(2r)}` terms only from characters satisfying `chi^{2r}=chi_0`;
- `x^{1/(2r+1)}log x` terms only from characters satisfying `chi^{2r+1}=chi_0`.

The target theorem is an explicit residue asymptotic written as sums of residues of the twisted Dirichlet series, with a smaller uniform remainder for fixed `q`.

### Initial assessment

This is the strongest two-bridge candidate: divisor-box geometry determines the exponent layers, while character Fourier analysis selects the torsion frequencies visible in residue fibers.

**Preliminary status:** survives; likely finalist, subject to priority audit.

---

## OLS-CAND-006 — Boundary divisor secondary terms

Let

\[
B(n)=\tau(n)-I(n).
\]

Then a boundary-point summatory formula follows from the divisor problem and OLS-CAND-002.

**Decision:** merge as a corollary of OLS-CAND-002. It is not an independent target.

---

## OLS-CAND-007 — Rank of truncated divisibility aggregation

The matrix `1_{d|n}`, `1<=d<=D`, `1<=n<=N`, has rank `D` for `N>=D` by its triangular `D x D` submatrix.

**Decision:** killed as elementary linear algebra.

---

## OLS-CAND-008 — Recovery from full divisor aggregates

For

\[
A_d=\sum_{d\mid n}a_n,
\]

finite Möbius inversion gives

\[
a_n=\sum_{k\le N/n}\mu(k)A_{nk}.
\]

**Decision:** killed as classical Möbius inversion.

---

## OLS-CAND-009 — Mean normalized prime-factor mass energy

The proposed limit

\[
\frac1x\sum_{n\le x}
\sum_p\left(\frac{v_p(n)\log p}{\log n}\right)^q
\longrightarrow\frac1q
\]

is expected from the Poisson–Dirichlet limit for normalized logarithmic prime factors.

**Decision:** killed pending an exact citation; likely a known probabilistic consequence rather than a new PVG theorem.

---

## OLS-CAND-010 — Shape-conditioned residue Parseval

For any valuation selector `W(n)`, character orthogonality exactly converts reduced-residue variance into nonprincipal character energy.

**Decision:** killed as direct Parseval/orthogonality. A nontrivial asymptotic for a specific `W` may still produce a new candidate.

---

## Preliminary shortlist

1. `OLS-CAND-001` — face-enumerator Selberg–Delange family;
2. `OLS-CAND-002` — strict-interior two-scale asymptotic;
3. `OLS-CAND-005` — torsion-character residue bias.

`OLS-CAND-004` is retained as a likely prerequisite lemma. `OLS-CAND-003` is retained as a later generalization.

No finalist is yet certified original. The next gate is an exact literature and proof-risk audit of the three-item shortlist.
