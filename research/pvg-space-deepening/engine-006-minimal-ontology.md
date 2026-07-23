# ENGINE-006 WP-2 — Minimal Ontology

```text
Engine: ENGINE-006
Work package: WP-2 — Minimal Ontology
Parent goal: GOAL-PVG-INVERSE-GEOMETRY-001
Status: COMPLETE_FOR_REVIEW
Experimental expansion: NOT USED
Phase D: NOT AUTHORIZED
Date: 2026-07-23
```

## 1. Governing conclusion

The nine candidate terms do not define nine independent mathematical objects. The smallest nonredundant ontology needed to recover all exact ENGINE-004 reconstruction and information-loss statements has:

```text
CORE OBJECT A: an integer point, presented either as N or as its finite-support valuation vector nu(N)
CORE OBJECT B: the typed distinct-prime representation relation over that point
```

The two presentations `N` and `nu(N)` are a typed equivalence, not two independent primitives. Support, parity route, prime-pair fiber rows, centered coordinates, spectra, owner incidence, and support incidence are derived objects or projections.

This is a minimal ontology for the completed inverse-geometry program, not a claim that arithmetic itself has only two primitive notions.

## 2. Ambient standard structure

The following are treated as standard background and are not counted as new PVG primitives:

```text
positive integers
prime predicate / set of primes
finite sets and relations
gcd, parity, addition, subtraction
finite-support exponent vectors
```

Their use carries no novelty claim.

## 3. Retained core objects

### O1 — Integer point with valuation presentation

For `N >= 1`,

\[
\nu(N)=(\nu_p(N))_p
\]

has finite support and determines `N` by

\[
N=\prod_p p^{\nu_p(N)}.
\]

```text
Role: base point to which every fiber, coordinate row, support label, and route label is attached
Status: PRIMITIVE GOVERNED OBJECT with two TYPED-EQUIVALENT presentations
Presentations: N <-> nu(N)
Retains: complete multiplicative identity of N
Loses: nothing when the full finite-support vector is retained
```

Minimality witness: removing the base point makes `D(N)` generally noninjective and destroys fixed-base reconstruction of prime pairs.

### O2 — Typed distinct-prime representation relation

Define the relation

\[
\mathcal R=\{(N,p,q):p<q,\ p,q\text{ prime},\ p+q=N\}.
\]

Equivalently, the fiber over `N` is

\[
\mathcal R_2(N)=\{(p,q):(N,p,q)\in\mathcal R\}.
\]

```text
Role: arithmetic content being represented by centered coordinates
Status: PRIMITIVE GOVERNED RELATION
Dependencies: integer base type and standard prime predicate
Retains: pair labels, base point, ordering convention, multiplicity
Loses: nothing inside its declared distinct unordered-pair convention
```

Minimality witness: valuation data alone does not determine the additive prime-pair fiber; the representation relation cannot be reconstructed from support or parity labels.

## 4. Derived objects

### D1 — Support

\[
\operatorname{supp}(N)=\{p:\nu_p(N)>0\}.
\]

```text
Status: DERIVED from O1
Role: multiplicative face label
Retains: which prime coordinates are nonzero
Loses: all positive exponent values and therefore integer identity
```

### D2 — Parity route

\[
\rho(N)=
\begin{cases}
\text{even route},&2\in\operatorname{supp}(N),\\
\text{odd route},&2\notin\operatorname{supp}(N).
\end{cases}
\]

```text
Status: DERIVED from D1, equivalently from N mod 2
Role: selects the normalization and the possible prime-pair form
Retains: one parity bit
Loses: all remaining valuation, support, integer, and multiplicity information
```

### D3 — Prime-pair fiber

`R_2(N)` is the row/fiber of O2 over the retained base point `N`.

```text
Status: DERIVED FIBER, not a separate primitive
Role: fixed-base representation set
Retains: all pair labels over N
Loses: nothing relative to O2 when N is retained
```

### D4 — Centered coordinate

For `(N,p,q)` in O2,

\[
\Delta=q-p.
\]

For even `N=2m`, define `d=\Delta/2`; for represented odd `N`, the governed coordinate is `d=\Delta=N-4`.

```text
Status: DERIVED COORDINATE
Role: sum-and-difference parametrization of a pair in a typed fiber
Retains: the pair exactly only together with N and the route convention
Loses: midpoint/base point and pair labels when used alone
```

### D5 — Governed spectrum row

\[
D(N)=\{d:(N,p,q)\in\mathcal R\text{ and }d\text{ is the governed coordinate of }(p,q)\}.
\]

```text
Status: DERIVED IMAGE of the fiber under D4
Role: coordinate presentation of R_2(N)
Retains: full fiber multiplicity and reconstruction when N is retained
Loses: N, support, midpoint, and pair identity when detached from N
```

### D6 — Integer-coordinate incidence relation

\[
I=\{(N,d):d\in D(N)\}.
\]

```text
Status: DERIVED RELATION / transpose-compatible presentation of all spectrum rows
Role: global row-column view of D(N)
Retains: every nonempty D(N) row when integer labels are retained
Loses: direct prime-pair labels unless reconstruction uses N and route
```

### D7 — Support-coordinate incidence

\[
I_{\mathrm{supp}}=\{(\operatorname{supp}(N),d):(N,d)\in I\}.
\]

