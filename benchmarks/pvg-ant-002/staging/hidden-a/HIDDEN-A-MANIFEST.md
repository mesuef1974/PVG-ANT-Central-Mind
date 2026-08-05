# HIDDEN-A-MANIFEST-001 (staging)

**Stage:** S1 authoring workshop of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001` — STEP A.
**Produces:** the staging manifest for `Hidden Set A` of `ADVERSARIAL-PVG-ANT-BENCHMARK-002`,
under `governance/programs/BENCHMARK-002-SEALING-PROTOCOL-001.md` (§2, §3, §8, §9),
`BENCHMARK-002-DISTRIBUTION-MATRIX-001.md`, `BENCHMARK-002-FROZEN-SCORING-RUBRIC-001.md`,
and `BENCHMARK-002-ROLE-SEPARATION-RECEIPT-001.md`.
**Status:** STAGING — Set A authored and machine-validated; concealment defect found and
contained 2026-08-05 (see §5 correction and BENCHMARK-002-HIDDEN-A-CONTAINMENT-DEFECT-001). This is **not** the sealed G1
`HIDDEN-A-MANIFEST` bundle; sealing (SHA-256-MANIFEST over the full bundle, LEAKAGE-AUDIT,
ENVIRONMENT-FREEZE-RECEIPT, BENCHMARK-002-SEALED) remains ahead. Set B is authored separately
in an isolated session and is **not** touched here.
**Ceiling:** capability measurement only — zero RH progress, zero GRH progress, no secured path.
This manifest contains **no cases' gold keys** (only their hashes) and **no B material**.

## 0. Head separation and pre-stage sync (RULE-SYNC-PER-STAGE-RECEIPTS-001)
```
S1-AUTHORING-HEAD        = 3235fd7 and beyond   (Set A authored on the moving control head)
ARM-CURRENT-FROZEN-HEAD  = 6960cb5              (S2 measures the frozen mind — never sees A keys/B)
authoring branch         = s1/hidden-a-authoring-001
pre-stage timestamp      = 2026-07-14T12:42:57Z
branch base / origin/main= 3235fd7b6b85af8ede7a21c293d5b350503eb362 (ahead/behind 0/0, tree clean)
```

## 1. Realized per-axis distribution (machine-validated; must equal the frozen matrix)
Validation is enforced by `author_hidden_a.py::validate`; the script exits non-zero on any breach.
```
#   capability axis                          A(target)  A(realized)
1   ANT correctness                              4           4
2   PVG -> ANT translation                       3           3
3   ANT -> PVG translation                       3           3
4   LOSS / non-invertibility accounting  *       5           5
5   quantifier discipline                *       5           5
6   normalization                        *       5           5
7   provenance                                   3           3
8   scope / domain-of-validity containment       3           3
9   tool selection                               3           3
10  certificate classification                  4           4
11  proof-gap detection                  *       5           5
12  overclaim refusal                    *       5           5
    -------------------------------------------------------------
    TOTAL                                       48          48
    weighted (*) axes                           25          25   (52%)
    standard axes                               23          23   (48%)
```
Invariants held: A = 48 ≥ 48; every axis ≥ 3 in A; the five failure-prone axes carry 5 each;
per-axis realized == frozen target (no ≥-floor slack used, so no distribution-change event).

## 2. Cross-cutting quotas realized (DISTRIBUTION-MATRIX §2; all minima met)
```
quota                                          floor   realized
abstention / impossibility cases                 ≥ 8       9
LOSS levels present                          0,1,2,3,4   {0,1,2,3,4}   (each ≥ 1)
cases carrying an explicit LOSS judgment         ≥ 10      10
composition depth ≥ 2                            ≥ 8        8
reverse-inference cases                          ≥ 6       10
tier tag on every case (B0|B1|B2)                all       48/48
answerable at B0 (pure reasoning)                ≥ 12      32
```
Tier split realized: B0 = 32, B1 = 15, B2 = 1 (the B2 case is the exact-π(10^13) tool-routing
task, which requires a governed external engine).

LOSS-level anchors (each level instantiated): LOSS-0 `B002-A-03-3` · LOSS-1 `B002-A-04-4`,
`B002-A-02-1` · LOSS-2 `B002-A-04-3`, `B002-A-02-3`, `B002-A-03-2` · LOSS-3 `B002-A-04-2`,
`B002-A-03-1` · LOSS-4 `B002-A-04-1`, `B002-A-04-5`.

## 3. Per-case schema (SEALING §3) — every case carries all fields
```
case_id · prompt · capability_target · expected_structure · rubric ·
fatal_errors[closed §5 codes] · partial_credit · certificate_requirements ·
forbidden_claims · source_basis · leakage_class[closed §8 value] · tags
```
`tags` = {loss_level, loss_judgment, composition_depth, reverse_inference, abstention}.
`fatal_errors` validated against the closed §5 code set; `leakage_class` against the closed §8
set; every `rubric` component-weight vector sums to 100.

## 4. Leakage screen (SEALING §8 — conceptual outranks textual)
Every case screened against: Benchmark 001; all Translation Kernel cards (Pass 001 + Pass 002);
Core Ontology objects/morphisms/witnesses; prior project examples and chats; the I_r theorem and
its pipeline; book-ledger units; near formulations.
```
result: 48/48 = LEAK-0-CLEAR (eligible). 0 rejected, 0 quarantined.
```
Screening notes: the residue→character and principal-subtraction motifs of Benchmark 001 (e.g.
`B001-RE-01/02/03`) were deliberately avoided; the axis-2 residue-style case was replaced with an
additive-energy / L4 exponential-sum construction to remove conceptual overlap (`LEAK-2`). All
scenarios are classical source-grounded ANT (Mertens, PNT/PNT-in-AP, divisor problem,
Selberg-Delange, explicit formula, Bombieri-Vinogradov, Helfgott) or elementary
arithmetic-function projections, freshly framed — none reproduces a project card. The full
`LEAKAGE-AUDIT` G1 artifact will aggregate this per-case screen across A and B.

## 5. Role separation realized (ROLE-SEPARATION §2, §4)
```
R1/R2 (this session) authored A prompts, expected_structure, rubric fields, tags, and gold keys
       on the control head — a session that is NEVER an answering (R3) context.
