# COF Related-Work Audit 002 — Theorem-Level Comparison

Status: completed preliminary theorem-level audit; external bibliography still incomplete.

## 1. Purpose

This audit compares each central result in `COF-FOUNDATIONS-DRAFT-v0.2` against the closest established optimization families found in a focused search. It is not a priority certificate and does not authorize a novelty claim.

## 2. Literature families identified

### 2.1 Precedence-constrained knapsack

The Precedence-Constrained Knapsack Problem (PCKP) selects items under a capacity constraint while respecting a directed acyclic precedence relation. This establishes that budgeted selection with ancestor closure is a known optimization family.

Representative current primary source:

- V. Dose, F. Furini, M. Locatelli, `Optimal Macroitem Sequences in the Precedence Constrained Knapsack Problem`, arXiv:2606.22018 (2026).

Consequence for COF: precedence DAGs, ancestor closure, and closure-aware density ideas cannot be claimed as new in isolation.

### 2.2 Knapsack cover inequalities and minimal covers

Minimal covers and lifted cover inequalities are classical tools for knapsack and covering formulations. A cover is an inclusion-minimal family whose total load violates a capacity, and its supersets are also forbidden.

Representative primary sources:

- A. Bazzi, S. Fiorini, S. Huang, O. Svensson, `Small Extended Formulation for Knapsack Cover Inequalities from Monotone Circuits`, arXiv:1609.03737.
- W.-K. Chen, Y.-H. Dai, `On the complexity of sequentially lifting cover inequalities for the knapsack polytope`, arXiv:1811.10010.
- C. Hojny, C. Roy, `Computational Aspects of Lifted Cover Inequalities for Knapsacks with Few Different Weights`, arXiv:2412.14919.

Consequence for COF: inclusion-minimal forbidden families, upward closure of infeasibility, and antichain compression are known combinatorial and polyhedral principles.

### 2.3 Conflict analysis in integer programming

Conflict graphs and conflict learning are established inside MIP and MINLP search. They record combinations of decisions that cannot coexist and use those conflicts for propagation or cutting.

Representative primary sources:

- J. Witzig, T. Berthold, S. Heinz, `A Status Report on Conflict Analysis in Mixed Integer Nonlinear Programming`, arXiv:1902.02591.
- G. Mexi, F. Serrano, T. Berthold, A. Gleixner, J. Nordström, `Cut-based Conflict Analysis in Mixed Integer Programming`, arXiv:2410.15110.

Consequence for COF: pairwise conflict graphs, higher-order no-good constraints, propagation from infeasible combinations, and conflict-informed search are known ideas.

### 2.4 Maximum coverage and threshold coverage

Budgeted selection that maximizes the number of covered targets is close to maximum coverage. COF differs because a target may require accumulated weighted contribution to cross an individual threshold rather than being covered by one selected set.

The nearest safe classification is therefore:

- maximum coverage: known special case when contributions are binary and threshold one;
- weighted threshold activation: known modeling pattern;
- COF packaging: project-specific synthesis until a closer named precedent is found.

## 3. Theorem-by-theorem comparison

### Definition 2.1 — finite certificate optimization structure

COF form:

`(I,T,A,L,Theta)` with objective equal to the number of targets satisfying `L_S(t) > Theta(t)`.

Closest antecedents:

- budgeted maximum coverage;
- threshold covering;
- binary integer formulations with target activation variables.

Classification:

`Framework definition / project-specific packaging`, not authorized as historically novel.

Required manuscript wording:

> We use a certificate-oriented abstraction of a finite threshold-activation selection problem.

Do not write:

> We introduce the first general theory of certificate optimization.

### Definition 2.2 and Theorem 3.1 — additive structure and monotonicity

COF form:

`L_S(t)=beta(t)+sum_{i in S} Gamma(i,t)`.

If all contributions are nonnegative, inclusion is monotone.

Closest antecedents:

- additive 0–1 integer models;
- monotone threshold functions;
- weighted coverage.

Classification:

`Known identity / elementary theorem`.

