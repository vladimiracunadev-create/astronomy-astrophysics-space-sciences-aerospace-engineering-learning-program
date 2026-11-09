#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C22: interferometria de superficie: cuatro pasos, desenvolvimiento de fase y mapa de error de forma.

Datos: SINTETICOS (superficie con inclinacion de 1500 nm en x y 600 nm en y, desenfoque de 800 nm, astigmatismo de 40 nm, esferica de 25 nm; ruido de fase gaussiano de 0,02 rad; malla 64 x 64; semilla 20261109).
lambda = 632,8 nm (laser de helio-neon, valor de uso general no consultado aqui). Ningun interferograma real.
Modelo: doble paso, fase phi = 4 pi h/lambda; cuatro interferogramas I_k = A + B cos(phi + k pi/2); phi = atan2(I4 - I2, I1 - I3); desenvolvimiento por filas y alineacion de filas; ajuste por minimos cuadrados
de piston, inclinaciones y desenfoque (1, x, y, r^2) sobre el circulo; PV y RMS del resto.
Verificacion independiente: el mismo ajuste aplicado a la superficie verdadera (sin interferometria) da el valor de referencia; numero de franjas = PV/(lambda/2).
Supuestos: desplazamientos de fase exactos, sin errores de vibracion ni de calibracion, fase pequena por pixel. Validez: gradientes de fase < pi por pixel.
Tolerancia: RMS recuperado frente a RMS verdadero, 1 nm; diferencia RMS punto a punto menor que 2 nm.
"""
from __future__ import annotations
import math, platform, random

LAM = 632.8; M = 64

def verdadera(x, y):
    r2 = x * x + y * y
    return 1500 * x + 600 * y + 800 * r2 + 40 * (x * x - y * y) + 25 * (6 * r2 * r2 - 6 * r2 + 1)

def solve(Am, b):
    n = len(b)
    Mx = [Am[i][:] + [b[i]] for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(Mx[r][i])); Mx[i], Mx[p] = Mx[p], Mx[i]
        for r in range(i + 1, n):
            f = Mx[r][i] / Mx[i][i]
            for c in range(i, n + 1): Mx[r][c] -= f * Mx[i][c]
    x = [0.0] * n
    for i in range(n - 1, -1, -1): x[i] = (Mx[i][n] - sum(Mx[i][j] * x[j] for j in range(i + 1, n))) / Mx[i][i]
    return x

def ajustar(h, pts):
    base = lambda x, y: (1.0, x, y, x * x + y * y)
    A = [[0.0] * 4 for _ in range(4)]; b = [0.0] * 4
    for (i, j, x, y) in pts:
        f = base(x, y)
        for a in range(4):
            b[a] += f[a] * h[i][j]
            for c in range(4): A[a][c] += f[a] * f[c]
    co = solve(A, b)
    res = {}
    for (i, j, x, y) in pts:
        f = base(x, y)
        res[(i, j)] = h[i][j] - sum(co[a] * f[a] for a in range(4))
    v = list(res.values()); m = sum(v) / len(v)
    rms = math.sqrt(sum((q - m) ** 2 for q in v) / len(v))
    return rms, max(v) - min(v), res

def calc():
    rng = random.Random(20261109)
    xs = [(-1 + 2 * (j + 0.5) / M) for j in range(M)]
    h = [[verdadera(xs[j], xs[i]) for j in range(M)] for i in range(M)]
    phi = [[4 * math.pi * h[i][j] / LAM for j in range(M)] for i in range(M)]
    fase = [[0.0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            p = phi[i][j] + rng.gauss(0, 0.02)
            I = [2 + 1.0 * math.cos(p + k * math.pi / 2) for k in range(4)]
            fase[i][j] = math.atan2(I[3] - I[1], I[0] - I[2])
    des = [[0.0] * M for _ in range(M)]
    for i in range(M):
        acc = fase[i][0]; des[i][0] = acc
        for j in range(1, M):
            d = fase[i][j] - fase[i][j - 1]
            d -= 2 * math.pi * round(d / (2 * math.pi))
            acc += d; des[i][j] = acc
    for i in range(1, M):
        d = des[i][0] - des[i - 1][0]
        k = round(d / (2 * math.pi))
        for j in range(M): des[i][j] -= 2 * math.pi * k
    # alinear al verdadero en el pixel central modulo 2 pi y convertir a nm
    ci = M // 2; cj = M // 2
    k0 = round((des[ci][cj] - phi[ci][cj]) / (2 * math.pi))
    rec = [[(des[i][j] - 2 * math.pi * k0) * LAM / (4 * math.pi) for j in range(M)] for i in range(M)]
    pts = [(i, j, xs[j], xs[i]) for i in range(M) for j in range(M) if xs[j] ** 2 + xs[i] ** 2 <= 1.0]
    rms_t, pv_t, res_t = ajustar(h, pts)
    rms_r, pv_r, res_r = ajustar(rec, pts)
    dif = [res_r[k] - res_t[k] for k in res_t]; md = sum(dif) / len(dif)
    rms_dif = math.sqrt(sum((d - md) ** 2 for d in dif) / len(dif))
    r = dict(puntos=len(pts), rms_verdadero=rms_t, pv_verdadero=pv_t, rms_recuperado=rms_r, pv_recuperado=pv_r, rms_diferencia=rms_dif)
    r["franjas_totales"] = (max(max(f) for f in h) - min(min(f) for f in h)) / (LAM / 2)
    r["franjas_resto"] = pv_t / (LAM / 2)
    r["rms_ondas"] = rms_t / LAM
    r["frente_rms_nm"] = 2 * rms_t
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        print(f"{k} = {v:.6g}")
    assert abs(r["rms_recuperado"] - r["rms_verdadero"]) < 1.0
    assert r["rms_diferencia"] < 2.0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
