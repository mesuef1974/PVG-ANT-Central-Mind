# PVG–ANT Central Mind

> **Canonical repository:** `D:\PVG-ANT-Central-Mind`  
> **Purpose:** build a reusable PVG–ANT research language and a governed native theory of Prime-Valuation Geometry.

## Current governing state

```text
Governing program:
  GOAL-PVG-INVERSE-GEOMETRY-001

Active operational goal:
  GOAL-OP-INVERSE-PRIME-FIBERS-001 = active_current

Engine and phase:
  ENGINE-004
  Phase C — Inverse Prime Fibers

Archived theorem route:
  GOAL-OP-ONE-THEOREM-001 = superseded_with_reason
  non-governing

Phase D:
  NOT AUTHORIZED
```

The owner redirected the project to inverse geometry. The earlier one-theorem program is retained as historical research memory only; it is not the current front.

PR #63 remains open, draft, and unmerged on:

```text
agent/pvg-point-classification-inverse-geometry-001
```

`main` remains unchanged until explicit owner authorization.

## Research compass and goal memory

```text
named object or question
→ readiness card and frozen scope
→ exact PVG encoding
→ proved identity / finite test / negative certificate
→ loss accounting
→ honest classification
→ reproducible artifact
→ goal-state update
→ Stage Review
```

Canonical references:

- `central-mind-charter.md`
- `central-mind-goals.md`
- `governance/pvg-ant-research-compass-v1.md`
- `governance/pvg-ant-goal-memory-and-return-protocol-v1.md`
- `governance/pvg-inverse-geometry-engine-architecture-v1.md`
- `governance/readiness/ENGINE-004-INVERSE-PRIME-FIBERS.md`
- `governance/checkpoints/ENGINE-004-CENTERED-GAP-COORDINATES-001.md`
- `governance/checkpoints/ENGINE-004-PASS-002-CENTERED-RADIUS-SPECTRA-001.md`
- `governance/readiness/ENGINE-004-PASS-003-CENTERED-RADIUS-INCIDENCE.md`
- `registries/program-goals.jsonl`
- `registries/goal-state-overrides-engine-004.jsonl`
- `transition-memory/latest-state.md`
- `transition-memory/next-action.md`

## Supreme law

\[
\boxed{
\text{Geometry}
\leftrightarrow
\text{Analysis}
\leftrightarrow
\text{Certificate}
}
\]

```text
No registry, no entry.
No classification, no claim.
No certificate, no theorem.
No readiness gate, no research execution.
No parent goal, no detour.
No explicit Stage Review, no phase transition.
No fetched canonical state, no new work branch.
No Goldbach, PNT, RH, or GRH progress without a complete proof certificate.
```

The earlier v0.6 and Coherence Audit 005 controls remain retained compatibility infrastructure; they do not determine the current research front.

## ENGINE-004 frozen box

```text
support prime limit = 11
support face sizes = 1,2,3
integer cap = 100000
support faces = 25
certified Phase-B integer points = 884
prime-pair convention = unordered distinct primes p<q
```

No cap expansion is authorized.

## Exact inverse prime-fiber structure

For each certified point \(N\in\mathcal N(F)\),

\[
\mathcal R_2(N)=\{\{p,q\}:p<q,\ p+q=N\}.
\]

The support face controls the parity route:

```text
2 in F     ⇔ N is even; every distinct-prime pair is odd+odd.
2 not in F ⇔ N is odd; R_2(N) is empty or {{2,N-2}}.
```

For \(\Delta=q-p\),

\[
p=\frac{N-\Delta}{2},
\qquad
q=\frac{N+\Delta}{2},
\]

\[
\Delta\equiv N\pmod2,
\qquad
N^2-\Delta^2=4pq,
\qquad
\gcd(N,\Delta)=\gcd(N,2).
\]

For even \(N\), \(m=N/2\) and \(d=\Delta/2\) satisfy

\[
p=m-d,
\qquad
q=m+d,
\qquad
m^2-d^2=pq,
\qquad
\gcd(m,d)=1.
\]

These are elementary exact identities. No historical originality claim is made.

## Prime-fiber finite certificate

```text
integer points                         = 884
representable points                   = 745
nonrepresentable points                = 139
unordered distinct-prime pairs         = 218024
centered-gap coordinates               = 218024
independent-scan mismatches             = 0
maximum multiplicity                   = 1557
maximum point                          = 97200
maximum support                        = {2,3,5}
```

