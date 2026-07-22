# Current Capabilities

Live capability snapshot. Registries, explicit state overrides, certificates, maturation receipts, and deterministic summaries remain the machine truth.

## 1. Live goal state

```text
Strategic:
  GOAL-PVG-ANT-STRATEGIC-001 = active_fixed

Governing research program:
  GOAL-PVG-INVERSE-GEOMETRY-001 = active_long_term

Sole active operational goal:
  GOAL-OP-INVERSE-PRIME-FIBERS-001 = active_current
  ENGINE-004 / Phase C — Inverse Prime Fibers

Archived theorem route:
  GOAL-OP-ONE-THEOREM-001 = superseded_with_reason
  non-governing

Phase D:
  NOT AUTHORIZED

Publication:
  GOAL-OP-FORMAL-PUBLICATION-001 = blocked
```

State resolution is:

```text
registries/program-goals.jsonl
+ ordered registries/goal-state-overrides-*.jsonl
→ current governed goal state
```

Exactly one operational goal is active. Historical goals and closures remain accessible without competing for control.

## 2. Goal-memory capability

The machine-audited goal graph preserves:

```text
parent_goal_ids
return_to_goal_ids
goal links
readiness card
frozen scope
execution
certificate
Stage Review
current-state override
```

Installed controls:

- no goal deletion;
- one active operational goal;
- every active task has a parent, measurable deliverable, stop rule, claim ceiling, and return gate;
- state overrides are explicit owner-authorized replacements, not duplicate concept definitions;
- Phase D needs a separate readiness decision;
- the archived theorem route is not automatically reactivated.

## 3. Native PVG foundation

```text
canonical PVG objects = 20
canonical morphisms/projections = 24
deterministic recovery/loss witnesses = 16
PVG-UNDERSTANDING-DEEPENING-001 = checkpoint_pass
ontology = frozen
```

Core capabilities include full valuation vectors, labeled and Boolean support, exponent and height profiles, total height, log mass, divisor boxes, simplex incidence, residue and character fibers, convolution, local prime-axis germs, reconstruction, and explicit loss levels.

The system distinguishes

\[
\nu(n)=(\nu_2(n),\nu_3(n),\ldots)
\]

from

\[
\operatorname{supp}(n)=\{p:\nu_p(n)>0\}.
\]

Support does not recover exponents; unlabeled shapes do not recover labels; scalar summaries do not recover the full vector.

## 4. Closed inverse prerequisites

```text
ENGINE-002 — General Inverse Support Kernel = CLOSED
ENGINE-003 — Inverse Integer Fibers = CLOSED
SYNTHESIS-001 — Support-Fiber Dynamics = CLOSED
PASS-025 — Reverse Support Preimage = CLOSED historical prototype
```

ENGINE-003 supplies the exact-support fibers

\[
\mathcal N(F)=\left\{\prod_{p\in F}p^{e_p}:e_p\ge1\right\},
\]

with exponent-lattice coordinates, divisibility order, Hasse covers, and deterministic bounded generation.

PASS-025 remains a finite example of the broader inverse pipeline. Its depth-12 witness is frozen-class dependent and does not imply global minimality, unbounded depth, or termination.

## 5. Active ENGINE-004 prime-fiber capability

For every certified Phase-B point \(N\in\mathcal N(F)\),

\[
\mathcal R_2(N)=\{\{p,q\}:p<q,\ p+q=N\}.
\]

The data contract separates:

```text
support face F
→ exact-support integer N
→ prime-pair fiber R_2(N)
→ multiplicity
→ centered-gap coordinates
→ governed centered-radius spectrum D(N)
```

`prime_fiber_record(n, support)` rejects a false support label.

### Exact support routing

```text
2 in F     ⇔ N is even; distinct-prime representations are odd+odd.
2 not in F ⇔ N is odd; R_2(N) is empty or {{2,N-2}}.
```

Support determines the parity route, not the multiplicity.

### Centered-gap coordinate

For \(p<q\), \(p+q=N\), and \(\Delta=q-p\),

\[
p=\frac{N-\Delta}{2},\qquad q=\frac{N+\Delta}{2},
\]

\[
\Delta\equiv N\pmod2,\qquad N^2-\Delta^2=4pq,
\qquad \gcd(N,\Delta)=\gcd(N,2).
\]

For even \(N\), with \(m=N/2\) and \(d=\Delta/2\),

\[
p=m-d,\qquad q=m+d,\qquad m^2-d^2=pq,
\qquad \gcd(m,d)=1.
\]

Classification: `IDENTITY / PROVED`.

## 6. Frozen prime-fiber certificate

