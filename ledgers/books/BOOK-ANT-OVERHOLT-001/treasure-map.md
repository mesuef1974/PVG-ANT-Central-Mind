# Overholt — Treasure Map

Book ID: `BOOK-ANT-OVERHOLT-001`. **Book Treasure Retrofit Pass 001** — طبقةٌ فوق الإغلاق `audit.md` لا تمسّه. تحكمها `governance/book-treasure-extraction-protocol.md` (نموذج Overholt = المعيارُ الكامل). كلُّ كنزٍ مؤصَّلٌ على `overholt-ledger.json` (11 فصلًا)، مطبَّعٌ إلى معرِّفاتٍ مسجَّلة. لا نصٌّ منسوخ، لا ادّعاءُ إتقانٍ كامل.

```text
Treasure ID: TREASURE-OVERHOLT-001
Treasure:    Chebyshev weights (Λ, θ, ψ)
Source:      Overholt Ch1 / Ch6 — no verbatim text
Type:        founding weighted prime-counting objects
Why it matters: the weights that make prime counting analytically tractable (ψ smoother than π).
ANT role:    ψ(x)=Σ_{n≤x} Λ(n), θ(x)=Σ_{p≤x} log p; Λ underlies −ζ'/ζ = Σ Λ(n) n^{-s}.
PVG translation: prime-power valuation weight on the integer axis (mass, not phase).
Wall / certificate: strong error in ψ(x)−x needs zero information — MC-002.
Classification: Known.
Normalized output: → Object (prime-counting weight) ; consumed by → Tool TOOL-PERRON-001.
```

```text
Treasure ID: TREASURE-OVERHOLT-002
Treasure:    Dirichlet convolution
Source:      Overholt Ch1 — no verbatim text
Type:        algebraic composition law of arithmetic functions
Why it matters: turns arithmetic-function relations into an algebra ("convolution is arithmetic geometry").
ANT role:    (f*g)(n)=Σ_{d|n} f(d) g(n/d); F=1*f is the summatory transform.
PVG translation: composition over the divisor cube; convolution = divisor-box geometry.
Wall / certificate: none (unconditional identity).
Classification: Known / Identity.
Normalized output: → Tool (arithmetic-function composition) ; → Rule RULE-PVG-001 (geometry axis).
```

```text
Treasure ID: TREASURE-OVERHOLT-003
Treasure:    Möbius inversion
Source:      Overholt Ch1 — no verbatim text
Type:        inversion identity
Why it matters: recovers a function from its divisor-sums; backbone of ANT algebra.
ANT role:    F = 1*f  ⟺  f = μ*F.
PVG translation: signed inclusion–exclusion over the divisor cube.
Wall / certificate: none (unconditional identity).
Classification: Known / Identity.
Normalized output: → Tool TOOL-MOBIUS-001 ; → Observable OBS-MOBIUS-001.
```

```text
Treasure ID: TREASURE-OVERHOLT-004
Treasure:    Hyperbola method
Source:      Overholt Ch1 — no verbatim text
Type:        summation-splitting technique
Why it matters: extracts main terms from divisor sums by splitting the hyperbola d·e≤x.
ANT role:    Σ_{n≤x} d(n) = 2Σ_{d≤√x}⌊x/d⌋ − ⌊√x⌋²; the Dirichlet divisor estimate.
PVG translation: symmetric truncation of the divisor-box lattice.
Wall / certificate: none for the main term (the divisor error is a separate open problem).
Classification: Known.
Normalized output: → Tool TOOL-HYPERBOLA-001 ; → Observable OBS-DIVISOR-001.
```

```text
Treasure ID: TREASURE-OVERHOLT-005
Treasure:    Average vs normal order (normal order, Mertens function)
Source:      Overholt Ch2 — no verbatim text
Type:        diagnostic distinction
Why it matters: average, typical, concentration, and cancellation are DIFFERENT tests.
ANT role:    ω(n) has normal order log log n (Hardy–Ramanujan); average ≠ pointwise.
PVG translation: separating mean valuation from typical valuation on the observable ladder.
Wall / certificate: average does not imply pointwise cancellation — WALL-AVERAGE-NORMAL.
Classification: Known / Diagnostic.
Normalized output: → Wall WALL-AVERAGE-NORMAL ; → Rule RULE-AVERAGE-NORMAL-001 ; → Observable OBS-OMEGA-001.
```

