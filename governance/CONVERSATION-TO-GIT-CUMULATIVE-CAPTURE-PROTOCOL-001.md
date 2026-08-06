# Conversation-to-Git Cumulative Capture Protocol 001

Status: active on `agent/pvg-axis-sum-continuation-002`

Classification: Governance

## Purpose

Prevent loss of research value created in conversation. Every substantive mathematical, architectural, governance, benchmark, tooling, or planning contribution must be converted into repository state before it is called complete.

## Completion rule

```text
conversation explanation != completed work
completed work = repository artifact + commit + pushed branch state
```

## Capture classes

Every substantive contribution is classified as one of:

```text
UNIT
PROTOCOL
DECISION
TOOL_SPEC
BENCHMARK_SPEC
AUDIT
REGISTRY_UPDATE
ROADMAP_UPDATE
OPEN_WALL
EXPERIMENT_PLAN
```

Informal discussion that creates no reusable project state may remain uncaptured. Any discussion that changes definitions, architecture, dependencies, scientific ceilings, validation status, next actions, or project goals must be captured.

## Step-by-step operating rule

For each completed step:

1. identify the reusable artifact;
2. assign a stable path and status;
3. record classification and validation state;
4. record dependencies and scientific ceiling;
5. create or update the repository file;
6. commit immediately to the current working branch;
7. report the path and commit SHA;
8. do not combine unrelated completed steps into one delayed batch when separate commits are practical.

## Cumulative integrity requirements

No component may disappear merely because a later architecture supersedes it. Superseded material must be:

- retained and marked superseded;
- linked to its replacement;
- or migrated with an explicit migration receipt.

Deletion without a traceable replacement or governance reason is prohibited.

## Conversation checkpoint

At natural checkpoints, maintain a current-state ledger containing:

```text
current branch
current head
completed artifacts
planned artifacts
blocked artifacts
scientific ceilings
validation not yet performed
merge or infrastructure blockers
```

## Honest-status rule

The following are distinct and must not be collapsed:

```text
discussed
specified
implemented
executed
benchmarked
validated
merged
released
```

A file specification does not imply executable implementation. A public benchmark definition does not imply a benchmark run. Local evidence does not imply GitHub Actions success. Architecture does not imply autonomous specialist competence.

## Branch rule

Current cumulative work is written to:

`agent/pvg-axis-sum-continuation-002`

PR #58 remains frozen separately until its required GitHub status check is green. New cumulative work must not alter the frozen PR head.

## Scientific preservation rule

All captured artifacts must preserve the project ceilings:

```text
NO fabricated novelty
NO Goldbach proof claim without proof certificate
NO RH/GRH progress claim without proof certificate
NO autonomous validation claim without isolated locked evaluation
NO publication-readiness claim without publication governance
```

## Utilization objective

The accumulated repository is not an archive-only destination. When maturity gates are met, the project must expose reusable value through:

- installed specialist skills;
- executable reasoning schemas;
- benchmarks and evaluators;
- research memory graphs;
- governed planning and diagnostic tools;
- formal or computational interfaces where justified.

## Current enforcement state

```text
PROTOCOL = ACTIVE
RETROACTIVE_FULL_CONVERSATION_IMPORT = NOT_CLAIMED
CURRENT_PATH_CAPTURE = REQUIRED
STEPWISE_PUSH = REQUIRED
LOSSLESS_MIGRATION = REQUIRED
```
