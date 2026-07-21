# PVG Space Deepening Research Agenda

**Program family:** `PVG-INVERSE-GEOMETRY-001`  
**Priority:** understand Prime Valuation Geometry itself before using it as decoration around another theorem target  
**Status:** research agenda only; no experiment pass is authorized by this file alone

---

## 1. Starting observation

A simple drawing of prime axes and valuation points exposed several exact structures at once:

- prime-support faces;
- fixed-\(\Omega\) simplex levels;
- Pascal counts of lattice points;
- primitive and composite rays;
- geometric sequences along every lattice direction;
- axis ratios as horizontal transfer generators;
- gcd recovery from adjacent pairs;
- additive and subtractive transitions to new support faces;
- divisor boxes below points and multiple cones above them;
- exponent partitions and Young-lattice shape growth.

The purpose of this agenda is to treat that visual discovery as a disciplined source of questions, not as proof of novelty.

---

## 2. Research firewall

Every item must be labeled as one of:

```text
IDENTITY
REINTERPRETATION
FINITE-DIAGNOSTIC
BOUNDARY
CANDIDATE-MECHANISM
OPEN-QUESTION
THEOREM-CANDIDATE
```

No item advances to `THEOREM-CANDIDATE` merely because it is visually striking. Required escalation steps are:

```text
exact definition
→ finite examples and counterexamples
→ symbolic derivation where possible
→ source and priority search
→ preregistered computation if needed
→ independent verification
→ theorem or negative closure
```

No Goldbach, RH, GRH, primality, or factorization breakthrough may be claimed from the agenda.

---

## 3. Domain A — intrinsic geometry of fixed prime faces

### Core objects

For a finite labeled prime set \(P=\{p_1,\ldots,p_s\}\), study

\[
C_P=\mathbb N_0^s
\]

and its level sections

\[
\Sigma_r(P)=\{a\in\mathbb N_0^s:\sum_i a_i=r\}.
\]

### Questions

1. What are the exact face, boundary, and incidence counts at every codimension?
2. What graph is obtained from unit transfers \(e_j-e_i\)?
3. What are its diameter, distance distribution, degree sequence, and automorphisms?
4. What are the adjacency and Laplacian spectra for finite \(s,r\)?
5. Which results depend only on \((s,r)\), and which depend on the prime labels?
6. How do quotient spaces by coordinate permutations compare with partition/Young lattices?
7. Which natural metrics are preserved or distorted by the arithmetic map
   \(a\mapsto\prod p_i^{a_i}\)?

### First finite pass

Enumerate all sections with

```text
2 <= s <= 5
1 <= r <= 12
```

and verify counts, graph distances, boundaries, automorphism candidates, and spectra.

**Current class:** identities plus finite combinatorial diagnostics.

---

## 4. Domain B — directional arithmetic

Every integer direction \(h\) yields

\[
Q(h)=\prod_i p_i^{h_i}
\]

and every admissible line yields a geometric sequence.

### Questions

1. How should directions be classified up to sign, scaling, support, and permutation?
2. Which directions remain inside one face, one level, or one support stratum?
3. Which finite linear operators preserve a direction?
4. What changes when the direction has positive, zero, or negative total height?
5. Can directions be organized into primitive direction classes with canonical representatives?
6. What is the correct notion of angular separation in exponent coordinates and log-weighted coordinates?
7. How does direction composition correspond to multiplication of ratios?

### Exact kernel

For a geometric line \(a_k=AQ^k\) and a finite filter

\[
P(E)=c_0+c_1E+\cdots+c_mE^m,
\]

we have

\[
P(E)a_k=AQ^kP(Q).
\]

The research question is not this identity itself, but what arithmetic information is carried by the factorization of \(P(Q)\).

**Current class:** identity plus open arithmetic classification.

---

## 5. Domain C — arithmetic functions on local neighborhoods

For a primitive horizontal move

\[
N\mapsto N\frac{p_j}{p_i},
\]

study the change in arithmetic observables.

### Priority observables

\[
\omega,\ \Omega,\ \tau,\ \sigma,\ \varphi,\ \mu,\ \lambda,
\]

as well as

\[
\log n,\quad \frac{\sigma(n)}n,\quad \frac{\varphi(n)}n,
\]