Potential contribution:

The explicit separation between the certificate functional and the search machinery is useful exposition, not yet a novelty claim.

### Theorem 3.3 — feasibility-preserving dominance exchange

COF form:

If object `i` dominates object `j` coordinatewise over every target and the one-for-one replacement preserves feasibility, replacing `j` by `i` cannot reduce any certificate.

Closest antecedents:

- dominance preprocessing in knapsack;
- exchange arguments in combinatorial optimization;
- Pareto dominance in multiobjective contribution vectors.

Classification:

`Known exchange principle specialized to certificate vectors`.

Project-specific value:

The theorem correctly shows that global contribution nonnegativity is unnecessary; only pairwise coordinatewise dominance and replacement feasibility are required.

Safe claim:

`a precise hypothesis separation within the COF formulation`.

### Theorem 3.5 — existence of a precedence-legal optimum

COF form:

Repeated feasibility-preserving dominance exchanges along an acyclic rank orientation transform an optimum into a precedence-legal optimum.

Closest antecedents:

- precedence-constrained selection;
- closure systems;
- terminating exchange and normalization arguments.

Classification:

`Likely standard proof pattern / exact closest theorem not yet identified`.

Audit requirement:

Search specifically for canonicalization of optimal solutions under dominance-generated precedence and for closure-preserving exchange systems.

Current claim status:

`Candidate project-specific lemma; novelty unresolved`.

### Theorems 4.3–4.4 — safe pruning and exact finite Branch-and-Bound

Closest antecedent:

Classical Branch-and-Bound correctness.

Classification:

`Known`.

Manuscript action:

Present as a self-contained correctness lemma needed for executable crosslinks, not as a research contribution.

### Theorem 5.2 — coordinatewise top-b upper bound

COF form:

For each target, the sum of any residual `b` selected contributions is bounded by the sum of the `b` largest residual contributions for that target.

Closest antecedents:

- order-statistic bounds;
- optimistic targetwise relaxations;
- knapsack and cardinality upper bounds.

Classification:

`Known / elementary`.

Project-specific value:

The manuscript correctly handles signed contributions for exact cardinality and distinguishes `exactly b` from `at most b`.

### Section 6 — precedence propagation

Closest antecedents:

- constraint propagation on implication DAGs;
- precedence-constrained knapsack closure;
- descendant exclusion after ancestor exclusion.

Classification:

`Known algorithmic mechanism`.

No novelty claim authorized.

### Theorem 7.2 — leave-one-out mandatory-object test

COF form:

If the optimistic top-b bound excluding object `i` cannot certify target `t`, every certifying completion must contain `i`.

Closest antecedents:

- reduced-cost or bound-based variable fixing;
- probing;
- indispensability tests;
- forcing in constraint programming;
- knapsack cover reasoning.

Current assessment:

The logical form is standard: prove a variable mandatory by showing infeasibility under its exclusion. The specific targetwise top-b implementation is a clean specialization.

Classification:

`Known proof pattern / project-specific exact specialization`.

Novelty status:

Not authorized.

### Proposition 7.3 — precedence-closed mandatory requirements

If an object is mandatory and every legal solution containing it must contain its ancestors, the ancestor closure is mandatory.

Classification:

`Known implication closure / Identity`.

### Pairwise compatibility graph

COF form:

Targets are declared incompatible when the union of their sound mandatory closures exceeds the remaining budget.

Closest antecedents:

- conflict graphs;
- incompatible requirements under resource capacity;
- pairwise no-good constraints.

Important distinction:

The vertices are targets, not selected objects. An edge means that the two targets cannot both be certified under the mandatory-set relaxation. This is a derived target-level conflict graph.

Classification:

`Project-specific construction from known ingredients`.

This target-level derivation is one of the strongest defensible contributions of the current framework.

### Higher-order compatibility hypergraph

COF form:

A target family `H` is forbidden under the mandatory-set relaxation when the union of its mandatory closures exceeds the residual budget.

Closest antecedents:

