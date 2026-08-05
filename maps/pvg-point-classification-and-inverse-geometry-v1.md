# PVG Point Classification and Inverse Geometry v1

**Program:** `PVG-INVERSE-GEOMETRY-001`  
**Status:** foundational exact grammar and executable prototype  
**Priority:** deepen native understanding of Prime Valuation Geometry before opening further theorem targets  
**Scientific class:** exact identities / exact encoding / governed research program; no originality or theorem-strength claim

---

## 1. Ambient space and forward encoding

For every positive integer

\[
n=\prod_{p\in\mathbb P}p^{v_p(n)},
\]

define the finitely supported labeled valuation vector

\[
\nu(n)=(v_p(n))_{p\in\mathbb P}\in\mathbb N_0^{(\mathbb P)}.
\]

The prime labels are part of the geometry. The map is exact:

\[
\nu(mn)=\nu(m)+\nu(n),
\qquad
m\mid n\iff \nu(m)\leq \nu(n)
\]

coordinatewise.

The point \(1\) is the origin. Each prime \(p\) is the first nonzero lattice point
\(e_p\) on the prime axis \(p\).

---

## 2. First classifier: the minimal prime-support face

Define

\[
\operatorname{supp}(n)=\{p:v_p(n)>0\},
\qquad
\omega(n)=|\operatorname{supp}(n)|.
\]

The minimal labeled face containing \(\nu(n)\) is

\[
C_{\operatorname{supp}(n)}
=
\left\{
\sum_{p\mid n}x_pe_p:x_p\geq 0
\right\}.
\]

Because every active exponent is positive, \(\nu(n)\) lies in the relative interior of this
minimal face.

| \(\omega(n)\) | geometric class | arithmetic form |
|---:|---|---|
| 0 | origin | \(n=1\) |
| 1 | point on one prime axis | \(n=p^a\) |
| 2 | relative interior of a two-prime face | \(n=p^a q^b\) |
| 3 | relative interior of a three-prime face | \(n=p^a q^b r^c\) |
| \(s\) | relative interior of an \(s\)-prime face | \(n=\prod_{i=1}^s p_i^{a_i}\) |

The full cone face has dimension \(s=\omega(n)\). Its horizontal section at fixed total
height has dimension \(s-1\).

---

## 3. Second classifier: horizontal valuation level

Define the total valuation height

\[
\Omega(n)=\sum_p v_p(n).
\]

The global horizontal level is

\[
\Sigma_m=\{n:\Omega(n)=m\}.
\]

Inside a fixed \(s\)-prime face, the section

\[
x_1+\cdots+x_s=m,\qquad x_i\geq 0
\]

is an \((s-1)\)-simplex lattice.

Examples:

- one axis: one point at each level;
- two axes: a line segment of lattice points;
- three axes: a triangular lattice;
- four axes: a tetrahedral lattice;
- \(s\) axes: an \((s-1)\)-simplex.

The number of closed-face points is

\[
\binom{m+s-1}{s-1},
\]

while the number of relative-interior points using all \(s\) axes is

\[
\binom{m-1}{s-1}.
\]

These are exact stars-and-bars counts. Their Pascal recurrences count face sections; they
do not by themselves constitute a new theorem.

The normalized exponents

\[
\beta_p(n)=\frac{v_p(n)}{\Omega(n)}
\]

are barycentric coordinates of the point in its horizontal simplex.

---

## 4. Third classifier: squarefree floor and repeat depth

Define

\[
\operatorname{rad}(n)=\prod_{p\mid n}p
\]

and

\[
\eta(n)=\Omega(n)-\omega(n)
       =\sum_{p\mid n}(v_p(n)-1).
\]

Then

\[
\nu(n)
=
\nu(\operatorname{rad}(n))
+
\sum_{p\mid n}(v_p(n)-1)e_p.
\]

Interpretation:

- \(\operatorname{rad}(n)\) identifies the labeled face and its squarefree floor point;
- \(\eta(n)\) measures the total repeated-prime depth above that floor;
- \(\eta(n)=0\) exactly for squarefree points.

