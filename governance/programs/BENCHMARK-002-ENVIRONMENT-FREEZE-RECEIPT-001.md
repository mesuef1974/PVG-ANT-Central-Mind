# BENCHMARK-002-ENVIRONMENT-FREEZE-RECEIPT-001

**Stage:** S1 (window closes 2026-08-16) of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001`.
**Operationalizes:** `BENCHMARK-002-SEALING-PROTOCOL-001.md` §10, extended by
`BENCHMARK-002-HIDDEN-A-CONTAINMENT-DEFECT-001.md` remedy R1.
**Status:** `INCOMPLETE — NOT VALID FOR ANY RUN.` Field 14 is settled. Fields 1–13 are proposed
where they are decisions and left open where they are observations; none is in force until the
owner ratifies.
**Classification:** Diagnostic (evaluation-environment receipt; creates no theorem).
**Ceiling:** capability measurement only — zero RH progress, zero GRH progress, no secured path.

## Why this file exists in an incomplete state

Remedy R1 is the containment for the Set-A concealment defect. Withdrawing the generator does not
contain anything — git history retains it — so the whole containment rests on *where the answering
process is allowed to look*. A rule that lives only in a certificate is not a constraint; it becomes
one when it is a field of the receipt that gates the run. This file is therefore created **before**
the run, with the pin settled and everything else openly unset, so that:

```
no S2 run may be treated as a hidden measurement while any field below reads UNSET.
```

An incomplete receipt is an honest artifact. A receipt filled with plausible values for a run that
has not happened would be a fabricated one.

## Field 14 — repository pin (SETTLED, binding)

```
answering checkout            = 6960cb5
reachable commits             = exactly one
refs present in the workspace = zero
remote                        = removed after fetch
rationale                     = 6960cb5 (2026-07-12) strictly precedes the Set-A authoring head
                                3235fd7 (2026-07-13); its tree contains no Set-A artifact and no
                                authoring generator
applies to                    = tier B1 (15 cases, repository retrieval)
                                tier B2 (1 case, full governed tools)
