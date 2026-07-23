# ENGINE-006 WP-5 — Structural Proposition Audit

Status: CHECKPOINT_PASS / CLOSED

## Scope

This audit tests only propositions already implicit in the typed map system developed in ENGINE-006 WP-1 through WP-4. No new dataset, numerical experiment, conjecture generation, or novelty claim is authorized.

Each proposition is classified by:

- formal status;
- whether valuation data are essential;
- whether additive data are essential;
- whether their interaction is essential;
- whether the statement is reconstructible from standard antecedents;
- whether it adds proof strength.

## Governing objects

Let

- `nu(N)` be the finite-support prime-valuation vector of a positive integer `N`;
- `supp(N)` its prime support;
- `R_2(N) = {(p,q): p<q, p+q=N, p,q prime}`;
- `Delta = (q-p)/2` for an admissible distinct-prime representation;
- `D(N)` the corresponding centered-coordinate set;
- `I = {(N,d): d in D(N)}` the integer-coordinate incidence relation;
- `E_0 = {N: D(N)=empty}` the empty-row registry.

## Proposition ledger

### P1 — Reconstruction of the integer from its valuation vector

Statement:

`N = product_p p^(nu_p(N))`, with finite support.

Classification: `REDUNDANT_STANDARD_FACT`.

Dependence audit:

- Uses valuation data essentially? YES.
- Uses additive data essentially? NO.
- Uses their interaction essentially? NO.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

Reason: this is unique factorization expressed in valuation coordinates.

### P2 — Support is a lossy quotient of valuation data

Statement:

The map `nu(N) -> supp(N)` forgets all positive exponent values while retaining only zero/nonzero coordinates. Its fiber over a finite prime set `F` is the family of all positive exponent assignments on `F`.

Classification: `PROVED` and `REDUNDANT_STANDARD_FACT`.

Dependence audit:

- Uses valuation data essentially? YES.
- Uses additive data essentially? NO.
- Uses their interaction essentially? NO.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

### P3 — Reconstruction of a distinct prime pair from fixed base and centered coordinate

Statement:

For fixed `N` and admissible `Delta`,

`p = N/2 - Delta`, `q = N/2 + Delta`.

Conversely, each `(p,q) in R_2(N)` determines `Delta = (q-p)/2`.

Classification: `IDENTITY`.

Dependence audit:

- Uses valuation data essentially? NO.
- Uses additive data essentially? YES.
- Uses their interaction essentially? NO.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

### P4 — Equivalence of labeled prime-pair fibers and labeled centered spectra

Statement:

For fixed labeled base `N`, the maps in P3 induce a bijection

`R_2(N) <-> D(N)`.

Classification: `PROVED`.

Dependence audit:

- Uses valuation data essentially? NO.
- Uses additive data essentially? YES.
- Uses their interaction essentially? NO.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

### P5 — Integer-coordinate incidence reconstructs every nonempty spectrum row

Statement:

For each `N` appearing as a first coordinate of `I`,

`D(N) = {d : (N,d) in I}`.

Classification: `IDENTITY`.

Dependence audit:

- Uses valuation data essentially? NO.
- Uses additive data essentially? YES.
- Uses their interaction essentially? NO.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

### P6 — Empty-row registry is necessary for complete row-family reconstruction

Statement:

The incidence relation `I` alone does not distinguish a registered integer with empty row from an integer absent from the registry. The pair `(I,E_0)` reconstructs the complete registered family of spectrum rows.

Classification: `PROVED`.

Dependence audit:

- Uses valuation data essentially? NO.
- Uses additive data essentially? YES.
- Uses their interaction essentially? NO.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

This is a genuine data-contract requirement, not a new arithmetic theorem.

### P7 — Forgetting the base label destroys general invertibility

Statement:

The map `(N,D(N)) -> D(N)` is not invertible in general unless the base can be independently recovered from side information.

Classification: `PROVED`.

Dependence audit:

- Uses valuation data essentially? NO.
- Uses additive data essentially? YES.
- Uses their interaction essentially? NO.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

The loss occurs at label deletion, not in the centered-coordinate parametrization itself.

### P8 — Support-coordinate incidence is strictly less informative than integer-coordinate incidence

Statement:

Projecting `(N,d)` to `(supp(N),d)` identifies all integer owners sharing the same support and coordinate. Integer ownership cannot generally be reconstructed from the projected relation.

Classification: `PROVED`.

