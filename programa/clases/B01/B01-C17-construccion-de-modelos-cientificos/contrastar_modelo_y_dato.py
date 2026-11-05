#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C17: contrastar dos modelos del período orbital con datos publicados.

Datos PUBLICADOS: NASA NSSDC Planetary Fact Sheet (act. 18-mar-2025): distancia al Sol [10^6 km]
y período orbital [d] de los 8 planetas. 1 au = 149 597 870 700 m (exacta); año = 365,25 d.
Modelos: A) T = k·a^p con p AJUSTADO por mínimos cuadrados en escala logarítmica;
B) T = c·a (exponente forzado a 1, «período proporcional a la distancia»).
Supuestos: errores relativos similares en todos los planetas; los datos de 3–4 cifras.
Dominio de validez: planetas del Sistema Solar (órbitas alrededor del Sol). Tolerancias:
ajuste de exponente exacto (1,5 ± 1e-9) sobre datos sintéticos T = a^1,5 y exponente ajustado
dentro de 0,01 de 1,5 con los datos reales; el modelo B debe tener un residuo mayor (criterio de
comparación declarado antes de ejecutar).
"""

from __future__ import annotations

import math
import platform
import sys

AU_KM = 149_597_870.7
ANIO = 365.25
DATOS = [  # (nombre, a [1e6 km], T [d])
    ("Mercurio", 57.9, 88.0), ("Venus", 108.2, 224.7), ("Tierra", 149.6, 365.2),
    ("Marte", 228.0, 687.0), ("Júpiter", 778.5, 4331), ("Saturno", 1432.0, 10747),
    ("Urano", 2867.0, 30589), ("Neptuno", 4515.0, 59800),
]


def ajuste_potencia(x: list[float], y: list[float]) -> tuple[float, float]:
    """Mínimos cuadrados de ln y = ln k + p ln x. Devuelve (p, k)."""
    lx, ly = [math.log(v) for v in x], [math.log(v) for v in y]
    n = len(x)
    mx, my = sum(lx) / n, sum(ly) / n
    p = sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / sum((a - mx) ** 2 for a in lx)
    return p, math.exp(my - p * mx)


def rms_log(x, y, f) -> float:
    return (sum((math.log(b) - math.log(f(a))) ** 2 for a, b in zip(x, y)) / len(x)) ** 0.5


def pruebas() -> None:
    xs = [0.4, 1.0, 5.2, 30.0]
    p, k = ajuste_potencia(xs, [a**1.5 for a in xs])
    assert abs(p - 1.5) < 1e-9 and abs(k - 1.0) < 1e-9                       # caso analítico exacto
    a = [d[1] * 1e6 / AU_KM for d in DATOS]
    t = [d[2] / ANIO for d in DATOS]
    pa, _ = ajuste_potencia(a, t)
    assert abs(pa - 1.5) < 0.01, pa                                           # exponente con datos reales
    c = math.exp(sum(math.log(b / x) for x, b in zip(a, t)) / len(a))
    assert rms_log(a, t, lambda x: x**1.5) < rms_log(a, t, lambda x: c * x)   # A mejor que B


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    a = [d[1] * 1e6 / AU_KM for d in DATOS]
    t = [d[2] / ANIO for d in DATOS]
    p, k = ajuste_potencia(a, t)
    c = math.exp(sum(math.log(b / x) for x, b in zip(a, t)) / len(a))
    print(f"Modelo A (ajustado): T = {k:.4f}·a^{p:.4f}  [T en años, a en au]")
    print(f"Modelo K (p = 1,5 fijo): residuo RMS(ln) = {rms_log(a, t, lambda x: x**1.5):.4f}")
    print(f"Modelo A: residuo RMS(ln) = {rms_log(a, t, lambda x: k * x**p):.4f}")
    print(f"Modelo B (T = c·a, c = {c:.3f}): residuo RMS(ln) = {rms_log(a, t, lambda x: c * x):.4f}")
    for (nombre, *_), x, y in zip(DATOS, a, t):
        print(f"  {nombre:9s} a = {x:7.3f} au  T = {y:8.3f} a  T_K = {x**1.5:8.3f}  err = {(x**1.5 / y - 1) * 100:+.2f} %")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
