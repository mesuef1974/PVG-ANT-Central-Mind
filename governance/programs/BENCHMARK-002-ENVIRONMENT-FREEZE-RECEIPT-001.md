# BENCHMARK-002-ENVIRONMENT-FREEZE-RECEIPT-001

**Stage:** S1 (window closes 2026-08-16) of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001`.
**Operationalizes:** `BENCHMARK-002-SEALING-PROTOCOL-001.md` §10, extended by
`BENCHMARK-002-HIDDEN-A-CONTAINMENT-DEFECT-001.md` remedy R1.
**Status:** `INCOMPLETE — NOT VALID FOR ANY RUN.` Field 14 is settled. Fields 1–13 record the
answering environment and are owner-supplied facts about a run that has not happened.
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
full-history clone            = FORBIDDEN (shallow checkout of the pinned commit only)
reachable heads               = exactly one: 6960cb5
rationale                     = 6960cb5 (2026-07-12) strictly precedes the Set-A authoring head
                                3235fd7 (2026-07-13); `git ls-tree -r 6960cb5` contains no
                                Set-A artifact and no authoring generator
verification command          = git -C <answering-workspace> rev-parse HEAD   -> 6960cb5...
                                git -C <answering-workspace> ls-tree -r HEAD | grep -ci hidden
                                                                              -> 0
applies to                    = tier B1 (15 cases, repository retrieval)
                                tier B2 (1 case, full governed tools)
tier B0 (32 cases)            = pure reasoning; no retrieval channel; unaffected either way
```

Any deviation in this field does not produce a degraded measurement. It produces **no** hidden
measurement, because the answering process could read the answers.

## Fields 1–13 — answering environment (UNSET)

Per `SEALING` §10, a change in any single field produces a NEW named run and never overwrites a
prior baseline. Record each explicitly; `UNSET` is a blocker, never a default.

```
 1  model / provider / version        UNSET
 2  system prompt hash                UNSET
 3  memory / context manifest         UNSET   (must exclude A keys and all B material)
 4  context-window limit              UNSET
 5  allowed tools and tool versions   UNSET   (B0 reasoning · B1 +repo retrieval · B2 +full governed)
 6  temperature                       UNSET
 7  top_p                             UNSET
 8  max_tokens                        UNSET
 9  seed (where supported)            UNSET
10  stop sequences                    UNSET
11  timeout policy                    UNSET
12  attempt and repetition counts     UNSET
13  date and execution environment    UNSET
```

## Gate

```
[ ] fields 1-13 recorded explicitly, no UNSET remaining
[x] field 14 settled and verifiable by the two commands above
[ ] answering workspace verified at 6960cb5 immediately before the run, not before the session
[ ] context manifest (field 3) confirmed to carry no A key and no B material
```

Until every box is checked, `CURRENT-MIND-RAW-BASELINE-001` cannot be opened and no number
produced by any run may be recorded as a hidden-set score.

## Ceiling
```
environment receipt only · no cases · no keys · no runs · no scores
zero RH progress · zero GRH progress · no secured path
```
