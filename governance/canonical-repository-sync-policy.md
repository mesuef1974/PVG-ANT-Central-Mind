# Canonical Repository Synchronization Policy

**Policy ID:** `POLICY-CANONICAL-SYNC-001`  
**Status:** governing repository-side; local scheduled activation required once per workstation  
**Classification:** Governance / Repository Operations

## 1. Canonical truth

`origin/main` is the canonical repository truth. A local clone is an execution copy, not an independent state authority.

The governing rule is `RULE-CANONICAL-SYNC-001`:

> Every work session begins from a fetched and verified `origin/main`; local `main` may advance only by fast-forward; divergence, a dirty worktree, or an unexpected remote stops automatic synchronization rather than resolving it silently.

## 2. What permanent synchronization means

Permanent synchronization does **not** mean overwriting uncommitted work or auto-resolving conflicts. It means:

1. the remote-tracking state is fetched repeatedly;
2. a clean local `main` is fast-forwarded automatically when safe;
3. feature work is created only from a verified current `origin/main`;
4. direct pushes and force pushes to `main` are forbidden;
5. every merge is accepted only through the required `governance-gate` ruleset;
6. stale, dirty, ahead, or diverged states are reported as blockers.

This is deliberately fail-closed. A synchronization alarm is not repaired by `reset --hard`, force push, stash deletion, or implicit conflict resolution.

## 3. Remote enforcement

The remote repository must retain:

```text
ruleset                    = governance-required
target                     = refs/heads/main
required status check      = governance-gate
bypass actors              = none
current user can bypass    = never
```

For the strongest merge-state synchronization, the ruleset should also require the pull-request head to be current with `main` before merging (`strict_required_status_checks_policy = true`). This setting is external repository configuration and cannot be inferred from files alone.

## 4. Local synchronization command

The canonical command is:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File tools/sync_canonical_main.ps1 `
  -Mode SafeSync
```

Modes:

- `Audit`: fetch and report only;
- `SafeSync`: fetch, then fast-forward only when the current branch is a clean `main`;
- `PrepareBranch`: require a clean worktree and `HEAD == origin/main` before a new work branch begins.

The command verifies the repository identity, fetches `origin/main`, computes ahead/behind counts, and refuses unsafe mutation.

## 5. Scheduled local activation

Each Windows workstation that acts as a canonical working clone should run the installer once:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass `
  -File tools/install_canonical_sync_task.ps1
```

The installed task performs `SafeSync` every fifteen minutes. When the clone is dirty or on a feature branch it fetches and reports but does not rewrite work.

Because scheduled tasks live outside Git, repository CI can verify the installer and synchronization logic but cannot prove that a particular workstation has activated the task. Local activation therefore requires a separate operator receipt.

## 6. Required session protocol

### Start of work

```text
fetch origin/main
→ verify repository identity
→ verify clean worktree
→ verify HEAD is based on current origin/main
→ create or continue a feature branch
```

### Before push

```text
fetch origin/main
→ inspect ahead/behind
→ rebase or merge only by explicit reviewed action
→ run required guards
→ push feature branch
```

### After merge

```text
switch to main
→ fetch origin/main
→ fast-forward only
→ verify clean tree
→ record main SHA in the maturation receipt
```

## 7. Prohibitions

- no direct work on `main`;
- no force push to `main`;
- no automatic hard reset;
- no silent stash or deletion of local work;
- no automatic conflict resolution;
- no claim of local synchronization without a fetched SHA and clean-tree evidence;
- no claim that repository-side policy proves workstation-side task activation.

## 8. Scientific scope

This policy changes repository reliability only. It creates no mathematical knowledge, theorem, originality certificate, publication readiness, RH progress, or GRH progress.
