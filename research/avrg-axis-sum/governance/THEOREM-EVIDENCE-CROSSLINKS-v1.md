# Theorem-to-Evidence Crosslinks — Theory Freeze v1.0

Status: canonical evidence registry for Paper 1.

Purpose: connect every accepted result to its proof source, hand-checkable examples, and computational evidence without confusing finite verification with proof.

## Evidence classes

- **P** — deductive proof in the canonical theory.
- **H** — hand-checkable finite example.
- **C** — computational finite verification.
- **R** — exact reformulation of a known statement; not a new theorem about primes.

Computational evidence supports auditing and error detection. It does not replace the general proofs.

## Canonical sources

- Theory core: `research/avrg-axis-sum/theory/CANONICAL-DEFINITIONS-AND-RESULTS-v1.md`
- Proof audit: `research/avrg-axis-sum/governance/PROOF-AUDIT-v1.md`
- Dependency audit: `research/avrg-axis-sum/governance/DEPENDENCY-AND-NUMBERING-AUDIT-v1.md`
- Rank verifier: `research/avrg-axis-sum/code/verify_pvg_fiber_reconstruction_rank.py`
- Rank result: `research/avrg-axis-sum/results/pvg_fiber_reconstruction_rank_verification_001.json`
- Examples:
  - `research/avrg-axis-sum/examples/MANUAL-EXAMPLE-N10.md`
  - `research/avrg-axis-sum/examples/MANUAL-EXAMPLE-N12.md`
  - `research/avrg-axis-sum/examples/MANUAL-EXAMPLE-N24.md`
  - `research/avrg-axis-sum/examples/MANUAL-EXAMPLE-N30.md`

## Result registry

| ID | Result | Proof | Hand evidence | Computational evidence | Status |
|---|---|---|---|---|---|
| T1 | No-information-loss theorem | Canonical §2, using exact recovery | N=10,12,24,30 fiber tables | not needed | certified |
| T2 | Fiber convolution identity | Canonical §3 | constant-function check in all four examples | not needed | certified |
| T3 | Fiber reflection structure | Canonical §2 | orbit decompositions for N=10,12,24,30 | not needed | certified |
| T4 | Single-modulus rank theorem | Canonical §5 | injective/noninjective channels in all four examples | 9,900 cases, N,r≤100, zero mismatches | certified |
| T5 | Kernel-dimension formula | rank-nullity from T4 | explicit kernel bases in all four examples | implied by verified ranks | certified |
| T6 | Joint-modulus rank theorem | Canonical §6 via compatible residue signatures modulo L | no dedicated hand example yet | no dedicated verifier yet | proved; extra evidence optional |
| T7 | Joint-modulus conditioning | Canonical §6: injective incidence matrix becomes identity after row deletion/reordering | no dedicated hand example yet | no dedicated verifier yet | proved; extra evidence optional |
| T8 | Fourier equivalence | Canonical §5: full DFT is invertible | conceptual check only | no dedicated verifier needed | certified |
| C1 | General single-modulus injectivity criterion | immediate from T4 | r=9,11,23,29 injective examples; r=5,7,11,13 noninjective examples | explicit recovery checked by verifier for odd r≥N−1 | certified |
| C2 | Joint reconstruction criterion | immediate from T6 | no dedicated hand example yet | no dedicated verifier yet | proved; extra evidence optional |
| C3 | Zero-frequency identity | partition of column indices by residue channel | channel totals in examples | verifier confirms sum row never increases rank in all 9,900 cases | certified |
| P1 | Character-row redundancy | not yet defined and proved in canonical core | none | none | pending; excluded from proved core |
| R1 | Goldbach intersection form | exact use of valuation injectivity | N=10,12,24,30 prime-prime intersections | not applicable | exact reformulation only |
| R2 | von Mangoldt support on prime-power axes | definition of Λ and exact recovery | visible in valuation tables | not applicable | exact reformulation only |

## Coverage assessment

### Fully covered by proof plus manual examples

T1, T2, T3, T4, T5, C1, C3, R1, and R2.

### Proved but lacking a dedicated worked multiple-modulus example

T6, T7, and C2.

This is not a logical gap. It is an exposition and test-coverage gap. During the freeze, the permitted remedy is to add one worked joint-modulus example without introducing any new concept.

### Deliberately pending

P1 remains outside the proved core. It must not be cited as a theorem until the character measurement operator, treatment of nonunits, and factorization through residue-channel data are explicitly defined and proved.

## Computational certificate summary

The verifier constructs the exact incidence matrix

\[
(D_{N,r})_{d,a}=1_{\{2a-N\equiv d\pmod r\}}
\]

for every

\[
2\le N\le100,\qquad 1\le r\le100.
\]

It checked 9,900 parameter pairs and reported:

- rank mismatch count: 0;
- maximum rank error: 0;
- the all-ones sum row never increased rank;
- explicit recovery succeeded for every tested odd `r >= N-1`.

These are finite checks of statements already proved symbolically.

## Freeze decision

The computational cross-link requirement is complete for the single-modulus theory. The remaining evidence task is a single dedicated joint-modulus worked example for T6, T7, and C2. That task is classified as documentation/test completion, not theoretical expansion.
