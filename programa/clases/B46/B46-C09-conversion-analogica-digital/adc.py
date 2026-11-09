#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C09: cuantizacion, SNR de un convertidor y correccion de Van Vleck (semilla fija).

Datos: ninguno externo. Los bits (2 a 10), la amplitud de plena escala y el coeficiente de correlacion son SINTETICOS (semilla 20261109).
Modelo: (a) SNR de un tono a plena escala cuantizado a N bits frente a 6,02 N + 1,76 dB; (b) correlacion de dos senales gaussianas con
coeficiente rho digitalizadas a 1 bit: r1 = (2/pi) arcsin(rho), de donde rho = sin(pi r1/2) (relacion de Van Vleck); eficiencia 2/pi en S/N.
Supuestos: senales gaussianas estacionarias, umbral en cero. Validez: orientativa.
Tolerancia: SNR dentro de 0,6 dB de la formula; rho recuperado dentro de 0,01.
"""
from __future__ import annotations
import math, platform, random

def snr_tono(bits):
    n = 20000
    L = 2 ** (bits - 1)
    ps = pe = 0.0
    for k in range(n):
        x = 0.999 * math.sin(2 * math.pi * 0.1234567 * k + 0.3)
        q = (math.floor(x * L) + 0.5) / L
        ps += x * x
        pe += (q - x) ** 2
    return 10 * math.log10(ps / pe)

def calc():
    rng = random.Random(20261109)
    snr = [(b, snr_tono(b), 6.02 * b + 1.76) for b in (2, 4, 6, 8, 10)]
    N = 200000
    filas = []
    for rho in (0.1, 0.5, 0.9):
        s = 0
        sx = sy = 0.0
        for _ in range(N):
            a, b = rng.gauss(0, 1), rng.gauss(0, 1)
            x, y = a, rho * a + math.sqrt(1 - rho * rho) * b
            sx += x * y
            s += (1 if x > 0 else -1) * (1 if y > 0 else -1)
        r1 = s / N
        filas.append((rho, sx / N, r1, math.sin(math.pi * r1 / 2), 2 / math.pi * math.asin(rho)))
    # eficiencia en S/N: desviacion de r1 frente a la de analogico para rho ~ 0 (N pequeno)
    reps, M = 600, 200
    va = vd = 0.0
    ra, rd = [], []
    for _ in range(reps):
        sa = sd = 0.0
        for _ in range(M):
            x, y = rng.gauss(0, 1), rng.gauss(0, 1)
            sa += x * y
            sd += (1 if x > 0 else -1) * (1 if y > 0 else -1)
        ra.append(sa / M)
        rd.append(sd / M)
    sa_ = math.sqrt(sum(v * v for v in ra) / reps)
    sd_ = math.sqrt(sum(v * v for v in rd) / reps)
    # sigma de rho estimado: analogico sa_, 1 bit sd_/(2/pi) (pendiente de r1 respecto de rho en cero)
    return dict(snr=snr, filas=filas, sa=sa_, sd=sd_, ef=sa_ / (sd_ / (2 / math.pi)), ef_teo=2 / math.pi)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'bits':>5} {'SNR simulada [dB]':>18} {'6.02N+1.76 [dB]':>16}")
    for b, s, t in r["snr"]:
        print(f"{b:5d} {s:18.2f} {t:16.2f}")
    print(f"{'rho':>5} {'analogica':>10} {'1 bit r1':>9} {'rho (Van Vleck)':>16} {'(2/pi)asin(rho)':>16}")
    for rho, an, r1, rv, teo in r["filas"]:
        print(f"{rho:5.2f} {an:10.4f} {r1:9.4f} {rv:16.4f} {teo:16.4f}")
    print(f"sigma de r (200 muestras): analogico {r['sa']:.4f} ; 1 bit {r['sd']:.4f}")
    print(f"eficiencia en S/N del 1 bit con rho = 0: {r['ef']:.3f} (2/pi = {r['ef_teo']:.3f})")
    for b, s, t in r["snr"]:
        assert abs(s - t) < 1.0
    for rho, an, r1, rv, teo in r["filas"]:
        assert abs(rv - rho) < 0.01 and abs(r1 - teo) < 0.01
    assert abs(r["ef"] - r["ef_teo"]) < 0.05
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