tier B0 (32 cases)            = pure reasoning; no retrieval channel; unaffected either way
```

### The checkout is not the pin — the construction is

Naming the commit is insufficient, and this was established by executing it rather than by reasoning
about it. A `git clone` followed by `git checkout 6960cb5` yields a **clean working tree** — zero
Benchmark 002 files — while the object store silently carries every remote ref, including
`origin/main` and `s1/hidden-a-authoring-001`. Measured on such a workspace:

```
git ls-files | grep -c pvg-ant-002        ->    0     (tree looks contained)
git rev-list --all --count                -> 1201     (object store is not)
git log --all -- <generator path>         ->    2 commits reachable
```

A retrieval-capable agent needs no exotic access to defeat that: `git log --all` and `git show`
are ordinary repository retrieval, which is exactly what tier B1 grants. The naive construction
therefore reproduces the original disclosure with a tree that passes inspection.

### Binding construction procedure

```bash
git init -q <answering-workspace>
cd <answering-workspace>
git remote add origin <repo>
git fetch -q --depth 1 --no-tags origin 6960cb54b49d3318af7807ea5829c0232192dc60
git checkout -q FETCH_HEAD
git remote remove origin          # no path back to the objects that were not fetched
```

### Verification (all five must hold immediately before the run)

```
git rev-parse HEAD                      -> 6960cb54b49d3318af7807ea5829c0232192dc60
git rev-list --all --count              -> 1
git for-each-ref | wc -l                -> 0
test -f .git/shallow                    -> present
git log --all --name-only --pretty=format: | grep -ci hidden-a   -> 0
```

Executed 2026-08-05 against the correct construction: HEAD matched, 1 commit reachable, 0 refs,
shallow marker present, 0 hidden-a paths in any reachable commit, 0 Benchmark 002 files in the
tree, and 489 files available — a functional workspace for tier B1 retrieval.

Any deviation in this field does not produce a degraded measurement. It produces **no** hidden
measurement, because the answering process could read the answers.

## Fields 1–13 — answering environment (PROPOSED, awaiting owner ratification)

Per `SEALING` §10, a change in any single field produces a NEW named run and never overwrites a
prior baseline.

Two kinds of field are mixed here and the distinction is load-bearing. Fields **2, 4, 13** and the
model identity in field 1 are *observations*: they can only be recorded from the run that happens,
and proposing values for them would be fabrication. Everything else is a *decision*, and a decision
can be made now, in the open, before anyone knows which way it favours the result. Freezing the
decisions in advance is the point of a freeze receipt — settling them after seeing a score is how a
baseline becomes unfalsifiable.

```
 1  model / provider / version        PENDING-OWNER
       decided : exactly one named model for the whole run; no mid-run substitution, no
                 fallback tier, no router. A different model is a different named run.
       observed: the exact provider model id and version string, verbatim.

 2  system prompt hash                PENDING-RUN
       decided : SHA-256 over the exact bytes of the system prompt as sent, recorded before
                 the first case.
       observed: the digest.

 3  memory / context manifest         PROPOSED: empty
       no persistent memory, no project memory files, no CLAUDE.md or equivalent injection,
       no prior-session carryover, no retrieval index built over any head other than 6960cb5.
       The answering context begins at zero and holds only: the case prompt, the tier's tool
       affordances, and (tiers B1/B2) the pinned workspace of field 14.
       This is the field the Set-A defect would have travelled through. It carries no A key
       and no B material by construction, because it carries nothing.

 4  context-window limit              PENDING-RUN — record the model's actual limit as-is

 5  allowed tools and tool versions   PROPOSED
       B0  (32 cases)  no tools. Reasoning only. No retrieval, no execution, no network.
       B1  (15 cases)  + read-only retrieval over the field-14 workspace ONLY: read, grep,
                       glob. No network. No git history commands (`log --all`, `show` on
                       unreachable objects) — the workspace has one commit, and this bar keeps
                       it that way even if the construction is later relaxed by accident.
       B2  ( 1 case)   + the governed external engines named in the case (exact prime counting).
                       Record each engine's version string.

 6  temperature                       PROPOSED: 0
 7  top_p                             PROPOSED: 1
 8  max_tokens                        PROPOSED: 8192 per case
       enough for a structured answer with certificate reasoning; a truncation is recorded as
       a truncation and never silently rescored.

 9  seed                              PROPOSED: 20260805 where supported;
       where unsupported, record the literal string "unsupported" — never omit the field, and
       never imply determinism the provider does not offer.

10  stop sequences                    PROPOSED: none

11  timeout policy                    PROPOSED: 15 minutes wall clock per case.
       On timeout the case is recorded as NO-ANSWER and scored as such. It is never retried,
       never extended, and never dropped from the denominator.

12  attempt and repetition counts     PROPOSED: exactly 1 attempt per case.
       No retries, no regeneration, no best-of-n, no human re-prompting, no "the model was
       having a bad run". The first answer is the answer. This single field is what separates
       a measurement from a demonstration, and it is the one most likely to be quietly bent
       once a disappointing number appears.

13  date and execution environment    PENDING-RUN — recorded at execution
```

### Ratification

The `PROPOSED` values above are not in force. They become field values when the owner ratifies
them, in writing, in this file. Until then this receipt remains `INCOMPLETE` and the gate below
stays closed — a proposal is not a decision, and this document does not get to promote its own.

## Gate

```
[ ] fields 1-13 recorded explicitly: every PROPOSED value ratified by the owner, every
    PENDING-RUN value observed and written down, nothing left PENDING-OWNER
[x] field 14 settled, with a binding construction procedure and five executed checks
[ ] answering workspace rebuilt by that procedure and re-verified immediately before the run,
    not once per session -- a workspace that was correct yesterday proves nothing today
[ ] context manifest (field 3) confirmed to carry no A key and no B material
```

Until every box is checked, `CURRENT-MIND-RAW-BASELINE-001` cannot be opened and no number
produced by any run may be recorded as a hidden-set score.

## Ceiling
```
environment receipt only · no cases · no keys · no runs · no scores
zero RH progress · zero GRH progress · no secured path
```
