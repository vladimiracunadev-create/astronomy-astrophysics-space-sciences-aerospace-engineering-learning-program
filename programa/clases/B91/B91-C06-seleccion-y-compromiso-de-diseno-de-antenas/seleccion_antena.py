#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B91-C06: seleccion de antena con matriz de decision, frente de Pareto y sensibilidad a los pesos.

Sin datos publicados: candidatos, masas, costos y eficiencias son SINTETICOS (ilustrativos, no de productos reales).
Requisito SINTETICO: enlace de bajada a 8.4 GHz que exige G >= 30 dBi hacia la Tierra, envolvente de lado maximo 1.0 m, masa <= 6 kg.
Ganancia por apertura: G = eta (pi D/lambda)^2 para reflector, bocina y parche-arreglo (con su eficiencia sintetica); helice: G aprox 10.8 + 10 log(N (C/lambda)^2 (S/lambda)) con C = lambda (estimacion clasica de Kraus, no consultada).
Segunda via: el frente de Pareto se obtiene por dominancia de pares y se compara con un barrido de 20 000 vectores de pesos aleatorios (semilla 91): toda solucion ganadora de algun peso debe estar en el frente.
Tolerancias: ninguna solucion ganadora fuera del frente (0 casos).
"""
from __future__ import annotations
import math, platform, random

C = 299_792_458.0
F = 8.4e9
LAM = C / F


def g_ap(d, eta):
    return 10 * math.log10(eta * (math.pi * d / LAM) ** 2)


# (nombre, ganancia dBi, masa kg, apertura/lado m, costo (unidades relativas), riesgo 1-5)
def candidatos():
    h_n = 12
    g_helice = 10.8 + 10 * math.log10(h_n * 1.0 * (0.25))  # C = lambda -> (C/lam)^2 = 1; S = 0.25 lam
    return [
        ("parche 4x4", 13.0, 0.15, 0.20, 1.0, 1),
        ("helice 12 vueltas", g_helice, 0.40, 0.45, 1.5, 1),
        ("bocina corrugada", g_ap(0.30, 0.60), 1.20, 0.45, 3.0, 1),
        ("reflector 0.6 m", g_ap(0.60, 0.60), 1.80, 0.60, 4.0, 2),
        ("reflector 1.0 m", g_ap(1.00, 0.62), 4.50, 1.00, 7.0, 2),
        ("reflector 1.0 m desplegable", g_ap(1.00, 0.55), 3.20, 0.35, 12.0, 4),
        ("arreglo 16x16 (barrido)", 10 * math.log10(256 * 0.7) + 0.0, 5.50, 0.25, 30.0, 3),
    ]


def pareto(items):
    # objetivos: maximizar ganancia, minimizar masa, apertura, costo, riesgo
    def domina(a, b):
        mejor = a[1] >= b[1] and a[2] <= b[2] and a[3] <= b[3] and a[4] <= b[4] and a[5] <= b[5]
        estricto = a[1] > b[1] or a[2] < b[2] or a[3] < b[3] or a[4] < b[4] or a[5] < b[5]
        return mejor and estricto
    return [x for x in items if not any(domina(y, x) for y in items if y is not x)]


def puntuar(items, pesos):
    g = [x[1] for x in items]
    cols = [g, [x[2] for x in items], [x[3] for x in items], [x[4] for x in items], [x[5] for x in items]]
    res = []
    for i, x in enumerate(items):
        s = 0.0
        for j, (col, w) in enumerate(zip(cols, pesos)):
            lo, hi = min(col), max(col)
            v = (col[i] - lo) / (hi - lo) if hi > lo else 0.0
            s += w * (v if j == 0 else 1.0 - v)
        res.append(s)
    return res


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    cand = candidatos()
    print(f"Requisito SINTETICO: G >= 30 dBi a {F/1e9} GHz (lambda = {LAM*1e3:.2f} mm), lado <= 1.0 m, masa <= 6 kg")
    print(" candidato                    G [dBi]  masa [kg]  lado [m]  costo   riesgo  cumple")
    ok = []
    for c in cand:
        cumple = c[1] >= 30.0 and c[3] <= 1.0 and c[2] <= 6.0
        if cumple:
            ok.append(c)
        print(f" {c[0]:27s} {c[1]:7.2f}  {c[2]:8.2f}  {c[3]:7.2f}  {c[4]:6.1f}  {c[5]:5d}   {'si' if cumple else 'no'}")
    fr = pareto(ok)
    print("Frente de Pareto entre los que cumplen:", ", ".join(c[0] for c in fr))
    pesos0 = (0.35, 0.25, 0.15, 0.15, 0.10)
    pts = puntuar(ok, pesos0)
    orden = sorted(zip(pts, ok), key=lambda t: -t[0])
    print("Suma ponderada (pesos 0.35 ganancia, 0.25 masa, 0.15 lado, 0.15 costo, 0.10 riesgo; normalizacion min-max):")
    for p, c in orden:
        print(f"   {c[0]:27s} {p:.4f}")
    rnd = random.Random(91)
    gana = {}
    fuera = 0
    for _ in range(20000):
        w = [rnd.random() for _ in range(5)]
        s = sum(w)
        w = [x / s for x in w]
        pts = puntuar(ok, w)
        i = max(range(len(ok)), key=lambda k: pts[k])
        gana[ok[i][0]] = gana.get(ok[i][0], 0) + 1
        if ok[i] not in fr:
            fuera += 1
    print("Sensibilidad: ganador en 20 000 vectores de pesos aleatorios (semilla 91)")
    for k, v in sorted(gana.items(), key=lambda t: -t[1]):
        print(f"   {k:27s} {v:6d}  ({100*v/20000:5.1f} %)")
    print(f"Ganadores fuera del frente de Pareto: {fuera}")
    assert fuera == 0
    print("Margen de enlace con cada candidato que cumple (SINTETICO: se necesitan 30 dBi; margen = G - 30):")
    for c in ok:
        print(f"   {c[0]:27s} {c[1]-30:+.2f} dB")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
