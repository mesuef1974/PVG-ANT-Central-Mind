# IGD001 — Ingham Gate Numerical Diagnostic

Diagnostic pass for the **Ingham gate**, the admission test that must be passed before
`PVG-Additive` is opened. This directory contains a *numerical diagnostic only*.

```text
INGHAM-GATE     = NOT-ATTEMPTED
PVG-CONTRIBUTION = NOT-SHOWN
SCIENTIFIC-JUDGMENT (on the theorem) = CLOSED
```

Passing the gate requires **deriving** the asymptotic inside the PVG framework.
Citing a published formula is not passing. Reproducing it numerically is not passing.
This pass does neither; it only checks that the transcribed constants are not corrupted
before any derivation work is built on top of them.

## Object

```text
D_h(x) = sum_{n <= x} d(n) d(n+h)
```

Classical statement (Ingham 1927; Estermann 1931 expansion; error improved by
Heath-Brown; modern uniform treatment via Motohashi 1994):

```text
D_h(x) = (6/pi^2) sigma_{-1}(h) x log^2 x + a_1(h) x log x + a_2(h) x + O(x^{11/12+eps})
```

The two derived, zero-free-parameter predictions tested here:

```text
R_h(x) = D_h(x)/D_1(x) = sigma_{-1}(h) - 4 sigma'_{-1}(h)/log x + O(1/log^2 x)
Q_h    = lim log^2 x [ R_h/sigma_{-1}(h) - 1 + 4 rho_h/log x ] = 2 K rho_h + 4 tau_h
```

with `sigma'_{-1}(h) = sum_{d|h} log(d)/d`, `sigma''_{-1}(h) = sum_{d|h} log(d)^2/d`,
`rho_h = sigma'_{-1}(h)/sigma_{-1}(h)`, `tau_h = sigma''_{-1}(h)/sigma_{-1}(h)`,
`K = 2(2 gamma - 1 - 2 zeta'(2)/zeta(2)) = 2.5887066320...`

## Layout

| path | contents |
|---|---|
| `PRE_RUN_SPECIFICATION.md` | the protocol as agreed **before** execution (transcribed after) |
| `protocol.json` | machine-readable form of the same |
| `src/` | `d1.c`, `dmulti.c` (segmented divisor sieves), `brute.c` (independent check) |
| `data/dmulti_out.txt` | raw checkpoint sums |
| `analysis/verify_igd001.py` | recomputes every reported quantity from the raw data |
| `reports/IGD001_RESULT.md` | verdicts |
| `certificates/` | execution receipt and closure review |

## Reproduce

```bash
gcc -O3 -march=native -fopenmp src/dmulti.c -o dmulti && ./dmulti 10 > data/dmulti_out.txt
gcc -O2 src/brute.c -o brute && ./brute 1000000        # independent cross-check at 1e6
python analysis/verify_igd001.py
```

Runtime for `X_max = 1e10`: ~200 s on 20 threads.

## Related

Structural bridge: [`maps/bridges/BRIDGE-DIVISOR-BOX-CONVOLUTION-001.md`](../../../../maps/bridges/BRIDGE-DIVISOR-BOX-CONVOLUTION-001.md).
That bridge is an exact structural identity; its maturity is **not** changed by this pass,
and it already records that the divisor-box picture alone does not produce an asymptotic.
