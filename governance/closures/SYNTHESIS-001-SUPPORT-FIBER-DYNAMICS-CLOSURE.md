# SYNTHESIS-001 — Support-Fiber Dynamics Closure Review

```text
Closure ID: SYNTHESIS-001-SUPPORT-FIBER-DYNAMICS-CLOSURE-001
Goal ID: GOAL-OP-SUPPORT-FIBER-SYNTHESIS-001
Date: 2026-07-22
Decision: CLOSED
Next bounded operational goal: GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001 / PASS-025
Mandatory return checkpoint: GOAL-OP-ONE-THEOREM-001
```

## 1. Scope reviewed

SYNTHESIS-001 was authorized to consolidate PASS-013 through PASS-024 without opening a new computation or claiming a theorem.

The required deliverable was:

- common notation;
- exact propositions from the transition definition;
- simple numerical examples;
- full-valuation versus support-projection loss map;
- PASS-013–024 theory map;
- exact/finite/open classification matrix;
- reverse links to ANT;
- governed next questions.

## 2. Deliverables

Completed:

- `research/pvg-space-deepening/synthesis-001-support-fiber-dynamics.md`;
- `tests/test_pvg_support_fiber_synthesis.py`;
- `.github/workflows/pvg-support-fiber-synthesis-audit.yml`;
- integration into `tools/sync_pvg_inverse_geometry_worktree.ps1`;
- goal-memory, Research Compass, and detached-worktree verification.

## 3. Exact reusable results

The synthesis freezes the following exact statements.

1. For a finite prime face \(S\),

\[
\mathcal T(S)=\{\operatorname{supp}(a+b):a,b\in S,\ a<b\}
\]

is a family of successor faces.

2. For a binary face,

\[
\mathcal T(\{p,q\})=\{\operatorname{supp}(p+q)\}.
\]

3. Equal sums give equal orbit tails from depth 1.

4. Equal supports of sums give equal orbit tails from depth 1.

5. For distinct primes \(p,q\),

\[
\{p,q\}\cap\operatorname{supp}(p+q)=\varnothing.
\]

6. The numerical preimage of an exact support \(F\) consists of products of positive powers of all primes in \(F\), with no outside prime.

These are identities or known consequences of unique factorization and parity. No historical originality claim is made.

## 4. Information-loss result

The synthesis records explicitly that:

\[
\nu(n)\mapsto\operatorname{supp}(n)
\]

loses exponent information. Therefore PASS-013–024 study a support-projected system, not the full additive geometry of valuation vectors.

This prevents the support-face program from silently replacing the larger PVG-foundations goal.

## 5. Finite evidence retained

The synthesis registers, without promotion:

- the finite atlases and basin geometry at prime limit 100;
- the fixed-depth wall and exact depth-six threshold at 359;
- the sum-706 depth-six family;
- the support-fiber threshold ladder through depth 11 under the PASS-024 sum cap;
- absence of depth 12 only through the registered cap;
- the distinction between endpoint-signature stabilization and bounded orbit closure.

Every such statement remains finite and cap-dependent.

## 6. ANT reverse translation

The synthesis separates:

```text
representation multiplicity r_2(N)
from
geometric class = orbit of supp(N)
```

It connects the first layer to additive convolution and the weighted function:

\[
R_\Lambda(N)=\sum_{a+b=N}\Lambda(a)\Lambda(b),
\]

and identifies support/orbit-stratified averages as candidate research objects.

No analytic estimate, cancellation lemma, circle-method improvement, or Goldbach result was produced.

## 7. Verification

```text
PVG Support-Fiber Synthesis Audit = PASS
support-fiber synthesis tests = PASS
Research Compass Audit = PASS
Goal Memory and Traceability Audit = PASS
PVG Inverse Geometry Audit = PASS
safe detached-worktree synchronization = PASS
State Coherence / Honesty / Continuity = PASS on the governing state
```

The initial test failure was a test-interface error: `factor_support` had been imported under the obsolete name `support`. It was corrected without changing the mathematics.

## 8. Maturity review

```text
Vocabulary and definitions: L1-L2 complete for the declared support system
Structural simplification: L2 achieved
Transfer principle: not yet certified at L3
Research mechanism: support-fiber compression is a finite algorithmic mechanism
Original lemma: none certified
Original theorem: none certified
```

## 9. Goal service and knowledge return

SYNTHESIS-001 served:

- `GOAL-PVG-ADDITIVE-DYNAMICS-001` by unifying its objects and boundaries;
- `GOAL-PVG-ANT-ADDITIVE-BRIDGE-001` by providing reverse representation-language links;
- `GOAL-PVG-FOUNDATIONS-001` by preserving the distinction between full valuations and support;
- `GOAL-GOVERNANCE-MEMORY-001` by recording exact, finite, and open layers;
- `GOAL-PVG-ANT-ORIGINALITY-001` by converting the experiment chain into bounded questions.

Reusable knowledge returned:

- binary-face transition identity;
- sum/support fiber identity;
- support preimage characterization;
- loss map;
- finite/open claim matrix;
- PASS-025 ranked question set.

## 10. Stage Review decision

Decision type:

```text
bounded_extension
```

Authorized next goal:

```text
GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001
PASS-025 — Reverse Support-Preimage Generator
```

Reason:

- it follows directly from the exact preimage characterization;
- it replaces blind bound expansion with targeted reverse generation;
- it has a measurable binary outcome: depth-12 witness or finite negative certificate;
- its scope and stop rule are already registered.

## 11. Return gate

The bounded extension does not authorize PASS-026.

After PASS-025, the project must perform a Stage Review that chooses one of:

1. return to `GOAL-OP-ONE-THEOREM-001`;
2. close the additive-dynamics parent with a certificate;
3. authorize one newly bounded extension with explicit evidence and stop rule.

The theorem program remains paused, not cancelled.

## 12. Scientific ceiling

SYNTHESIS-001 does not establish:

- general termination;
- a universal closure-depth bound;
- unbounded depth;
- an asymptotic depth law;
- historical originality;
- a new ANT estimate;
- Goldbach, PNT, RH, or GRH progress;
- publication readiness.

**Honest classification:** closed synthesis of exact definitions, known identities, finite verified evidence, diagnostic reinterpretation, and open research questions. No original theorem certified.
