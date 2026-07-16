# RMG-GOV-001 — Mandatory PVG Necessity Gate

Status: `active_for_new_claims / retrospective_audit_pending`

## Governing question

Before a result is labelled a PVG contribution, test:

> If PVG notation, valuation vectors, and PVG-specific structure are removed, do the statement, proof, and discovery mechanism remain materially unchanged?

## Necessity levels

- `PVG-N0 DECORATIVE_RENAMING`: PVG can be removed without loss.
- `PVG-N1 EQUIVALENT_REPARAMETERIZATION`: exact coordinate change only.
- `PVG-N2 ORGANIZATIONAL_OR_PROOF_ECONOMY`: no new mathematical object, but genuine compression or structural organization.
- `PVG-N3 PVG_GENERATED_DIAGNOSTIC`: PVG materially suggests a new observable, diagnostic, or experiment, even if the final proof is classical.
- `PVG-N4 PVG_GENERATED_THEOREM_STATEMENT`: the theorem statement materially arises from PVG structure.
- `PVG-N5 PVG_ESSENTIAL_PROOF`: the proof requires genuinely PVG-specific structure.

## Mandatory fields for PVG claims

Any record claiming `PVG contribution`, `PVG-derived`, `new PVG theorem`, or `PVG mechanism` must include:

- `pvg_necessity_level`
- `removal_test_result`
- `what_breaks_without_pvg`
- `classical_reduction`
- `novelty_class`
- `prior_art_status`

## Permitted classifications

- `ORIGINAL_PVG_RESULT`
- `PVG_GENERATED_OBSERVABLE`
- `PVG_REINTERPRETATION`
- `CLASSICAL_RESULT_IN_RMG`
- `DIAGNOSTIC_ONLY`
- `PRIOR_ART_OVERLAP`

## Claim ceiling

A result at `PVG-N0` or `PVG-N1` may remain valuable to the ANT–PVG mind, but must not be described as a new PVG theorem without an independent novelty argument.

A finite computation cannot raise the necessity level. Necessity concerns the mathematical role of PVG, not the amount of testing.

## Immediate governance decision

All future RMG units must carry a necessity classification whenever they mention a PVG contribution. Retrospective migration of existing theorem-labelled files is required before publication or training-corpus authorization.
