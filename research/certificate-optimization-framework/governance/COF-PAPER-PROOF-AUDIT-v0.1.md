# COF Paper Proof Audit v0.1

## Scope

This audit reviews `COF-FOUNDATIONS-DRAFT-v0.1.md` theorem by theorem before LaTeX conversion. It checks logical sufficiency, assumption minimality, distinction between the original certification problem and its relaxations, and links to the underlying foundation units.

## Verdict

`CONDITIONALLY_COHERENT — REQUIRES TWO ASSUMPTION REPAIRS AND EXPLICIT PROOF INSERTIONS`

No fatal contradiction was found. Two assumptions in the draft are stronger or less explicit than necessary:

1. the coordinatewise top-`b` upper bound does not require nonnegative contributions under an exact residual cardinality `b`;
2. the precedence-legal optimum statement requires an explicit feasibility-preserving exchange hypothesis and a terminating rank order.

## A. Core structure

### A1. Basic certificate structure

**Draft location:** Section 2.1.

**Status:** sound definition.

Required data:

- finite object set `I`;
- finite target set `T`;
- admissible configurations `A subseteq 2^I`;
- certificate values `L_S(t)`;
- thresholds `Theta(t)`;
- objective `F(S)` equal to the number of strict threshold crossings.

No additive assumption is used here.

### A2. Additive realization

**Draft location:** Section 2.2.

**Statement:**

\[
L_S(t)=\beta(t)+\sum_{i\in S}\Gamma(i,t).
\]

**Status:** sound.

The update identity follows immediately. Nonnegativity is correctly separated as an optional property.

## B. Monotonicity and exchange

### B1. Monotonicity

**Draft location:** Theorem 3.1.

**Dependencies:** additive structure plus `Gamma(i,t) >= 0`.

**Status:** sound.

For `S subseteq U`,

\[
L_U(t)-L_S(t)=\sum_{i\in U\setminus S}\Gamma(i,t)\ge0.
\]

Strict threshold certification is therefore preserved.

### B2. Dominance exchange

**Draft location:** Theorem 3.3.

**Dependencies:** additive structure and componentwise dominance only.

**Status:** sound, with one necessary feasibility clause.

The theorem must state that the exchanged set

\[
S'=(S\setminus\{j\})\cup\{i\}
\]

is admissible. Equivalently, the admissible family must be preserved by the specific exchange. Without this clause the objective comparison is valid algebraically, but `S'` may not belong to the optimization domain.

Correct theorem form:

> If `S` is admissible, `j in S`, `i notin S`, `i succeeds j`, and `S'` is admissible, then `F(S') >= F(S)`.

Nonnegativity is not required.

### B3. Precedence-legal optimum

**Draft location:** Section 3.4.

**Current issue:** the phrase “subject to equal-cardinality exchange” is not a complete hypothesis.

A sufficient precise form is:

- orient the usable dominance exchanges by an acyclic relation `prec`;
- assign a rank `rho:I -> {1,...,|I|}` strictly increasing along `prec`;
- require that whenever a configuration contains a child but omits a required parent, replacing that child by the parent preserves admissibility;
- each replacement does not decrease `F` by dominance exchange.

The potential

\[
\Phi(S)=\sum_{i\in S}\rho(i)
\]

strictly decreases or increases according to the chosen orientation, so repeated repairs terminate. The terminal configuration is legal and has objective at least that of the initial optimum; hence it is also optimal.

**Classification:** exact finite theorem after the above hypotheses are inserted.

### B4. No deletion

**Draft location:** Section 3.5.

**Status:** sound boundary statement.

Dominance gives a replacement rule, not permission to remove the dominated object from the ground set.

## C. Branch-and-Bound

### C1. Admissible upper bound

**Draft location:** Definition 4.1.

**Status:** sound.

### C2. Safe pruning

**Draft location:** Theorem 4.2.

**Status:** sound.

If all completions at a node have value at most the incumbent, no strictly better solution is lost.

### C3. Exactness

**Draft location:** Theorem 4.3.

**Status:** sound for finite search.

No additivity, nonnegativity, dominance, Fourier, or PVG input is needed. The theorem is a finite exhaustive-search invariant.

## D. Coordinatewise top-b bound

**Draft location:** Section 5.

### D1. Exact residual budget

Suppose each completion chooses exactly `b` objects from the undecided set `R`. For each target let `M_b(t;R)` be the sum of the `b` largest real numbers among `Gamma(i,t)`, `i in R`.

Then every residual `b`-set `Q` satisfies

\[
\sum_{i\in Q}\Gamma(i,t)\le M_b(t;R),
\]

regardless of signs.

