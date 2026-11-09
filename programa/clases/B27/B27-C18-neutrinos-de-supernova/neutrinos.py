#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B27-C18: numero de neutrinos, sucesos esperados en un detector y retraso por masa.

Datos: c, MeV por julio, constante de Avogadro (NIST CODATA 2022), 1 au (IERS TN36), consultados 2026-11-09.
Referencia de contexto: revision de neutrinos de supernova de Mirizzi et al., arXiv:1508.00785 (resumen). La energia
liberada en neutrinos (2.5e46 J), la energia media (10 MeV), la distancia (10 kpc), la seccion eficaz de referencia
(1e-41 cm^2 a 10 MeV, creciendo como E^2), la masa del detector (1 kt de agua) y la masa del neutrino (1 eV) son
ILUSTRATIVOS (sinteticos); no se cita ninguna medicion.
Modelo: N = E_nu/<E>; fluencia = N_i/(4 pi d^2) para un sabor que toma 1/6 de la energia; sucesos = fluencia * sigma * N_p;
retraso de un neutrino de masa m y energia E frente a la luz: dt = (d/c)(1 - beta)/beta con 1 - beta = (mc^2/E)^2/(1 + beta),
aproximacion (d/2c)(mc^2/E)^2.
Supuestos: espectro monoenergetico, sin oscilaciones, sin eficiencia. Validez: orden de magnitud.
Tolerancia: 1e-6 entre el retraso estable y la aproximacion (mc^2/E = 1e-7).
"""
from __future__ import annotations
import math
import platform
import sys

C = 299792458.0
MEV = 1.602176634e-13
NA = 6.02214076e23
AU = 1.49597870700e11
KPC = 1e3 * 648000 / math.pi * AU


def retraso_estable(d, mc2, e):
    beta = math.sqrt(1 - (mc2 / e) ** 2)
    um = (mc2 / e) ** 2 / (1 + beta)
    return d / C * um / beta


def retraso_ingenuo(d, mc2, e):
    beta = math.sqrt(1 - (mc2 / e) ** 2)
    return d / C * (1 - beta) / beta


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    e_nu, e_med = 2.5e46, 10 * MEV
    n_tot = e_nu / e_med
    n_sabor = n_tot / 6
    d = 10 * KPC
    flu = n_sabor / (4 * math.pi * d ** 2)
    print(f"1 kpc = {KPC:.6e} m ; d = 10 kpc = {d:.4e} m")
    print(f"N_total = {n_tot:.4e} neutrinos ; por sabor (1/6) = {n_sabor:.4e} ; fluencia a 10 kpc = {flu:.4e} /m2 = {flu * 1e-4:.4e} /cm2")
    n_p = 2 * NA * 1e9 / 18.0           # protones libres en 1 kt de agua (18 g/mol)
    sigma = 1e-41 * 1e-4                # m2
    sucesos = flu * sigma * n_p
    print(f"protones libres en 1 kt de agua = {n_p:.4e} ; sucesos esperados = {sucesos:.1f} (sigma = 1e-41 cm2 ilustrativa)")
    print(f"{'E [MeV]':>8} {'sigma(E) [cm2]':>16} {'sucesos':>9}")
    for e in (5.0, 10.0, 20.0, 40.0):
        s = 1e-41 * (e / 10) ** 2
        n_ev = (e_nu / (e * MEV) / 6) / (4 * math.pi * d ** 2) * s * 1e-4 * n_p
        print(f"{e:8.1f} {s:16.3e} {n_ev:9.1f}")
    # retraso por masa
    print(f"{'E [MeV]':>8} {'retraso estable [s]':>20} {'aprox [s]':>12} {'ingenuo [s]':>14}")
    for e_mev in (10.0, 20.0, 40.0):
        e = e_mev * MEV
        mc2 = 1.0 * 1.602176634e-19         # 1 eV
        est = retraso_estable(d, mc2, e)
        apr = d / (2 * C) * (mc2 / e) ** 2
        ing = retraso_ingenuo(d, mc2, e)
        assert abs(est / apr - 1) < 1e-6, "retraso estable frente a aproximacion"
        print(f"{e_mev:8.1f} {est:20.6e} {apr:12.4e} {ing:14.6e}")
    t10 = retraso_estable(d, 1.602176634e-19, 10 * MEV)
    t20 = retraso_estable(d, 1.602176634e-19, 20 * MEV)
    print(f"diferencia de llegada entre 10 y 20 MeV por masa: {t10 - t20:.4e} s")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
