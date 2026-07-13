# BENCHMARK-002-AUTHORING-WORKSHOP-RECEIPT-001

**Stage:** S1 authoring workshop of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001`.
**Opens:** the case-authoring workshop for `ADVERSARIAL-PVG-ANT-BENCHMARK-002`, under
`BENCHMARK-002-SEALING-PROTOCOL-001.md` (governed on main at `5a02032`) and the registered
spec. This receipt records that the workshop's preconditions are met; it does NOT contain
cases or keys, and no case or key has been authored yet. Capability measurement only —
zero RH progress, zero GRH progress.

## 1. Pre-stage sync receipt (RULE-SYNC-PER-STAGE-RECEIPTS-001)
```
timestamp:    2026-07-13T18:47:08Z
branch:       s1/benchmark-002-authoring-workshop-001
branch base:  5a02032acd9fdfb00baf1d85f69a75fff4b1436d  (from synced main, PR #38 merged)
origin/main:  5a02032acd9fdfb00baf1d85f69a75fff4b1436d
ahead/behind: 0 / 0        tracked tree: clean
```

## 2. Workshop preconditions (all met at open)
```
sealing protocol governed on main        BENCHMARK-002-SEALING-PROTOCOL-001  (PR #38, merged)
roles fixed                              BENCHMARK-002-ROLE-SEPARATION-RECEIPT-001
distribution locked                      BENCHMARK-002-DISTRIBUTION-MATRIX-001 (A 48 / B 48)
rubric frozen (before authoring)         BENCHMARK-002-FROZEN-SCORING-RUBRIC-001
head separation in force                 author 5a02032+  ·  measure frozen 6960cb5
```

## 3. Leakage-screen basis (enumerated now, applied per case — sealed §8)
Every case, in A and B, is screened (conceptual outranks textual) against:
```
Benchmark 001 · all Translation Kernel cards (Pass 001 + Pass 002) · Core Ontology
objects/morphisms/witnesses · prior project examples and chats · the I_r theorem and its
pipeline · book-ledger units · near formulations
```
Result recorded per case as `leakage_class` from the closed set
`LEAK-0-CLEAR | LEAK-1-TEXTUAL-OVERLAP | LEAK-2-CONCEPTUAL-OVERLAP |
LEAK-3-NEAR-FORMULATION-OR-PROJECT-DERIVED | LEAK-U-UNCERTAIN`. Reject on 1/2/3; quarantine on
U pending independent review; only LEAK-0 is eligible. Aggregated into `LEAKAGE-AUDIT` (G1).

## 4. A/B authoring plan (separation-safe — the next step, not this receipt)
```
STEP A  Author Hidden A ≥ 48 on the control head, per the distribution matrix and per-case
        schema (case_id · prompt · capability_target · expected_structure · rubric ·
        fatal_errors[§5 codes] · partial_credit · certificate_requirements · forbidden_claims ·
        source_basis · leakage_class[§8 codes]). Run the leakage screen on every case.
        Author A gold keys (R2), verify, and commit A key-HASHES before any scoring run.
STEP B  Author Hidden B ≥ 48 in an ISOLATED session (never a context that may act as R3).
        The current control-head session does NOT hold B. Encrypt B prompts AND keys offline;
        commit ONLY the ciphertext + a SHA-256 manifest. The B decryption key is owner-held
        (R5), offline.
SCREEN  Produce LEAKAGE-AUDIT over A and B.
CALIB   Author 6–10 calibration cases OUTSIDE the score (frozen-rubric §6).
```
No ARM-CURRENT run occurs during authoring. Answering (S2) is a separate, later, authorized
stage against the frozen `6960cb5`.

## 5. Path to G1 (BENCHMARK-002-SEALED)
```
this workshop receipt (roles · matrix · rubric)            ← here
→ author A (+ A key-hashes committed)
→ author B in isolation → offline-encrypt → ciphertext + SHA-256 to main
→ LEAKAGE-AUDIT
→ ENVIRONMENT-FREEZE-RECEIPT (13 explicit fields; answering manifest excludes A keys and B)
→ SHA-256-MANIFEST over the sealed bundle
→ BENCHMARK-002-SEALED  ⇒  G1 passed
```
G1 requires all eight sealed artifacts (`BENCHMARK-002-SEALED · HIDDEN-A-MANIFEST ·
HIDDEN-B-CIPHERTEXT · FROZEN-SCORING-RUBRIC · ROLE-SEPARATION-RECEIPT · LEAKAGE-AUDIT ·
ENVIRONMENT-FREEZE-RECEIPT · SHA-256-MANIFEST`) plus the S1 post-stage sync receipt. No
transition to S2 until every item exists. No run on ARM-CURRENT before G1 closes.

## 6. State at workshop open
```
S1 = OPEN · workshop = OPEN · cases authored = 0 · keys authored = 0
Benchmark 002 = NOT SEALED · G1 = NOT PASSED · S2 = NOT AUTHORIZED
ARM-CURRENT-FROZEN-HEAD = 6960cb5 · corpus/training = PROHIBITED
```

## Ceiling
```
workshop opening only · no cases · no keys · no runs · no scores
zero RH progress · zero GRH progress · no secured path
```
