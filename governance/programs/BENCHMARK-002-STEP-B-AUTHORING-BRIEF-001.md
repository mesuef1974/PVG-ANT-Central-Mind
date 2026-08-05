# BENCHMARK-002-STEP-B-AUTHORING-BRIEF-001

**Stage:** S1 (window closes 2026-08-16) of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001` — STEP B.
**Operationalizes:** `BENCHMARK-002-SEALING-PROTOCOL-001.md` §2, §3, §7, §8, §9, extended by
`BENCHMARK-002-HIDDEN-A-CONTAINMENT-DEFECT-001.md` remedy R4.
**Purpose:** the standing contract for the isolated session that authors `Hidden Set B`, so that
session does not re-derive the protocol and does not repeat the STEP A concealment defect.
**Contains:** no A material, no B cases, no keys, no runs. Frozen counts only, all already public.
**Ceiling:** capability measurement only — zero RH progress, zero GRH progress, no secured path.

## 0. Why the B session must be a different session

`SEALING` §0 makes one defect fatal to the whole benchmark: A/B prompts or keys entering the
answering context. `SEALING` §7 separates the case author, the key author, the answering agent, the
scoring agent, and the B custodian. A session that has handled Set-A keys — including any session
that regenerated them while auditing the containment defect — is disqualified from authoring B,
because B's independence from A is the only thing the single B run measures.

The authoring session must therefore begin cold: no A keys, no A prompts, no memory of the A cases.
It may read this brief, the sealing protocol, the distribution matrix, and the frozen rubric. All
four are public and contain no cases.

## 1. What B must hit (frozen, identical to A per axis)

From `BENCHMARK-002-DISTRIBUTION-MATRIX-001` §1 — this is frozen, not a target to negotiate:

```
#   capability axis                          B
1   ANT correctness                          4
2   PVG -> ANT translation                   3
3   ANT -> PVG translation                   3
4   LOSS / non-invertibility accounting  *   5
5   quantifier discipline                *   5
6   normalization                        *   5
7   provenance                               3
8   scope / domain-of-validity containment   3
9   tool selection                           3
10  certificate classification               4
11  proof-gap detection                  *   5
12  overclaim refusal                    *   5
    ---------------------------------------------
    TOTAL                                   48
```

Cross-cutting minima (§2 of the matrix), overlaid on the same 48:

```
abstention / impossibility cases                    >= 8
LOSS levels 0,1,2,3,4                               each >= 1; >= 10 cases carry a LOSS judgment
composition depth >= 2                              >= 8
reverse-inference cases                             >= 6
tier tag B0|B1|B2 on every case                     48/48;  >= 12 answerable at B0
```

Per-axis identity with A is what makes the A↔B comparison well-posed. Do not "improve" the
allocation.

## 2. Per-case schema (`SEALING` §3 — every field, every case)

```
case_id · prompt · capability_target · expected_structure · rubric ·
fatal_errors[closed §5 codes] · partial_credit · certificate_requirements ·
forbidden_claims · source_basis · leakage_class[closed §8 value] · tags
tags = {loss_level, loss_judgment, composition_depth, reverse_inference, abstention}
```

Every rubric component-weight vector sums to 100. `fatal_errors` draws only from the closed §5
code set; `leakage_class` only from the closed §8 set.

## 3. Leakage screen (`SEALING` §8 — conceptual outranks textual)

Screen every case against: Benchmark 001; all Translation Kernel cards (Pass 001 + 002); Core
Ontology objects/morphisms/witnesses; prior project examples and chats; the I_r theorem and its
pipeline; book-ledger units; near formulations. Decisions are fixed per value:

```
LEAK-0-CLEAR                                eligible
LEAK-1-TEXTUAL-OVERLAP                      reject
LEAK-2-CONCEPTUAL-OVERLAP                   reject
LEAK-3-NEAR-FORMULATION-OR-PROJECT-DERIVED  reject
LEAK-U-UNCERTAIN                            quarantine pending independent review
```

**New for B:** `Hidden Set A` is now public in the repository — prompts, scoring metadata, and the
authoring generator in git history. Any B case that is a near formulation of an A case is therefore
`LEAK-3`, **reject**. This is a real narrowing of the admissible space and the reason B must not be
authored by pattern-matching on A.

## 4. What reaches the repository (remedy R4 — the STEP A defect, not repeated)

STEP A withheld `A-keys.jsonl` by gitignore while committing the generator that re-emits it. Excluding
the output while committing the source is not concealment. For B:

```
COMMIT:      HIDDEN-B-CIPHERTEXT      encrypted prompts AND keys, offline-encrypted
             HIDDEN-B-SHA-256         manifest over the ciphertext
             HIDDEN-B-METADATA        realized per-axis counts and quota attestation, no cases

NEVER COMMIT: B prompts in plaintext
              B keys in plaintext
              any authoring script, notebook, or generator, in any language, that can re-emit
                either -- this is the R4 bar and it is structural, not a naming convention
              any file under the B staging directory outside its declared inventory
```

`SEALING` §9: a hash alone is not concealment. An independent custodian, distinct from the
answering agent, holds the decryption key.

## 5. Order of operations for the isolated session

```
1. Pre-stage sync receipt (RULE-SYNC-PER-STAGE-RECEIPTS-001): HEAD == origin/main, clean tree.
2. Author 48 cases against §1-§3 of this brief. Prompts separated from keys throughout.
3. Machine-validate the frozen invariants before anything is written out.
4. Encrypt prompts + keys offline. Verify the ciphertext decrypts to what was authored.
5. Commit ciphertext + SHA-256 + metadata only. Run the staging guard; it must PASS on content
   and inventory bars, not on filenames.
6. Post-stage sync receipt.
```

## 6. What remains after STEP B, before S2

```
[next]  LEAKAGE-AUDIT over A and B -- must record the Set-A containment defect, not a clean screen
[next]  6-10 calibration cases outside the score (FROZEN-SCORING-RUBRIC §6)
[next]  ENVIRONMENT-FREEZE-RECEIPT -- fields 1-13 currently UNSET; field 14 (the 6960cb5 pin)
        is settled in BENCHMARK-002-ENVIRONMENT-FREEZE-RECEIPT-001
[next]  SHA-256-MANIFEST over the sealed bundle -> BENCHMARK-002-SEALED
```

No S2 transition until every G1 item exists. The single B run is the only generalization measure;
the A rerun never is.

## Ceiling
```
authoring contract only · no cases · no keys · no runs · no scores
zero RH progress · zero GRH progress · no secured path
```
