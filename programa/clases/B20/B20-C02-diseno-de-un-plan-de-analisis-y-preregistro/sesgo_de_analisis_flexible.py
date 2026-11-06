#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B20-C02: costo de elegir el análisis después de ver los datos.

Datos: SIMULADOS (números pseudoaleatorios gaussianos con semilla fija; la
hipótesis nula es verdadera por construcción: no hay efecto). Modelo: en cada
ensayo se prueba si la media de n=30 valores N(0,1) difiere de 0 con una
prueba z bilateral (sigma conocida = 1), con nivel alfa = 0,05. Se comparan
(a) un análisis único fijado de antemano, (b) el "mejor" de k análisis
independientes elegido después de ver los p, y (c) la corrección de Bonferroni.
Supuestos: los k análisis usan datos independientes (caso extremo y calculable;
en la práctica las variantes comparten datos y se correlacionan). Validez:
ilustra el mecanismo, no estima el sesgo de un estudio real. Tolerancia:
frecuencias simuladas frente a la fórmula exacta 1-(1-alfa)^k con 4 desviaciones
típicas binomiales de margen.
"""

from __future__ import annotations

import math
import random
import sys

ALFA = 0.05
N = 30
ENSAYOS = 20_000
SEMILLA = 20261105


def p_bilateral(z: float) -> float:
    """p bilateral de una normal estándar: erfc(|z|/sqrt(2))."""
    return math.erfc(abs(z) / math.sqrt(2.0))


def un_p(rng: random.Random) -> float:
    media = sum(rng.gauss(0.0, 1.0) for _ in range(N)) / N
    return p_bilateral(media * math.sqrt(N))


def frecuencia(k: int, umbral: float, rng: random.Random) -> float:
    """Fracción de ensayos donde el mínimo de k p-valores queda bajo el umbral."""
    aciertos = 0
    for _ in range(ENSAYOS):
        if min(un_p(rng) for _ in range(k)) < umbral:
            aciertos += 1
    return aciertos / ENSAYOS


def teorica(k: int, umbral: float) -> float:
    return 1.0 - (1.0 - umbral) ** k


def phi(x: float) -> float:
    """Función de distribución acumulada de la normal estándar."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def potencia(d: float, n: int) -> float:
    """Potencia aproximada de la prueba z bilateral para un efecto d (en unidades de sigma)."""
    return phi(d * math.sqrt(n) - 1.959964)


def n_minimo(d: float, objetivo: float = 0.80) -> int:
    n = 1
    while potencia(d, n) < objetivo:
        n += 1
    return n


def pruebas() -> None:
    assert abs(phi(0.0) - 0.5) < 1e-15 and abs(phi(1.959964) - 0.975) < 1e-6
    assert n_minimo(0.5) == 32 and n_minimo(0.4) == 50     # (1,96+0,8416)^2/d^2 redondeado hacia arriba
    # referencia analítica independiente de la simulación
    assert abs(p_bilateral(1.959964) - 0.05) < 1e-6          # z crítico clásico
    assert abs(teorica(1, ALFA) - 0.05) < 1e-12
    assert abs(teorica(10, ALFA) - 0.4012630607616213) < 1e-12
    # la simulación debe respetar la fórmula exacta
    rng = random.Random(SEMILLA)
    for k, umbral in ((1, ALFA), (5, ALFA), (5, ALFA / 5)):
        f = frecuencia(k, umbral, rng)
        t = teorica(k, umbral)
        sd = math.sqrt(t * (1 - t) / ENSAYOS)
        assert abs(f - t) < 4 * sd, (k, umbral, f, t)


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    pruebas()
    print(f"python {sys.version.split()[0]} | pruebas OK | datos SIMULADOS (sin efecto real)")
    print(f"n={N}, alfa={ALFA}, ensayos={ENSAYOS}, semilla={SEMILLA}")
    rng = random.Random(SEMILLA)
    print(f"{'k':>3} {'umbral':>8} {'simulado':>9} {'exacto':>8}")
    for k, umbral, nombre in ((1, ALFA, "análisis único preregistrado"),
                              (5, ALFA, "mejor de 5, sin corregir"),
                              (10, ALFA, "mejor de 10, sin corregir"),
                              (5, ALFA / 5, "mejor de 5, Bonferroni")):
        f = frecuencia(k, umbral, rng)
        print(f"{k:>3} {umbral:>8.3f} {f:>9.3f} {teorica(k, umbral):>8.3f}  {nombre}")
    print(f"Tamaño mínimo para potencia 0,80: d=0,5 -> n={n_minimo(0.5)}; d=0,4 -> n={n_minimo(0.4)}")
    print(f"Potencia con d=0,5 y n=32: {potencia(0.5, 32):.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
