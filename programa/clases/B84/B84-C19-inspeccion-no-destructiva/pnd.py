#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C19: capacidad de deteccion de defectos: regla 29/29, curva POD logistica ajustada a datos de acierto/fallo y ultrasonidos.

El estandar NASA-STD-5009 Rev. C (ficha consultada el 2026-11-10) exige una demostracion cuantitativa de la probabilidad de deteccion (POD) cuando se requiere
control de fractura. NO se consultaron sus requisitos numericos: la regla 90/95 y la regla 29/29 se usan aqui como conceptos estadisticos clasicos
(se verifican por calculo) y no como cita del estandar.
DATOS SINTETICOS (generados aqui con semilla 84019, NO medidos): 80 defectos con tamanos lognormales (mediana 1,0 mm, sigma_ln = 0,6) y deteccion de Bernoulli con
POD verdadera logistica en ln(a): logit POD = (ln a - mu)/s con mu = ln(0,8 mm) y s = 0,25.
Ajuste: regresion logistica de logit POD = b0 + b1 ln a por Newton-Raphson; a90 = exp((ln 9 - b0)/b1); cota superior 95 % por el metodo delta con la matriz de
informacion de Fisher (aproximacion de Wald, no la razon de verosimilitud).
Ultrasonidos (ILUSTRATIVO): d = v t/2 con v = 6320 m/s (onda longitudinal en aluminio, valor tipico no consultado); lambda = v/f; resolucion axial ~ lambda/2 (regla gruesa).
Tolerancia: 0,9^29 < 0,05 y 0,9^28 > 0,05 (aritmetica exacta); a90 ajustado dentro de un factor 1,5 del verdadero.
"""
from __future__ import annotations
import math, platform, random

MU, S = math.log(0.8), 0.25


def pod(a):
    return 1.0 / (1.0 + math.exp(-(math.log(a) - MU) / S))


def ajustar(xs, ys):
    b0, b1 = 0.0, 1.0
    for _ in range(100):
        g0 = g1 = 0.0
        h00 = h01 = h11 = 0.0
        for x, y in zip(xs, ys):
            p = 1 / (1 + math.exp(-(b0 + b1 * x)))
            w = p * (1 - p)
            g0 += y - p
            g1 += (y - p) * x
            h00 += w
            h01 += w * x
            h11 += w * x * x
        det = h00 * h11 - h01 * h01
        d0 = (h11 * g0 - h01 * g1) / det
        d1 = (-h01 * g0 + h00 * g1) / det
        b0 += d0
        b1 += d1
        if abs(d0) + abs(d1) < 1e-12:
            break
    return b0, b1, (h11 / det, -h01 / det, h00 / det)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n_min = math.ceil(math.log(0.05) / math.log(0.9))
    print(f"Regla clasica: con POD = 0,90 la probabilidad de 29 aciertos seguidos es 0,9^29 = {0.9 ** 29:.5f} (< 0,05); con 28, 0,9^28 = {0.9 ** 28:.5f} (> 0,05); n minimo = {n_min}")
    print("Probabilidad de aprobar la demostracion 29/29 segun la POD real:")
    for p in (0.90, 0.95, 0.98, 0.99):
        print(f"  POD real = {p:.2f} -> P(29 de 29) = {p ** 29:.4f}")
    rng = random.Random(84019)
    n = 80
    a = [math.exp(math.log(1.0) + 0.6 * rng.gauss(0, 1)) for _ in range(n)]
    y = [1.0 if rng.random() < pod(ai) else 0.0 for ai in a]
    print(f"80 defectos SINTETICOS: {int(sum(y))} detectados ({sum(y) / n * 100:.1f} %); POD verdadera: a50 = 0,800 mm, a90 = {math.exp(MU + S * math.log(9)):.4f} mm")
    xs = [math.log(ai) for ai in a]
    b0, b1, cov = ajustar(xs, y)
    x90 = (math.log(9) - b0) / b1
    a50 = math.exp(-b0 / b1)
    # gradiente de x90 respecto de (b0, b1)
    g = (-1 / b1, -(math.log(9) - b0) / b1 ** 2)
    var = g[0] ** 2 * cov[0] + 2 * g[0] * g[1] * cov[1] + g[1] ** 2 * cov[2]
    se = math.sqrt(var)
    print(f"Ajuste logistico: b0 = {b0:.3f}, b1 = {b1:.3f} ; a50 = {a50:.4f} mm ; a90 = {math.exp(x90):.4f} mm ; error tipico de ln a90 = {se:.3f}")
    print(f"a90/95 (cota superior de Wald, una cola) = {math.exp(x90 + 1.645 * se):.4f} mm")
    print("POD ajustada frente a verdadera:")
    for ai in (0.3, 0.5, 0.8, 1.0, 1.5, 2.0):
        pf = 1 / (1 + math.exp(-(b0 + b1 * math.log(ai))))
        print(f"  a = {ai:.1f} mm  POD ajustada = {pf:.3f}  verdadera = {pod(ai):.3f}")
    print("Ultrasonidos (v = 6320 m/s, valor tipico NO consultado):")
    for t in (2e-6, 5e-6, 10e-6):
        print(f"  tiempo de ida y vuelta {t * 1e6:4.1f} us -> profundidad {6320 * t / 2 * 1e3:6.2f} mm")
    for f in (2.25e6, 5e6, 10e6):
        lam = 6320 / f * 1e3
        print(f"  f = {f / 1e6:5.2f} MHz -> lambda = {lam:5.3f} mm, resolucion axial gruesa ~ {lam / 2:5.3f} mm")
    assert 0.9 ** 29 < 0.05 < 0.9 ** 28 and n_min == 29
    assert math.exp(x90) / math.exp(MU + S * math.log(9)) < 1.5 and math.exp(x90) / math.exp(MU + S * math.log(9)) > 1 / 1.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
