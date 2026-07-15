# ACTIVE-002-D — Row Preconditioning Status

Status: `CLOSED — PASS WITH CORRECTION`

## Completed

1. Proved that invertible left preconditioning preserves rank and kernel.
2. Defined canonical row normalization by inverse row norm.
3. Proved that Frobenius block normalization is ineffective in this model because every marginal block has Frobenius norm \(\sqrt{N-1}\).
4. Added a reusable verifier.
5. Verified six benchmark full-rank designs with zero rank mismatches and zero numerical nullspace-projector discrepancy.
6. Recorded conditioning improvements under row normalization for all six benchmarks.
7. Corrected the previously inconsistent \(N=30\) best-conditioned benchmark in the cost-rank-conditioning summary.

## Key numerical outcomes

- \(N=16,\{5,11\}\): \(\kappa^+\) improved from approximately \(9.0926\) to \(7.8623\).
- \(N=24,\{5,9,11\}\): \(108.7134\to92.4884\).
- \(N=24,\{7,9,11\}\): \(32.3756\to29.5267\).
- \(N=30,\{5,7,9,11\}\): \(1938.1831\to1763.5913\).
- \(N=30,\{7,8,9,11,12\}\): \(98.1734\to89.6487\).

## Correction receipt

The earlier summary had reported the \(N=30\), \(\{7,8,9,11,12\}\) design with

\[
\sigma_{\min}^+\approx0.00803,
\qquad
\kappa^+\approx589.01.
\]

An independent matrix reconstruction showed the correct values are

\[
\sigma_{\min}^+\approx0.04136795,
\qquad
\kappa^+\approx98.17338.
\]

The canonical JSON summary was corrected. The correction changes no rank theorem and no qualitative conclusion that conditioning matters; it materially improves the quantitative benchmark and is therefore recorded explicitly.

## Controlling files

- `theory/LEFT-PRECONDITIONING-ROW-NORMALIZATION-v1.1.md`
- `code/verify_row_preconditioning.py`
- `results/row_preconditioning_verification_v1.1.json`
- corrected `results/cost_rank_conditioning_pareto_summary_v1.1.json`

## Scientific classification

- Information preservation under invertible left scaling: `PROVED THEOREM`.
- Frobenius block-normalization ineffectiveness: `PROVED MODEL-SPECIFIC PROPOSITION`.
- Row-normalization improvements on listed cases: `COMPUTATION`.
- Global optimality of row normalization: `NOT CLAIMED`.

## Next target

`ACTIVE-002-E — optimized positive diagonal scaling`:

search for row or block weights minimizing \(\kappa_2^+\), with explicit normalization to remove the irrelevant global scale and with independent verification against the row-normalized baseline.
