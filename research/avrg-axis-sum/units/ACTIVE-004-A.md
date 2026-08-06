# ACTIVE-004-A — Addition-Fiber Specialist Reasoning Protocol

Status: validated_intake
Classification: Diagnostic
Validation status: architecture_only_unbenchmarked
Branch: `agent/pvg-axis-sum-continuation-002`
Parent program: PVG axis addition / addition-fiber reasoning

## 1. Mission

Convert the axis-addition body of knowledge from a stored research package into an executable reasoning protocol for the Central Mind.

The protocol must accept an additive question involving an integer target `N`, a domain, an optional weight, an optional modulus `r`, and an optional reconstruction objective, then return a structured answer that separates:

1. the exact integer fiber;
2. valuation transport;
3. the chosen weight or observable;
4. residue or difference channels;
5. Fourier information;
6. reconstruction status;
7. the missing analytic certificate.

The protocol is diagnostic. It does not itself prove Goldbach, produce new major/minor arc estimates, certify asymptotics, or establish novelty.

## 2. Input contract

A valid query is normalized to the tuple

```text
Q = (N, domain, order_mode, support_filter, weight, modulus, observable, target_claim)
```

where:

- `N` is the additive target;
- `domain` specifies `N`, `Z`, positive integers, nonnegative integers, primes, prime powers, or another explicitly declared locus;
- `order_mode` is `ordered` or `unordered`;
- `support_filter` restricts admissible summands;
- `weight` is a function on the fiber, such as `1`, `Lambda(a)Lambda(N-a)`, or an indicator;
- `modulus` is optional and must be positive when present;
- `observable` identifies the requested channel, Fourier coefficient, marginal, rank, kernel, or reconstruction target;
- `target_claim` states whether the user asks for an identity, computation, reconstruction, asymptotic, positivity statement, or theorem-level consequence.

Missing fields must be surfaced rather than silently invented when they materially change the mathematics.

## 3. Seven-layer reasoning pipeline

### Layer 1 — Exact integer fiber

Define the carrier before introducing geometry:

\[
\mathcal F_N(A,B)=\{(a,b)\in A\times B:a+b=N\}.
\]

For the standard positive ordered fiber:

\[
\mathcal F_N=\{(a,N-a):1\le a<N\}.
\]

The protocol must state:

- whether order matters;
- the exact cardinality when elementary;
- any parity or support restrictions;
- whether the fiber is empty, finite, or infinite under the chosen domain.

### Layer 2 — Valuation transport

Only after the integer relation is fixed, transport the fiber through prime valuations:

\[
\mathcal G_N=\{(\nu(a),\nu(N-a)):(a,N-a)\in\mathcal F_N\}.
\]

Mandatory warning:

```text
nu(a+b) is not obtained by coordinatewise addition of nu(a) and nu(b).
```

The protocol must distinguish:

- the integer pair `(a,b)`;
- the valuation pair `(nu(a),nu(b))`;
- the valuation of the target `nu(N)`;
- multiplicative structure inside each summand from the additive relation between summands.

### Layer 3 — Weight and additive observable

For a weight `w_N(a)`, define

\[
R_w(N)=\sum_{1\le a<N} w_N(a).
\]

Canonical cases include:

\[
w_N(a)=1,
\]

\[
w_N(a)=\mathbf 1_{\mathbb P}(a)\mathbf 1_{\mathbb P}(N-a),
\]

and

\[
w_N(a)=\Lambda(a)\Lambda(N-a).
\]

The answer must say whether the weight detects:

- all representations;
- prime representations;
- prime-power contamination;
- multiplicity;
- ordered versus unordered counting.

### Layer 4 — Difference/residue channel

For modulus `r`, define the difference label

\[
d\equiv a-b\equiv 2a-N\pmod r.
\]

The channel operator is

\[
(D_{N,r}w)_d=
\sum_{\substack{1\le a<N\\2a-N\equiv d\pmod r}}w_a.
\]

The effective period is

\[
q(r)=\frac{r}{\gcd(2,r)}.
\]

The protocol must check:

- whether every residue class is attainable;
- the parity obstruction when `r` is even;
- whether channels are indexed modulo `r` or compressed to the effective period;
- whether the requested observable is a complete channel vector or only a marginal.

### Layer 5 — Fourier spectrum

For the channel vector `c_d=(D_{N,r}w)_d`, define a finite Fourier transform, with normalization stated explicitly:

\[
\widehat c(k)=\sum_{d\bmod r}c_d e^{-2\pi i kd/r}.
\]

Equivalent direct form:

\[
\widehat c(k)=
\sum_{1\le a<N}w_a e^{-2\pi i k(2a-N)/r}.
\]

The protocol must not use the symmetric phase

\[
e(\alpha a)e(\alpha(N-a))=e(\alpha N)
\]

as a nontrivial discriminator on a fixed fiber, because it is constant there.

It must distinguish:

- full spectrum;
- retained frequencies;
- conjugacy constraints for real channels;
- frequency loss;
- exact inversion versus approximate recovery.

### Layer 6 — Reconstruction certificate

Before claiming reconstruction, the protocol must identify the measurement map

\[
M:W_N\to Y
\]

and check at least:

1. domain dimension;
2. rank;
3. kernel;
4. retained measurements;
5. normalization;
6. conditioning when numerical recovery is discussed.

