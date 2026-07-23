# ENGINE-006 WP-1 — Inverse-Geometry Synthesis Claim Ledger

```text
Engine: ENGINE-006
Work package: WP-1 — Claim inventory
Parent goal: GOAL-PVG-INVERSE-GEOMETRY-001
Input chain: ENGINE-004 PASS-001 through PASS-004
Status: COMPLETE_FOR_REVIEW
Experimental expansion: NOT USED
Phase D: NOT AUTHORIZED
Date: 2026-07-23
```

## 1. Ledger rules

Each row records one material claim rather than one sentence occurrence. Repeated formulations are consolidated under one claim ID. The allowed scientific labels are:

```text
IDENTITY
PROVED
FINITE-VERIFIED
INTERPRETATION
HYPOTHESIS
OPEN
```

`DIAGNOSTIC`, `KNOWN`, and governance labels from source documents are retained only as notes; they are not substituted for the six governing labels.

The ledger does not certify novelty. A new geometric phrase does not create a new theorem.

## 2. Consolidated claim ledger

| Claim ID | Source | Object | Consolidated statement | Classification | Basis | Standard antecedent | Information added | Information lost | Scope ceiling |
|---|---|---|---|---|---|---|---|---|---|
| E6-C001 | PASS-001 | prime-pair fiber | For fixed `N`, `R_2(N)={{p,q}:p<q, p+q=N}` is the governed distinct unordered prime-pair fiber. | IDENTITY | definition | additive representation set | explicit fiber object | none | distinct pairs only |
| E6-C002 | PASS-001 | centered gap | `Delta=q-p` and fixed `(N,Delta)` recover `p=(N-Delta)/2`, `q=(N+Delta)/2`. | IDENTITY | direct algebra | sum-and-difference coordinates | lossless coordinate chart over fixed `N` | discarding `N` loses midpoint | no novelty claim |
| E6-C003 | PASS-001 | parity | Every admitted coordinate satisfies `Delta ≡ N (mod 2)`. | PROVED | parity of sum/difference | elementary parity | admissibility filter | no pair labels by itself | exact, global for governed pairs |
| E6-C004 | PASS-001 | factor identity | `N^2-Delta^2=4pq`. | IDENTITY | algebraic expansion | difference of squares | product relation | does not determine primality alone | exact |
| E6-C005 | PASS-001 | gcd | `gcd(N,Delta)=gcd(N,2)` for distinct prime pairs. | PROVED | common-divisor argument | elementary gcd law | coprimality constraint | no multiplicity information | exact for governed distinct pairs |
| E6-C006 | PASS-001 | midpoint-radius | For even `N=2m`, `d=Delta/2`, one has `p=m-d`, `q=m+d`, and `gcd(m,d)=1`. | PROVED | E6-C002 and E6-C005 | standard midpoint parametrization | normalized coordinate form | `d` alone loses `m` | exact |
| E6-C007 | PASS-001 | support route | `2 in supp(N)` iff `N` is even; even governed pairs are odd+odd, while odd `N` has at most `{2,N-2}`. | PROVED | factor-support parity | elementary parity and unique even prime | route decomposition | support beyond presence of 2 is discarded | exact |
| E6-C008 | PASS-001 | data contract | `prime_fiber_record(N,F)` must reject `F != supp(N)`. | IDENTITY | object-consistency requirement | typed data validation | prevents label leakage | no mathematical content beyond consistency | implementation contract |
| E6-C009 | PASS-001 | frozen certificate | All 884 registered fibers matched an independent scan; 218024 pair occurrences were recorded. | FINITE-VERIFIED | deterministic certificate and tests | exhaustive bounded enumeration | complete governed-box validation | no statement beyond frozen box | primes<=11, support size<=3, N<=100000 |
| E6-C010 | PASS-001 | nonrepresentation | In the frozen box, the only nonrepresented points whose support contains 2 are `2,4,6`. | FINITE-VERIFIED | complete enumeration | bounded observation | exact finite exception list | no global Goldbach implication | frozen box only |
| E6-C011 | PASS-002 | governed spectrum | `D(N)={Delta/2}` for even `N` and `D(N)={Delta}` for odd `N`. | IDENTITY | definition | coordinate normalization | unified route-dependent spectrum | normalization hides original scale unless route known | governed convention only |
| E6-C012 | PASS-002 | odd route | For represented odd `N`, the unique governed coordinate is `d=N-4`, recovering `(2,d+2)`. | PROVED | E6-C007 | unique even-prime route | injective odd coordinate encoding | no extra support data | exact |
| E6-C013 | PASS-002 | reconstruction | `(N,D(N))` reconstructs the complete distinct-prime fiber and `|D(N)|=|R_2(N)|`. | PROVED | coordinatewise application of E6-C002/E6-C006/E6-C012 | finite set transport under bijection | lossless compressed representation over fixed base | `D(N)` alone is generally lossy | exact |
| E6-C014 | PASS-002 | odd injectivity | Two represented odd points cannot share the same governed coordinate. | PROVED | `N=d+4` | elementary injectivity | route-specific uniqueness | says nothing about even owners | exact |
| E6-C015 | PASS-002 | spectrum collisions | The only nonempty complete-spectrum collision in the frozen box is `D(5)=D(8)=D(12)={1}`. | FINITE-VERIFIED | complete spectrum certificate | bounded set comparison | collision inventory | no global collision theorem | frozen box only |
| E6-C016 | PASS-002 | containment | Frozen-box spectrum containment counts and the three non-singleton proper-subset spectra are exactly those certified. | FINITE-VERIFIED | exhaustive certificate | finite poset computation | bounded inclusion geometry | no asymptotic law | frozen box only |
| E6-C017 | PASS-002 | projection loss | `D(N)` without `N` generally loses midpoint, integer identity, support, and prime-pair labels. | PROVED | explicit noninjectivity/collisions | projection theory | precise loss statement | deliberately discards base point | exact qualitative statement |
| E6-C018 | PASS-002 | geometric spectrum language | Calling `D(N)` a centered-radius spectrum is a geometric reformulation of a finite coordinate fiber. | INTERPRETATION | terminology | additive parametrization | visualization and organization | no new arithmetic force established | no novelty claim |
| E6-C019 | PASS-003 | coordinate owners | `O(d)={N:d in D(N)}` and the incidence relation reconstructs every nonempty row `D(N)`. | IDENTITY | transpose of membership relation | bipartite incidence matrix | column/row dual view | empty rows need separate registration | exact |
| E6-C020 | PASS-003 | support projection | `F(d)={supp(N):N in O(d)}` is the support projection of integer owners and may collapse distinct owners. | PROVED | image under support map | set-image projection | support-conditioned incidence | loses exponent vector and integer identity | exact |
| E6-C021 | PASS-003 | static components | Connected components are properties of the static bipartite incidence graph, not orbits, basins, attractors, or dynamics. | PROVED | definition of graph component | graph theory | prevents dynamical overinterpretation | no temporal structure | exact boundary statement |
| E6-C022 | PASS-003 | odd owner incidence | No governed coordinate has two odd integer owners. | PROVED | E6-C014 | injectivity | route-conditioned degree bound | no bound for even owners | exact |
| E6-C023 | PASS-003 | incidence counts | Shared-coordinate counts, support intersections, owner degrees, co-occurrences, and 12 static components are exactly as certified. | FINITE-VERIFIED | exhaustive incidence certificate | bounded bipartite graph computation | complete finite incidence profile | no general graph law | frozen box only |
| E6-C024 | PASS-003 | support incidence language | Viewing prime-pair coordinates as nodes incident to integer and support owners is a bipartite/hypergraph reinterpretation. | INTERPRETATION | representational equivalence | standard incidence structures | exposes recoverability and projection | does not create new arithmetic relations | no novelty claim |
| E6-C025 | PASS-004 | support strata | Grouping points by exact support, support size, parity route, or decimal bin is a stratification of the finite registry. | IDENTITY | definitions | ordinary partitioning/grouping | conditioned summaries | grouping can discard integer identity and exponents | finite registry convention |
| E6-C026 | PASS-004 | support non-determination | In the frozen box, equal exact support does not determine representation multiplicity. | FINITE-VERIFIED | explicit counterexample witnesses | finite counterexample logic | falsifies a bounded deterministic claim | does not establish distributional independence | frozen box witness |
| E6-C027 | PASS-004 | support-size non-determination | In the frozen box, equal support size does not determine representation multiplicity. | FINITE-VERIFIED | explicit witnesses | finite counterexample logic | removes coarse deterministic explanation | no general statistical conclusion | frozen box witness |
| E6-C028 | PASS-004 | parity/bin non-determination | In the frozen box, parity plus decimal bin does not determine exact support. | FINITE-VERIFIED | explicit witnesses | finite counterexample logic | records residual support variation | no causal conclusion | frozen box witness |
| E6-C029 | PASS-004 | rank reversals | Four conditioned rank reversals and 50 matched-neighborhood witnesses occur in the certified registry. | FINITE-VERIFIED | deterministic grouped arithmetic | bounded descriptive comparison | exact diagnostic inventory | no significance, causality, or stability claim | frozen box only |
| E6-C030 | PASS-004 | causal support effect | Exact support has a causal or independent effect on prime-pair multiplicity after controlling other variables. | OPEN | not established | causal/statistical inference would be required | potential research question | current certificates are insufficient | no claim admitted |
| E6-C031 | PASS-004 | general support law | There exists a general law connecting support geometry to representation multiplicity. | OPEN | no theorem or valid extrapolation | additive number theory / probabilistic modelling | possible future target | current finite diagnostics insufficient | outside present authorization |
| E6-C032 | ENGINE-004 closure | program value | ENGINE-004 provides a coherent exact data model, lossless fixed-base coordinates, and explicit information-loss maps. | PROVED | synthesis of E6-C001–E6-C024 | standard algebra plus typed incidence representation | durable organizational infrastructure | theorem/novelty value not implied | exact framework claim |
| E6-C033 | ENGINE-004 closure | independent theory | The completed inverse-geometry language constitutes a mathematically independent new theory. | OPEN | not established | requires nonredundancy, prior-art, and theorem audits | central ENGINE-006 question | terminology and finite computation are insufficient | no claim admitted |

