# RMG-GOV-005 Source Locator Resolution

Status: IMPLEMENTED_SPECIFICATION
Scope: high-risk theorem and PVG-contribution claims

## Purpose

Resolve every retrospective claim overlay to a concrete repository locator before source-file migration. A locator is not evidence of novelty; it is only an auditable pointer to the governed source.

## Required locator fields

- `claim_id`
- `repository`
- `branch_or_commit`
- `source_path`
- `section_or_symbol`
- `source_resolution_status`
- `content_review_status`
- `overlay_id`

## Resolution states

- `EXACT_FILE_AND_SECTION`
- `EXACT_FILE_SECTION_PENDING`
- `PATTERN_LOCATOR_ONLY`
- `UNRESOLVED`
- `SOURCE_NOT_PRESENT_ON_CURRENT_BRANCH`

No claim may be migrated into a source file from `PATTERN_LOCATOR_ONLY` or `UNRESOLVED`.

## Rules

1. Search-index hits are discovery aids, not authoritative source resolution.
2. Branch-specific files must be fetched from the governed branch or exact commit.
3. A source locator never upgrades `prior_art_status`, `math_contribution_level`, or `pvg_necessity_level`.
4. Missing source context freezes the claim at its conservative overlay ceiling.
5. Historical files remain unchanged until a reviewed migration patch exists.

## Current ceiling

`SOURCE_LOCATOR_PROTOCOL = ACTIVE`

`REPOSITORY_WIDE_SOURCE_RESOLUTION = NOT_COMPLETE`