Allowed conclusions:

```text
exactly reconstructible
reconstructible modulo kernel
not reconstructible from supplied marginals
identifiable only under additional structural assumptions
numerically ill-conditioned
```

Forbidden shortcut:

```text
A visually rich set of channels or Fourier coefficients implies full recovery.
```

### Layer 7 — Analytic certificate and wall

The final layer classifies the strongest justified statement.

The protocol must separate:

```text
finite identity
finite computation
exact linear-algebra theorem
reinterpretation in PVG
statistical diagnostic
conditional asymptotic
known theorem from analytic number theory
new theorem claim
open problem
```

For Goldbach-facing questions, it must identify the missing certificate, such as:

- positivity for every sufficiently large even `N`;
- a uniform major-arc main term;
- a minor-arc bound strong enough to preserve positivity;
- removal of prime-power contamination;
- conversion of average results into pointwise results;
- parity-sensitive sieve information.

The protocol must stop at the wall instead of converting diagnostics into theorem claims.

## 4. Output schema

Every specialist answer should be renderable in the following machine-readable conceptual shape:

```text
AXIS_ADDITION_DIAGNOSIS
- target: N
- domain:
- order_mode:
- integer_fiber:
- valuation_transport:
- weight:
- channel_definition:
- effective_period:
- Fourier_observable:
- measurement_rank:
- kernel:
- reconstruction_status:
- claim_classification:
- analytic_certificate_present:
- missing_certificate:
- scientific_ceiling:
```

Fields not requested may be concise, but no theorem-level conclusion may omit `claim_classification`, `analytic_certificate_present`, and `missing_certificate`.

## 5. Decision rules

### Rule A — Fiber first

Never start from valuation vectors and guess an additive relation. Recover or define the integer fiber first.

### Rule B — Weight explicitness

No phrase such as “number of Goldbach representations” is accepted without specifying ordered/unordered counting and prime indicator versus von Mangoldt weight.

### Rule C — Channel completeness

A marginal, one modulus, or a sparse frequency set is not treated as the joint additive object.

### Rule D — Rank before reconstruction

No reconstruction claim before rank and kernel are stated or proved.

### Rule E — Finite/asymptotic separation

Finite verification up to a bound is evidence, not an asymptotic theorem and not a proof for all integers.

### Rule F — Known/new separation

Any use of circle-method, sieve, character-sum, or zero-density input must be labeled as known source mathematics unless a new proof is supplied and audited.

## 6. Canonical test cases

### Case 1 — `N=5`, unweighted ordered fiber

Expected core output:

\[
\mathcal F_5=\{(1,4),(2,3),(3,2),(4,1)\}.
\]

Valuation transport must preserve the distinction between the four integer pairs even when structural symmetries are noted.

Classification: finite identity.

### Case 2 — `N=24`, unordered prime fiber

Expected prime representations:

\[
24=5+19=7+17=11+13.
\]

The protocol must state that this verifies one target only and does not imply Goldbach universally.

Classification: finite computation.

### Case 3 — `N=30`, von Mangoldt weight

Define

\[
R_\Lambda(30)=\sum_{1\le a<30}\Lambda(a)\Lambda(30-a).
\]

The answer must distinguish prime-prime terms from prime-power terms.

Classification: exact weighted identity plus finite computation if evaluated.

### Case 4 — Modulus `r=6`

The effective period is

\[
q(6)=3.
\]

The protocol must explain why multiplication by `2` modulo `6` does not produce six independent difference classes.

Classification: exact modular linear-algebra fact.

### Case 5 — Sparse Fourier retention

Given only selected `\widehat c(k)`, the protocol must formulate the restricted measurement map and refuse exact reconstruction unless injectivity on the declared model class is proved.

Classification: reconstruction diagnostic.

## 7. Failure modes to detect

The specialist must explicitly reject or repair answers exhibiting any of the following:

1. coordinatewise valuation addition used for ordinary addition;
2. ordered and unordered representations conflated;
3. `Lambda` weight treated as a pure prime indicator;
4. modulo `r` channels assumed independent without checking `gcd(2,r)`;
5. constant symmetric phase advertised as informative;
6. marginal data described as the full joint object;
7. rank omitted before inversion;
8. finite experiments promoted to an all-`N` theorem;
9. average Goldbach statements promoted to pointwise Goldbach;
10. a diagnostic called a proof.

## 8. Validation plan

This unit installs the protocol architecture only. It does not declare autonomous competence.

Required next validation stages:

```text
ACTIVE-004-B: locked specialist benchmark cases
ACTIVE-004-C: adversarial claim-classification tests
ACTIVE-004-D: reconstruction/rank challenge set
ACTIVE-004-E: Goldbach-wall and certificate audit
```

A hidden or locked benchmark must test both correct derivations and refusal behavior.

## 9. Honest closure state

```text
PROTOCOL_SPECIFICATION = COMPLETE
MACHINE_EXECUTION_LAYER = NOT_BUILT
LOCKED_BENCHMARK = NOT_RUN
AUTONOMOUS_SPECIALIST_VALIDATION = NOT_GRANTED
GOLDBACH_PROGRESS = NONE
RH_GRH_PROGRESS = NONE
NEXT_ACTION = ACTIVE-004-B
```
