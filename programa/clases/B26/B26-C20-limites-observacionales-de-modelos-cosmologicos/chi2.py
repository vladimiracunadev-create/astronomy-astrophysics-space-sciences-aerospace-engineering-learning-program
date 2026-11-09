#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C20: ajuste de Omega_m con supernovas SINTETICAS por chi^2 y cobertura del intervalo.

Datos: ninguno observado. 100 supernovas sinteticas con z entre 0.02 y 1.0 (fijas) y modulos de distancia
mu = mu_teorico(Om_verd = 0.315) + ruido gaussiano de 0.15 mag, mas una constante global desconocida
(calibracion); se marginaliza analiticamente. Resultado publicado con el que se contrasta: Pantheon+,
Omega_m = 0.334 +/- 0.018 (SNe solas, LCDM plano; Brout et al., arXiv:2202.04077, resumen, consultado 2026-11-09).
Modelo: LCDM plano, D_L(z; Om) de B26-C19; chi^2(Om) = sum (mu_i - mu_t(z_i; Om) - M)^2 / s^2 minimizado
sobre M. Intervalo de 68 %: Delta chi^2 = 1. Cobertura con 200 realizaciones del ruido (semilla fija).
Supuestos: errores gaussianos independientes y conocidos, forma de la funcion H(z) conocida. Validez: ilustrativa.
Tolerancia: Om recuperado dentro de 3 sigma; cobertura entre 55 % y 80 % (esperado ~68 %).
"""
from __future__ import annotations
import math
import platform
import random
import sys

C_KMS, H0 = 299792.458, 67.4
OM_VERD, SIG, N = 0.315, 0.15, 100


def mu_t(z, om, n=300):
    h = z / n
    E = lambda zz: math.sqrt(om * (1 + zz) ** 3 + (1 - om))
    s = 1 / E(0) + 1 / E(z)
    for i in range(1, n):
        s += (4 if i % 2 else 2) / E(i * h)
    dl = (1 + z) * C_KMS / H0 * s * h / 3
    return 5 * math.log10(dl * 1e5)


def chi2(mu_obs, mu_th):
    d = [o - t for o, t in zip(mu_obs, mu_th)]
    m = sum(d) / len(d)
    return sum((x - m) ** 2 for x in d) / SIG ** 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    zs = [0.02 + 0.98 * i / (N - 1) for i in range(N)]
    grid = [0.05 + 0.005 * i for i in range(151)]               # Om de 0.05 a 0.80
    teoria = [[mu_t(z, om) for z in zs] for om in grid]
    verd = [mu_t(z, OM_VERD) for z in zs]
    rng = random.Random(20)
    # una realizacion detallada
    obs = [v + rng.gauss(0, SIG) for v in verd]
    c2 = [chi2(obs, row) for row in teoria]
    i0 = min(range(len(grid)), key=lambda i: c2[i])
    c0 = c2[i0]
    inside = [grid[i] for i in range(len(grid)) if c2[i] <= c0 + 1]
    lo, hi = min(inside), max(inside)
    sig = 0.5 * (hi - lo)
    print(f"mejor ajuste: Om = {grid[i0]:.3f} ; chi2_min = {c0:.1f} para {N - 2} grados de libertad")
    print(f"intervalo de 68 % (Delta chi2 = 1): [{lo:.3f}, {hi:.3f}] -> Om = {grid[i0]:.3f} +/- {sig:.3f}")
    assert abs(grid[i0] - OM_VERD) < 3 * sig, "Om fuera de 3 sigma"
    # sanity: chi2 en la verdad cercana al minimo
    print(f"chi2/dof = {c0 / (N - 2):.2f}")
    # cobertura
    cubre = 0
    for _ in range(200):
        o = [v + rng.gauss(0, SIG) for v in verd]
        cc = [chi2(o, row) for row in teoria]
        j0 = min(range(len(grid)), key=lambda i: cc[i])
        ins = [grid[i] for i in range(len(grid)) if cc[i] <= cc[j0] + 1]
        if min(ins) - 0.0025 <= OM_VERD <= max(ins) + 0.0025:
            cubre += 1
    print(f"cobertura del intervalo de Delta chi2 = 1 en 200 realizaciones: {cubre / 2:.1f} % (esperado ~68 %)")
    assert 55 <= cubre / 2 <= 80, "cobertura fuera de rango"
    print("Pantheon+ (publicado, solo SNe): Om = 0.334 +/- 0.018 ; diferencia con la verdad sintetica 0.315 = 1.1 sigma de esa medida")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