gold keys (R2)  →  A-keys.jsonl  : OWNER-HELD, .gitignored, never in R3 context.
       CORRECTION 2026-08-05: the key FILE was never committed, but the generator that
       deterministically re-emits it WAS. The keys were therefore disclosed as generator
       source from 3235fd7 to 3133c80. See BENCHMARK-002-HIDDEN-A-CONTAINMENT-DEFECT-001.
key-hashes      →  HIDDEN-A-KEY-HASHES.txt : committed BEFORE any scoring run (§9, §4.4).
R3 (ARM-CURRENT 6960cb5) will receive PROMPTS ONLY at S2; never expected_structure, never keys.
R4 receives the frozen rubric + prompts + frozen responses + keys + metadata only POST-freeze.
B: not present in this session in any form (authored later in isolation; only ciphertext+SHA-256
   will reach main).
```

## 6. File inventory (this staging directory)
```
author_hidden_a.py          WITHDRAWN 2026-08-05 to owner custody outside the repository:
                            it carried all 48 gold keys as plaintext literals (remedy R2)
A-prompts.jsonl             R3-facing: case_id · capability_target · tier · prompt · leakage_class
A-scoring-metadata.jsonl    R4-facing: full schema MINUS gold key
A-keys.jsonl                R2 gold keys — OWNER-HELD, gitignored (file never committed;
                            but see the correction in §5 — the generator was)
HIDDEN-A-KEY-HASHES.txt     SHA-256 per case + aggregate (committed)
HIDDEN-A-MANIFEST.md        this manifest (committed; no keys)
.gitignore                  excludes A-keys.jsonl
```
```
AGGREGATE A key hash (SHA-256 over per-case case_id:hash lines):
1987512d402007909b840bbc80bddfc33cee2ba1ae8aa69b6ceca945b1f88fd6
```
Regeneration from the generator is deterministic, so the committed hashes bind the exact keys held
in owner custody. That same determinism is what made committing the generator a disclosure rather
than a convenience: the aggregate above was re-derived from the tracked tree alone on 2026-08-05
and matched exactly. A hash over re-derivable keys is a fixity commitment, not concealment.
The generator now lives in owner custody and regeneration is no longer possible from this tree.

## 7. What remains before G1 (BENCHMARK-002-SEALED)
```
[done]  STEP A: author A (48), machine-validate invariants, commit A key-hashes  ← here
[next]  STEP B: author B (48) in an isolated session → offline-encrypt prompts+keys
                → commit ciphertext + SHA-256 only (HIDDEN-B-CIPHERTEXT)
[next]  LEAKAGE-AUDIT over A and B
[next]  6–10 calibration cases outside the score (FROZEN-SCORING-RUBRIC §6)
[next]  ENVIRONMENT-FREEZE-RECEIPT (13 explicit fields; answering manifest excludes A keys and B)
[next]  SHA-256-MANIFEST over the sealed bundle → BENCHMARK-002-SEALED
```
No ARM-CURRENT run occurs during authoring. No transition to S2 until every G1 item exists.

## Ceiling
```
staging manifest only · no gold keys · no B material · no runs · no scores
zero RH progress · zero GRH progress · no secured path
```
