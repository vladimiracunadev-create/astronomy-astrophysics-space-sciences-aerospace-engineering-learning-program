#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B29-C17: dispersion de un pulso de radio, desdispersion y recuperacion de la medida de dispersion.

Datos: c, e, m_e, epsilon_0 (NIST CODATA 2022) y 1 au (IERS TN36), consultados 2026-11-09; 1 pc = 648000/pi au. Contexto: Lorimer y colaboradores descubrieron un estallido
de 30 Jy con duracion menor de 5 ms cuya dispersion implica una distancia menor de 1 Gpc (arXiv:0709.4301, resumen); Petroff revisa los estallidos rapidos de radio
(arXiv:1904.07947, resumen), consultados 2026-11-09. La banda (1200-1500 MHz, 32 canales), la medida de dispersion (300 pc/cm^3), la anchura del pulso (1.5 ms) y el ruido
son ILUSTRATIVOS (sinteticos).
Modelo: retardo entre frecuencias f1 < f2 (MHz): dt = k_DM DM (1/f1^2 - 1/f2^2) con k_DM = e^2/(8 pi^2 epsilon_0 m_e c) = 4148.8 s MHz^2 cm^3/pc (calculada aqui);
desdispersion: desplazar cada canal al retardo del trial y sumar; relacion senal-ruido del maximo de la serie sumada; busqueda en una rejilla de DM; Monte Carlo (semilla fija).
Supuestos: pulso gaussiano, ruido blanco gaussiano, sin dispersion intra-canal, sin ensanchamiento por dispersion. Validez: ilustrativa.
Tolerancia: constante de dispersion dentro del 0.5 % de 4148.8; DM recuperada dentro de 8 pc/cm^3 de la verdadera en el 100 % de los ensayos y con desviacion menor que 4.
"""
from __future__ import annotations
import math
import platform
import random
import statistics
import sys

C, E, ME, EPS0 = 299792458.0, 1.602176634e-19, 9.1093837139e-31, 8.8541878188e-12
AU = 1.49597870700e11
PC = 648000 / math.pi * AU
K_SI = E ** 2 / (8 * math.pi ** 2 * EPS0 * ME * C)
K_DM = K_SI * PC * 1e6 / 1e12            # s MHz^2 cm^3/pc

NCH, F0, F1 = 32, 1200.0, 1500.0
DT_MS, NT = 1.0, 1024
FREQS = [F0 + (F1 - F0) * (i + 0.5) / NCH for i in range(NCH)]
F_REF = FREQS[-1]


def retardo_ms(dm, f):
    return 1e3 * K_DM * dm * (1 / f ** 2 - 1 / F_REF ** 2)


def sintetizar(dm, t_ref_ms, ancho_ms, amp, rng):
    datos = []
    for f in FREQS:
        t_c = t_ref_ms + retardo_ms(dm, f)
        fila = []
        for i in range(NT):
            t = i * DT_MS
            fila.append(rng.gauss(0, 1) + amp * math.exp(-0.5 * ((t - t_c) / ancho_ms) ** 2))
        datos.append(fila)
    return datos


def desdispersar(datos, dm):
    serie = [0.0] * NT
    for f, fila in zip(FREQS, datos):
        s = int(round(retardo_ms(dm, f) / DT_MS))
        for i in range(NT - s):
            serie[i] += fila[i + s]
    return serie


def snr_pico(serie):
    m = statistics.median(serie)
    dev = [abs(x - m) for x in serie]
    sigma = 1.4826 * statistics.median(dev)
    return (max(serie) - m) / sigma


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"k_DM = e^2/(8 pi^2 epsilon_0 m_e c) = {K_DM:.2f} s MHz^2 cm^3/pc")
    assert abs(K_DM / 4148.8 - 1) < 5e-3
    for dm in (100.0, 300.0, 1000.0):
        print(f"DM = {dm:6.0f} pc/cm3: retardo entre {F0:.0f} y {F1:.0f} MHz = {1e3 * K_DM * dm * (1 / F0 ** 2 - 1 / F1 ** 2):8.1f} ms")
    # resolucion en DM
    ancho = 1.5
    d_dm = ancho * 1e-3 / (K_DM * (1 / F0 ** 2 - 1 / F1 ** 2))
    print(f"resolucion en DM para un pulso de {ancho} ms en la banda completa: ~{d_dm:.2f} pc/cm3")
    # dispersion intra-canal
    dnu = (F1 - F0) / NCH
    smear = 2 * K_DM * 300.0 * dnu / (0.5 * (F0 + F1)) ** 3
    print(f"ensanchamiento intra-canal ({dnu:.2f} MHz, DM = 300, f centrales): {smear * 1e3:.3f} ms")
    rng = random.Random(20261109)
    dm_v, trials = 300.0, [250.0 + 100.0 * i / 100 for i in range(101)]
    # una realizacion: perfil de SNR frente a DM
    datos = sintetizar(dm_v, 300.0, ancho, 0.9, rng)
    perfil = [snr_pico(desdispersar(datos, d)) for d in trials]
    imax = max(range(len(perfil)), key=lambda i: perfil[i])
    print(f"{'DM trial':>9} {'SNR':>8}")
    for d, s in zip(trials[::10], perfil[::10]):
        print(f"{d:9.1f} {s:8.2f}")
    print(f"maximo en DM = {trials[imax]:.1f} con SNR = {perfil[imax]:.2f} ; SNR sin desdispersar (DM = 0) = {snr_pico(desdispersar(datos, 0.0)):.2f}")
    # Monte Carlo
    rec = []
    for _ in range(25):
        dat = sintetizar(dm_v, 300.0, ancho, 0.9, rng)
        pf = [snr_pico(desdispersar(dat, d)) for d in trials[::2]]
        j = max(range(len(pf)), key=lambda i: pf[i])
        rec.append(trials[::2][j])
    print(f"25 realizaciones: DM recuperada = {statistics.mean(rec):.2f} +/- {statistics.pstdev(rec):.2f} (verdadera {dm_v})")
    assert all(abs(r - dm_v) < 8.0 for r in rec) and statistics.pstdev(rec) < 4.0, "recuperacion de DM"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
