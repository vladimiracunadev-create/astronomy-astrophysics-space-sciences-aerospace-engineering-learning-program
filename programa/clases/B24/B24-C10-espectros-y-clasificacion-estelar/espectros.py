#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B24-C10: ley de Wien, Boltzmann y Saha para el hidrogeno.

Datos (NIST CODATA 2022, consultados 2026-11-09): h, c, k_B, m_e, eV, constante de
desplazamiento de Wien. Energia de ionizacion del H: 13.605693 eV (NIST, Rydberg hc en eV).
Presion electronica P_e = 1 Pa y el tamano de la suma de estados (n <= 6): valores ILUSTRATIVOS
(estimados) para una atmosfera de tipo A; no son una estrella concreta.
Modelo: Planck B_lambda(T) y su maximo numerico frente a la constante de Wien; Saha
n_II/n_I = (kT/P_e)(2 pi m_e kT/h^2)^(3/2) exp(-chi/kT) (2 g_II/g_I = 1 para H); Boltzmann
n(2)/n(total neutro) = 8 exp(-E2/kT)/U con g_n = 2 n^2 y U = sum_{n<=6} g_n exp(-E_n/kT).
Supuestos: equilibrio termodinamico local, atmosfera de H puro. Validez: ilustrativa de la
fuerza relativa de la linea de Balmer. Tolerancia: 1e-6 en el maximo de Planck; 1e-3 en la
particion de traslacion por cuadratura.
"""
from __future__ import annotations
import math
import platform
import sys

H, C, KB, ME = 6.62607015e-34, 299792458.0, 1.380649e-23, 9.1093837139e-31
EV = 1.602176634e-19
B_WIEN = 2.897771955e-3
CHI = 13.605693122990 * EV
PE = 1.0


def planck(lam, T):
    x = H * C / (lam * KB * T)
    return 2 * H * C * C / lam ** 5 / math.expm1(x)


def pico_planck(T):
    a, b = 1e-8, 1e-5
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(300):
        if planck(c, T) > planck(d, T):
            b = d
        else:
            a = c
        c, d = b - g * (b - a), a + g * (b - a)
    return (a + b) / 2


def part_traslacion_cerrada(T):
    return (2 * math.pi * ME * KB * T / H ** 2) ** 1.5


def part_traslacion_cuadratura(T, n=200000):
    """2 * Int 4 pi p^2 dp/h^3 exp(-p^2/(2 m k T)) / 2 (el 2 del espin se cancela con g_II/g_I = 1/2)."""
    pmax = 12 * math.sqrt(2 * ME * KB * T)
    dp = pmax / n
    s = 0.0
    for i in range(n):
        p = (i + 0.5) * dp
        s += 4 * math.pi * p * p * math.exp(-p * p / (2 * ME * KB * T)) * dp
    return s / H ** 3


def saha_ratio(T):
    return (KB * T / PE) * part_traslacion_cerrada(T) * math.exp(-CHI / (KB * T))


def frac_n2(T):
    e = lambda n: CHI * (1 - 1 / n ** 2)
    u = sum(2 * n * n * math.exp(-e(n) / (KB * T)) for n in range(1, 7))
    return 8 * math.exp(-e(2) / (KB * T)) / u


def balmer(T):
    return frac_n2(T) / (1 + saha_ratio(T))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for T in (3200.0, 5772.0, 9900.0, 30000.0):
        lam = pico_planck(T)
        assert abs(lam * T / B_WIEN - 1) < 1e-6, "Wien: maximo numerico != constante NIST"
        print(f"T = {T:7.0f} K -> lambda_max = {lam * 1e9:7.1f} nm")
    t = 8000.0
    assert abs(part_traslacion_cuadratura(t) / part_traslacion_cerrada(t) - 1) < 1e-3
    temps = [4000 + 100 * i for i in range(0, 121)]
    vals = [balmer(T) for T in temps]
    imax = max(range(len(vals)), key=lambda i: vals[i])
    print(f"Saha: fraccion neutra a 9900 K = {1 / (1 + saha_ratio(9900.0)):.3f}")
    print(f"Balmer (relativo) a 5772 K = {balmer(5772.0) / vals[imax]:.2e} ; a 30000 K = {balmer(30000.0) / vals[imax]:.2e}")
    print(f"maximo de la linea de Balmer (P_e = 1 Pa, H puro): T = {temps[imax]} K")
    assert 6000 < temps[imax] < 14000
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
