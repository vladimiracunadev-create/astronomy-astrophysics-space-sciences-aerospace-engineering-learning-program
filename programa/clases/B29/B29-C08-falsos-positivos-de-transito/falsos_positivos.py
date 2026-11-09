#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C08: dilucion de una binaria eclipsante, prueba par-impar y potencia de deteccion.

Datos: ninguna constante fisica. Contexto: Fressin y colaboradores simulan los falsos positivos astrofisicos de Kepler (binarias eclipsantes de fondo o ligadas
que imitan un transito) y la fraccion que superaria el cribado de candidatos (arXiv:1301.0842, resumen, consultado 2026-11-09). La profundidad de la binaria
(20 %), los flujos de la binaria y del objetivo, el numero de eclipses, el ruido por tránsito (1000 ppm) y las diferencias par-impar son ILUSTRATIVOS.
Modelo: profundidad observada de una binaria diluida delta_obs = delta_EB F_EB/(F_EB + F_obj); si el periodo verdadero es el doble, los eclipses impares y
pares tienen profundidades distintas D1, D2; estadistico Z = (D_par - D_impar)/(sigma sqrt(2/n)) con n eclipses de cada tipo y ruido sigma por eclipse.
Monte Carlo (semilla fija): tasa de falsas alarmas a 3 sigma (dos colas, esperada 0.27 %) con D1 = D2 y potencia con diferencias de 0.5, 1 y 2 sigma.
Supuestos: ruido gaussiano independiente por eclipse. Validez: ilustrativa.
Tolerancia: tasa de falsas alarmas dentro de 4 desviaciones binomiales de 0.0027; potencia analitica frente a Monte Carlo dentro de 0.01.
"""
from __future__ import annotations
import math
import platform
import random
import sys


def Phi(z):
    return 0.5 * math.erfc(-z / math.sqrt(2))


def diluida(delta_eb, f_eb, f_obj):
    return delta_eb * f_eb / (f_eb + f_obj)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'F_EB/F_obj':>11} {'delta observada':>16}")
    for r in (0.001, 0.01, 0.05, 0.2, 1.0):
        print(f"{r:11.3f} {diluida(0.20, r, 1.0):16.5e}")
    # una binaria de fondo 100 veces mas debil que el objetivo con eclipses de 20 % imita un planeta del tamano de Neptuno
    d = diluida(0.20, 0.01, 1.0)
    print(f"binaria 100 veces mas debil con eclipse de 20 %: profundidad observada = {d * 1e6:.0f} ppm = la de un planeta con k = {math.sqrt(d):.4f}")
    # prueba par-impar
    rng = random.Random(20261109)
    sigma, n_ecl = 1000e-6, 8
    sd = sigma * math.sqrt(2 / n_ecl)
    print(f"error de la diferencia par-impar con {n_ecl} eclipses de cada tipo y sigma = {sigma * 1e6:.0f} ppm: {sd * 1e6:.1f} ppm")
    N = 40000
    umbral = 3.0
    falsas = 0
    for _ in range(N):
        a = rng.gauss(0, sigma / math.sqrt(n_ecl))
        b = rng.gauss(0, sigma / math.sqrt(n_ecl))
        if abs((a - b) / sd) > umbral:
            falsas += 1
    p_esp = 2 * (1 - Phi(umbral))
    sdf = math.sqrt(p_esp * (1 - p_esp) / N)
    print(f"tasa de falsas alarmas a {umbral} sigma: {falsas / N:.5f} (esperada {p_esp:.5f} +/- {sdf:.5f})")
    assert abs(falsas / N - p_esp) < 4 * sdf
    print(f"{'delta D / sd':>13} {'potencia analitica':>19} {'potencia MC':>12}")
    for k in (0.5, 1.0, 2.0, 3.0, 5.0):
        dd = k * sd
        det = 0
        for _ in range(N):
            a = dd + rng.gauss(0, sigma / math.sqrt(n_ecl))
            b = rng.gauss(0, sigma / math.sqrt(n_ecl))
            if abs((a - b) / sd) > umbral:
                det += 1
        pa = (1 - Phi(umbral - k)) + Phi(-umbral - k)
        pm = det / N
        assert abs(pa - pm) < 0.01, f"potencia k={k}"
        print(f"{k:13.1f} {pa:19.4f} {pm:12.4f}")
    # numero de eclipses necesarios para detectar una diferencia del 10 % de una profundidad de 5000 ppm a 3 sigma con potencia 0.5
    dd = 0.10 * 5000e-6
    n_nec = 2 * (umbral * sigma / dd) ** 2
    print(f"para detectar una diferencia de {dd * 1e6:.0f} ppm (10 % de 5000 ppm) con potencia 0.5 hacen falta ~{n_nec:.0f} eclipses de cada tipo")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