## 3. Classification totals

```text
IDENTITY         = 8
PROVED           = 12
FINITE-VERIFIED  = 9
INTERPRETATION   = 2
HYPOTHESIS       = 0
OPEN             = 2
TOTAL            = 33
```

The absence of `HYPOTHESIS` rows is deliberate. ENGINE-004 closed without admitting a preregistered predictive mechanism. Candidate causal or general-law statements remain `OPEN`, not hypotheses supported by the completed certificates.

## 4. Redundancy consolidation

The following source phrases are not independent claims:

```text
centered gap / centered radius / midpoint-radius coordinate
  -> one sum-and-difference coordinate family with route-dependent normalization

prime-pair fiber / governed spectrum over fixed N
  -> bijective presentations once N is retained

coordinate-owner graph / incidence matrix / owner relation
  -> equivalent presentations of membership d in D(N)

support owner / support projection
  -> image of integer-owner incidence under N -> supp(N)

static component
  -> ordinary connected component; no dynamical content
```

## 5. First synthesis conclusion

The durable content currently established is not a new arithmetic law. It is a controlled representational stack:

```text
prime pair
  <-> fixed-base centered coordinate
  <-> spectrum row
  <-> incidence membership
  -> support projection
  -> route projection
```

The first four arrows are lossless only when their required base labels are retained. The final projections are lossy. The finite certificates measure the behavior of these maps in one frozen registry; they do not promote the maps into asymptotic or causal laws.

## 6. Work-package decision

```text
WP-1 CLAIM INVENTORY = COMPLETE_FOR_REVIEW
WP-2 MINIMAL ONTOLOGY = NOT YET OPENED
new experiment = NOT AUTHORIZED
Phase D = NOT AUTHORIZED
```

**Honest conclusion:** ENGINE-004 established an exact and reproducible coordinate/incidence organization of bounded additive prime-pair fibers. Whether that organization is nonredundant enough to support an independent theory remains `OPEN` and is the purpose of later ENGINE-006 work packages.