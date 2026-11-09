#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C18: precision del retardo VLBI por la pendiente de fase y su traduccion a longitud de linea de base (semilla fija).

Datos: c de NIST CODATA 2022 (consultada 2026-11-09). La banda (8,0 a 8,5 GHz en 16 canales), el retardo verdadero (1234,5 ns), la S/N por canal
(10, 20, 40) y la linea de base de 6000 km con fuente a 60 grados del eje son ILUSTRATIVOS; no son de ninguna red real.
Modelo: fase por canal phi_k = 2 pi nu_k tau + ruido gaussiano de desviacion 1/SNR; el retardo es la pendiente de un ajuste por minimos
cuadrados del fase desenrollada. Cota teorica: sigma_tau = (1/SNR)/(2 pi sqrt(N) sigma_nu), con sigma_nu = rms de las frecuencias de los canales.
Longitud: dtau c = dB cos(angulo entre la linea de base y la fuente).
Supuestos: fase sin ambiguedades (se parte de un retardo aproximado conocido), ruido blanco, sin ionosfera. Validez: orientativa.
Tolerancia: sigma simulada dentro del 10 % de la cota para 4000 repeticiones.
"""
from __future__ import annotations
import math, platform, random
C = 299792458.0

def calc():
    rng = random.Random(20261109)
    N = 16
    nus = [8.0e9 + k * (0.5e9 / (N - 1)) for k in range(N)]
    mnu = sum(nus) / N
    snu = math.sqrt(sum((v - mnu) ** 2 for v in nus) / N)
    tau0 = 1234.5e-9
    filas = []
    for snr in (10.0, 20.0, 40.0):
        est = []
        for _ in range(4000):
            ph = [2 * math.pi * (v - mnu) * tau0 + rng.gauss(0, 1 / snr) for v in nus]
            y = sum(ph) / N
            pend = sum((v - mnu) * (p - y) for v, p in zip(nus, ph)) / sum((v - mnu) ** 2 for v in nus)
            est.append(pend / (2 * math.pi))
        m = sum(est) / len(est)
        sd = math.sqrt(sum((e - m) ** 2 for e in est) / (len(est) - 1))
        teor = 1 / snr / (2 * math.pi * math.sqrt(N) * snu)
        filas.append((snr, m, sd, teor))
    sig_ps = filas[0][2] * 1e12
    dB_mm = filas[0][2] * C * 1e3 / math.cos(math.radians(60))
    return dict(filas=filas, snu=snu, tau0=tau0, dB_mm=dB_mm, c_mm_ps=C * 1e-12 * 1e3, tect=20.0)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"dispersion rms de las frecuencias = {r['snu']/1e6:.2f} MHz ; 1 ps equivale a {r['c_mm_ps']:.4f} mm de camino")
    print(f"{'S/N por canal':>14} {'tau medio [ns]':>15} {'sigma simulada [ps]':>20} {'cota [ps]':>10}")
    for snr, m, sd, teor in r["filas"]:
        print(f"{snr:14.0f} {m*1e9:15.6f} {sd*1e12:20.3f} {teor*1e12:10.3f}")
    print(f"con S/N = 10: error de la linea de base (fuente a 60 grados) = {r['dB_mm']:.2f} mm")
    for snr, m, sd, teor in r["filas"]:
        assert abs(sd / teor - 1) < 0.1 and abs(m - r["tau0"]) < 5 * teor / math.sqrt(4000) * 3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
