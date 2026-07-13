# BENCHMARK-002-SEALING-PROTOCOL-001

**Stage:** S1 (open 2026-07-13) of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001`.
**Operationalizes:** `governance/programs/ADVERSARIAL-PVG-ANT-BENCHMARK-002.md` (the registered
spec). This document is the execution-ready expansion of that spec — one benchmark, not two.
Where the two differ, the registered spec governs; this document only pins concrete decisions
it left at policy level.
**Classification:** Governance / evaluation-program sealing protocol. Capability measurement
only — no theorem, no originality, no L3 promotion. Zero RH progress, zero GRH progress.
**Scope of this artifact:** the SEALING PROTOCOL only. It contains **no cases, no keys, no
runs, no scores**. Case authoring is the next S1 step, under this protocol.

## Pre-stage sync receipt (RULE-SYNC-PER-STAGE-RECEIPTS-001)
```
timestamp:   2026-07-13T17:34:47Z
branch base: 0836355661dc4b04a4d4451cc11f8f521c8fbd8b (from synced main)
origin/main: 0836355661dc4b04a4d4451cc11f8f521c8fbd8b
ahead/behind: 0/0   tracked tree: clean
```

## 0. The head separation (non-negotiable)
```
S1-AUTHORING-HEAD     = 0836355 and beyond  (we AUTHOR A/B on the moving control head)
ARM-CURRENT-FROZEN-HEAD = 6960cb5           (S2 MEASURES the frozen mind at 6960cb5)
```
S2 runs the mind frozen at 6960cb5 — **not** the mind that authored or saw the S1 files.
**A/B prompts AND keys must never enter the ARM-CURRENT answering context.** This is the
single defect that would invalidate the entire benchmark.

## 1. Capability scope (what B-002 measures)
Adversarial coverage of the PVG–ANT operating capabilities, not general math trivia. Twelve
axes (each a `capability_target`):
1. ANT correctness (results/hypotheses/range)
2. PVG → ANT translation
3. ANT → PVG translation
4. LOSS / non-invertibility accounting
5. quantifier discipline (∀ε, o(1), uniformity)
6. normalization (variables/scales/signs consistent)
7. provenance (result ↔ source ↔ dependencies traceable)
8. scope / domain-of-validity containment
9. tool selection (when Python/PARI/Arb/Lean/none)
10. certificate classification (Known/Diagnostic/Theorem/Wall/…)
11. proof-gap detection
12. overclaim refusal (correct abstention vs impossibility-with-counterexample)

## 2. Case-distribution matrix (adversarial, not 96 generic questions)
- `Hidden Set A` ≥ 48, `Hidden Set B` ≥ 48, total ≥ 96; authored in the same workshop, same
  rubric, same leakage screen, same distribution.
- Cases are distributed **across the twelve axes**, not massed on easy ones; each axis carries
  both A and B cases so B is a true independent generalization set, not a topic B never saw.
- Adversarial weighting toward the axes the autopsies flagged as most failure-prone
  (quantifier discipline, normalization, LOSS, overclaim refusal, proof-gap detection).
- Distribution counts per axis × set are fixed in the workshop and frozen with the rubric; the
  final matrix is recorded in `HIDDEN-A-MANIFEST` / `HIDDEN-B-CIPHERTEXT` metadata.

## 3. Per-case field schema (every case)
```
case_id · prompt · capability_target · expected_structure · rubric ·
fatal_errors · partial_credit · certificate_requirements · forbidden_claims ·
source_basis · leakage_class
```
`expected_structure` is the shape a correct answer must have (not a leaked gold string in the
prompt). `certificate_requirements` states which of the five Diagnostic→Theorem certificates a
"proved" answer would need. `source_basis` records provenance for the leakage screen.
`fatal_errors` draws only from the closed §5 code vocabulary; `leakage_class` draws only from
the closed §8 vocabulary.

## 4. Frozen scoring rubric (frozen BEFORE authoring completes)
Partial credit; hypothesis correctness; tool selection; composition correctness; over-claim
penalty; correct-abstention reward; the distinction between "I do not know" and "the inference
is impossible" (impossibility requires a counterexample or a named missing certificate);
reverse-inference validity; LOSS-level accounting; PVG-materiality scoring. 6–10 calibration
cases (outside the final score) confirm scorers apply the rubric identically before real
scoring.

### Confidence-interval methodology (matched to score type)
No single blanket method: the interval must match the kind of score, because partial credit is
not a binomial proportion.
```
Binary pass/fail and fatal-error rates
  → 95% Wilson score intervals.
Bounded partial-credit and composite scores
  → 95% stratified nonparametric bootstrap intervals, 10,000 resamples, one fixed recorded seed.
