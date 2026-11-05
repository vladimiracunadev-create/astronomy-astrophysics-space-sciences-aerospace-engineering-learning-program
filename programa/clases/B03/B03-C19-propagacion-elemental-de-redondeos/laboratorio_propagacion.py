#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C19: propagación elemental de redondeos y comparación con una simulación.

Datos: semieje de la Tierra y período sidéreo (NASA Earth Fact Sheet: 149,598e6 km y 365,256 d)
REDONDEADOS a tres cifras (1,50e8 km y 365 d) para simular datos de baja calidad; velocidad orbital
media publicada 29,78 km/s (misma ficha) como referencia. Cada dato vale su cifra redondeada ±media
unidad de la última cifra, con distribución uniforme (supuesto). Modelo: v = 2 pi a / T.
Método A: cotas (peor caso). Método B: cuadratura de incertidumbres relativas (JCGM 100:2008,
ec. 12), con u = semiancho / sqrt(3) para una distribución uniforme. Método C: SIMULACIÓN de
Monte Carlo (semilla fija, resultados sintéticos). Tolerancia: la desviación simulada coincide con la
del método B dentro del 2 %; el peor caso contiene toda la simulación.
"""
from __future__ import annotations

import math
import platform
import random

A_KM, A_SEMI = 1.50e8, 0.005e8           # valor y semiancho (media unidad de la última cifra)
T_D, T_SEMI = 365.0, 0.5
V_NASA = 29.78                           # km/s, referencia publicada
DIA_S = 86_400.0


def velocidad(a: float, t_dias: float) -> float:
    return 2 * math.pi * a / (t_dias * DIA_S)


def pruebas() -> None:
    v0 = velocidad(A_KM, T_D)
    # peor caso: a máxima y T mínimo
    v_max = velocidad(A_KM + A_SEMI, T_D - T_SEMI)
    v_min = velocidad(A_KM - A_SEMI, T_D + T_SEMI)
    assert v_min < v0 < v_max
    assert v_min <= V_NASA <= v_max                                    # la referencia publicada cae dentro del peor caso
    # cuadratura relativa
    ur = math.hypot(A_SEMI / A_KM, T_SEMI / T_D) / math.sqrt(3)
    rnd = random.Random(2026)
    muestras = [velocidad(A_KM + rnd.uniform(-A_SEMI, A_SEMI), T_D + rnd.uniform(-T_SEMI, T_SEMI)) for _ in range(200_000)]
    media = sum(muestras) / len(muestras)
    sd = math.sqrt(sum((x - media) ** 2 for x in muestras) / (len(muestras) - 1))
    assert abs(sd / v0 - ur) / ur < 0.02, (sd / v0, ur)               # Monte Carlo ≈ cuadratura
    assert min(muestras) >= v_min and max(muestras) <= v_max           # el peor caso contiene todo
    assert abs((1.0 + 0.1) * (1.0 - 0.1) - 0.99) < 1e-12              # (1+r)(1-r) = 1 - r^2 (cuadratura de segundo orden)


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    v0 = velocidad(A_KM, T_D)
    v_max = velocidad(A_KM + A_SEMI, T_D - T_SEMI)
    v_min = velocidad(A_KM - A_SEMI, T_D + T_SEMI)
    ur = math.hypot(A_SEMI / A_KM, T_SEMI / T_D) / math.sqrt(3)
    print(f"v = {v0:.4f} km/s; peor caso: [{v_min:.4f}, {v_max:.4f}] (semiancho {(v_max - v_min) / 2:.4f} km/s); referencia NASA {V_NASA} km/s")
    print(f"Cuadratura: u_r = {ur:.3e} -> u = {ur * v0:.4f} km/s")
    rnd = random.Random(2026)
    muestras = [velocidad(A_KM + rnd.uniform(-A_SEMI, A_SEMI), T_D + rnd.uniform(-T_SEMI, T_SEMI)) for _ in range(200_000)]
    media = sum(muestras) / len(muestras)
    sd = math.sqrt(sum((x - media) ** 2 for x in muestras) / (len(muestras) - 1))
    print(f"Simulación (sintética, 200 000 muestras): media {media:.4f} km/s, desviación {sd:.4f} km/s (relativa {sd / v0:.3e})")
    u1 = 0.05 / math.sqrt(3)
    print(f"Suma de 3 redondeos de ±0,05: cota (peor caso) {3 * 0.05:.3f}; incertidumbre estándar {math.sqrt(3) * u1:.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
