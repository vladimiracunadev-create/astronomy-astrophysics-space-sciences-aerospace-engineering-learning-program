#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C11: frente de Pareto entre tiempo de vuelo y carga util para disenos de bajo empuje.

Datos: g0 = 9,80665 m/s^2 (convencional, no consultado). Todo lo demas es SINTETICO e ILUSTRATIVO (semilla 20260810).
Modelo (el de B81-C10): m0 = 1000 kg, dv = 4000 m/s, eta = 0,6; aceleracion a (log-uniforme en [1e-4, 5e-3] m/s^2), Isp en {1500, 2500, 3500} s,
masa especifica de potencia alfa en [15, 40] kg/kW. Objetivos a minimizar: tiempo t = dv/a [dias] y menos la carga util [kg]; se descartan disenos con carga util <= 0.
Muestra: 300 disenos. Frente: conjunto de no dominados, por (a) doble bucle y (b) barrido ordenado por tiempo. Hipervolumen respecto a (t_ref = 2000 d, carga util = 0)
por barrido exacto y por Monte Carlo (semilla fija). Punto de rodilla: maxima distancia a la recta que une los extremos del frente (objetivos normalizados).
Tolerancias: los dos metodos de frente coinciden exactamente; hipervolumen MC frente al exacto < 2 %.
"""
from __future__ import annotations
import math, platform, random

G0 = 9.80665
M0, DV, ETA = 1000.0, 4000.0, 0.6


def diseno(a, isp, alfa):
    ve = G0 * isp
    P = M0 * a * ve / (2 * ETA)
    carga = M0 * math.exp(-DV / ve) - alfa / 1000.0 * P
    return DV / a / 86400.0, carga


def frente_doble(pts):
    res = []
    for i, p in enumerate(pts):
        dom = False
        for j, q in enumerate(pts):
            if i != j and q[0] <= p[0] and q[1] >= p[1] and (q[0] < p[0] or q[1] > p[1]):
                dom = True
                break
        if not dom:
            res.append(p)
    return sorted(res)


def frente_barrido(pts):
    res = []
    mejor = -1e18
    for p in sorted(pts, key=lambda z: (z[0], -z[1])):
        if p[1] > mejor:
            res.append(p)
            mejor = p[1]
    return res


def hipervolumen(fr, tref, cref):
    hv = 0.0
    for i, (t, c) in enumerate(fr):
        t_next = fr[i + 1][0] if i + 1 < len(fr) else tref
        hv += (t_next - t) * (c - cref)
    return hv


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20260810)
    pts, etiquetas = [], {}
    while len(pts) < 300:
        a = math.exp(rng.uniform(math.log(1e-4), math.log(5e-3)))
        isp = rng.choice((1500, 2500, 3500))
        alfa = rng.uniform(15, 40)
        t, c = diseno(a, isp, alfa)
        if c > 0:
            pts.append((t, c))
            etiquetas[(t, c)] = (a, isp, alfa)
    f1 = frente_doble(pts)
    f2 = frente_barrido(pts)
    print(f"Muestra SINTETICA: {len(pts)} disenos (semilla 20260810) ; frente doble bucle = {len(f1)} puntos ; frente por barrido = {len(f2)} puntos ; coinciden: {f1 == f2}")
    tref, cref = 2000.0, 0.0
    hv = hipervolumen(f2, tref, cref)
    rng2 = random.Random(7)
    cmax = max(p[1] for p in pts)
    n = 400000
    k = 0
    for _ in range(n):
        t = rng2.uniform(0, tref)
        c = rng2.uniform(0, cmax)
        if any(p[0] <= t and p[1] >= c for p in f2):
            k += 1
    hv_mc = k / n * tref * cmax
    print(f"Hipervolumen exacto = {hv:.1f} d kg ; Monte Carlo ({n} muestras) = {hv_mc:.1f} ; diferencia relativa = {abs(hv-hv_mc)/hv:.2e}")
    t0, c0 = f2[0]; t1, c1 = f2[-1]
    def norm(p):
        return ((p[0] - t0) / (t1 - t0), (c1 - p[1]) / (c1 - c0))  # (tiempo normalizado, 'malo' de la carga util normalizado), ambos a minimizar
    mejor = (-1, None)
    for p in f2:
        x, y = norm(p)
        # recta entre extremos (0,y0)-(1,y1) en espacio normalizado: (0,1)-(1,0) para el primero/ultimo
        dist = (1 - x - y) / math.sqrt(2)  # positivo = por debajo de la recta entre extremos (mejor que el promedio)
        if dist > mejor[0]:
            mejor = (dist, p)
    a, isp, alfa = etiquetas[mejor[1]]
    print(f"Extremo rapido: t = {t0:.1f} d, carga = {c0:.1f} kg ; extremo de carga: t = {t1:.1f} d, carga = {c1:.1f} kg")
    print(f"Punto de rodilla: t = {mejor[1][0]:.1f} d, carga = {mejor[1][1]:.1f} kg (a = {a:.2e} m/s^2, Isp = {isp} s, alfa = {alfa:.1f} kg/kW)")
    print("Suma ponderada J = w t_norm + (1-w) (perdida de carga util normalizada): diseno elegido segun el peso w")
    for w in (0.1, 0.3, 0.5, 0.7, 0.9):
        elegido = min(f2, key=lambda p: w * norm(p)[0] + (1 - w) * norm(p)[1])
        print(f"  w = {w:.1f}: t = {elegido[0]:7.1f} d, carga = {elegido[1]:7.1f} kg")
    assert f1 == f2
    assert abs(hv - hv_mc) / hv < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
