# Scope-Amendment, Debt, and Certificate-Record Policy

Registry ID: `SCOPE-AMENDMENT-AND-DEBT-POLICY-001` · Status: **Active Governance** · Classification: Governance / Coherence Policy.

General (book-independent) governance layer, first instantiated for the Opera de Cribro Opening Pass (v0.7) but written to govern every book whose scope declares a load-bearing certificate structure. It records how a frozen scope may be amended, how a missing obligation (a *debt*) is tracked and settled, how book-overlay closure is kept distinct from declared-objective completion, and the structural record required for any application-specific parity-crossing certificate.

Ceiling (unchanged): zero RH progress · zero GRH progress · no secured path.

---

## 1. Judgment cycle (source-first, project-governed)

```text
TOC / preface        -> provisional routing hypothesis (recorded, never a trusted verdict)
source packet        -> grounded unit classification
closure review       -> trusted unit status
load-bearing discovery -> forward obligation, or a named State-Repair (never silent reopen)
trusted debt settlement -> debt becomes satisfied, not erased
objective coverage audit -> recommendation only
independent governance order -> declared_objective_coverage.complete may be flipped
```

**Discovery rule:** source-first. `MC-001` and the project frontiers do NOT determine mining selection.
**Promotion rule:** project-governed. Frontier / `MC-001` links are added only AFTER normalization, in `integration-links.md`.

A frozen scope's chapter routing is a **provisional hypothesis only**. A trusted classification requires a source packet and a closure review. A mismatch between the provisional hypothesis and the packet is **recorded** (`packet_mismatch = true`, original hypothesis + packet-grounded classification + reason), never silently rewritten.

---

## 2. Load-bearing structure (declared and frozen before mining)

The scope document must declare, before any packet, the list of **load-bearing certificate nodes** on which the declared objective depends. Each node carries:

```text
status = unexamined | packet_received | normalized | closed
load_bearing_for_declared_scope = true
deferral_allowed = false
```

`deferral_allowed` does NOT flip to `true` by an ordinary in-unit edit — only by an independent governance order (§3). Without a frozen list, "load-bearing" would be a manipulable post-hoc judgment; the freeze is what makes the no-silent-deferral rule falsifiable.

**Reduction** of a node (removing it from the load-bearing set) carries the burden of proof: retention is the default, reduction is the claim. The reviewer verdict is `failed_to_show_nonessential` (keeps the node) — never `proved_nonessential` — when in doubt.

**Discovery** of a new indispensable node not on the frozen list is expansion-only: the burden is reversed. Retention of the list is the default; the proposer must show the node is **not** absorbable into an existing node. Reviewer verdicts: `failed_to_absorb` (accepts the new node) / `absorbed_without_loss` (rejects it); doubt rejects the addition. An accepted discovery **generates a forward obligation and blocks closure until classified and resolved** — it does NOT reopen a closed unit. If it conflicts with a trusted closed claim, the path is a **named, bounded State-Repair**, not a rewrite of the closed unit's history.

---

## 3. Scope amendment (four classes, distinct closure effects)

A frozen scope is amended ONLY by an independent governance order that names its cause and leaves an audit trail. The cause class determines the effect on closure — capacity failure must NOT close a layer with the same force as a source boundary.

```text
source_boundary_amendment
  trigger        = the source itself defers / externalizes the node (proved from the source)
  old_status     = load_bearing_pending
  new_status     = external_source_dependency
  closure_effect = MAY permit book-source overlay closure (passes through the coverage-audit lens,
                   not automatically); the debt is recorded as a persistent named debt
  persistent_debt = true

objective_relevance_amendment
  trigger        = packet + review show the node is not in fact load-bearing for the declared objective
  old_status     = provisionally_load_bearing
  new_status     = non_load_bearing_for_declared_objective
  closure_effect = neutral ONLY after a falsifier review whose burden is to show the node IS essential
                   (verdict failed_to_show_nonessential keeps it load-bearing)

capacity_limit_amendment
  trigger        = the material is genuinely load-bearing but exceeds our safe normalization capacity now
  old_status     = load_bearing_pending
  new_status     = capacity_deferred
  closure_effect = BLOCKS full book_overlay_closed (the material is in the source and was not absorbed;
                   the failure is ours, not the book's)

load_bearing_discovery_amendment
  trigger        = a source packet reveals a previously undeclared indispensable node
  direction      = scope expansion only
  closure_effect = blocks book_overlay_closed until the node is classified and resolved
  requires       = independent governance order + exact source-grounded reason
  falsifier_task = try to absorb it into an existing LB node without loss
```

