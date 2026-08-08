# COF-FOUNDATION-003 — Status v0.1

## Decision

`VALIDATED_FOUNDATION_WITH_SCOPE_CORRECTION`

## Artifact

- `theory/COF-MANDATORY-CLOSURES-AND-MINIMAL-OBSTRUCTIONS-v0.1.md`

## Established

1. A mandatory set is any sound necessary residual-object set for one target.
2. Joint certification implies inclusion of the union of the corresponding mandatory sets.
3. Under a downward-closed node resource family, mandatory compatibility is necessary for simultaneous certification.
4. Maximizing target-family size under mandatory compatibility gives an admissible Branch-and-Bound upper bound.
5. Pairwise compatibility gives a weaker graph relaxation; higher-order forbidden families give the full mandatory-union relaxation.
6. Inclusion-minimal forbidden families form an antichain that exactly compresses all forbidden families of the relaxation.
7. Minimal forbidden families yield valid 0–1 target cuts.
8. The top-gain mandatory-object test is a construction theorem inside additive, nonnegative, cardinality-budget COF; the hypergraph theory itself is more general.

## Scope corrections

### Correction 1 — necessary, not sufficient

The statement

> feasible simultaneous certification families are precisely the families containing no forbidden mandatory-union hyperedge

is too strong without an additional sufficiency theorem.

The proved statement is:

> every actually simultaneously certifiable family is mandatory-compatible.

Therefore the hypergraph computes an exact optimum of a necessary-set relaxation and a safe upper bound for the original certification problem.

### Correction 2 — no uniqueness

The statement

> every forbidden family contains a unique inclusion-minimal obstruction

is false in general.

The correct statement is:

> every finite forbidden family contains at least one inclusion-minimal forbidden obstruction.

Multiple incomparable minimal obstructions may occur inside the same forbidden family.

## Dependency boundary

The abstract results require neither Fourier analysis nor PVG. Additivity and nonnegativity are required only for the current top-gain construction of mandatory sets. Precedence is optional and enters only when closing mandatory sets under sound ancestor implications.

## Application inheritance

ACTIVE-003-Q/R/S remain valid as exact finite-search strengthening after reading:

- `exact` as exact relative to the mandatory-compatibility relaxation where appropriate;
- `feasible` in the hypergraph layer as mandatory-compatible, not necessarily actually certifiable;
- minimal-obstruction containment as existence, not uniqueness.

The verified optimum agreement and zero-false-certificate counts are unchanged.

## Scientific classification

- abstract finite combinatorics: proved;
- transfer from necessary sets to admissible upper bound: proved;
- minimal-antichain compression: proved;
- current mandatory-set generator: additive-COF realization;
- benchmark gains: empirical and application-specific;
- second independent realization: absent;
- polynomial-time claim: none;
- Goldbach claim: none;
- RH/GRH progress: none.

## Next action

`COF-FOUNDATION-004 — Unified theorem dependency matrix and core paper skeleton`
