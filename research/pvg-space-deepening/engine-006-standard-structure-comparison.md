# ENGINE-006 WP-4 — Standard-Structure Comparison

```text
Task ID: ENGINE-006-WP-4-STANDARD-STRUCTURE-COMPARISON
Parent goal: GOAL-PVG-INVERSE-GEOMETRY-001
Engine: ENGINE-006
Status: COMPLETE
Date: 2026-07-23
New experiment: NOT AUTHORIZED
Novelty claim: NOT AUTHORIZED
```

## 1. Governing question

Does the retained ENGINE-006 framework contain mathematical information or proof power that is not reconstructible from standard antecedent structures?

The comparison classes are:

```text
EQUIVALENCE
SPECIALIZATION
REINTERPRETATION
STRICTLY LESS INFORMATIVE
STRICTLY MORE INFORMATIVE
UNRESOLVED
```

A geometric vocabulary, a finite certificate, or a useful combination of standard structures is not by itself evidence for a new theory.

## 2. Retained ENGINE-006 core

WP-2 reduced the working ontology to:

```text
O1: integer object with typed-equivalent presentations N <-> nu(N)
O2: typed distinct-prime representation relation
    R = {(N,p,q): p<q, p+q=N}
```

WP-3 established a reversible layer and a forgetful layer.

Reversible layer:

```text
N <-> nu(N)
(N,p,q) <-> admissible (N,Delta)
(N,R_2(N)) <-> (N,D(N))
representation relation <-> integer-coordinate incidence
```

Forgetful layer:

```text
N -> supp(N)
N -> parity route
supp(N) -> parity route
(N,D(N)) -> D(N)
integer-coordinate incidence -> support-coordinate incidence
registered empty rows -> omission from bare incidence
```

## 3. Comparison matrix

| ENGINE-006 object or claim | Standard antecedent | Classification | Reason |
|---|---|---|---|
| `N <-> nu(N)` | finite-support valuation vector / unique factorization | EQUIVALENCE | The integer and its finitely supported exponent vector determine each other exactly. |
| multiplication as vector addition | free commutative monoid on primes | EQUIVALENCE | This is the standard monoid isomorphism induced by unique factorization. |
| divisibility as coordinatewise order | divisor poset / product order | EQUIVALENCE | `a | b` iff `nu_p(a) <= nu_p(b)` for every prime `p`. |
| gcd/lcm as coordinatewise min/max | divisor lattice | EQUIVALENCE | These are standard lattice operations in valuation coordinates. |
| support face `supp(N)` | support stratification of finitely supported vectors | REINTERPRETATION | The geometric term “face” is useful language, but the object is exactly the nonzero-coordinate set. |
| support size / level | number of distinct prime factors `omega(N)` | EQUIVALENCE | No additional invariant is introduced. |
| prime-power rays | coordinate axes in the free commutative monoid | REINTERPRETATION | Geometric imagery reorganizes a standard basis description. |
| support projection | coordinate-support map | EQUIVALENCE | The map is the usual forgetful map deleting positive exponent values. |
| parity route | residue class modulo 2 / indicator `2 in supp(N)` | EQUIVALENCE | For positive integers, parity is completely determined by the 2-coordinate. |
| divisor box below `N` | finite product of chains `[0,nu_p(N)]` | EQUIVALENCE | This is the standard divisor lattice interval. |
| distinct-prime pair fiber `R_2(N)` | additive representation fiber of `p+q=N` | EQUIVALENCE | The fiber is standard additive number-theory data, merely typed over the base `N`. |
| centered coordinate `Delta=(q-p)/2` | standard midpoint/difference parametrization | EQUIVALENCE | With fixed `N`, the inverse formulas `p=N/2-Delta`, `q=N/2+Delta` recover the pair. |
| governed spectrum row `D(N)` | image of the prime-pair fiber under the difference coordinate | SPECIALIZATION | It is a chosen coordinate presentation of the standard additive fiber. |
| integer-coordinate incidence | bipartite incidence relation between bases and coordinates | EQUIVALENCE | The relation contains exactly the same nonempty row data when owners are retained. |
| support-coordinate incidence | quotient of owner incidence by equal support | STRICTLY LESS INFORMATIVE | Distinct integer owners with the same support are identified. |
| bare spectrum `D(N)` without `N` | forgetful image under base deletion | STRICTLY LESS INFORMATIVE | The base, midpoint, support, and route are not generally reconstructible. |
| empty-row registry | explicit domain metadata for a partial/incidence representation | REINTERPRETATION | The need to retain empty registered objects is standard data-model completeness, though important for proof hygiene. |
| coordinate-owner graph | incidence graph of a binary relation | EQUIVALENCE | Graph and incidence-matrix presentations are interchangeable. |
| connected components of the static graph | ordinary graph connected components | EQUIVALENCE | No new component notion is present. |
| complete typed reversible/forgetful diagram | composition of standard isomorphisms and forgetful maps | REINTERPRETATION | The value lies in unifying bookkeeping and loss control, not in a new primitive structure. |

