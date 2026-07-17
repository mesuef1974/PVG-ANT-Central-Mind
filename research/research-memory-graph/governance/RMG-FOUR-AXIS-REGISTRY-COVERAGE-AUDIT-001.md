# RMG-FOUR-AXIS-REGISTRY-COVERAGE-AUDIT-001

Status: COMPLETED READ-ONLY COVERAGE AUDIT — OPERATIONAL AUTHORITY NOT GRANTED

Date: 2026-07-17

## Scope

This audit measures the legal RMG JSONL registry as it exists on `agent/pvg-axis-sum-continuation-002`.

It is read-only. It does not rewrite records, infer missing classifications, repair the adapter, authorize TKG migration, or promote any mathematical claim.

## Corpus

```text
legal RMG records          252
observed source classes     49
```

The 49 observed classes exceed the approximately 30 source labels measured in TKG. RMG therefore carries a larger normalization debt than TKG, not a smaller one.

## Mathematical-contribution coverage

```text
math_contribution_level present      72 / 252
math_contribution_level absent      180 / 252
```

The 180 records without a MATH axis are not primarily structural records.

```text
structural / dependency / task / governance records       15
untyped records                                             66
records with explicit mathematical content                 99
                                                          ----
total without MATH                                         180
```

The 99 mathematically substantive records include source classes such as:

- `ALGEBRA_IDENTITY`;
- `ANTI_COLLAPSE`;
- `ALGEBRA_LAW`;
- `ERROR_LADDER`;
- `BOUNDARY`;
- `OBJECT`;
- `TRANSLATION`;
- `IDENTITY`;
- `CERTIFICATE`;
- `CLAIM_REJECTION`.

Thus 165/180 missing-MATH records are not explained by ordinary edge or metadata exemptions.

## Coupling of MATH, OPS, and CERT

Presence and absence of the following three axes are perfectly coupled across the measured corpus:

- `math_contribution_level`;
- `operational_maturity`;
- `certificate_strength`.

```text
records with identical MATH/OPS/CERT presence state    252 / 252
records carrying MATH without OPS                          0
records carrying OPS without CERT                          0
records carrying CERT without MATH                         0
```

No legal record demonstrates independent assignment of any one of these three axes.

This does not prove the three concepts are logically identical. It proves that the registry has not operationally exercised their intended independence.

## Assimilation behaves differently

`assimilation_level` is not perfectly coupled to the other three axes and is the only measured governance axis showing independent variation.

Examples from the measurement include:

```text
untyped records: ASSIM present 22 / 66, while MATH/OPS/CERT present 0 / 66
OBJECT records:  ASSIM present 11 / 11, while MATH/OPS/CERT present 3 / 11
```

Therefore the four-axis separation exists as a design vocabulary, but only ASSIM has been materially exercised as an independent registry dimension.

## Main finding

```text
FOUR-AXIS SEPARATION = DESIGNED
FOUR-AXIS SEPARATION = NOT OPERATIONALLY PRACTISED
```

RMG-GOV-001 is a specification of intended governance, not evidence that the legal registry currently implements that governance.

The primary blocker is not schema syntax, adapter code, or verifier coverage. It is unresolved human authorship and classification debt.

## Human-authorship debt

Across RMG and TKG, the measured unresolved population includes approximately:

```text
RMG untyped records                              66
RMG mathematically substantive records no MATH   99
TKG untyped records                              27
TKG concept-like records with no known ceiling   12
```

These sets may overlap in semantic purpose and the total is not asserted as 204 unique claims. The figures identify the scale of reviewed human work required.

A schema, adapter, heuristic, or conservative default must not substitute for that authorship.

## Consequences

1. RMG remains the preferred architecture because parallel repository-wide memory authorities are prohibited.
2. RMG does not yet have operational authority over TKG.
3. TKG migration remains blocked.
4. The current adapter remains blocked.
5. The existing RMG-GOV-002 verifier remains defective because it accepts generated `MATH-M0` without value-origin provenance.
6. No canonical type may be assigned to the 66 untyped RMG records by heuristic.
7. No MATH/OPS/CERT value may be filled merely to satisfy schema completeness.
8. Human-reviewed classification and authorship must precede migration execution.

## Required next gate

The next authorized deliverable is:

`RMG-HUMAN-AUTHORSHIP-AND-CLASSIFICATION-QUEUE-001`

It must be an inventory and review queue, not an automatic migration.

At minimum it must separate:

- genuinely non-applicable structural records;
- typed mathematical records missing one or more governance axes;
- untyped mathematical records;
- records with authored aliases requiring normalization;
- records requiring new human-authored classification;
- records requiring new human-authored claim ceilings.

## Current state

```text
RMG ARCHITECTURAL AUTHORITY = PREFERRED
RMG OPERATIONAL AUTHORITY OVER TKG = NOT GRANTED
RMG FOUR-AXIS REGISTRY COVERAGE AUDIT = COMPLETE
RMG FOUR-AXIS PRACTICE = NOT DEMONSTRATED
MATH/OPS/CERT INDEPENDENCE = NOT DEMONSTRATED
ASSIM INDEPENDENCE = PARTIALLY DEMONSTRATED
PRIMARY BLOCKER = HUMAN AUTHORSHIP AND CLASSIFICATION DEBT
RMG ADAPTER REPAIR = BLOCKED BEHIND AUTHORSHIP POLICY
TKG MAPPING = NOT AUTHORIZED
TKG MIGRATION = NOT AUTHORIZED
MERGE TO MAIN = NOT AUTHORIZED
MATH = MATH-M0
PNT / PNT-AP / GOLDBACH / RH / GRH PROGRESS = NONE
```
