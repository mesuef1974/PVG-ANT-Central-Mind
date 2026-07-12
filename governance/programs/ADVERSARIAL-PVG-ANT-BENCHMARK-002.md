# ADVERSARIAL-PVG-ANT-BENCHMARK-002 — Protocol Specification

```text
kind                    = evaluation_program
parent                  = PVG-ANT-CENTRAL-MIND-MATURATION-002
research_front          = none
scientific_claim_ceiling = capability measurement only
status                  = NOT_STARTED (this document is specification only)
```

This is NOT a second operational research goal. It measures capability; it
creates no theorem, lemma, originality, or L3 promotion. This PR contains no
cases, no keys, no runs.

## 1. Hidden sets

1. `Hidden Set A` ≥ 48 new cases — the development set.
2. `Hidden Set B` ≥ 48 new independent cases — the generalization set.
3. Total ≥ 96. A and B are authored in the same workshop, under the same
   rubric, leakage screen, and topical distribution.
4. Set B custody: prompts AND keys encrypted offline; an independent
   custodian holds the decryption key; only ciphertext and a SHA-256
   manifest are committed to protected main. A hash alone is NOT sufficient
   concealment for B. The answering agent never sees B prompts or keys
   during development.
5. Set A keys: held outside the answering process; key hashes committed
   before any scoring run.

## 2. Role separation (even if executed by different agents)

```text
case author | key author/verifier | answering agent | scoring agent
```

The case author is never the sole scorer. The scoring agent receives only
the frozen rubric and the keys.

## 3. Frozen execution configuration (before any run)

Model and version; system prompt; conversation context and memory; allowed
tools; randomness settings or seed where possible; attempt/repetition
counts; run date and environment. Any change = a new named run, never an
overwrite.

## 4. Access tiers and comparison arms

Tiers: `B0` reasoning only · `B1` repository retrieval allowed · `B2` full
governed tool use.

Primary arms (all others are exploratory, not headline estimates):

1. Full PVG–ANT / B0 vs Full PVG–ANT / B2;
2. Full PVG–ANT / B2 vs ANT-only (cards/tools without PVG ontology) / B2;
3. Full PVG–ANT / B2 vs PVG-vocabulary-only (no ANT routing) / B2;
4. Full PVG–ANT / B2 vs retrieval-only baseline.

Arm 2 is the PVG-materiality measurement: whether PVG adds anything beyond
well-organized ANT.

## 5. Frozen rubric (before authoring completes)

Partial credit; hypothesis correctness; tool selection; composition
correctness; over-claim penalty; correct-abstention reward; the distinction
between "I do not know" and "the inference is impossible" (impossibility
requires a counterexample or a named missing certificate); reverse-inference
validity; LOSS-level accounting; PVG-materiality scoring.

## 6. Calibration

6–10 calibration cases outside the final score verify that scorers apply the
rubric identically before real scoring begins.

## 7. Leakage screen (conceptual, not only textual)

Every case is checked against: Benchmark 001; all Translation Kernel cards;
Core Ontology objects/morphisms/witnesses; prior project examples and chats;
the I_r theorem and its pipeline; book-ledger units; linguistically or
conceptually near formulations. Conceptual leakage outranks textual overlap.

## 8. Binding sequence (immutable order)

```text
raw hidden baseline on A
→ immutable raw-score freeze
→ open A keys
→ immutable error map
→ morphism composer
→ rerun A, labeled contaminated/development
→ ablation arms
→ targeted learning from named failure clusters
→ ONE single run of B — the only generalization measurement
```

The A rerun is NEVER evidence of generalization. Only the single B run is.

## 9. Reporting

Uncertainty intervals (n≈48 per set: report intervals, never decimals that
fake precision); score by domain; by LOSS level; by composition depth; by
reverse-inference type; correct vs incorrect abstention; by tool tier; by
ablation arm.

## 10. Prohibitions inside this program

No new translation cards before the raw A error map; no Pass 003; no
targeted learning before the error map; no gold answers in the answering
process; no modification of Benchmark 001; no L3 promotion from benchmark
success; no maturation receipt before the raw A baseline exists.

## Ceiling

```text
capability measurement only
zero RH progress
zero GRH progress
no secured path
```

**Classification:** Governance / Evaluation-program specification. No mathematical claim.