Dependence audit:

- Uses valuation data essentially? YES, through support.
- Uses additive data essentially? YES, through `d`.
- Uses their interaction essentially? YES for the definition of the projected mixed relation.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

This is the first proposition whose formulation uses both layers essentially, but its content remains a standard non-injectivity statement about a forgetful map.

### P9 — Parity route factors through support only on an explicitly typed domain

Statement:

For positive integers, parity is determined by whether `2` belongs to `supp(N)`. Hence the parity map factors through support:

`N -> supp(N) -> parity(N)`.

Classification: `REDUNDANT_STANDARD_FACT`.

Dependence audit:

- Uses valuation data essentially? YES, or equivalently divisibility by `2`.
- Uses additive data essentially? NO.
- Uses their interaction essentially? NO.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

Any route convention richer than ordinary parity must be separately defined before a stronger proposition is well posed.

### P10 — The mixed typed diagram commutes where all maps are defined

Statement:

Reconstructing `(p,q)` from `(N,Delta)` and then projecting to the prime-pair fiber yields the same labeled representation obtained directly from the fiber-to-coordinate correspondence. Likewise, reconstructing `N` from `nu(N)` before attaching its labeled additive row yields the same labeled row as attaching the row to the original integer label.

Classification: `PROVED`.

Dependence audit:

- Uses valuation data essentially? YES in the second square.
- Uses additive data essentially? YES.
- Uses their interaction essentially? YES at the level of typed composition.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

The commutativity is bookkeeping coherence between independently standard maps.

### P11 — No interaction-essential arithmetic theorem is currently established

Statement:

Among the audited propositions, none proves an arithmetic conclusion that requires both valuation structure and additive prime-pair structure in a way not reconstructible from their standard antecedents.

Classification: `PROVED` as a bounded audit conclusion.

Dependence audit:

- Uses valuation data essentially? YES, to test candidates.
- Uses additive data essentially? YES, to test candidates.
- Uses their interaction essentially? YES, as the audit subject.
- Reconstructible from standard antecedents? YES.
- Adds proof strength? NO.

This is a claim about the current governed corpus, not about all possible future PVG formulations.

### P12 — Independent proof-strength advantage of the current PVG language

Statement:

The current PVG formulation shortens or enables a proof that is unavailable or materially weaker in the standard antecedent language.

Classification: `OPEN`.

Dependence audit:

- Uses valuation data essentially? UNRESOLVED.
- Uses additive data essentially? UNRESOLVED.
- Uses their interaction essentially? UNRESOLVED.
- Reconstructible from standard antecedents? UNRESOLVED.
- Adds proof strength? UNRESOLVED.

No witness theorem or controlled proof comparison has yet been produced.

## Summary table

| ID | Main status | Interaction-essential? | Standard-reconstructible? | Adds proof strength? |
|---|---|---:|---:|---:|
| P1 | REDUNDANT_STANDARD_FACT | NO | YES | NO |
| P2 | PROVED / REDUNDANT_STANDARD_FACT | NO | YES | NO |
| P3 | IDENTITY | NO | YES | NO |
| P4 | PROVED | NO | YES | NO |
| P5 | IDENTITY | NO | YES | NO |
| P6 | PROVED | NO | YES | NO |
| P7 | PROVED | NO | YES | NO |
| P8 | PROVED | YES | YES | NO |
| P9 | REDUNDANT_STANDARD_FACT | NO | YES | NO |
| P10 | PROVED | YES | YES | NO |
| P11 | PROVED bounded audit conclusion | YES | YES | NO |
| P12 | OPEN | UNRESOLVED | UNRESOLVED | UNRESOLVED |

## Audit conclusion

The proposition audit confirms three levels:

1. Exact identities and reconstruction statements.
2. Useful mixed-layer data-contract propositions, especially owner projection and empty-row preservation.
3. No currently established interaction-essential arithmetic theorem or proof-strength gain.

The current framework is mathematically coherent and operationally useful, but its established propositions remain reconstructible from standard valuation, additive-parametrization, incidence, and forgetful-map antecedents.

## Scientific ceiling

- New theorem: NOT CLAIMED.
- New primitive arithmetic object: NOT ESTABLISHED.
- Independent theory: NOT ESTABLISHED.
- Proof-strength advantage: OPEN.
- Publication readiness: NOT ESTABLISHED.
- Goldbach/PNT/RH/GRH progress: FALSE.
