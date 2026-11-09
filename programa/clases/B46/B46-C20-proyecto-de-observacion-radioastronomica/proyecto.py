#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C20: presupuesto de sensibilidad y de tiempo de un proyecto de observacion, con validacion Monte Carlo (semilla fija).

Datos: k y c de NIST CODATA 2022 (consultada 2026-11-09); 1420.405751768 MHz de la linea de HI consultado en Wikipedia (Hydrogen line) el 2026-11-09.
El plato de 25 m, la eficiencia 0,6, T_sys = 35 K, la linea (pico 0,25 K, FWHM 20 km/s), el canal de 2 km/s, la S/N objetivo de 5, la eficiencia de
observacion del 60 % y el conjunto de 6 antenas son ILUSTRATIVOS; no describen un proyecto ni un instrumento reales. Semilla 20261109.
Modelo: ON/OFF con tiempo igual: sigma_T = T_sys sqrt(2/(dnu t)) con t el tiempo en cada estado; t_on = 2 (S/N T_sys/T_p)^2/dnu. Interferometro:
sigma_S = SEFD/sqrt(N_bl dnu t) con SEFD = 2 k T_sys/A_e (una polarizacion, parte real). Monte Carlo: S/N medida = (T_p + ruido)/sigma.
Supuestos: ruido blanco gaussiano, sin baseline estructurada ni interferencias. Validez: orientativa.
Tolerancia: S/N media de la simulacion dentro de 0,1 de 5; fraccion de deteccion a 3 sigma dentro de 0,01 de la analitica.
"""
from __future__ import annotations
import math, platform, random
K, C = 1.380649e-23, 299792458.0
NU = 1420.405751768e6

def calc():
    rng = random.Random(20261109)
    Tsys, Tp, dv, snr = 35.0, 0.25, 2.0, 5.0
    dnu = NU * dv * 1e3 / C
    t_state = 2 * (snr * Tsys / Tp) ** 2 / dnu         # tiempo por estado: sigma = Tsys sqrt(2/(dnu t))
    sigma = Tsys * math.sqrt(2 / (dnu * t_state))
    t_total = 2 * t_state
    t_cal = t_total / 0.6
    # Monte Carlo
    medidas = [(Tp + rng.gauss(0, sigma)) / sigma for _ in range(20000)]
    m = sum(medidas) / len(medidas)
    sd = math.sqrt(sum((x - m) ** 2 for x in medidas) / (len(medidas) - 1))
    fr3 = sum(1 for x in medidas if x > 3) / len(medidas)
    ana3 = 0.5 * (1 + math.erf((snr - 3) / math.sqrt(2)))
    # conjunto
    Ae = 0.6 * math.pi * 25.0 ** 2 / 4
    sefd = 2 * K * Tsys / Ae / 1e-26
    nbl = 6 * 5 // 2
    t_int = 600.0
    sS = sefd / math.sqrt(nbl * dnu * t_int)
    # volumen de datos
    bytes_dia = 4096 * 8 * 86400
    return dict(dnu=dnu, t_state=t_state, sigma=sigma, t_total=t_total, t_cal=t_cal, m=m, sd=sd, fr3=fr3, ana3=ana3, sefd=sefd, sS=sS,
                nbl=nbl, Ae=Ae, gb_dia=bytes_dia / 1e9, K_por_Jy=Ae / (2 * K) * 1e-26)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"canal de 2 km/s = {r['dnu']/1e3:.3f} kHz ; sigma objetivo = {r['sigma']*1e3:.1f} mK (pico 250 mK / 5)")
    print(f"tiempo por estado = {r['t_state']:.1f} s ; ON+OFF = {r['t_total']:.1f} s ; con eficiencia 60 % = {r['t_cal']:.1f} s de reloj")
    print(f"Monte Carlo (20000): S/N media = {r['m']:.3f} ; desviacion = {r['sd']:.3f} ; fraccion sobre 3 sigma = {r['fr3']:.4f} (analitica {r['ana3']:.4f})")
    print(f"SEFD = {r['sefd']:.0f} Jy ; conjunto de {r['nbl']} lineas de base, 600 s: sigma_S = {r['sS']*1e3:.2f} mJy por canal de 2 km/s")
    print(f"volumen de datos = {r['gb_dia']:.2f} GB por dia (4096 canales, 8 bytes, 1 s)")
    assert abs(r["m"] - 5.0) < 0.1 and abs(r["sd"] - 1.0) < 0.03
    assert abs(r["fr3"] - r["ana3"]) < 0.01
    assert abs(r["sigma"] - 0.05) < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
