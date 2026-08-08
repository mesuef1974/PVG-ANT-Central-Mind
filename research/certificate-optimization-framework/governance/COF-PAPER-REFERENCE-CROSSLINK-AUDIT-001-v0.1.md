# COF-PAPER-REFERENCE-CROSSLINK-AUDIT-001

## Status

`PASS_WITH_SCOPED_LIMITS`

This audit links every mathematical claim in `paper/COF-FOUNDATIONS-DRAFT-v0.2.md` to one of three evidence layers:

1. abstract proof source;
2. Fourier/PVG realization source;
3. executable or JSON verification receipt.

The layers are not interchangeable. Finite verification does not replace proof, and abstract proof does not validate implementation.

---

## 1. Abstract theorem crosslinks

| Paper item | Claim | Abstract source | Evidence class |
|---|---|---|---|
| Definition 2.1 | finite certificate optimization structure | `theory/COF-ADDITIVE-CERTIFICATE-STRUCTURE-v0.1.md` | definition |
| Definition 2.2 | additive representation `L_S=beta+sum Gamma` | `theory/COF-ADDITIVE-CERTIFICATE-STRUCTURE-v0.1.md` | definition |
| Theorem 3.1 | monotonicity under `Gamma>=0` | `theory/COF-ADDITIVE-CERTIFICATE-STRUCTURE-v0.1.md` | exact proof |
| Theorem 3.3 | feasibility-preserving dominance exchange | `theory/COF-ADDITIVE-CERTIFICATE-STRUCTURE-v0.1.md`; repaired assumptions in `governance/COF-PAPER-PROOF-AUDIT-v0.1.md` | exact proof |
| Definition 3.4 | precedence exchange system | `theory/COF-ADDITIVE-CERTIFICATE-STRUCTURE-v0.1.md`; termination repair in `governance/COF-PAPER-PROOF-AUDIT-v0.1.md` | definition plus repair |
| Theorem 3.5 | existence of a precedence-legal optimum | same sources as Definition 3.4 | exact finite proof |
| Boundary 3.6 | dominance is not deletion | `theory/COF-ADDITIVE-CERTIFICATE-STRUCTURE-v0.1.md` | exact boundary/counterexample principle |
| Definition 4.2 | admissible node upper bound | `theory/COF-EXACT-BRANCH-AND-BOUND-AND-PRECEDENCE-v0.1.md` | definition |
| Theorem 4.3 | safe pruning | same source | exact proof |
| Theorem 4.4 | exactness of finite Branch-and-Bound | same source | exact proof |
| Definition 5.1 | exact-`b` coordinatewise top sum | `theory/COF-EXACT-BRANCH-AND-BOUND-AND-PRECEDENCE-v0.1.md`; signed correction in `governance/COF-PAPER-PROOF-AUDIT-v0.1.md` | definition plus repair |
| Theorem 5.2 | signed exact-cardinality upper bound | same sources | exact finite proof |
| Corollary 5.3 | at-most-`b` upper bound | same sources | exact finite proof |
| Section 6 | precedence propagation and infeasibility closures | `theory/COF-EXACT-BRANCH-AND-BOUND-AND-PRECEDENCE-v0.1.md` | exact proof |
| Definition 7.1 | sound mandatory set | `theory/COF-MANDATORY-CLOSURES-AND-MINIMAL-OBSTRUCTIONS-v0.1.md` | definition |
| Theorem 7.2 | leave-one-out mandatory test | same source; exact/at-most budget correction in `governance/COF-PAPER-PROOF-AUDIT-v0.1.md` | exact finite proof |
| Proposition 7.3 | precedence closure preserves mandatory soundness | same source | exact proof |
| Theorem 8.2 | actual simultaneous certification implies mandatory compatibility | same source | exact proof |
| Corollary 8.3 | mandatory-union value is an admissible upper bound | same source | exact proof |
| Definition 8.4 | pairwise compatibility graph and coloring bound | same source | exact relaxation proof |
| Definition 8.5 | mandatory-conflict hypergraph | same source | exact relaxation definition |
| Theorem 9.1 | minimal-obstruction characterization | same source | exact finite proof |
| Corollary 9.2 | exact antichain compression of the relaxation | same source | exact finite proof |