---

## 5. Fourth classifier: unlabeled exponent shape

Sort the positive exponents in decreasing order:

\[
\lambda(n)=\operatorname{sort}\{v_p(n):p\mid n\}.
\]

Then \(\lambda(n)\) is a partition of \(\Omega(n)\). It keeps the abstract geometric shape
while erasing the prime labels.

At level \(\Omega=4\), the possible shapes are

\[
(4),\ (3,1),\ (2,2),\ (2,1,1),\ (1,1,1,1).
\]

Multiplication by a prime either increases one part by \(1\), or appends a new part \(1\).
After forgetting labels, inter-level growth follows the Young-lattice incidence pattern.

This shape layer is noninjective: it does not recover the integer or its residue behavior.

---

## 6. Fifth classifier: primitive ray and radial index

Let the positive exponents be \(a_1,\ldots,a_s\), and define

\[
d(n)=\gcd(a_1,\ldots,a_s).
\]

Set

\[
u(n)=\prod_{i=1}^s p_i^{a_i/d(n)}.
\]

Then

\[
\boxed{n=u(n)^{d(n)}}
\]

and the exponent vector of \(u(n)\) is primitive: its coordinates have gcd \(1\).

Thus every point \(n>1\) has a unique:

- primitive ray generator \(u(n)\);
- radial index \(d(n)\);
- primitive direction \(\nu(u(n))\).

Examples:

\[
36=6^2,\qquad
900=30^2,\qquad
1728=12^3.
\]

If all active exponents are equal, the point lies on the balanced support diagonal generated
by \(\operatorname{rad}(n)\).

---

## 7. Directional geometry: lines are geometric sequences

Let \(x\) be a valuation vector and let \(h\in\mathbb Z^{(\mathbb P)}\) have finite support.
Whenever \(x+kh\) remains in the nonnegative lattice,

\[
\Phi(x+kh)
=
\Phi(x)\,Q(h)^k,
\qquad
Q(h)=\prod_p p^{h_p}.
\]

Therefore:

\[
\boxed{\text{lattice lines in valuation space correspond to geometric sequences}.}
\]

Three direction types are distinguished by

\[
H(h)=\sum_p h_p.
\]

- \(H(h)>0\): ascending direction through higher \(\Omega\)-levels;
- \(H(h)=0\): horizontal direction inside one \(\Omega\)-level;
- \(H(h)<0\): descending direction, finite until a coordinate reaches zero.

In the \(2,3\) face:

- \(h=(1,0)\) gives ratio \(2\);
- \(h=(0,1)\) gives ratio \(3\);
- \(h=(1,1)\) gives ratio \(6\);
- \(h=(-1,1)\) gives horizontal ratio \(3/2\).

For example,

\[
6,36,216,\ldots
\]

is the line through \(\nu(6)\) in direction \((1,1)\).

---

## 8. Local linear interactions preserve direction

Let a directional line be

\[
a_k=a_0Q^k.
\]

For a finite linear translation-invariant operator

\[
(Ta)_k=\sum_{j=0}^m c_j a_{k+j},
\]

define

\[
P(t)=\sum_{j=0}^m c_jt^j.
\]

Then

\[
\boxed{(Ta)_k=a_0P(Q)Q^k.}
\]

Hence every nonzero output remains a geometric sequence with the same directional ratio
\(Q\), but its base point is multiplied by \(P(Q)\).

Special cases:

\[
a_k+a_{k+h}=a_k(1+Q^h),
\]

\[
a_{k+h}-a_k=a_k(Q^h-1),
\]

\[
S^r a_k=a_k(1+Q)^r,
\qquad
\Delta^r a_k=a_k(Q-1)^r.
\]

The new prime factors of \(P(Q)\) determine which additional prime axes enter the translated
line. Direction preservation and support preservation are different statements.

---

## 9. The \(2,3\) face as the first case study

At horizontal level \(r\), the face section is

\[
A_{r,k}=2^{r-k}3^k,\qquad 0\leq k\leq r.
\]

