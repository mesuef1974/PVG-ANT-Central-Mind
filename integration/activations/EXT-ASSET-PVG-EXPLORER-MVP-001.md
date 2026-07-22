# External Asset Activation — PVG Explorer MVP 1.0

```text
Task ID: PVG-EXPLORER-INTERACTIVE-WEB-001
Asset ID: EXT-ASSET-PVG-EXPLORER-MVP-001
Date: 2026-07-23
Status: BUILT_EXTERNAL / VALIDATED_LOCAL / NOT_IMPORTED_AS_HEAVY_HTML
Governing program: GOAL-PVG-INVERSE-GEOMETRY-001
Phase D: NOT AUTHORIZED
```

## Exact missing capability

A professional interactive visual laboratory for the geometry of PVG rays, projective directions, Pascal layers, and vector addition.

## Smallest sufficient external asset

```text
PVG-Explorer/
  index.html
  styles.css
  app.js
  README.md
PVG-Explorer-MVP.zip
```

The application remains external in accordance with `maps/legacy-assets-routing.md`: heavy presentation may remain external while strategy, claims, and validation records remain canonical.

## Implemented capabilities

- interactive Three.js PVG space on the prime axes `2,3,5`;
- layer filtering by `Omega` and support size `omega`;
- projective reduction to primitive valuation directions;
- geometric rays for bases `2,3,5,6,12,18,30,60` and valid custom bases;
- integer and fractional exponent motion along one ray;
- point inspection with factorization, support, `Omega`, and `omega`;
- two-point vector addition displaying `nu(mn)=nu(m)+nu(n)`;
- Pascal-layer table;
- number search and PNG scene export.

## Validation

```text
JavaScript syntax check: PASS
HTTP smoke test index.html: PASS
HTTP smoke test app.js: PASS
required files present and nonempty: PASS
```

## External bundle certificate

```text
file: PVG-Explorer-MVP.zip
sha256: 3abec11502edc6db5dfc28aa0907ff26197ca6808a2f76477a796da62cee758f
```

## Scientific ceiling

- visualization and finite exploration only;
- no primality-test claim;
- no Goldbach, PNT, RH, or GRH claim or progress;
- no Phase-D dynamics authorization;
- no originality or publication-readiness claim.

## Knowledge returned to Central Mind

The projective PVG object is represented by the primitive direction

\[
\operatorname{prim}(\nu(n))=\frac{\nu(n)}{\gcd(\nu_{p_1}(n),\ldots,\nu_{p_s}(n))},
\]

and powers move linearly on one ray:

\[
\nu(a^t)=t\nu(a)
\]

for integer exponents and as a visual extension for rational/real ray parameters.

## Deactivation condition

The external asset is inactive after delivery. Further work requires a new named task and readiness decision.
