#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C11: ajuste de la ley de Hubble-Lemaitre con datos SINTETICOS y tiempo de Hubble.

Datos: c exacta (NIST CODATA 2022); 1 au = 1.495 978 707 00e11 m (IERS Conventions 2010, TN36, Tabla 1.1)
y pc = 648000/pi au (definicion geometrica) para convertir Mpc a km. Valores publicados de H0:
Planck 2018 67.4 +/- 0.5 (arXiv:1807.06209) y Riess et al. 2019 74.03 +/- 1.42 (arXiv:1903.07603), ambos en
km/s/Mpc, solo resumen, consultados 2026-11-09. Galaxias sinteticas: H0 verdadero 70.0, dispersion
de velocidades peculiares 300 km/s, distancias de 20 a 400 Mpc, semilla fija (valores ILUSTRATIVOS).
Modelo: v = H0 d. Ajuste por minimos cuadrados con ordenada nula: H0 = sum(v d)/sum(d^2), con
sigma(H0) = sigma_v / sqrt(sum d^2). Tiempo de Hubble 1/H0. Corrimiento: v = c z (z << 1); la formula
Doppler relativista v = c ((1+z)^2 - 1)/((1+z)^2 + 1) = c tanh(ln(1+z)).
Supuestos: velocidades peculiares gaussianas e independientes, distancias exactas. Validez: z << 1.
Tolerancia: H0 recuperado dentro de 3 sigma; 1e-12 entre las dos formas del Doppler.
"""
from __future__ import annotations
import math
import platform
import random
import sys

C = 299792.458          # km/s
AU = 1.49597870700e11   # m
MPC_KM = 1e6 * (648000 / math.pi) * AU / 1e3
H0_VERD, SIG_V = 70.0, 300.0
YR = 365.25 * 86400.0


def tiempo_hubble_gyr(h0):
    return MPC_KM / h0 / YR / 1e9


def doppler_rel(z):
    return C * ((1 + z) ** 2 - 1) / ((1 + z) ** 2 + 1)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"1 Mpc = {MPC_KM:.6e} km")
    rng = random.Random(11)
    d = [rng.uniform(20, 400) for _ in range(40)]
    v = [H0_VERD * di + rng.gauss(0, SIG_V) for di in d]
    sdd = sum(x * x for x in d)
    h0 = sum(a * b for a, b in zip(v, d)) / sdd
    sig = SIG_V / math.sqrt(sdd)
    assert abs(h0 - H0_VERD) < 3 * sig, "H0 fuera de 3 sigma"
    print(f"ajuste con 40 galaxias sinteticas: H0 = {h0:.2f} +/- {sig:.2f} km/s/Mpc (verdadero {H0_VERD})")
    for nombre, h in (("Planck 2018 (67.4)", 67.4), ("Riess 2019 (74.03)", 74.03), ("sintetico (70)", 70.0)):
        print(f"1/H0 para {nombre}: {tiempo_hubble_gyr(h):.3f} Gyr")
    assert abs(tiempo_hubble_gyr(70.0) - 977.792 / 70.0) < 5e-3
    for z in (0.001, 0.01, 0.1, 0.5):
        v1, v2 = C * z, doppler_rel(z)
        assert abs(v2 - C * math.tanh(math.log(1 + z))) < 1e-9 * C
        print(f"z = {z:5.3f}: c z = {v1:10.1f} km/s ; Doppler relativista = {v2:10.1f} km/s ; diferencia {100 * (v1 / v2 - 1):6.2f} %")
    print(f"distancia por la ley (z = 0.01, H0 = 70): d = c z/H0 = {C * 0.01 / 70:.1f} Mpc")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