The dependency classification for these items is recorded in:

- `governance/COF-THEOREM-DEPENDENCY-MATRIX-v0.1.md`.

---

## 2. Fourier realization crosslinks

| Paper statement | Primary realization source |
|---|---|
| reduced local channel Fourier decomposition | `research/avrg-axis-sum/theory/LOCAL-CHANNEL-FOURIER-DECOMPOSITION-v1.2.md` |
| effective period reduction | `research/avrg-axis-sum/theory/EFFECTIVE-PERIOD-REDUCED-FOURIER-THEOREM-v1.2.md` |
| reduced major/minor frequency split | `research/avrg-axis-sum/theory/REDUCED-MAJOR-MINOR-FREQUENCY-SPLIT-v1.2.md` |
| retained-frequency lower-bound construction | `research/avrg-axis-sum/theory/EXACT-FREQUENCY-RETENTION-BUDGET-OPTIMIZER-v1.2.md` |
| exact Branch-and-Bound realization | `research/avrg-axis-sum/theory/EXACT-FREQUENCY-RETENTION-BRANCH-AND-BOUND-v1.2.md` |
| componentwise frequency dominance | `research/avrg-axis-sum/theory/FREQUENCY-DOMINANCE-PRECEDENCE-CONSTRAINT-v1.2.md` |
| precedence-aware exact search | `research/avrg-axis-sum/theory/PRECEDENCE-AWARE-EXACT-BRANCH-AND-BOUND-v1.0.md` |
| precedence-aware upper bound | `research/avrg-axis-sum/theory/PRECEDENCE-AWARE-UPPER-BOUND-v1.0.md` |
| certification-margin mandatory sets | `research/avrg-axis-sum/theory/CERTIFICATION-MARGIN-AWARE-PRUNING-v1.0.md` |
| mandatory compatibility hypergraph | `research/avrg-axis-sum/theory/HYPERGRAPH-COMPATIBILITY-CERTIFICATION-v1.0.md` |
| minimal forbidden hyperedges | `research/avrg-axis-sum/theory/MINIMAL-FORBIDDEN-CHANNEL-HYPEREDGES-v1.0.md` |

### Realization identity used in the paper

The paper uses

\[
L_S(c)=\beta(c)+\sum_{k\in S}G_k(c),
\qquad
G_k(c)=P_k(c)+|P_k(c)|\ge 0.
\]

The exact notation and indexing must remain synchronized with:

- `research/avrg-axis-sum/governance/NOTATION.md`;
- `research/avrg-axis-sum/theory/EXACT-FREQUENCY-RETENTION-BUDGET-OPTIMIZER-v1.2.md`;
- `research/avrg-axis-sum/theory/EXACT-FREQUENCY-RETENTION-BRANCH-AND-BOUND-v1.2.md`.

The arithmetic baseline and contamination threshold depend on:

- `research/avrg-axis-sum/theory/VON-MANGOLDT-ADDITIVE-FIBER-OBSERVABLES-v1.2.md`;
- `research/avrg-axis-sum/theory/HIGHER-PRIME-POWER-CONTAMINATION-BOUND-v1.2.md`;
- `research/avrg-axis-sum/theory/LOCAL-CHANNEL-HPP-CONTAMINATION-BOUND-v1.2.md`.

---

## 3. Executable evidence crosslinks

