# Next Action

```text
Date: 2026-07-22
Governing program: GOAL-PVG-INVERSE-GEOMETRY-001
Active operational goal: GOAL-OP-INVERSE-PRIME-FIBERS-001 = active_current
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
GOAL-OP-ONE-THEOREM-001 = superseded_with_reason / archived / non-governing
Phase D: NOT AUTHORIZED
```

## Closed current checkpoints

```text
ENGINE-004-CENTERED-GAP-COORDINATES-001 = CHECKPOINT_PASS
ENGINE-004-PASS-002-CENTERED-RADIUS-SPECTRA-001 = CHECKPOINT_PASS
Stage decision = continue_within_phase_c
```

PASS-002 installed the governed spectrum

\[
D(N)=
\begin{cases}
\{\Delta/2:\Delta\in\Delta_2(N)\},&N\text{ even},\\
\Delta_2(N),&N\text{ odd},
\end{cases}
\]

with exact reconstruction:

```text
N=2m and d in D(N) => (p,q)=(m-d,m+d)
N odd and represented => d=N-4 and (p,q)=(2,d+2)
(N,D(N)) reconstructs the complete distinct-prime fiber
|D(N)|=|R_2(N)|
```

Registered finite facts include:

```text
218024 coordinate occurrences
36797 unique coordinates
27799 shared coordinate values
85 cross-route coordinate values
0 odd/odd coordinate collisions
743 unique nonempty spectra for 745 represented points
one nonempty spectrum collision: D(5)=D(8)=D(12)={1}
2048 proper containment edges
10 containments with non-singleton subset
```

All are finite-box statements unless explicitly marked `IDENTITY / PROVED`.

## Immediate governed task — PASS-003

Study the exact coordinate-owner incidence geometry in the unchanged frozen box.

Define the owner set of a governed coordinate \(d\):

\[
\mathcal O(d)=\{N:d\in D(N)\},
\]

and its support projection

\[
\mathcal F(d)=\{\operatorname{supp}(N):N\in\mathcal O(d)\}.
\]

The pass may compute and certify only:

1. the complete coordinate-to-integer incidence relation;
2. the complete coordinate-to-support-face projection;
3. owner multiplicity classes \(|\mathcal O(d)|\);
4. support multiplicity classes \(|\mathcal F(d)|\);
5. even/even and odd/even route-conditioned ownership;
6. intersections \(\mathcal O(d_1)\cap\mathcal O(d_2)\) already visible in spectra;
7. support-face intersection and separation patterns;
8. exact finite hypergraph degree sequences and connected components, if defined without iteration;
9. invariants preserved or lost by projection from owners to support faces;
10. independent regeneration, deterministic ordering, tests, and a compact certificate.

## Preregistered separation of layers

```text
coordinate d
→ prime-pair occurrence over N
→ integer owner N
→ exact support face F
→ route class
```

These layers must not be conflated.

In particular:

- repeated coordinate does not imply repeated prime pair;
- repeated coordinate does not identify the midpoint;
- repeated support ownership does not determine the exponent vector;
- projection from integer owners to support faces can collapse distinct points;
- graph or hypergraph language is finite incidence language only, not Phase-D orbit dynamics.

## Required outputs

- `tools/pvg_centered_radius_incidence.py` or an equivalently named ENGINE-004 tool;
- dedicated complete-box tests;
- independent implementation or independently structured scan;
- compact deterministic JSON certificate and SHA-256;
- a mathematical report with exact laws separated from finite observations;
- a named ENGINE-004 PASS-003 checkpoint;
- CI assertions for all preregistered totals and claim-ceiling flags;
- updated transition state and PR body.

## Retained capability state — supporting, not governing

```text
TRANSLATION-KERNEL-V2-PASS-001 = checkpoint_pass
PVG-ANT-BENCHMARK-001 = checkpoint_pass
TRANSLATION-KERNEL-V2-PASS-002 = checkpoint_pass
PVG-UNDERSTANDING-DEEPENING-001 = checkpoint_pass
GOVERNANCE-ENFORCEMENT-CLOSURE-001 = CLOSED
CENTRAL-MIND-CONTINUITY-001 = installed_repository_side
CENTRAL-MIND-CONTINUITY-CLOSURE-002 = closed
Current maturation receipt = MATURATION-RECEIPT-007
MNTII-006-E = CLOSED by v0.6-e-closure
TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001 = retained on demand
Montgomery A/B/legacy-E = quarantined / source-mismatch / not live
```

These stages and tools do not create a second research front. Quarantined source-mismatch material is negative memory only.

```text
ADVERSARIAL-PVG-ANT-BENCHMARK-002 = NOT_STARTED
registries/planned.jsonl is empty
Dataset 004 remains unauthorized
no targeted learning before the immutable raw error map
no local component training, corpus promotion, LoRA, or SFT
no automatic Lean expansion
```

## Required scientific classification

Every statement must be labeled as one of:

```text
IDENTITY
PROVED
FINITE-VERIFIED
INTERPRETATION
HYPOTHESIS
OPEN
```

No degree distribution, collision, connected component, absence, extremum, or support pattern may be promoted beyond the frozen box.

## Required implementation discipline

- keep the 884-point box unchanged;
- preregister exact outputs before interpretation;
- preserve coordinate/pair/integer/support/route separation;
- add independent verification and deterministic regeneration;
- run honesty, state coherence, Research Compass, and Goal Memory audits;
- push every coherent change to `agent/pvg-point-classification-inverse-geometry-001`;
- keep PR #63 draft and unmerged unless the owner explicitly authorizes otherwise.

## Stop conditions

Stop and require a new readiness decision before:

- Phase D orbit dynamics or iterative transitions;
- support-prime, face-size, or integer-cap expansion;
- weighted, averaged, density, or asymptotic representation analysis;
- ANT translation beyond exact elementary identities;
- theorem-target activation or theorem-path return;
- a second theorem target;
- originality, publication, Goldbach, PNT, RH, or GRH claims.

## Current ceiling

The authorized next action is exact finite incidence geometry of centered-radius coordinates inside ENGINE-004. It is not an orbit program, theorem program, major-conjecture program, or authorization for Phase D. There is no Goldbach or PNT progress and no RH/GRH progress.
