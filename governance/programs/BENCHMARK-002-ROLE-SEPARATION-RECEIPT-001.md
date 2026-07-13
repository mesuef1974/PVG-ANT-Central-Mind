# BENCHMARK-002-ROLE-SEPARATION-RECEIPT-001

**Stage:** S1 authoring workshop of `PVG-ANT-RESEARCH-MODEL-PROGRAM-001`.
**Governs:** who may see what, in which context, across the authoring → sealing → answering →
scoring lifecycle of `ADVERSARIAL-PVG-ANT-BENCHMARK-002`, under
`BENCHMARK-002-SEALING-PROTOCOL-001.md` §0, §7, §9 and registered spec §2.
**This IS the G1 artifact `ROLE-SEPARATION-RECEIPT`** (a post-authoring confirmation addendum
is appended at seal time). Frozen at workshop open. Contains NO cases, NO keys.
Capability measurement only — zero RH progress, zero GRH progress.

## 0. The one defect this receipt exists to prevent
```
A/B prompts AND keys must never enter the ARM-CURRENT answering context.
```
The answering agent is the mind frozen at `6960cb5` (ARM-CURRENT), instantiated fresh for both
the S2 raw-A baseline and the separate, later S8 single-B generalization run. The authoring is
done on the moving control head (`5a02032` and beyond). If the context that answers is the same context
that authored or saw A keys or B, the entire benchmark is void. Every rule below serves this.

## 1. The five roles
```
R1 case author           authors prompt · expected_structure · rubric field · tags
R2 key author / verifier authors and verifies gold keys for A and B
R3 answering agent       ARM-CURRENT frozen at 6960cb5 — the system under test
R4 scoring agent         scores frozen responses under the frozen rubric (phased access, §1a)
R5 B custodian           holds the B decryption key offline; guards B concealment
```
Registered spec §2 fixes four roles; the sealing protocol §7 adds R5 (the independent B
custodian of §1.4). R1 is never the sole R4. R5 is distinct from R3.

### 1a. R4 (scoring agent) phased access
R4 receives, **only after the corresponding answering run has been immutably frozen**:
- the frozen scoring rubric,
- the prompts being scored,
- the answering agent's frozen responses,
- the applicable gold keys,
- the minimum case metadata required for scoring.

R4 does NOT receive authoring deliberations, hidden-set custody material, or any key before the
corresponding responses are immutably frozen. For Set B, R5 releases the B prompts and keys to
R4 only after the single authorized B answering run has completed and its responses have been
immutably frozen.

## 2. How separation is actually realized (honest mechanism)
This project runs with one human owner and AI assistants, not five separate human operators.
Separation is therefore realized by **context/session isolation + owner key custody + an
immutable sequence**, and the load-bearing guarantee is verifiable, not organizational:
```
CONTEXT ISOLATION
  Authoring sessions (R1/R2) run on the moving control head and are DISTINCT sessions from
  the S2 answering session (R3). The answering agent is instantiated fresh from the 6960cb5
  snapshot with a memory/context manifest that provably EXCLUDES: all A prompts held for
  authoring, all A keys, and all of B. (The ENVIRONMENT-FREEZE-RECEIPT attests this manifest
  at G1/S2.)
B IN A SEPARATE CONTEXT
  B prompts and keys are authored in an isolated session and are NEVER pasted into any context
  that may act as R3. The current control-head workshop session explicitly does NOT hold B.
  Only B ciphertext + a SHA-256 manifest enter main; a hash alone is not concealment.
KEY CUSTODY (owner-held)
  The owner is the human R5 custodian: the B decryption key is offline and owner-held. A keys
  are held outside the answering process; A key-hashes are committed BEFORE any scoring run.
SEQUENCING GATE
  R4 scores only AFTER the raw-A baseline is frozen and A keys are opened (binding sequence).
  B is decrypted only for its single final generalization run (program stage S8 — the last step
  of the immutable binding sequence, after the A rerun, ablation arms, and targeted learning),
  into a fresh R3 context.
```

## 3. What each role may see (access table)
```
role  A prompts     A keys        B ciphertext  B prompts/keys   frozen rubric
R1    yes (authors) no*           no            authors in       yes (co-authors)
                                                isolated session
R2    yes           yes (authors) no            authors in       yes
                                                isolated session
R3    yes, at S2    NEVER         no            NEVER (except     no (rubric is not the test)
      baseline only               (ciphertext)  the single B run,
                                                prompts only)
R4    post-freeze²  post-freeze²  no            via R5, post-     yes; + frozen responses,
                                                B-run-freeze²     scored prompts, metadata
R5    no            no            yes (guards)  holds B key       no
```
`*` R1 may know a case's intended answer shape (expected_structure) but the gold key of record
is R2's; R1 is never the sole scorer (R4).
`²` R4 receives each item ONLY after the corresponding answering run is immutably frozen; for
Set B, R5 releases the B prompts and keys to R4 only after the single B run is frozen (§1a, §4).

## 4. Binding constraints (frozen)
```
1. The control-head authoring session is NEVER any answering context (neither the S2 raw-A
   baseline nor the S8 single-B run).
2. A keys and B never enter any context that will act as R3.
3. B is authored and encrypted in an isolated session; only ciphertext + SHA-256 reach main.
4. A key-hashes are committed before any scoring run; scoring is post-baseline-freeze only.
5. R1 ≠ sole R4; R5 ≠ R3. R4 receives — only after the corresponding answering run is
   immutably frozen — the frozen rubric, the scored prompts, the frozen responses, the
   applicable keys, and the minimum scoring metadata; never authoring deliberations, custody
   material, or any key before the matching responses are frozen (§1a).
6. For Set B, R5 releases the B prompts and keys to R4 only after the single authorized B
   answering run has completed and its responses are immutably frozen.
7. Any breach of 1–6 voids the affected set and is recorded as a leakage incident, not hidden.
```

## 5. Post-authoring confirmation (appended at seal time — placeholder now)
At G1 this receipt gains a confirmation block attesting, with evidence, that: the S2 answering
manifest excluded A keys and B; B ciphertext-only reached main; A key-hashes were committed
pre-scoring; and no role-boundary breach occurred. Not yet attestable — authoring has not begun.

## Ceiling
```
role and custody rules only · no cases · no keys · no runs
zero RH progress · zero GRH progress · no secured path
```
