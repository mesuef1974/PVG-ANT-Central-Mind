# Theory Freeze Lift Decision — v1.1

Date: 2026-07-15

Branch: `agent/pvg-addition-fibers-theory-001`

## Decision

`THEORY-FREEZE-v1.0` is hereby lifted by explicit owner instruction.

New status:

```text
THEORY-STATE = ACTIVE-RESEARCH-v1.1
FREEZE = LIFTED
OWNER AUTHORIZATION = GRANTED
```

## Scope of the lift

The lift authorizes new theoretical development beyond the frozen Paper 1 core, while preserving the completed v1.0 core as a stable baseline.

The following remain mandatory:

1. Every new definition must be explicit.
2. Every theorem claim must include a proof or remain labeled conjecture/candidate statement.
3. Finite computation must not be presented as proof of a general theorem.
4. Goldbach, RH, GRH, major-arc, minor-arc, and sieve claims remain subject to the existing scientific ceiling.
5. No novelty or priority claim is authorized without a deeper literature review.
6. Completed research units must be committed and pushed continuously.

## Frozen baseline preserved

The following artifacts remain the controlling v1.0 baseline:

- `theory/CANONICAL-DEFINITIONS-AND-RESULTS-v1.md`;
- `paper/PAPER-001-PRIME-VALUATION-ADDITION-FIBERS-DRAFT.md`;
- `governance/PROOF-AUDIT-v1.md`;
- `governance/DEPENDENCY-AND-NUMBERING-AUDIT-v1.md`;
- `governance/THEOREM-EVIDENCE-CROSSLINKS-v1.md`;
- `governance/PAPER-001-TEXTUAL-CONSISTENCY-AUDIT-v1.md`.

These files may be corrected if a genuine error is found, but new research should be developed in new v1.1 files before any later canonical integration.

## First activated research target

The first active target is the marginal stacked operator

\[
M_{N;\mathbf r}
=
\begin{pmatrix}
D_{N,r_1}\\
\vdots\\
D_{N,r_s}
\end{pmatrix}.
\]

Research objective:

- determine exact rank formulas where possible;
- characterize the kernel;
- understand the distinction between separate marginals and full joint signatures;
- compute singular values and conditioning;
- identify natural graph- or incidence-theoretic models.

## Classification

This decision changes governance status only. It does not itself establish a new mathematical theorem.
