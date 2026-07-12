# Appendix A — Governance Reliability

Purpose: evidence that the material in this packet was not selected or
promoted after results.

1. **Required merge gate.** Every change to `main` passes a CI gate running
   eleven core guards (honesty vocabulary, registry/markdown sync, state
   coherence, forbidden-promotion, duplicate-concept, citation, compass,
   legacy assets, continuity, source policy, outreach-deadline) plus the
   kernel, translation, benchmark, ontology, lemma-selection, and
   theorem-hold audit suites with deterministic-output checks
   (`git diff --exit-code` after every regenerator).
2. **No bypass.** Repository ruleset `governance-required` enforces the gate
   as a required status on `main` with strict up-to-date mode, empty bypass
   list, and owner bypass = never.
3. **Machine truth.** Registries (JSONL) are canonical; prose layers are
   audited against them. Every capability stage carries a machine-readable
   maturation receipt; receipts are append-only and historically immutable.
4. **Failure preservation.** Negative results, quarantined material, and
   named walls are registered and guarded against silent revival; an
   unresolved replication is recorded as UNRESOLVED, not as signal.
5. **Pre-registration discipline.** Dataset protocols are frozen before
   data; the external-review stopping protocol was recorded before any
   packet was sent; the outreach decision deadline is pinned inside its
   guard so the registry cannot renegotiate it.
6. **Honest scoring history.** Internal benchmark numbers are labeled
   registry coverage, never model performance; the first raw hidden-set
   score, once produced, is frozen immutable.

```text
zero RH progress · zero GRH progress · no secured path
```

**Classification:** Governance reliability appendix. No mathematical claim.
