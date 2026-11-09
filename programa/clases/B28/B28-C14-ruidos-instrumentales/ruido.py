#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C14: ruido coloreado, espectro de potencia, blanqueo y relacion senal-ruido de un filtro acoplado.

Datos: ninguna constante fisica. Contexto: Advanced LIGO usa brazos de 4 km con cavidades y reciclaje (arXiv:1411.4547, resumen,
consultado 2026-11-09). La forma del espectro del ruido, la tasa de muestreo, la duracion y la amplitud de la senal son SINTETICOS
(generados aqui con semilla fija); no representan ningun detector.
Modelo: ruido gaussiano estacionario con densidad espectral S(f) = S0 (1 + (f0/f)^4) generado por sintesis de Fourier
(FFT de Cooley-Tukey implementada aqui); estimacion de S(f) por periodograma promediado (Welch sin solapamiento, ventana de Hann);
blanqueo d_w = IFFT(FFT(d)/sqrt(S)); relacion senal-ruido optima rho^2 = 4 Re Int |h(f)|^2/S(f) df, comprobada contra la correlacion
temporal con la plantilla blanqueada.
Supuestos: ruido gaussiano estacionario. Validez: ilustrativa.
Tolerancia: periodograma dentro del 25 % de la densidad teorica a 16, 64 y 128 Hz (la fuga de la ventana sesga las frecuencias extremas); media del filtro dentro de 3 errores + 0.2.
"""
from __future__ import annotations
import cmath
import math
import platform
import random
import statistics
import sys


def fft(a, inv=False):
    n = len(a)
    if n == 1:
        return a[:]
    par, impar = fft(a[0::2], inv), fft(a[1::2], inv)
    s = 1 if inv else -1
    out = [0j] * n
    for k in range(n // 2):
        w = cmath.exp(s * 2j * math.pi * k / n) * impar[k]
        out[k] = par[k] + w
        out[k + n // 2] = par[k] - w
    return out


def ifft(a):
    n = len(a)
    return [x / n for x in fft(a, inv=True)]


def densidad(f, s0=1.0, f0=20.0):
    return s0 * (1 + (f0 / f) ** 4)


def ruido(n, fs, rng):
    """Ruido real con densidad unilateral S(f): coeficientes de Fourier gaussianos de varianza S N fs/4 ... (convencion numpy: var(x) = Int S df)."""
    df = fs / n
    c = [0j] * n
    for k in range(1, n // 2):
        f = k * df
        sig = math.sqrt(densidad(f) * n * fs / 4)
        c[k] = complex(rng.gauss(0, sig), rng.gauss(0, sig))
        c[n - k] = c[k].conjugate()
    c[n // 2] = complex(rng.gauss(0, math.sqrt(densidad(n // 2 * df) * n * fs / 2)), 0)
    x = ifft(c)
    return [v.real for v in x]


def periodograma(x, fs, nseg):
    n = len(x) // nseg
    w = [0.5 - 0.5 * math.cos(2 * math.pi * i / n) for i in range(n)]
    u = sum(v * v for v in w) / n
    acum = [0.0] * (n // 2 + 1)
    for s in range(nseg):
        seg = [x[s * n + i] * w[i] for i in range(n)]
        z = fft([complex(v) for v in seg])
        for k in range(n // 2 + 1):
            acum[k] += 2 * abs(z[k]) ** 2 / (fs * n * u)
    return [a / nseg for a in acum], fs / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    # prueba de la FFT frente a la definicion
    x = [math.sin(0.3 * i) + 0.1 * i for i in range(16)]
    z = fft([complex(v) for v in x])
    for k in (0, 3, 7):
        d = sum(x[j] * cmath.exp(-2j * math.pi * j * k / 16) for j in range(16))
        assert abs(z[k] - d) < 1e-9, "FFT frente a la definicion"
    back = ifft(z)
    assert max(abs(back[i] - x[i]) for i in range(16)) < 1e-12, "FFT inversa"
    print("FFT de Cooley-Tukey: coincide con la definicion (1e-9) y se invierte (1e-12)")
    rng = random.Random(20261109)
    fs, n = 1024.0, 2 ** 14
    d = ruido(n, fs, rng)
    var = statistics.pvariance(d)
    print(f"ruido sintetico: N = {n}, fs = {fs} Hz, duracion = {n / fs:.1f} s ; varianza = {var:.4g}")
    p, df = periodograma(d, fs, 8)
    print(f"{'f [Hz]':>8} {'S estimada':>12} {'S teorica':>12} {'cociente':>9}")
    for f in (8.0, 16.0, 32.0, 64.0, 128.0, 256.0):
        k = round(f / df)
        est = sum(p[k - 1:k + 2]) / 3
        print(f"{k * df:8.1f} {est:12.4f} {densidad(k * df):12.4f} {est / densidad(k * df):9.3f}")
    # pendiente a baja frecuencia (f << f0): S ~ f^-4
    k1, k2 = round(5.0 / df), round(10.0 / df)
    pend = math.log(sum(p[k1 - 1:k1 + 2]) / sum(p[k2 - 1:k2 + 2])) / math.log(k2 / k1)
    teor = math.log(densidad(5.0) / densidad(10.0)) / math.log(2)
    print(f"pendiente de S entre 5 y 10 Hz = {-pend:.3f} (teorica con f0 = 20 Hz: {-teor:.3f}) ; la diferencia puede deberse a fuga espectral de la ventana de Hann (no se aisla aqui)")
    for f in (16.0, 64.0, 128.0):
        k = round(f / df)
        r = sum(p[k - 1:k + 2]) / 3 / densidad(k * df)
        assert abs(r - 1) < 0.25, f"periodograma a {f} Hz"
    # senal y filtro acoplado
    m = 2048
    t = [i / fs for i in range(m)]
    h = [math.sin(2 * math.pi * (60 + 40 * ti) * ti) * math.exp(-((ti - 1.0) / 0.4) ** 2) for ti in t]
    amp = 10.0
    # rho^2 teorico a partir de la densidad espectral
    hf = fft([complex(v) for v in h] + [0j] * (n - m))
    rho2 = 0.0
    for k in range(1, n // 2):
        f = k * df if False else k * fs / n
        rho2 += 4 * abs(hf[k]) ** 2 / (fs ** 2) / densidad(f) * (fs / n)
    rho = amp * math.sqrt(rho2)
    print(f"relacion senal-ruido optima (teorica) para amplitud {amp}: rho = {rho:.3f}")
    # filtro acoplado sobre muchas realizaciones: salida = <d, h>_S / sqrt(<h,h>_S) en el dominio de la frecuencia
    salidas = []
    for _ in range(100):
        r = ruido(n, fs, rng)
        d_ = [r[i] + (amp * h[i] if i < m else 0.0) for i in range(n)]
        df_ = fft([complex(v) for v in d_])
        num = 0.0
        for k in range(1, n // 2):
            f = k * fs / n
            num += 4 * (df_[k] * hf[k].conjugate()).real / (fs ** 2) / densidad(f) * (fs / n)
        salidas.append(num / math.sqrt(rho2))
    media, desv = statistics.mean(salidas), statistics.pstdev(salidas)
    print(f"filtro acoplado, 100 realizaciones con la senal inyectada: media = {media:.3f} (esperada {rho:.3f}) ; desviacion = {desv:.3f} (esperada 1)")
    assert abs(media - rho) < 3 * 1.0 / math.sqrt(100) + 0.2 and abs(desv - 1) < 0.2, "filtro acoplado"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
