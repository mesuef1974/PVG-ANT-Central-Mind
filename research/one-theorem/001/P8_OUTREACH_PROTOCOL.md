# P8 External Outreach Protocol — ONE-LEMMA-TARGET-001

**Stage:** `P8-EXTERNAL-REFEREE-001`  
**Purpose:** obtain independent priority and proof judgments without overstating originality or asking one reviewer to certify every aspect of the project.

## 1. Separate the two roles

### Role A — priority and significance reviewer

This reviewer is asked only to assess:

1. whether the weight
   \[
   I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0)
   \]
   has an established name or appears in earlier literature;
2. whether the stated smoothed arithmetic-progression theorem is subsumed by a published general theorem;
3. whether the result is routine, modest, or potentially substantive.

This reviewer is **not** asked to certify every proof line.

### Role B — analytic proof referee

This reviewer is asked only to audit:

1. the Bell-series and Euler-factor calculation;
2. the factorization
   \[
   D_{r,\chi}(s)=L(2rs,\chi^{2r})L((2r+1)s,\chi^{2r+1})^2H_{r,\chi}(s);
   \]
3. the half-plane of holomorphy and convergence for `H`;
4. treatment of primes dividing the modulus;
5. Mellin normalization, contour shift, residues, and parameter dependence;
6. the final fixed-parameter error term.

This reviewer is **not** asked to certify originality.

## 2. Contact order

1. Contact one priority reviewer first.
2. Contact one proof referee independently.
3. Do not send the same request to many people simultaneously without disclosure.
4. If a candidate declines or does not respond, record the outcome and move to the next candidate.
5. Do not interpret silence as approval.

## 3. Materials to send

Because the repository is private, do not send private GitHub links unless access has been granted. Prepare a compact attachment bundle containing:

- the exact theorem statement;
- the definition and divisor-box interpretation of `I_r`;
- a proof outline;
- the relevant full proof for the proof referee;
- the source-audit summary for the priority reviewer;
- the scientific-ceiling statement.

Canonical internal files:

- `P8_EXTERNAL_REFEREE_PACKET.md`;
- `P8_EXTERNAL_VALIDATION_001.md`;
- `P8_EXTERNAL_VALIDATION_002.md`;
- `P8-external-source-ledger.json`;
- the complete proof files under `research/one-theorem/001/`.

## 4. Mandatory wording discipline

Every request must state:

- the result is internally proved but not externally refereed;
- the analytic machinery is classical;
- quadratic/cubic torsion-character selection is classical;
- no claim of certified originality is being made;
- the purpose of the request is to determine the correct classification.

Do not use (every phrase below is forbidden):

- “new theorem” without qualification (forbidden);
- “breakthrough” (forbidden);
- “new method” (forbidden);
- “RH/GRH progress” (forbidden);
- “publication ready” (forbidden).

## 5. Reviewer outcomes

Record exactly one outcome for each role.

### Priority outcome

- `NO_EXACT_PRECEDENT_LOCATED`
- `KNOWN_UNDER_OTHER_NAME`
- `SUBSUMED_BY_GENERAL_THEOREM`
- `POSSIBLY_NEW_BUT_ROUTINE`
- `POSSIBLY_NEW_AND_MODESTLY_SIGNIFICANT`
- `INSUFFICIENT_INFORMATION`

### Proof outcome

- `PROOF_PASS`
- `PASS_WITH_MINOR_REPAIRS`
- `MAJOR_REPAIR_REQUIRED`
- `STATEMENT_REQUIRES_WEAKENING`
- `PROOF_FAIL`
- `INSUFFICIENT_INFORMATION`

## 6. Terminal classification rule

The project may close `One-Theorem Program 001` only after both roles produce usable judgments.

Possible terminal classifications remain:

A. original modest theorem;
B. new PVG-derived application of a known general theorem;
C. known result in different notation;
D. corrected theorem;
E. correct but insufficiently significant without strengthening.

## 7. Current ceiling

```text
Internal proof: complete.
Online source audit: partial pass.
Priority review: absent.
External proof review: absent.
Certified originality: absent.
Publication readiness: absent.
RH progress: none.
GRH progress: none.
```
