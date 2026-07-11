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

## 11. Reconciled legacy bridges

The following bridges were recovered through `Legacy Research Assets Reconciliation 001`. They are canonical language entries, not newly discovered mathematics.

### 11.1 Sieve level ↔ truncated valuation information

**Bridge ID:** `BRIDGE-SIEVE-TRUNCATED-VALUATION-001`

For `d≤D`, let

\[
I_d(n)=\mathbf 1_{d\mid n}.
\]

The family of pointwise divisibility indicators is equivalent to the truncated valuation vector

\[
\nu^{(D)}(n)=
\left(
\min\left(v_p(n),\left\lfloor\frac{\log D}{\log p}\right\rfloor\right)
\right)_{p\le D}.
\]

Thus the pointwise sigma-algebra generated by `I_d`, `d≤D`, is the one generated by `ν^(D)`.

- **Preserved:** divisibility by every integer up to `D`, including visible prime-power depths.
- **Lost:** deeper exponents, primes above `D`, ordering, additive phase, and any later information discarded by aggregation.
- **Simplification gain:** structural.
- **Classification:** exact known identity / reinterpretation.
- **Source asset:** `EXT-ASSET-PVG-SIEVE-001`.

### 11.2 Pointwise valuation data ↔ aggregated sieve data

**Bridge ID:** `BRIDGE-SIEVE-AGGREGATION-LOSS-001`

The pointwise map

\[
n\mapsto \nu^{(D)}(n)
\]

is not equivalent to the aggregated family data

\[
A_d=\sum_{d\mid n}a_n,
\qquad d\le D.
\]

Aggregation may preserve expected local densities while losing sign, phase, ordering, correlations, and target-purity information.

- **Preserved:** selected divisibility moments and remainder certificates.
- **Lost:** individual factorization profiles and information not encoded by the chosen aggregate statistics.
- **Research use:** formulate quantitative information-deficiency questions before invoking a parity or distribution wall.
- **Simplification gain:** structural / analytic diagnostic.
- **Classification:** information-loss diagnostic, not a theorem about the parity barrier.
- **Source asset:** `EXT-ASSET-PVG-SIEVE-001`.

### 11.3 Principal-character removal in residue fibers

**Bridge ID:** `BRIDGE-RESIDUE-PRINCIPAL-REMOVAL-001`

Define the principal-subtracted normalized residue-fiber error by

\[
\mathcal E^\circ(T;q,a)
=
 e^{-T/2}
\left(
\psi(e^T;q,a)
-
\frac{\psi_q(e^T)}{\varphi(q)}
\right).
\]

Then character decomposition contains only non-principal characters:

\[
\mathcal E^\circ(T;q,a)
=
\frac{e^{-T/2}}{\varphi(q)}
\sum_{\chi\ne\chi_0}
\overline{\chi(a)}\,\psi(e^T,\chi),
\]

subject to the exact convention used for `ψ(x,χ)` and reduced residue classes.

- **Preserved:** genuinely family-specific character fluctuation.
- **Removed:** the common principal-character / zeta-axis component.
- **Simplification gain:** analytic normalization.
- **Classification:** exact character-orthogonality bridge.
- **Source asset:** `EXT-ASSET-OPEN-PROBLEMS-001`.

### 11.4 Residue-fiber variance ↔ non-principal character second moment

**Bridge ID:** `BRIDGE-RESIDUE-VARIANCE-PARSEVAL-001`

For

\[
V^\circ(T;q)
=
\frac1{\varphi(q)}
\sum_{(a,q)=1}
|\mathcal E^\circ(T;q,a)|^2,
\]

character orthogonality yields a Parseval identity relating `V°` to a second moment over `χ≠χ₀`. The exact factor of `φ(q)` must be recorded with the normalization convention.

- **Preserved:** full `L²` energy across reduced residue fibers.
- **Lost:** individual character phase after taking the second moment.
- **Analytic transform:** finite Fourier transform on the reduced residue group.
- **Simplification gain:** analytic decomposition.
- **Classification:** exact Parseval bridge; no GRH consequence by itself.
- **Source asset:** `EXT-ASSET-OPEN-PROBLEMS-001`.

### 11.5 Structural layer separation

**Bridge ID:** `BRIDGE-PVG-LAYER-SEPARATION-001`

```text
support geometry
≠ convolution geometry
≠ residue geometry
≠ spectral geometry
```

- support geometry records active coordinates and their depths;
- convolution geometry records additive decompositions of valuation vectors;
- residue geometry requires modular labels and character Fourier coordinates;
- spectral geometry requires explicit zero/eigenvalue data and positivity or operator certificates.

No transition between these layers is licensed without a named bridge and information-loss audit.

- **Simplification gain:** routing and error prevention.
- **Classification:** diagnostic governance principle.
- **Source assets:** `EXT-ASSET-PVG-SIEVE-001`, `EXT-ASSET-ZETA-LITERATURE-001`.

### 11.6 Edge-error separation

**Bridge ID:** `BRIDGE-EDGE-ERROR-SEPARATION-001`

For a compactly supported smoothing kernel `Φ_h` and a prime-ray remainder `R₁`, let

\[
S_h=R_1*\Phi_h,
\qquad
E_h(T)=S_h(T)-R_1(T).
\]

Under the elementary regularity and support assumptions recorded by the source note, one obtains an edge estimate of the form

\[
|E_h(T)|\ll_\Phi T e^T h+T.
\]

The role of the bridge is to separate an elementary desmoothing contribution from the genuinely difficult estimate on the smoothed central term.

- **Preserved:** scale and smoothing dependence.
- **Lost:** none at the identity level; the estimate depends on the source hypotheses.
- **Research use:** locate the true missing certificate rather than blaming the boundary term.
- **Simplification gain:** analytic barrier localization.
- **Classification:** known elementary estimate / diagnostic; not RH progress.
- **Source asset:** `EXT-ASSET-PVG-SIEVE-001`.

## 12. Legacy bridge activation rule

A legacy bridge is used only through:

```text
named task
→ Research Readiness Card
→ smallest sufficient external asset
→ exact bridge and source activation
→ proof/test/certificate
→ knowledge return
```

The routing table is `maps/legacy-assets-routing.md`. The source registry is `registries/external-research-assets.jsonl`. Negative closures are stored in `registries/negative-results.jsonl`.