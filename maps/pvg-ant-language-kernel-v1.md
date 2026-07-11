# PVG–ANT Language Kernel v1.0

**Purpose:** canonical reusable translation layer between Prime-Valuation Geometry and Analytic Number Theory.  
**Classification:** Exact identities + Reinterpretation + Diagnostic. Individual entries may later receive stronger certificates.

## 1. Core encoding

For

\[
n=\prod_p p^{v_p(n)},
\]

define

\[
\nu(n)=(v_p(n))_p
\]

with finite support and logarithmic weight

\[
\ell(\alpha)=\sum_p \alpha_p\log p.
\]

Then

\[
\ell(\nu(n))=\log n.
\]

The image of positive integers is the finitely supported lattice

\[
\mathbb N_0^{(\mathcal P)}.
\]

## 2. Canonical object dictionary

| ANT object | PVG object | Exact bridge | Information status |
|---|---|---|---|
| integer `n` | lattice point `ν(n)` | unique factorization | lossless |
| multiplication | vector addition | `ν(mn)=ν(m)+ν(n)` | lossless |
| divisibility | coordinate order | `d|n ⇔ ν(d)≤ν(n)` | lossless |
| prime `p` | unit vector `e_p` | `Ω(p)=1` | lossless |
| prime power | axis point `ke_p` | `p^k` | lossless |
| squarefree integer | Boolean lattice point | each coordinate in `{0,1}` | lossless |
| `Ω(n)` | `ℓ¹` height | `Ω(n)=Σ_p v_p(n)` | lossless |
| `ω(n)` | support cardinality | `ω(n)=|supp ν(n)|` | lossless |
| `log n` | weighted hyperplane coordinate | `Σ_p v_p(n)log p` | lossless |
| divisor set | integer box below `ν(n)` | `0≤β≤ν(n)` | lossless |
| `τ(n)` | box cardinality | `∏_p(v_p(n)+1)` | lossless |
| `n≤x` | logarithmic half-space | `ℓ(ν(n))≤log x` | lossless |
| short interval | thin logarithmic slab | `log x<ℓ(ν(n))≤log(x+h)` | order-sensitive |
| reduced residue class | arithmetic fiber | character orthogonality | bridge required |
| local Euler factor | one coordinate generating function | prime-power data | lossless locally |
| Euler product | coordinate product | multiplicativity | analytic convergence required |

## 3. Canonical operation dictionary

### 3.1 Dirichlet convolution

If `f(n)=F(ν(n))` and `g(n)=G(ν(n))`, then

\[
(f*g)(n)=\sum_{d\mid n}f(d)g(n/d)
=\sum_{\beta+\gamma=\nu(n)}F(\beta)G(\gamma).
\]

**PVG reading:** convolution is additive decomposition of a lattice point.

### 3.2 Multiplicative functions

A multiplicative function is determined by its coordinate-axis values on prime powers, with coprime products corresponding to disjoint-support vector addition.

### 3.3 Dirichlet series

For an observable `F` on the valuation lattice,

\[
\mathcal D_F(s)=\sum_{n\ge1}\frac{F(\nu(n))}{n^s}
=\sum_{\alpha\in\mathbb N_0^{(\mathcal P)}}F(\alpha)e^{-s\ell(\alpha)}.
\]

This is a weighted Laplace transform of the lattice observable. An Euler product exists only under the appropriate coordinate factorization.

### 3.4 Sieve

Divisibility by a prime `p` is the condition `v_p(n)≥1`. Sifting by primes below `z` removes unions of coordinate half-spaces. The geometric description does not itself cross parity or produce primes.

### 3.5 Characters and residue fibers

The congruence indicator for reduced residue classes is reconstructed through character Fourier coordinates. The residue fiber is not determined by `ν(n)` alone without retaining the prime labels and modular images.

## 4. Translation record required for every new bridge

Every bridge added to this kernel must contain:

```text
Bridge ID
Classical object
PVG object
Exact forward map
Exact reverse map or information loss
Preserved structure
Lost structure
Analytic transform
Required hypotheses
Simplification gain
Research use
Known literature
Honest classification
Certificate
```

## 5. Simplification-gain test

A translation is materially useful only if it produces at least one:

1. **Linearization:** a nonlinear arithmetic operation becomes additive or linear.
2. **Decomposition:** a global quantity splits into controlled coordinate pieces.
3. **Localization:** selected primes, supports, fibers, or faces can be isolated.
4. **Compression:** cases or hypotheses collapse into a single geometric statement.
5. **Transfer:** a geometric estimate yields an analytic estimate or conversely.
6. **Proof economy:** a proof becomes shorter, more general, or structurally clearer.
7. **New observable:** the geometry suggests a meaningful quantity not already native in the classical formulation.
8. **New question:** the translation reveals a precise research problem.

The recorded value is:

```text
none | expository | structural | analytic | proof-producing
```

## 6. Information-loss audit

PVG is naturally strong for multiplicative structure but does not automatically linearize addition. Every translation involving any of the following must state the extra bridge:

- `n+m`;
- short intervals and order on the number line;
- gaps between primes;
- exponential phases;
- zero sums and explicit formulas;
- spectral data.

A geometric rephrasing that discards ordering, phase, residue, or scale information may not be reversed without a named certificate.

## 7. Standard research flow through the kernel

```text
Classical question
→ identify factorization-dependent part
→ select exact PVG observables
→ decompose lattice geometry
→ derive analytic transform
→ formulate transfer lemma
→ prove or test
→ translate conclusion back to ANT
→ audit originality and PVG necessity
```

## 8. Initial reusable bridge targets

The first certified kernel release should stabilize at least these eight families:

1. multiplication/divisibility/order;
2. divisor boxes and convolution;
3. multiplicative observables and Euler factors;
4. logarithmic half-spaces and weighted lattice sums;
5. squarefree support geometry and Möbius;
6. residue fibers and character transforms;
7. sieve as coordinate exclusion with remainder certificates;
8. local/global transfer through Dirichlet series and contour/Tauberian tools.

## 9. Maturity state

The current kernel is strongest at `L1 Exact translation` and partially at `L2 Structural simplification`. A bridge reaches `L3 Transfer principle` only when it has a proved lemma with hypotheses and an analytic consequence.

## 10. Ceiling

- a dictionary entry is not a theorem;
- an exact identity may be known mathematics;
- a cleaner picture is not an originality claim;
- an Euler-product analogy is invalid without convergence and factorization checks;
- additive and spectral information are not recovered for free;
- no RH/GRH progress is implied.