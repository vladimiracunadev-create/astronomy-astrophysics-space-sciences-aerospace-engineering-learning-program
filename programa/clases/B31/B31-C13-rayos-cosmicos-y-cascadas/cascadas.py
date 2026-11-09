#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C13: modelo de cascada de Heitler, espectro de potencias y umbral de interaccion con el fondo cosmico de microondas.

Datos: masa del proton (938.272 089 43 MeV), k_B (NIST CODATA 2022), consultados 2026-11-09. La energia critica xi_c = 85 MeV, la longitud de radiacion de 37 g/cm^2, el indice espectral
(2.7), la masa de la resonancia Delta (1232 MeV), la temperatura del fondo (2.725 K), el factor 2.7 para la energia media de un foton y la energia primaria (1e18 eV) son ILUSTRATIVOS (sinteticos).
Modelo: (1) cascada de Heitler: n generaciones con N = 2^n particulas y energia E_0/2^n; la cascada se detiene en E_0/2^n = xi_c, de modo que N_max = E_0/xi_c y X_max = lambda_r ln(E_0/xi_c);
tasa de elongacion dX_max/dlog10(E_0) = lambda_r ln 10; superposicion para un nucleo de masa A: X_max(A) = X_max(1) - lambda_r ln A; (2) espectro N(>E) ~ E^-(gamma - 1) muestreado
con semilla fija y estimador de maxima verosimilitud; (3) umbral de produccion de la Delta en una colision frontal proton-foton: E_th = (m_Delta^2 - m_p^2)/(4 epsilon), verificado con el invariante s = m_p^2 + 2 epsilon (E + p) de la colision frontal.
Supuestos: cascada electromagnetica simplificada, colision frontal. Validez: orden de magnitud.
Tolerancia: generaciones enteras frente a la formula a 1e-12; indice estimado dentro de 3 errores; umbral por cuadrivectores frente a la formula cerrada a 1e-9.
"""
from __future__ import annotations
import math
import platform
import random
import sys

MP_MEV, MDELTA_MEV = 938.27208943, 1232.0
KB_EV = 8.617333262e-5
XI_C, LAM_R = 85e6, 37.0


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'E_0 [eV]':>10} {'generaciones n':>15} {'N_max = E_0/xi_c':>18} {'X_max [g/cm^2]':>15}")
    for e0 in (1e15, 1e17, 1e18, 1e19, 1e20):
        n = math.log2(e0 / XI_C)
        nmax = 2 ** n
        assert abs(nmax / (e0 / XI_C) - 1) < 1e-12
        print(f"{e0:10.0e} {n:15.3f} {e0 / XI_C:18.4e} {LAM_R * math.log(e0 / XI_C):15.1f}")
    el = (LAM_R * math.log(1e19 / XI_C) - LAM_R * math.log(1e18 / XI_C))
    print(f"tasa de elongacion: X_max(1e19) - X_max(1e18) = {el:.2f} g/cm^2 por decada ; lambda_r ln 10 = {LAM_R * math.log(10):.2f}")
    assert abs(el / (LAM_R * math.log(10)) - 1) < 1e-12
    xp = LAM_R * math.log(1e18 / XI_C)
    print(f"nucleo de hierro (A = 56) a 1e18 eV: X_max = {xp - LAM_R * math.log(56):.1f} g/cm^2 ; desplazamiento = {-LAM_R * math.log(56):.1f} g/cm^2 respecto del proton ({xp:.1f})")
    # espectro
    rng = random.Random(20261109)
    gamma, n = 2.7, 5000
    xs = [(1 - rng.random()) ** (-1 / (gamma - 1)) for _ in range(n)]
    g_hat = 1 + n / sum(math.log(x) for x in xs)
    err = (g_hat - 1) / math.sqrt(n)
    print(f"{n} eventos con indice diferencial {gamma}: estimado = {g_hat:.4f} +/- {err:.4f}")
    assert abs(g_hat - gamma) < 3 * err
    frac = sum(1 for x in xs if x > 10) / n
    print(f"fraccion con energia > 10 veces el umbral: {frac:.4f} ; teoria 10^-(gamma - 1) = {10 ** -(gamma - 1):.4f}")
    # umbral
    eps = 2.7 * KB_EV * 2.725
    e_th_formula = (MDELTA_MEV ** 2 - MP_MEV ** 2) * 1e12 / (4 * eps)       # eV^2 / eV -> eV (masas en MeV -> 1e12 eV^2)
    lo, hi = 1e18, 1e23
    for _ in range(300):
        e = math.sqrt(lo * hi)
        p = math.sqrt(e * e - (MP_MEV * 1e6) ** 2)
        s = (MP_MEV * 1e6) ** 2 + 2 * eps * (e + p)   # invariante s = m^2 + 2 eps (E + p) para un foton en sentido contrario (evita la cancelacion de E^2 - p^2)
        if s < (MDELTA_MEV * 1e6) ** 2:
            lo = e
        else:
            hi = e
    e_th_num = math.sqrt(lo * hi)
    print(f"energia media del foton del fondo: {eps * 1e4:.3f}e-4 eV ; umbral de la Delta: formula = {e_th_formula:.4e} eV ; cuadrivectores = {e_th_num:.4e} eV ; cociente = {e_th_num / e_th_formula:.8f}")
    assert abs(e_th_num / e_th_formula - 1) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
