# ENGINE-004 PASS-002 — Centered-Radius Spectra Checkpoint

```text
Checkpoint ID: ENGINE-004-PASS-002-CENTERED-RADIUS-SPECTRA-001
Goal ID: GOAL-OP-INVERSE-PRIME-FIBERS-001
Program: GOAL-PVG-INVERSE-GEOMETRY-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Decision: CHECKPOINT_PASS
Goal status after checkpoint: active_current
Stage decision: continue_within_phase_c
Phase D: NOT AUTHORIZED
Date: 2026-07-22
```

## Frozen scope preserved

```text
support primes <= 11
support face sizes = 1,2,3
integer cap = 100000
support faces = 25
integer points = 884
prime-pair convention = unordered, distinct, p<q
```

No support-prime, face-size, integer-cap, or phase expansion occurred.

## Governed object

For every certified point \(N\), with centered-gap fiber \(\Delta_2(N)\),

\[
D(N)=
\begin{cases}
\{\Delta/2:\Delta\in\Delta_2(N)\},&N\text{ even},\\
\Delta_2(N),&N\text{ odd}.
\end{cases}
\]

An earlier scale-free ratio `Delta/N` was explicitly rejected as outside the governed object for this pass. No conclusion from that superseded coordinate is admitted.

## Exact results admitted

For even \(N=2m\) and \(d\in D(N)\),

\[
p=m-d,
\qquad
q=m+d.
\]

For odd represented \(N\),

\[
d=N-4,
\qquad
N=d+4,
\qquad
(p,q)=(2,d+2).
\]

Consequently,

\[
(N,D(N))
\]

reconstructs the complete distinct-prime fiber, and

\[
|D(N)|=|\mathcal R_2(N)|.
\]

Two represented odd points cannot share one governed coordinate.

**Classification:** `IDENTITY / PROVED`.

## Complete frozen-box certificate

```text
representable points                         = 745
nonrepresentable points                      = 139
total coordinate occurrences                 = 218024
unique coordinate values                     = 36797
unique even-route coordinate values          = 36787
unique odd-route coordinate values           = 95
cross-route coordinate values                = 85
odd-only coordinate values                   = 10
unique spectra including empty               = 744
unique nonempty spectra                      = 743
nonempty spectrum collision classes          = 1
empty spectrum class size                    = 139
proper containment edges                     = 2048
singleton-subset containment edges           = 2038
non-singleton-subset containment edges       = 10
shared coordinate values                     = 27799
even/even shared coordinate values           = 27714
odd/even shared coordinate values            = 85
odd/odd shared coordinate values             = 0
```

The only nonempty complete-spectrum collision is

\[
D(5)=D(8)=D(12)=\{1\}.
\]

The only non-singleton spectra appearing as proper subsets are

\[
(4,2),
\qquad
(9,3),
\qquad
(45,33,3).
\]

The most widely shared coordinate is \(d=7\), occurring at 64 frozen-box points.

**Classification:** `FINITE-VERIFIED` inside the frozen 884-point box only.

## Information-loss statement

```text
(N,D(N)) = lossless for the complete distinct-prime fiber
D(N) alone = generally loses N, midpoint, support label, and pair labels
```

The spectrum is therefore not intrinsically lossy; loss occurs when the base point \(N\) is discarded.

**Classification:** exact recovery statement plus `INTERPRETATION` of the projection.

## Reproducibility certificate

```text
tool = tools/pvg_centered_radius_spectra.py
tests = tests/test_pvg_centered_radius_spectra.py
report = research/pvg-space-deepening/engine-004-pass-002-centered-radius-spectra.md
certificate = research/pvg-space-deepening/data/centered-radius-spectra-summary.json
workflow = .github/workflows/pvg-centered-radius-spectra-audit.yml
compact SHA-256 including trailing newline = 4064f2a2be99e92b20d6cc8917d8f4e8ba75ddab3c2b53e4baec7616ae19d468
```

Verified on repository head `a069ed84f21cfac58c36c0d29c13cb218bb21fd8` before checkpoint creation:

```text
PVG Centered-Radius Spectra Audit = SUCCESS
Governance Required Gate = SUCCESS
complete frozen-box tests = SUCCESS
certificate regeneration and digest match = SUCCESS
honesty audit = SUCCESS
state coherence audit = SUCCESS
research compass audit = SUCCESS
goal-memory audit = SUCCESS
```

## Stage decision

```text
continue_within_phase_c
```

ENGINE-004 remains the sole active operational goal. The next bounded question is the exact incidence geometry of centered-radius coordinates across integer points and support faces inside the same frozen box.

Admissible next work:

- coordinate-owner incidence classes;
- support-conditioned ownership and intersections;
- exact coordinate multiplicity distributions;
- route-conditioned incidence;
- finite hypergraph and containment invariants;
- deterministic independent verification.

Not authorized:

- Phase D or orbit dynamics;
- cap expansion;
- theorem-path reactivation;
- weighted or asymptotic representation analysis;
- Goldbach, PNT, RH, or GRH claims;
- originality or publication-readiness promotion.

## Honest classification

Exact elementary reconstruction laws, a complete finite spectrum certificate, and governed computational infrastructure. No original lemma or theorem is certified.
