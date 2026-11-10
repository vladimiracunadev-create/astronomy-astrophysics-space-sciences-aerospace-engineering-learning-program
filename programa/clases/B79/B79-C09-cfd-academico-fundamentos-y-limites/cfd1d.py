#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C09: CFD academico 1D - volumenes finitos, orden de convergencia y limites.

Consultado (2026-11-10): NASA Glenn, Navier-Stokes resueltos con CFD; el modelo de turbulencia aproxima el tensor de tensiones.
ESTANDAR (no consultado): esquema central y esquema upwind de primer orden; orden observado p = log2(e_h / e_{h/2});
indice de convergencia de malla (GCI) de Roache con factor de seguridad 1.25.
PROBLEMA (sintetico, ilustrativo): u dphi/dx = Gamma d2phi/dx2 en [0, 1], phi(0) = 0, phi(1) = 1; Pe = u L / Gamma = 40.
Solucion exacta: phi = (exp(Pe x) - 1) / (exp(Pe) - 1). Resolucion con sistema tridiagonal (Thomas) en N celdas.
Tolerancias: orden observado central en [1.9, 2.1]; upwind en [0.8, 1.2] (mallas finas).
"""
import math, platform

PE = 40.0


def exacta(x):
    return (math.exp(PE * x) - 1) / (math.exp(PE) - 1)


def resolver(n, esquema):
    """Nodos i = 0..n con phi_0 = 0, phi_n = 1; ecuacion en nodos interiores."""
    h = 1.0 / n
    d = 1.0 / PE  # Gamma/u con u = 1
    a, b, c, r = [], [], [], []
    for i in range(1, n):
        if esquema == "central":
            lo = -d / (h * h) - 1 / (2 * h)
            hi = -d / (h * h) + 1 / (2 * h)
            di = 2 * d / (h * h)
        else:  # upwind primer orden (u > 0)
            lo = -d / (h * h) - 1 / h
            hi = -d / (h * h)
            di = 2 * d / (h * h) + 1 / h
        a.append(lo); b.append(di); c.append(hi); r.append(0.0)
    r[-1] -= c[-1] * 1.0
    m = n - 1
    for i in range(1, m):
        w = a[i] / b[i - 1]
        b[i] -= w * c[i - 1]
        r[i] -= w * r[i - 1]
    x = [0.0] * m
    x[-1] = r[-1] / b[-1]
    for i in range(m - 2, -1, -1):
        x[i] = (r[i] - c[i] * x[i + 1]) / b[i]
    return [0.0] + x + [1.0]


def error_max(phi):
    n = len(phi) - 1
    return max(abs(phi[i] - exacta(i / n)) for i in range(n + 1))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Problema SINTETICO: u phi' = Gamma phi'' en [0,1], Pe = {PE}, phi(0)=0, phi(1)=1")
    res = {}
    for esq in ("central", "upwind"):
        print(f"Esquema {esq}")
        print("    N    Pe celda   error max      orden observado   min(phi)")
        prev = None
        for n in (10, 20, 40, 80, 160, 320):
            phi = resolver(n, esq)
            e = error_max(phi)
            orden = "      -" if prev is None else f"{math.log2(prev / e):7.3f}"
            print(f" {n:4d}   {PE / n:6.2f}    {e:.4e}      {orden}          {min(phi):8.5f}")
            res.setdefault(esq, []).append((n, e, min(phi)))
            prev = e
    # ordenes finales
    oc = math.log2(res["central"][-2][1] / res["central"][-1][1])
    ou = math.log2(res["upwind"][-2][1] / res["upwind"][-1][1])
    print(f"Orden observado en las mallas finas: central = {oc:.3f} ; upwind = {ou:.3f}")
    # GCI con tres mallas finas (upwind)
    e1, e2, e3 = res["upwind"][-1][1], res["upwind"][-2][1], res["upwind"][-3][1]
    # estimacion con el valor en x = 0.95 (cantidad de interes), no con el error exacto
    q = []
    for n in (80, 160, 320):
        phi = resolver(n, "upwind")
        q.append(phi[int(round(0.95 * n))])
    p_obs = math.log2(abs(q[0] - q[1]) / abs(q[1] - q[2]))
    gci = 1.25 * abs(q[2] - q[1]) / q[2] / (2 ** p_obs - 1)
    print(f"GCI (upwind, phi(0.95) con 80/160/320 celdas): orden = {p_obs:.3f} ; GCI fino = {100 * gci:.3f} %")
    print(f" phi(0.95): mallas = {q[0]:.6f}, {q[1]:.6f}, {q[2]:.6f} ; exacta = {exacta(0.95):.6f}")
    # verificacion no es validacion: modelo equivocado (solo difusion) convergido en malla
    n = 320
    mal = [i / n for i in range(n + 1)]
    e_mal = max(abs(mal[i] - exacta(i / n)) for i in range(n + 1))
    print(f"Modelo equivocado (solo difusion, convergido en malla): error max respecto a la exacta = {e_mal:.3f}")
    assert 1.9 < oc < 2.1 and 0.8 < ou < 1.2
    assert res["central"][0][2] < -0.01  # oscilaciones con Pe de celda > 2
    assert all(m >= -1e-12 for _, _, m in res["upwind"])
    assert e_mal > 0.1
    print("Pruebas superadas.")


main()