## 4. Detailed comparisons

### 4.1 Valuation geometry and the free commutative monoid

Let

\[
\mathbb N_{>0}^{\times}
\longrightarrow
\mathbb N^{(\mathcal P)},
\qquad
N\longmapsto \nu(N),
\]

where `N^(P)` denotes finitely supported functions from the prime set to the nonnegative integers.

Unique factorization gives a monoid isomorphism:

\[
\nu(MN)=\nu(M)+\nu(N).
\]

Therefore the foundational multiplicative geometry is not merely analogous to the free commutative monoid on the primes; it is a coordinate presentation of that monoid.

Classification:

```text
EQUIVALENCE
```

The geometric vocabulary remains useful for visualization, pedagogy, and composing maps, but it does not create an additional algebraic object.

### 4.2 Divisibility, gcd, lcm, and divisor boxes

For positive integers:

\[
a\mid b
\iff
\nu_p(a)\leq \nu_p(b)\quad\text{for every prime }p.
\]

Also:

\[
\nu(\gcd(a,b))=\min(\nu(a),\nu(b)),
\qquad
\nu(\operatorname{lcm}(a,b))=\max(\nu(a),\nu(b)).
\]

The divisors of `N` form the product of finite chains:

\[
\prod_{p\mid N}\{0,1,\dots,\nu_p(N)\}.
\]

Classification:

```text
EQUIVALENCE
```

The “box” language is a geometric rendering of the standard divisor-lattice interval.

### 4.3 Support stratification

The support map

\[
\sigma(N)=\operatorname{supp}(N)
\]

forgets all positive exponent values while retaining only which prime coordinates are active.

Its fiber over a finite prime set `F` is:

\[
\sigma^{-1}(F)=
\left\{
\prod_{p\in F}p^{a_p}: a_p\geq 1
\right\}.
\]

The terms “support face,” “level,” and “ray” are useful geometric interpretations of standard support strata.

Classification:

```text
REINTERPRETATION
```

No strictly stronger invariant has been demonstrated.

### 4.4 Additive prime-pair parametrization

For fixed `N`, the distinct-prime representation fiber is

\[
R_2(N)=\{(p,q):p<q,\ p+q=N,\ p,q\text{ prime}\}.
\]

The centered coordinate

\[
\Delta=\frac{q-p}{2}
\]

has inverse formulas

\[
p=\frac N2-\Delta,
\qquad
q=\frac N2+\Delta.
\]

Hence, after retaining the base and admissible domain, this is a standard change of coordinates on the additive fiber.

Classifications:

```text
prime-pair fiber = EQUIVALENCE with standard additive representation fiber
centered coordinate = EQUIVALENCE with midpoint/difference parametrization
spectrum row D(N) = SPECIALIZATION as a chosen coordinate image
```

No new additive invariant has yet been proved.

### 4.5 Incidence structures

The relation

\[
I=\{(N,d):d\in D(N)\}
\]

is a standard binary relation, equivalently represented as:

```text
incidence matrix
bipartite graph
family of nonempty rows
```

