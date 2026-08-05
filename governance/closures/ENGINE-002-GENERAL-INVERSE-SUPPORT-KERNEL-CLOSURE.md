# ENGINE-002 — General Inverse Support Kernel Closure Review

```text
Closure ID: ENGINE-002-GENERAL-INVERSE-SUPPORT-KERNEL-CLOSURE-001
Goal ID: GOAL-OP-INVERSE-SUPPORT-KERNEL-001
Date: 2026-07-22
Decision: CLOSED
Stage decision: return
Return goal: GOAL-OP-ONE-THEOREM-001
Phase B: NOT AUTHORIZED
Depth search: NOT AUTHORIZED
```

## 1. Scope closed

ENGINE-002 was authorized to build Phase A of the inverse geometry engine inside one frozen finite box:

```text
target prime limit = 31
predecessor prime limit = 31
predecessor face sizes = 2,3,4
maximum target face size = 4
```

No adaptive expansion was authorized.

## 2. Exact results returned

### Witness-edge law

\[
F\in\mathcal T(E)
\iff
E\text{ contains a pair }\{a,b\}\text{ with }\operatorname{supp}(a+b)=F.
\]

### Support-fiber law

Witness sums lie among:

\[
\prod_{r\in F}r^{e_r},\qquad e_r\ge1,\qquad n\le2P.
\]

### Parity routing

```text
2 in F     → odd + odd witnesses
2 not in F → 2 + odd witnesses
```

### Radical and axis exclusion

Inside a prime universe bounded by \(P\):

\[
\operatorname{rad}(F)>2P
\quad\text{or}\quad
\max(F)>2P
\]

implies no witness edge in the box.

## 3. Implementation delivered

- `tools/pvg_inverse_support_kernel.py`;
- `tests/test_pvg_inverse_support_kernel.py`;
- `research/pvg-space-deepening/engine-002-general-inverse-support-kernel.md`;
- `research/pvg-space-deepening/data/inverse-support-kernel-summary.json`;
- `.github/workflows/pvg-inverse-support-kernel-audit.yml`.

The API includes:

```text
successors(face)
witness_edges(target, prime_limit)
predecessors(target, prime_limit, face_sizes)
predecessor_certificate(target, predecessor)
reachability_table(...)
```

## 4. Finite-box certificate

```text
prime axes = 11
predecessor faces = 550
forward pair evaluations = 2530
target faces = 561
reachable targets = 20
unreachable targets inside box = 541
```

Reachable target sizes:

```text
size 1 = 7
size 2 = 11
size 3 = 2
size 4 = 0
```

Predecessor incidences:

```text
size 2 = 55
size 3 = 457
size 4 = 1656
```

## 5. Verification

The compressed generator was compared against independent complete forward enumeration for all 561 targets.

```text
soundness = PASS
completeness inside frozen box = PASS
deduplication = PASS
determinism = PASS
multi-axis sizes 3 and 4 = PASS
registered certificate regeneration = PASS
```

The mathematical and certificate steps of the dedicated CI gate passed before closure. Governance failures encountered during integration were state-link synchronization issues, not failures of the inverse kernel.

## 6. Maturity

```text
Exact inverse-support identities = L1
Structural search compression = L2
Finite complete inverse-support kernel = L2-L3 infrastructure
Analytic transfer principle = absent
Original ANT lemma = absent
```

## 7. Knowledge return

ENGINE-002 returns to the long-term inverse geometry goal:

- witness-edge graph model;
- exact support-fiber generator;
- parity routing;
- radical exclusion;
- general multi-axis predecessor API;
- finite reachable/unreachable certificates;
- a deterministic data contract.

It also returns to the theorem program a possible future tool, but no current theorem step requires Phase B.

## 8. Stage decision

```text
return
```

The active operational front returns to:

`GOAL-OP-ONE-THEOREM-001`.

Phase B — Inverse Integer Fibers is not opened. It requires a new readiness card and a named theorem or transfer need.

## 9. Ceiling

This closure proves no global reachability or unreachability, no termination theorem, no depth-growth theorem, and no result in Goldbach, PNT, RH, or GRH.

**Honest classification:** closed exact finite-box inverse-support infrastructure; no original ANT theorem.
