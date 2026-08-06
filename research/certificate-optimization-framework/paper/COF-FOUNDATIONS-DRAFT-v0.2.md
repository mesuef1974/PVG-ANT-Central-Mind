# Certificate Optimization Framework: Additive Structures, Exact Search, and Minimal Obstructions

## Draft v0.2 — proof-audited manuscript

### Abstract

We introduce a finite framework for optimization problems in which a constrained set of objects is selected to maximize the number of targets receiving rigorous certificates. The framework separates the certificate functional from the search machinery and distinguishes actual simultaneous certification from compatibility relaxations used only for upper bounds. For additive certificate structures we prove monotonicity under nonnegative contributions, a feasibility-preserving dominance-exchange theorem that does not require nonnegativity, and existence of precedence-legal optima under an acyclic terminating exchange system. Independently of additivity, we formulate exact finite Branch-and-Bound through comprehensive branching and admissible node bounds. Under exact cardinality constraints we derive coordinatewise upper bounds that remain valid for signed contributions. Sound mandatory object sets generate pairwise and higher-order target-compatibility relaxations. Inclusion-minimal forbidden target families form an antichain that exactly compresses the mandatory-set relaxation. The framework is realized by a Fourier frequency-retention problem arising from prime-valuation addition fibers. This paper establishes a framework and one documented realization; it does not claim broad transferability, polynomial-time algorithms, or progress on Goldbach's conjecture, RH, or GRH.

---

## 1. Introduction

Many rigorous computational arguments have a common architecture. A finite collection of objects may be retained, measured, or activated. Each selected object changes certified lower bounds attached to a finite family of targets. A target is counted only when its lower bound crosses an independently justified threshold. The optimization problem is to choose an admissible configuration that certifies as many targets as possible.

The motivating case comes from a Fourier decomposition of prime-valuation addition-fiber observables. The selectable objects are reduced Fourier frequencies, the targets are reduced residue channels, and certification requires a retained-frequency lower bound to dominate a separately bounded higher-prime-power contamination term. During the exact-search development of that application, several results emerged that do not depend on prime valuations, Fourier analysis, or additive number theory: dominance exchange, precedence propagation, admissible Branch-and-Bound, mandatory-set compatibility, and minimal forbidden obstructions.

The purpose of this paper is to isolate those results under explicit hypotheses. The abstraction is deliberately conservative. We do not assert that every certificate-selection problem fits the model. We also do not identify mandatory compatibility with actual simultaneous certification. Mandatory compatibility is a necessary relaxation used to derive safe upper bounds.

### 1.1 Contributions

The paper provides:

1. a finite certificate-optimization structure and its additive subclass;
2. monotonicity and feasibility-preserving dominance exchange;
3. precedence-legal optimal configurations under an acyclic terminating exchange system;
4. exact finite Branch-and-Bound based only on comprehensive branching and admissible upper bounds;
5. coordinatewise upper bounds under exact or at-most cardinality constraints;
6. sound mandatory sets and precedence-closed mandatory requirements;
7. pairwise and higher-order target-compatibility relaxations;
8. an inclusion-minimal obstruction theorem and exact antichain compression of the mandatory-set relaxation;
9. a Fourier realization arising from prime-valuation addition fibers;
10. a dependency and evidence protocol separating abstract, Fourier, arithmetic, and computational layers.

### 1.2 Scientific boundary

The present work contains one substantial realization. A broad transferability claim requires a second independent application and is not made here. No polynomial-time complexity result or uniform speedup is claimed. The arithmetic realization does not prove Goldbach's conjecture and gives no RH/GRH progress.

---

## 2. Certificate Optimization Structures

### Definition 2.1 (finite certificate optimization structure)

A finite certificate optimization structure is a tuple

\[
\mathfrak C=(I,T,\mathcal A,L,\Theta),
\]

where:

- `I` is a finite object set;
- `T` is a finite target set;
- `\mathcal A\subseteq 2^I` is the family of admissible configurations;
- `L_S(t)\in\mathbb R` is the certified lower-bound value for `S\in\mathcal A` and `t\in T`;
- `\Theta:T\to\mathbb R` is the threshold map.

A target `t` is certified by `S` when

\[
L_S(t)>\Theta(t).
\]

The objective is

\[
F(S)=\left|\{t\in T:L_S(t)>\Theta(t)\}\right|,
\]

and the optimization problem is

\[
\max_{S\in\mathcal A}F(S).
\]

### Definition 2.2 (additive certificate structure)

The structure is additive if there are maps

\[
\beta:T\to\mathbb R,
\qquad
\Gamma:I\times T\to\mathbb R
\]

such that

\[
L_S(t)=\beta(t)+\sum_{i\in S}\Gamma(i,t).
\]

