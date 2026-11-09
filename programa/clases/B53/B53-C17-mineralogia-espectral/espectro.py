#!/usr/bin/env python3
"""B53-C17: banda de absorcion SINTETICA. Continuo 0.30 + 0.05 (lam - 0.7); banda gaussiana d = 0.25 en 1.05 um, sigma = 0.08 um;
ruido 0.003. Semilla 20261109, 500 repeticiones. Tolerancias: sesgo del centro < 0.002 um; de profundidad < 0.01."""
import math, platform, random

LAM = [0.70 + 0.005 * i for i in range(181)]
L0, D0, S0, NOISE = 1.05, 0.25, 0.08, 0.003

def espectro(rng, ruido):
    return [(0.30 + 0.05 * (l - 0.7)) * (1 - D0 * math.exp(-(l - L0) ** 2 / (2 * S0 ** 2))) + (rng.gauss(0, NOISE) if ruido else 0.0) for l in LAM]

def mc(xs, ys, grado):
    n = grado + 1
    a = [[sum(x ** (i + j) for x in xs) for j in range(n)] for i in range(n)]
    b = [sum(y * x ** i for x, y in zip(xs, ys)) for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(a[r][i]))
        a[i], a[p], b[i], b[p] = a[p], a[i], b[p], b[i]
        for r in range(i + 1, n):
            f = a[r][i] / a[i][i]
            for c in range(i, n):
                a[r][c] -= f * a[i][c]
            b[r] -= f * b[i]
    s = [0.0] * n
    for i in range(n - 1, -1, -1):
        s[i] = (b[i] - sum(a[i][j] * s[j] for j in range(i + 1, n))) / a[i][i]
    return s

def medir(esp):
    sh = [(l, r) for l, r in zip(LAM, esp) if 0.72 <= l <= 0.78 or 1.38 <= l <= 1.45]
    c0, c1 = mc([l for l, _ in sh], [r for _, r in sh], 1)
    rem = [r / (c0 + c1 * l) for l, r in zip(LAM, esp)]
    v = [(l - L0, r) for l, r in zip(LAM, rem) if abs(l - L0) <= 0.06 + 1e-9]
    c, b, a = mc([x for x, _ in v], [y for _, y in v], 2)
    xm = -b / (2 * a)
    return L0 + xm, 1 - (c + b * xm + a * xm * xm)

def compute():
    rng = random.Random(20261109)
    c0, d0 = medir(espectro(rng, False))
    cs, ds = [], []
    for _ in range(500):
        c, d = medir(espectro(rng, True))
        cs.append(c); ds.append(d)
    m = lambda v: sum(v) / len(v)
    sd = lambda v: math.sqrt(sum((e - m(v)) ** 2 for e in v) / (len(v) - 1))
    return dict(c0=c0, d0=d0, c_mean=m(cs), c_sd=sd(cs), d_mean=m(ds), d_sd=sd(ds), c_b=m(cs) - L0, d_b=m(ds) - D0)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"sin ruido: centro = {r['c0']:.5f} um ; profundidad = {r['d0']:.5f} (verdaderos 1.05000 y 0.25000)")
    print(f"500 espectros: centro = {r['c_mean']:.5f} +- {r['c_sd']:.5f} um (sesgo {r['c_b']:+.5f}) ; profundidad = {r['d_mean']:.5f} +- {r['d_sd']:.5f} (sesgo {r['d_b']:+.5f})")
    assert abs(r["c_b"]) < 0.002 and abs(r["d_b"]) < 0.01
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
