# Governance Enforcement Closure 001

**ID:** GOVERNANCE-ENFORCEMENT-CLOSURE-001  
**Date:** 2026-07-12  
**Scope:** repair the failing core guards, wire all guards into a mandatory CI
merge gate, unify declared state with registry truth, and close
PVG-UNDERSTANDING-DEEPENING-001.  
**Authorization:** user decision of 2026-07-12 adopting the two-track plan
(external P8 verification preparation in parallel; no sending without explicit
authorization; this closure as the first internal package).

## 1. Verdict

`PASS — all required CI jobs green from clean GitHub Actions checkouts; ontology checkpoint closed and frozen.`

## 2. Finding classification

Rule applied: every alarm classified as **repository defect** | **guard
defect** | **documented historical exception** before any fix. No broad
whitelists, no loosening of honesty rules, no silencing.

| # | Guard | Finding | Class | Action |
|---|---|---|---|---|
| 1 | honesty_audit | 11 × `external-research-assets.jsonl` missing `classification` | guard defect (vocabulary gap) | `external_research_asset` documented as a status kind in `governance/classification-system.md`; `STATUS_KINDS` extended accordingly. Entries already carry lifecycle `status`. |
| 2 | honesty_audit | 6 × `negative-results.jsonl` non-canonical classification strings | repository defect | entries restamped with canonical classifications (`Known`/`Diagnostic`); original wording preserved verbatim in `classification_note`. |
| 3 | honesty_audit | 8 × `pvg-ant-bridges.jsonl` missing `kind`, 8 × non-canonical classification | repository defect | `kind: bridge` added; canonical stamps (`Identity`/`Known`) applied; original wording preserved in `classification_note`; `bridge` added to the classification-kind list. |
| 4 | honesty_audit | `P8_OUTREACH_PROTOCOL.md:78` flagged “breakthrough” | repository defect (line lacked inline negation context) | every bullet of the Do-not-use list now carries an explicit `(forbidden)` marker; no guard exemption added. |
| 5 | registry_sync_audit | 3 × `WALL-001` unknown id | guard defect (false positive) | tokenizer captured the trailing `WALL-001` piece of longer identifiers as a standalone id; fixed with a negative lookbehind. No registry entry was missing. |
| 6 | no_pdf_audit | `Books_others/` reported “not ignored” | guard defect (false positive) | `.gitignore` was already correct; the probe now uses the path-pattern form `Books_others/`. Exit code `1` means not ignored, while fatal git errors are reported separately and fail the guard. Source policy is unchanged. |
| 7 | state_coherence_audit | latest-state pinned to the v0.6/Montgomery era | guard defect (era-pinned) | replaced by registry-derived checks: every active `GOAL-OP-*` goal must appear in README, current-capabilities, latest-state, and next-action. |
| 8 | state_coherence_audit | next-action accepted only an old fixed phrase set | guard defect (era-pinned) | replaced by the same live-registry contract. Malformed or non-object JSON in `program-goals.jsonl` now fails the guard instead of being skipped. |
| 9 | state_coherence_audit | empty `planned.jsonl` not reflected in next-action | repository defect | next-action now records `planned.jsonl = empty`. |
| 10 | state_coherence_audit | capability map missing bounded-gaps tool and v0.6-e closure | repository defect (ontology rewrite dropped substrate truth) | installed book-layer substrate paragraph restored, including the live bounded-gaps diagnostic and closure-reviewed units. |
| 11 | state_coherence_audit | next-action missing quarantine markers | repository defect | Montgomery A/B/legacy-E quarantine remains explicit and in force. |
| 12 | state_coherence_audit | README missing source-grounding-corrected story and v0.6-E Closure Review pointer | repository defect | README now tells the corrected Montgomery story and points to both closure-review tracks. |
| 13 | local session inspection | untracked `formal/lean/audit/LeanP3Pass009Discovery.lean` | repository defect (unauthorized draft) | removed from the inspected checkout; remote `origin/main` did not track the path. The CI repository-policy job rejects future inclusion unless separately authorized. |
| 14 | state review | root README strategic block contradicted `program-goals.jsonl` | repository defect | block rewritten from registry truth: One-Theorem is the active external-validation hold; prior operational goals are closed; formal-publication remains blocked. |
| 15 | external PR review | Bell coefficient witness used a hard-coded list | repository defect | coefficients now regenerate from the actual `I_r(p^a)` formula; the expected sequence remains a separate assertion. |
| 16 | external PR review | capability map dropped retained Pass 001 and Benchmark 001 checkpoints | repository defect | both `checkpoint_pass` entries restored alongside Pass 002 and the ontology checkpoint. |
| 17 | external PR review | theorem scope alternated between “fixed-parameter” and fixed `q,r,W` | repository defect | live state, capability map, and P8 validation use the precise fixed-`q`, fixed-`r`, fixed-`W` wording. |
| 18 | CI review | deterministic generators could pass while leaving an uncommitted diff | guard defect | every generator-bearing CI job now ends with `git diff --exit-code`. Original Lemma Selection and repository-policy checks were added to the aggregate gate. |

