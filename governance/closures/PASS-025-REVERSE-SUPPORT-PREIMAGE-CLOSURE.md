# PASS-025 — Reverse Support-Preimage Closure Review

```text
Closure ID: PASS-025-REVERSE-SUPPORT-PREIMAGE-CLOSURE-001
Goal ID: GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001
Date: 2026-07-22
Decision: CLOSED
Outcome: DEPTH_12_WITNESS_FOUND_WITHIN_FROZEN_CLASS
Stage decision: return
Return goal: GOAL-OP-ONE-THEOREM-001
PASS-026: NOT AUTHORIZED
```

## 1. Scope reviewed

PASS-025 was authorized as one fixed-cap reverse-preimage search after the closure of SYNTHESIS-001.

Its declared binary output was:

1. a forward-verified depth-12 prime-pair witness inside the frozen class; or
2. a finite absence certificate inside that class.

No adaptive cap increase, multi-axis expansion, or PASS-026 continuation was authorized.

## 2. Frozen configuration

The registered run used:

```text
target_prime_pair_closure_depth = 12
known_tail_support = {2,167071}
known_tail_support_closure_depth = 10
reverse_support_depth_budget = 1
predecessor_support_class = binary prime faces only
reverse_seed_integer_cap = 5,346,272
candidate_support_node_cap = 50,000
candidate_integer_cap = 10^12
prime_pair_realization_cap = 10^12
orbit_verification_depth_cap = 16
registered_top_witness_count = 25
```

The configuration is recorded in:

`governance/frozen-config/PASS-025-REVERSE-SUPPORT-PREIMAGE-FROZEN-CONFIG.md`.

## 3. Contamination accounting

A small reconnaissance preceded configuration freeze. It indicated that the reverse route was feasible and that a candidate could lie beyond the PASS-024 sum cap.

Therefore:

```text
registered run = confirmatory, exhaustive inside the frozen class, not blinded
```

No global minimality or discovery-priority claim is permitted.

## 4. Exact reverse mechanism

For a binary predecessor support:

\[
E=\{a,b\},
\]

all exact-support integers under the candidate cap have the form:

\[
m=a^i b^j,\qquad i,j\ge1.
\]

Because the registered predecessors are odd-prime faces, \(m\) is odd. A prime-pair realization must therefore be:

\[
m=2+(m-2).
\]

The preceding support is valid when:

\[
a+b=n,
\qquad
\operatorname{supp}(n)=\{2,167071\}.
\]

This yields:

\[
\{2,m-2\}\to\{a,b\}\to\{2,167071\}.
\]

The identities are exact consequences of the transition definition and unique factorization.

## 5. Bookkeeping correction

The exploratory prototype could incorrectly associate a predecessor support with more than one seed label.

The registered implementation stores:

```text
predecessor support {a,b} -> one seed a+b
```

and aborts if the same support is associated with different sums.

All registered predecessor supports reconstructed exactly one seed and mapped to the frozen tail.

## 6. Registered finite scope

```text
seed integers = 5
total distinct-prime seed representations = 35,936
unique binary predecessor supports = 35,936
predecessor supports with candidate integers = 14,500
exact-support candidate integers = 14,589
primality tests = 14,589
prime-producing witness candidates = 1,106
forward-verified promoted witnesses = 25
```

The predecessor count was below the frozen cap. No truncation occurred.

## 7. First witness inside the frozen class

The first witness under the frozen ranking is:

\[
\boxed{\{2,27397961\}}.
\]

Its sum is:

\[
27397963=41\cdot668243,
\]

so:

\[
\operatorname{supp}(27397963)=\{41,668243\}.
\]

The predecessor seed satisfies:

\[
41+668243=668284=2^2\cdot167071,
\]

and therefore:

\[
\operatorname{supp}(668284)=\{2,167071\}.
\]

## 8. Forward orbit certificate

\[
\begin{aligned}
\{2,27397961\}
&\to\{41,668243\}\\
&\to\{2,167071\}\\
&\to\{3,55691\}\\
&\to\{2,27847\}\\
&\to\{3,9283\}\\
&\to\{2,4643\}\\
&\to\{5,929\}\\
&\to\{2,467\}\\
&\to\{7,67\}\\
&\to\{2,37\}\\
&\to\{3,13\}\\
&\to\{2\}.
\end{aligned}
\]

Thus:

\[
\boxed{d_{\mathrm{closure}}(\{2,27397961\})=12}.
\]

This is a concrete finite instance under the registered transition law.

## 9. Minimality scope

The witness minimizes the exposing prime limit only inside:

- the frozen tail \(\{2,167071\}\);
- one reverse layer;
- binary predecessor supports;
- the five registered seed integers;
- the frozen integer and realization caps;
- the frozen ranking rule.

No global minimum depth-12 threshold is claimed.

## 10. Verification

```text
PVG Reverse Support-Preimage Audit = PASS
PASS-025 unit and regeneration tests = PASS
registered CLI certificate = PASS
goal-memory and return gate = PASS
PVG Inverse Geometry Audit = PASS
safe detached-worktree synchronization through PASS-025 = PASS
Governance Required Gate = PASS on the pre-closure active state
```

The committed certificate is:

`research/pvg-space-deepening/data/reverse-support-preimage-summary.json`.

## 11. Maturity review

```text
Exact reverse construction: L2 structural simplification
Bounded candidate-generation mechanism: L4 finite research mechanism
ANT transfer lemma: absent
New analytic estimate: absent
Original lemma: none certified
Original theorem: none certified
```

PASS-025 demonstrates a material computational role for PVG: it targets a deep orbit without scanning every represented sum up to the witness.

It does not yet demonstrate a proof-producing analytic role.

## 12. Knowledge return

Returned to the Central Mind:

1. reverse support-preimage generation;
2. exact predecessor-to-seed association;
3. frozen-class minimality discipline;
4. a concrete depth-12 orbit certificate;
5. evidence that deep finite witnesses may occur far beyond small forward caps;
6. the boundary between structural candidate generation and ANT estimation;
7. contamination accounting for confirmatory computational passes.

## 13. Stage decision

The Stage Review chooses:

```text
return
```

not `bounded_extension`.

Reasons:

- PASS-025 achieved its declared success criterion;
- the requested reverse mechanism is installed and reusable;
- another depth-only PASS would repeat the same maturity level;
- no transfer lemma or ANT estimate was produced;
- the governed mandatory return checkpoint is `GOAL-OP-ONE-THEOREM-001`.

## 14. Returned theorem-program state

After this closure:

```text
GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001 = closed
GOAL-OP-ONE-THEOREM-001 = active_external_validation_hold
PASS-026 = NOT AUTHORIZED
```

`ONE-LEMMA-TARGET-001` remains frozen. The external priority and proof requests remain sent and awaiting responses. No further packet may be sent without explicit owner authorization.

## 15. Scientific ceiling

PASS-025 does not prove:

- that the witness is globally first;
- unbounded closure depth;
- general termination;
- existence or nonexistence of a universal depth bound;
- an asymptotic threshold law;
- a new estimate for a representation function;
- a Goldbach theorem;
- historical originality;
- publication readiness;
- PNT, RH, or GRH progress.

**Honest classification:** closed finite computational mechanism with an exact depth-12 witness inside a frozen, explicitly contaminated class. No original lemma or theorem certified.
