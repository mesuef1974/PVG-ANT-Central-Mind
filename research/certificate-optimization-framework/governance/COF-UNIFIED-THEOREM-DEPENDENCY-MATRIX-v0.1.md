# COF Unified Theorem Dependency Matrix v0.1

## Purpose

This matrix separates the abstract Certificate Optimization Framework from the additive realization, exact-search machinery, precedence layer, and PVG–Fourier application.

Legend:

- `Core`: finite object/target/configuration language;
- `Add`: additive certificate representation;
- `NN`: nonnegative contributions;
- `Dom`: componentwise dominance;
- `Prec`: sound acyclic precedence orientation;
- `B`: cardinality budget;
- `UB`: admissible node upper bound;
- `Mand`: sound mandatory sets;
- `Down`: downward-closed node resource family;
- `Fourier/PVG`: application-specific input.

| ID | Result | Core | Add | NN | Dom | Prec | B | UB | Mand | Down | Fourier/PVG | Classification |
|---|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|
| COF-T001 | additive update identity | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | definition/identity |
| COF-T002 | monotonicity of `L_S` and `F(S)` | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | theorem |
| COF-T003 | dominance exchange | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | theorem |
| COF-T004 | existence of precedence-legal optimum | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | theorem |
| COF-T005 | dominated-object deletion is generally invalid | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | boundary/counterexample |
| COF-T006 | safe Branch-and-Bound pruning | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | theorem |
| COF-T007 | exactness of finite comprehensive Branch-and-Bound | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | theorem |
| COF-T008 | coordinatewise top-gain upper bound | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | theorem |
| COF-T009 | inclusion precedence propagation | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | theorem |
| COF-T010 | exclusion precedence propagation | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | theorem |
| COF-T011 | precedence-aware exact-search preservation | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | ✗ | theorem |
| COF-T012 | joint necessity of mandatory sets | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | theorem |
| COF-T013 | admissible mandatory-compatibility bound | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | theorem |
| COF-T014 | pairwise compatibility graph bound | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | theorem |
| COF-T015 | higher-order bound dominates pairwise relaxation | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | theorem |
| COF-T016 | minimal-obstruction characterization of the relaxation | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | theorem |
| COF-T017 | exact antichain compression | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | theorem |
| COF-T018 | valid minimal-obstruction 0–1 cuts | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✗ | theorem |
| COF-T019 | top-gain mandatory-object test | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | theorem |
| FCF-R001 | reduced-frequency additive realization | ✓ | ✓ | ✓ | application | application | ✓ | ✗ | ✗ | ✗ | ✓ | realization theorem |
| PVG-R001 | prime-valuation addition-fiber realization | ✓ | application | application | application | application | application | application | application | application | ✓ | realization theorem |

## Layer assignment

### Abstract COF core

`COF-T001` through `COF-T019`, with each theorem carrying only the assumptions marked above.

### Fourier Certificate Framework

The Fourier layer must prove that its retained-frequency lower bound has the additive nonnegative form required by the COF theorems and must separately certify all tail and contamination thresholds.

### PVG application

The PVG layer supplies the arithmetic observables, reduced residue channels, exact Fourier identities, and the independently validated higher-prime-power contamination interface.

## Corrections enforced by the matrix

1. Branch-and-Bound exactness is not an additive theorem.
2. Dominance exchange does not require nonnegative contributions.
3. Mandatory compatibility is necessary, not sufficient, for simultaneous certification.
4. Minimal-obstruction compression is exact for the mandatory-set relaxation, not automatically for the original certification problem.
5. A forbidden family may contain multiple minimal forbidden obstructions.
6. Finite benchmark equality with exhaustive optimization is evidence for the implementation, not an assumption in the abstract theorem.

## Current maturity

- abstract foundations: three validated units;
- unified dependency audit: complete at v0.1;
- coherent paper draft: next;
- second independent realization: absent;
- transferability claim: not yet authorized.
