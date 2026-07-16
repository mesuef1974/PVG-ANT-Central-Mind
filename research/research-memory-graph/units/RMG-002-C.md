# RMG-002-C — Dirichlet Series / Euler Product Dependency Graph and Convergence-Certificate Discipline

Status: completed / finite verification PASS 12/12

Classification: Knowledge Architecture / Analytic Certificate Discipline / Computational Diagnostic

Branch: `agent/pvg-axis-sum-continuation-002`

## 1. Mission

Separate four layers that must not be collapsed:

```text
arithmetic coefficients
→ formal Dirichlet series
→ formal Euler factors
→ analytic Euler product in a certified domain
```

The unit records exactly which certificate is needed at each transition.

## 2. Delivered artifacts

```text
research/research-memory-graph/registry/dirichlet-series-euler-product-dependencies.jsonl
research/research-memory-graph/code/verify_rmg_002_c.py
research/research-memory-graph/results/rmg_002_c_verification.json
research/research-memory-graph/units/RMG-002-C.md
```

## 3. Governing dependency chain

For an arithmetic function `a`:

\[
D_a(s)=\sum_{n\ge1}a(n)n^{-s}
\]

is first a formal or domain-limited analytic object.

If `a` is multiplicative, prime-power coefficients determine formal local factors:

\[
\sum_{k\ge0}a(p^k)p^{-ks}.
\]

The passage to

\[
D_a(s)=\prod_p\left(\sum_{k\ge0}a(p^k)p^{-ks}\right)
\]

as an analytic equality requires a declared convergence certificate. Multiplicativity alone does not supply global convergence.

## 4. PVG translation

For `v=nu(n)` and `A(v)=a(n)`:

\[
D_a(s)=\sum_v A(v)e^{-sH_{\log}(v)},
\qquad
H_{\log}(v)=\sum_p v_p\log p.
\]

Translation class:

```text
EXACT_IDENTITY_REWRITE
```

Preserved:

- all coefficients;
- prime-factor coordinates;
- logarithmic heights;
- finite truncations.

Not supplied:

- convergence;
- analytic continuation;
- poles;
- zero locations;
- growth estimates;
- zero-free regions.

## 5. Certificate registry

### Absolute convergence certificate

A sufficient form is:

\[
\sum_n |a(n)|n^{-\sigma}<\infty.
\]

Within the certified domain it permits regrouping and prime-factor aggregation. It does not permit continuation beyond that domain.

### Local-factor certificate

Multiplicativity plus declared prime-power coefficients determines the formal local factors. It does not certify the infinite product.

## 6. Positive examples

For zeta:

\[
\zeta(s)=\sum_{n\ge1}n^{-s}=\prod_p(1-p^{-s})^{-1},
\qquad \Re(s)>1.
\]

For Möbius:

\[
\sum_{n\ge1}\frac{\mu(n)}{n^s}=\prod_p(1-p^{-s}),
\qquad \Re(s)>1.
\]

The half-plane is part of the statement, not optional metadata.

## 7. Anti-collapse rules

Rejected:

```text
finite truncated product
⇒ infinite analytic Euler product
```

Reason: finite coefficient agreement contains no tail estimate.

Rejected:

```text
PVG log-height reindexing
⇒ analytic continuation
```

Reason: reindexing changes coordinates, not analytic control.

Rejected:

```text
formal Euler factors
⇒ zero-free region or RH information
```

Reason: zero control requires separate analytic certificates.

## 8. Verification

The standard-library-only harness returned:

```text
PASS 12/12
```

Selected evidence:

- 625 coefficients in a bounded zeta local-factor expansion, all equal to one;
- 16 squarefree coefficients from truncated Möbius factors matching `mu(n)`;
- at `s=2`, finite series/product discrepancy approximately `4.59e-05`;
- at `s=1.5`, discrepancy approximately `1.67e-03`;
- harmonic growth from `H_1000≈7.48547` to `H_10000≈9.78761`, diagnosing failure at `s=1`;
- finite PVG log-height reindexing matched exactly to displayed precision.

These computations illustrate certificate boundaries; they do not prove infinite convergence theorems by themselves.

## 9. Assimilation decision

```text
DIRICHLET_SERIES_DEPENDENCY_GRAPH = L5_COMPUTATIONALLY_REGRESSION_TESTED
EULER_PRODUCT_CERTIFICATE_DISCIPLINE = L5_COMPUTATIONALLY_REGRESSION_TESTED
ANALYTIC_CONTINUATION = NOT ADDED
ZERO_FREE_REGION = NOT ADDED
LEAN_FORMALIZATION = NOT ADDED
L6_PROMOTION = NOT AUTHORIZED
```

## 10. Scientific ceiling

```text
KNOWN IDENTITIES + FINITE NUMERICAL DIAGNOSTICS
NOT A NEW CONVERGENCE THEOREM
NOT ANALYTIC CONTINUATION
NOT A ZERO-FREE REGION
NO RH OR GRH PROGRESS
```

## 11. Acceptance decision

```text
DEPENDENCY_REGISTRY = PASS
CONVERGENCE_CERTIFICATE_GATE = PASS
PVG_LOSS_PROFILE = PASS
POSITIVE_EXAMPLES = PASS
ANTI_COLLAPSE_CASES = PASS
NUMERICAL_HARNESS = PASS 12/12
RMG-002-C = COMPLETED
```

## 12. Next governed step

```text
RMG-002-D — von Mangoldt / Logarithmic Derivative / Chebyshev Observable Graph
```

It should connect `Lambda`, `-zeta'/zeta`, `theta`, `psi`, prime powers, explicit-formula dependencies, and the exact boundary between finite PVG observables and zero-sensitive analytic statements.