Within this frozen box only, the nonrepresentable points on supports containing axis 2 are `2,4,6`.

## PASS-002 centered-radius spectra

The governed spectrum is

\[
D(N)=
\begin{cases}
\{\Delta/2:\Delta\in\Delta_2(N)\},&N\text{ even},\\
\Delta_2(N),&N\text{ odd}.
\end{cases}
\]

Exact recovery:

```text
N=2m and d in D(N) => (p,q)=(m-d,m+d)
N odd and represented => d=N-4 and (p,q)=(2,d+2)
(N,D(N)) reconstructs the complete distinct-prime fiber
|D(N)|=|R_2(N)|
```

Finite certificate:

```text
total coordinate occurrences                 = 218024
unique coordinate values                     = 36797
unique spectra including empty               = 744
unique nonempty spectra                      = 743
nonempty spectrum collision classes          = 1
proper containment edges                     = 2048
non-singleton-subset containment edges       = 10
shared coordinate values                     = 27799
cross-route coordinate values                = 85
odd/odd shared coordinate values             = 0
```

The only nonempty complete-spectrum collision is

\[
D(5)=D(8)=D(12)=\{1\}.
\]

The most widely shared coordinate is \(d=7\), occurring at 64 frozen-box points.

```text
(N,D(N)) = lossless for the complete pair fiber
D(N) alone = generally loses N, midpoint, support label, and pair labels
```

Classification: exact/proved recovery plus finite-verified frozen-box geometry.

## Checkpoints and next pass

```text
ENGINE-004-CENTERED-GAP-COORDINATES-001 = CHECKPOINT_PASS
ENGINE-004-PASS-002-CENTERED-RADIUS-SPECTRA-001 = CHECKPOINT_PASS
ENGINE-004-PASS-003-CENTERED-RADIUS-INCIDENCE = READY
ENGINE-004 = active_current
Stage decision = continue_within_phase_c
Phase D = NOT AUTHORIZED
PVG Centered-Radius Spectra Audit = SUCCESS
Governance Required Gate = SUCCESS
```

PASS-003 is restricted to static coordinate-owner incidence geometry inside the same 884-point box. It does not authorize iteration, orbit dynamics, cap expansion, or asymptotics.

## Retained capability state

```text
TRANSLATION-KERNEL-V2-PASS-001 = checkpoint_pass
PVG-ANT-BENCHMARK-001 = checkpoint_pass
TRANSLATION-KERNEL-V2-PASS-002 = checkpoint_pass
PVG-UNDERSTANDING-DEEPENING-001 = checkpoint_pass
GOVERNANCE-ENFORCEMENT-CLOSURE-001 = CLOSED
CENTRAL-MIND-CONTINUITY-001 = installed_repository_side
CENTRAL-MIND-CONTINUITY-CLOSURE-002 = closed
Current maturation receipt = MATURATION-RECEIPT-007
ADVERSARIAL-PVG-ANT-BENCHMARK-002 = NOT_STARTED
Dataset 004 remains unauthorized
```

These are supporting capabilities. They do not create another active research front.

## Retained source-grounding history

Historical source-grounding safeguards remain active as non-governing capability memory — the source-grounding-corrected Montgomery story includes the `v0.6-E Closure Review` and `v0.6-G Closure Review` tracks, and the quarantine of mismatched A/B/legacy-E material.

```text
MNTII-006-E = CLOSED by v0.6-e-closure
TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001 = retained on demand
A/B/legacy-E = quarantined / source-mismatch / not live
```

This source history supplies tools and negative memory only. It does not reopen book mining, the theorem route, or a second active research front.

## Historical inverse-geometry foundation

The branch retains exact point passports, native valuation geometry, support/height/simplex structures, additive cells, support-fiber synthesis, reverse support preimages, ENGINE-002, ENGINE-003, deterministic tools, tests, certificates, and visual laboratories.

PASS-025’s depth-12 witness remains finite and frozen-class dependent. It does not establish global minimality, unbounded depth, or general termination.

## Scientific ceiling

- inverse geometry only;
- exact identities and complete finite verification only;
- no theorem-route reactivation;
- no Phase D without a separate readiness decision;
- no cap expansion or asymptotic estimate;
- no historical originality or publication-readiness claim;
- no Goldbach, PNT, RH, or GRH progress;
- no trained neural network or approved training corpus.

**Classification:** governed research infrastructure and exact finite inverse geometry. No original lemma or theorem is certified.
