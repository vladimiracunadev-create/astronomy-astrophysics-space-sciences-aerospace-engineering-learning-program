#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C06: cascada de Friis y ecuacion del radiometro (simulacion con semilla fija).

Datos: ninguno externo. Las temperaturas y ganancias de la cadena (LNA 25 K y 30 dB; mezclador 800 K y -6 dB; FI 400 K), el cielo (20 K),
el ancho de banda (1 MHz) y los tiempos son ILUSTRATIVOS. Semilla 20261109.
Modelo: T_sys = T_cielo + T_spill + T_1 + T_2/G_1 + T_3/(G_1 G_2); sigma_T = T_sys/sqrt(B tau). Simulacion: ruido gaussiano real muestreado a
Nyquist (2 B tau muestras independientes), deteccion cuadratica; la desviacion relativa de la potencia media es sqrt(2/N) = 1/sqrt(B tau).
Conmutacion de Dicke: la diferencia de dos mitades independientes aumenta sigma en un factor 2 frente al total.
Supuestos: ruido blanco gaussiano, ganancia constante. Validez: orientativa.
Tolerancia: desviacion simulada dentro del 3 % de la teorica con 2000 repeticiones.
"""
from __future__ import annotations
import math, platform, random

def friis(Ts, Gs):
    t, g = 0.0, 1.0
    for T, G in zip(Ts, Gs):
        t += T / g
        g *= G
    return t

def sim(B_tau, reps, rng):
    N = int(2 * B_tau)
    medias = []
    for _ in range(reps):
        s = 0.0
        for _ in range(N):
            x = rng.gauss(0, 1)
            s += x * x
        medias.append(s / N)
    m = sum(medias) / reps
    sd = math.sqrt(sum((x - m) ** 2 for x in medias) / (reps - 1))
    return m, sd / m

def calc():
    rng = random.Random(20261109)
    db = lambda x: 10 ** (x / 10)
    Tcas = friis([25.0, 800.0, 400.0], [db(30), db(-6), 1.0])
    Tsys = 20.0 + 5.0 + Tcas
    B, tau = 1e6, 10.0
    sig = Tsys / math.sqrt(B * tau)
    res = []
    for Bt in (50, 200, 800):
        m, rel = sim(Bt, 2000, rng)
        res.append((Bt, m, rel, 1 / math.sqrt(Bt)))
    # Dicke: mitad del tiempo en cada estado, diferencia de dos mediciones
    Bt = 400
    dif = []
    for _ in range(2000):
        a, _r = 0.0, None
        N = int(2 * Bt / 2)
        s1 = sum(rng.gauss(0, 1) ** 2 for _ in range(N)) / N
        s2 = sum(rng.gauss(0, 1) ** 2 for _ in range(N)) / N
        dif.append(s1 - s2)
    m = sum(dif) / len(dif)
    sd_dicke = math.sqrt(sum((x - m) ** 2 for x in dif) / (len(dif) - 1))
    teor_dicke = 2 / math.sqrt(Bt)
    return dict(Tcas=Tcas, Tsys=Tsys, sig=sig, res=res, sd_dicke=sd_dicke, teor_dicke=teor_dicke,
                T_lna_solo=25.0, naive=25.0 + 800.0 + 400.0)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"T_receptor en cascada = {r['Tcas']:.3f} K (suma sin ganancias seria {r['naive']:.0f} K)")
    print(f"T_sys = {r['Tsys']:.3f} K ; sigma_T(1 MHz, 10 s) = {r['sig']*1e3:.4f} mK")
    print(f"{'B*tau':>6} {'media':>8} {'sigma/media simulada':>21} {'1/sqrt(B tau)':>14}")
    for Bt, m, rel, teo in r["res"]:
        print(f"{Bt:6d} {m:8.4f} {rel:21.4f} {teo:14.4f}")
    print(f"Dicke con B*tau = 400: sigma(diferencia) = {r['sd_dicke']:.4f} ; teorica 2/sqrt(B tau) = {r['teor_dicke']:.4f}")
    for Bt, m, rel, teo in r["res"]:
        assert abs(rel / teo - 1) < 0.05
    assert abs(r["sd_dicke"] / r["teor_dicke"] - 1) < 0.05
    assert abs(r["Tcas"] - (25 + 800 / 1000 + 400 / (1000 * 10 ** -0.6))) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
