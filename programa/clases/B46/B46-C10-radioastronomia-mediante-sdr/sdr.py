#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C10: espectrometro de un SDR simulado: FFT, promediado y ancho de banda equivalente de ruido.

Datos: ninguno externo. La tasa de muestreo (2,4 MHz), el tamano de la FFT (1024), el tono (+120 kHz) y su amplitud son SINTETICOS (semilla 20261109).
Modelo: muestras I/Q complejas = ruido gaussiano complejo + tono; FFT radix 2 con ventana de Hann; espectro de potencia promediado sobre M espectros:
la desviacion relativa por canal cae como 1/sqrt(M). Ancho de banda equivalente de ruido de la ventana (ENBW) = N suma w^2/(suma w)^2 bines (Hann: 1,5).
Supuestos: ruido blanco, sin desbalance IQ ni espurios. Validez: orientativa.
Tolerancia: ENBW 1,5 dentro de 0,001; caida 1/sqrt(M) dentro del 10 %.
"""
from __future__ import annotations
import cmath, math, platform, random

def fft(x):
    n = len(x)
    if n == 1:
        return x
    p, q = fft(x[0::2]), fft(x[1::2])
    out = [0j] * n
    for k in range(n // 2):
        t = cmath.exp(-2j * math.pi * k / n) * q[k]
        out[k], out[k + n // 2] = p[k] + t, p[k] - t
    return out

def calc():
    rng = random.Random(20261109)
    N, fs = 1024, 2.4e6
    w = [0.5 - 0.5 * math.cos(2 * math.pi * i / N) for i in range(N)]
    enbw = N * sum(v * v for v in w) / sum(w) ** 2
    ftono, amp = 120e3, 0.5
    bin_t = round(ftono / fs * N)
    Ms = (1, 4, 16, 64)
    res = []
    espectros = []
    for s in range(64):
        x = [complex(rng.gauss(0, 1), rng.gauss(0, 1)) / math.sqrt(2) + amp * cmath.exp(2j * math.pi * ftono / fs * (s * N + i)) for i in range(N)]
        X = fft([a * b for a, b in zip(x, w)])
        espectros.append([abs(v) ** 2 for v in X])
    for M in Ms:
        prom = [sum(espectros[s][k] for s in range(M)) / M for k in range(N)]
        ruido = [prom[k] for k in range(N) if abs(k - bin_t) > 8 and abs(k - bin_t - N) > 8]
        m = sum(ruido) / len(ruido)
        sd = math.sqrt(sum((v - m) ** 2 for v in ruido) / (len(ruido) - 1))
        res.append((M, m, sd / m, 1 / math.sqrt(M), prom[bin_t] / m))
    return dict(res=res, enbw=enbw, df=fs / N, bin_t=bin_t, pico_teo=(amp * sum(w)) ** 2 / (sum(v * v for v in w)))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"resolucion = {r['df']:.2f} Hz por canal ; ENBW de Hann = {r['enbw']:.4f} bines ; canal del tono = {r['bin_t']}")
    print(f"{'M':>4} {'media ruido':>12} {'sigma/media':>12} {'1/sqrt(M)':>10} {'pico/ruido':>11}")
    for M, m, rel, teo, snr in r["res"]:
        print(f"{M:4d} {m:12.3f} {rel:12.4f} {teo:10.4f} {snr:11.1f}")
    assert abs(r["enbw"] - 1.5) < 1e-3
    for M, m, rel, teo, snr in r["res"]:
        assert abs(rel / teo - 1) < 0.1
    assert r["res"][-1][4] > 100
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
