# Sync-Per-Stage Receipts Policy

**Rule:** RULE-SYNC-PER-STAGE-RECEIPTS-001
**Status:** binding operating law (owner ruling 2026-07-12)
**Supplements:** governance/canonical-repository-sync-policy.md (does not replace it)
**Classification:** Diagnostic (governance; creates no theorem)

## Governing rule

Local–remote synchronization is an operational condition of every program
stage, not side maintenance.

```text
origin/main      = the canonical repository truth
local main       = an operating replica that must match it
feature branches = the only place where work happens
```

## Binding protocol

### Before starting any stage or package

```powershell
git switch main
git fetch --prune origin
git merge --ff-only origin/main
git status --short
git rev-parse HEAD
git rev-parse origin/main
```

Work may start only if `HEAD == origin/main` and the tracked tree is clean.
The proof is recorded as a **Pre-stage sync receipt**.

### During work

- Every change happens on an independent branch cut from synced `main`.
- No direct commit on `main`. No force push. No automated hard reset.
- No automatic stash or deletion. No silent conflict handling.
- Every change merges through a pull request and the required
  `governance-gate` status.

### Before opening or updating a pull request

Fetch and rebase (or merge, per repository policy) onto `origin/main`, run
the guards locally, and record: branch-base SHA, branch-head SHA,
`origin/main` SHA, tree status, and guard results.

### After merging a stage's outputs

Repeat the sync sequence on `main` and prove:

```text
branch = main
HEAD   = origin/main
ahead  = 0
behind = 0
tracked changes = 0
```

The proof is recorded as a **Post-stage sync receipt**.
**No stage closes without it.**

## Receipt contents

Every receipt (pre and post) records:

```text
timestamp
local HEAD
origin/main SHA
branch
ahead/behind
tracked-tree status
scheduled-task status
last sync result
```

## Scheduled task = helper layer only

The workstation task `PVG-ANT-Canonical-Sync` (every 15 minutes: fetch,
then safe fast-forward only, never silent conflict handling) is a helper
layer. It is not a substitute for the two receipts.

## Dashboard enforcement

The execution dashboard `PVG_ANT_Model_Roadmap/index.html` (Roadmap v2.2)
carries two mandatory fields on every stage — Pre-stage sync receipt and
Post-stage sync receipt — and programmatically refuses to mark a stage
completed while the post-stage receipt is empty. The dashboard enforces the
receipt's existence; the truth of its content is proved by the git commands
themselves, which the receipt transcribes.

## Deferred upgrade (approved in principle, not yet built)

After G0, the sync script may emit a machine-generated JSON receipt
(timestamp, branch, local_head, origin_main, ahead, behind,
tracked_tree_clean, scheduled_task, last_sync_result, receipt_sha256) that
the dashboard imports instead of manual typing, with a guard verifying
fields and hash. This upgrade is not a reason to open a new package.

## Ceiling

Synchronization governance creates no theorem: zero RH progress, zero GRH
progress, no publication readiness, no originality certificate.