```text
Status: DERIVED LOSSY PROJECTION of D6
Role: support-conditioned ownership summary
Retains: existence of at least one owner with a given support
Loses: integer identity, exponent vector, owner multiplicity unless separately counted, and pair labels
```

## 5. Aliases removed

```text
centered gap / centered radius
  -> route-dependent presentations of D4

prime-pair fiber / fixed-base governed spectrum
  -> typed-equivalent presentations D3 and (N,D5), not identical without N

owner graph / incidence matrix
  -> presentations of D6

support owner / support projection
  -> row/column language for D7

static component / connected component
  -> ordinary graph-theoretic property derived from D6 or D7
```

These terms may remain as explanatory vocabulary, but they are not separate primitives or independent mathematical evidence.

## 6. Map audit

| Map | Type | Retained labels | Exact status | Information loss |
|---|---|---|---|---|
| `nu(N) -> N` | BIJECTION onto positive integers | full prime-indexed finite-support vector | exact fundamental-factorization recovery | none |
| `N -> nu(N)` | BIJECTION | integer identity | exact | none |
| `N -> supp(N)` | LOSSY PROJECTION | base integer only at input | exact definition | exponents and integer identity |
| `N -> rho(N)` | LOSSY PROJECTION | base integer only at input | exact parity map | all but parity bit |
| `(N,p,q) -> (N,Delta)` | TYPED EQUIVALENCE | fixed N, route, pair convention | exact | none with N retained |
| `(N,Delta) -> (N,p,q)` | PARTIAL MAP / BIJECTION on admissible typed image | N and admissibility conditions | exact on image | undefined off admissible image |
| `(N,R_2(N)) -> (N,D(N))` | TYPED EQUIVALENCE | N and route normalization | exact | none |
| `(N,D(N)) -> (N,R_2(N))` | TYPED EQUIVALENCE | N and route normalization | exact | none |
| `D(N) without N` | LOSSY PROJECTION | coordinate set only | exact projection | base point, midpoint, support, pair labels |
| `I -> {D(N)}` | TYPED EQUIVALENCE for registered nonempty rows | integer labels | exact row reconstruction | empty rows require external registry |
| `I -> I_supp` | LOSSY PROJECTION | support image | exact image map | integer owners, exponents, pair labels |
| `supp(N) -> rho(N)` | SURJECTION onto two route classes within the governed domain | support label | exact via membership of 2 | all support detail except presence of 2 |

## 7. Dependency diagram

```text
standard primes + positive integers
             |
             v
O1: N <-----------------------> nu(N)
 |                                  |
 |                                  v
 |                              D1: supp(N)
 |                                  |
 |                                  v
 |                              D2: rho(N)
 |
 +---- O2: R relation (N,p,q)
              |
              +--> D3: R_2(N)
              |
              +--> D4: centered coordinate
                         |
                         v
                     D5: D(N)
                         |
                         v
                     D6: I(N,d)
                         |
                         v
                     D7: I_supp(supp(N),d)
```

Every downward projection may lose information. Horizontal typed equivalences are lossless only with all displayed labels retained.

## 8. Minimality result

The candidate list reduces as follows:

```text
primitive governed objects/relations = 2
  O1 integer point with valuation presentation
  O2 typed distinct-prime representation relation

derived objects = 7
  support
  parity route
  prime-pair fiber row
  centered coordinate
  spectrum row
  integer-coordinate incidence
  support-coordinate incidence

independent aliases retained = 0
```

Why two are necessary:

1. O1 cannot be removed because all recoverability claims are typed over a retained base point and because support/route are functions of it.
2. O2 cannot be removed because multiplicative valuation data does not determine additive prime-pair representations.
3. Every other governed object is definable from O1 and O2 using standard set, arithmetic, and projection operations.

**Classification:** the definitions are `IDENTITY`; the dependency and minimality consequences are `PROVED` relative to the declared ENGINE-004 language. This does not prove categorical or foundational minimality among every conceivable formalization.

## 9. Information-retention summary

```text
FULL INFORMATION:
  N <-> nu(N)
  (N,R_2(N)) <-> (N,D(N))
  typed admissible (N,Delta) <-> (N,p,q)

PARTIAL INFORMATION:
  support
  parity route
  D(N) without N
  support-coordinate incidence
  graph summaries and component counts
```

The durable contribution is therefore not a new primitive arithmetic object. It is a disciplined typed map system that makes recoverability and information loss explicit.

## 10. Unresolved ontology questions

```text
OPEN-1: whether the representation relation O2 should be treated as part of PVG or as an external additive relation placed over the valuation space
OPEN-2: whether a future framework gains proof power by retaining D6 as a first-class object rather than a derived database view
OPEN-3: whether any nontrivial theorem depends essentially on the combined multiplicative/additive typing rather than on standard additive parametrization alone
OPEN-4: independent-theory status remains OPEN pending standard-structure and proposition audits
```

## 11. Work-package decision

```text
WP-2 MINIMAL ONTOLOGY = COMPLETE_FOR_REVIEW
WP-3 RECONSTRUCTION AND LOSS AUDIT = NOT YET OPENED
new experiment = NOT AUTHORIZED
Phase D = NOT AUTHORIZED
```

No original theorem, novelty, publication-readiness, Goldbach, PNT, RH, or GRH claim is certified.