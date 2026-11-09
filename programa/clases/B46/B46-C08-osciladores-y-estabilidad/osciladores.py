#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C08: desviacion de Allan de ruido blanco de frecuencia y de marcha aleatoria, por dos vias.

Datos: ninguno externo. Las series son SINTETICAS (semilla 20261109; amplitud de 1e-12 por muestra). La definicion de la varianza de Allan en
terminos de frecuencia fraccional y de datos de fase se consulto en Wikipedia (Allan variance) el 2026-11-09.
Modelo: y_k fraccional (ruido blanco, o marcha aleatoria = suma acumulada de ruido blanco); sigma_y^2(m tau0) = 1/2 <(ybar_{k+m} - ybar_k)^2>
(via frecuencia) y = <(x_{k+2m} - 2 x_{k+m} + x_k)^2>/(2 (m tau0)^2) con x = tau0 * suma de y (via fase). Pendientes del ajuste log-log.
Supuestos: sin tiempo muerto, estimador sin solapamiento. Validez: orientativa.
Tolerancia: ambas vias coinciden a 1e-9 relativo; pendiente de ruido blanco -0,5 +/- 0,05 y de marcha aleatoria +0,5 +/- 0,08.
"""
from __future__ import annotations
import math, platform, random

TAU0 = 1.0

def adev_freq(y, m):
    n = len(y) // m
    yb = [sum(y[i * m:(i + 1) * m]) / m for i in range(n)]
    d = [(yb[i + 1] - yb[i]) ** 2 for i in range(n - 1)]
    return math.sqrt(0.5 * sum(d) / len(d))

def adev_fase(x, m):
    # x[i] = fase en tiempo i*tau0 ; datos a paso m
    xs = x[::m]
    d = [(xs[i + 2] - 2 * xs[i + 1] + xs[i]) ** 2 for i in range(len(xs) - 2)]
    tau = m * TAU0
    return math.sqrt(sum(d) / len(d) / (2 * tau * tau))

def pend(taus, vals):
    lx = [math.log(t) for t in taus]
    ly = [math.log(v) for v in vals]
    mx, my = sum(lx) / len(lx), sum(ly) / len(ly)
    return sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / sum((a - mx) ** 2 for a in lx)

def calc():
    rng = random.Random(20261109)
    n = 2 ** 16
    ms = [1, 2, 4, 8, 16, 32, 64]
    out = {}
    for tipo in ("blanco", "marcha"):
        w = [rng.gauss(0, 1e-12) for _ in range(n)]
        if tipo == "blanco":
            y = w
        else:
            y, s = [], 0.0
            for v in w:
                s += v
                y.append(s)
        x = [0.0]
        for v in y:
            x.append(x[-1] + v * TAU0)
        af = [adev_freq(y, m) for m in ms]
        ap = [adev_fase(x, m) for m in ms]
        out[tipo] = dict(af=af, ap=ap, pend=pend([m * TAU0 for m in ms], af))
    return dict(ms=ms, out=out)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for tipo, d in r["out"].items():
        print(f"ruido {tipo}: pendiente log-log = {d['pend']:.3f}")
        print(f"{'tau [s]':>8} {'ADEV (frecuencia)':>19} {'ADEV (fase)':>13} {'cociente':>9}")
        for m, a, b in zip(r["ms"], d["af"], d["ap"]):
            print(f"{m*TAU0:8.0f} {a:19.4e} {b:13.4e} {a/b:9.6f}")
    b, mr = r["out"]["blanco"], r["out"]["marcha"]
    for d in (b, mr):
        for a, c in zip(d["af"], d["ap"]):
            assert abs(a / c - 1) < 1e-9
    assert abs(b["pend"] + 0.5) < 0.05
    assert abs(mr["pend"] - 0.5) < 0.08
    assert abs(b["af"][0] / 1e-12 - 1) < 0.05
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
