# Edge-Case Repair: Difference-Phase Constancy at N=2

Status: mandatory correction under `THEORY-FREEZE-v1.0`.

## Issue

The unqualified statement

\[
a\mapsto e(\alpha(2a-N))\text{ is constant on the full fiber}
\iff 2\alpha\in\mathbb Z
\]

is false when \(N=2\), because the index set contains only \(a=1\). A function on a one-point set is constant for every \(\alpha\).

## Correct statement

For \(N=2\), the difference phase is constant for every \(\alpha\).

For \(N\ge3\), the map

\[
a\longmapsto e(\alpha(2a-N))
\]

is constant on all indices \(a=1,\ldots,N-1\) if and only if

\[
2\alpha\in\mathbb Z.
\]

## Proof

When \(N=2\), there is only one phase value.

When \(N\ge3\), at least two consecutive indices occur. The ratio of consecutive phase values is

\[
\frac{e(\alpha(2(a+1)-N))}{e(\alpha(2a-N))}=e(2\alpha).
\]

All phase values are equal exactly when \(e(2\alpha)=1\), equivalently \(2\alpha\in\mathbb Z\).

## Integration requirement

This correction supersedes the unqualified constancy criterion wherever it appears in:

- `CANONICAL-DEFINITIONS-AND-RESULTS-v1.md`;
- `PAPER-001-PRIME-VALUATION-ADDITION-FIBERS-DRAFT.md`;
- `THEORY-STATUS.md`.

Until those files are textually updated, this repair file is the controlling statement.
