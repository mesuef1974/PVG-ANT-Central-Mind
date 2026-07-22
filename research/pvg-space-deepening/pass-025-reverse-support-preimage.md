# PASS-025 — Reverse Support-Preimage Generator

**ID:** `PASS-025-REVERSE-SUPPORT-PREIMAGE`  
**Goal:** `GOAL-OP-REVERSE-SUPPORT-PREIMAGE-001`  
**Configuration:** `PASS-025-REVERSE-SUPPORT-PREIMAGE-FROZEN-CONFIG-001`  
**Outcome:** `DEPTH_12_WITNESS_FOUND_WITHIN_FROZEN_CLASS`  
**Classification:** finite verified witness inside a frozen contaminated search class  
**Date:** 2026-07-22

## 1. Question

Can the exact support-preimage identity from SYNTHESIS-001 be used in reverse to generate a depth-12 prime-pair face without blindly increasing the PASS-024 sum cap?

The registered target was one extra reverse support layer above the known depth-11 family whose support tail begins at:

\[
F_{10}=\{2,167071\}.
\]

The frozen chain was:

```text
source prime pair
→ binary predecessor support E
→ {2,167071}
→ known depth-10 tail
→ terminal axis
```

## 2. Exact reverse construction

For a binary support:

\[
E=\{a,b\},
\]

all integers with exact support \(E\) are:

\[
m=a^i b^j,\qquad i,j\ge1.
\]

If \(a,b\) are odd, then every such \(m\) is odd. A representation of \(m\) by two primes must therefore use the prime 2:

\[
m=2+(m-2).
\]

Thus a valid source face is produced whenever \(m-2\) is prime.

To make \(E\) a predecessor of the known tail, the registered pass first required:

\[
a+b=n,
\qquad
\operatorname{supp}(n)=\{2,167071\}.
\]

This yields the exact reverse route:

\[
\{2,m-2\}
\to
\{a,b\}
\to
\{2,167071\}.
\]

## 3. Frozen scope

The configuration was committed before registered result promotion:

```text
target depth                      = 12
known tail support                = {2,167071}
known tail closure depth          = 10
reverse support depth budget      = 1
predecessor class                 = binary prime faces
reverse seed integer cap          = 5,346,272
candidate support node cap        = 50,000
candidate integer cap             = 10^12
prime-pair realization cap        = 10^12
orbit verification depth cap      = 16
registered witness count          = 25
```

No cap was increased after the registered result was observed.

## 4. Contamination record

A small reconnaissance run preceded the frozen configuration. It showed only that the route was feasible and that a candidate could lie above the PASS-024 sum cap.

Therefore PASS-025 is:

```text
confirmatory and exhaustive inside the frozen class
```

not blinded, and not a valid basis for a global minimality claim.

## 5. Seed fiber

The exact-support seed integers under the frozen cap are:

\[
2^e\cdot167071,\qquad 1\le e\le5.
\]

Hence:

```text
334142
668284
1336568
2673136
5346272
```

Their distinct-prime representation counts are:

| Seed | Exponents | Distinct prime pairs |
|---:|---:|---:|
| 334142 | `(1,1)` | 1596 |
| 668284 | `(2,1)` | 2917 |
| 1336568 | `(3,1)` | 5136 |
| 2673136 | `(4,1)` | 9388 |
| 5346272 | `(5,1)` | 16899 |

Total binary predecessor supports:

\[
\boxed{35936}.
\]

This is below the frozen node cap \(50000\), so no truncation occurred.

## 6. Regression correction: predecessor-to-seed association

The exploratory prototype contained an invalid bookkeeping possibility: a predecessor support could inherit more than one seed label even though its sum is fixed.

The registered tool replaces that structure by the map:

```text
predecessor support {a,b} → exactly one seed a+b
```

and fails immediately if the same predecessor appears with two different seed sums.

The registered verification confirms:

```text
every predecessor has one seed sum = true
every predecessor reconstructs its seed = true
every predecessor maps to {2,167071} = true
```

This is a correction to the prototype bookkeeping, not a change to the mathematical transition.

## 7. Candidate enumeration

Among the 35936 predecessor supports:

- 14500 have at least one exact-support integer under \(10^{12}\);
- 14589 exact-support integers were generated;
- 14589 deterministic primality tests were performed on \(m-2\);
- 1106 source-pair candidates passed primality;
- the best 25 under the frozen ranking were forward-verified.

Per-seed candidate counts:

