#!/usr/bin/env python3
"""Recompute every quantity reported in reports/IGD001_RESULT.md from data/dmulti_out.txt.

Exits non-zero if any reported number fails to reproduce, or if the h=1 verdict is not
DATA-CONSISTENT. This script verifies internal consistency of the pass; it does not
verify the theorem, and it does not read any primary text.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, os.pardir, "data", "dmulti_out.txt")

SHIFTS = [1, 2, 6, 12, 30]
A0 = 6 / math.pi**2
GAMMA = 0.5772156649015329
ZETA2 = math.pi**2 / 6
ZETA2P = -0.9375482543158438          # zeta'(2)
K_STAR = 2 * (2 * GAMMA - 1 - 2 * (ZETA2P / ZETA2))

SCENARIOS = {
    "CLAIMED": K_STAR,
    "Z-TERM-OMITTED": 2 * (2 * GAMMA - 1),
    "Z-COEFFICIENT-HALF": 2 * (2 * GAMMA - 1 - ZETA2P / ZETA2),
    "Z-SIGN-REVERSED": 2 * (2 * GAMMA - 1 + 2 * (ZETA2P / ZETA2)),
}


def divisors(h):
    return [d for d in range(1, h + 1) if h % d == 0]


def sigmas(h):
    ds = divisors(h)
    s = sum(1.0 / d for d in ds)
    sp = sum(math.log(d) / d for d in ds)
    spp = sum(math.log(d) ** 2 / d for d in ds)
    return s, sp, spp


def load():
    d = {}
    with open(DATA) as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            p = line.split()
            d[int(p[0])] = {h: int(v) for h, v in zip(SHIFTS, p[1:])}
    return d


def main():
    D = load()
    xs = sorted(D)
    fail = []

    print("K_star = %.10f" % K_STAR)
    print("a_0    = %.13f\n" % A0)

    # --- Phase 1: h = 1 -----------------------------------------------------
    Y = {x: D[x][1] / x - A0 * math.log(x) ** 2 for x in xs}
    print("x            D_1(x)              Y_1(x)")
    for x in xs:
        print("1e%-2d %20d      %12.6f" % (round(math.log10(x)), D[x][1], Y[x]))

    def K(x1, x2):
        return (Y[x2] - Y[x1]) / (A0 * math.log(x2 / x1))

    fam = [(xs[0], xs[-1]), (xs[1], xs[-1]), (xs[0], xs[-2])]
    ks = [K(a, b) for a, b in fam]
    U = max(ks) - min(ks)
    print("\nJUDGMENT FAMILY")
    for (a, b), k in zip(fam, ks):
        print("  Khat(1e%d,1e%d) = %.8f  dev %+.8f"
              % (round(math.log10(a)), round(math.log10(b)), k, k - K_STAR))
    print("  U_K^judgment  = %.8f  (rel %.2e)" % (U, U / K_STAR))

    print("\nDRIFT DIAGNOSTIC")
    ds = []
    for j in range(6, 10):
        k = K(10**j, 10**(j + 1))
        ds.append(abs(k - K_STAR))
        print("  Khat(1e%d,1e%d) = %.8f  d_%d = %.8f" % (j, j + 1, k, j, ds[-1]))
    drift_ok = ds[-1] < ds[0]
    rises = [ds[i + 1] > ds[i] for i in range(len(ds) - 1)]
    two_rises = any(rises[i] and rises[i + 1] for i in range(len(rises) - 1))
    print("  d_9 < d_6: %s   two consecutive rises: %s" % (drift_ok, two_rises))

    print("\nREFERENCE SCENARIOS")
    for name, kv in SCENARIOS.items():
        print("  %-20s K=%+10.6f  |Khat_primary - K| = %.6f" % (name, kv, abs(ks[0] - kv)))
    separation = min(abs(ks[0] - v) for n, v in SCENARIOS.items() if n != "CLAIMED")

    consistent = (abs(ks[0] - K_STAR) < 1e-2 and drift_ok and not two_rises
                  and separation > 100 * U)
    verdict = "K-H1-DATA-CONSISTENT" if consistent else "K-H1-DATA-INCONSISTENT"
    print("\nVERDICT: %s" % verdict)
    if not consistent:
        fail.append("h=1 verdict")

    # --- Second-order constant at h = 1 -------------------------------------
    N = 2000000
    z = zp = zpp = 0.0
    for n in range(1, N + 1):
        l = math.log(n)
        t = 1.0 / (n * n)
        z += t
        zp -= l * t
        zpp += l * l * t
    lg = math.log(N)
    z += 1.0 / N
    zp -= (lg + 1) / N
    zpp += (lg * lg + 2 * lg + 2) / N
    Z = zp / z
    A = 2 * GAMMA - 2 * Z
    C1_star = A * A - 2 * A + 2 - 4 * (zpp / z - Z * Z)
    C1_meas = (Y[xs[-1]] - A0 * K_STAR * math.log(xs[-1])) / A0
    print("\nC_1* predicted = %.7f   C_1 measured = %.7f   diff %.2e"
          % (C1_star, C1_meas, C1_star - C1_meas))
    if abs(C1_star - C1_meas) > 1e-3:
        fail.append("C_1* corroboration")

    # --- Phase 2: blinded shifts -------------------------------------------
    print("\nBLINDED SHIFTS  h = 2, 6, 12, 30")
    print("  h    R_h(1e10)    first-order   rel      3-term model  rel")
    ratios = []
    for h in SHIFTS[1:]:
        s, sp, spp = sigmas(h)
        Q = 2 * K_STAR * sp / s + 4 * spp / s
        x = xs[-1]
        L = math.log(x)
        R = D[x][h] / D[x][1]
        p1 = s - 4 * sp / L
        p2 = p1 + s * Q / L**2
        ratios.append((R - p1) / (s * Q / L**2))
        print("  %2d  %.7f  %.7f  %+.2e  %.7f  %+.2e"
              % (h, R, p1, (R - p1) / p1, p2, (R - p2) / p2))
        if abs((R - p2) / p2) > 5e-3:
            fail.append("3-term model at h=%d" % h)
    spread = max(ratios) - min(ratios)
    print("  residual/predicted-Q ratios: " + " ".join("%.4f" % r for r in ratios))
    print("  spread across shifts = %.4f (h-independence of the residual)" % spread)
    if spread > 0.02:
        fail.append("h-independence of residual")

    print("\nINGHAM-GATE = NOT-ATTEMPTED")
    print("PVG-CONTRIBUTION = NOT-SHOWN")

    if fail:
        print("\nFAILED CHECKS: " + ", ".join(fail))
        return 1
    print("\nAll reported quantities reproduce.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
