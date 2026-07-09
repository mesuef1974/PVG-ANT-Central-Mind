# State Coherence Policy

Registry ID: STATE-COHERENCE-POLICY-001 · Status: Active Governance · Classification: Governance / Coherence Policy.

The Central Mind must be **navigable**, not merely safe. A reader must be able to open the repository and immediately know: what is currently true, what is closed, what is partial, what is deferred, what is forbidden, what the next action is, and which claims are NOT being made.

## Three kinds of PASS

```text
Safety PASS    : no forbidden claims (no RH/GRH progress, no crossed wall, no solved missing certificate,
                 no prime detector, no parity break). Enforced by honesty_audit + forbidden_promotion_audit.
Coherence PASS : the mind's state is truthful and up to date — navigation files, registries, capability
                 maps, and book READMEs do not contradict the audits and unit files. Enforced by
                 state_coherence_audit.
Coverage PASS  : no central treasure was mined without being registered (per-book missed-treasures ledger).
```

A green Safety PASS alone is **not enough**. `PASS` must never mean only "we said nothing dangerous".

## Roles (Course Correction 005)

```text
ChatGPT     = mathematical treasure analyst and PVG/ANT interpreter. Supplies Treasure Packets.
Local agent = repository engineer, registry maintainer, guard runner, coherence auditor.
              Implements, organizes, normalizes, cross-links, audits, and guards the supplied treasures.
              Does NOT independently invent mathematical treasures. No new unit without a Treasure Packet.
```

## Book status vocabulary (registries/books.jsonl)

```text
available_not_imported  : registered book, no ledger content yet.
scope_open              : a scope opened, no unit executed.
partial_overlay         : some units mined; overlay in progress; mastery deferred.
unit_closed             : a single unit closure-reviewed.
phase_closed            : a version phase (e.g. v0.4) closure-reviewed.
book_overlay_closed     : the four-file treasure overlay closed for the book (mastery may be deferred).
mastery_deferred        : a marker; full-book proof/exercise coverage not claimed.
```

A book with unit files and passed closure audits must NOT be described as `scope_open` or `not_started`.

## Quarantine (pre-packet / unvalidated units)

A unit created before, or outside, the Treasure-Packet protocol — or otherwise not yet validated from source — is **quarantined**:

```text
- it EXISTS in the repository (reality is not denied),
- but it is NOT trusted as a mined treasure, NOT closure-reviewed, NOT promoted to closed / PASS,
- README, registry, and transition-memory MUST mark it quarantined / unvalidated / pre-packet,
- it is NOT eligible for its closure review until validated from source (ChatGPT Treasure Packet).
```

Current quarantine: **MNTII-006-E** (exists at HEAD; no v0.6-e-closure; pending source-grounded intake).

## Enforcement

`tools/state_coherence_audit.py` fails on stale-state contradictions (closure↔README, registry↔ledger, transition-memory truth, unit-existence↔"No unit X" phrases, and the quarantine markers). It is a **repository-truth checker**, not a mathematical-completeness checker. It joins the guard set (now seven).

**Ceiling (unchanged):** zero RH progress · zero GRH progress · no secured path.

**Honest classification:** Governance / Coherence Policy. No RH/GRH progress.
