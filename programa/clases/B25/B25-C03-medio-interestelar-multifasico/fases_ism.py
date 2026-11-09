#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C03: presion termica, velocidad del sonido y masa de las fases del medio interestelar.

Datos: Tabla I de Ferriere (2001), arXiv:astro-ph/0106359 (texto del PDF consultado 2026-11-09),
valores ESTIMADOS cerca del Sol: fase, T (K), n (cm^-3, nucleos de H), Sigma_sol (Msol/pc2),
M (1e9 Msol). La Tabla da rangos; aqui se usa un valor representativo por fase (el centro
geometrico del rango, un criterio NUESTRO). Constantes: k_B, m_p (NIST, CODATA 2022, 2026-11-09); 1 pc = 3,0856776e16 m (conversion).
El factor 1,42 m_p por nucleo de H y los porcentajes 70,4/28,1/1,5 % proceden del mismo texto.
Modelo: gas ideal, presion termica p/k = n_tot T con n_tot = n (aprox. para el calculo
relativo), velocidad del sonido adiabatica c = sqrt(gamma k T / (mu m_p)), gamma = 5/3.
Supuestos: fases homogeneas e independientes; se ignora la presion magnetica, turbulenta y de
rayos cosmicos. mu = 1,3 (neutro atomico) y 0,6 (ionizado) son valores ILUSTRATIVOS.
Validez: orden de magnitud (factor 2-3). Tolerancias: 1e-9 en identidades.
"""
from __future__ import annotations
import math
import platform
import sys

KB = 1.380649e-23
MP = 1.67262192595e-27
PC = 3.0856775814913673e16
MSOL = 1.3271244e20 / 6.67430e-11

# nombre: (T_min, T_max, n_min, n_max, Sigma Msol/pc2, mu)
FASES = {
    "cold atomic (CNM)": (50.0, 100.0, 20.0, 50.0, 3.5, 1.3),
    "warm atomic (WNM)": (6000.0, 10000.0, 0.2, 0.5, 3.5, 1.3),
    "warm ionized (WIM)": (8000.0, 8000.0, 0.2, 0.5, 1.4, 0.6),
    "hot ionized (HIM)": (1e6, 1e6, 0.0065, 0.0065, None, 0.6),
}


def centro(a, b):
    return math.sqrt(a * b)


def presion_sobre_k(n, t):
    return n * t


def sonido(t, mu, gamma=5.0 / 3.0):
    return math.sqrt(gamma * KB * t / (mu * MP))


def sigma_a_n(sigma_msol_pc2, altura_pc=None):
    """Densidad de columna N (cm^-2 de nucleos de H) desde Sigma, con rho = 1,42 m_p N."""
    g_cm2 = sigma_msol_pc2 * MSOL * 1e3 / (PC * 100) ** 2  # g/cm^2
    return g_cm2 / (1.42 * MP * 1e3)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # Prueba 1: 1,42 = 1/0,704 (fraccion de masa de hidrogeno 70,4 %)
    assert abs(1 / 0.704 - 1.42) < 1e-3
    # Prueba 2: conversion de unidades Sigma -> N, comprobada por una via independiente
    # (masa / area en SI)
    m_si = 1.0 * MSOL
    area_si = PC ** 2
    n_via2 = (m_si / area_si) * 1e-4 / (1.42 * MP)  # kg/m2 -> kg/cm2 -> nucleos/cm2
    assert abs(sigma_a_n(1.0) / n_via2 - 1) < 1e-9
    # Prueba 3: escala del sonido
    assert abs(sonido(4e4, 1.3) / sonido(1e4, 1.3) - 2.0) < 1e-12
    print("fase | T repr. (K) | n repr. (cm^-3) | p/k (K cm^-3) | c (km/s)")
    pks = {}
    for nombre, (t0, t1, n0, n1, sig, mu) in FASES.items():
        t, n = centro(t0, t1), centro(n0, n1)
        pks[nombre] = presion_sobre_k(n, t)
        print(f"{nombre:20s} {t:9.0f} {n:11.3g} {pks[nombre]:11.0f} {sonido(t, mu) / 1e3:8.1f}")
    cn, wn = pks["cold atomic (CNM)"], pks["warm atomic (WNM)"]
    print(f"p/k(CNM) / p/k(WNM) = {cn / wn:.2f}")
    sig_total = sum(f[4] for f in FASES.values() if f[4])
    print(f"Sigma gas atomico+ionizado = {sig_total:.1f} Msol/pc2 ; N = {sigma_a_n(sig_total):.2e} cm^-2")
    print(f"densidad media de la Tabla: n = {2.7e-24 / (1.42 * MP * 1e3):.2f} cm^-3 (de 2,7e-24 g/cm3)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
