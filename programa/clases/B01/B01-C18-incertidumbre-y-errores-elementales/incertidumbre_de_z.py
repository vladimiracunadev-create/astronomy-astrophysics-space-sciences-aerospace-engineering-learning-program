#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B01-C18: incertidumbre tipo A de una medición repetida y propagación a z.

Datos SINTÉTICOS: 10 lecturas simuladas de λ_obs de la línea Hα (valor verdadero fijado en
662,90 nm, ruido gaussiano de 0,08 nm, semilla fija) y λ_rep = 656,3 nm con incertidumbre
estándar tipo B de 0,05 nm (supuesto de la clase). Modelo: media y desviación estándar
experimental (GUM 4.2); u(media) = s/√n; ley de propagación de incertidumbres de la GUM 5.1.2
para entradas no correlacionadas: u_c² = Σ (∂f/∂x_i)² u(x_i)²; z = (λ_obs − λ_rep)/λ_rep.
Supuestos: ruido gaussiano independiente; sin error sistemático en λ_obs. Dominio de validez:
incertidumbres pequeñas frente al valor (linealización). Tolerancias: media y s del caso
analítico {1,2,3,4,5} exactas a 1e-12; propagación frente a Monte Carlo independiente (200 000
tiradas) dentro del 3 %.
"""

from __future__ import annotations

import math
import platform
import random
import statistics
import sys

LAM_VERDADERO = 662.90
SIGMA_RUIDO = 0.08
LAM_REP, U_REP = 656.3, 0.05


def tipo_a(x: list[float]) -> tuple[float, float, float]:
    n = len(x)
    m = sum(x) / n
    s = math.sqrt(sum((v - m) ** 2 for v in x) / (n - 1))
    return m, s, s / math.sqrt(n)


def u_z(lam_obs: float, u_obs: float) -> tuple[float, float]:
    z = (lam_obs - LAM_REP) / LAM_REP
    d_obs = 1 / LAM_REP
    d_rep = -lam_obs / LAM_REP**2
    return z, math.sqrt((d_obs * u_obs) ** 2 + (d_rep * U_REP) ** 2)


def pruebas() -> None:
    m, s, u = tipo_a([1, 2, 3, 4, 5])
    assert abs(m - 3) < 1e-12 and abs(s - math.sqrt(2.5)) < 1e-12 and abs(u - math.sqrt(0.5)) < 1e-12
    rnd = random.Random(1)
    lo, uo = 662.9, 0.03
    muestras = []
    for _ in range(200_000):
        a, b = rnd.gauss(lo, uo), rnd.gauss(LAM_REP, U_REP)
        muestras.append((a - b) / b)
    _, u_gum = u_z(lo, uo)
    assert abs(statistics.pstdev(muestras) - u_gum) / u_gum < 0.03, (statistics.pstdev(muestras), u_gum)


def main() -> int:
    pruebas()
    print(f"python {sys.version.split()[0]} ({platform.system()}) | pruebas OK")
    rnd = random.Random(2026)
    lect = [rnd.gauss(LAM_VERDADERO, SIGMA_RUIDO) for _ in range(10)]
    m, s, u = tipo_a(lect)
    print("Lecturas (nm): " + " ".join(f"{v:.2f}" for v in lect))
    print(f"media = {m:.3f} nm ; s = {s:.3f} nm ; u(media) = s/√n = {u:.3f} nm")
    z, uz = u_z(m, u)
    print(f"z = {z:.5f} ± {uz:.5f} (u estándar) ; relativa = {uz / z * 100:.1f} %")
    c = 299_792.458
    print(f"v ≈ c z = {c * z:.0f} ± {c * uz:.0f} km/s")
    print(f"Expandida (k = 2): z = {z:.5f} ± {2 * uz:.5f}")
    for nombre, v, e1, e2 in (("OPERA v1", 60.7, 6.9, 7.4), ("OPERA v4", 6.5, 7.4, 8.3)):
        sig = math.hypot(e1, e2)
        print(f"{nombre}: {v} ns ; σ combinada = {sig:.1f} ns ; razón = {v / sig:.1f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
