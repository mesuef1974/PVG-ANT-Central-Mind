# RMG-001-A — Research Memory Graph Core Ontology and Typed Translation Edges

Status: specification complete / graph population not yet executed

Classification: Architecture

Validation status: ontology_defined_not_instantiated

Branch: `agent/pvg-axis-sum-continuation-002`

Parent charter: `governance/NUMBER-THEORY-RESEARCH-MIND-CHARTER-001.md`

## 1. Mission

Build the core ontology for a durable Research Memory Graph that can absorb analytic number theory, represent Prime-Valuation Geometry, and encode precise bidirectional translations between them.

The graph is not a document index. It is the semantic backbone of a future specialist research mind and a possible future neural-symbolic system.

Goldbach is one application domain among many. The graph must support the wider landscape of analytic number theory, including:

- arithmetic functions;
- Dirichlet series and Euler products;
- prime distribution;
- characters and L-functions;
- additive number theory;
- sieve methods;
- exponential sums;
- zero-density and large-value methods;
- Tauberian and contour methods;
- probabilistic number theory;
- spectral/operator viewpoints;
- computational and formal verification layers;
- PVG observables and geometric translations.

## 2. Governing principle

Every mathematical object must be represented through the Geometry–Analysis–Certificate triangle:

```text
GEOMETRY
what structure appears in valuation space?

ANALYSIS
how does the object appear in sums, series, products, transforms, estimates, and limiting laws?

CERTIFICATE
what is known, what is inferred, what is missing, and what may be claimed?
```

No node is considered research-ready unless these three aspects are either populated or explicitly marked missing.

## 3. Node classes

The graph must support at least the following typed node classes.

### 3.1 Mathematical object nodes

```text
INTEGER_OBJECT
PRIME_OBJECT
ARITHMETIC_FUNCTION
VALUATION_VECTOR
ADDITIVE_FIBER
RESIDUE_CLASS
CHARACTER
DIRICHLET_SERIES
EULER_PRODUCT
L_FUNCTION
GENERATING_FUNCTION
EXPONENTIAL_SUM
OPERATOR
KERNEL
SPECTRUM
MEASURE
DISTRIBUTION
ASYMPTOTIC_FORMULA
ERROR_TERM
```

### 3.2 Method nodes

```text
CIRCLE_METHOD
SIEVE_METHOD
CHARACTER_SUM_METHOD
TAUBERIAN_METHOD
CONTOUR_METHOD
ZERO_DENSITY_METHOD
LARGE_VALUES_METHOD
FOURIER_METHOD
SPECTRAL_METHOD
PROBABILISTIC_METHOD
COMPUTATIONAL_METHOD
FORMAL_PROOF_METHOD
PVG_TRANSLATION_METHOD
COF_METHOD
```

### 3.3 Statement nodes

```text
IDENTITY
LEMMA
THEOREM
CONJECTURE
CONDITIONAL_STATEMENT
FINITE_VERIFICATION
HEURISTIC
DIAGNOSTIC
NO_GO_RESULT
BOUNDARY_STATEMENT
```

### 3.4 Certificate nodes

```text
IDENTITY_CERTIFICATE
FINITE_COMPUTATION_CERTIFICATE
FORMAL_PROOF_CERTIFICATE
ASYMPTOTIC_CERTIFICATE
UNIFORM_ERROR_CERTIFICATE
POSITIVITY_CERTIFICATE
RANK_CERTIFICATE
KERNEL_CERTIFICATE
STABILITY_CERTIFICATE
LITERATURE_CERTIFICATE
NOVELTY_CERTIFICATE
REPRODUCIBILITY_CERTIFICATE
GOVERNANCE_CERTIFICATE
```

### 3.5 Source and provenance nodes

```text
BOOK
PAPER
CHAPTER
SECTION
DATASET
EXPERIMENT
LEAN_FILE
SCRIPT
WORKFLOW
UNIT
SKILL
TOOL
AUDIT
DECISION
ERROR_RECORD
```

### 3.6 PVG-specific nodes

```text
PVG_POINT
PVG_SUPPORT
PVG_HEIGHT
PVG_MASS
PVG_EDGE
PVG_DIVISOR_BOX
PVG_PHASE
PVG_FIBER
PVG_CHANNEL
PVG_TRANSLATION_RULE
PVG_OBSERVABLE
PVG_WALL
```