Closure must show **who fell short: the source or the project.** A `capacity_deferred` block is carried as a structured reason on the existing status, not as a new status word:

```text
overlay_status      = partial_overlay
overlay_block_reason = capacity_deferred(<amendment-id>)
```

This keeps the state vocabulary small (no `partial_overlay_governed` / `scope_reduced_by_capacity` proliferation) while the machine-readable reason carries the meaning.

---

## 4. Debt (persistent, never erased; a reference is not a settlement)

A named missing obligation is a stable entity with an append-only event log:

```text
DEBT-<SCOPE>-<TOPIC>-<NNN>
  events (append-only): identified_in_source -> routed_to_external_source -> packet_received
                        -> partially_normalized -> certificate_extracted -> adversarially_closed
  debt_resolution = unresolved | satisfied
  satisfied_by    = UNIT-ID | null
  resolution_review = REVIEW-ID | null
```

Settlement discipline — the governing inequalities:

```text
reference found   != debt paid
packet received   != debt paid
unit created      != debt paid
debt paid         =  named missing obligation closed by a trusted, closure-reviewed unit
                     that explicitly covers what the debt named
```

When a later book (e.g. Montgomery's "later volume" for the deferred zero-density / large-values material) arrives, its first debt event is `routed_to_external_source`, NOT `satisfied`. The debt entry is never deleted, even after settlement — a settled debt keeps its full event history and its `satisfied_by` / `resolution_review` pointers. Finding a bibliographic reference must never become the illusion of holding the certificate.

---

## 5. Book overlay vs declared-objective coverage (two separate axes)

Covering a book's material within its explicit bounds, and completing the certificate theory the project declared as this cycle's objective, are **different judgments**:

```text
book_overlay_closed  !=  declared_objective_coverage.complete  !=  mastery  !=  mathematical closure
```

There is no automatic implication `book_overlay_closed => declared_objective_coverage.complete`. The declared-objective axis is a structured field, not a computed flag:

```text
declared_objective_coverage:
  complete       = true | false
  blocking_debts = [DEBT-...]
```

`complete = true` is NOT a silent computed result of the last debt closing — it is an audited governance event: an independent **objective-coverage audit** (distinct from the overlay coverage audit), an adversarial review, then a separate governance order to flip it. Montgomery is the lived precedent: its book overlay is closed while the zero-density pillar remains incomplete in the mind (a source-boundary debt to a later volume).

---

## 6. Application-specific certificate record (`C_sieve`)

Any unit classified `application_specific_certificate` must carry a complete crossing-certificate record. Naming "we have Type II" is NOT a proof of assembly; the record is the assembly-proof barrier.

```text
C_sieve(A, T, D, B, L, E):
  A - sequence / family
  T - exact target (primes | asymptotic | lower bound | almost-primes | ...)
  D - decomposition identity / sieve weights
  B - bilinear certificate and its parameter ranges
  L - linear distribution / local-density certificate (level of distribution, local obstructions)
  E - complete error-budget closure

non-transfer fields (mandatory, above the record):
  external_input           (harmonic | spectral/automorphic | exponential sums | L-functions | ...)
  uniformity_range
  local_obstructions
  sequence_specific_features
  non_transfer_statement
  wall_remaining_outside_this_case
```

- **No empty field.** A field may hold the explicit value `not_applicable`, never a blank — blank conflates "does not apply" with "not examined".
- `not_applicable` is two-part: a machine-readable `reason_code` and a prose `reason_text` (e.g. `reason_code = TARGET_IS_PURE_UPPER_BOUND`, `reason_text = No bilinear prime-producing certificate is claimed in this unit.`).
- The guard forbids crossing / production / asymptotic language ("parity barrier crossed", "primes produced", "asymptotic established") whenever any `C_sieve` field is empty or unclosed. The historical exemption applies only when the same physical line carries both the historical marker and the claim — no paragraph, heading, neighbouring line, or ambient `legacy` exemption.

**Ceiling:** a complete application-specific certificate is a certificate for one sequence in named ranges — it is **not** a general crossing of the parity barrier, not an `MC-001` solution path, and not RH/GRH progress.

---

**Honest classification:** Governance / Coherence Policy. No RH progress. No GRH progress. No secured path.
