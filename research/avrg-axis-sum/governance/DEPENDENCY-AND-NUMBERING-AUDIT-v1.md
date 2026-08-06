# Dependency and Numbering Audit — Theory Freeze v1.0

Status: complete first-pass structural audit.

Purpose: record the logical dependency graph, verify numbering continuity, and identify any theorem whose statement relies on an undefined or unproved object.

## 1. Numbering audit

The canonical core uses continuous section-local numbering:

- Section 1: Definitions 1.1–1.2, Proposition 1.3.
- Section 2: Definitions 2.1–2.2, Theorem 2.3, Definition 2.4, Proposition 2.5.
- Section 3: Definitions 3.1–3.3, Theorem 3.4.
- Section 4: Definitions 4.1–4.2, Proposition 4.3, Exact Reformulation 4.4.
- Section 5: Definitions 5.1–5.3, Theorem 5.4, Corollaries 5.5–5.6, Propositions 5.7–5.8.
- Section 6: Definition 6.1, Theorem 6.2, Corollary 6.3, Proposition 6.4, Definition 6.5.
- Section 7: Definition 7.1, Proposition 7.2.
- Section 8: Open Problems 8.1–8.4, Deferred Observation 8.5.

Result: **PASS**. No duplicate labels, gaps requiring repair, or cross-section collisions remain.

## 2. Core dependency graph

```text
Definition 1.1  prime-valuation vector
        |
        v
Definition 1.2  recovery map
        |
        v
Proposition 1.3 exact recovery / injectivity
        |
        +------------------------------+
        |                              |
        v                              v
Definition 2.2 valuation fiber     Definition 3.2 valuation lift
        |                              |
        v                              v
Theorem 2.3 no loss               Theorem 3.4 convolution identity
        |
        v
Proposition 2.5 reflection
```

The channel layer is logically separate from the arithmetic-function layer once the fiber index set is fixed:

```text
Definition 5.1 weight space
        |
Definition 5.2 difference coordinate
        |
Definition 5.3 channel operator
        |
        v
Theorem 5.4 rank formula
   |       |        |
   v       v        v
Cor. 5.5  Cor. 5.6  Prop. 5.7
kernel    injective zero mode
        |
        v
Prop. 5.8 Fourier equivalence
```

The multi-modulus layer depends only on the single-modulus equivalence relation:

```text
Definition 6.1 joint operator
        |
Theorem 5.4 single-modulus rank
        |
        v
Theorem 6.2 joint rank
   |              |
   v              v
Corollary 6.3   Proposition 6.4
injectivity     conditioning
```

The phase correction is independent of the rank theorems:

```text
Definition 7.1 difference phase
        |
        v
Proposition 7.2 constancy criterion
```

## 3. Element-by-element dependency ledger

| Element | Direct dependencies | Used by | Status |
|---|---|---|---|
| Definition 1.1 | none | 1.2, 2.2, 4.1, 4.2 | PASS |
| Definition 1.2 | 1.1 | 1.3, 2.2, 3.2 | PASS |
| Proposition 1.3 | 1.1, 1.2, fundamental theorem of arithmetic | 2.3, 3.4 | PASS |
| Definition 2.1 | none beyond positive integers | 2.2, 2.3, 2.5 | PASS |
| Definition 2.2 | 1.1, 1.2, 2.1 | 2.3, 2.5, 3.1, 4.4 | PASS |
| Theorem 2.3 | 1.3, 2.2 | exact interpretation of all examples | PASS |
| Definition 2.4 | ordered pair structure | 2.5 | PASS |
| Proposition 2.5 | 2.1–2.4 | examples | PASS |
| Definition 3.1 | 2.2 | 3.4 | PASS |
| Definition 3.2 | 1.2 | 3.4, 4.3 | PASS |
| Definition 3.3 | arithmetic functions | 3.4 | PASS |
| Theorem 3.4 | 1.3, 3.1–3.3 | Paper 1 translation layer | PASS |
| Definitions 4.1–4.2 | 1.1 | 4.3, 4.4 | PASS |
| Proposition 4.3 | 3.2, 4.2, classical definition of \(\Lambda\) | applications only | PASS |
| Reformulation 4.4 | 2.2, 4.1 | examples only | PASS, not a prime theorem |
| Definitions 5.1–5.3 | finite-dimensional linear algebra | 5.4–5.8 | PASS |
| Theorem 5.4 | 5.1–5.3, elementary congruences | 5.5–5.8, 6.2 | PASS |
| Corollary 5.5 | 5.4, rank-nullity | examples | PASS |
| Corollary 5.6 | 5.4 | examples, reconstruction | PASS |
| Proposition 5.7 | 5.3 | zero Fourier mode interpretation | PASS |
| Proposition 5.8 | 5.3, invertibility of DFT | Fourier interpretation | PASS |
| Definition 6.1 | 5.2 | 6.2–6.4 | PASS |
| Theorem 6.2 | 5.4, lcm congruence equivalence | 6.3–6.4 | PASS |
| Corollary 6.3 | 6.2 | reconstruction | PASS |
| Proposition 6.4 | 6.1, 6.3 | stability statement | PASS |
| Definition 6.5 | 5.3 | Open Problem 8.1 | PASS |
| Definition 7.1 | elementary exponential notation | 7.2 | PASS |
| Proposition 7.2 | 7.1 | phase correction | PASS |
| Deferred Observation 8.5 | not yet defined/proved | none in core | correctly deferred |

## 4. Hidden-convention audit

The following conventions are now explicit:

1. \(N\ge2\) for every positive addition fiber and channel space.
2. \(r\ge1\) for every modular channel.
3. Vectors in \(\mathbb N_0^{(\mathbb P)}\) have finite support.
4. Fibers are ordered unless explicitly quotiented by reflection.
5. Channel output coordinates are indexed by residue classes, not by chosen integer representatives.
6. The joint operator records the full residue tuple, whereas the marginal operator vertically stacks separate channel totals.
7. Singular-value claims use the standard Euclidean norms on the stated coordinate spaces.
8. Goldbach statements are exact reformulations only.

Result: **PASS after canonical repairs**.

## 5. Structural risk register

- **Dirichlet-character observation:** correctly removed from the proved-corollary list; remains deferred.
- **Joint-operator codomain:** now explicit through \(\Sigma_{\mathbf r}\).
- **Injectivity criterion:** now stated as an if-and-only-if condition, including valid even-modulus cases.
- **Difference-phase wording:** now has the exact constancy criterion \(2\alpha\in\mathbb Z\).
- **Zero-frequency statement:** now appears as a proved proposition rather than an unsupported note.

No remaining structural blocker was found in the canonical core.

## 6. Audit verdict

```text
NUMBERING = PASS
DEPENDENCIES = PASS
HIDDEN CONVENTIONS = PASS AFTER REPAIRS
UNDEFINED PROVED CLAIMS = 0
DEFERRED UNPROVED OBSERVATIONS = 1
NEXT = computational cross-link audit
```
