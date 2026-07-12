# Appendix B — Adversarial Benchmark 002 Protocol

The full normative specification lives at
`governance/programs/ADVERSARIAL-PVG-ANT-BENCHMARK-002.md`; this appendix
summarizes it for reviewers.

- **Two hidden sets.** Set A (≥ 48 new cases) is the development set; Set B
  (≥ 48 independent cases) is the generalization set, with prompts AND keys
  encrypted offline under an independent custodian — only ciphertext and a
  SHA-256 manifest are committed. A hash alone is not treated as
  concealment.
- **Role separation.** Case author, key author/verifier, answering agent,
  and scoring agent are distinct roles; the case author is never the sole
  scorer.
- **Frozen execution.** Model and version, system prompt, context, tools,
  randomness, attempt counts, and environment are frozen before any run.
- **Access tiers and arms.** B0 reasoning-only / B1 repository retrieval /
  B2 full governed tools; four primary comparison arms, including full mind
  vs ANT-only-without-PVG — the direct PVG-materiality measurement.
- **Rubric.** Frozen before authoring completes: partial credit,
  hypothesis correctness, tool selection, composition correctness,
  over-claim penalty, correct-abstention reward, the ignorance-vs-
  impossibility distinction, reverse-inference validity, LOSS accounting,
  PVG materiality. Calibration cases sit outside the final score.
- **Leakage.** Every case is screened conceptually (not just textually)
  against Benchmark 001, all translation cards, the core ontology, prior
  project examples, the I_r pipeline, book-ledger units, and near
  formulations.
- **Binding sequence.** Raw baseline on A → immutable freeze → keys opened
  → error map → composer tool → contaminated A rerun → ablation → targeted
  learning → **one single run of B**, which is the only generalization
  measurement. The A rerun is never generalization evidence.
- **Reporting.** Uncertainty intervals (no fake decimal precision), broken
  down by domain, LOSS level, composition depth, reverse-inference type,
  abstention correctness, tool tier, and arm.

Status at packet time: specification registered; NOT_STARTED; no cases, no
keys, no runs.

```text
capability measurement only · zero RH progress · zero GRH progress
```

**Classification:** Evaluation-protocol appendix. No mathematical claim.
