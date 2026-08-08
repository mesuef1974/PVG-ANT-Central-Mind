# COF Claim–Literature Matrix 001

Status: `preliminary_related_work_audit / novelty_not_authorized`

Scope: classify every theorem-level component of **Certificate Optimization Framework Foundations v0.2** against established optimization language before any submission-readiness claim.

This document is intentionally conservative. It records antecedent families and safe claim wording. It does not establish priority, novelty, or broad transferability.

## 1. Audit rule

For each project claim, distinguish:

- `IDENTICAL OR STANDARD`: the mathematical statement is a routine or classical instance of a known paradigm;
- `SPECIALIZATION`: the result is a direct specialization of known machinery;
- `PROJECT-SPECIFIC SYNTHESIS`: the ingredients are known, but the exact organization around threshold certificates is not yet matched to a precedent;
- `CANDIDATE DISTINCT RESULT`: no close match has yet been located, but novelty is not authorized;
- `BOUNDARY`: additional literature or a second application is required.

## 2. Claim matrix

| COF component | Closest established family | Current relation assessment | Safe classification | Required wording |
|---|---|---|---|---|
| finite object selection under a cardinality budget | 0–1 knapsack, cardinality-constrained selection, maximum coverage | standard | Known | do not claim novelty |
| objective counting threshold-crossing targets | maximum coverage, partial coverage, threshold activation, multi-criteria selection | related formulation | Project-specific synthesis | present as a certificate-oriented objective, not a new optimization universe |
| additive certificate identity `L_S(t)=beta(t)+sum Gamma(i,t)` | additive set functions, linear 0–1 models | standard algebraic model | Identity / Known | state that the contribution is the separation of certificate semantics from search |
| monotonicity under `Gamma(i,t)>=0` | monotone set functions | immediate standard implication | Known / Identity | theorem may remain for internal dependency clarity, not as originality claim |
| componentwise dominance | dominance relations in knapsack and integer programming | standard principle | Known | cite dominance literature; retain exact hypotheses |
| feasibility-preserving one-for-one dominance exchange | exchange under dominance with side constraints | likely specialization | Reinterpretation / Candidate synthesis | emphasize feasibility preservation and signed-contribution independence |
| dominance does not imply deletion | standard caution in constrained dominance preprocessing | standard boundary | Known / Boundary | retain as a correctness warning |
| precedence DAG and ancestor closure | precedence-constrained knapsack and covering | standard | Known | use established precedence terminology |
| existence of a precedence-legal optimum through terminating dominance exchanges | precedence repair plus exchange argument | related but exact theorem match not yet located | Candidate distinct result | novelty not authorized; search exchange-system and closure-system literature |
| exact finite Branch-and-Bound under comprehensive branching and admissible bounds | classical Branch-and-Bound | standard correctness theorem | Known | retain only as framework completeness theorem |
| targetwise top-`b` coordinate bound | cardinality-constrained linear upper bounds; optimistic separable relaxation | direct specialization | Known / Specialization | do not claim novelty |
| leave-one-out mandatory-object test | reduced-cost / forcing tests; knapsack cover reasoning; indispensable-item tests | likely known in equivalent form | Candidate specialization | use `sound forcing test`; search alternative names before submission |
| precedence closure of mandatory objects | closure systems under implication constraints | direct implication | Identity / Specialization | no novelty claim |
| pairwise target compatibility from mandatory-closure union cost | conflict graph induced by resource infeasibility | close to conflict-graph modeling | Project-specific synthesis | describe as a necessary relaxation over targets |
| higher-order target incompatibility | conflict hypergraphs; set-packing constraints | known concept | Known concept / Project-specific construction | novelty may lie only in how target hyperedges are generated |
| minimal forbidden target families form an antichain | minimal infeasible sets in the Boolean lattice; Sperner-family structure | standard combinatorial consequence | Known / Identity | retain as exact compression statement, not as a new antichain theorem |
| all forbidden supersets represented by inclusion-minimal obstructions | monotone property represented by minimal forbidden sets | standard | Known / Identity | claim exact compression for this relaxation only |
| certificate-margin-aware pruning | Branch-and-Bound bound strengthening from target deficits and forcing | application-specific algorithmic synthesis | Candidate distinct algorithmic result | report exactness and finite performance only |
| precedence-closure-ratio branching order | density/ratio branching using closure cost | close to precedence-knapsack density heuristics | Heuristic / Computational Verification | no universal speedup claim |
| Fourier frequency-retention realization | spectral subset selection under certified tail bounds | application-specific | Reinterpretation / Diagnostic | keep separate from abstract COF claims |

## 3. Primary antecedent families to audit

### 3.1 Precedence-constrained knapsack

The established problem selects items under a capacity constraint and a directed acyclic precedence relation. This is the closest family for COF ancestor closure, legal configurations, and closure-aware branch decisions.

Required search terms:

- `precedence constrained knapsack problem`;
- `partially ordered knapsack`;
- `knapsack with dependency constraints`;
- `closure problem with a knapsack constraint`;
- `precedence constrained covering`;
- `macroitems precedence knapsack`.

A current primary reference located during the audit is:

