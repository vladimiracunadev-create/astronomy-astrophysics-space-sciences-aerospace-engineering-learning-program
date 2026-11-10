#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B80-C05: redundancia de sensores, espacio de paridad, deteccion y aislamiento de una falla de sesgo.

Datos: SINTETICOS e ILUSTRATIVOS (semilla fija 80005). Seis sensores de un eje (p. ej. acelerometros) con direcciones sinteticas
(los vertices de un hemi-icosaedro no se usan: se dan seis vectores unitarios elegidos para el ejemplo). Medicion z = H x + e + falla,
con x en R^3 (el vector medido), e ~ N(0, sigma^2 I), sigma = 0.01 (unidad arbitraria, p. ej. m/s2).
Estimador: minimos cuadrados x_hat = (H^T H)^-1 H^T z. Residuo r = (I - H (H^T H)^-1 H^T) z = P z (independiente de x).
Estadistico de deteccion: J = |r|^2 / sigma^2 ~ chi-cuadrado con n - 3 = 3 grados de libertad en ausencia de falla.
Umbral para falsa alarma 1e-3: se calcula resolviendo la funcion de distribucion chi-cuadrado de 3 grados de libertad (forma cerrada con erf).
Aislamiento: se elige el sensor i que maximiza |P_i . r|/|P_i| (correlacion del residuo con la columna i de P).
Segunda via: Monte Carlo de la tasa de falsa alarma (20000 ensayos) frente a 1e-3, y exactitud del aislamiento (500 ensayos por tamano de falla).
"""
from __future__ import annotations
import math, platform, random

SIG = 0.01
DIRS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1), (1, -1, 1), (-1, 1, 1)]


def unit(v):
    n = math.sqrt(sum(c * c for c in v))
    return [c / n for c in v]


H = [unit(d) for d in DIRS]
N = len(H)


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def inv3(M):
    a, b, c = M[0]
    d, e, f = M[1]
    g, h, i = M[2]
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    return [[(e * i - f * h) / det, (c * h - b * i) / det, (b * f - c * e) / det],
            [(f * g - d * i) / det, (a * i - c * g) / det, (c * d - a * f) / det],
            [(d * h - e * g) / det, (b * g - a * h) / det, (a * e - b * d) / det]]


HtH = mm(tr(H), H)
PINV = mm(inv3(HtH), tr(H))
Pm = mm(H, PINV)
Pres = [[(1.0 if i == j else 0.0) - Pm[i][j] for j in range(N)] for i in range(N)]


def cdf_chi2_3(x):
    return math.erf(math.sqrt(x / 2.0)) - math.sqrt(2.0 * x / math.pi) * math.exp(-x / 2.0)


def umbral(alfa):
    lo, hi = 0.0, 100.0
    for _ in range(100):
        mid = 0.5 * (lo + hi)
        if cdf_chi2_3(mid) < 1.0 - alfa:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def residuo(z):
    return [sum(Pres[i][j] * z[j] for j in range(N)) for i in range(N)]


def mide(rnd, x, fallo=None, tam=0.0):
    z = [sum(H[i][j] * x[j] for j in range(3)) + rnd.gauss(0, SIG) for i in range(N)]
    if fallo is not None:
        z[fallo] += tam
    return z


def estadistico(r):
    return sum(c * c for c in r) / SIG ** 2


def aislar(r):
    mejor, ib = -1.0, -1
    for i in range(N):
        col = [Pres[k][i] for k in range(N)]
        nc = math.sqrt(sum(c * c for c in col))
        corr = abs(sum(r[k] * col[k] for k in range(N))) / nc
        if corr > mejor:
            mejor, ib = corr, i
    return ib


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rank_trace = sum(Pres[i][i] for i in range(N))
    print(f"Datos SINTETICOS (semilla 80005): n = {N} sensores, 3 ejes -> grados de libertad de paridad = {N - 3}; traza de (I - P) = {rank_trace:.6f}")
    th = umbral(1e-3)
    print(f"Umbral chi-cuadrado (3 gl, falsa alarma 1e-3) = {th:.3f} ; verificacion F(umbral) = {cdf_chi2_3(th):.6f}")
    rnd = random.Random(80005)
    x = (1.0, -2.0, 0.5)
    fa = 0
    M = 20000
    for _ in range(M):
        r = residuo(mide(rnd, x))
        if estadistico(r) > th:
            fa += 1
    print(f"Falsa alarma observada sin falla: {fa / M:.5f} (esperada 0.00100, {M} ensayos)")
    print(" falla [sigma]   deteccion   aislamiento correcto (sensor 3 con falla)")
    res = {}
    for k in (2, 5, 10, 20):
        det = ok = 0
        T = 500
        for _ in range(T):
            r = residuo(mide(rnd, x, fallo=3, tam=k * SIG))
            if estadistico(r) > th:
                det += 1
                if aislar(r) == 3:
                    ok += 1
        res[k] = (det / T, ok / max(det, 1))
        print(f"{k:12d} {det / T:12.3f} {ok / max(det, 1):26.3f}")
    # El residuo no depende de x: mismo ruido con x distinto
    z1 = mide(random.Random(7), (0.0, 0.0, 0.0))
    z2 = mide(random.Random(7), (50.0, -30.0, 12.0))
    d = max(abs(a - b) for a, b in zip(residuo(z1), residuo(z2)))
    print(f"Diferencia maxima del residuo entre x = 0 y x = (50, -30, 12): {d:.2e}")
    assert abs(rank_trace - 3.0) < 1e-9
    assert abs(fa / M - 1e-3) < 1e-3
    assert res[20][0] > 0.99 and res[20][1] > 0.99
    assert res[2][0] < 0.2
    assert d < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
