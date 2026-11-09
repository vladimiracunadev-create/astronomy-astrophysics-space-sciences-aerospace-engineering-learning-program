#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C19: distancia de luminosidad en modelos con constante cosmologica, EdS y abierto.

Datos: H0 = 67.4 km/s/Mpc y Omega_m = 0.315 (Planck 2018, arXiv:1807.06209, resumen, consultado 2026-11-09);
c exacta (NIST CODATA 2022). Los modelos Einstein-de Sitter (Om = 1) y abierto sin Lambda (Om = 0.3,
Ok = 0.7) son comparaciones ILUSTRATIVAS; Riess et al. (astro-ph/9805201) encontraron SNe Ia 10-15 % mas
lejanas que lo esperado sin constante cosmologica (resumen); Pantheon+ (arXiv:2202.04077): 1550 SNe Ia,
Omega_m = 0.334 +/- 0.018 (solo SNe, plano LCDM, resumen).
Modelo: E(z)^2 = Om (1+z)^3 + Ok (1+z)^2 + OL, Ok = 1 - Om - OL. Distancia comovil D_C = (c/H0) Int dz/E;
transversal D_M = D_C (Ok = 0), (c/H0) sinh(sqrt(Ok) D_C H0/c)/sqrt(Ok) (Ok > 0). D_L = (1+z) D_M.
Modulo de distancia mu = 5 log10(D_L / 10 pc). Soluciones cerradas: EdS D_L = 2(c/H0)(1+z)(1 - 1/sqrt(1+z));
Milne (Om = OL = 0, Ok = 1) D_L = (c/H0) z (1 + z/2).
Supuestos: sin radiacion; homogeneidad. Validez: z <~ 2.
Tolerancia: 1e-9 frente a las soluciones cerradas.
"""
from __future__ import annotations
import math
import platform
import sys

C_KMS = 299792.458
H0 = 67.4


def dl_mpc(z, om, ol, n=4000):
    ok = 1 - om - ol
    E = lambda zz: math.sqrt(om * (1 + zz) ** 3 + ok * (1 + zz) ** 2 + ol)
    h = z / n
    s = 1 / E(0) + 1 / E(z)
    for i in range(1, n):
        s += (4 if i % 2 else 2) / E(i * h)
    dc = C_KMS / H0 * s * h / 3
    if ok > 1e-12:
        dm = C_KMS / H0 / math.sqrt(ok) * math.sinh(math.sqrt(ok) * dc * H0 / C_KMS)
    elif ok < -1e-12:
        dm = C_KMS / H0 / math.sqrt(-ok) * math.sin(math.sqrt(-ok) * dc * H0 / C_KMS)
    else:
        dm = dc
    return (1 + z) * dm


def mu(dl):
    return 5 * math.log10(dl * 1e6 / 10.0)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for z in (0.1, 0.5, 1.0):
        eds = dl_mpc(z, 1.0, 0.0)
        assert abs(eds / (2 * C_KMS / H0 * (1 + z) * (1 - 1 / math.sqrt(1 + z))) - 1) < 1e-9, "EdS"
        mil = dl_mpc(z, 0.0, 0.0)
        assert abs(mil / (C_KMS / H0 * z * (1 + z / 2)) - 1) < 1e-9, "Milne"
    print(f"{'z':>5} {'LCDM (0.315,0.685)':>20} {'EdS (1,0)':>11} {'abierto (0.3,0)':>16}  [D_L en Mpc, H0 = {H0}]")
    for z in (0.1, 0.5, 1.0, 1.5):
        a, b, c = dl_mpc(z, 0.315, 0.685), dl_mpc(z, 1.0, 0.0), dl_mpc(z, 0.3, 0.0)
        print(f"{z:5.1f} {a:20.1f} {b:11.1f} {c:16.1f}")
    for z in (0.5, 1.0):
        a, c = dl_mpc(z, 0.315, 0.685), dl_mpc(z, 0.3, 0.0)
        print(f"z = {z}: D_L(LCDM)/D_L(abierto sin L) = {a / c:.4f} ({100 * (a / c - 1):+.1f} %) ; delta mu = {mu(a) - mu(c):+.3f} mag")
    z = 0.5
    print(f"z = 0.5: mu(LCDM) = {mu(dl_mpc(z, 0.315, 0.685)):.3f} ; mu(EdS) = {mu(dl_mpc(z, 1.0, 0.0)):.3f}")
    # dependencia con Omega_m (plano)
    for om in (0.25, 0.315, 0.334):
        print(f"plano Om = {om}: D_L(z = 0.5) = {dl_mpc(0.5, om, 1 - om):.1f} Mpc")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
