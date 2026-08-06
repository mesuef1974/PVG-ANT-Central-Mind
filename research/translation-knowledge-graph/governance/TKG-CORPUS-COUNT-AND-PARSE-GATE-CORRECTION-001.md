# TKG-CORPUS-COUNT-AND-PARSE-GATE-CORRECTION-001

Status: SUPERSEDING COUNT CORRECTION

Date: 2026-07-17

## Superseded measurements

Any TKG governance document on this branch that treats the corpus as 118 records, Family A as 64 records, or axis-complete records as 81 is numerically superseded by this correction.

The earlier parser silently omitted two malformed TKG-004 records. Therefore historical ratios such as `45/118`, `76/118`, and `73/118` are not valid whole-corpus measurements. They remain evidence about the 118 parseable records seen by the earlier measurement only.

## Corrected corpus

```text
TKG total physical records             120
Family A records                        66
Family B records                        54
axis-complete records                   83
human-authorship queue                  37
source-integrity repairs                 2
```

The two recovered records are:

- `TKG004-IDENTITY-ZETA-LAMBDA`;
- `TKG004-NODE-GENERALIZED-MANGOLDT`.

Both contain authored type and governance fields after structural JSON repair. They do not change the 12/15/10 queue distribution.

## Parse-first rule

The canonical order of operations is now:

1. enumerate physical nonblank JSONL lines;
2. parse every line as exactly one JSON object;
3. classify failures as `UNPARSEABLE / NEEDS_REPAIR`;
4. block type and ceiling classification until repair;
5. only then measure field coverage and construct queues.

No future audit may silently skip malformed lines.

## Current scientific boundary

This correction improves source integrity and measurement accuracy only.

```text
MATH = MATH-M0
reasoning = NOT ESTABLISHED
PNT / PNT-AP / Goldbach / RH / GRH progress = NONE
benchmark sealed = NO
merge to main = NOT AUTHORIZED
```
