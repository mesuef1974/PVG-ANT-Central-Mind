# ENGINE-004 PASS-003 — Centered-Radius Incidence Readiness

```text
Task ID: ENGINE-004-PASS-003-CENTERED-RADIUS-INCIDENCE
Goal ID: GOAL-OP-INVERSE-PRIME-FIBERS-001
Parent program: GOAL-PVG-INVERSE-GEOMETRY-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Decision: READY
Status: ACTIVE_CURRENT_SUBPASS
Date: 2026-07-22
Phase D: NOT AUTHORIZED
```

## Research question

Inside the already certified 884-point box, what exact finite incidence geometry is induced by the governed centered-radius coordinates?

For

\[
D(N)=
\begin{cases}
\{\Delta/2:\Delta\in\Delta_2(N)\},&N\text{ even},\\
\Delta_2(N),&N\text{ odd},
\end{cases}
\]

define

\[
\mathcal O(d)=\{N:d\in D(N)\},
\qquad
\mathcal F(d)=\{\operatorname{supp}(N):N\in\mathcal O(d)\}.
\]

The pass asks how coordinates, prime-pair occurrences, integer owners, support faces, and parity routes are related without conflating these layers.

## Frozen domain

```text
support prime limit = 11
support face sizes = 1,2,3
integer cap = 100000
support faces = 25
integer points = 884
represented points = 745
coordinate occurrences = 218024
unique governed coordinates = 36797
```

No expansion is permitted inside PASS-003.

## Preregistered objects

```text
coordinate d
pair occurrence (p,q,N,d)
integer-owner set O(d)
support-owner set F(d)
route-conditioned owner sets O_even(d), O_odd(d)
coordinate incidence hypergraph
coordinate co-occurrence relation induced by spectra D(N)
integer-to-support projection of incidence
```

## Required exact identities

The pass may reuse but must independently verify:

- \(d\in D(N)\) if and only if its exact reconstruction is a registered distinct-prime pair over \(N\);
- \(|D(N)|=|\mathcal R_2(N)|\);
- represented odd points have coordinate \(d=N-4\);
- odd-route coordinate ownership is injective;
- the integer-owner incidence relation reconstructs every nonempty spectrum by row restriction;
- projecting integer owners to support faces is surjective onto \(\mathcal F(d)\) by definition but need not be injective.

Any stronger statement requires a proof or finite certificate.

## Preregistered finite outputs

The deterministic summary must include:

1. coordinate degree distribution \(d\mapsto|\mathcal O(d)|\);
2. support degree distribution \(d\mapsto|\mathcal F(d)|\);
3. route decomposition of every shared coordinate;
4. cross-route coordinate inventory;
5. coordinate values with maximal integer degree and support degree;
6. count of coordinates collapsing multiple integer owners onto one support face;
7. support-pair intersection counts;
8. complete nonzero coordinate co-occurrence counts or a lossless compressed certificate;
9. connected components only for a single preregistered, non-iterated incidence graph definition;
10. independent scan mismatch count;
11. deterministic ordering and SHA-256;
12. claim-ceiling flags.

Exact numerical values are not preregistered here; they must be generated and independently reproduced before interpretation.

## Required separation

```text
same coordinate ≠ same prime pair
same coordinate ≠ same midpoint
same coordinate ≠ same integer
same support face ≠ same exponent vector
same support projection ≠ same integer-owner incidence
finite graph connectivity ≠ orbit dynamics
```

## Verification design

Production route:

- reuse certified integer points and governed spectra;
- build direct coordinate-owner and support-owner indexes;
- sort all emitted records deterministically.

Independent route:

- rescan every registered prime pair;
- derive its governed coordinate directly from parity and gap;
- rebuild owner/support/route sets without calling the production index builder;
- compare all 218,024 occurrences and all registered aggregate fields.

Required tests:

- small hand-checkable examples including \(d=1\) and \(d=7\);
- all 884 points;
- all 218,024 occurrences;
- all 36,797 unique coordinates;
- exact support projection;
- independent equality;
- rejection of malformed or out-of-domain incidence records;
- claim-ceiling assertions.

## Admissible graph language

A finite bipartite graph or hypergraph may be used only as a static representation of incidence in the frozen box.

Not admitted:

- iterating a graph map;
- defining orbits, basins, attractors, or transitions;
- inferring behavior outside the frozen box;
- treating connectedness as an asymptotic or arithmetic theorem.

These require Phase D or another explicit readiness decision.

## Required artifacts

```text
tools/pvg_centered_radius_incidence.py
tests/test_pvg_centered_radius_incidence.py
research/pvg-space-deepening/engine-004-pass-003-centered-radius-incidence.md
research/pvg-space-deepening/data/centered-radius-incidence-summary.json
.github/workflows/pvg-centered-radius-incidence-audit.yml
governance/checkpoints/ENGINE-004-PASS-003-CENTERED-RADIUS-INCIDENCE-001.md
```

Equivalent governed names are acceptable if consistently registered.

## Stop rule

Stop PASS-003 and return to the ENGINE-004 parent review when:

- all preregistered incidence outputs are certified; or
- a mismatch reveals a defect in PASS-001/PASS-002; or
- the task requires cap expansion, iteration, weighting, averaging, or asymptotics.

Do not open another subpass automatically after closure.

## Claim ceiling

```text
historical originality = false
original lemma/theorem = false
Phase D authorized = false
Goldbach progress = false
PNT progress = false
RH progress = false
GRH progress = false
publication readiness = false
```

**Honest classification:** ready for exact static finite-incidence analysis under ENGINE-004 only.
