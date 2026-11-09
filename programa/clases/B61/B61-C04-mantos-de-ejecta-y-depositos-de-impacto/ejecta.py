#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B61-C04: espesor del manto de ejecta, volumen y exponente derivado de la balistica.

Datos: SINTETICOS/ILUSTRATIVOS. La ley t(r) = t_rim (r/R)^-3 y t_rim ~ 0.04 R (craters pequenos) se tomaron de un
  articulo de arXiv que atribuye la forma a McGetchin et al. (1973) (consultado 2026-11-09 por resumen de busqueda;
  el original no se leyo). mu = 0.55 es ilustrativo (ver B61-C01). d/D = 0.2 ilustrativo.
Modelo (unidades relativas a R; cuerpo plano sin atmosfera):
  (1) volumen del manto fuera del borde: V = int_R^inf 2 pi r t(r) dr = 2 pi t_rim R^2 (analitico) frente a integracion
      numerica en variable log r hasta 1e5 R (diferencia por la cola truncada ~ 1e-5);
  (2) exponente derivado: si M(>v) ~ v^(-3 mu) y el alcance L ~ v^2, entonces M(>L) ~ L^(-3mu/2) y
      t(L) ~ L^(-3mu/2 - 2). Se verifica con Monte Carlo (semilla 20261109) y se compara con -3.
Tolerancias: volumen 1e-4 relativo; pendiente de Monte Carlo 0.05 absoluto.
Limites: la ley de -3 es empirica en 2-3 R; la derivacion balistica ignora curvatura, zonas de eyeccion y flujo de bloques.
"""
from __future__ import annotations
import math, platform, random

MU = 0.55


def volumen_manto(trim_sobre_R, nlog=200000, rmax=1e5):
    # unidades R = 1
    a, b = 0.0, math.log(rmax)
    h = (b - a) / nlog
    v = 0.0
    for i in range(nlog):
        lr = a + (i + 0.5) * h
        r = math.exp(lr)
        v += 2 * math.pi * r * (trim_sobre_R * r ** -3) * r * h
    return v


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    trim = 0.04
    va = 2 * math.pi * trim
    vn = volumen_manto(trim)
    print(f"V_manto/R^3 : analitico {va:.6f} ; numerico {vn:.6f} ; dif. relativa {abs(vn/va-1):.2e}")
    assert abs(vn / va - 1) < 1e-4
    d = 0.2 * 2  # d/R con d/D = 0.2 -> d = 0.4 R
    R = 1.0
    Vbol = math.pi * d * R * (3 * R * R + d * d) / 6
    print(f"Volumen del bol (casquete, d/D=0.2) = {Vbol:.6f} R^3 ; razon V_manto/V_bol = {va/Vbol:.3f}")
    for k in (2.0, 3.0):
        frac = 1 - (k) ** -1.0  # fraccion del volumen que queda dentro de k R: 1 - 1/k
        print(f"Fraccion del volumen del manto dentro de {k:.0f} R = {frac:.3f}")
    # espesor a 2R y 3R
    for k in (1.0, 2.0, 3.0, 5.0):
        print(f"t({k:.0f} R) = {trim * k ** -3:.6f} R")
    # exponente derivado
    rng = random.Random(20261109)
    N = 400000
    L = []
    for _ in range(N):
        x = rng.uniform(1.0, 1000.0) ** (1 / 3)  # x/a con masa ~ x^3
        v = x ** (-1.0 / MU)
        L.append(v * v)
    L.sort()
    # densidad superficial: conteo en anillos logaritmicos / area del anillo
    edges = [L[int(f * N)] for f in (0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80)]
    pts = []
    for a_, b_ in zip(edges[:-1], edges[1:]):
        cuenta = sum(1 for l in L if a_ <= l < b_)
        area = math.pi * (b_ * b_ - a_ * a_) if False else math.pi * (b_ - a_) * (b_ + a_)
        # L es distancia (alcance), area del anillo = pi (b^2 - a^2)
        pts.append((math.log(math.sqrt(a_ * b_)), math.log(cuenta / (math.pi * (b_ ** 2 - a_ ** 2)))))
    mx = sum(p[0] for p in pts) / len(pts)
    my = sum(p[1] for p in pts) / len(pts)
    sl = sum((p[0] - mx) * (p[1] - my) for p in pts) / sum((p[0] - mx) ** 2 for p in pts)
    teo = -(3 * MU / 2 + 2)
    print(f"Pendiente de t(L) en Monte Carlo = {sl:.3f} ; derivada = -(3mu/2+2) = {teo:.3f} ; ley empirica = -3")
    assert abs(sl - teo) < 0.05
    print(f"Con mu = 2/3 (escalado de energia) la derivada da {-(3*(2/3)/2+2):.3f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
