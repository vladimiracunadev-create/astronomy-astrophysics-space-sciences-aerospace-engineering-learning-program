#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B34-C09: alineacion temporal de curvas de luz de tres instrumentos con distinta cadencia y retardo.

Datos: ninguna constante fisica. Las curvas de luz sinteticas (pulso gaussiano de una fulguracion), las cadencias (2 s, 10 s y 24 s), los retardos (0, 14 s y -8 s), el ruido (3 %) y la semilla fija son
ILUSTRATIVOS (sinteticos); no se integra ningun instrumento real.
Modelo: remuestreo a una malla comun de 1 s por interpolacion lineal; correlacion cruzada normalizada para retardos de -60 a 60 s con paso de 1 s; refinamiento sub-muestra con el vertice de la parabola
ajustada a los tres puntos mas altos; incertidumbre por Monte Carlo (200 repeticiones de ruido).
Supuestos: la misma forma en todos los instrumentos y un retardo constante. Validez: ilustrativa.
Tolerancia: retardos recuperados dentro de 1.5 s de los impuestos.
"""
from __future__ import annotations
import math, platform, random, sys

def pulso(t, t0=300.0, s=30.0):
    return math.exp(-0.5 * ((t - t0) / s) ** 2)

def serie(cad, ret, rng, ruido=0.03):
    ts = [i * cad for i in range(int(600 / cad) + 1)]
    return ts, [pulso(t - ret) * (1 + rng.gauss(0, ruido)) + rng.gauss(0, 0.005) for t in ts]

def remuestrea(ts, ys, malla):
    out = []
    j = 0
    for t in malla:
        while j + 1 < len(ts) - 1 and ts[j + 1] < t:
            j += 1
        if t <= ts[0]:
            out.append(ys[0])
        elif t >= ts[-1]:
            out.append(ys[-1])
        else:
            f = (t - ts[j]) / (ts[j + 1] - ts[j])
            out.append(ys[j] * (1 - f) + ys[j + 1] * f)
    return out

def retardo(a, b):
    mejor = []
    n = len(a)
    for d in range(-60, 61):
        x = [a[i] for i in range(n) if 0 <= i + d < n]
        y = [b[i + d] for i in range(n) if 0 <= i + d < n]
        mx, my = sum(x) / len(x), sum(y) / len(y)
        c = sum((p - mx) * (q - my) for p, q in zip(x, y)) / math.sqrt(sum((p - mx) ** 2 for p in x) * sum((q - my) ** 2 for q in y))
        mejor.append((c, d))
    i = max(range(len(mejor)), key=lambda k: mejor[k][0])
    if 0 < i < len(mejor) - 1:
        y0, y1, y2 = mejor[i - 1][0], mejor[i][0], mejor[i + 1][0]
        den = y0 - 2 * y1 + y2
        off = 0.5 * (y0 - y2) / den if den else 0.0
    else:
        off = 0.0
    return mejor[i][1] + off, mejor[i][0]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    malla = [float(i) for i in range(601)]
    cfg = {"A": (2.0, 0.0), "B": (10.0, 14.0), "C": (24.0, -8.0)}
    print(f"{'par':<6} {'retardo impuesto [s]':>21} {'recuperado [s]':>15} {'correlacion':>12} {'sigma (200 repeticiones) [s]':>30}")
    base = {}
    for k, (cad, ret) in cfg.items():
        ts, ys = serie(cad, ret, rng)
        base[k] = remuestrea(ts, ys, malla)
    for par in (("A", "B"), ("A", "C"), ("B", "C")):
        imp = cfg[par[1]][1] - cfg[par[0]][1]
        rec, c = retardo(base[par[0]], base[par[1]])
        rs = []
        for _ in range(200):
            m1 = remuestrea(*serie(cfg[par[0]][0], cfg[par[0]][1], rng), malla)
            m2 = remuestrea(*serie(cfg[par[1]][0], cfg[par[1]][1], rng), malla)
            rs.append(retardo(m1, m2)[0])
        m = sum(rs) / len(rs)
        sd = math.sqrt(sum((x - m) ** 2 for x in rs) / (len(rs) - 1))
        print(f"{par[0] + '-' + par[1]:<6} {imp:21.1f} {rec:15.2f} {c:12.4f} {sd:30.3f}")
        assert abs(rec - imp) < 1.5, par
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
