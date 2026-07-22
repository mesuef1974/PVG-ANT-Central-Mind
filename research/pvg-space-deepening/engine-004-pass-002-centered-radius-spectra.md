# ENGINE-004 PASS-002 — Governed Centered-Radius Spectra

```text
Goal ID: GOAL-OP-INVERSE-PRIME-FIBERS-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Status: implementation_checkpoint / awaiting complete CI
Scope: frozen 884-point box only
Phase D: NOT AUTHORIZED
Classification: IDENTITY / PROVED / FINITE-VERIFIED after complete audit
```

## Authorized object

For each centered gap

\[
\Delta=q-p,
\]

define the governed spectrum

\[
D(N)=
\begin{cases}
\{\Delta/2:\Delta\in\Delta_2(N)\},&N\text{ even},\\
\Delta_2(N),&N\text{ odd}.
\end{cases}
\]

For even `N=2m`, every gap is `Delta=2d`, and

\[
p=m-d,\qquad q=m+d,\qquad \gcd(m,d)=1.
\]

For odd `N`, the prime fiber is empty or consists of `2+(N-2)`, so retaining the unnormalized gap preserves the authorized odd route.

## Governance correction

An initial implementation used the scale-free ratio `Delta/N`. That coordinate is mathematically valid, but it was not the object authorized by `transition-memory/next-action.md`. It has therefore been removed from this pass. No result from that superseded implementation is promoted.

## Finite relations

Inside the unchanged frozen box, compute only:

1. equality classes of nonempty spectra;
2. strict containment relations;
3. coordinate collisions across integer points and support faces;
4. point-to-spectrum compression;
5. information preserved and lost by the spectrum projection.

These are exact finite set relations, not asymptotic statements.

## Implementation

```text
tools/pvg_centered_radius_spectra.py
tests/test_pvg_centered_radius_spectra.py
.github/workflows/pvg-centered-radius-spectra-audit.yml
```

Required commands:

```text
python -m unittest -v tests/test_pvg_centered_radius_spectra.py
python tools/pvg_centered_radius_spectra.py --registered-summary --compact
python tools/honesty_audit.py
python tools/state_coherence_audit.py
```

## Current claim ceiling

```text
Definitions and parity routing: IDENTITY / PROVED
Frozen-box enumeration: FINITE-VERIFIED only after complete CI success
Compression meaning: INTERPRETATION
Historical originality: NOT CLAIMED
```

This pass does not authorize cap expansion, Phase D, orbit dynamics, theorem reactivation, an asymptotic law, or any Goldbach, PNT, RH, or GRH claim.
