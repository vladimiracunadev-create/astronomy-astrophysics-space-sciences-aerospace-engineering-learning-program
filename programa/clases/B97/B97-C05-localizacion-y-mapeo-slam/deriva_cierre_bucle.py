#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C05: deriva de la odometria y cierre de bucle en un grafo de poses (por mínimos cuadrados).

Todos los datos son SINTETICOS e ILUSTRATIVOS (no medidos): trayectoria cuadrada de 10 m de lado con pasos de 1 m (40 poses), ruido de odometria
sigma_o = 0.05 m por paso y eje, sesgo de 0.01 m por paso en x, restriccion de cierre con sigma_l = 0.02 m, semilla fija.
Modelo: por eje, x_{k+1} - x_k = u_k (peso 1/sigma_o^2), x_0 = 0 y x_N - x_0 = 0 (peso 1/sigma_l^2). Minimos cuadrados lineales por ecuaciones normales
con eliminacion de Gauss; los dos ejes son independientes.
Segunda via: solucion analitica por simetria, x_N = e0 sigma_l^2 / (sigma_l^2 + N sigma_o^2), con e0 el error de la odometria pura (tolerancia 1e-9).
Unidades SI; sistema de referencia plano, origen en el punto de partida.
"""
from __future__ import annotations
import math, platform, random

LADO, PASO, SO, SL, SESGO, SEMILLA = 10.0, 1.0, 0.05, 0.02, 0.01, 20261110   # ILUSTRATIVOS / SINTETICOS


def trayectoria():
    n = int(LADO / PASO)
    pasos = [(PASO, 0.0)] * n + [(0.0, PASO)] * n + [(-PASO, 0.0)] * n + [(0.0, -PASO)] * n
    return pasos


def resolver(u, so, sl):
    """Resuelve el eje: incognitas x_1..x_N con x_0 = 0 y cierre x_N = 0."""
    n = len(u)
    a = [[0.0] * n for _ in range(n)]
    b = [0.0] * n
    wo, wl = 1 / so ** 2, 1 / sl ** 2
    for k in range(n):                       # restriccion x_{k+1} - x_k = u_k, con x_0 = 0 (indice -1)
        i, j = k - 1, k
        if i >= 0:
            a[i][i] += wo; a[i][j] -= wo; a[j][i] -= wo
            b[i] -= wo * u[k]
        a[j][j] += wo
        b[j] += wo * u[k]
    a[n - 1][n - 1] += wl                    # cierre: x_N = 0
    for c in range(n):                       # Gauss con pivoteo parcial
        p = max(range(c, n), key=lambda r: abs(a[r][c]))
        a[c], a[p] = a[p], a[c]; b[c], b[p] = b[p], b[c]
        for r in range(c + 1, n):
            f = a[r][c] / a[c][c]
            for k in range(c, n):
                a[r][k] -= f * a[c][k]
            b[r] -= f * b[c]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (b[r] - sum(a[r][k] * x[k] for k in range(r + 1, n))) / a[r][r]
    return x


def calc():
    rng = random.Random(SEMILLA)
    pasos = trayectoria()
    n = len(pasos)
    ux = [p[0] + SESGO + rng.gauss(0, SO) for p in pasos]
    uy = [p[1] + rng.gauss(0, SO) for p in pasos]
    vx, vy = [0.0], [0.0]                    # verdad y odometria pura
    tx, ty = [0.0], [0.0]
    for k in range(n):
        tx.append(tx[-1] + pasos[k][0]); ty.append(ty[-1] + pasos[k][1])
        vx.append(vx[-1] + ux[k]); vy.append(vy[-1] + uy[k])
    ox = [0.0] + resolver(ux, SO, SL)
    oy = [0.0] + resolver(uy, SO, SL)
    err_dr = math.hypot(vx[-1], vy[-1])
    err_opt = math.hypot(ox[-1], oy[-1])
    rms = lambda xs, ys: math.sqrt(sum((xs[i] - tx[i]) ** 2 + (ys[i] - ty[i]) ** 2 for i in range(n + 1)) / (n + 1))
    ex_teo = vx[-1] * SL ** 2 / (SL ** 2 + n * SO ** 2)
    ey_teo = vy[-1] * SL ** 2 / (SL ** 2 + n * SO ** 2)
    return dict(n=n, err_dr=err_dr, err_opt=err_opt, rms_dr=rms(vx, vy), rms_opt=rms(ox, oy), dif=max(abs(ox[-1] - ex_teo), abs(oy[-1] - ey_teo)),
                e0x=vx[-1], e0y=vy[-1], factor=SL ** 2 / (SL ** 2 + n * SO ** 2), razon=err_dr / err_opt, rms_razon=rms(vx, vy) / rms(ox, oy))


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: cuadrado de {LADO} m, {r['n']} pasos de {PASO} m; sigma_o = {SO} m; sesgo {SESGO} m/paso en x; sigma_l = {SL} m; semilla {SEMILLA}")
    print(f"Odometria pura: error de cierre = {r['err_dr']:.4f} m (e0x = {r['e0x']:.4f}, e0y = {r['e0y']:.4f}); RMS de la trayectoria = {r['rms_dr']:.4f} m")
    print(f"Con cierre de bucle: error de cierre = {r['err_opt']:.4f} m; RMS de la trayectoria = {r['rms_opt']:.4f} m")
    print(f"Factor analitico del cierre = {r['factor']:.5f}; diferencia con la solucion numerica = {r['dif']:.2e} m")
    print(f"Mejora del error de cierre: x{r['razon']:.1f}; mejora del RMS: x{r['rms_razon']:.2f}")
    assert r["dif"] < 1e-9 and r["err_opt"] < r["err_dr"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