Hence, for `i\notin S`,

\[
L_{S\cup\{i\}}(t)-L_S(t)=\Gamma(i,t).
\]

Nonnegativity,

\[
\Gamma(i,t)\ge0,
\]

is an optional property and is not part of the definition.

---

## 3. Monotonicity, Dominance, and Canonical Optima

### Theorem 3.1 (monotonicity)

If the additive structure satisfies `\Gamma(i,t)\ge0` for all objects and targets, then

\[
S\subseteq U
\quad\Longrightarrow\quad
L_S(t)\le L_U(t)
\]

for every target, and consequently

\[
F(S)\le F(U).
\]

### Definition 3.2 (componentwise dominance)

For `i,j\in I`, write

\[
i\succeq j
\]

when

\[
\Gamma(i,t)\ge\Gamma(j,t)
\]

for every target `t`.

### Theorem 3.3 (feasibility-preserving dominance exchange)

Let `S\in\mathcal A`, let `j\in S`, `i\notin S`, and suppose `i\succeq j`. If

\[
S'=(S\setminus\{j\})\cup\{i\}
\]

also belongs to `\mathcal A`, then

\[
L_{S'}(t)\ge L_S(t)
\]

for every target, and therefore

\[
F(S')\ge F(S).
\]

#### Proof

For each target,

\[
L_{S'}(t)-L_S(t)=\Gamma(i,t)-\Gamma(j,t)\ge0.
\]

The objective comparison follows by preservation of strict threshold crossings. Nonnegativity of all contributions is not required. ∎

### Definition 3.4 (precedence exchange system)

A precedence exchange system consists of:

1. an acyclic directed relation on objects;
2. a rank map `\rho:I\to\{1,\ldots,|I|\}` strictly monotone along directed edges;
3. the rule that if an admissible configuration contains a required child but omits its parent, the one-for-one parent-for-child exchange remains admissible;
4. componentwise dominance of each parent over the child it replaces.

A configuration is legal when it contains every required ancestor of each selected object.

### Theorem 3.5 (existence of a precedence-legal optimum)

Every optimum in a finite precedence exchange system can be transformed into a legal optimum by finitely many feasibility-preserving dominance exchanges.

#### Proof

Start from an optimal configuration. Whenever it violates precedence, replace a violating child by a required parent. The exchange preserves admissibility and does not decrease the objective by Theorem 3.3. The rank potential

\[
\Phi(S)=\sum_{i\in S}\rho(i)
\]

changes strictly in the chosen acyclic direction at every repair. Since only finitely many configurations exist, the process terminates. The terminal configuration is legal and has objective at least the original optimum, hence is itself optimal. ∎

### Boundary 3.6 (dominance is not deletion)

Dominance does not permit unconditional deletion of the dominated object from the ground set. An optimum may contain both objects. The valid conclusion is an exchange or precedence rule under preserved feasibility.

---

## 4. Exact Finite Branch-and-Bound

### Definition 4.1 (node and completion family)

A search node `\nu` represents a finite family `\mathcal C(\nu)` of feasible completions. Let `F_{\mathrm{inc}}` be the best objective value already found.

### Definition 4.2 (admissible upper bound)

A node function `U(\nu)` is admissible if

\[
F(Q)\le U(\nu)
\]

for every completion `Q\in\mathcal C(\nu)`.

### Theorem 4.3 (safe pruning)

If

\[
U(\nu)\le F_{\mathrm{inc}},
\]

then pruning node `\nu` cannot remove a strictly better solution.

### Theorem 4.4 (exactness of finite Branch-and-Bound)

A finite Branch-and-Bound procedure returns the exact optimum if:

1. every feasible configuration is represented by a root-to-leaf path unless safely pruned;
2. terminal feasible configurations are evaluated exactly;
3. every pruning bound is admissible.

This theorem is independent of additivity, nonnegativity, dominance, Fourier analysis, and PVG.

---

## 5. Coordinatewise Bounds Under Cardinality Constraints

At a node let `S` be selected, `R` undecided, and let the completion select exactly `b` objects from `R`.

### Definition 5.1 (exact-b top sum)

For a target `t`, let `M_b(t;R)` be the sum of the `b` largest values in

\[
\{\Gamma(i,t):i\in R\}.
\]

### Theorem 5.2 (signed exact-cardinality upper bound)

For every residual `b`-set `Q\subseteq R`,

\[
\sum_{i\in Q}\Gamma(i,t)\le M_b(t;R).
\]

Therefore

\[
U_{\mathrm{coord}}(\nu)
=
\left|
\left\{
 t:
 L_S(t)+M_b(t;R)>\Theta(t)
\right\}
\right|
\]

is an admissible upper bound.

No sign condition on `\Gamma` is required.

### Corollary 5.3 (at-most-b budget)

If a completion may choose at most `b` objects, define

\[
M_{\le b}(t;R)
=
\max_{0\le k\le b}M_k(t;R).
\]

Replacing `M_b` by `M_{\le b}` gives an admissible bound. Under nonnegative contributions, `M_{\le b}=M_b` whenever at least `b` objects remain.

### Remark 5.4

The bound is targetwise optimistic: different targets may use different hypothetical top sets. This is safe but can be loose.

---

## 6. Precedence Propagation

For each object `j`, let `A(j)` be its transitive required-ancestor set, and let `D(i)` be the set of descendants requiring `i`.

At a node with selected set `S` and excluded set `X`, define the propagated closures

\[
S^+=S\cup\bigcup_{j\in S}A(j),
\]

\[
X^+=X\cup\bigcup_{i\in X}D(i).
\]

A node is infeasible when:

- `S^+\cap X^+\ne\varnothing`;
- the selected closure exceeds the budget;
- too few undecided objects remain to complete an exact budget.

By Theorem 3.5, restricting exact search to legal configurations preserves at least one optimum.

---

## 7. Mandatory Sets

### Definition 7.1 (sound mandatory set)

At node `\nu`, a set `M_\nu(t)` is mandatory for target `t` if every feasible completion certifying `t` contains `M_\nu(t)`.

If a completion certifies every target in `A\subseteq T`, it contains

\[
M_\nu(A)=\bigcup_{t\in A}M_\nu(t).
\]

### Theorem 7.2 (leave-one-out mandatory test, exact budget)

Suppose the residual completion must choose exactly `b` objects from `R`. If, for `i\in R`,

\[
L_S(t)+M_b(t;R\setminus\{i\})\le\Theta(t),
\]

then every completion certifying `t` must include `i`.

#### Proof

Any exact-`b` completion omitting `i` is a `b`-subset of `R\setminus\{i\}`. Its contribution is at most the corresponding top-`b` sum and therefore cannot cross the threshold. ∎

For an at-most-`b` budget, use `M_{\le b}` instead.

### Proposition 7.3 (precedence closure)

If every legal completion containing `i` must also contain `A(i)`, then

\[
\overline M_\nu(t)
=
\bigcup_{i\in M_\nu(t)}(A(i)\cup\{i\})
\]

is also mandatory.

Mandatory-set detection is necessary, not sufficient: containing all detected mandatory objects does not by itself guarantee certification.

---

## 8. Compatibility Graphs and Hypergraphs

Let `\mathcal R_\nu\subseteq2^I` be a downward-closed residual resource family containing every feasible residual selection.

### Definition 8.1 (mandatory compatibility)

A target family `A\subseteq T` is mandatory-compatible when

\[
M_\nu(A)\in\mathcal R_\nu.
\]

### Theorem 8.2 (necessity of mandatory compatibility)

Every simultaneously certifiable target family is mandatory-compatible.

#### Proof

If a feasible residual selection `Q` certifies `A`, then `M_\nu(A)\subseteq Q` by mandatory soundness. Since `Q\in\mathcal R_\nu` and the resource family is downward closed, `M_\nu(A)\in\mathcal R_\nu`. ∎

The converse is not asserted.

### Corollary 8.3 (mandatory-union upper bound)

Define

\[
U_{\mathrm{mand}}(\nu)
=
\max\{|A|:M_\nu(A)\in\mathcal R_\nu\}.
\]

Then `U_{\mathrm{mand}}` is admissible for the original certification problem.

It is exact for the mandatory-compatibility relaxation, not necessarily for actual simultaneous certification.

### Definition 8.4 (pairwise compatibility graph)

Vertices are individually possible targets. Two vertices are adjacent when their mandatory union belongs to `\mathcal R_\nu`.

Every actually certifiable target family is a clique. Hence

\[
|A|\le\omega(G)\le\chi(G)\le k
\]

for any proper coloring using `k` colors. Pairwise compatibility may miss higher-order conflicts.

### Definition 8.5 (mandatory-conflict hypergraph)

A target family `E` is forbidden when

\[
M_\nu(E)\notin\mathcal R_\nu.
\]

The hypergraph of forbidden families represents the full mandatory-union relaxation.

---

## 9. Minimal Forbidden Obstructions

A forbidden family `E` is inclusion-minimal if every proper subset is mandatory-compatible. Let `\mathcal F_{\min}(\nu)` be the family of all minimal forbidden obstructions.

### Theorem 9.1 (minimal-obstruction characterization)

A target family `A` is mandatory-compatible if and only if it contains no member of `\mathcal F_{\min}(\nu)`.

#### Proof

If `A` contains a minimal forbidden family `E`, downward closure of compatibility implies `A` is forbidden. Conversely, if `A` is forbidden, finiteness permits choosing an inclusion-minimal forbidden subset `E\subseteq A`. Then `E\in\mathcal F_{\min}(\nu)`. ∎

Every forbidden family contains at least one minimal obstruction. It need not contain a unique one.

### Corollary 9.2 (exact antichain compression)

The feasible families defined by all forbidden sets are exactly those defined by the minimal antichain. Therefore

\[
U_{\min}(\nu)=U_{\mathrm{mand}}(\nu).
\]

Each minimal obstruction gives a valid relaxation cut

\[
\sum_{t\in E}x_t\le |E|-1.
\]

The compression is exact as a representation of the mandatory-set relaxation. Extracting the full antichain may still require exponential work.

---

## 10. Fourier Certificate Realization

In the motivating realization, the objects are retained reduced Fourier frequencies and the targets are reduced residue channels. The lower bound has the additive form

\[
L_S(c)=\beta(c)+\sum_{k\in S}G_k(c),
\]

where

\[
G_k(c)=P_k(c)+|P_k(c)|\ge0,
\]

and

\[
\beta(c)
=
\frac{R_\Lambda(N)}q
+P_{\mathrm{Nyq}}(c)
-\sum_k|P_k(c)|.
\]

Thus this realization satisfies both additivity and nonnegativity. Frequency dominance induces precedence. Exact-budget frequency retention realizes the cardinality-constrained search model. Leave-one-out channel margin tests generate mandatory frequency sets; precedence closure then generates graph, hypergraph, and minimal-obstruction relaxations.

---

## 11. Prime-Valuation Addition-Fiber Application

The arithmetic realization begins with prime-valuation addition fibers and von Mangoldt observables. Reduced residue channels admit an exact finite Fourier decomposition after effective-period reduction. A retained-frequency lower bound is compared with an independently bounded higher-prime-power contamination term. The COF layer then selects frequencies while preserving exact finite-search certification.

The implementation was checked on a stated finite benchmark against exhaustive frequency selection, with zero optimum mismatches and zero false prime-pair certificates in the recorded runs. These computations validate the implementation only on that finite range; they do not prove an asymptotic statement or an open conjecture.

---

## 12. Dependency and Evidence Protocol

Every theorem is classified by whether it requires:

- finite certificate language;
- additive representation;
- nonnegative contributions;
- feasibility-preserving exchange;
- componentwise dominance;
- acyclic precedence and rank termination;
- exact or at-most cardinality budget;
- an admissible upper bound;
- sound mandatory sets;
- a downward-closed resource family;
- Fourier input;
- PVG/arithmetic input.

The proof layer and executable layer remain separate. Executable verifiers may validate exhaustive-optimum agreement, bound behavior on tested nodes, precedence consistency, minimality and coverage of obstructions, and false-certificate counts. They do not substitute for the abstract proofs.

### 12.1 Foundation sources

- `theory/COF-ADDITIVE-CERTIFICATE-STRUCTURE-v0.1.md`
- `theory/COF-EXACT-BRANCH-AND-BOUND-AND-PRECEDENCE-v0.1.md`
- `theory/COF-MANDATORY-CLOSURES-AND-MINIMAL-OBSTRUCTIONS-v0.1.md`
- `governance/COF-THEOREM-DEPENDENCY-MATRIX-v0.1.md`
- `governance/COF-PAPER-PROOF-AUDIT-v0.1.md`

### 12.2 Realization sources

The Fourier/PVG realization is documented under:

- `research/avrg-axis-sum/theory/`
- `research/avrg-axis-sum/governance/ACTIVE-003-K` through `ACTIVE-003-S`;
- corresponding executable verifiers and JSON result receipts under `research/avrg-axis-sum/code/` and `results/`.

---

## 13. Limitations and Open Directions

The current framework has one substantial realization. The principal next test is transferability to an independent problem that does not use prime valuations or Fourier number theory.

Other research directions include:

- weighted target objectives;
- non-cardinality downward-closed resource systems;
- stronger mandatory-set extraction;
- dynamically generated obstruction cuts;
- complexity classifications for restricted incidence structures;
- approximation guarantees when exact hypergraph optimization is too expensive;
- formal verification of the finite core theorems.

These are directions, not established results of this version.

---

## 14. Conclusion

Certificate optimization separates naturally into a proof layer and a search layer. The proof layer defines sound lower bounds and thresholds. The search layer exploits monotonicity, feasibility-preserving dominance, admissible upper bounds, mandatory requirements, and minimal obstructions without changing what counts as a certificate.

The abstract results are finite and exact under their stated assumptions. The Fourier/PVG realization demonstrates that the framework organizes a nontrivial arithmetic certification problem. Broader claims await an independent transfer study.