It is a finite geometric sequence of ratio \(3/2\).

Adjacent points have the form

\[
A_{r,k}=2g,\qquad A_{r,k+1}=3g.
\]

Therefore:

\[
A_{r,k}+A_{r,k+1}=5g,
\]

\[
A_{r,k+1}-A_{r,k}=g,
\]

\[
\gcd(A_{r,k},A_{r,k+1})=g,
\]

\[
\operatorname{lcm}(A_{r,k},A_{r,k+1})=6g.
\]

Thus every adjacent cell has the normalized signature

\[
1:2:3:5:6
\]

for

\[
\gcd:x:y:x+y:\operatorname{lcm}.
\]

Repeated adjacent sums generate

\[
2^a3^b5^c,\qquad a+b+c=r,
\]

while repeated differences recover lower \(2,3\)-face levels. For points separated by
\(h\) steps,

\[
x=2^hg,\qquad y=3^hg,
\]

so

\[
x+y=(2^h+3^h)g,
\qquad
y-x=(3^h-2^h)g.
\]

This identifies a larger research family governed by the factorizations of \(Q^h\pm1\).

---

## 10. Divisibility geometry of a point

For

\[
n=\prod_{i=1}^s p_i^{a_i},
\]

the divisor set is the labeled lattice box

\[
B(n)=\prod_{i=1}^s\{0,1,\ldots,a_i\}.
\]

Its cardinality is

\[
\tau(n)=\prod_{i=1}^s(a_i+1).
\]

The multiples of \(n\) form the translated positive cone

\[
\nu(n)+\mathbb N_0^{(\mathbb P)}.
\]

Thus every point is simultaneously:

- the upper corner of a finite divisor box;
- the anchor of an infinite multiple cone;
- a point on one primitive ray;
- a point in one minimal labeled face;
- a point in one horizontal \(\Omega\)-level.

---

## 11. Canonical geometric passport

For an exactly factored integer, define

\[
\mathscr P(n)=
\bigl(
\nu(n),
\operatorname{supp}(n),
\omega(n),
\Omega(n),
\operatorname{rad}(n),
\eta(n),
\lambda(n),
u(n),
d(n),
B(n)
\bigr).
\]

The passport answers:

1. **Where does the point live?** — labeled support face.
2. **At what height?** — \(\Omega(n)\).
3. **How deep above the squarefree floor?** — \(\eta(n)\).
4. **What is its unlabeled shape?** — \(\lambda(n)\).
5. **On which primitive ray?** — \(u(n)\).
6. **How far along that ray?** — \(d(n)\).
7. **What lies below and above it in divisibility order?** — divisor box and multiple cone.

No single scalar among \(\omega,\Omega,\tau,\log n\) replaces this labeled passport as a
geometric object.

---

## 12. Inverse geometry: from an integer to its exact location

Given only the decimal integer \(n\), exact inverse geometry requires the complete prime
factorization

\[
n=\prod p_i^{a_i}.
\]

Then the location is immediate:

\[
n
\longmapsto
\{(p_i,a_i)\}
\longmapsto
\nu(n)
\longmapsto
\mathscr P(n).
\]

Conversely, the full labeled valuation vector gives the prime factorization and reconstructs
\(n\).

Therefore, in a direct computational sense:

\[
\boxed{\text{exact PVG inverse location and complete integer factorization are equivalent data}.}
\]

This is not a claim that factorization becomes easy. It is the correct identification of the
inverse problem.

### Exact protocol

1. Validate \(n\geq1\).
2. Obtain a complete certified prime factorization.
3. Verify primality certificates and reconstruct the product.
4. Build the labeled valuation vector.
5. Extract support and \(\omega\).
6. Compute \(\Omega\), radical, repeat depth, and shape partition.
7. Compute primitive ray generator and radial index.
8. Construct horizontal barycentric coordinates.
9. Construct divisor-box and multiple-cone descriptors.
10. Emit the canonical passport with a factorization confidence status.

---

## 13. Partial factorization and geometric uncertainty

Suppose only

\[
n=AC
\]