## 3. Enforcement wiring

`.github/workflows/governance-required-gate.yml` runs on every pull request and
push to `main`. It includes:

- a clean-checkout and Lean-freeze repository-policy job;
- the nine core guards;
- Language Kernel v1;
- Translation Kernel v2 Pass 001 and Pass 002;
- Benchmark 001 and post-Pass-002 rescore;
- PVG Core Ontology v1;
- Original Lemma Selection;
- One-Theorem P0-P8 and external-validation hold;
- deterministic generated-state checks.

The aggregate `governance-gate` job fails if any required job fails.

Repository-settings follow-up remains necessary: mark `governance-gate` as a
required status check in branch protection for `main`. The available connector
cannot change that setting, so the workflow is present and green but branch
protection must be enabled in GitHub settings to prevent manual bypass.

## 4. PVG-UNDERSTANDING-DEEPENING-001 closure review

Program exit criteria (`governance/programs/PVG-UNDERSTANDING-DEEPENING-001.md`):

| Criterion | State |
|---|---|
| ≥ 18 canonical PVG objects | 20 present |
| ≥ 20 canonical morphisms/projections | 24 present |
| explicit reconstruction lattice | `maps/pvg-core-grammar-v1.md` reconstruction section |
| explicit composition table with ANT interfaces | `maps/pvg-core-grammar-v1.md` sections 5–6 |
| deterministic audit of examples and non-injectivity witnesses | ontology audit PASS; 16 witnesses; formula-driven Bell witness; generated results equal committed results |
| readiness decision for Adversarial Benchmark 002 | recorded in transition memory |

Decision: `checkpoint_candidate → checkpoint_pass`. The ontology
(20 objects, 24 morphisms, 16 witnesses, grammar map) is **frozen** before
Benchmark 002: no card, object, morphism, or witness expansion until the held-out
error map is produced, absent a separate explicit authorization.

## 5. Verified CI state

```text
repository-policy             PASS
nine core guards              PASS
Language Kernel v1            PASS
Translation Kernel v2 P001    PASS
Translation Kernel v2 P002    PASS
Benchmark 001 + rescore        PASS
PVG Core Ontology v1           PASS
Original Lemma Selection       PASS
One-Theorem P0-P8 hold         PASS
deterministic generated state  PASS
aggregate governance-gate      PASS
```

## 6. What this closure is not

This closure changes no mathematical state. It creates no theorem, no second
lemma target, no hidden benchmark score, and no originality certificate. The
theorem program remains on external-validation hold; P8 outreach remains
prepared and unsent until explicit user authorization.

```text
zero RH progress
zero GRH progress
no secured path
```

**Classification:** Governance / Enforcement closure audit. No mathematical claim.
