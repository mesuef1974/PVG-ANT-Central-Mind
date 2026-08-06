# RMG-002-F — Zeta Zero / Explicit Formula / Prime-Observable Dependency Boundary

Status: completed / boundary-registry verification PASS 6/6

Classification: Knowledge Architecture / Analytic Boundary / Governance Diagnostic

Branch: `agent/pvg-axis-sum-continuation-002`

## 1. Mission

Represent the dependency boundary connecting von Mangoldt weights, Chebyshev observables, the Riemann zeta function, its nontrivial zeros, and classical explicit formulas without collapsing arithmetic reindexing into complex-analytic proof.

## 2. Delivered artifacts

```text
research/research-memory-graph/registry/zeta-zero-explicit-formula-boundary.jsonl
research/research-memory-graph/code/verify_rmg_002_f.py
research/research-memory-graph/results/rmg_002_f_verification.json
```

## 3. Core dependency graph

The unit records the exact finite identity

\[
\psi(x)=\sum_{n\le x}\Lambda(n),
\]

and the known analytic chain

```text
zeta meromorphic continuation
→ pole, trivial zeros, nontrivial zeros
→ contour/residue explicit formula
→ weighted prime-power observable psi(x).
```

The direction from zero data to prime-counting oscillation is recorded as a classical analytic dependency. It is not represented as an intrinsic PVG theorem.

## 4. Explicit-formula components

Three governed components are registered:

1. the pole at `s=1`, supplying the principal term under standard normalizations;
2. nontrivial zeros, supplying oscillatory correction terms;
3. trivial zeros and archimedean/gamma-factor terms, supplying normalization-sensitive secondary corrections.

No single schematic formula is declared canonical across all normalizations. The registry stores component roles rather than pretending all versions have identical endpoint conventions.

## 5. ANT ↔ PVG translation

### Exact arithmetic layer

A positive single-axis point

\[
v=k e_p
\]

recovers exactly the prime power `p^k` and its von Mangoldt weight `log p`.

The cumulative observable `psi(x)` is exactly the logarithmic mass of positive single-axis points whose decoded integers are at most `x`.

### Lost analytic layer

The exact arithmetic translation does not contain by itself:

- meromorphic continuation;
- the functional equation;
- contour displacement;
- residue calculus;
- zero multiplicities and locations;
- convergence and truncation estimates for explicit formulas.

Therefore the current translation from explicit-formula data to PVG is diagnostic and externally supplied, not an exact intrinsic realization.

## 6. Inverse boundary

Full finite jump data for `psi` determines the finite sequence of von Mangoldt values on the corresponding interval. This does not imply recovery of the global nontrivial-zero multiset.

In particular:

```text
one value psi(x)              → highly lossy aggregate
finitely many psi values      → finite arithmetic information
all exact jump data on a finite interval → finite Lambda data
finite Lambda data            → does not determine all zeta zeros
```

Any inverse explicit-formula statement requires an independently specified function space, transform, completeness theorem, limiting process, and stability certificate.

## 7. Negative reasoning certificates

The graph rejects:

```text
finite verification of zeros up to height T
⇒ RH
```

because RH quantifies over every nontrivial zero.

It also rejects:

```text
PVG reindexing of Lambda or psi
⇒ classical explicit formula
```

because analytic continuation, contour methods, residues, and error control remain missing.

Finally:

```text
exact integer encoding by valuation vectors
⇒ zero-location theorem
```

is explicitly classified as an anti-collapse violation.

## 8. Verification

The standard-library verifier checks:

- registry size: 12 records;
- unique record identifiers;
- presence of the three explicit-formula component classes;
- two negative claim-rejection records;
- at least two boundary records;
- two directional translation records.

Observed result:

```text
PASS 6/6
```

## 9. Assimilation status

```text
L5_COMPUTATIONALLY_REGRESSION_TESTED:
- dependency and boundary registry structure
- translation loss accounting
- negative claim-rejection rules

L3_BIDIRECTIONALLY_ANALYZED:
- explicit-formula component graph

L2_TRANSLATED_TO_PVG:
- nontrivial-zero contribution as externally supplied diagnostic labels
```

No node is promoted to L6: no project-owned Lean proof was added.

No zero node is promoted to L4 merely by registry verification; the verification tests the representation and governance rules, not the truth of new zero claims.

## 10. Scientific ceiling

```text
KNOWN ANT DEPENDENCY MAP
EXACT FINITE ARITHMETIC OBSERVABLE TRANSLATION
DIAGNOSTIC ZERO-TO-PRIME LINK ONLY
NO INTRINSIC PVG ZERO RECOVERY
NO NEW EXPLICIT-FORMULA PROOF
NO RH OR GRH PROGRESS
NO TRAINING-CORPUS AUTHORIZATION
```

## 11. Acceptance decision

```text
DEPENDENCY_REGISTRY = PASS
EXPLICIT_FORMULA_COMPONENT_BOUNDARY = PASS
ANT_TO_PVG_LOSS_PROFILE = PASS
PVG_TO_ANT_RETURN_BOUNDARY = PASS
NEGATIVE_REASONING_RULES = PASS
VERIFICATION = PASS 6/6
RMG-002-F = COMPLETED
```

## 12. Next governed step

```text
RMG-003-A — Dirichlet Characters, Residue-Phase Observables,
and L-Function Translation Registry
```

The next unit should reuse the existing character orthogonality and residue-fiber tools, distinguish principal and nonprincipal characters, and preserve the strict boundary between finite residue-phase computations and GRH-level zero control.