```text
support prime limit                    = 11
support face sizes                     = 1,2,3
integer cap                            = 100000
support faces                          = 25
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

Route decomposition:

```text
contains axis 2:
  11 faces / 653 points / 650 representable / 217929 pairs

excludes axis 2:
  14 faces / 231 points / 95 representable / 95 pairs
```

Inside the frozen box, the only nonrepresentable points on supports containing axis 2 are `2,4,6`. This is `FINITE-VERIFIED`, not a global statement.

## 7. PASS-002 centered-radius capability

\[
D(N)=
\begin{cases}
\{\Delta/2:\Delta\in\Delta_2(N)\},&N\text{ even},\\
\Delta_2(N),&N\text{ odd}.
\end{cases}
\]

Exact laws:

```text
N=2m and d in D(N) => (p,q)=(m-d,m+d)
N odd and represented => d=N-4 and (p,q)=(2,d+2)
(N,D(N)) reconstructs the complete distinct-prime fiber
|D(N)|=|R_2(N)|
represented odd points have no internal coordinate collision
```

Finite certificate:

```text
total coordinate occurrences                 = 218024
unique coordinate values                     = 36797
unique even-route coordinate values          = 36787
unique odd-route coordinate values           = 95
cross-route coordinate values                = 85
odd-only coordinate values                   = 10
unique spectra including empty               = 744
unique nonempty spectra                      = 743
nonempty spectrum collision classes          = 1
proper containment edges                     = 2048
non-singleton-subset containment edges       = 10
shared coordinate values                     = 27799
odd/odd shared coordinate values             = 0
```

The only nonempty complete-spectrum collision is

\[
D(5)=D(8)=D(12)=\{1\}.
\]

The most widely shared coordinate is \(d=7\), at 64 frozen points.

```text
(N,D(N)) = lossless for the complete pair fiber
D(N) alone = generally loses N, midpoint, support label, and pair labels
```

Classification: `IDENTITY / PROVED / FINITE-VERIFIED / INTERPRETATION`.

## 8. Checkpoints and active subpass

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

PASS-003 may build only static coordinate-owner incidence structures inside the unchanged 884-point box:

```text
coordinate d
→ owning integer points O(d)
→ owning support faces F(d)
→ parity-route class
```

Finite graph or hypergraph language is permitted only for static incidence. Iteration, orbit dynamics, basins, attractors, cap expansion, weighting, and asymptotics are blocked.

## 9. Computational capability

Installed on the draft branch:

- exact Python generators;
- independent sieve and independently structured scans;
- exact-support membership guards;
- deterministic JSON certificates and digest checks;
- complete-box unit tests;
- Goal Memory, Research Compass, honesty, state-coherence, and governance audits;
- analytical and immersive visual laboratories.

These tools support reproducibility and discovery. They do not replace proof.

## 10. Translation and maturation capability

```text
closed Language Kernel v1 families = 8
TRANSLATION-KERNEL-V2-PASS-001 = checkpoint_pass
PVG-ANT-BENCHMARK-001 = checkpoint_pass
TRANSLATION-KERNEL-V2-PASS-002 = checkpoint_pass
combined translation inventory = 44
L3 promotions = 0
GOVERNANCE-ENFORCEMENT-CLOSURE-001 = CLOSED
CENTRAL-MIND-CONTINUITY-001 = installed_repository_side
CENTRAL-MIND-CONTINUITY-CLOSURE-002 = closed
Current maturation receipt = MATURATION-RECEIPT-007
```

These are retained supporting capabilities and do not create a second active front.

```text
ADVERSARIAL-PVG-ANT-BENCHMARK-002 = NOT_STARTED
Dataset 004 remains unauthorized
trained neural network = none
approved training corpus = none
```

## 11. Retained source-grounded ANT tools

The installed book-layer substrate remains available on demand without governing the active research program.

```text
MNTII-006-E = CLOSED
v0.6-e-closure = PASS
TOOL-MONTGOMERY-BOUNDED-GAPS-DIAGNOSTIC-001 = retained live diagnostic
A/B/legacy-E = quarantined / source-mismatch / not live
```

The bounded-gaps diagnostic is a retained capability, not a current theorem target. The source-grounding-corrected Montgomery history and its quarantine markers remain binding negative memory.

## 12. Scientific ceiling

The current system provides exact inverse-coordinate theory, corrected data contracts, complete finite verification, and governed computational infrastructure.

It does not provide:

- an original certified lemma or theorem;
- an asymptotic representation estimate;
- a global reachability or termination theorem;
- historical originality certification;
- publication readiness;
- Goldbach, PNT, RH, or GRH progress;
- a trained research model or approved training corpus.

**Classification:** exact/proved inverse geometry plus finite-verified infrastructure under ENGINE-004.