When the registered domain and empty-row registry are retained, the complete row family is reconstructed. Without the empty-row registry, registered bases with empty fibers disappear.

Classification:

```text
EQUIVALENCE with a typed bipartite incidence structure
```

The explicit empty-row warning is important for data contracts and proof hygiene, but it is not a new incidence theory.

### 4.6 Quotient and forgetful maps

The maps

```text
N -> supp(N)
N -> parity route
(N,D(N)) -> D(N)
integer owner -> support owner
```

are ordinary forgetful or quotient maps. Their fibers measure exactly what was discarded.

Classifications:

```text
EQUIVALENCE with standard forgetful-map language
outputs are STRICTLY LESS INFORMATIVE than their typed inputs
```

The ENGINE-006 contribution here is the disciplined declaration of all labels needed for inversion.

## 5. Search for strictly more informative content

A retained ENGINE-006 object would be `STRICTLY MORE INFORMATIVE` than its standard antecedent only if it contained data not reconstructible from that antecedent.

The audit found no such object.

```text
STRICTLY MORE INFORMATIVE findings = 0
```

The combined typed package does place multiplicative and additive data in one governed diagram, but every current component and transition is reconstructible from:

```text
valuation vector of N
standard support map
standard additive representation relation
standard difference parametrization
standard incidence relation
standard forgetful maps
```

Thus the current combined framework is not proved to possess strictly greater information content than the collection of its standard antecedents.

## 6. Search for proof advantage

A proof advantage would require at least one result whose argument essentially depends on the combined PVG typing and cannot be translated back without loss into standard valuation, additive-fiber, and incidence language.

No such theorem is presently established.

```text
essential combined-typing theorem = NOT FOUND
proof-strength advantage = UNRESOLVED
```

The current framework may improve:

- proof hygiene;
- visualization;
- data contracts;
- tracking of reversible versus irreversible transformations;
- disciplined interaction between multiplicative and additive views.

These are real methodological benefits, but they are not yet evidence of stronger theorem-producing power.

## 7. Final classification ledger

```text
EQUIVALENCE
- N <-> nu(N)
- free commutative monoid presentation
- divisibility/order
- gcd/lcm lattice operations
- support size = omega(N)
- parity route
- divisor box
- prime-pair fiber
- centered coordinate with fixed base
- integer-coordinate incidence
- graph/matrix/component presentations

SPECIALIZATION
- governed spectrum row D(N)
- selected distinct-prime, ordered, centered coordinate convention

REINTERPRETATION
- rays, faces, levels, boxes as geometric language
- empty-row registry as explicit typed-domain metadata
- unified reversible/forgetful diagram

STRICTLY LESS INFORMATIVE
- support projection
- parity projection
- bare D(N) after deleting N
- support-owner incidence
- incidence with omitted empty registered rows

STRICTLY MORE INFORMATIVE
- none established

UNRESOLVED
- whether the combined multiplicative-additive typing yields an essential theorem
- whether the framework can support a genuinely new invariant
- whether it merits independent-theory status
```

## 8. Scientific conclusion

The strongest justified conclusion is:

> The current inverse-geometry framework is a rigorous, typed synthesis of standard valuation geometry, additive prime-pair parametrization, incidence structures, and forgetful maps. Its established value is organizational and diagnostic. It has not yet been shown to contain a new primitive arithmetic object, strictly greater information, or independent proof strength.

Classification:

```text
standard mathematical content = EQUIVALENCE / SPECIALIZATION
geometric language = REINTERPRETATION
project-level synthesis value = INTERPRETATION
strict novelty or independent theory = OPEN
```

## 9. Return rule

```text
ENGINE-006 WP-4 = COMPLETE
ENGINE-006 = RETURN_TO_PARENT_REVIEW
WP-5 Structural Proposition Audit = NOT AUTHORIZED AUTOMATICALLY
new experiment = NOT AUTHORIZED
Phase D = NOT AUTHORIZED
```

No originality, priority, publication-readiness, Goldbach, PNT, RH, or GRH claim is made.
