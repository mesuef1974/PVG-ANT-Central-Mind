# COF Paper v0.2 Review Status

## Manuscript

`research/certificate-optimization-framework/paper/COF-FOUNDATIONS-DRAFT-v0.2.md`

## Review basis

- COF-FOUNDATION-001: additive certificate structure, monotonicity, exchange;
- COF-FOUNDATION-002: exact Branch-and-Bound and precedence propagation;
- COF-FOUNDATION-003: mandatory closures, compatibility relaxations, minimal obstructions;
- COF-FOUNDATION-004: theorem dependency matrix and paper integration;
- `COF-PAPER-PROOF-AUDIT-v0.1.md`.

## Repairs incorporated

1. dominance exchange now explicitly requires preservation of admissibility;
2. precedence-legal optimum now uses an acyclic rank and terminating potential;
3. exact-cardinality top-`b` bounds allow signed contributions;
4. at-most-cardinality bounds use `M_{<=b}`;
5. mandatory leave-one-out tests follow the same exact/at-most distinction;
6. graph and hypergraph constructions are labeled as compatibility relaxations;
7. minimal-obstruction containment is existential, not unique;
8. antichain compression is exact for the mandatory-set relaxation only;
9. computational verification is separated from abstract proof.

## Gate result

```text
ABSTRACT DEFINITIONS = PASS
THEOREM ASSUMPTIONS = PASS
PROOF LOGIC = PASS
RELAXATION SCOPE = PASS
PVG CLAIM BOUNDARY = PASS
TRANSFERABILITY CLAIM = NOT AUTHORIZED
SECOND INDEPENDENT APPLICATION = ABSENT
LATEX LOGIC GATE = OPEN
REFERENCE CROSSLINK GATE = OPEN / NOT COMPLETE
SUBMISSION READINESS = NOT AUTHORIZED
```

## Next action

`COF-PAPER-REFERENCE-CROSSLINK-AUDIT-001`

Required work:

- map each abstract theorem to its foundation source;
- map each Fourier/PVG formula to its source theory file;
- map every benchmark number to its JSON receipt;
- remove any benchmark number not directly supported by a committed receipt;
- only then create the LaTeX manuscript.