- V. Dose, F. Furini, M. Locatelli, *Optimal Macroitem Sequences in the Precedence Constrained Knapsack Problem*, 2026 preprint.

This recent paper confirms that closure-respecting grouped objects and ratio structure are active established themes. It does not by itself settle the older priority record.

### 3.2 Conflict graphs and conflict hypergraphs

Pairwise incompatibility graphs are standard in integer programming and combinatorial optimization. Higher-order incompatibility is naturally represented by hyperedges or set-packing inequalities.

Required search terms:

- `knapsack problem with conflict graph`;
- `conflict graph branch and cut`;
- `hypergraph conflict constraints optimization`;
- `minimal infeasible set inequalities`;
- `set packing hypergraph incompatibility`.

The COF-specific object is not the existence of conflict graphs. It is the construction of **target conflicts** from unions of sound mandatory closures under a certificate budget.

### 3.3 Cover inequalities and minimal infeasible sets

Minimal covers of knapsack constraints and lifted cover inequalities are classical. Minimal infeasible subsystems and minimal forbidden sets also provide exact descriptions of upward-closed infeasibility families.

Required search terms:

- `minimal cover inequalities knapsack`;
- `lifted cover inequalities`;
- `minimal infeasible subsets binary optimization`;
- `minimal forbidden sets antichain`;
- `monotone Boolean function minimal true false points`.

A modern primary reference confirming the continuing role of minimal covers is:

- C. Hojny, C. Roy, *Computational Aspects of Lifted Cover Inequalities for Knapsacks with Few Different Weights*, 2024 preprint.

COF minimal forbidden target hyperedges must therefore be presented as an exact antichain representation of its mandatory-set relaxation, not as the invention of minimal obstruction methods.

### 3.4 Hypergraph dualization

Enumeration of minimal hitting sets and hypergraph transversals is a mature area. It is relevant if future COF work converts forbidden target hyperedges into minimal corrective object sets.

Representative primary reference:

- K. Murakami, T. Uno, *Efficient Algorithms for Dualizing Large-Scale Hypergraphs*, 2011 preprint.

Current COF does not yet solve the general dualization problem.

## 4. Claims that remain defensible now

The following statements are supported internally without a novelty claim:

1. the v0.2 theorem system is logically valid under its stated finite hypotheses;
2. the abstract framework cleanly separates certificate semantics, admissibility, and search;
3. monotonicity and dominance exchange require different hypotheses;
4. dominance is an exchange/precedence rule, not an unconditional deletion rule;
5. mandatory-set compatibility is only a necessary relaxation, not simultaneous certification;
6. minimal forbidden target families exactly compress the upward-closed forbidden family induced by that relaxation;
7. the Fourier frequency-retention problem is one exact realization;
8. the implementation was verified against exhaustive search on the recorded finite domain.

## 5. Claims not authorized

The audit does not authorize:

- `COF is a new general optimization theory`;
- `the first use of dominance, precedence, mandatory sets, conflict graphs, hypergraphs, or minimal obstructions`;
- `the first exact Branch-and-Bound for this broad class`;
- `a polynomial-time algorithm`;
- `uniform computational acceleration`;
- `broad transferability`;
- `submission readiness`;
- any Goldbach, RH, or GRH claim.

## 6. Safe manuscript revision

Replace broad introductory language such as:

> We introduce a new general optimization theory.

with:

> We develop a finite certificate-oriented formulation that separates threshold-certificate semantics from exact search and organizes dominance exchange, precedence closure, forcing tests, and higher-order incompatibility bounds in one explicit theorem system.

Recommended abstract boundary:

> The individual optimization ingredients have established antecedents in knapsack, precedence-constrained selection, conflict modeling, and minimal-obstruction methods. The present contribution is a proof-audited synthesis around target certificates together with one Fourier realization. Priority and broad transferability remain open pending a full bibliographic audit and an independent second application.

## 7. Next required evidence

Before submission-readiness review:

1. complete backward and forward citation chaining for precedence-constrained knapsack;
2. locate the earliest exact forcing/indispensable-item test equivalent to Theorem 7.2, if one exists;
3. compare minimal forbidden target hyperedges with knapsack covers and conflict-hypergraph cuts;
4. compare the precedence-legal optimum theorem with closure systems, greedoids, antimatroids, and exchange systems;
5. build a second application unrelated to PVG, Fourier analysis, or Goldbach;
6. revise the LaTeX bibliography and related-work section;
7. rerun theorem/reference/executable crosslink audits.

## 8. Audit decision

```text
COF FOUNDATIONS LOGICAL STATUS = VALIDATED
COMPONENT NOVELTY = NOT ESTABLISHED
PROJECT-SPECIFIC SYNTHESIS = SUPPORTED
GENERAL FRAMEWORK CLAIM = NOT AUTHORIZED
SECOND APPLICATION = REQUIRED
EXTERNAL BIBLIOGRAPHY = INCOMPLETE
SUBMISSION READINESS = NOT AUTHORIZED
```

Scientific ceiling: this audit changes claim scope only. It proves no new number-theoretic estimate and gives no progress on Goldbach, RH, or GRH.
