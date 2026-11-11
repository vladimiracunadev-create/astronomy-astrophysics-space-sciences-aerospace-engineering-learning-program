#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C20: potencia y tamano de muestra de un protocolo SIMULADO pre/post con N pequeno (datos SINTETICOS).

Diseno: medicion antes y despues de una exposicion simulada en los mismos individuos (t de Student pareada, bilateral, alfa = 0.05). Diferencias ~ N(d, 1) con d
el tamano del efecto estandarizado (d de Cohen para diferencias pareadas). Valores criticos t(0.975) conocidos: gl 3 = 3.182, 5 = 2.571, 7 = 2.365, 11 = 2.201, 19 = 2.093,
29 = 2.045 (recordados por el autor; NO consultados aqui; se verifican por simulacion bajo el nulo). Potencia = fraccion de 20000 simulaciones con |t| > t_crit. Tamano necesario
aproximado n ~ ((1.96 + 0.84)/d)^2 + 2 para 80 % (aprox. normal). Semilla 105. No es un protocolo real ni una guia clinica. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

TCRIT = {3: 3.182, 5: 2.571, 7: 2.365, 11: 2.201, 19: 2.093, 29: 2.045}


def potencia(n, d, rng, sims=20000):
    x = rng.normal(d, 1.0, (sims, n))
    t = x.mean(axis=1) / (x.std(axis=1, ddof=1) / np.sqrt(n))
    return float(np.mean(np.abs(t) > TCRIT[n - 1]))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): diferencias normales; t criticos recordados y verificados bajo el nulo; protocolo simulado")
    rng = np.random.default_rng(105)
    print("Tasa de error tipo I bajo el nulo (d = 0):")
    for n in (4, 6, 8, 12, 20, 30):
        print(f"  n = {n:2d}: {potencia(n, 0.0, rng):.4f} (objetivo 0.05)")
    print("Potencia segun n y tamano del efecto d:")
    print("   n   d=0.5   d=0.8   d=1.0   d=1.5   d=2.0")
    tabla = {}
    for n in (4, 6, 8, 12, 20, 30):
        fila = [potencia(n, d, rng) for d in (0.5, 0.8, 1.0, 1.5, 2.0)]
        tabla[n] = fila
        print(f"  {n:2d}   " + "   ".join(f"{p:.3f}" for p in fila))
    print("n aproximado para 80 % de potencia (aprox. normal + 2):")
    for d in (0.5, 0.8, 1.0, 1.5, 2.0):
        print(f"  d = {d:3.1f}: n ~ {((1.96 + 0.84) / d) ** 2 + 2:5.1f}")
    # efecto minimo detectable con 80 % de potencia con n = 6 (busqueda)
    for n in (6, 12):
        d_min = None
        for d in np.arange(0.2, 4.0, 0.05):
            if potencia(n, d, rng, 4000) >= 0.8:
                d_min = d; break
        print(f"Efecto minimo con 80 % de potencia y n = {n}: d ~ {d_min:.2f}")
    # inflacion de la significacion: 10 comparaciones independientes
    print(f"Probabilidad de al menos un falso positivo en 10 comparaciones con alfa 0.05 = {1 - 0.95 ** 10:.3f}; con Bonferroni (alfa/10): {1 - 0.995 ** 10:.3f}")
    assert abs(potencia(8, 0.0, rng) - 0.05) < 0.01
    assert tabla[6][2] < tabla[12][2] < tabla[30][2]
    assert tabla[6][4] > tabla[6][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
