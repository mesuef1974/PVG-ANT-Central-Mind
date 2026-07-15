# COF-FOUNDATION-003 — Mandatory Closures, Compatibility Hypergraphs, and Minimal Obstructions

## Status

Validated abstract foundation for necessary-set upper bounds and their exact combinatorial compression.

This unit does **not** claim that mandatory-set compatibility is sufficient for simultaneous certification. It gives a safe relaxation and an exact representation of that relaxation.

---

## 1. Search-node model

Let \(I\) be a finite object set, \(T\) a finite target set, and let \(\nu\) be a node of a finite exact-search tree.

Write \(\mathcal C(\nu)\) for the family of feasible completions at \(\nu\). Each completion \(Q\in\mathcal C(\nu)\) determines a selected residual-object set, again denoted \(Q\subseteq I\).

Let

\[
\operatorname{Cert}(Q)\subseteq T
\]

be the targets certified by completion \(Q\).

No additive certificate representation is required in this section.

---

## 2. Mandatory sets

### Definition 2.1 (mandatory set)

For a target \(t\in T\), a set

\[
M_\nu(t)\subseteq I
\]

is **mandatory at node \(\nu\)** when

\[
t\in\operatorname{Cert}(Q)
\quad\Longrightarrow\quad
M_\nu(t)\subseteq Q
\]

for every \(Q\in\mathcal C(\nu)\).

The set need not be sufficient for certification and need not contain every object that is individually necessary. It is any sound necessary-set certificate.

### Lemma 2.2 (joint necessity)

If a completion \(Q\) certifies every target in \(A\subseteq T\), then

\[
\bigcup_{t\in A}M_\nu(t)\subseteq Q.
\]

**Proof.** Apply the defining implication target by target and take unions. ∎

---

## 3. Resource-feasibility relaxation

### Definition 3.1 (node resource family)

Let \(\mathcal R_\nu\subseteq 2^I\) be a downward-closed family such that

\[
Q\in\mathcal C(\nu)
\quad\Longrightarrow\quad
Q\in\mathcal R_\nu.
\]

Downward-closed means

\[
A\subseteq B\in\mathcal R_\nu
\quad\Longrightarrow\quad
A\in\mathcal R_\nu.
\]

Typical exact-budget realization: if \(b\) residual slots remain and excluded objects are unavailable, then

\[
\mathcal R_\nu
=
\{A\subseteq R_\nu: |A|\le b\}.
\]

### Definition 3.2 (mandatory-compatible target family)

A target family \(A\subseteq T\) is **mandatory-compatible** at \(\nu\) when

\[
M_\nu(A)
:=
\bigcup_{t\in A}M_\nu(t)
\in\mathcal R_\nu.
\]

### Theorem 3.3 (necessity of mandatory compatibility)

Every simultaneously certifiable target family is mandatory-compatible.

**Proof.** Suppose \(Q\in\mathcal C(\nu)\) certifies every target in \(A\). By Lemma 2.2,

\[
M_\nu(A)\subseteq Q.
\]

Since \(Q\in\mathcal R_\nu\) and \(\mathcal R_\nu\) is downward-closed, \(M_\nu(A)\in\mathcal R_\nu\). ∎

### Warning 3.4 (necessity is not sufficiency)

In general,

\[
M_\nu(A)\in\mathcal R_\nu
\]

does **not** imply that one completion certifies all targets in \(A\).

Mandatory sets encode necessary resource use, not the full certificate equations. Therefore the compatibility structure below is a relaxation.

---

## 4. Hypergraph upper bound

### Definition 4.1 (forbidden family)

A target family \(E\subseteq T\) is forbidden when

\[
M_\nu(E)\notin\mathcal R_\nu.
\]

Let \(\mathcal H_\nu\) denote the hypergraph whose vertex set is the set of individually possible targets and whose hyperedges are all forbidden families.

### Definition 4.2 (mandatory-compatibility bound)

Define

\[
U_{\mathrm{mand}}(\nu)
=
\max\left\{|A|:
A\subseteq T,
M_\nu(A)\in\mathcal R_\nu
\right\}.
\]

### Theorem 4.3 (admissibility)

For every completion \(Q\in\mathcal C(\nu)\),

\[
|\operatorname{Cert}(Q)|
\le
U_{\mathrm{mand}}(\nu).
\]

Hence \(U_{\mathrm{mand}}\) is an admissible Branch-and-Bound upper bound.

**Proof.** Apply Theorem 3.3 to \(A=\operatorname{Cert}(Q)\). ∎

### Classification

The word **exact** may be used only in the following restricted sense:

> \(U_{\mathrm{mand}}\) is the exact optimum of the mandatory-compatibility relaxation.

It need not equal the largest number of targets actually certifiable by one completion.

---

## 5. Pairwise compatibility graph

Join two targets \(s,t\) when

\[
M_\nu(s)\cup M_\nu(t)
\in\mathcal R_\nu.
\]

Every simultaneously certifiable target family is a clique. Therefore any clique-number upper bound, including the number of colors in any proper coloring, is admissible.

