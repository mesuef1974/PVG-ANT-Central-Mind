# PVG–ANT Language Kernel v1 — Release Index

**Operational goal:** `GOAL-OP-LANGUAGE-KERNEL-V1-001`  
**Registry:** `registries/pvg-ant-bridges.jsonl`  
**Examples:** `maps/bridge-example-expected.json`  
**Classification ceiling:** certified L1/L2 language; no original lemma or theorem.

## Frozen canonical families

| # | Canonical bridge | Family | Maturity | Gain | Card |
|---:|---|---|---|---|---|
| 1 | `BRIDGE-MULTIPLICATIVE-LINEARIZATION-001` | multiplication/divisibility/order | L2 | structural | `maps/bridges/BRIDGE-MULTIPLICATIVE-LINEARIZATION-001.md` |
| 2 | `BRIDGE-DIVISOR-BOX-CONVOLUTION-001` | divisor boxes/convolution | L2 | structural | `maps/bridges/BRIDGE-DIVISOR-BOX-CONVOLUTION-001.md` |
| 3 | `BRIDGE-EULER-COORDINATE-FACTORIZATION-001` | multiplicative observables/Euler factors | L2 | analytic | `maps/bridges/BRIDGE-EULER-COORDINATE-FACTORIZATION-001.md` |
| 4 | `BRIDGE-LOG-HALFSPACE-LATTICE-SUM-001` | logarithmic half-spaces/weighted sums | L1 | expository | `maps/bridges/BRIDGE-LOG-HALFSPACE-LATTICE-SUM-001.md` |
| 5 | `BRIDGE-SQUAREFREE-MOBIUS-001` | squarefree support/Möbius | L2 | structural | `maps/bridges/BRIDGE-SQUAREFREE-MOBIUS-001.md` |
| 6 | `BRIDGE-RESIDUE-CHARACTER-FOURIER-001` | residue fibers/characters | L2 | analytic | `maps/bridges/BRIDGE-RESIDUE-CHARACTER-FOURIER-001.md` |
| 7 | `BRIDGE-SIEVE-INFORMATION-001` | sieve visibility/aggregation/certificates | L2 | analytic | `maps/bridges/BRIDGE-SIEVE-INFORMATION-001.md` |
| 8 | `BRIDGE-ANALYTIC-TRANSFER-001` | local/global analytic transfer | L2 | analytic | `maps/bridges/BRIDGE-ANALYTIC-TRANSFER-001.md` |

## Relation to previously reconciled bridges

The detailed legacy entries remain valid source bridges:

- `BRIDGE-SIEVE-TRUNCATED-VALUATION-001` and `BRIDGE-SIEVE-AGGREGATION-LOSS-001` are components of canonical family 7.
- `BRIDGE-RESIDUE-PRINCIPAL-REMOVAL-001` and `BRIDGE-RESIDUE-VARIANCE-PARSEVAL-001` are components of canonical family 6.
- `BRIDGE-PVG-LAYER-SEPARATION-001` is a routing law applied to all eight families.
- `BRIDGE-EDGE-ERROR-SEPARATION-001` is a barrier-localization example under canonical family 8.

No historical bridge is silently deleted or promoted. The release registry defines the eight reusable families; the main kernel retains their derivation and source context.

## Release rule

A family is reusable only when:

1. its registry row is complete;
2. its card names forward and reverse maps or loss;
3. its analytic transform and hypotheses are explicit;
4. its finite example matches the committed certificate;
5. its gain and maturity pass `tools/language_kernel_audit.py`.

No family in v1 is L3. A later L3 promotion requires a proved transfer lemma with a genuine analytic consequence.