- no-good hyperedges;
- capacity covers;
- conflict hypergraphs;
- minimal infeasible subsystems.

Classification:

`Known combinatorial object; project-specific target-certificate derivation`.

### Minimal forbidden target families and antichain compression

COF form:

The complete upward-closed forbidden family is represented exactly by its inclusion-minimal members.

Closest antecedents:

- minimal knapsack covers;
- clutters and Sperner families;
- minimal infeasible sets;
- hypergraph antichains.

Classification:

`Known principle`.

Project-specific contribution:

Demonstrating that the mandatory-target incompatibility relaxation has this structure and integrating it as a safe bound in the exact search.

### Fourier realization

The map

`Gamma(k,c)=P_k(c)+|P_k(c)|`

and the derivation of target certificates from retained Fourier frequencies belong to the PVG/Fourier application.

Classification:

`Application-specific exact realization`.

It does not establish general transferability.

## 4. Revised contribution hierarchy

### Tier A — known foundations

- Branch-and-Bound correctness;
- additive monotonicity;
- order-statistic upper bounds;
- precedence closure and propagation;
- dominance exchange as a general pattern;
- conflict graphs and no-good constraints;
- minimal covers and antichain compression.

### Tier B — exact specializations worth retaining

- signed exact-cardinality targetwise bound;
- leave-one-out mandatory-object test specialized to threshold certificates;
- distinction between dominance exchange and deletion;
- distinction between actual simultaneous certification and mandatory-set compatibility.

### Tier C — strongest project-specific synthesis

- deriving object requirements separately for each certificate target;
- closing those requirements under precedence;
- deriving target-level pairwise and higher-order incompatibility from union cost;
- integrating minimal forbidden target hyperedges into an exact certificate-aware Branch-and-Bound;
- realizing the framework in the Fourier frequency-retention problem.

### Tier D — claims still blocked

- first general theory of certificate optimization;
- historical novelty of the theorem package;
- broad transferability;
- uniform computational superiority;
- polynomial-time solvability.

## 5. Required changes to the v0.2 manuscript

1. Replace `We introduce a finite framework` in the abstract by `We formulate a certificate-oriented finite framework`.
2. Move classical Branch-and-Bound exactness from the headline contribution list to the methodological foundation list.
3. Label monotonicity and the top-b bound as elementary supporting lemmas.
4. Present dominance exchange as a specialized exchange lemma, emphasizing the exact assumptions rather than novelty.
5. Make the target-level nature of compatibility graphs explicit.
6. State that minimal obstruction antichain compression is an application of a standard upward-closed-family principle.
7. Define the main contribution as the combined derivation pipeline:

`certificate deficits -> mandatory objects -> precedence closure -> target incompatibility -> minimal target obstructions -> exact bound`.

8. Add a related-work section covering PCKP, minimal knapsack covers, conflict analysis, threshold coverage, and minimal infeasible subsystems.
9. Keep submission readiness blocked until stable bibliographic records and a second independent application exist.

## 6. Search gaps remaining

The following focused searches remain mandatory:

- exact precedents for threshold-target activation with additive contributions;
- variable forcing by leave-one-out cardinality upper bounds;
- target-level conflict graphs derived from mandatory resource unions;
- canonical optimal representatives under dominance-generated precedence;
- minimal infeasible target families in test selection, sensor selection, and diagnosis;
- clutters and blocker duality as possible exact language for the obstruction antichain.

## 7. Decision

```text
COF FOUNDATIONS MATHEMATICAL VALIDITY = UNCHANGED
CLASSICAL COMPONENT NOVELTY = NOT CLAIMED
TARGET-LEVEL MANDATORY-CONFLICT PIPELINE = PROJECT-SPECIFIC SYNTHESIS
HISTORICAL NOVELTY = UNRESOLVED
SECOND INDEPENDENT APPLICATION = ABSENT
EXTERNAL BIBLIOGRAPHY = PARTIAL
SUBMISSION READINESS = NOT AUTHORIZED
```

No Goldbach, RH, GRH, polynomial-time, or broad-transferability claim is made.