## 4. Mandatory node fields

Every node must carry:

```text
node_id
node_type
canonical_name
short_definition
status
classification
source_provenance
created_by
created_at
last_reviewed_at
scientific_ceiling
confidence_vector
validation_state
```

Optional but strongly preferred fields:

```text
notation
aliases
input_contract
output_contract
assumptions
domain
normalization
known_results
open_questions
pvg_view
ant_view
certificate_present
certificate_missing
error_links
benchmark_links
formalization_links
computational_links
```

Unknown fields must be marked explicitly rather than omitted when omission could be mistaken for evidence.

## 5. Typed edge classes

The graph must use typed, directional edges.

### 5.1 Dependency edges

```text
DEPENDS_ON
REQUIRES
USES
PROVED_BY
CERTIFIED_BY
VALIDATED_BY
IMPLEMENTED_BY
BENCHMARKED_BY
FORMALIZED_BY
COMPUTED_BY
```

### 5.2 Translation edges

```text
TRANSLATES_TO
TRANSLATES_FROM
PVG_REALIZES
ANT_REALIZES
GEOMETRIC_IMAGE_OF
ANALYTIC_IMAGE_OF
PRESERVES
LOSES_INFORMATION
REFINES
COARSENS
DUAL_TO
FOURIER_DUAL_OF
GENERATES
ENCODES
DECODES
```

### 5.3 Logical edges

```text
IMPLIES
DOES_NOT_IMPLY
EQUIVALENT_TO
CONDITIONAL_ON
CONTRADICTS
GENERALIZES
SPECIALIZES
APPROXIMATES
BOUNDED_BY
OBSTRUCTED_BY
```

### 5.4 Research-state edges

```text
EXTENDS
SUPERSEDES
CORRECTS
INVALIDATES
QUARANTINES
REOPENS
CLOSES
RISKS
MISSING_CERTIFICATE_FOR
NEXT_ACTION_FOR
```

### 5.5 Provenance edges

```text
EXTRACTED_FROM
CITED_BY
DISCUSSED_IN
RECORDED_IN
AUTHORED_IN
AUDITED_IN
```

## 6. Translation edge contract

A translation edge between ANT and PVG is invalid unless it records:

```text
source_object
target_object
translation_direction
translation_rule
preserved_information
lost_information
required_assumptions
normalization
inverse_available
inverse_conditions
certificate_type
scientific_classification
```

### 6.1 Translation classifications

Every translation is classified as exactly one of:

```text
EXACT_BIJECTION
EXACT_INJECTION
EXACT_SURJECTION
EXACT_IDENTITY_REWRITE
LOSSY_PROJECTION
COARSE_DIAGNOSTIC
STATISTICAL_CORRESPONDENCE
CONDITIONAL_TRANSLATION
HEURISTIC_ANALOGY
UNVALIDATED_CANDIDATE
```

No analogy may be represented as an equivalence.

## 7. Canonical ANT ↔ PVG translation template

For each analytic-number-theory concept, the graph should attempt to populate:

```text
ANT_OBJECT
- classical definition
- standard notation
- generating series or transform
- known main term
- known error term
- known theorem status
- unresolved wall

PVG_TRANSLATION
- valuation-space carrier
- support geometry
- height or mass observable
- edge or fiber structure
- phase or residue structure
- information preserved
- information lost

CERTIFICATE
- exact identity available?
- analytic estimate available?
- inverse translation available?
- finite verification available?
- formal proof available?
- publication-level claim allowed?
```

## 8. Required translation families

The first graph population program must eventually cover at least these families.

### 8.1 Multiplicative structure

```text
integer multiplication
↔ valuation-vector addition

gcd / lcm
↔ coordinatewise minimum / maximum

divisibility
↔ partial order in valuation space

multiplicative functions
↔ observables on valuation geometry
```

### 8.2 Dirichlet-series structure

```text
arithmetic function
↔ weighted PVG observable

Dirichlet series
↔ transform of valuation-space weights

Euler product
↔ prime-axis factorization

logarithmic derivative
↔ prime-power weighted observable
```

### 8.3 Additive structure

