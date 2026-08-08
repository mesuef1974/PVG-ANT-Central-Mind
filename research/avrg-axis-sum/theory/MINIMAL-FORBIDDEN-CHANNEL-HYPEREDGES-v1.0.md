# ACTIVE-003-S — Minimal Forbidden Channel Hyperedges

## Status

Exact combinatorial compression of ACTIVE-003-R. No Goldbach, RH, GRH, or polynomial-time claim.

## 1. Node data

At a branch-and-bound node let the residual frequency budget be `t`. For every potentially certifiable reduced channel `c`, let

\[
\overline M_c
\]

be the mandatory precedence-closed set of still-unselected frequencies required by the certification-margin test.

For a channel family `T`, define

\[
\mathcal M(T)=\bigcup_{c\in T}\overline M_c.
\]

The family is jointly feasible only if

\[
|\mathcal M(T)|\le t.
\]

A forbidden channel hyperedge is therefore a family `E` satisfying

\[
|\mathcal M(E)|>t.
\]

## 2. Minimal forbidden hyperedges

A forbidden hyperedge `E` is inclusion-minimal when

\[
|\mathcal M(E)|>t
\]

and every proper subset `E'\subsetneq E` satisfies

\[
|\mathcal M(E')|\le t.
\]

Write the family of all minimal forbidden hyperedges as

\[
\mathcal F_{\min}.
\]

## 3. Minimal-obstruction theorem

**Theorem.** A channel family `T` is jointly feasible if and only if it contains no member of `\mathcal F_{\min}`.

### Proof

If `T` contains `E\in\mathcal F_{\min}`, then

\[
\mathcal M(E)\subseteq\mathcal M(T)
\]

and hence `|\mathcal M(T)|>t`; thus `T` is infeasible.

Conversely, suppose `T` is infeasible. Since `T` is finite, choose an inclusion-minimal infeasible subset `E\subseteq T`. Then `E\in\mathcal F_{\min}`. Therefore every infeasible family contains a minimal forbidden hyperedge. ∎

## 4. Exact compressed hypergraph bound

Define

\[
UB_{\min}
=
\max\{|T|: \forall E\in\mathcal F_{\min},\ E\nsubseteq T\}.
\]

By the theorem,

\[
\boxed{UB_{\min}=UB_{\mathrm{hyp}}.}
\]

Thus replacing all forbidden families by the antichain `\mathcal F_{\min}` preserves the exact ACTIVE-003-R upper bound.

## 5. Extraction algorithm

Enumerate channel subsets in increasing cardinality. A subset `E` is retained exactly when:

1. `|\mathcal M(E)|>t`;
2. no previously retained minimal forbidden hyperedge is contained in `E`.

Because enumeration is size-increasing, the second test is equivalent to inclusion-minimality.

## 6. Reuse as cuts

Each `E\in\mathcal F_{\min}` yields the exact 0–1 cut

\[
\sum_{c\in E}x_c\le |E|-1,
\]

where `x_c=1` means channel `c` is certified by the completion.

These cuts may be cached at the node and used by an exact maximum-cardinality search over channel subsets. They do not alter the frequency-selection feasible region and cannot create a false certificate.

## 7. Expected computational return

The unit targets representation and repeated-query cost rather than a stronger upper bound:

- bound value must equal ACTIVE-003-R at every tested node;
- branch-and-bound node and leaf counts must therefore be identical when all minimal cuts are solved exactly;
- the measurable gain is reduction from all forbidden subsets to an inclusion-antichain of minimal obstructions;
- no uniform runtime improvement is claimed because extraction itself is exponential in the number of potentially certifiable channels.

## 8. Verification obligations

The executable verifier must check:

1. every retained hyperedge is forbidden;
2. every retained hyperedge is inclusion-minimal;
3. every forbidden family contains a retained hyperedge;
4. `UB_min = UB_hyp` at every visited search node;
5. exact optimum agreement with exhaustive frequency selection;
6. zero false certificates against independently reconstructed prime-prime channel mass;
7. counts by minimal-hyperedge cardinality;
8. total forbidden families versus minimal forbidden families;
9. an explicit node with strict representation compression.

## 9. Scientific classification

- minimal-obstruction theorem: exact finite combinatorics;
- compressed cut family: exact reformulation;
- computational reduction: empirical and benchmark-specific;
- Goldbach proof: none;
- RH/GRH progress: none;
- polynomial-time claim: none.
