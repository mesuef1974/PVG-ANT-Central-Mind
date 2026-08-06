# Certificate Optimization Framework

## Additive Certificate Structure v0.1

Status: foundational draft with proved statements

Scientific classification:

- abstract mathematical framework;
- exact finite-set statements;
- no claim that COF is yet a general theory;
- no Goldbach, RH, or GRH claim.

---

## 1. Purpose

The certificate-optimization work developed for Fourier frequency selection uses two objects that must not be left unrelated:

1. a contribution map, and
2. a certified lower-bound functional.

Merely specifying both objects does not imply monotonicity, exchange, dominance, or canonical optimal solutions. The first COF layer therefore isolates the precise relation that is actually used in the existing proofs.

---

## 2. Additive certificate structure

Let \(I\) and \(T\) be finite sets. Elements of \(I\) are called **items** and elements of \(T\) are called **targets**.

An **additive certificate structure** is a tuple

\[
\mathfrak C=(I,T,\beta,\Gamma,\Theta),
\]

where

\[
\beta:T\to\mathbb R,
\qquad
\Gamma:I\times T\to\mathbb R,
\qquad
\Theta:T\to\mathbb R.
\]

For every configuration \(S\subseteq I\), define

\[
L_S(t)=\beta(t)+\sum_{i\in S}\Gamma(i,t).
\]

The target \(t\) is **certified by \(S\)** when

\[
L_S(t)>\Theta(t).
\]

The certificate-count functional is

\[
F(S)=\#\{t\in T:L_S(t)>\Theta(t)\}.
\]

Under a cardinality budget \(B\), the optimization problem is

\[
\max\{F(S):S\subseteq I,\ |S|\le B\}.
\]

The equality

\[
L_{S\cup\{i\}}(t)-L_S(t)=\Gamma(i,t)
\]

for \(i\notin S\) is the exact bridge between the contribution map and the certificate functional.

---

## 3. Why an arbitrary certificate functional is insufficient

If \(L\) is an arbitrary set-indexed functional, the sign or ordering of \(\Gamma\) need not control the change in \(L\). Therefore none of the following follows merely from the existence of \(\Gamma\):

- monotonicity of \(F\);
- dominance exchange;
- existence of precedence-respecting optima;
- correctness of dominance propagation.

The additive-update identity, or a weaker explicitly stated marginal-update condition, is required.

For COF v0.1 the additive structure is adopted because it is exact for the motivating Fourier realization and gives a clean dependency boundary.

---

## 4. Monotonicity theorem

### Theorem 4.1

Suppose

\[
\Gamma(i,t)\ge0
\]

for all \(i\in I\) and \(t\in T\). If \(S\subseteq U\), then

\[
L_S(t)\le L_U(t)
\]

for every target \(t\), and consequently

\[
F(S)\le F(U).
\]

### Proof

Since \(S\subseteq U\),

\[
L_U(t)-L_S(t)
=
\sum_{i\in U\setminus S}\Gamma(i,t)
\ge0.
\]

Thus every target certified by \(S\) remains certified by \(U\). Hence \(F(S)\le F(U)\). \(\square\)

### Dependency

- finite item and target sets;
- additive-update identity;
- coordinatewise nonnegativity of contributions;
- no budget assumption;
- no Fourier or PVG assumption.

---

## 5. Dominance and exchange

### Definition 5.1

An item \(i\) **dominates** an item \(j\), written

\[
i\succeq j,
\]

when

\[
\Gamma(i,t)\ge\Gamma(j,t)
\]

for every \(t\in T\).

### Theorem 5.2 — Exchange theorem

Let \(S\subseteq I\), with \(j\in S\) and \(i\notin S\). If \(i\succeq j\), define

\[
S'=(S\setminus\{j\})\cup\{i\}.
\]

Then