and residue/character values.

### Questions

1. Which functions are exactly affine in exponent coordinates?
2. Which become multiplicative ratios depending only on \((p_i,p_j,a_i,a_j)\)?
3. Which are monotone along an oriented horizontal line?
4. Which are convex or log-convex?
5. Which have extrema at vertices, boundaries, or balanced points?
6. Which local changes depend only on the axis pair and not the common base?
7. Which observables detect the boundary before an exponent reaches zero?

### Kill criterion

A pattern that disappears after normalization or reduces immediately to a standard one-line identity is recorded as a useful reinterpretation, not a new mechanism.

**Current class:** mixed identities and finite diagnostics.

---

## 6. Domain D — additive and subtractive face transitions

For adjacent points

\[
N=gp_i,\qquad M=gp_j,
\]

addition and subtraction give

\[
N+M=g(p_i+p_j),
\]

\[
|N-M|=g|p_i-p_j|.
\]

For points separated along a geometric direction, factors of

\[
Q^h+1,\qquad Q^h-1
\]

determine the new axes.

### Questions

1. Build a directed graph whose vertices are support faces and whose edges are induced by sums or differences.
2. Classify when total valuation height is preserved, increased, or decreased.
3. Identify periodic divisibility laws in \(Q^h\pm1\).
4. Separate primitive prime-divisor phenomena from repeated old-axis factors.
5. Measure how support dimension changes under local addition.
6. Determine which transitions are controlled entirely by the axis pair and which depend on the common base.
7. Connect the finite geometry to known cyclotomic factorizations and primitive-divisor theorems before claiming new structure.

**Current class:** exact reduction; distribution questions open.

---

## 7. Domain E — inverse geometry from incomplete observations

### Observation models

1. exact decimal integer only;
2. complete factorization;
3. partial factorization;
4. one adjacent neighbor;
5. several unlabeled neighbors;
6. pairwise gcds only;
7. ratios only;
8. short geometric progressions;
9. arithmetic-function values on a local ball;
10. residue or character projections.

### Questions

1. What is the smallest observation set that reconstructs the labeled support?
2. What reconstructs exponents but not labels?
3. What reconstructs the primitive ray?
4. When do multiple nonisomorphic points have identical local signatures?
5. Can uncertainty be represented as a finite union of faces, cones, or fibers?
6. What are explicit counterexamples to each invalid inverse claim?
7. How does noise or missing data change identifiability?

### Required output

Every inverse procedure must state:

```text
retained information
lost information
injective or noninjective
counterexample
certificate required for exact recovery
```

**Current class:** inverse-problem program.

---

## 8. Domain F — factorization and primality diagnostics

PVG may organize factorization clues, but it does not automatically create factors.

### Candidate experiments

1. Generate structured candidate neighbors and compute gcds with the target.
2. Compare axis-ratio searches with Fermat-style near-square searches.
3. Detect perfect-power rays before general factorization.
4. Use repeated local observations to recover a support subset.
5. Explore whether residue constraints prune candidate directions.
6. Test special families such as semiprimes with close factors, smooth numbers, and powerful numbers.

### Mandatory baselines

- trial division where appropriate;
- Fermat factorization for close factors;
- Pollard rho;
- ECM for suitable sizes;
- standard primality tests.

### Success criterion

A PVG method must improve a measurable quantity such as runtime, candidate count, memory, certificate clarity, or success rate on a preregistered family. A geometric retelling without measurable gain is classified as reinterpretation.

**Current class:** candidate mechanism; no speedup established.

---

## 9. Domain G — probability and random walks on levels

The horizontal neighbor graph admits natural walks that preserve \(\Omega\).

### Questions

1. What is the stationary distribution for symmetric and weighted axis-transfer walks?
2. How fast do walks mix on \(\Sigma_r(P)\)?
3. How do boundary effects change local degree and return probabilities?
4. What distributions of exponent shapes arise after quotienting labels?
5. What happens when transition probabilities are weighted by \(\log p\), prime gaps, or arithmetic-function changes?
6. Can random walks model constrained multiplicative perturbations of integers?
7. Which limiting laws are already standard multinomial/urn phenomena?

