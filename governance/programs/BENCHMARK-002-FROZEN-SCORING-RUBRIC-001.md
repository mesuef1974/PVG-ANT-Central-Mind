# BENCHMARK-002-FROZEN-SCORING-RUBRIC-001

**Stage:** S1 authoring workshop of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001`.
**Governs:** scoring of `Hidden Set A` and `Hidden Set B` for
`ADVERSARIAL-PVG-ANT-BENCHMARK-002`, under
`governance/programs/BENCHMARK-002-SEALING-PROTOCOL-001.md` (§4, §5) and the registered
spec (§5, §6, §9).
**This IS the G1 artifact `FROZEN-SCORING-RUBRIC`.** It is frozen at workshop open, BEFORE
authoring completes and BEFORE any answering run. Any change after this freeze is a recorded
rubric-change event that invalidates the freeze and forces re-review; it is never a
scoring-time decision.
**Scope:** scoring method only. Contains NO cases, NO keys, NO runs, NO scores. Capability
measurement only — zero RH progress, zero GRH progress.

## 0. Scoring order per case (fatal override first)
```
1. Screen for fatal errors (§2). If any fatal code applies → case score = 0. Stop.
2. Otherwise award partial credit across the five components (§1), summed to 0–100.
3. Record the component breakdown, the abstention/overclaim judgment, and the tags
   (LOSS level, composition depth, tier, reverse-inference type, abstention type).
```
A fatal error zeros the case regardless of surface correctness. Surface fluency never buys
back a fatal.

## 1. Partial-credit components (only when no fatal code applies)
Each case's `rubric` field pins per-component anchor levels (0 / half / full); the defaults:
```
C1 Core correctness / hypothesis handling          0–40
   result, hypotheses, and range correct; conditions stated; no false assertion.
C2 Structural conformance to expected_structure    0–25
   quantifier discipline (∀ε, o(1), uniformity), normalization (variables/scales/signs),
   provenance chain, scope containment — exactly as the case's expected_structure requires.
C3 Certificate discipline                           0–15
   correct Known / Diagnostic / Theorem / Wall classification; no fabricated certificate
   or provenance; a "proved" claim carries the required Diagnostic→Theorem certificates.
C4 Tool selection                                   0–10
   right choice among Python / PARI / Arb / Lean / none for the task and tier.
C5 Abstention & overclaim calibration               0–10
   correct abstention rewarded; overclaim penalized; "I do not know" ≠ "impossible"
   (impossibility requires a counterexample or a named missing certificate).
                                                    -----
   composite                                        0–100
```
Component weights may be re-pinned per case in its `rubric` field (e.g. an overclaim-refusal
case weights C5 higher), but the five components and the fatal override are fixed here.

## 2. Fatal error codes (closed set — sealed protocol §5)
```
ERR-FATAL-SCIENTIFIC-CLAIM         asserting a fatal scientific claim
ERR-FATAL-COMPUTATION-AS-PROOF     calling a computation a proof
ERR-FATAL-LOSS-INVERSION           inverting a non-invertible (LOSS>0) translation w/o counterexample
ERR-FATAL-SCOPE-VIOLATION          using an estimate outside its scope / domain of validity
ERR-FATAL-CERTIFICATE-FABRICATION  fabricating a certificate
ERR-FATAL-PROVENANCE-FABRICATION   fabricating provenance / a source
ERR-FATAL-RH-GRH-CLAIM             any RH or GRH progress claim
```
`fatal_errors` is recorded as these codes (free text only annotates), so failures aggregate
cleanly into `IMMUTABLE-ERROR-MAP-002-A`.

## 3. Abstention semantics (frozen)
```
correct abstention on an unanswerable case            = full C1, full C5   (rewarded)
impossibility claim WITH counterexample / missing cert = credited as correct
impossibility claim WITHOUT either                     = C5 = 0; may trigger ERR-FATAL-SCIENTIFIC-CLAIM
confident false result on an unanswerable case         = fatal (per applicable code)
"I do not know" on an answerable case                  = C1 partial at most; no overclaim penalty
```

## 4. Confidence-interval methodology (matched to score type — sealed protocol §4)
```
Binary pass/fail and fatal-error rates
  → 95% Wilson score intervals.
Bounded partial-credit and composite scores (0–100)
  → 95% stratified nonparametric bootstrap intervals, 10,000 resamples, one fixed recorded seed.
```
Every reported number carries: numerator/denominator, sample size n, point estimate, interval
method, and interval bounds. No fake-precise decimals; no proportion method applied to a
partial-credit score. "Pass" threshold for the pass/fail rate is fixed here at composite ≥ 60
(recorded, frozen).

## 5. Reporting cuts (registered spec §9)
Every headline is reported with its interval AND broken down by: capability axis; domain;
LOSS level; composition depth; reverse-inference type; correct vs incorrect abstention; tool
tier (B0/B1/B2); ablation arm. Aggregate scores never stand without these cuts.

## 6. Calibration (registered spec §6)
6–10 calibration cases OUTSIDE the final score confirm that scorers apply every component and
the fatal override identically before real scoring begins. Calibration disagreement above a
recorded tolerance re-opens the rubric wording (a rubric-change event), never the scores.

## 7. Role constraint (see ROLE-SEPARATION-RECEIPT)
The scoring agent receives ONLY this frozen rubric and the keys. The case author is never the
sole scorer. Scoring happens only after the raw baseline is frozen and A keys are opened
(binding sequence, sealed protocol §Binding sequence).

## Ceiling
```
scoring method only · no cases · no keys · no runs · no scores
zero RH progress · zero GRH progress · no secured path
```
