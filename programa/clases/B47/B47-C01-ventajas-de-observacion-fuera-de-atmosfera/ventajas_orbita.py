#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C01: que se gana al observar fuera de la atmosfera (resolucion, transmision y columna de aire).

Datos: k_B = 1,380649e-23 J/K, atomic mass constant u = 1,66053906892e-27 kg y g0 = 9,80665 m/s2 de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09).
ILUSTRATIVOS (no medidos): apertura D = 0,5 m, r0 = 0,10 m a 500 nm, profundidad optica cenital 0,2, temperatura media 250 K y masa molar media del aire 28,965 g/mol
(valor estandar de uso general, no consultado en esta clase).
Modelo: (1) limite de difraccion FWHM = 1,028 lambda/D; (2) seeing FWHM = 0,98 lambda/r0 con r0 proporcional a lambda^(6/5); (3) atmosfera isoterma, escala H = k T/(m g);
fraccion de masa de aire por encima de h = exp(-h/H), contrastada con una integral numerica de la densidad; (4) Beer-Lambert T = exp(-tau sec z).
Supuestos: isoterma, gravedad constante, atmosfera plana. Validez: ilustrativa; la atmosfera real no es isoterma ni plana a grandes angulos cenitales.
Tolerancia: columna numerica frente a exp(-h/H), 1e-3 relativo.
"""
from __future__ import annotations
import math, platform

KB = 1.380649e-23
U = 1.66053906892e-27
G0 = 9.80665
ARCSEC = math.pi / 180 / 3600


def calc():
    r = {}
    lam, d = 550e-9, 0.5
    r["lam_nm"], r["d"] = 550, d
    r["fwhm_dif"] = 1.028 * lam / d / ARCSEC
    r0_500 = 0.10
    r0 = r0_500 * (lam / 500e-9) ** 1.2
    r["r0"] = r0
    r["fwhm_see"] = 0.98 * lam / r0 / ARCSEC
    r["ratio"] = r["fwhm_see"] / r["fwhm_dif"]
    r["d_igual"] = 1.028 * r0 / 0.98          # apertura donde seeing = difraccion
    m = 28.965e-3 / 6.02214076e23              # kg por molecula (N_A exacto de NIST)
    t = 250.0
    h = KB * t / (m * G0)
    r["H"] = h
    # columna por encima de una altura: analitica y numerica (trapecio sobre densidad)
    def num(hh):
        n = 20000
        top = hh + 40 * h
        dz = (top - hh) / n
        s = 0.5 * (math.exp(-hh / h) + math.exp(-top / h))
        for k in range(1, n):
            s += math.exp(-(hh + k * dz) / h)
        return s * dz / h
    r["col"] = {}
    for km in (10, 36, 100, 400):
        a = math.exp(-km * 1e3 / h)
        b = num(km * 1e3)
        r["col"][km] = (a, b)
    tau0 = 0.2
    r["trans"] = {z: math.exp(-tau0 / math.cos(math.radians(z))) for z in (0, 30, 60)}
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"difraccion D = {r['d']} m a {r['lam_nm']} nm: FWHM = {r['fwhm_dif']:.3f} arcsec")
    print(f"seeing con r0(550 nm) = {r['r0']:.4f} m: FWHM = {r['fwhm_see']:.3f} arcsec ; cociente seeing/difraccion = {r['ratio']:.2f}")
    print(f"apertura donde seeing = difraccion: D = {r['d_igual']:.4f} m")
    print(f"altura de escala H = kT/(mg) = {r['H']:.1f} m")
    print(f"{'h [km]':>8} {'exp(-h/H)':>14} {'integral':>14}")
    for km, (a, b) in r["col"].items():
        print(f"{km:8d} {a:14.4e} {b:14.4e}")
        assert abs(a - b) / a < 1e-3
    for z, t in r["trans"].items():
        print(f"transmision cenital a z = {z} grados: {t:.4f} (espacio: 1.0000)")
    assert 7000 < r["H"] < 7600
    assert abs(r["fwhm_dif"] - 0.2332) < 0.01
    assert r["trans"][60] < r["trans"][30] < r["trans"][0] < 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
