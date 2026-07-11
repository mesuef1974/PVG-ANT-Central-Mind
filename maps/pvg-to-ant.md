# PVG ↔ ANT Translation Map

**Canonical kernel:** `maps/pvg-ant-language-kernel-v1.md`  
**Purpose:** quick routing map; the kernel is the authoritative bridge specification.  
**Classification:** Exact identities / Reinterpretation / Diagnostic unless a stronger certificate is named.

## Quick dictionary

| PVG | ANT | Core bridge | Default ceiling |
|---|---|---|---|
| lattice point `ν(n)` | integer factorization | unique factorization | Identity |
| vector addition | multiplication | `ν(mn)=ν(m)+ν(n)` | Identity |
| coordinate order | divisibility | `d|n ⇔ ν(d)≤ν(n)` | Identity |
| support | `ω(n)` / squarefree structure | active prime coordinates | Identity |
| `ℓ¹` height | `Ω(n)` | sum of valuations | Identity |
| weighted coordinate | `log n` | `Σv_p(n)log p` | Identity |
| divisor box | divisors / `τ_k` | lattice box below `ν(n)` | Identity / Structural |
| additive point decomposition | Dirichlet convolution | `β+γ=ν(n)` | Identity / Structural |
| coordinate local factor | Euler factor | prime-power generating data | Structural, convergence required |
| logarithmic half-space | `n≤x` sums | `Σv_p log p≤log x` | Reinterpretation / Analytic bridge |
| thin logarithmic slab | short interval | order-sensitive bridge | Boundary |
| coordinate exclusion | sieve | divisibility faces + remainder certificate | Structural / Diagnostic |
| residue fiber | characters / progressions | Fourier reconstruction | Analytic bridge |
| phase observable | `μ, λ, χ, n^{it}` | Halász/pretentious test required | Diagnostic |

## Required route for any new translation

```text
Classical object
→ exact PVG encoding
→ reverse map or information loss
→ geometric decomposition
→ analytic transform
→ transfer lemma
→ certificate
→ ANT restatement
→ originality and PVG-necessity test
```

## Do not rebuild bridges

A bridge already certified in `pvg-ant-language-kernel-v1.md` is reused. A new version is allowed only when:

- a defect is found;
- a stronger reverse map is proved;
- information loss is reduced;
- a new transfer lemma raises the maturity level.

## Translation limits

PVG naturally linearizes multiplicative structure. It does not recover for free:

- addition `n+m`;
- order and gaps;
- exponential phase;
- zero/spectral data;
- uniform short-interval estimates;
- prime production from sieve formulation.

Each such bridge must name the added analytic certificate.

## Simplification-gain label

Every bridge records one:

```text
none | expository | structural | analytic | proof-producing
```

Only `structural`, `analytic`, or `proof-producing` gains can support a research mechanism, and none imply originality without literature review.

## Operating references

- `governance/pvg-ant-research-compass-v1.md`
- `governance/task-triggered-knowledge-activation-policy.md`
- `governance/templates/research-readiness-card.md`
- `registries/program-goals.jsonl`

**Ceiling:** translation is not proof; reinterpretation is not a new theorem; no RH/GRH progress.