is certified, where \(A\) is completely factored and \(C\) is an unresolved cofactor coprime
to \(A\). Then

\[
\nu(n)=\nu(A)+\nu(C).
\]

The known vector \(\nu(A)\) is an exact anchor, but the following may remain unknown:

- the residual prime labels;
- residual support dimension \(\omega(C)\);
- residual height \(\Omega(C)\);
- final exponent partition;
- final primitive ray;
- exact minimal face.

The correct output is not a guessed point. It is an **epistemic uncertainty fiber** anchored
at \(\nu(A)\), together with the unresolved cofactor \(C\) and all available certificates.

### Confidence levels

- `IG-0 EXACT-AUTOMATIC`: complete certified factorization produced by the tool.
- `IG-1 EXACT-SUPPLIED`: complete externally supplied factorization verified by product and
  primality certificates.
- `IG-2 PARTIAL-ANCHORED`: certified known coordinates plus unresolved cofactor.
- `IG-3 SUMMARY-ONLY`: only support, shape, or scalar summaries are known.
- `IG-4 PROJECTED`: only a low-dimensional visualization or aggregate is available.

Only `IG-0` and `IG-1` authorize an exact point passport.

---

## 14. Executable prototype

The repository tool

```text
tools/pvg_inverse_geometry.py
```

implements:

- certified automatic factorization for \(1\leq n<2^{64}\);
- deterministic Miller–Rabin primality in that domain;
- Pollard–Rho splitting;
- exact passport construction;
- complete supplied factorizations for larger \(n\), provided every listed prime is below
  \(2^{64}\) and is certified by the deterministic test;
- deliberate refusal to invent an exact location when the factorization is incomplete.

Examples:

```bash
python tools/pvg_inverse_geometry.py 900
python tools/pvg_inverse_geometry.py 36 --compact
python tools/pvg_inverse_geometry.py \
  14697715679690864505827555550150426126974976 \
  --factors "2^80,3^40"
```

The automatic domain is an implementation boundary, not a mathematical boundary.

---

## 15. Research program opened by the classification

The first systematic research sequence is:

### One-axis study

- prime rays and prime-power germs;
- radial operators;
- local Bell-series interface.

### Two-axis face study

- every direction and its geometric ratio;
- horizontal sections;
- adjacent and fixed-gap interactions;
- factors of \(Q^h\pm1\);
- support-preserving versus support-expanding operators;
- the complete \(2,3\) case before general \(p,q\).

### Three-axis study

- triangular horizontal lattices;
- directional planes and lines;
- pair and triple interaction operators;
- simplex recurrences and transition faces.

### Four and more axes

- tetrahedral and higher-simplex sections;
- support-incidence combinatorics;
- low-dimensional projections versus exact labeled geometry;
- scalable inverse passports and uncertainty fibers.

### Open research questions

1. Which local operators preserve a given support face?
2. Which operators preserve only the directional ratio?
3. How do prime factors of \(P(Q)\) control face transitions?
4. Which \(Q\) satisfy that \(Q\pm1\) remains smooth on the same support?
5. What periodic divisibility laws appear in \(Q^h\pm1\)?
6. Which observed patterns are standard recurrence theory, and which PVG organization is
   materially useful?
7. Can the classification improve tool routing in analytic number theory without overstating
theorem content?

---

## 16. Governance and scientific ceiling

The following are exact:

- unique valuation encoding;
- support-face classification;
- \(\omega,\Omega,\operatorname{rad},\eta,\lambda\);
- primitive-ray decomposition;
- divisor-box and multiple-cone descriptions;
- lattice-line/geometric-sequence identity;
- finite linear-operator identity \(T(a)_k=P(Q)a_k\);
- the stated \(2,3\)-face identities.

The following remain research-program claims, not established novelty:

- that this organization is new;
- that it yields new asymptotic estimates;
- that it materially improves a theorem proof;
- that the factorization bottleneck has been weakened;
- that low-dimensional visualization preserves exact PVG geometry.

No Goldbach proof, RH/GRH progress, publication readiness, or originality certification is
claimed.
