#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C07: funcion de transferencia optica (OTF/MTF) como transformada de la PSF y como autocorrelacion de la pupila.

Datos: ninguna constante fisica. Pupila circular de 32 pixeles en malla de 128 x 128 y 0,10 rad rms de defocus son ILUSTRATIVOS.
Modelo: OTF = F{PSF} / F{PSF}(0). Vias independientes: (a) FFT de la PSF; (b) autocorrelacion directa de la pupila; (c) formula analitica de la MTF de una
pupila circular ideal MTF(v) = (2/pi)[acos(v) - v sqrt(1-v^2)], con v = f / fc y fc = D / lambda (en pixeles de pupila, el retraso maximo es 32).
Ademas se submuestrea la PSF cada 4 pixeles (1 lambda/D por pixel, bajo el criterio de Nyquist) y se predice el solapamiento: OTF_sub(v) = MTF(v) + MTF(1 - v).
Supuestos: iluminacion incoherente, sistema invariante por desplazamiento. Validez: ideal; la MTF de un detector real incluye ademas el pixel y el ruido.
Tolerancia: FFT frente a autocorrelacion a 1e-9 ; frente a la formula analitica a 0,02 (discretizacion de la pupila) ; solapamiento a 0,02.
"""
from __future__ import annotations
import cmath, math, platform

N = 128
DP = 32

def fft(a):
    n = len(a)
    a = list(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    m = 2
    while m <= n:
        w = cmath.exp(-2j * math.pi / m)
        for s in range(0, n, m):
            t = 1 + 0j
            for k in range(m // 2):
                u, v = a[s + k], a[s + k + m // 2] * t
                a[s + k], a[s + k + m // 2] = u + v, u - v
                t *= w
        m <<= 1
    return a

def fft2(g):
    f = [fft(r) for r in g]
    cols = [fft([f[i][j] for i in range(len(f))]) for j in range(len(f[0]))]
    return [[cols[j][i] for j in range(len(f[0]))] for i in range(len(f))]

def mtf_teo(v):
    if v >= 1:
        return 0.0
    return 2 / math.pi * (math.acos(v) - v * math.sqrt(1 - v * v))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    c = N // 2
    P = [[1.0 if math.hypot(i - c + 0.5, j - c + 0.5) <= DP / 2 else 0.0 for j in range(N)] for i in range(N)]
    npix = sum(sum(r) for r in P)
    campo = [[complex(P[i][j]) for j in range(N)] for i in range(N)]
    F = fft2(campo)
    psf = [[abs(F[i][j]) ** 2 for j in range(N)] for i in range(N)]
    O = fft2([[complex(v) for v in r] for r in psf])
    o0 = O[0][0].real
    print(f"OTF(0) = {o0:.1f} = N^2 * npix = {N * N * npix:.1f}")
    assert abs(o0 - N * N * npix) < 1e-6 * o0
    print(f"{'lag [px]':>9} {'v=lag/32':>9} {'OTF FFT':>9} {'autocorr':>9} {'analitica':>9}")
    peor_a = peor_t = 0.0
    for lag in (0, 4, 8, 12, 16, 20, 24, 28, 32, 36):
        otf = O[0][lag].real / o0
        # autocorrelacion directa a lo largo del eje j (periodica)
        ac = sum(P[i][j] * P[i][(j + lag) % N] for i in range(N) for j in range(N)) / npix
        v = lag / DP
        teo = mtf_teo(v)
        peor_a = max(peor_a, abs(otf - ac))
        peor_t = max(peor_t, abs(otf - teo))
        print(f"{lag:9d} {v:9.3f} {otf:9.5f} {ac:9.5f} {teo:9.5f}")
    assert peor_a < 1e-9, peor_a
    assert peor_t < 0.02, peor_t
    imag = max(abs(O[0][l].imag) / o0 for l in range(N))
    print(f"parte imaginaria maxima de la OTF (PSF simetrica): {imag:.2e}")
    assert imag < 1e-9
    # solapamiento por submuestreo (cada 4 pixeles = 1 lambda/D)
    sub = [[complex(psf[(4 * i) % N][(4 * j) % N]) for j in range(32)] for i in range(32)]
    Os = fft2(sub)
    os0 = Os[0][0].real
    print(f"{'v':>6} {'OTF submuestreada':>18} {'MTF(v)+MTF(1-v)':>16} {'MTF(v)':>8}")
    peor_s = 0.0
    for m in (2, 4, 8, 12, 16):
        # el indice m de la malla de 32 puntos es el retraso m de la pupila; el submuestreo suma O(m) y O(m - 32)
        v = m / DP
        medido = Os[0][m].real / os0
        pred = mtf_teo(v) + mtf_teo(1 - v)
        peor_s = max(peor_s, abs(medido - pred))
        print(f"{v:6.3f} {medido:18.5f} {pred:16.5f} {mtf_teo(v):8.5f}")
    assert peor_s < 0.03, peor_s
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
