#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C24: fotometria por ajuste de PSF de dos estrellas mezcladas, frente a la apertura.

Datos: todo SINTETICO e ILUSTRATIVO (semilla 20261109): imagen de 21 x 21 pixeles con dos estrellas de sigma 2,0 pixeles separadas 3,0 pixeles (F1 = 3000 e-, F2 = 1000 e-), cielo de 20 e-/pixel,
ruido de lectura de 5 e- y ruido de fotones gaussiano. No es un campo real ni un codigo de produccion (no se reproduce ningun paquete como DAOPHOT).
Modelo: D = F1 P1 + F2 P2 + B con P gaussianas normalizadas muestreadas en el centro del pixel; ajuste lineal ponderado de (F1, F2, B) con posiciones y PSF conocidas; covarianza (A^T W A)^-1;
posicion de la segunda estrella por rejilla de chi cuadrado y refinamiento parabolico.
Supuestos: PSF conocida, ruido independiente con varianza del modelo verdadero (pesos fijos). Validez: una PSF real no es gaussiana y debe construirse a partir de estrellas aisladas.
Tolerancia: dispersion Monte Carlo de los flujos frente a la covarianza formal a 8 %; la apertura sobreestima F1 en mas de 10 %; el ajuste no tiene sesgo significativo.
"""
from __future__ import annotations
import math, platform, random, sys

SEMILLA = 20261109
L = 21
SIG = 2.0
X1, Y1 = 8.5, 10.0
SEP = 3.0
F1, F2 = 3000.0, 1000.0
B = 20.0
RN = 5.0
NSIM = 600


def psf(cx, cy):
    out = []
    for j in range(L):
        for i in range(L):
            out.append(math.exp(-0.5 * ((i - cx) ** 2 + (j - cy) ** 2) / SIG ** 2) / (2 * math.pi * SIG ** 2))
    return out


def resolver3(A, b):
    n = 3
    M = [A[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1):
                M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x


def inv3(A):
    cols = []
    for k in range(3):
        e = [1.0 if i == k else 0.0 for i in range(3)]
        cols.append(resolver3(A, e))
    return [[cols[j][i] for j in range(3)] for i in range(3)]


def normal(base, D, w):
    A = [[sum(base[i][p] * base[j][p] * w[p] for p in range(len(D))) for j in range(3)] for i in range(3)]
    b = [sum(base[i][p] * D[p] * w[p] for p in range(len(D))) for i in range(3)]
    return A, b


def chi2(base, D, w, x):
    return sum(w[p] * (D[p] - sum(x[i] * base[i][p] for i in range(3))) ** 2 for p in range(len(D)))


def calcular():
    rnd = random.Random(SEMILLA)
    n = L * L
    P1, P2 = psf(X1, Y1), psf(X1 + SEP, Y1)
    uno = [1.0] * n
    verd = [F1 * P1[p] + F2 * P2[p] + B for p in range(n)]
    w = [1.0 / (verd[p] + RN ** 2) for p in range(n)]
    A, _ = normal([P1, P2, uno], verd, w)
    cov = inv3(A)
    r = {"cov": cov}
    r["sig_F1"], r["sig_F2"] = math.sqrt(cov[0][0]), math.sqrt(cov[1][1])
    r["corr12"] = cov[0][1] / math.sqrt(cov[0][0] * cov[1][1])
    r["ap_contam"] = None
    # apertura de radio 4 centrada en la estrella 1
    ap = [j * L + i for j in range(L) for i in range(L) if math.hypot(i - X1, j - Y1) <= 4.0]
    frac1 = sum(P1[p] for p in ap)
    r["ap_n"] = len(ap)
    r["frac1"] = frac1
    cont2 = sum(F2 * P2[p] for p in ap)
    r["ap_sesgo_pred"] = cont2 / frac1
    est_ap, est_psf, est1, est2, pos = [], [], [], [], []
    desplazamientos = [d * 0.1 for d in range(-4, 5)]
    for _ in range(NSIM):
        D = [rnd.gauss(verd[p], math.sqrt(verd[p] + RN ** 2)) for p in range(n)]
        est_ap.append((sum(D[p] - B for p in ap)) / frac1)
        A, b = normal([P1, P2, uno], D, w)
        x = resolver3(A, b)
        est1.append(x[0])
        est2.append(x[1])
        # posicion de la estrella 2
        ch = []
        for d in desplazamientos:
            Q2 = psf(X1 + SEP + d, Y1)
            Ad, bd = normal([P1, Q2, uno], D, w)
            xd = resolver3(Ad, bd)
            ch.append(chi2([P1, Q2, uno], D, w, xd))
        j = min(range(len(ch)), key=lambda t: ch[t])
        if 0 < j < len(ch) - 1:
            y0, y1, y2 = ch[j - 1], ch[j], ch[j + 1]
            dd = 0.5 * (y0 - y2) / (y0 - 2 * y1 + y2)
        else:
            dd = 0.0
        pos.append((j + dd - 4) * 0.1)
    def sd(v):
        m = sum(v) / len(v)
        return math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1)), m
    r["mc1"], r["mc2"] = sd(est1), sd(est2)
    r["mc_ap"] = sd(est_ap)
    r["mc_pos"] = sd(pos)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"covarianza formal: sigma_F1 = {r['sig_F1']:.2f} e- ; sigma_F2 = {r['sig_F2']:.2f} e- ; correlacion F1-F2 = {r['corr12']:.3f}")
    print(f"apertura de radio 4 px ({r['ap_n']} pixeles, fraccion de F1 = {r['frac1']:.4f}): sesgo previsto por la vecina = {r['ap_sesgo_pred']:.1f} e-")
    print(f"{'metodo':>22} {'media F1':>9} {'sigma F1':>9} {'media F2':>9} {'sigma F2':>9}")
    print(f"{'ajuste de PSF':>22} {r['mc1'][1]:9.1f} {r['mc1'][0]:9.2f} {r['mc2'][1]:9.1f} {r['mc2'][0]:9.2f}")
    print(f"{'apertura (F1 solo)':>22} {r['mc_ap'][1]:9.1f} {r['mc_ap'][0]:9.2f}")
    print(f"posicion de la estrella 2 (desplazamiento respecto de lo verdadero, px): media {r['mc_pos'][1]:+.4f} ; sigma {r['mc_pos'][0]:.4f}")
    assert abs(r["mc1"][0] / r["sig_F1"] - 1) < 0.08 and abs(r["mc2"][0] / r["sig_F2"] - 1) < 0.08
    assert abs(r["mc1"][1] - F1) < 4 * r["mc1"][0] / math.sqrt(NSIM)
    assert abs(r["mc2"][1] - F2) < 4 * r["mc2"][0] / math.sqrt(NSIM)
    assert r["mc_ap"][1] > 1.10 * F1
    assert abs(r["mc_ap"][1] - F1 - r["ap_sesgo_pred"]) < 4 * r["mc_ap"][0] / math.sqrt(NSIM) + 1.0
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
