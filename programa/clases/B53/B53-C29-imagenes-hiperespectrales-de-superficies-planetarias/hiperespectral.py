#!/usr/bin/env python3
"""B53-C29: desmezclado espectral de un cubo SINTETICO (20 x 20 x 50 bandas, 0.4-2.5 um). 3 miembros extremos inventados,
ruido 0.005, abundancias Dirichlet uniforme, semilla 20261109. Tolerancia: RMS medido dentro de 10 % del teorico."""
import math, platform, random

NB, NPIX, SIG = 50, 400, 0.005
LAM = [0.4 + (2.5 - 0.4) * i / (NB - 1) for i in range(NB)]

def miembros():
    e1 = [0.50 - 0.30 * math.exp(-(l - 1.0) ** 2 / 0.02) for l in LAM]
    e2 = [0.40 + 0.08 * l - 0.20 * math.exp(-(l - 2.0) ** 2 / 0.03) for l in LAM]
    e3 = [0.70 - 0.40 * math.exp(-(l - 0.6) ** 2 / 0.01) - 0.10 * math.exp(-(l - 1.5) ** 2 / 0.02) for l in LAM]
    return [e1, e2, e3]

def inv3(g):
    a, b, c = g[0]; d, e, f = g[1]; h, i, j = g[2]
    det = a * (e * j - f * i) - b * (d * j - f * h) + c * (d * i - e * h)
    return [[(e * j - f * i) / det, (c * i - b * j) / det, (b * f - c * e) / det],
            [(f * h - d * j) / det, (a * j - c * h) / det, (c * d - a * f) / det],
            [(d * i - e * h) / det, (b * h - a * i) / det, (a * e - b * d) / det]]

def mv(m, v):
    return [sum(m[i][k] * v[k] for k in range(3)) for i in range(3)]

def sam(u, v):
    return math.degrees(math.acos(sum(a * b for a, b in zip(u, v)) / math.sqrt(sum(a * a for a in u) * sum(b * b for b in v))))

def compute():
    rng = random.Random(20261109)
    E = miembros()
    G = [[sum(E[i][k] * E[j][k] for k in range(NB)) for j in range(3)] for i in range(3)]
    Gi = inv3(G)
    uno = [1.0, 1.0, 1.0]
    Giu = mv(Gi, uno)
    den = sum(Giu)
    se_u = se_c = 0.0
    neg = 0
    for _ in range(NPIX):
        w = [rng.expovariate(1.0) for _ in range(3)]
        a = [x / sum(w) for x in w]
        y = [sum(a[j] * E[j][k] for j in range(3)) + rng.gauss(0, SIG) for k in range(NB)]
        mty = [sum(E[j][k] * y[k] for k in range(NB)) for j in range(3)]
        au = mv(Gi, mty)
        ac = [au[j] + Giu[j] * (1 - sum(au)) / den for j in range(3)]
        se_u += sum((au[j] - a[j]) ** 2 for j in range(3)) / 3
        se_c += sum((ac[j] - a[j]) ** 2 for j in range(3)) / 3
        neg += any(x < 0 for x in au)
    th_u = SIG * math.sqrt(sum(Gi[i][i] for i in range(3)) / 3)
    cov_c = [[Gi[i][j] - Giu[i] * Giu[j] / den for j in range(3)] for i in range(3)]
    th_c = SIG * math.sqrt(sum(cov_c[i][i] for i in range(3)) / 3)
    return dict(rmse_u=math.sqrt(se_u / NPIX), th_u=th_u, rmse_c=math.sqrt(se_c / NPIX), th_c=th_c, neg=100 * neg / NPIX,
                sam12=sam(E[0], E[1]), sam13=sam(E[0], E[2]), sam23=sam(E[1], E[2]))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = compute()
    print(f"RMS de abundancias sin restriccion = {r['rmse_u']:.5f} (teorico {r['th_u']:.5f}) ; con suma uno = {r['rmse_c']:.5f} (teorico {r['th_c']:.5f})")
    print(f"pixeles con alguna abundancia negativa = {r['neg']:.1f} %")
    print(f"SAM entre miembros: 1-2 {r['sam12']:.2f} ; 1-3 {r['sam13']:.2f} ; 2-3 {r['sam23']:.2f} grados")
    assert abs(r["rmse_u"] / r["th_u"] - 1) < 0.10 and abs(r["rmse_c"] / r["th_c"] - 1) < 0.10 and r["rmse_c"] < r["rmse_u"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