Therefore the upper bound is admissible **without nonnegativity** under an exact residual budget.

### D2. At-most residual budget

If completions may choose at most `b` objects, signed contributions require

\[
M_{\le b}(t;R)=
\max_{0\le k\le b}\{\text{sum of the }k\text{ largest contributions}\}.
\]

Equivalently, select at most `b` positive contributions after sorting. Nonnegativity allows the simpler exact-`b` expression.

### D3. Required paper repair

Section 5 should distinguish:

- exact-cardinality theorem: signed contributions allowed;
- at-most-cardinality corollary: use `M_{<=b}`, or assume nonnegativity.

## E. Precedence propagation

**Draft location:** Section 6.

**Status:** sound after B3 supplies existence of an optimal legal solution.

Including a child forces all ancestors. Excluding an ancestor forces all descendants that require it. Contradictory closures, budget overflow, and insufficient remaining capacity are exact infeasibility tests.

## F. Mandatory sets

### F1. Abstract sound mandatory set

**Draft location:** Definition 7.1.

**Status:** sound.

### F2. Additive leave-one-out construction

**Draft location:** Section 7.2.

Under an exact residual budget `b`, if the coordinatewise best residual value after forbidding `i` does not cross the threshold, then every certifying completion must include `i`.

This proof uses the same exact-`b` top-sum lemma as Section 5 and does not require nonnegative contributions. For an at-most budget, the `M_{<=b}` variant is required.

The test is necessary only. Containing all detected mandatory objects is not sufficient for certification.

### F3. Precedence closure

Sound when every feasible legal completion containing an object also contains its declared ancestors.

## G. Compatibility relaxation

### G1. Downward-closed resource family

**Draft location:** Section 8.

**Status:** sound.

Assume every feasible residual selection belongs to `R_nu`, and `R_nu` is downward closed. If a completion certifies target family `A`, it contains the mandatory union `M_nu(A)`. Downward closure implies `M_nu(A) in R_nu`.

Thus actual simultaneous certification implies mandatory compatibility.

The converse is not established.

### G2. Mandatory-union bound

**Status:** admissible for the original problem and exact for the mandatory-compatibility relaxation.

It must not be described as an exact characterization of actual certification.

### G3. Pairwise graph coloring

**Status:** sound.

Every actually certifiable family is a clique in the pairwise compatibility graph. Any proper coloring using `k` colors satisfies `omega <= chi <= k`, hence gives a safe upper bound.

Pairwise compatibility is not sufficient for higher-order compatibility.

## H. Minimal forbidden obstructions

**Draft location:** Section 9.

### H1. Minimal-obstruction theorem

**Status:** sound for finite target sets and downward-closed compatibility.

A family is mandatory-compatible iff it contains no inclusion-minimal forbidden family.

Every forbidden family contains **at least one** minimal forbidden subfamily. Uniqueness is not claimed and is generally false.

### H2. Antichain compression

**Status:** sound.

All forbidden families and the minimal forbidden antichain define the same feasible families of the mandatory-set relaxation. Hence they produce the same relaxation optimum.

### H3. Cuts

Each minimal forbidden family `E` gives the exact relaxation cut

\[
\sum_{t\in E}x_t\le |E|-1.
\]

This cut constrains the target-family relaxation; it does not by itself alter or characterize the original object-selection feasible region.

## I. Fourier/PVG realization

**Draft locations:** Sections 10–11.

**Status:** structurally consistent with the recorded realization, subject to source crosslinks in the final paper.

The paper must link the formulas for `G_k(c)`, the baseline `beta(c)`, reduced period, contamination threshold, and benchmark counts to their dedicated theory and result files. Finite benchmark agreement validates the implementation only on the stated range.

## J. Required manuscript actions

1. Insert the admissibility-preserving clause in Theorem 3.3.
2. Replace the informal legal-optimum paragraph with a theorem using an acyclic rank and terminating potential.
3. Repair Section 5 to distinguish exact-cardinality signed bounds from at-most-cardinality bounds.
4. Apply the same repair to mandatory-set extraction in Section 7.2.
5. Label graph/hypergraph constructions consistently as relaxations of actual simultaneous certification.
6. Add theorem-source and executable-evidence crosslinks.
7. Keep transferability, polynomial complexity, Goldbach, RH, and GRH claims explicitly outside scope.

## Final audit status

```text
THEOREM LOGIC = PASS AFTER STATED REPAIRS
RELAXATION SCOPE = PASS
ARITHMETIC CLAIM BOUNDARY = PASS
TRANSFERABILITY CLAIM = NOT AUTHORIZED
LATEX CONVERSION = BLOCKED UNTIL MANUSCRIPT REPAIR
```