```text
Treasure ID: TREASURE-OVERHOLT-006
Treasure:    Dirichlet characters (orthogonality, Gauss sums)
Source:      Overholt Ch3 / Ch7 — no verbatim text
Type:        finite Fourier modes on residue classes
Why it matters: characters are the finite Fourier modes that separate residue classes.
ANT role:    1_{n≡a(q)} = φ(q)^{-1} Σ_χ conj(χ(a)) χ(n); Gauss sums carry the phase.
PVG translation: residue-fiber observables; character = phase reading on the fiber.
Wall / certificate: non-principal modes require L-function zero-control — MC-005.
Classification: Known.
Normalized output: → Tool TOOL-CHARACTER-ORTHOGONALITY-001, TOOL-CHARACTER-SUM-PHASE-001 ; → Observable OBS-CHARACTER-001, OBS-RESIDUE-FIBER-001.
```

```text
Treasure ID: TREASURE-OVERHOLT-007
Treasure:    Euler products
Source:      Overholt Ch3 / Ch9 — no verbatim text
Type:        multiplicative factorization over prime axes
Why it matters: encodes multiplicativity as a product over prime axes; the bridge to zeros.
ANT role:    ζ(s)=Π_p (1−p^{-s})^{-1}; L(s,χ)=Π_p (1−χ(p)p^{-s})^{-1}.
PVG translation: factorization over the prime-valuation axes (primes / prime powers / prime ideals).
Wall / certificate: none for the identity (zero-control is downstream).
Classification: Known.
Normalized output: → Tool TOOL-EULER-PRODUCT-001.
```

```text
Treasure ID: TREASURE-OVERHOLT-008
Treasure:    Circle method (major/minor arcs, Weyl sums, singular series)
Source:      Overholt Ch4 — no verbatim text
Type:        additive-problem decomposition
Why it matters: local density (major arcs) must be matched by cancellation (minor arcs).
ANT role:    ∫_0^1 = ∫_major + ∫_minor; singular series = local density product.
PVG translation: additive support geometry; the minor arc is where structure must cancel.
Wall / certificate: minor-arc cancellation — WALL-MINOR-ARC; parity limit MC-001.
Classification: Known / Boundary.
Normalized output: → Wall WALL-MINOR-ARC (+ WALL-PARITY) ; → Object (singular series / arcs, folded).
```

```text
Treasure ID: TREASURE-OVERHOLT-009
Treasure:    Perron / contour extraction
Source:      Overholt Ch5 — no verbatim text
Type:        Dirichlet-series-to-summatory transform
Why it matters: "counting is residue extraction from Dirichlet series."
ANT role:    Σ_{n≤x} a_n = (2πi)^{-1} ∫ A(s) x^s/s ds; poles → main terms.
PVG translation: contour transfer from the multiplicative series to the counting function.
Wall / certificate: contour/truncation error, then zero-free control downstream.
Classification: Known.
Normalized output: → Tool TOOL-PERRON-001.
```

```text
Treasure ID: TREASURE-OVERHOLT-010
Treasure:    Prime Number Theorem (pole at 1 + zero-free boundary)
Source:      Overholt Ch6 — no verbatim text
Type:        first prime-counting law
Why it matters: pole at s=1 gives the main term x; the zero-free boundary gives the error.
ANT role:    ψ(x) ~ x  ⟺  ζ(s)≠0 on Re s=1; error size = zero-free width.
PVG translation: prime-weight certificate; the boundary is the wall, not the pole.
Wall / certificate: strong ψ(x)−x error needs zero-free/RH — MC-002 (unsolved), WALL-ZERO-FREE.
Classification: Known / Boundary.
Normalized output: → Wall WALL-ZERO-FREE ; → Missing Certificate MC-002.
```