```
Every reported number carries: numerator/denominator, sample size n, point estimate, interval
method, and interval bounds. No fake-precise decimals; no proportion method applied to a
partial-credit score.

## 5. Error taxonomy (fatal vs partial)
`fatal_errors` is a **closed set of standardized codes** (a free-text note may annotate a code
but never replaces it), so failures aggregate cleanly into `IMMUTABLE-ERROR-MAP-002-A`:
```
ERR-FATAL-SCIENTIFIC-CLAIM         asserting a fatal scientific claim
ERR-FATAL-COMPUTATION-AS-PROOF     calling a computation a proof
ERR-FATAL-LOSS-INVERSION           inverting a non-invertible (LOSS>0) translation w/o counterexample
ERR-FATAL-SCOPE-VIOLATION          using an estimate outside its scope / domain of validity
ERR-FATAL-CERTIFICATE-FABRICATION  fabricating a certificate
ERR-FATAL-PROVENANCE-FABRICATION   fabricating provenance / a source
ERR-FATAL-RH-GRH-CLAIM             any RH or GRH progress claim
```
Any fatal code zeros the case regardless of surface correctness. The list is frozen with the
rubric; adding a code is a rubric change, never a scoring-time decision.

## 6. Abstention & overclaim policy
Correct abstention is rewarded. "I don't know" ≠ "impossible": an impossibility claim must
carry a counterexample or a named missing certificate. Any originality/publication/RH/GRH
claim is a fatal overclaim.

## 7. Role separation (registered §2)
```
case author | key author/verifier | answering agent | scoring agent | B custodian
```
The case author is never the sole scorer. The scoring agent receives only the frozen rubric
and the keys. The B custodian holds the B decryption key and is distinct from the answering
agent. Recorded in `ROLE-SEPARATION-RECEIPT`.

## 8. Leakage policy (conceptual outranks textual)
Every case is screened against: Benchmark 001; all Translation Kernel cards; Core Ontology
objects/morphisms/witnesses; prior project examples and chats; the I_r theorem and its
pipeline; book-ledger units; near formulations. `leakage_class` is a **closed list with a fixed
decision per value** — the screener is never forced to declare "clean" under doubt:
```
LEAK-0-CLEAR                                eligible
LEAK-1-TEXTUAL-OVERLAP                      reject
LEAK-2-CONCEPTUAL-OVERLAP                   reject
LEAK-3-NEAR-FORMULATION-OR-PROJECT-DERIVED  reject
LEAK-U-UNCERTAIN                            quarantine pending independent review
```
Conceptual leakage (`LEAK-2`) disqualifies a case even at zero textual overlap; uncertainty
(`LEAK-U`) quarantines rather than admits. Recorded in `LEAKAGE-AUDIT`.

## 9. Set-B concealment
Both B **prompts and keys** are encrypted offline; only the ciphertext + a SHA-256 manifest
are committed. An independent custodian holds the decryption key. A hash alone is NOT
concealment. Set-A keys are held outside the answering process; A key-hashes are committed
before any scoring run. The answering agent never sees B during development.

## 10. Frozen execution environment (recorded before any S2 run)
ARM-CURRENT = the mind frozen at 6960cb5. The `ENVIRONMENT-FREEZE-RECEIPT` records every field
below **explicitly**; a change in any single one produces a NEW named run and never overwrites a
prior baseline:
```
model / provider / version
system prompt hash
memory / context manifest
context-window limit
allowed tools and tool versions   (tier B0 reasoning · B1 +repo retrieval · B2 +full governed tools)
temperature
top_p
max_tokens
seed (where supported)
stop sequences
timeout policy
attempt and repetition counts
date and execution environment
```
Recorded in `ENVIRONMENT-FREEZE-RECEIPT`.

## Binding sequence (immutable; registered §8)
```
raw hidden baseline on A → immutable raw-score freeze → open A keys → immutable error map
→ morphism composer → rerun A (labeled contaminated/development) → ablation arms
→ targeted learning from named failure clusters → ONE single run of B (the only generalization measure)
```
The A rerun is NEVER evidence of generalization; only the single B run is.

## S1 exit (G1) — all required before S2
```
BENCHMARK-002-SEALED · HIDDEN-A-MANIFEST · HIDDEN-B-CIPHERTEXT · FROZEN-SCORING-RUBRIC
ROLE-SEPARATION-RECEIPT · LEAKAGE-AUDIT · ENVIRONMENT-FREEZE-RECEIPT · SHA-256-MANIFEST
```
Plus the S1 Post-stage sync receipt. No transition to S2 until every item exists.

## Prohibitions (registered §10 + program)
No new translation cards before the raw-A error map; no Pass 003; no targeted learning before
the error map; no gold answers in the answering process; no modification of Benchmark 001; no
L3 promotion from benchmark success; no maturation receipt before the raw-A baseline exists;
no corpus/training before CURRENT-MIND-RAW-BASELINE-001 + IMMUTABLE-ERROR-MAP-002-A.

## Ceiling
```
capability measurement only · zero RH progress · zero GRH progress · no secured path
```
