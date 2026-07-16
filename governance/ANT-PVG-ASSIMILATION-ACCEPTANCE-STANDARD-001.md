# ANT–PVG Assimilation Acceptance Standard 001

Status: active specification
Classification: Governance / Cognitive Architecture
Branch: `agent/pvg-axis-sum-continuation-002`

## 1. Purpose

This standard defines when the Central Mind may honestly claim that a concept from analytic number theory has been assimilated.

A concept is not assimilated merely because its definition was copied, summarized, or mentioned. Assimilation requires a governed, reversible-as-far-as-possible translation package connecting the current analytic-number-theory formulation to Prime-Valuation Geometry, together with numerical examples and computational verification.

## 2. Mandatory assimilation packet

Every ANT concept must be represented by the packet:

```text
ANT_PVG_ASSIMILATION_PACKET
- object_id
- canonical_ANT_name
- canonical_definition
- equivalent_ANT_forms
- hypotheses_and_domain
- standard_examples
- counterexamples_or_boundary_cases
- dependencies
- theorem_lemma_conjecture_links
- ANT_to_PVG_map
- PVG_geometric_object
- preserved_information
- lost_information
- injectivity_status
- inverse_or_partial_inverse
- inverse_conditions
- PVG_to_ANT_return_map
- numerical_examples
- computational_checks
- formalization_status
- certificate_status
- common_failure_modes
- scientific_classification
- open_translation_questions
```

No field may be silently omitted. Unknown items must be marked `UNKNOWN`, `NOT_BUILT`, `NOT_PROVED`, or `NOT_APPLICABLE`.

## 3. Four required representations

A concept is not fully assimilated until it has all four representations:

1. **Current ANT representation** — accepted definitions, equivalent forms, hypotheses, and known theorem context.
2. **PVG representation** — the corresponding geometric object, observable, fiber, locus, channel, transform, or operator.
3. **Computational representation** — data structures, algorithms, finite examples, exact checks, and reproducible experiments.
4. **Cognitive representation** — dependencies, translation edges, certificates, errors, and reasoning routes inside the Research Memory Graph.

A fifth optional but preferred representation is:

5. **Formal representation** — Lean or another proof-assistant encoding when feasible.

## 4. Bidirectional translation requirement

For every translation `T : ANT -> PVG`, the packet must state:

```text
translation_type = exact_isomorphism | exact_embedding | quotient | projection | lossy_diagnostic | heuristic_analogy | absent
```

It must also state whether a return map `S : PVG -> ANT` exists and whether:

```text
S(T(x)) = x
```

holds exactly, modulo an equivalence relation, only on a restricted domain, approximately, or not at all.

Visual similarity is never accepted as proof of equivalence.

## 5. Numerical example requirement

Every assimilated definition must include numerical examples covering at least:

- a basic positive example;
- a nontrivial structural example;
- a boundary or exceptional case;
- a case exposing translation loss when loss exists.

The example must be computed in both languages where possible:

```text
integer / ANT side
-> valuation-vector / PVG side
-> translated observable
-> return check
```

## 6. Computational verification requirement

Every packet must define executable checks appropriate to its claim. Possible check classes include:

```text
exact_identity_check
finite_enumeration_check
round_trip_translation_check
rank_kernel_check
normalization_check
Euler_product_coefficient_check
Dirichlet_series_coefficient_check
residue_channel_check
numerical_error_bound_check
counterexample_search
regression_check
```

Computational verification is evidence for the tested range only. It does not promote a finite result to an asymptotic theorem or universal conjecture.

## 7. Theorem, lemma, and conjecture linkage

Definitions must not be isolated cards. Each packet must link the object to:

- theorems that use it;
- lemmas that construct or estimate it;
- conjectures in which it appears;
- known barriers and missing certificates;
- related PVG objects and translation paths.

The Research Memory Graph must therefore support paths such as:

```text
canonical definition
-> analytic tool
-> theorem or conjecture
-> PVG translation
-> geometric observable
-> certificate wall
```

## 8. Assimilation levels

```text
L0_MENTIONED
L1_DEFINED_IN_ANT
L2_TRANSLATED_TO_PVG
L3_BIDIRECTIONALLY_ANALYZED
L4_NUMERICALLY_VERIFIED
L5_COMPUTATIONALLY_REGRESSION_TESTED
L6_FORMALLY_VERIFIED
L7_BENCHMARKED_FOR_REASONING
```

The word `assimilated` without qualification is allowed only at level L4 or above. `Mastered` is not allowed until locked reasoning evaluation and certificate governance are complete.

## 9. Scientific ceiling

The standard prohibits:

- calling a PVG reformulation a new theorem;
- calling a geometric picture a proof;
- hiding loss in a translation;
- using examples as universal evidence;
- claiming inverse translation without injectivity or model restrictions;
- claiming novelty without literature review;
- claiming neural training readiness from documentation alone.

## 10. Operational rule

Every future ANT mining unit must produce, at minimum:

```text
1. canonical definition card
2. ANT -> PVG translation card
3. PVG -> ANT return analysis
4. numerical example set
5. computational check specification or implementation
6. RMG node and edge update
7. honest status and missing-certificate statement
```

## 11. Current state

```text
STANDARD = ACTIVE
RETROFIT_OF_EXISTING_UNITS = REQUIRED
AUTOMATED_PACKET_VALIDATOR = NOT_BUILT
FULL_ANT_COVERAGE = NOT_CLAIMED
NEURAL_TRAINING_CORPUS = NOT_AUTHORIZED
NEXT_ACTION = RMG-001-B
```
