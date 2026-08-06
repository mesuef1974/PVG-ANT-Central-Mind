# REASONING-ORCHESTRATOR-001

## Status

`validated_intake`

## Purpose

This unit turns the Translation Knowledge Graph from a collection of separate reasoning modules into a governed multi-hop router. It does not prove theorems. It identifies the relevant TKG modules, assembles their hypothesis ledgers, exposes blocked inference edges, preserves provenance, and emits a conservative claim ceiling.

## Scope

The orchestrator routes across `TKG-001` through `TKG-015`.

Its output schema is:

1. normalized question;
2. detected intents;
3. selected TKG units;
4. reasoning path;
5. required hypotheses;
6. missing certificates;
7. blocked edges;
8. ANT ↔ PVG translation status;
9. preserved information;
10. lost information;
11. claim ceiling;
12. next valid action.

## Core routing rule

A question is not answered by selecting one formula. It is decomposed into one or more intents. Each intent activates a governed TKG route.

Examples:

```text
Möbius inversion / divisor convolution
→ TKG-001 + TKG-002
```

```text
Euler product / Dirichlet-series product
→ TKG-003 + TKG-004
```

```text
explicit formula / Perron / contour shift
→ TKG-011 + TKG-012 + TKG-013 + TKG-014
```

```text
PNT asymptotic transfer
→ coefficient layer + transform layer + boundary layer + TKG-015
```

## Hypothesis ledger

The orchestrator treats theorem hypotheses as first-class objects. For example, an explicit-formula route requires at least:

- fixed kernel;
- certified continuation region;
- complete pole/zero ledger;
- verified residues;
- certified contour-side estimates;
- fixed zero-sum and endpoint conventions;
- fixed limit order.

A Tauberian route requires:

- exact theorem variant;
- coefficient positivity or suitable monotonicity;
- verified main polar part;
- certified boundary regularity;
- fixed normalization and conclusion scope.

The orchestrator may report missing certificates. It may not invent them.

## Blocked inference edges

The following edges are blocked by default:

```text
Euler product → PNT
finite computation → asymptotic theorem
functional-equation symmetry → RH
character orthogonality → PNT in arithmetic progressions
formal contour shift → explicit formula
simple pole → Tauberian conclusion
PVG reinterpretation → new theorem
syntactic completeness → analytic authorization
```

A blocked edge may only be replaced by a complete, separately verified proof route.

## PVG role

The orchestrator records whether a step is:

- valuation-local;
- labelled-axis exact;
- residue-harmonic;
- archimedean;
- complex-analytic;
- hybrid and nonlocal.

This prevents the false claim that every ANT operation is internally local to PVG.

## Example 1: valid finite route

Question:

```text
Use Möbius inversion on this divisor convolution.
```

Expected route:

```text
intent = arithmetic_identity
units = TKG-001, TKG-002
claim ceiling = ASSIM-L3 / MATH-M0
```

## Example 2: rejected shortcut

Question:

```text
The Euler product proves the Prime Number Theorem.
```

The orchestrator selects the Euler-product and PNT dependency units, then emits:

```text
blocked edge = Euler product → PNT
missing certificates include boundary nonvanishing and a valid transfer theorem
PNT progress = NONE
MATH = MATH-M0
```

## Example 3: analytic route

Question:

```text
Build an explicit formula using Perron and a contour shift.
```

Expected route:

```text
TKG-011 → TKG-012 → TKG-013 → TKG-014
```

The result remains at `ASSIM-L2` unless the analytic certificates are independently verified.

## Query harness

```bash
python research/translation-knowledge-graph/code/query_reasoning_orchestrator_001.py \
  "The Euler product proves the Prime Number Theorem"
```

A hypothesis can be marked as supplied:

```bash
python research/translation-knowledge-graph/code/query_reasoning_orchestrator_001.py \
  "Build an explicit formula by Perron contour shift" \
  --supplied "kernel fixed" "limit order fixed"
```

Marking a string as supplied does not validate it. Authorization remains false.

## Verification

The committed structural verifier checks:

- arithmetic-identity routing;
- PNT shortcut rejection;
- RH shortcut rejection;
- multi-unit explicit-formula routing;
- missing-certificate reporting;
- unclassified-question handling;
- permanent closure of automatic theorem promotion.

Execution is not claimed from the connector-only environment.

## Scientific ceiling

```text
ASSIM = L2 or L3 depending on route
MATH = MATH-M0
PNT progress = NONE
PNT-AP progress = NONE
Goldbach progress = NONE
RH progress = NONE
GRH progress = NONE
automatic theorem promotion = BLOCKED
```

## Next governed action

Build `BENCHMARK-TKG-001` with definitional, computational, multi-hop, diagnostic, and adversarial cases. The benchmark must test the orchestrator rather than merely test isolated formulas.
