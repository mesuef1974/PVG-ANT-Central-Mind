# BENCHMARK-002-LEAKAGE-AUDIT-001

**Stage:** S1 (window closes 2026-08-16) of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001`.
**Satisfies:** the `LEAKAGE-AUDIT` item of the S1 exit (G1) in `BENCHMARK-002-SEALING-PROTOCOL-001.md`,
under §8 (leakage policy) and §9 (concealment).
**Covers:** `Hidden Set A` (48 cases, plaintext in-tree) and `Hidden Set B` (48 cases, sealed as
ciphertext).
**Classification:** Diagnostic — evaluation-integrity audit. Creates no theorem.
**Contains no case, no prompt, no key.** Aggregate measurements and verdicts only.
**Ceiling:** capability measurement only — zero RH progress, zero GRH progress, no secured path.

## 0. This is not a clean screen

`SEALING` §8 asks whether the hidden sets leak. The honest answer has three parts, and only the
first is clean.

```
textual leakage      measured here, independently, across all four screening corpora   CLEAR
conceptual leakage   self-reported by each authoring session; NOT independently verified
concealment          Set A was disclosed for three weeks; Set B carries a custody deviation
```

An audit that reported only the first line would be true and useless. The Set-A concealment defect
was found *after* a guard had reported "no plaintext key leakage" against the defective tree for
three weeks, so this document states what was measured, what was accepted on report, and what
remains uncertified.

## 1. Textual screen — measured, not relayed

5-gram Jaccard similarity over prompt text, computed for this audit rather than taken from either
authoring session's own report. Threshold for review: 0.25.

```
corpus                   units    max(A)   max(B)   pairs >= 0.25
Benchmark 001               60     0.000    0.008        0
Kernel v2 Pass 001          24     0.000    0.004        0
Kernel v2 Pass 002          12     0.000    0.000        0
Core Ontology v1            44     0.000    0.000        0
------------------------------------------------------------------
Hidden Set A vs Hidden Set B (48 x 48)   max 0.022        0
within Hidden Set B (internal duplication)  max 0.000     0
```

Verdict: **no textual overlap at any threshold that would matter.** The highest value anywhere is
0.022, which is shared vocabulary in a field with a fixed technical lexicon, not shared formulation.

## 2. What this screen cannot see

`SEALING` §8 is explicit that conceptual leakage outranks textual: `LEAK-2` disqualifies a case at
*zero* textual overlap. N-gram similarity cannot detect `LEAK-2`. A case that reuses a project
insight in entirely fresh words scores 0.000 here and is still disqualifying.

So the `LEAK-0-CLEAR` classification on all 96 cases rests on:

```
Set A   the A-authoring session's per-case conceptual screen, self-reported in HIDDEN-A-MANIFEST §4
Set B   the B-authoring session's per-case conceptual screen, self-reported, with candidate cases
        discarded and re-authored on disjoint terrain rather than admitted
```

Both are **self-reports**. Neither has been checked by a party that did not author the cases. In a
benchmark whose staging guard already once reported PASS against a defective tree, a self-reported
screen is a claim, not a certificate.

```
MISSING CERTIFICATE: independent conceptual-leakage review of both hidden sets by a reviewer
who authored neither. Until it exists, LEAK-0-CLEAR is the authors' judgment, not a verified
property.
```

This is recorded as a named missing certificate rather than closed by assertion. It does not block
G1 — the protocol requires the screen, not an independent re-screen — but it bounds what a later
reader may claim about leakage.

## 3. Set A — concealment failed, and was contained

Recorded in full in `BENCHMARK-002-HIDDEN-A-CONTAINMENT-DEFECT-001`; summarized here because a
leakage audit that omitted it would be the omission.

```
defect     the committed generator carried all 48 gold keys as plaintext literals; run alone
           outside the repository it re-emitted them and reproduced the committed aggregate
           hash exactly. Withholding the key file while committing its deterministic source
           is not concealment.
window     3235fd7 (2026-07-13) through 3133c80 (2026-08-05), and the objects remain in history
detection  none of the guards. Found by adversarial re-derivation, not by CI.
bound      ARM-CURRENT (6960cb5, 2026-07-12) strictly precedes the authoring head and holds no
           Set-A material, so nothing is baked into the measured mind. The exposure was a live
           retrieval channel affecting the 16 B1/B2-tier cases only.
remedy     environment pin (RULE-HIDDEN-SET-ENVIRONMENT-PIN-001), generator withdrawn to owner
           custody, staging guard rebuilt on content and inventory bars.
residual   git history retains the generator. Containment is the pin, not the withdrawal.
           A full-history clone still discloses Set A.
```

Consequence for Set B, and it is a real narrowing: Set A is now public. Every B case was screened
against it as a potential `LEAK-3-NEAR-FORMULATION-OR-PROJECT-DERIVED` source — a screen that did
not exist when Set A itself was authored.

## 4. Set B — concealment holds, custody does not

```
sealed     age v1.3.1, X25519. Prompts AND keys encrypted together, per SEALING §9.
committed  ciphertext + SHA-256 manifest + case-free metadata. Nothing else.
verified   round trip confirmed before any plaintext was deleted: decrypt(ciphertext)
           reproduced the plaintext bundle digest exactly.
guard      the staging guard now enforces a strict allowlist on hidden-b/ — only HIDDEN-B-*,
           and no extension that cannot be ciphertext or a hash manifest. Installed BEFORE any
           B artifact existed, and tested against a fixture carrying a generator and plaintext
           prompts, which it rejected.
working copies  the normalization backups were deleted before sealing. A second plaintext copy
           of a hidden set is the defect this stage exists to contain.
```

**Custody deviation — open.** `SEALING` §9 requires a custodian independent of the answering
process. The owner directed that the key be generated in this session and handed over. It was
written straight to a file and never printed, so it did not enter the generating context — but
*generated here* is not *independently held*.

```
DEVIATION: the B decryption key was generated by the same session that assembled the sealed
bundle. Recorded as a deviation, not described as compliance.
CLOSES WHEN: the owner moves B-CUSTODY-IDENTITY.key to a location only they control, and the
copy in the working custody directory is destroyed.
```

## 5. Role separation as actually realized

```
R1/R2 Set A   authoring session, 2026-07-14                          separate
R1/R2 Set B   cold session, 2026-08-06; never opened any hidden-a
              file and never searched history for Set A               separate
R3  answering ARM-CURRENT at 6960cb5 — has seen neither set           separate, and pinned
R4  scoring   not yet assigned                                        PENDING
B custodian   see §4                                                  DEVIATION
```

One further exposure, stated plainly: the session that audited the Set-A defect regenerated all 48
A keys twice to prove the leak, and later assembled and sealed Set B without reading its cases —
the B plaintext was written by the cold session directly to owner custody and never entered the
assembling context. That session is disqualified as an answering context and as a Set-B author.
It is neither.

## 6. Verdict

```
textual leakage, A and B, all corpora                     CLEAR (measured here)
conceptual leakage                                        SCREENED, NOT INDEPENDENTLY VERIFIED
Set A concealment                                         FAILED, CONTAINED, residual in history
Set B concealment                                         HOLDS
Set B custody independence                                DEVIATION, open
scoring role assignment                                   PENDING
```

G1 blockers arising from this audit: none. Open items it records: the missing independent
conceptual review, the custody deviation, and the unassigned scoring role.

## Ceiling
```
audit only · no cases · no keys · no runs · no scores
a leakage screen is not a proof of independence
zero RH progress · zero GRH progress · no secured path
```
