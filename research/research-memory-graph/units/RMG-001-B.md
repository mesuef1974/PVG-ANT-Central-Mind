# RMG-001-B — Seed Graph for ANT ↔ PVG Core Translation Families

Status: seed graph specification complete / executable graph not yet built
Classification: Diagnostic / Knowledge Architecture
Validation status: seed_nodes_defined_not_executed

## 1. Mission

Populate the first governed Research Memory Graph with actual analytic-number-theory objects and explicit Prime-Valuation Geometry translations.

This seed is deliberately foundational. It begins with objects that admit exact or nearly exact translation before moving to asymptotic tools where translation is more delicate.

## 2. Seed node families

### Family A — Integers and valuation vectors

Canonical ANT object:

```text
positive integer n
```

PVG translation:

\[
\nu(n)=(v_p(n))_{p\in\mathbb P}.
\]

Translation class:

```text
exact_embedding_and_bijection_onto_finitely_supported_nonnegative_vectors
```

Preserved information:

- complete prime factorization;
- divisibility;
- gcd and lcm;
- multiplication and division when defined.

Core identities:

\[
\nu(mn)=\nu(m)+\nu(n),
\]

\[
\nu(\gcd(m,n))=\min(\nu(m),\nu(n)),
\]

\[
\nu(\operatorname{lcm}(m,n))=\max(\nu(m),\nu(n)).
\]

Numerical example:

\[
12=2^2\cdot3,\qquad 18=2\cdot3^2.
\]

Hence

\[
\nu(12)=(2,1,0,\ldots),\qquad
\nu(18)=(1,2,0,\ldots).
\]

Then

\[
\nu(216)=\nu(12\cdot18)=(3,3,0,\ldots),
\]

\[
\nu(\gcd(12,18))=(1,1,0,\ldots)=\nu(6),
\]

\[
\nu(\operatorname{lcm}(12,18))=(2,2,0,\ldots)=\nu(36).
\]

Required checks:

```text
round_trip_integer_vector_check
multiplication_addition_check
gcd_coordinate_min_check
lcm_coordinate_max_check
```

### Family B — Arithmetic functions as PVG observables

Canonical ANT object:

\[
f:\mathbb N\to\mathbb C.
\]

PVG representation:

\[
F(v)=f\!\left(\prod_p p^{v_p}\right)
\]

for finitely supported valuation vectors `v`.

Translation class:

```text
exact_reindexing
```

Return map:

\[
f(n)=F(\nu(n)).
\]

This is exact because the valuation representation uniquely determines `n`.

Seed observables:

```text
1(n)
mu(n)
Lambda(n)
tau(n)
sigma_k(n)
phi(n)
prime_indicator(n)
```

PVG interpretations:

- `1(n)`: constant observable on the lattice;
- `mu(n)`: zero off the squarefree locus and sign by support size on the squarefree locus;
- `Lambda(n)`: supported on single-axis points and weighted by `log p`;
- `tau(n)`: divisor-box cardinality `product_p (v_p+1)`;
- `sigma_k(n)`: weighted sum over the divisor box;
- `phi(n)`: axis-local multiplicative observable;
- prime indicator: unit points on a single prime axis.

Numerical example for `n=12`, with `nu(12)=(2,1)`:

\[
\tau(12)=(2+1)(1+1)=6.
\]

The divisor box consists of

\[
(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),
\]

corresponding to

\[
1,2,4,3,6,12.
\]

For von Mangoldt:

\[
\Lambda(8)=\log 2,\qquad \nu(8)=(3,0,\ldots),
\]

while

\[
\Lambda(12)=0
\]

because `nu(12)` has support on two axes.

Required checks:

```text
observable_round_trip_check
tau_divisor_box_cardinality_check
mu_squarefree_locus_check
Lambda_single_axis_support_check
```

### Family C — Multiplicativity and geometric decomposition

Canonical ANT condition:

\[
f(mn)=f(m)f(n)\quad\text{when }\gcd(m,n)=1.
\]

PVG translation:

```text
F(u+v)=F(u)F(v) when supports of u and v are disjoint.
```

Complete multiplicativity becomes:

```text
F(u+v)=F(u)F(v) for all finitely supported nonnegative vectors u,v.
```

Translation class:

```text
exact_structural_equivalence
```

Numerical example using Euler phi:

\[
\varphi(12)=\varphi(4)\varphi(3)=2\cdot2=4
\]

because the valuation supports of `4` and `3` are disjoint.

But

\[
\varphi(4\cdot2)\ne\varphi(4)\varphi(2),
\]

which exposes the coprimality condition geometrically as support overlap.

Required checks:

```text
coprime_disjoint_support_equivalence
multiplicative_observable_check
support_overlap_boundary_case
```

### Family D — Dirichlet convolution as divisor-box aggregation

Canonical ANT definition:

\[
(f*g)(n)=\sum_{d\mid n}f(d)g(n/d).
\]

PVG translation for `v=nu(n)`:

\[
(F\star_{\mathrm{box}}G)(v)
=
\sum_{0\le u\le v}F(u)G(v-u).
\]

Translation class:

```text
exact_isomorphism_of_convolution_structures
```

The divisor relation `d|n` becomes the coordinatewise box condition `0<=nu(d)<=nu(n)`.

Numerical example for `n=12`, `v=(2,1)`:

