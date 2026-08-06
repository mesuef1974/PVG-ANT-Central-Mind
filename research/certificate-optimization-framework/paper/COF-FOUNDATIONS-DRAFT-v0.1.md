# Certificate Optimization Framework: Additive Structures, Exact Search, and Minimal Obstructions

## Draft v0.1

### Abstract

We introduce a finite mathematical framework for optimization problems in which one selects a constrained set of objects in order to maximize the number of targets that receive rigorous certificates. The framework separates four layers that are often conflated: the certificate functional, structural dominance, exact search, and target-compatibility relaxations. For additive certificate structures we prove monotonicity under nonnegative contributions, a dominance-exchange theorem that does not require nonnegativity, and the existence of precedence-legal optimal solutions. Independently of additivity, we formulate exact finite Branch-and-Bound through admissible node upper bounds. We then introduce sound mandatory sets for targets and derive graph and hypergraph upper bounds from their joint resource requirements. Inclusion-minimal forbidden target families form an antichain that exactly compresses the mandatory-set relaxation. The framework is realized by a Fourier frequency-retention problem arising from prime-valuation addition fibers. That realization motivates the theory but is not required by its abstract proofs. The present work establishes a framework and one documented realization; it does not claim a universal optimization theory, polynomial-time algorithms, or progress on Goldbach's conjecture, RH, or GRH.

---

## 1. Introduction

Many rigorous computational arguments share the same hidden architecture. A finite collection of objects may be retained, measured, or activated. Each selected object changes a family of certified lower bounds. A target is counted only when its lower bound crosses an independently justified threshold. The optimization problem is to choose a constrained configuration that certifies as many targets as possible.

The motivating case for this paper comes from a Fourier decomposition of prime-valuation addition-fiber observables. There, the selectable objects are reduced Fourier frequencies, the targets are reduced residue channels, and certification requires a retained-frequency lower bound to dominate a separately bounded higher-prime-power contamination term. During the exact-search development of that application, several results emerged that do not depend on prime valuations, Fourier analysis, or additive number theory. These include dominance exchange, precedence propagation, admissible Branch-and-Bound, mandatory-set compatibility, and minimal forbidden obstructions.

The purpose of this paper is to isolate those results in a precise framework. The abstraction is deliberately conservative. We do not assert that every certificate-selection problem fits the model, nor that mandatory-set compatibility characterizes actual simultaneous certification. Instead, we identify exact assumptions for each theorem and distinguish the original certification problem from the relaxations used to bound it.

### 1.1 Contributions

The paper provides:

1. a finite certificate-optimization structure and an additive realization;
2. monotonicity and dominance-exchange theorems with minimal assumptions;
3. precedence-legal canonical optima without deleting dominated objects;
4. a formulation of exact finite Branch-and-Bound requiring only comprehensive branching and admissible upper bounds;
5. additive coordinatewise upper bounds under a cardinality budget;
6. sound mandatory sets and precedence-closed mandatory requirements;
7. pairwise and higher-order target-compatibility relaxations;
8. an inclusion-minimal obstruction theorem and exact antichain compression of the mandatory-set relaxation;
9. a realization through Fourier certificates for prime-valuation addition fibers;
10. a theorem-dependency map separating abstract, Fourier, and arithmetic assumptions.

### 1.2 Scientific boundary

The present paper establishes a framework with one substantial realization. A claim of broad transferability requires a second independent application and is therefore deferred. No polynomial-time complexity result or uniform speedup is claimed. The arithmetic application does not prove Goldbach's conjecture and gives no RH/GRH progress.

---

## 2. Certificate Optimization Structures

### 2.1 Basic data

A finite certificate optimization structure consists of:

- a finite object set \(I\);
- a finite target set \(T\);
- a family \(\mathcal A\subseteq 2^I\) of admissible configurations;
- certificate lower bounds \(L_S(t)\in\mathbb R\) for \(S\in\mathcal A\), \(t\in T\);
- thresholds \(\Theta(t)\in\mathbb R\).

A target \(t\) is certified by \(S\) when

\[
L_S(t)>\Theta(t).
\]

The objective is

\[
F(S)=\left|\{t\in T:L_S(t)>\Theta(t)\}\right|.
\]

The optimization problem is

\[
\max_{S\in\mathcal A}F(S).
\]

### 2.2 Additive certificate structures

An additive certificate structure has a baseline \(\beta:T\to\mathbb R\) and contribution map

\[
\Gamma:I\times T\to\mathbb R
\]

such that

\[
L_S(t)=\beta(t)+\sum_{i\in S}\Gamma(i,t).
\]

The exact update identity is

\[
L_{S\cup\{i\}}(t)-L_S(t)=\Gamma(i,t)
\]

whenever \(i\notin S\).

Nonnegativity is an optional property:

\[
\Gamma(i,t)\ge0.
\]

It is not part of the definition.

---

## 3. Monotonicity, Dominance, and Exchange

