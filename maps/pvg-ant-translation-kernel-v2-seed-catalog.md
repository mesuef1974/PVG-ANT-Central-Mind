# PVG–ANT Translation Kernel v2 — Seed Catalog

**Pass:** `TRANSLATION-KERNEL-V2-PASS-001`  
**Status:** validated intake; not closed  
**Machine truth:** `registries/pvg-ant-translation-kernel-v2/*.jsonl`

Pass 001 preserves the eight closed v1 bridge families and adds 24 operational cards. Each registry row contains the full forward/reverse map, preserved and lost information, tool routing, wall, required certificate, positive example, counterexample, and anti-overclaim statement.

## Inventory

| ID | Domain | Direction | Title | Test |
|---|---|---|---|---|
| `TR-V2-SUPPORT-OMEGA-001` | `geometry_arithmetic` | `bidirectional` | Valuation support and prime-factor counts | `EX2-SUPPORT-360` |
| `TR-V2-RADICAL-BOOLEAN-001` | `geometry_arithmetic` | `bidirectional` | Boolean support cube and squarefree projection | `EX2-RADICAL-72` |
| `TR-V2-HEIGHT-ADDITIVE-001` | `geometry_arithmetic` | `bidirectional` | Coordinate height sums and additive functions | `EX2-HEIGHT-360` |
| `TR-V2-LOG-MASS-001` | `geometry_arithmetic` | `bidirectional` | Prime-coordinate logarithmic mass and integer size | `EX2-LOG-72` |
| `TR-V2-DIVISOR-BOX-TAU-001` | `geometry_arithmetic` | `bidirectional` | Divisor boxes and lattice-point counts | `EX2-DIVBOX-360` |
| `TR-V2-MARGIN-INTERIOR-001` | `geometry_arithmetic` | `bidirectional` | Margin-interior points and weighted powerful support | `EX2-MARGIN-432` |
| `TR-V2-FACE-ENUMERATOR-001` | `geometry_arithmetic` | `bidirectional` | Face enumerators and boundary-coordinate polynomials | `EX2-FACE-72` |
| `TR-V2-POWERFUL-SUPPORT-001` | `geometry_arithmetic` | `bidirectional` | Minimum height constraints and k-full integers | `EX2-POWERFUL-72` |
| `TR-V2-BELL-SERIES-001` | `local_analytic` | `bidirectional` | Prime-axis data and Bell series | `EX2-BELL-R2` |
| `TR-V2-FIRST-LOCAL-LAYER-001` | `local_analytic` | `pvg_to_ant` | First nonzero local exponent and candidate main scale | `EX2-FIRST-LAYER-R2` |
| `TR-V2-POLE-LOG-DEGREE-001` | `local_analytic` | `bidirectional` | Pole order and logarithmic polynomial degree | `EX2-POLE-ORDER` |
| `TR-V2-RESIDUAL-CANCELLATION-001` | `local_analytic` | `pvg_to_ant` | Residual local order and continuation half-plane | `EX2-RESIDUAL-R1` |
| `TR-V2-MELLIN-SMOOTHING-001` | `transforms` | `bidirectional` | Smooth size weights and Mellin inversion | `EX2-MELLIN-NORMALIZATION` |
| `TR-V2-PERRON-SHARP-CUTOFF-001` | `transforms` | `bidirectional` | Sharp cutoffs and Perron or Tauberian transfer | `EX2-PERRON-KERNEL` |
| `TR-V2-CONVOLUTION-DECOMPOSITION-001` | `geometry_arithmetic` | `bidirectional` | Valuation-vector decompositions and Dirichlet convolution | `EX2-CONVOLUTION-12` |
| `TR-V2-RESIDUE-FOURIER-001` | `residues` | `bidirectional` | Residue fibers and character Fourier coordinates | `EX2-RESIDUE-MOD5` |
| `TR-V2-PRINCIPAL-SUBTRACTION-001` | `residues` | `bidirectional` | Principal-mode removal and balanced residue fluctuations | `EX2-PRINCIPAL-CENTER` |
| `TR-V2-FIBER-VARIANCE-001` | `residues` | `bidirectional` | Residue-fiber variance and character second moments | `EX2-FIBER-PARSEVAL` |
| `TR-V2-SIEVE-TRUNCATION-001` | `sieve` | `bidirectional` | Truncated valuation depth and sieve visibility | `EX2-SIEVE-72-D9` |
| `TR-V2-AGGREGATE-LOSS-001` | `sieve` | `ant_to_pvg` | Aggregate sieve data and noninjective information loss | `EX2-AGGREGATE-LOSS` |
| `TR-V2-BILINEAR-TYPE12-001` | `sieve` | `bidirectional` | Two-block valuation interactions and Type I/II structure | `EX2-BILINEAR-ROUTING` |
| `TR-V2-PARITY-PHASE-WALL-001` | `sieve` | `ant_to_pvg` | Support data versus parity, sign, and phase walls | `EX2-PARITY-SIGN` |
| `TR-V2-ADDITIVE-PROBABILISTIC-001` | `probabilistic` | `bidirectional` | Local coordinate contributions and probabilistic additive models | `EX2-ADDITIVE-MOMENTS` |
| `TR-V2-EXCEPTIONAL-SET-IMPACT-001` | `probabilistic` | `bidirectional` | Geometric exceptional sets and weighted impact | `EX2-EXCEPTIONAL-SPIKE` |

## Domain counts

- `geometry_arithmetic`: 9
- `local_analytic`: 4
- `probabilistic`: 2
- `residues`: 3
- `sieve`: 4
- `transforms`: 2

## Pass ceiling

```text
New operational cards = 24
Closed v1 families retained = 8
Combined inventory = 32
L3 promotions = 0
Second theorem target = not opened
One-Theorem 001 hold = unchanged
Dataset 004 = unauthorized
RH/GRH progress = none
```