| Seed | Exact-support integers tested | Prime-producing candidates |
|---:|---:|---:|
| 334142 | 1617 | 67 |
| 668284 | 2946 | 360 |
| 1336568 | 5153 | 287 |
| 2673136 | 3419 | 327 |
| 5346272 | 1454 | 65 |

## 8. First witness inside the frozen class

The minimum exposing prime limit under the frozen ranking is:

\[
\boxed{27397961}.
\]

The source pair is:

\[
\boxed{\{2,27397961\}}.
\]

Its sum is:

\[
27397963=41\cdot668243.
\]

Therefore:

\[
\operatorname{supp}(27397963)=\{41,668243\}.
\]

The predecessor seed is:

\[
41+668243=668284=2^2\cdot167071,
\]

so:

\[
\operatorname{supp}(668284)=\{2,167071\}.
\]

The exact first two transitions are consequently:

\[
\{2,27397961\}
\to
\{41,668243\}
\to
\{2,167071\}.
\]

## 9. Full verified depth-12 orbit

The registered forward certificate is:

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

Thus the face closure depth of the source pair is:

\[
\boxed{12}.
\]

Every transition was regenerated from the canonical support-of-sums rule.

## 10. What is minimal here?

The witness is minimum only with respect to:

```text
1. exposing prime limit
2. source sum
3. predecessor radical
4. predecessor support
5. seed sum
```

inside all of the following frozen restrictions:

- the tail \(\{2,167071\}\);
- one reverse layer;
- binary predecessor supports;
- the five seed integers under \(5346272\);
- candidate integers under \(10^{12}\);
- source primes under \(10^{12}\).

It is not claimed to be the globally smallest depth-12 prime pair.

## 11. Relation to PASS-024

PASS-024 found no depth-12 case for represented sums up to:

\[
400000.
\]

PASS-025 did not linearly increase that cap. It used the registered depth-11 tail to construct reverse candidates and found a depth-12 witness whose source sum is:

\[
27397963.
\]

The result demonstrates that reverse support-preimage generation is materially more targeted than scanning every represented sum up to the witness.

This is a finite computational gain, not an asymptotic complexity theorem.

## 12. ANT interpretation

The source sum satisfies:

\[
r_2(27397963)\ge1
\]

because:

\[
27397963=2+27397961.
\]

The PVG layer classifies this representation by the support orbit of the sum. The new contribution of PASS-025 is not a lower bound for \(r_2(N)\); it is a reverse mechanism that selects candidate \(N\) from a desired orbit tail before testing prime representation.

Thus the present gain is:

```text
structural candidate generation
```

not a new analytic estimate.

## 13. Verification package

Files:

```text
tools/pvg_reverse_support_preimage.py
tests/test_pvg_reverse_support_preimage.py
research/pvg-space-deepening/data/reverse-support-preimage-summary.json
governance/frozen-config/PASS-025-REVERSE-SUPPORT-PREIMAGE-FROZEN-CONFIG.md
```

Verification includes:

- deterministic seed generation;
- exhaustive prime-pair enumeration for all five seeds;
- one-to-one predecessor/seed association;
- exact-support candidate generation;
- deterministic 64-bit Miller–Rabin;
- full forward verification for the promoted 25 witnesses;
- committed-summary regeneration;
- cap-failure negative test;
- invalid-depth configuration rejection.

## 14. Stage interpretation

PASS-025 succeeds at its declared binary outcome:

```text
DEPTH_12_WITNESS_FOUND_WITHIN_FROZEN_CLASS
```

It does not justify PASS-026 automatically. The result must return through the mandatory Stage Review to:

`GOAL-OP-ONE-THEOREM-001`.

The useful knowledge to return is:

1. reverse support preimages are computationally effective;
2. exact seed association is load-bearing;
3. deep witnesses can be constructed far above a small forward cap;
4. support-tail targeting gives a reusable search mechanism;
5. the mechanism still lacks an ANT transfer lemma or asymptotic estimate.

## 15. Scientific ceiling

PASS-025 does not prove:

- that this is the globally first depth-12 witness;
- that depths are unbounded;
- that every orbit terminates;
- that a universal depth bound exists or does not exist;
- an asymptotic law for depth thresholds;
- a new Goldbach theorem;
- a new estimate for representation functions;
- historical originality;
- PNT, RH, or GRH progress.

**Honest classification:** exact reverse construction plus a finite verified depth-12 witness inside one frozen, explicitly contaminated binary-predecessor search class. No original theorem certified.