### Theorem 3.1 (monotonicity)

If \(\Gamma(i,t)\ge0\) for every \(i,t\), then

\[
S\subseteq U
\quad\Longrightarrow\quad
L_S(t)\le L_U(t)
\]

for every target, and consequently

\[
F(S)\le F(U).
\]

### Definition 3.2 (dominance)

For objects \(i,j\in I\), write

\[
i\succeq j
\]

when

\[
\Gamma(i,t)\ge\Gamma(j,t)
\]

for every target \(t\).

### Theorem 3.3 (dominance exchange)

Let \(S\) contain \(j\) but not \(i\), and suppose \(i\succeq j\). Then

\[
S'=(S\setminus\{j\})\cup\{i\}
\]

satisfies

\[
L_{S'}(t)\ge L_S(t)
\]

for every target, hence

\[
F(S')\ge F(S).
\]

This theorem does not require nonnegative contributions.

### 3.4 Precedence orientation and legal optima

Choose an acyclic orientation of dominance and tie relations. A configuration is precedence-legal when inclusion of a descendant implies inclusion of all required ancestors, subject to equal-cardinality exchange.

Under an admissible family preserved by these exchanges, repeated replacement yields a precedence-legal optimal configuration.

### 3.5 Boundary: dominance is not deletion

Dominance does not imply that the dominated object can be removed from the ground set. An optimum may require both a dominant and a dominated object when the budget exceeds one or when their combined contribution is useful. The valid consequence is an exchange or precedence rule, not unconditional deletion.

---

## 4. Exact Finite Branch-and-Bound

### 4.1 Node model

A search node \(\nu\) represents a family \(\mathcal C(\nu)\) of feasible completions. Let \(F_{\mathrm{inc}}\) be the best certified-target count already found.

### Definition 4.1 (admissible upper bound)

A node function \(U(\nu)\) is admissible when

\[
F(Q)\le U(\nu)
\]

for every completion \(Q\in\mathcal C(\nu)\).

### Theorem 4.2 (safe pruning)

If

\[
U(\nu)\le F_{\mathrm{inc}},
\]

then pruning node \(\nu\) cannot remove a strictly better solution.

### Theorem 4.3 (exactness)

A finite Branch-and-Bound procedure returns the exact optimum if:

1. every feasible configuration is represented by some root-to-leaf path unless safely pruned;
2. terminal feasible configurations are evaluated exactly;
3. every pruning bound is admissible.

This theorem is independent of additivity, nonnegativity, dominance, and the motivating application.

---

## 5. Additive Upper Bounds Under a Cardinality Budget

At a node let \(S\) be selected, \(R\) undecided, and \(b\) the residual number of objects to select. Under nonnegative additive contributions, let \(M_b(t;R)\) be the sum of the \(b\) largest values among \(\{\Gamma(i,t):i\in R\}\), with the natural convention when fewer than \(b\) objects remain.

Define

\[
U_{\mathrm{coord}}(\nu)
=
\left|\left\{t:
L_S(t)+M_b(t;R)>\Theta(t)
\right\}\right|.
\]

Every completion can add at most \(M_b(t;R)\) to target \(t\), so \(U_{\mathrm{coord}}\) is admissible.

The bound is targetwise optimistic: different targets may use different hypothetical top-\(b\) object sets. This is safe but can be loose.

---

## 6. Precedence Propagation

For each object \(j\), let \(A(j)\) denote its transitive precedence ancestors. Inclusion of \(j\) forces inclusion of \(A(j)\). Exclusion of an ancestor forces exclusion of every descendant requiring it.

The propagated selected and excluded sets are obtained by transitive closure. A node is infeasible if these closures intersect, violate the cardinality budget, or leave too few objects to complete the exact budget.

Precedence-aware search remains exact because the exchange theorem guarantees at least one optimal legal solution.

---

## 7. Mandatory Sets

### Definition 7.1

At node \(\nu\), a set \(M_\nu(t)\) is mandatory for target \(t\) when every completion certifying \(t\) contains \(M_\nu(t)\).

If a completion certifies all targets in \(A\subseteq T\), it must contain

\[
M_\nu(A)=\bigcup_{t\in A}M_\nu(t).
\]

### 7.2 Construction in additive COF

Under a residual cardinality budget \(b\), object \(i\in R\) is mandatory for target \(t\) if the best targetwise completion available after forbidding \(i\) still fails:

\[
L_S(t)
+
\sum_{j\in\operatorname{Top}_b(R\setminus\{i\};t)}
\Gamma(j,t)
\le
\Theta(t).
\]

Sound precedence closure may then be applied to the resulting set.

The construction is necessary, not sufficient: containing all detected mandatory objects does not by itself guarantee certification.

---

## 8. Compatibility Graphs and Hypergraphs

Let \(\mathcal R_\nu\subseteq2^I\) be a downward-closed resource family containing every feasible residual selection. A target family \(A\) is mandatory-compatible when

\[
M_\nu(A)\in\mathcal R_\nu.
\]

Every simultaneously certifiable family is mandatory-compatible.

Define

\[
U_{\mathrm{mand}}(\nu)
=
\max\{|A|:M_\nu(A)\in\mathcal R_\nu\}.
\]

Then \(U_{\mathrm{mand}}\) is an admissible upper bound.

Pairwise mandatory compatibility yields a graph. Every actually certifiable target family is a clique, so any proper-coloring count is a safe upper bound. Pairwise compatibility may miss higher-order resource conflicts.

The full mandatory-union relaxation is represented by a hypergraph whose forbidden edges are target families \(E\) satisfying

\[
M_\nu(E)\notin\mathcal R_\nu.
\]

The resulting bound is exact for this relaxation, but not necessarily for actual certification.

---

## 9. Minimal Forbidden Obstructions

A forbidden family \(E\) is inclusion-minimal if every proper subset is mandatory-compatible. Let \(\mathcal F_{\min}(\nu)\) be the family of all such obstructions.

### Theorem 9.1

A target family \(A\) is mandatory-compatible if and only if it contains no member of \(\mathcal F_{\min}(\nu)\).

Every finite forbidden family contains at least one minimal forbidden obstruction. It need not contain a unique one.

### Corollary 9.2

The maximum target-family size obtained from all forbidden families equals that obtained from the minimal antichain alone:

\[
U_{\min}(\nu)=U_{\mathrm{mand}}(\nu).
\]

Each minimal obstruction gives a valid cut

\[
\sum_{t\in E}x_t\le |E|-1.
\]

The compression is exact as a representation of the mandatory-set relaxation. Its extraction may still be exponential.

---

## 10. Fourier Certificate Realization

In the motivating realization, objects are retained reduced Fourier frequencies and targets are reduced residue channels. The certified lower bound can be written

\[
L_S(c)=\beta(c)+\sum_{k\in S}G_k(c),
\]

where

\[
G_k(c)=P_k(c)+|P_k(c)|\ge0.
\]

The baseline is

\[
\beta(c)
=
\frac{R_\Lambda(N)}{q}
+P_{\mathrm{Nyq}}(c)
-
\sum_k|P_k(c)|.
\]

Thus the Fourier problem realizes the additive nonnegative COF hypotheses. Frequency dominance induces precedence. Exact-budget frequency selection realizes the cardinality-constrained search model. Channel margin tests generate mandatory frequency sets; their precedence closures generate the compatibility graph, higher-order hypergraph, and minimal obstruction antichain.

All arithmetic thresholds, Fourier identities, and contamination estimates must be proved independently in the realization layer. COF does not supply them.

---

## 11. Prime-Valuation Addition-Fiber Application

The arithmetic application begins with prime-valuation addition fibers and associated von Mangoldt observables. Reduced residue channels admit an exact finite Fourier decomposition after the effective-period reduction. A retained-frequency lower bound is compared with an independently established higher-prime-power contamination bound. The COF layer then selects retained frequencies while preserving exact finite-search certification.

The application has been exhaustively verified on a finite benchmark against exhaustive frequency selection, with zero optimum mismatches and zero false prime-pair certificates. These computations validate the implementation on the stated finite range; they do not convert the framework into a proof of an asymptotic or open number-theoretic statement.

---

## 12. Dependency and Reproducibility Protocol

Every theorem should record whether it requires:

- only finite certificate language;
- additive representation;
- nonnegative contributions;
- componentwise dominance;
- precedence orientation;
- cardinality budget;
- an admissible bound;
- sound mandatory sets;
- a downward-closed resource family;
- Fourier or PVG input.

Executable verifiers belong to the realization and validation layers. They should check exhaustive-optimum agreement, bound admissibility on visited nodes where feasible, precedence consistency, minimality and coverage of forbidden obstructions, and false-certificate counts against an independently reconstructed arithmetic observable.

---

## 13. Limitations and Open Directions

The current framework has one substantial realization. The principal next test is transferability to an independent problem that does not use prime valuations or Fourier number theory.

Other open directions include:

- weighted target objectives;
- non-cardinality downward-closed resource systems;
- stronger mandatory-set extraction;
- delayed or dynamically generated minimal-obstruction cuts;
- complexity classifications for restricted incidence structures;
- approximation guarantees when exact hypergraph optimization is too expensive;
- formal verification of the finite core theorems.

These are research directions, not established results of the present version.

---

## 14. Conclusion

Certificate optimization separates naturally into a proof layer and a search layer. The proof layer defines sound lower bounds and thresholds. The search layer may then exploit monotonicity, dominance, admissible upper bounds, mandatory requirements, and minimal obstructions without changing what counts as a certificate. This separation is the main structural contribution of the framework.

The abstract results are finite and exact under their stated assumptions. The Fourier/PVG realization demonstrates that the framework can organize a nontrivial arithmetic certification problem. Broader claims await an independent transfer study.