\[
L_{S'}(t)\ge L_S(t)
\]

for every \(t\in T\), and therefore

\[
F(S')\ge F(S).
\]

### Proof

For every target \(t\),

\[
L_{S'}(t)-L_S(t)
=
\Gamma(i,t)-\Gamma(j,t)
\ge0.
\]

The certification set cannot shrink, proving the claim. \(\square\)

### Important refinement

The exchange theorem does **not** require all contributions to be nonnegative. It only requires coordinatewise dominance of the exchanged pair. Therefore:

- global monotonicity uses nonnegativity;
- pairwise exchange uses only pairwise dominance.

This separates two assumptions that were previously easy to conflate.

---

## 6. Canonical optimal configurations

Assume a cardinality budget \(B\). Orient exact-equality classes by a fixed acyclic tie-breaking order, and take the transitive closure of strict dominance together with the oriented equalities.

A configuration \(S\) is **canonical** when

\[
j\in S\text{ and }i\succeq j
\quad\Longrightarrow\quad
i\in S
\]

for every directed precedence relation used by the canonicalization.

### Theorem 6.1

For every feasible configuration \(S\) there exists a canonical feasible configuration \(S^*\) such that

\[
|S^*|=|S|
\qquad\text{and}\qquad
F(S^*)\ge F(S).
\]

Consequently, at least one optimal solution is canonical.

### Proof sketch

Whenever a precedence violation occurs, replace the dominated selected item by an unselected dominator. The exchange theorem does not decrease \(F\), and cardinality is preserved. An acyclic orientation supplies a strictly decreasing finite rank measure on violations, so the process terminates. \(\square\)

### Limitation

This theorem proves the existence of a canonical optimum. It does not say that every optimum is canonical, and it does not justify deleting dominated items from the universe.

---

## 7. No-elimination boundary

Dominance gives a replacement rule, not a global elimination rule.

A dominated item may still be jointly useful with its dominator under a budget greater than one. Therefore the valid logical implication is

\[
j\in S\Longrightarrow i\in S
\]

for a chosen canonical optimum, not

\[
j\notin I.
\]

The Fourier instance \((N,r,q,B)=(15,12,6,2)\) supplies an explicit realization in which frequency \(2\) dominates frequency \(1\), yet the pair \(\{1,2\}\) certifies more targets than \(\{2\}\). The example belongs to the application layer; the logical boundary is abstract.

---

## 8. Exact Fourier realization

For the reduced Fourier certificate problem, define

\[
\beta(c)
=
\frac{R_\Lambda(N)}q+P_{\mathrm{Nyq}}(c)
-
\sum_k|P_k(c)|,
\]

and

\[
\Gamma(k,c)=G_k(c)=P_k(c)+|P_k(c)|\ge0.
\]

Then

\[
L_S(c)
=
\beta(c)+\sum_{k\in S}\Gamma(k,c),
\]

which is precisely an additive certificate structure.

The target threshold is

\[
\Theta(c)=C_{\mathrm{hpp}}(c).
\]

Thus the Fourier/PVG problem is an exact realization of COF v0.1, not merely an analogy.

---

## 9. Dependency matrix v0.1

| Result | Additive update | Nonnegative contributions | Pairwise dominance | Cardinality budget | Fourier/PVG |
|---|:---:|:---:|:---:|:---:|:---:|
| Target certification definition | yes | no | no | no | no |
| Monotonicity of \(L_S\) and \(F\) | yes | yes | no | no | no |
| Exchange theorem | yes | no | yes | no | no |
| Canonical optimum existence | yes | no | yes | yes for feasibility preservation | no |
| No-elimination warning | yes | no | yes | contextual | application gives explicit witness |
| Fourier realization | yes | yes | optional | yes in optimizer | yes |

---

## 10. Scope of the abstraction

COF v0.1 deliberately studies additive certificate structures. More general state-dependent marginal gains

\[
\Delta_i(S,t)=L_{S\cup\{i\}}(t)-L_S(t)
\]

may support weaker variants of the theory, but they require new assumptions:

- nonnegative marginals for monotonicity;
- exchange-compatible marginal dominance for replacement;
- additional consistency conditions for transitive precedence.

Those extensions are research directions, not claims of this foundational unit.

---

## 11. Honest classification

Established here:

1. a precise abstract object matching the existing Fourier optimizer;
2. an exact update identity linking contributions and certificate bounds;
3. abstract monotonicity and exchange theorems;
4. existence of canonical optima under acyclic precedence orientation;
5. a clean separation between monotonicity, exchange, and elimination.

Not established here:

1. novelty relative to all optimization literature;
2. transferability to a second independent application;
3. polynomial-time solvability;
4. a general theory for arbitrary set functionals or arbitrary constraints;
5. any progress on Goldbach, RH, or GRH.
