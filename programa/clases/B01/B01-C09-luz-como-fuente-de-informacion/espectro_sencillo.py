#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C09: leer un espectro sencillo (SINTÉTICO) y estimar una temperatura.

Datos: (1) un espectro de líneas SINTÉTICO generado aquí con corrimiento z conocido
(el «elemento X» no existe: sus longitudes de reposo son inventadas); (2) la temperatura
efectiva del Sol, 5772 K (NASA Sun Fact Sheet; IAU 2015 B3, valor nominal);
(3) constantes SI exactas h, c, k (BIPM, SI 9.ª ed.).
Modelo: z = (λ_obs − λ_rep)/λ_rep; cuerpo negro de Planck y ley de Wien derivada de h, c, k.
Supuestos: líneas bien identificadas; ruido gaussiano sintético de 0,05 nm; la estrella se
trata como cuerpo negro (aproximación). Dominio de validez: z << 1; formas continuas
aproximadas. Tolerancias: z recuperado a 5e-4; λ_max de Wien frente al máximo numérico de
Planck, 0,2 %.
"""

from __future__ import annotations

import math
import platform
import random
import sys

H = 6.626_070_15e-34   # J s (exacto, SI)
C = 299_792_458        # m/s (exacto, SI)
K = 1.380_649e-23      # J/K (exacto, SI)
T_SOL = 5772.0         # K (NASA / IAU nominal)


def planck(lam_m: float, t: float) -> float:
    return (2 * H * C**2 / lam_m**5) / math.expm1(H * C / (lam_m * K * t))


def wien_b() -> float:
    """b = h c / (k x), con x raíz de x = 5 (1 − e^−x) (bisección)."""
    lo, hi = 4.0, 6.0
    f = lambda x: x - 5 * (1 - math.exp(-x))
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if f(mid) < 0 else (lo, mid)
    x = (lo + hi) / 2
    return H * C / (K * x)


def maximo_numerico(t: float) -> float:
    mejor, lam_mejor = 0.0, 0.0
    for i in range(100, 3000):          # 100 nm a 3 000 nm
        lam = i * 1e-9
        v = planck(lam, t)
        if v > mejor:
            mejor, lam_mejor = v, lam
    return lam_mejor


def espectro_sintetico(z: float, semilla: int = 7):
    rnd = random.Random(semilla)
    reposo = {"X-1": 500.0, "X-2": 600.0, "X-3": 700.0}      # nm, inventadas
    return {n: (l, l * (1 + z) + rnd.gauss(0, 0.05)) for n, l in reposo.items()}


def pruebas() -> None:
    b = wien_b()
    lam_w = b / T_SOL
    assert abs(lam_w - maximo_numerico(T_SOL)) / lam_w < 2e-3, (lam_w, maximo_numerico(T_SOL))
    z_in = 0.02
    zs = [(o - r) / r for r, o in espectro_sintetico(z_in).values()]
    assert abs(sum(zs) / len(zs) - z_in) < 5e-4, zs


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    z_in = 0.02
    zs = []
    for nombre, (rep, obs) in espectro_sintetico(z_in).items():
        z = (obs - rep) / rep
        zs.append(z)
        print(f"{nombre}: reposo {rep:.1f} nm, observada {obs:.2f} nm, z = {z:.5f}")
    media = sum(zs) / len(zs)
    desv = (sum((z - media) ** 2 for z in zs) / (len(zs) - 1)) ** 0.5
    print(f"z medio = {media:.5f} (entrada {z_in}); dispersión entre líneas = {desv:.5f}")
    print(f"v aparente ≈ c·z = {299792.458 * media:.0f} km/s")
    b = wien_b()
    print(f"Constante de Wien derivada: b = {b:.6e} m K")
    print(f"λ_max del Sol (5772 K) = {b / T_SOL * 1e9:.1f} nm")
    print(f"Hα de C01: z = {(662.9 - 656.3) / 656.3:.5f}; v ≈ {299792.458 * (662.9 - 656.3) / 656.3:.0f} km/s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
