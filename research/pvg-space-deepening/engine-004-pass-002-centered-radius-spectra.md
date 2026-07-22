# ENGINE-004 PASS-002 — Governed Centered-Radius Spectra

```text
Goal ID: GOAL-OP-INVERSE-PRIME-FIBERS-001
Engine: ENGINE-004
Phase: C — Inverse Prime Fibers
Status: implementation complete / repository CI pending
Scope: frozen 884-point box only
Phase D: NOT AUTHORIZED
Classification: IDENTITY / PROVED / FINITE-VERIFIED / INTERPRETATION
```

## 1. Authorized object

For each centered gap

\[
\Delta=q-p,
\]

define

\[
D(N)=
\begin{cases}
\{\Delta/2:\Delta\in\Delta_2(N)\},&N\text{ even},\\
\Delta_2(N),&N\text{ odd}.
\end{cases}
\]

This is the object authorized by `transition-memory/next-action.md`.

An earlier implementation used the scale-free ratio `Delta/N`. That coordinate was removed from this pass because it was not the governed object. No result from that superseded implementation is promoted here.

## 2. Exact reconstruction laws

### Even route

Let \(N=2m\). Every admitted gap is \(\Delta=2d\), where \(d\in D(N)\), and

\[
p=m-d,
\qquad
q=m+d,
\qquad
\gcd(m,d)=1.
\]

Therefore \(N\) together with \(D(N)\) reconstructs the full distinct-prime fiber exactly.

### Odd route

An odd point has an empty fiber or one representation

\[
N=2+(N-2).
\]

Its unique coordinate is

\[
d=(N-2)-2=N-4.
\]

Hence

\[
N=d+4,
\qquad
(p,q)=(2,d+2).
\]

Two represented odd points cannot share one governed coordinate.

### Multiplicity

Different prime pairs over a fixed \(N\) have different gaps. Consequently

\[
|D(N)|=|\mathcal R_2(N)|.
\]

**Classification:** `IDENTITY / PROVED`.

## 3. Information preserved and lost

The projection must be described with its retained data made explicit.

```text
(N, D(N))
→ lossless recovery of the complete distinct-prime fiber
```

but

```text
D(N) alone
→ generally loses the midpoint, integer label, support label, and pair labels
```

Thus the spectrum is not intrinsically lossy; the loss occurs when the base point \(N\) is discarded.

**Classification:** exact recovery statement plus `INTERPRETATION` of the projection.

## 4. Frozen complete-box certificate

```text
support primes <= 11
support face sizes = 1,2,3
integer cap = 100000
integer points = 884
representable points = 745
nonrepresentable points = 139
total coordinate occurrences = 218024
```

Every one of the 218,024 coordinates reconstructs its registered prime pair from \(N\) and \(D(N)\).

### Spectrum classes

```text
unique spectra including the empty spectrum = 744
unique nonempty spectra = 743
represented points = 745
represented-point / nonempty-spectrum ratio = 745 / 743
nonempty spectrum collision classes = 1
empty spectrum class size = 139
```

The only nonempty collision is

\[
D(5)=D(8)=D(12)=\{1\},
\]

with

```text
5  = 2+3   on support {5}   — odd raw-gap route
8  = 3+5   on support {2}   — even half-gap route
12 = 5+7   on support {2,3} — even half-gap route
```

No other represented point in the frozen box shares its complete spectrum.

### Coordinate collisions

```text
unique coordinate values = 36797
unique even-route coordinate values = 36787
unique odd-route coordinate values = 95
odd values also appearing on the even route = 85
odd-only coordinate values = 10
shared coordinate values = 27799
  even/even shared values = 27714
  odd/even shared values = 85
  odd/odd shared values = 0
```

The most widely shared coordinate is \(d=7\), occurring at 64 frozen-box integer points. This records repeated gap geometry across different midpoints; it does not identify the integers or their support faces.

### Proper containment

```text
proper containment edges among unique nonempty spectra = 2048
edges with singleton subset spectrum = 2038
edges with non-singleton subset spectrum = 10
```

Only three non-singleton spectra occur as proper subsets:

\[
(4,2),
\qquad
(9,3),
\qquad
(45,33,3).
\]

Their ten complete finite-box containment edges are stored in the deterministic summary. This separation matters: the raw count 2048 is dominated by singleton-spectrum containment and should not be interpreted as a large family of deep multi-coordinate inclusions.

**Classification:** `FINITE-VERIFIED` in the frozen 884-point box only.

## 5. Reproducibility

```text
tools/pvg_centered_radius_spectra.py
tests/test_pvg_centered_radius_spectra.py
research/pvg-space-deepening/data/centered-radius-spectra-summary.json
.github/workflows/pvg-centered-radius-spectra-audit.yml
```

Commands:

```text
python -m unittest -v tests/test_pvg_centered_radius_spectra.py
python tools/pvg_centered_radius_spectra.py --registered-summary --compact
python tools/honesty_audit.py
python tools/state_coherence_audit.py
python tools/research_compass_audit.py
python tools/goal_memory_traceability_audit.py
```

The compact deterministic output, including its trailing newline, has SHA-256:

```text
4064f2a2be99e92b20d6cc8917d8f4e8ba75ddab3c2b53e4baec7616ae19d468
```

An independent implementation regenerated the same frozen counts and digest before push. Repository CI remains the final operational gate for this pass.

## 6. Honest conclusions

1. \(D(N)\) is an exact coordinate system for the prime fiber when the base point \(N\) is retained.
2. The odd route is coordinate-injective: its coordinate is \(N-4\).
3. Dropping \(N\) creates extensive coordinate collisions but almost no complete nonempty-spectrum collisions in this finite box.
4. The only complete nonempty collision crosses both support faces and parity routes.
5. Most proper containments are generated by singleton spectra; only ten have a non-singleton subset.

These conclusions are exact or finite-verified. They do not imply an asymptotic law or a statement outside the frozen domain.

## 7. Claim ceiling

This pass does not authorize:

- cap expansion;
- Phase D or orbit dynamics;
- theorem-path reactivation;
- an asymptotic estimate;
- historical originality or publication readiness;
- any Goldbach, PNT, RH, or GRH claim or progress.
