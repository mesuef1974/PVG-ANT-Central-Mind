# ACTIVE-003-D — Local Fourier Decomposition Status

Status: `CLOSED-PASS-v1.2`

## Scope

Decompose each von Mangoldt difference channel into its zero Fourier mode and its nonzero-frequency deviation, then combine that decomposition with the local higher-prime-power contamination bound.

## Proved

1. Exact inversion:

   \[
   Y_{N,r}^{\Lambda}(d)
   =
   \frac1r\sum_{h\bmod r}
   \widehat Y_{N,r}^{\Lambda}(h)e_r(-hd).
   \]

2. Zero/nonzero split:

   \[
   Y_{N,r}^{\Lambda}(d)
   =
   \frac{R_{\Lambda}(N)}r
   +
   \Delta_{N,r}^{\Lambda}(d).
   \]

3. Every Fourier coefficient is real because the additive-fiber weight is invariant under \(a\leftrightarrow N-a\).

4. Local prime-channel lower bound:

   \[
   Y_{N,r}^{\mathrm{pp}}(d)
   \ge
   \frac{R_{\Lambda}(N)}r
   +
   \Delta_{N,r}^{\Lambda}(d)
   -
   C_{N,r}(d).
   \]

5. If 
   \(|\Delta_{N,r}^{\Lambda}(d)|\le B_{N,r}(d)\), then

   \[
   \frac{R_{\Lambda}(N)}r
   >
   B_{N,r}(d)+C_{N,r}(d)
   \]

   is sufficient for a prime representation in channel \(d\).

## Verification

Range:

```text
2 <= N <= 500
1 <= r <= 25
```

Results:

```text
channel checks                = 162,175
Fourier inversion mismatches  = 0
reality mismatches            = 0
reflection mismatches         = 0
Parseval mismatches           = 0
exact local certificates      = 33,245
exact false certificates      = 0
uniform l1 certificates       = 414
uniform false certificates    = 0
prime-positive channels       = 39,956
status                        = PASS
```

## Scientific interpretation

The finite Fourier identity itself is exact but not a new prime theorem. It exposes the analytic target:

\[
\text{zero-mode lower bound}
-
\text{nonzero-mode deviation}
-
\text{higher-prime-power contamination}
>0.
\]

The crude triangle estimate

\[
|\Delta(d)|
\le
\frac1r\sum_{h\ne0}|\widehat Y(h)|
\]

is valid but loses most usable certificates: 414 versus 33,245 exact certificates in the benchmark. The next unit must exploit phase cancellation or a major/minor frequency split rather than summing all magnitudes.

## Controlling files

- `theory/LOCAL-CHANNEL-FOURIER-DECOMPOSITION-v1.2.md`
- `code/verify_local_channel_fourier_decomposition.py`
- `results/local_channel_fourier_decomposition_verification_v1.2.json`

## Classification

- Exact Fourier decomposition: `PROVED`.
- Local conditional prime certificate: `PROVED`.
- Finite verification: `PASS`.
- Nontrivial analytic nonzero-mode bound: `OPEN`.
- Goldbach progress: `NOT CLAIMED`.
- RH/GRH progress: `NONE`.

## Next target

`ACTIVE-003-E`: reduce the frequency system to its effective modulus \(q=r/\gcd(2,r)\), identify duplicate/vanishing Fourier modes, and test major-frequency versus residual-frequency decompositions before invoking deeper circle-method estimates.
