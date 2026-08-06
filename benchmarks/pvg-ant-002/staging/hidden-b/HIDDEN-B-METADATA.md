# HIDDEN-B-METADATA-001

**Stage:** S1 of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001` — STEP B.
**Produces:** case-free metadata for `Hidden Set B` of `ADVERSARIAL-PVG-ANT-BENCHMARK-002`, under
`BENCHMARK-002-SEALING-PROTOCOL-001.md` §2, §3, §9 and `BENCHMARK-002-STEP-B-AUTHORING-BRIEF-001.md`.
**Status:** authored, schema-normalized, independently verified, and sealed as ciphertext.
Not the G1 `BENCHMARK-002-SEALED` bundle; `LEAKAGE-AUDIT`, calibration, the completed
`ENVIRONMENT-FREEZE-RECEIPT`, and the `SHA-256-MANIFEST` remain ahead.
**Contains no case, no prompt, no key.** Counts and verdicts only.
**Ceiling:** capability measurement only — zero RH progress, zero GRH progress, no secured path.

## 1. Realized per-axis distribution (must equal the frozen matrix — it does)
```
#   capability axis                          B(target)  B(realized)
1   ANT correctness                              4           4
2   PVG -> ANT translation                       3           3
3   ANT -> PVG translation                       3           3
4   LOSS / non-invertibility accounting  *       5           5
5   quantifier discipline                *       5           5
6   normalization                        *       5           5
7   provenance                                   3           3
8   scope / domain-of-validity containment       3           3
9   tool selection                               3           3
10  certificate classification                   4           4
11  proof-gap detection                  *       5           5
12  overclaim refusal                    *       5           5
    -------------------------------------------------------------
    TOTAL                                       48          48
```
Per-axis identical to Set A, so the A↔B per-axis comparison is well-posed.

## 2. Cross-cutting quotas
```
quota                                          floor   realized
abstention / impossibility cases                 >= 8      12
cases carrying an explicit LOSS judgment         >= 10     11
LOSS levels present                          0,1,2,3,4   {0:1, 1:3, 2:3, 3:3, 4:1}
composition depth >= 2                           >= 8      16
reverse-inference cases                          >= 6       8
tier tag on every case (B0|B1|B2)                all      48/48
answerable at B0 (pure reasoning)                >= 12     23
```
Tier split: B0 = 23, B1 = 23, B2 = 2.

Realized label distributions (closed vocabularies, drawn from the same label space as Set A):
```
reverse_inference   projection-inversion 4 · mean-to-object-inversion 2 · affirming-the-consequent 2
                    conditional-inversion 0 · counterexample-refutation 0 · null 40
abstention          impossibility-of-claim 5 · impossibility-with-counterexample 4
                    report-to-verify 2 · correct-abstention 1 · null 36
```
Two reverse-inference labels went unused. No case was forced into a label to fill a slot; the
authoring session flagged the judgment call explicitly rather than leaving it silent — cases
turning on an explicit counterexample carry it as the *abstention* pattern rather than as a
reverse inference. If the frozen schema intends those to co-tag on both axes, that is a re-tagging
decision, recorded here as open rather than taken unilaterally.

## 3. Schema normalization (recorded, not silent)

The authoring session emitted a schema that diverged from Set A's frozen encoding in six fields.
Its own validation reported PASS because it validated against its own encoding — a claim checked
against itself. Independent field-by-field comparison against the committed Set A found:

```
capability_target        "axis4_loss_accounting"        -> 4                     mechanical
rubric                   {weights:{C1..C5}, anchors:{}} -> flat {C1..C5}         mechanical
                                                           anchors preserved as `rubric_anchors`
tags.loss_level          "LOSS-2" / "LOSS-NA"           -> 2 / null              mechanical
forbidden_claims         list of strings                -> single string         mechanical
tags.reverse_inference   true / false                   -> kind label / null     NOT mechanical
tags.abstention          true / false                   -> kind label / null     NOT mechanical
```

The first four were repaired mechanically. The last two were not: Set A carries *kind labels*
there, and a boolean has lost the information. Choosing a label requires knowing what the case
does, so the two fields were returned to the authoring session rather than guessed — inventing a
classification would be fabrication. Counts did not move across the repair (8 and 12).

None of this touched case semantics. It mattered because two halves of one benchmark under two
encodings are not comparable by any shared tool, which would have silently voided the per-axis
comparison the identical matrix exists to enable.

## 4. Independent verification (re-derived, not accepted)
```
A/B schema parity, all 12 top-level fields + 5 tag fields          PASS
label vocabularies are subsets of Set A's realized label space     PASS
per-axis counts == frozen matrix                                   PASS
48 / 48 / 48 lines; case_id sets identical across all three files  PASS
case_id format B002-B-<axis:02d>-<n>                               PASS
every rubric weight vector sums to exactly 100                     PASS
rubric component keys == Set A's C1..C5                            PASS
every fatal_errors entry in the closed §5 code set                 PASS
every leakage_class == LEAK-0-CLEAR                                PASS
no gold key present in prompts or in scoring metadata              PASS
keys file carries case_id + gold only; all keys non-empty          PASS
all three files valid JSONL                                        PASS
```

Textual leakage screen, 5-gram Jaccard over prompts, computed here rather than reported:
```
B vs Benchmark 001 (60 prompts)   max 0.009   mean 0.000   pairs >= 0.25 : 0
B vs Hidden Set A  (48 prompts)   max 0.022   mean 0.002   pairs >= 0.25 : 0
within B                                                   pairs >= 0.25 : 0
```
This measures **textual** overlap only. `LEAK-2` conceptual overlap is not detectable this way and
remains the responsibility of the per-case screen and the pending `LEAKAGE-AUDIT`.

## 5. Sealing
```
encryption           age v1.3.1, X25519 recipient
sealed bundle        tar.gz of B-prompts.jsonl + B-scoring-metadata.jsonl + B-keys.jsonl
plaintext digest     197909e5e0a14e7bb4881d06f374f29433a15a0a11432db1f1e494642b890f39
ciphertext digest    ee3e5d861b6406ff2499440f4586576c6b77f0deedc03f7545dbe3855c8c516d
round trip           VERIFIED before sealing — decrypt(ciphertext) reproduced the plaintext digest
committed here       ciphertext + SHA-256 manifest + this metadata. Nothing else.
plaintext location   owner custody, outside the repository
```

Working copies made during schema normalization were deleted before sealing. A second plaintext
copy of a hidden set is the exact shape of the defect this stage exists to contain.

## 6. Custody deviation (recorded, not hidden)

`SEALING` §9 requires an independent custodian to hold the decryption key. The owner directed that
the key be generated here and handed over. It was written straight to a file and never printed, so
it did not enter the generating context — but the custodian is **not** independent in the sense the
protocol intends, and this deviation is recorded for `LEAKAGE-AUDIT` rather than described as
compliance. The deviation closes when the owner moves `B-CUSTODY-IDENTITY.key` to a location only
they control.

## Ceiling
```
metadata only · no cases · no keys · no runs · no scores
zero RH progress · zero GRH progress · no secured path
```