\[
(1*1)(12)=\tau(12)=6.
\]

PVG calculation counts all six `u` in the divisor box.

Möbius inversion becomes inversion under box convolution:

\[
\mu*1=\varepsilon.
\]

Required checks:

```text
divisor_box_bijection_check
Dirichlet_convolution_box_convolution_check
Mobius_inverse_check
```

### Family E — Dirichlet series as transforms over valuation space

Canonical ANT object:

\[
D_f(s)=\sum_{n\ge1}\frac{f(n)}{n^s}.
\]

PVG translation:

\[
D_f(s)=
\sum_{v\in\mathbb N_0^{(\mathbb P)}}
F(v)\exp\!\left(-s\sum_p v_p\log p\right).
\]

Define the logarithmic height

\[
H_{\log}(v)=\sum_p v_p\log p.
\]

Then

\[
D_f(s)=\sum_v F(v)e^{-sH_{\log}(v)}.
\]

Translation class:

```text
exact_reindexing_of_the_series
```

The analytic content of convergence, continuation, poles, zeros, and growth is not supplied by the reindexing alone.

Numerical finite check for `f=1` and `n<=6`:

\[
\sum_{n=1}^{6}n^{-s}
\]

must equal the sum over the valuation vectors of

```text
1, 2, 3, 4, 5, 6
```

with weights `exp(-s H_log(v))`.

Required checks:

```text
finite_coefficient_reindexing_check
log_height_identity_check
convergence_claim_separation_check
```

### Family F — Euler products as independent axis aggregation

For multiplicative `f`, the standard Euler product is

\[
D_f(s)=\prod_p\left(\sum_{k\ge0}\frac{f(p^k)}{p^{ks}}\right)
\]

where justified.

PVG interpretation:

```text
each prime axis contributes a local generating factor;
the global object aggregates independent axis choices.
```

Translation class:

```text
exact_formal_factorization_under_multiplicativity;
analytic_equality_requires_convergence_certificate
```

For `f=1`:

\[
\zeta(s)=\prod_p(1-p^{-s})^{-1}
\]

in the half-plane of absolute convergence.

Numerical truncated check:

- choose primes up to `P`;
- expand local factors up to exponent bounds;
- compare coefficients with integers whose prime factors are at most `P` and whose exponents satisfy the bounds.

Required checks:

```text
truncated_Euler_product_coefficient_check
axis_local_factor_check
absolute_convergence_scope_check
```

### Family G — von Mangoldt and logarithmic axis support

Canonical definition:

\[
\Lambda(n)=
\begin{cases}
\log p,& n=p^k,\ k\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]

PVG object:

```text
single-axis support observable with axis label log p
```

More explicitly, for `v=nu(n)`:

\[
\Lambda_{\mathrm{PVG}}(v)=
\begin{cases}
\log p,& \operatorname{supp}(v)=\{p\},\\
0,&\text{otherwise}.
\end{cases}
\]

Translation class:

```text
exact_reindexing
```

Numerical examples:

```text
n=2, v=e_2, Lambda=log 2
n=8, v=3e_2, Lambda=log 2
n=9, v=2e_3, Lambda=log 3
n=12, v=2e_2+e_3, Lambda=0
```

The PVG image makes prime-power contamination explicit: all positive lattice points on one axis contribute, not only unit points.

Required checks:

```text
Lambda_prime_power_examples
single_axis_support_equivalence
prime_indicator_vs_Lambda_difference_check
```

## 3. Seed theorem and conjecture links

The graph must include typed edges connecting the seed objects to larger ANT structures:

```text
Lambda -> defines -> psi(x)
Lambda -> appears_in -> explicit_formula
Lambda -> weights -> Goldbach_representation_function
mu -> inverse_of -> constant_one_under_Dirichlet_convolution
multiplicativity -> enables -> Euler_product
Dirichlet_convolution -> translated_as -> divisor_box_convolution
zeta -> generated_by -> constant_one_Dirichlet_series
zeta -> linked_to -> prime_distribution
valuation_vector -> supports -> PVG_geometry
addition_fiber -> transports_to -> PVG_additive_geometry
```

These edges are structural links, not claims that PVG alone proves the connected theorems.

## 4. Required graph records

Each seed node must eventually be stored in machine-readable form with:

```text
node_id
node_type
canonical_definition
source_status
ANT_representation
PVG_representation
translation_type
inverse_status
preserved_information
lost_information
numeric_examples
check_ids
dependency_ids
certificate_ids
classification
```

Each edge must include:

```text
source_id
edge_type
target_id
conditions
strength
loss_profile
certificate_required
```

## 5. Acceptance state

```text
SEED_FAMILIES = 7
CANONICAL_DEFINITIONS = SPECIFIED
ANT_TO_PVG_TRANSLATIONS = SPECIFIED
PVG_TO_ANT_RETURN_ANALYSIS = SPECIFIED
NUMERICAL_EXAMPLES = INCLUDED
COMPUTATIONAL_CHECKS = SPECIFIED_NOT_RUN
MACHINE_READABLE_GRAPH = NOT_BUILT
REGRESSION_SUITE = NOT_BUILT
FULL_ANT_ASSIMILATION = NOT_CLAIMED
NEXT_ACTION = RMG-001-C
```

## 6. Next action

```text
RMG-001-C
Machine-readable node and edge registry plus executable numerical verification harness for the seed families
```