```text
a+b=N
↔ addition fiber transported into valuation space

weighted convolution
↔ weighted PVG fiber observable

residue classes
↔ modular channels

Fourier coefficients
↔ channel spectrum
```

### 8.4 Prime-distribution structure

```text
pi(x), theta(x), psi(x)
↔ cumulative PVG observables under declared truncation

prime density
↔ local support-density diagnostics

prime powers
↔ axis-height strata
```

### 8.5 Character and L-function structure

```text
Dirichlet character
↔ phase label on residue/PVG channels

L-function
↔ character-weighted transform

zero information
↔ analytic certificate layer, not automatically geometric proof
```

### 8.6 Sieve structure

```text
sifted set
↔ forbidden-support or residue-filter geometry

sieve weights
↔ signed observables on PVG loci

parity barrier
↔ certificate wall, not merely a visual obstruction
```

### 8.7 Probabilistic structure

```text
additive function distribution
↔ distribution of PVG observables

normal order
↔ typical valuation-geometry behavior

exceptional set
↔ low-density geometric locus
```

## 9. Translation-quality dimensions

Each translation receives a quality vector:

```text
mathematical_exactness
information_preservation
inverse_recoverability
normalization_clarity
certificate_strength
computational_testability
formalizability
literature_support
reuse_value
```

A high score in visual intuitiveness cannot compensate for a low score in mathematical exactness.

## 10. Neural-symbolic readiness

The graph is intended to support a future neural or neural-symbolic architecture, but it is not yet a training corpus.

Required future export properties:

```text
stable node identifiers
stable edge identifiers
typed relations
provenance-preserving chunks
positive and negative examples
certificate labels
error labels
confidence vectors
dependency subgraphs
reasoning traces
```

Training authorization remains separate. No hidden benchmark keys, private custody material, or uncertified claims may enter a future corpus automatically.

## 11. Anti-collapse rules

The graph must reject:

```text
PVG reformulation = ANT theorem
finite experiment = asymptotic statement
visual similarity = mathematical equivalence
Euler product notation = proof of prime distribution
Fourier representation = positivity theorem
high confidence in computation = high confidence in generalization
absence of known counterexample = proof
unregistered analogy = translation rule
```

## 12. First population seed

The first seed subgraph should contain:

```text
Prime-Valuation Geometry
Arithmetic Function
von Mangoldt Function
Dirichlet Series
Euler Product
Addition Fiber
Difference Channel
Finite Fourier Transform
Rank
Kernel
Certificate Optimization Framework
Goldbach Diagnostic
Scientific Ceiling
```

Canonical dependency examples:

```text
Difference Channel DEPENDS_ON Addition Fiber
Finite Fourier Transform ANALYZES Difference Channel
Rank CERTIFIES reconstruction feasibility
Kernel OBSTRUCTS unique reconstruction
COF USES retained measurements and target certificates
Goldbach Diagnostic USES Addition Fiber
Goldbach theorem claim MISSING_CERTIFICATE_FOR all-target positivity
```

## 13. Completion criteria

RMG-001-A is complete when:

1. core node classes are defined;
2. typed edge classes are defined;
3. translation edges require preservation/loss metadata;
4. provenance and scientific ceilings are mandatory;
5. neural-symbolic readiness is anticipated without authorizing training;
6. Goldbach is represented as one application subgraph, not the whole graph;
7. no populated graph or autonomous competence is falsely claimed.

## 14. Honest state

```text
RMG-001-A = SPECIFICATION_COMPLETE
CORE_ONTOLOGY = DEFINED
TYPED_EDGE_SCHEMA = DEFINED
TRANSLATION_CONTRACT = DEFINED
GRAPH_DATABASE = NOT_BUILT
SEED_GRAPH = NOT_POPULATED
AUTOMATED_EXTRACTION = NOT_BUILT
NEURAL_TRAINING_CORPUS = NOT_AUTHORIZED
AUTONOMOUS_NUMBER_THEORY_MIND = NOT_VALIDATED
GOLDBACH_PROGRESS = NONE
RH_GRH_PROGRESS = NONE
```

## 15. Next action

```text
NEXT_ACTION = RMG-001-B
TITLE = Seed Graph for ANT ↔ PVG Core Translation Families
```

RMG-001-B should instantiate the first governed nodes and edges from existing project units and book ledgers, with explicit provenance and no fabricated equivalences.