```text
Treasure ID: TREASURE-OVERHOLT-011
Treasure:    Siegel–Walfisz (L(s,χ), −L'/L, Landau repulsion)
Source:      Overholt Ch7 — no verbatim text
Type:        primes-in-AP distribution law
Why it matters: AP distribution is character-mode cancellation with exceptional-zero danger.
ANT role:    ψ(x;q,a) ~ x/φ(q) for q ≤ (log x)^A; Siegel zero → ineffectivity/bias.
PVG translation: residue-fiber distribution wall; the exceptional zero is a fiber anomaly.
Wall / certificate: exceptional (Siegel) zeros — WALL-SIEGEL; AP GRH-level MC-005 (and MC-002).
Classification: Known / Boundary.
Normalized output: → Wall WALL-SIEGEL ; → Tool TOOL-LFUNCTION-GENERATING-001 ; → Observable OBS-CHARACTER-001 ; → Missing Certificate MC-005.
```

```text
Treasure ID: TREASURE-OVERHOLT-012
Treasure:    Functional equations (Poisson summation, theta, Hadamard factorization, Phragmén–Lindelöf)
Source:      Overholt Ch8 — no verbatim text
Type:        archimedean/analytic transform layer
Why it matters: functional equations require gamma and archimedean structure; convexity bounds the critical strip.
ANT role:    θ-transformation ⇒ ζ functional equation; Hadamard factorization over zeros; Phragmén–Lindelöf convexity.
PVG translation: the analytic transform layer that relates s and 1−s (completed symmetry).
Wall / certificate: convexity/Lindelöf boundary — WALL-LINDELOF.
Classification: Known / Boundary.
Normalized output: → Wall WALL-LINDELOF ; → Tool (transform layer, folded).
```

```text
Treasure ID: TREASURE-OVERHOLT-013
Treasure:    Dedekind zeta / number fields (ideals, class number formula, Prime Ideal Theorem, Ikehara, Artin L)
Source:      Overholt Ch9 — no verbatim text
Type:        Euler products beyond Z
Why it matters: ideals restore Euler products over number fields; the norm is the size variable.
ANT role:    ζ_K(s)=Σ_{𝔞} N𝔞^{-s}=Π_𝔭 (1−N𝔭^{-s})^{-1}; class number formula = residue at s=1.
PVG translation: valuation geometry beyond Z (prime ideals / Frobenius fibers as axes).
Wall / certificate: Artin holomorphy and zero-control — WALL-ARTIN; MC-004.
Classification: Known / Boundary.
Normalized output: → Wall WALL-ARTIN ; → Missing Certificate MC-004.
```

```text
Treasure ID: TREASURE-OVERHOLT-014
Treasure:    Explicit formulas (Riemann/Weil, J(x), test functions)
Source:      Overholt Ch10 — no verbatim text
Type:        prime–zero accounting identity
Why it matters: poles give main terms; zeros give oscillatory errors; test functions filter visibility.
ANT role:    ψ_0(x)=x − Σ_ρ x^ρ/ρ + corrections; Weil formula pairs primes with zeros.
PVG translation: the exact accounting between prime mass, poles, and zeros.
Wall / certificate: zero location and positivity — WALL-POSITIVITY-WEIL; MC-003 (unsolved).
Classification: Known / Boundary. Explicit formulas TRANSFER the problem to zeros; they do NOT locate them.
Normalized output: → Wall WALL-POSITIVITY-WEIL ; → Tool TOOL-LFUNCTION-GENERATING-001 (generating object) ; → Missing Certificate MC-003.
```

```text
Treasure ID: TREASURE-OVERHOLT-015
Treasure:    Operational templates / classification protocol
Source:      Overholt Ch11 (supplementary; the book has 10 chapters) — no verbatim text
Type:        skill-discipline layer
Why it matters: theory becomes operational templates; the danger is confusing identity with proof.
ANT role:    problem → observable → tool → wall → certificate requirement (the working loop).
PVG translation: the certificate discipline that keeps relabeling from replacing zero-control.
Wall / certificate: "geometric relabeling does not replace zero-control" (RULE-PVG-001).
Classification: Diagnostic.
Normalized output: → Rule RULE-PVG-001 ; → Skill discipline SKILL-GOV-CERT-001.
```

**Honest classification:** Diagnostic (treasure map, retrofit layer). No RH/GRH progress. No complete-mastery claim.