However, pairwise compatibility may fail to detect a forbidden triple or larger family. Consequently,

\[
U_{\mathrm{mand}}
\le
U_{\mathrm{pair}},
\]

where \(U_{\mathrm{pair}}\) is any exact pairwise-clique relaxation bound.

The inequality can be strict.

---

## 6. Minimal forbidden obstructions

### Definition 6.1

A forbidden family \(E\) is **inclusion-minimal** when every proper subset is mandatory-compatible.

Let

\[
\mathcal F_{\min}(\nu)
=
\{E\subseteq T:
E\text{ is inclusion-minimal forbidden}\}.
\]

### Theorem 6.2 (minimal-obstruction theorem)

A target family \(A\subseteq T\) is mandatory-compatible if and only if it contains no member of \(\mathcal F_{\min}(\nu)\).

**Proof.**

If \(E\in\mathcal F_{\min}(\nu)\) and \(E\subseteq A\), then

\[
M_\nu(E)
\subseteq
M_\nu(A).
\]

If \(M_\nu(A)\in\mathcal R_\nu\), downward closure would imply \(M_\nu(E)\in\mathcal R_\nu\), contradicting that \(E\) is forbidden. Thus \(A\) is forbidden.

Conversely, if \(A\) is forbidden, finiteness allows us to choose an inclusion-minimal forbidden subset \(E\subseteq A\). Then \(E\in\mathcal F_{\min}(\nu)\). ∎

### Important correction

An infeasible family contains **at least one** minimal forbidden obstruction. It need not contain a unique one.

### Corollary 6.3 (exact antichain compression)

Define

\[
U_{\min}(\nu)
=
\max\left\{|A|:
\forall E\in\mathcal F_{\min}(\nu),
E\nsubseteq A
\right\}.
\]

Then

\[
\boxed{U_{\min}(\nu)=U_{\mathrm{mand}}(\nu)}.
\]

Thus the antichain of minimal forbidden families is an exact compression of the full forbidden-family description of the relaxation.

---

## 7. Valid 0–1 cuts

For every \(E\in\mathcal F_{\min}(\nu)\), introduce target indicators \(x_t\in\{0,1\}\). The inequality

\[
\sum_{t\in E}x_t
\le
|E|-1
\]

is valid for every actually certifiable target family, because every such family is mandatory-compatible.

These cuts constrain only the upper-bound subproblem. They do not alter the original object-selection feasible region and cannot create a false certificate.

---

## 8. Construction of mandatory sets in additive COF

Suppose COF-FOUNDATION-001 holds:

\[
L_S(t)
=
\beta(t)+\sum_{i\in S}\Gamma(i,t),
\qquad
\Gamma(i,t)\ge0,
\]

and the node has residual pool \(R\) and residual cardinality budget \(b\).

For \(i\in R\), if the best possible completion after forbidding \(i\) still fails target \(t\), namely

\[
L_S(t)
+
\sum_{j\in\operatorname{Top}_b(R\setminus\{i\};t)}
\Gamma(j,t)
\le
\Theta(t),
\]

then every completion certifying \(t\) must include \(i\).

Taking all such objects, followed by sound precedence closure, produces a mandatory set \(M_\nu(t)\).

This construction uses additive COF and nonnegative contributions. The abstract hypergraph and minimal-obstruction theorems do not.

---

## 9. Dependency classification

| Result | Finite targets | Mandatory-set soundness | Downward-closed resource family | Additivity | Nonnegativity | Cardinality budget | Precedence |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| joint necessity | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| admissible mandatory bound | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| pairwise graph bound | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| minimal-obstruction theorem | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ |
| antichain compression | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ |
| top-gain mandatory test | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | optional |
| precedence-closed mandatory sets | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ |

For the minimal-obstruction theorem, mandatory-set soundness is not needed as a purely combinatorial statement about the relaxation; it is needed only to transfer the resulting bound to the original certification problem.

---

## 10. PVG–Fourier realization

In the current application:

- objects are retained reduced Fourier frequencies;
- targets are reduced residue channels;
- \(M_\nu(c)\) is the precedence-closed set of frequencies shown necessary by the channel margin test;
- \(\mathcal R_\nu=\{A\subseteq R:|A|\le b\}\);
- the pairwise graph of ACTIVE-003-Q, higher-order hypergraph of ACTIVE-003-R, and minimal antichain of ACTIVE-003-S are realizations of this abstract construction.

The finite benchmark results remain application-specific evidence. They are not part of the abstract theorem.

---

## 11. Scientific boundary

Established here:

- an abstract necessary-set relaxation;
- an admissible hypergraph upper bound;
- exact minimal-obstruction compression of that relaxation;
- valid target-space cuts;
- a clean separation between abstract combinatorics and additive construction of mandatory sets.

Not established:

- sufficiency of mandatory compatibility for certification;
- polynomial-time extraction or optimization;
- uniform speedup;
- a second independent application;
- a Goldbach proof;
- RH/GRH progress.
