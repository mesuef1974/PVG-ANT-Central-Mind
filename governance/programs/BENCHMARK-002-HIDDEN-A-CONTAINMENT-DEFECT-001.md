# BENCHMARK-002-HIDDEN-A-CONTAINMENT-DEFECT-001

**Stage:** S1 (open 2026-07-13, window to 2026-08-16) of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001`.
**Classification:** Diagnostic — a negative certificate on a governance / concealment defect in the
STEP A staging artifacts of `ADVERSARIAL-PVG-ANT-BENCHMARK-002`. `Negative Certificate` is not a
member of the closed vocabulary in `governance/classification-system.md`; amending that vocabulary
is a governance act of its own and is not attempted here.
**Governs:** `BENCHMARK-002-SEALING-PROTOCOL-001.md` §0, §9; `BENCHMARK-002-ROLE-SEPARATION-RECEIPT-001.md`
§4.4; `HIDDEN-A-MANIFEST-001` (staging) §5, §6.
**Scope of this artifact:** the defect, its reproduction, its exact blast radius, and the binding
remedy. It contains **no gold keys**, no B material, no runs, no scores.
**Ceiling:** capability-measurement governance only — zero RH progress, zero GRH progress, no
secured path. A concealment defect is not a scientific result.

## 0. Pre-stage sync receipt (RULE-SYNC-PER-STAGE-RECEIPTS-001)
```
timestamp:    2026-08-05T03:18:33Z
branch:       claude/what-now-c825e1  (worktree; base for PR into main)
branch base:  3133c801b8aa1543c93695a6e704e6c63a79c5ea
origin/main:  3133c801b8aa1543c93695a6e704e6c63a79c5ea
ahead/behind: 0/0    tracked tree: clean
```

## 1. The defect

`SEALING-PROTOCOL` §9 requires that Set-A gold keys be held outside the answering process and that
only their SHA-256 hashes be committed. `HIDDEN-A-MANIFEST` §5 records this as realized, and
`benchmarks/pvg-ant-002/staging/hidden-a/.gitignore` excludes `A-keys.jsonl`.

The exclusion is nullified by a file the same directory commits:

```
benchmarks/pvg-ant-002/staging/hidden-a/author_hidden_a.py   918 lines, TRACKED
```

The generator carries all 48 gold-key strings as Python literals and writes `A-keys.jsonl` from
them. Withholding the *output* while committing the *source that deterministically produces it* is
not concealment. `HIDDEN-A-MANIFEST` §6 states the property outright without recognizing it as the
defect: "Regeneration is deterministic: `python author_hidden_a.py` re-emits identical files and
the same aggregate hash."

## 2. Reproduction (performed 2026-08-05, adversarial, from the tracked tree alone)

The committed generator was copied — alone, with no other repository file — into an empty
directory outside the repository and executed:

```
input:  author_hidden_a.py  (the tracked file, unmodified, no other input)
run:    python author_hidden_a.py    -> exit 0
output: A-keys.jsonl, A-prompts.jsonl, A-scoring-metadata.jsonl, HIDDEN-A-KEY-HASHES.txt

A-keys.jsonl line 1 = {case_id: "B002-A-01-1", <key field>: "<plaintext key; 48/48 present>"}

regenerated AGGREGATE = 1987512d402007909b840bbc80bddfc33cee2ba1ae8aa69b6ceca945b1f88fd6
committed  AGGREGATE = 1987512d402007909b840bbc80bddfc33cee2ba1ae8aa69b6ceca945b1f88fd6
verdict: EXACT MATCH
```

The aggregate hash committed to bind owner-held keys is re-derivable from the public tree, so the
hash commitment proves authorship-time fixity but grants **no** concealment. Any party with read
access to the repository holds the answer key to Set A.

## 3. Why every guard passed

`tools/hidden_set_staging_guard.py` carries an explicit leakage bar and reports
`PASS: ... no plaintext key leakage` against the defective tree. The bar is blind by construction:

```python
# the pre-hardening bar, as it stood at 3133c80
if f.startswith("benchmarks/pvg-ant-002/staging/hidden-a/") and f.endswith(".jsonl"):
    ...  # scan for a plaintext "gold" field
