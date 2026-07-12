# Continuous Central-Mind Maturation Policy

**Policy ID:** `POLICY-CONTINUOUS-MATURATION-001`  
**Status:** governing  
**Classification:** Governance / Capability Maturation

## 1. Governing principle

The Central Mind must become more capable after every closed stage, not merely larger.

The governing rule is `RULE-STAGE-MATURATION-RECEIPT-001`:

> No stage is closed as maturation unless it records a tested capability delta, the knowledge and language returned to the mind, the failures preserved, the synchronization evidence, and the unchanged scientific ceiling.

A new file, card, book unit, experiment, or proof attempt is not by itself maturation.

## 2. Required maturation dimensions

Every stage receipt records before/after values for these dimensions:

```text
K — operational knowledge
L — shared PVG–ANT language
R — reasoning/composition capability
C — certificate and wall discipline
F — reusable failure/negative memory
V — verification and reproducibility
S — repository/state synchronization
```

A stage may improve one dimension while leaving others unchanged. It may not claim improvement without a named test or reusable artifact.

## 3. Maturation receipt

Every completed capability or governance stage must append one row to `registries/maturation-events.jsonl` and fill the template `governance/templates/maturation-receipt.md` when the stage is substantial.

Minimum machine fields:

```text
id
stage_id
status
capability_before
capability_after
knowledge_delta
language_delta
reasoning_delta
certificate_delta
failure_memory_delta
verification
sync_evidence
claim_ceiling
classification
source
```

The latest receipt must be named in the four live truth layers:

- `README.md`;
- `maps/current-capabilities.md`;
- `transition-memory/latest-state.md`;
- `transition-memory/next-action.md`.

## 4. What counts as a real capability delta

Accepted examples:

- a new exact bidirectional translation with explicit recovery conditions;
- a new admissible morphism composition tested on held-out cases;
- a sharper information-loss classification with counterexamples;
- a new routing rule that selects the correct ANT tool under stated hypotheses;
- a negative certificate that blocks a repeated dead end;
- a reproducible proof or experiment pattern that survives independent checks;
- a governance guard that catches a previously silent contradiction.

Not accepted:

- more files without a new tested function;
- restating a known theorem;
- renaming a concept;
- a higher benchmark score on a contaminated set;
- closing a unit without returning its knowledge;
- claiming maturity from book count, token count, or registry size.

## 5. Stage input and output contract

### Before execution

A stage freezes:

```text
input state and canonical SHA
named task
readiness result
knowledge gaps
current language coverage
claim ceiling
success and failure criteria
```

### After execution

A stage returns:

```text
new operational knowledge
new or corrected common-language structures
tested reasoning delta
loss/certificate updates
negative memory
verification evidence
canonical synchronization evidence
next higher ceiling
```

## 6. Knowledge is load-bearing

Knowledge is indispensable, but indiscriminate accumulation is not maturity.

The task-triggered policy remains active: acquire the minimum trusted knowledge needed for the active task, then return it in reusable form. A stage that discovers a knowledge gap must classify it as:

```text
operationally_ready
known_but_needs_activation
source_available_not_extracted
missing
```

The stage may not hide a state-B/C/D prerequisite behind an analogy or an existing card title.

## 7. Benchmark separation

For `ADVERSARIAL-PVG-ANT-BENCHMARK-002`:

1. the raw hidden baseline comes before new translation cards;
2. the immutable error map identifies actual knowledge, language, and composition gaps;
3. targeted learning is authorized only from those failure clusters;
4. the same hidden set is rerun only with contamination and ablation accounting;
5. benchmark success cannot promote an L3 theorem or originality claim.

The continuity layer therefore installs the learning cycle without teaching to Benchmark 002 before its baseline.

## 8. Ceiling escalation

The existing maturity ladder remains governing. A stage receipt must distinguish:

- capacity added;
- capability tested;
- mechanism repeated;
- theorem-level progress.

Only the last category can raise a scientific claim ceiling, and only with its required proof and external certificates.

## 9. Closure rule

A stage cannot be called `checkpoint_pass`, `closed`, or `installed` in a live truth layer unless:

- a maturation event exists for its stage ID;
- all required fields are non-empty;
- verification is named;
- knowledge/language/failure deltas are explicit, including `none` when genuinely unchanged;
- the claim ceiling is preserved;
- repository synchronization evidence is recorded.

## 10. Scientific ceiling

Continuous maturation improves the research instrument. It does not by itself certify originality, prove a theorem, establish publication readiness, or create RH/GRH progress.
