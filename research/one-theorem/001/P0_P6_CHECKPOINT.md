# One-Theorem Program 001 — P0–P6 Checkpoint

**Target:** `ONE-LEMMA-TARGET-001`  
**Decision:** `CHECKPOINT PASS — COMPLETE MANUAL PROOF CANDIDATE, NOT YET CERTIFIED`  
**Program state:** remains active.

## Completed phases

| Phase | Result |
|---|---|
| P0 priority and terminology audit | PASS with narrowed originality claim |
| P1 independent symbolic audit | PASS |
| P2 local factorization and convergence | manual proof complete |
| P3 character decomposition | manual proof complete |
| P4 Mellin inversion and contour shift | manual proof complete |
| P5 residue constants and remainder | manual proof complete |
| P6 adversarial internal review | PASS at manual-logic level |

## Mathematical result currently supported

For fixed `q,r`, reduced `a mod q`, and `W in C_c^infinity(0,infinity)`, the manual proof candidate establishes a smoothed expansion for

\[
\sum_{n\equiv a\pmod q} I_r(n)W(n/x),
\qquad
I_r(n)=\prod_{p^\alpha\parallel n}\max(\alpha-2r+1,0),
\]

using the factorization

\[
D_{r,\chi}(s)
=
L(2rs,\chi^{2r})
L((2r+1)s,\chi^{2r+1})^2
H_{r,\chi}(s),
\]

with `H_{r,chi}` holomorphic for `Re(s)>1/(2r+2)`.

The expansion contains:

- an `x^(1/(2r))` layer from characters with `chi^(2r)=chi_0`;
- an `x^(1/(2r+1)) log x` layer from characters with `chi^(2r+1)=chi_0`;
- a smoothed error `O(x^(1/(2r+2)+epsilon))` for fixed parameters.

## Priority correction

Quadratic and cubic torsion-character selection is established prior art in square-full arithmetic-progression work. The possible contribution is therefore restricted to:

1. the divisor-box margin-interior weight `I_r`;
2. its general `2r`/`2r+1` layer structure;
3. the explicit weighted smoothed formula and constants;
4. the geometric PVG interpretation.

No claim is made that the torsion-selection mechanism itself is new.

## Automated certificates

- residual local order checked for `r=1,...,8`;
- simple- and double-pole constants independently verified with SymPy;
- principal-character finite part numerically verified for sample moduli;
- generated symbolic certificate equals the committed expected certificate;
- CI phase audit validates all P0–P6 artifacts and scientific ceilings.

## Remaining gates

### P7 source-grounded external review

- inspect the older square-full progression references cited by Chan;
- search for weighted powerful/k-full theorems covering the exact local weight;
- add exact source citations for fixed-strip Dirichlet-L growth and Mellin inversion;
- obtain an independent mathematical reading of the complete proof.

### P8 classification and closure

One of the following must be issued:

1. original theorem certificate;
2. new-observable/classical-method theorem classification;
3. exact known-result attribution;
4. corrected weaker theorem;
5. negative certificate or named missing condition.

## What this checkpoint does not do

- it does not close `GOAL-OP-ONE-THEOREM-001`;
- it does not certify originality;
- it does not authorize publication;
- it does not claim a new analytic method;
- it has no RH/GRH implication.

## Final checkpoint decision

```text
Manual proof candidate: COMPLETE.
Internal symbolic audit: PASS.
Internal adversarial logic review: PASS.
Source-grounded external review: PENDING.
Originality: PLAUSIBLE BUT UNCONFIRMED.
Certified theorem: NO.
```
