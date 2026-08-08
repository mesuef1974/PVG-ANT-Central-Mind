# COF Manuscript Related-Work Repair 001

Status: `implemented_as_safe_insert / full integration pending local compile`

## Scope

This repair applies the conclusions of `COF-RELATED-WORK-AUDIT-001` and `002` to the proof-audited COF manuscript without overstating bibliographic completeness.

## Completed artifact

A LaTeX-ready section was added at:

`paper/latex/COF-RELATED-WORK-SECTION-v0.3.tex`

It performs the following corrections:

1. identifies Branch-and-Bound, cardinality bounds, dominance, precedence constraints, conflict graphs, hypergraphs, minimal infeasible sets, and antichain representation as established ingredients;
2. states that the corresponding self-contained theorems are foundations and dependency nodes, not isolated novelty claims;
3. distinguishes target-level conflicts from ordinary conflicts among selectable objects;
4. identifies the strongest currently defensible synthesis as the pipeline

   `certificate deficit -> mandatory objects -> precedence closure -> target-level conflict -> minimal forbidden target families -> admissible exact-search bounds`;
5. preserves the boundary that historical novelty remains unresolved;
6. preserves the requirement for a second independent application before broad transferability claims.

## Required manuscript edits

### Abstract

Replace `We introduce a finite framework` by conservative language:

> We study a finite certificate-oriented formulation for constrained object selection and isolate an exact-search pipeline built from established optimization ingredients.

Add:

> The contribution claimed here is the explicit target-certificate synthesis and its verified Fourier realization, not priority for Branch-and-Bound, precedence constraints, dominance, conflict hypergraphs, or minimal-obstruction principles individually.

### Introduction

Insert:

```tex
\input{COF-RELATED-WORK-SECTION-v0.3.tex}
```

immediately after `Scientific boundary` and before `Certificate Optimization Structures`.

### Contributions list

Reclassify items as follows:

- definitions and dependency separation: framework organization;
- monotonicity, safe pruning, exact BnB, top-b bounds, and minimal antichain characterization: self-contained foundational results, not isolated priority claims;
- dominance-to-precedence canonicalization: theorem-level project formulation, priority unresolved;
- mandatory-deficit extraction and target-level graph/hypergraph construction: principal project-specific synthesis;
- Fourier/PVG realization and executable evidence: documented first application.

### Conclusion

Replace any implication of broad generality with:

> The manuscript establishes a finite exact formulation and one substantial realization. Its transfer value remains a hypothesis until an independent second application is completed.

## Bibliography gate

Current state:

```text
EXTERNAL BIBLIOGRAPHY = PARTIAL
THEOREM-LEVEL ANTECEDENT MATCHING = INCOMPLETE
HISTORICAL NOVELTY = UNRESOLVED
SUBMISSION READINESS = NOT AUTHORIZED
```

No unverified DOI, publisher metadata, or priority statement is inserted merely to make the bibliography appear complete.

## Validation still required

- integrate the input line into the main TeX file;
- compile the resulting manuscript locally;
- confirm section and cleveref crosslinks;
- rerun theorem/executable crosslink audits;
- record new page count and PDF hash;
- update manuscript version only after successful compile.

## Scientific ceiling

This repair changes positioning and attribution only. It proves no new theorem, establishes no originality claim, and gives no progress on Goldbach, RH, or GRH.