**Current class:** finite probability program; source normalization required.

---

## 10. Domain H — modular and character geometry

For a modulus \(q\), a valuation point maps to

\[
n\bmod q
\]

or to character phases

\[
\chi(n)=\prod_p\chi(p)^{v_p(n)}.
\]

### Questions

1. How do horizontal axis transfers act on residue fibers?
2. When does a direction have a finite period modulo \(q\)?
3. Which directions lie in the kernel of one or several characters?
4. Can local neighbor graphs be quotiented by residue or phase?
5. What information is lost when replacing labeled points by character energies?
6. Can arithmetic progressions be seen as unions of direction orbits under controlled hypotheses?

**Current class:** exact finite-group translation plus analytic-certification boundary.

---

## 11. Domain I — analytic distribution of geometric classes

### Counting questions

For \(n\le x\), count or weight points by:

- support size \(\omega(n)\);
- total height \(\Omega(n)\);
- exponent partition \(\lambda(n)\);
- repeat depth \(\eta(n)\);
- primitive-ray index;
- distance from a support diagonal;
- boundary depth in a face;
- local-neighborhood signature;
- factors appearing in directional transitions.

### Discipline

Many projections correspond to known additive-function, smooth-number, powerful-number, almost-prime, or sieve questions. The project must identify the exact classical object before treating a geometric name as new mathematics.

**Current class:** PVG-to-ANT translation front; no estimates installed by this agenda.

---

## 12. Domain J — topology, metrics, and embeddings

Several inequivalent geometries coexist:

1. unweighted exponent lattice distance;
2. weighted log distance using \(\log p\);
3. divisibility order;
4. graph distance on fixed levels;
5. Euclidean geometry of normalized exponents;
6. arithmetic distance on the integers;
7. residue or character pseudometrics.

### Questions

1. Which embeddings preserve adjacency?
2. Which preserve order?
3. Which preserve geodesics?
4. Which turn multiplication into translations?
5. Where does arithmetic size severely distort the simplex picture?
6. Is there a useful product or stratified topology joining all finite support faces?
7. What is the right completion, if any, for infinite valuation profiles or rational numbers?

**Current class:** foundational definitions and boundary analysis.

---

## 13. Domain K — extension beyond positive integers

Possible controlled extensions include:

- positive rationals: finitely supported integer valuation vectors;
- nonzero integers: sign bit plus positive valuation vector;
- ideals in Dedekind domains: prime-ideal valuation vectors;
- function fields: place valuations;
- algebraic numbers: several valuations with product-formula constraints.

Each extension changes the ambient lattice, admissible directions, and reconstruction rules. It must not be imported casually into the positive-integer model.

**Current class:** future comparative program.

---

## 14. Recommended first five passes

### PASS-001 — finite simplex atlas

Enumerate \(2\le s\le5\), \(1\le r\le12\). Verify point counts, boundary counts, degrees, distances, and spectra.

### PASS-002 — arithmetic observable atlas

Measure exact local changes of \(\tau,\sigma,\varphi,\mu,\omega,\Omega\) on all primitive edges in a controlled prime set.

### PASS-003 — additive transition atlas

Factor \(p_i\pm p_j\) and \(Q^h\pm1\) for preregistered axes and distances. Record support and level changes without making asymptotic claims.

### PASS-004 — inverse-identifiability benchmark

Create pairs of nonisomorphic points with matched partial signatures and determine what observations separate them.

### PASS-005 — factorization diagnostic benchmark

Compare any proposed neighbor/gcd strategy against classical baselines on preregistered integer families.

No later pass is authorized merely by this ordering. Each requires its own protocol and stopping rule.

---

## 15. Central working thesis

The useful object is not a static picture. It is a stratified arithmetic space with:

```text
points        = integers
coordinates   = prime valuations
faces         = finite prime supports
levels        = fixed total valuation height
rays          = powers of primitive generators
horizontal directions = ratios of prime axes
edges         = unit transfers of valuation mass
local operators = arithmetic transformations of neighboring points
projections   = classical arithmetic observables
```

The project will test whether this unified structure provides reusable proofs, diagnostics, algorithms, or tool-routing decisions that are materially clearer than the classical language alone.
