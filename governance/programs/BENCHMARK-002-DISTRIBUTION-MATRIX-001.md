# BENCHMARK-002-DISTRIBUTION-MATRIX-001

**Stage:** S1 authoring workshop of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001`.
**Governs:** how the `Hidden Set A` and `Hidden Set B` cases are allocated across the twelve
capability axes, under `BENCHMARK-002-SEALING-PROTOCOL-001.md` §1–§2 and registered spec §1.
**Frozen at workshop open.** The counts below are fixed before authoring and re-recorded into
`HIDDEN-A-MANIFEST` / `HIDDEN-B-CIPHERTEXT` metadata at seal time. Contains NO cases, NO keys.
Capability measurement only — zero RH progress, zero GRH progress.

## 1. Primary distribution — twelve axes × two sets
A and B use the SAME per-axis allocation so B is a true independent generalization mirror of A,
not a topic B never saw. `*` marks the autopsy-flagged failure-prone axes carrying adversarial
weight (quantifier discipline, normalization, LOSS, proof-gap detection, overclaim refusal).
```
#   capability axis                         A     B    (A+B)
1   ANT correctness                          4     4      8
2   PVG → ANT translation                    3     3      6
3   ANT → PVG translation                    3     3      6
4   LOSS / non-invertibility accounting  *   5     5     10
5   quantifier discipline                *   5     5     10
6   normalization                        *   5     5     10
7   provenance                               3     3      6
8   scope / domain-of-validity containment   3     3      6
9   tool selection                           3     3      6
10  certificate classification              4     4      8
11  proof-gap detection                  *   5     5     10
12  overclaim refusal                    *   5     5     10
    -----------------------------------------------------------
    TOTAL per set                           48    48     96
    weighted axes (*) subtotal per set      25 (52%)
    standard axes subtotal per set          23 (48%)
```
Invariants held by this matrix:
- `A = 48 ≥ 48`, `B = 48 ≥ 48`, `total = 96 ≥ 96`.
- Every axis carries ≥ 3 cases in EACH of A and B (no axis absent from either set).
- The five failure-prone axes each carry 5 per set; every standard axis carries 3–4.
- A and B are per-axis identical, so a per-axis A↔B comparison is well-posed.

## 2. Cross-cutting quotas (overlaid on the 48 — each case is ONE axis but carries these tags)
These minimum quotas ensure the reporting cuts of the frozen rubric §5 have signal. They
overlay the axis allocation; a single case counts once toward its axis and simultaneously
carries a LOSS tag, a composition-depth tag, a tier tag, and (where applicable) an
abstention/reverse-inference tag.
```
per set (A, and identically B):
  abstention / impossibility cases                 ≥ 8   (correct answer is abstain, or
                                                          impossible-with-counterexample/missing-cert)
  LOSS-level span                                  ≥ 1 case at each of LOSS-0,1,2,3,4;
                                                   ≥ 10 cases carry an explicit LOSS judgment
  composition depth ≥ 2 (multi-step morphism chain) ≥ 8
  reverse-inference cases (ANT→PVG or projection-inversion) ≥ 6
  tier labeling                                    every case tagged B0 | B1 | B2;
                                                   ≥ 12 answerable at B0 (pure reasoning)
```
Quotas are minima, not exact cell counts; over-constraining 48 cases into a full multi-way
cross-tab is forbidden (it would leak structure). Authors satisfy the minima while keeping
prompts natural and adversarial.

## 3. Adversarial intent (not 96 generic questions)
Weighting concentrates on the axes where the source autopsies and prior passes showed the
mind is most likely to fail silently: asserting uniformity it did not earn (axis 5), dropping
a normalization (axis 6), inverting a lossy translation (axis 4), missing a proof gap
(axis 11), or overclaiming instead of abstaining (axis 12). Easy-to-pass axes are capped so
the aggregate cannot be inflated by trivia.

## 4. Freeze and provenance
This matrix is frozen with `BENCHMARK-002-FROZEN-SCORING-RUBRIC-001` at workshop open. Any
change is a recorded distribution-change event that re-opens review; it is never an
authoring-time convenience. The final realized per-axis counts are re-attested in the seal
manifests and must equal this matrix (or exceed the ≥ floors with a recorded justification).

## Ceiling
```
allocation plan only · no cases · no keys · no runs
zero RH progress · zero GRH progress · no secured path
```