| Claimed implementation property | Executable | JSON receipt |
|---|---|---|
| exact budget optimizer matches exhaustive search | `research/avrg-axis-sum/code/verify_exact_frequency_retention_budget_optimizer.py` | `research/avrg-axis-sum/results/exact_frequency_retention_budget_optimizer_verification_v1.2.json` |
| Branch-and-Bound matches exhaustive optimum | `research/avrg-axis-sum/code/verify_exact_frequency_retention_branch_and_bound.py` | `research/avrg-axis-sum/results/exact_frequency_retention_branch_and_bound_verification_v1.2.json` |
| dominance/precedence checks | `research/avrg-axis-sum/code/verify_frequency_dominance_precedence_constraint.py` | `research/avrg-axis-sum/results/frequency_dominance_precedence_verification_v1.2.json` |
| precedence-aware exact search | `research/avrg-axis-sum/code/verify_precedence_aware_exact_branch_and_bound.py` | `research/avrg-axis-sum/results/precedence_aware_exact_branch_and_bound_verification_v1.0.json` |
| precedence-aware upper bound | `research/avrg-axis-sum/code/verify_precedence_aware_upper_bound.py` | `research/avrg-axis-sum/results/precedence_aware_upper_bound_verification_v1.0.json` |
| mandatory-set and margin-aware pruning | `research/avrg-axis-sum/code/verify_certification_margin_aware_pruning.py` | `research/avrg-axis-sum/results/certification_margin_aware_pruning_verification_v1.0.json` |
| hypergraph relaxation | `research/avrg-axis-sum/code/verify_hypergraph_compatibility_certification.py` | `research/avrg-axis-sum/results/hypergraph_compatibility_certification_v1.0.json` |
| minimal-obstruction compression | `research/avrg-axis-sum/code/verify_minimal_forbidden_channel_hyperedges_optimized.py` | `research/avrg-axis-sum/results/minimal_forbidden_channel_hyperedges_verification_v1.1.json` |
| independent arithmetic observable / false-certificate check | `research/avrg-axis-sum/code/verify_von_mangoldt_additive_fiber_observables.py` | `research/avrg-axis-sum/results/von_mangoldt_additive_fiber_verification_v1.2.json` |
| local higher-prime-power threshold | `research/avrg-axis-sum/code/verify_local_channel_hpp_contamination_bound.py` | `research/avrg-axis-sum/results/local_channel_hpp_contamination_bound_verification_v1.2.json` |

### Benchmark numbers authorized for manuscript use

The manuscript may state only benchmark claims explicitly tied to the corresponding receipt. Current authorized examples include:

- `12,987` optimization cases for the precedence/margin/hypergraph benchmark range;
- zero optimum mismatches in the relevant exact-search receipts;
- zero false prime-pair certificates in the corresponding independent observable checks;
- mandatory-margin node counts `65,971 -> 65,209` only when citing the margin-aware receipt;
- hypergraph node counts `65,209 -> 65,191` only when citing the hypergraph receipt;
- minimal-obstruction compression counts only when copied directly from the v1.1 minimal-hyperedge receipt.

The abstract COF paper should avoid crowding the main theorem statements with benchmark-specific counts. Such counts belong in a realization or computational-evidence subsection.

---

## 4. Scope corrections carried into the manuscript

The following boundaries are mandatory:

1. mandatory compatibility is necessary, not sufficient, for actual simultaneous certification;
2. `U_mand` is exact for the mandatory-set relaxation, not necessarily for the original certification problem;
3. every forbidden family contains at least one minimal obstruction, not a unique one;
4. Branch-and-Bound exactness is a theorem about admissible bounds and comprehensive branching, not about a particular heuristic;
5. finite exhaustive agreement validates the implementation only on the stated range;
6. no Goldbach, RH, GRH, polynomial-time, uniform-speedup, or universal-transferability claim is authorized.

---

## 5. Audit result

```text
ABSTRACT THEOREM CROSSLINKS = PASS
FOURIER REALIZATION CROSSLINKS = PASS
EXECUTABLE RECEIPT CROSSLINKS = PASS
SCOPE BOUNDARIES = PASS
SECOND INDEPENDENT APPLICATION = ABSENT
TRANSFERABILITY CLAIM = NOT AUTHORIZED
LATEX TRANSCRIPTION GATE = OPEN
SUBMISSION GATE = CLOSED
```

The next permitted action is transcription of `COF-FOUNDATIONS-DRAFT-v0.2.md` into LaTeX with stable theorem labels and internal references. Bibliographic positioning and compilation remain separate gates.