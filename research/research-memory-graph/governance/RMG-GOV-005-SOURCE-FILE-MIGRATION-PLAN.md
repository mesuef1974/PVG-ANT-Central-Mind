# RMG-GOV-005 Governed Source-File Migration Plan

Status: PLAN_COMMITTED / SOURCE_PATCHES_NOT_STARTED

## Objective

Apply reviewed governance overlays to original source files without erasing history or silently rewriting mathematical claims.

## Migration order

1. Resolve exact source path and section.
2. Fetch the source at the current branch head.
3. Record current blob SHA.
4. Prepare the smallest possible patch.
5. Add explicit classification fields or a visible governance note.
6. Preserve theorem statements and proofs unless a mathematical correction is independently established.
7. Run the new-record policy and unit-specific verifier.
8. Commit each source migration separately.

## Priority classes

### P0

- ambiguous `L0..L7` labels;
- RH/GRH or Goldbach claim ceilings;
- files claiming original PVG contribution;
- theorem files with unresolved novelty language.

### P1

- abbreviated RMG records requiring canonical-schema overlays;
- classical results presented with project-specific terminology;
- source files lacking prior-art status.

### P2

- purely descriptive or historical documents with no active claim effect.

## Non-destructive requirements

- no bulk search-and-replace across mathematical files;
- no deletion of historical wording without a supersession note;
- no automatic novelty downgrade or upgrade from keyword matching alone;
- no automatic `MATH-*` promotion from computation, regression, or formalization metadata;
- exact source SHA required before modification.

## Exit criteria

A migrated claim requires:

- exact source locator;
- reviewed necessity classification;
- reviewed prior-art status;
- canonical namespace fields;
- passing enforcement hook;
- independent commit receipt.

`SOURCE_FILE_MIGRATION = NOT_STARTED`

`BULK_AUTOMATIC_REWRITE = PROHIBITED`