```

The scan is restricted to `.jsonl`. The one file carrying all 48 keys is `.py`, so it is never
read. The remaining bars match on *filenames* (`A-keys.jsonl`, `*.keys.jsonl`) rather than on
content, so a key-bearing file under any other name passes untouched. The guard verified the
naming convention, not the property the convention exists to enforce.

This is the same failure shape already recorded for the continuity guard: presence-of-text checks
standing in for the invariant. A green check is not evidence of containment.

## 4. Blast radius — bounded, and the bound is load-bearing

The defect does **not** contaminate the mind that S2 measures.

```
ARM-CURRENT-FROZEN-HEAD = 6960cb5   authored 2026-07-12 23:25:23 +0300
S1 A-AUTHORING-HEAD     = 3235fd7   authored 2026-07-13 22:36:51 +0300
git merge-base --is-ancestor 6960cb5 3235fd7   -> true (6960cb5 strictly precedes A)
git ls-tree -r 6960cb5 -- '*hidden_a*'         -> empty (generator absent at the frozen head)
```

Set A did not exist when ARM-CURRENT was frozen. No A key can be baked into the frozen mind; the
`SEALING-PROTOCOL` §0 head separation held. What is open is a **live retrieval channel at S2**:

```
tier B0 = 32 cases   pure reasoning, no repository retrieval      -> not exposed
tier B1 = 15 cases   + repository retrieval                       -> EXPOSED
tier B2 =  1 case    + full governed tools                        -> EXPOSED
                     ------------------------------------------------
                     16 of 48 cases reachable if the answering
                     checkout is any head containing the generator
```

Exposure is therefore conditional on the answering environment, not intrinsic to the cases.

## 5. Certificate

```
CERTIFIED  : the committed tree at 3133c80 discloses all 48 Set-A gold keys.
CERTIFIED  : the committed aggregate key-hash is re-derivable from the tree and confers
             no concealment.
CERTIFIED  : the staging guard's leakage bar does not test the property it names.
CERTIFIED  : ARM-CURRENT at 6960cb5 contains no Set-A material; head separation held.
NOT CERTIFIED: that Set A is unusable. Concealment is recoverable by environment
             containment (§6); the cases themselves are unaffected.
MISSING    : an ENVIRONMENT-FREEZE-RECEIPT pinning the S2 answering checkout. Until it
             exists, no S2 run on tiers B1/B2 may be treated as a hidden measurement.
```

Set A is **not** re-authored. Re-authoring would have to re-hit the frozen twelve-axis matrix and
all seven cross-cutting quotas exactly, would have to screen every new case against the now-public
Set A as `LEAK-3-NEAR-FORMULATION-OR-PROJECT-DERIVED` on top of the existing screen, and would
break `SEALING-PROTOCOL` §2's same-workshop condition that is what makes B an independent
generalization set. The defect is in the environment, and the remedy belongs in the environment.

## 6. Binding remedy

```
R1. The S2 answering environment is pinned to a checkout of 6960cb5 — a tree that provably
    contains neither the generator nor any Set-A artifact. Recorded explicitly in the
    ENVIRONMENT-FREEZE-RECEIPT (SEALING §10) as a fourteenth field. Retrieval-capable tiers
    (B1, B2) may reach no other head, and no full-history clone.       [BINDING]
R2. author_hidden_a.py is withdrawn from the live tree into owner custody. This is
    defense-in-depth ONLY: git history retains the object, so deletion alone contains
    nothing. R1 is the containment; R2 narrows the accident surface.   [BINDING]
R3. The staging guard's leakage bar scans every tracked file under the staging directory
    regardless of extension, and bars any tracked file that can re-emit a gold key.
    Content, never filename.                                          [BINDING]
R4. The same bar applies to Set B before any B artifact is committed. B commits ciphertext
    and SHA-256 only; no B generator, in any language, reaches the tree. [BINDING]
```

## 7. What this changes in the S1 exit (G1)

No G1 item is removed. `ENVIRONMENT-FREEZE-RECEIPT` acquires the R1 pin as a required explicit
field, and `LEAKAGE-AUDIT` must record this defect and its remedy rather than reporting a clean
screen. `HIDDEN-A-MANIFEST` §5's claim that keys are "never committed" is corrected here: the keys
were never committed *as a key file*, and were disclosed *as generator source*.

STEP B remains not started. No B artifact of any kind exists in the repository.

## Ceiling
```
negative certificate only · no gold keys · no B material · no runs · no scores
a concealment defect is not a result · zero RH progress · zero GRH progress · no secured path
```
