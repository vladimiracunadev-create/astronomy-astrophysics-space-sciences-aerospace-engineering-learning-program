#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C04: difraccion de Fraunhofer de rendijas, doble rendija y red, por transformada de Fourier frente a formulas analiticas.

Datos: ninguna constante fisica. Rendija a = 50 um, separacion de la doble rendija d = 200 um, red de 5 rendijas y lambda = 500 nm son ILUSTRATIVOS.
Modelo: el campo lejano es la transformada de Fourier de la transmitancia de la apertura (FFT radix 2, N = 8192, muestreo 1 um); se contrasta con
I(u) = sinc^2(a u) para una rendija, con el factor cos^2(pi d u) para dos y con [sin(N pi d u)/(N sin(pi d u))]^2 para una red, con u = sin(theta)/lambda.
Supuestos: apertura delgada y unidimensional, iluminacion coherente, paraxial. Validez: ilustrativa de la teoria escalar.
Tolerancia: diferencias de intensidad normalizada menores que 2e-3 en los puntos comparados; ceros en u = n/a.
"""
from __future__ import annotations
import cmath, math, platform

N = 8192
DX = 1e-6
LAM = 500e-9

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

def rect(x0, ancho):
    g = [0.0] * N
    i0 = int(round((x0 - ancho / 2) / DX)) + N // 2
    for i in range(i0, i0 + int(round(ancho / DX))):
        g[i % N] = 1.0
    return g

def suma(*gs):
    return [min(1.0, sum(v)) for v in zip(*gs)]

def patron(g):
    # centrar el origen de la apertura en el indice 0 antes de la FFT es innecesario para la intensidad
    f = fft([complex(v) for v in g])
    inten = [abs(v) ** 2 for v in f]
    return inten

def sinc2(x):
    return 1.0 if x == 0 else (math.sin(math.pi * x) / (math.pi * x)) ** 2

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    a, d = 50e-6, 200e-6
    du = 1.0 / (N * DX)       # paso en frecuencia espacial u = sin(theta)/lambda
    print(f"paso en u = {du:.2f} 1/m ; paso angular = {du * LAM * 1e6:.1f} urad ; primer cero de la rendija en u = 1/a = {1 / a:.0f} 1/m (theta = {LAM / a * 1e3:.2f} mrad)")
    # 1 rendija
    p1 = patron(rect(0.0, a))
    p1n = [v / p1[0] for v in p1]
    print(f"{'u a':>6} {'I FFT':>10} {'sinc2':>10}")
    peor = 0.0
    for ua in (0.25, 0.5, 1.0, 1.5, 2.0, 2.5):
        k = int(round(ua / a / du))
        u = k * du
        teo = sinc2(a * u)
        peor = max(peor, abs(p1n[k] - teo))
        print(f"{a * u:6.2f} {p1n[k]:10.5f} {teo:10.5f}")
    assert peor < 2e-3
    # cero exacto
    k1 = int(round(1 / a / du))
    print(f"intensidad en el primer cero (k = {k1}): {p1n[k1]:.2e}")
    assert p1n[k1] < 1e-6
    # 2 rendijas
    p2 = patron(suma(rect(-d / 2, a), rect(d / 2, a)))
    p2n = [v / p2[0] for v in p2]
    peor2 = 0.0
    for k in range(1, 800, 37):
        u = k * du
        teo = sinc2(a * u) * math.cos(math.pi * d * u) ** 2
        peor2 = max(peor2, abs(p2n[k] - teo))
    print(f"doble rendija: maximo |I FFT - sinc2 * cos2| sobre 22 puntos = {peor2:.2e} ; franjas separadas por u = 1/d = {1 / d:.0f} 1/m")
    assert peor2 < 2e-3
    # red de 5 rendijas: maximos secundarios N-2 = 3 entre principales
    nr = 5
    gs = [rect((j - (nr - 1) / 2) * d, a) for j in range(nr)]
    p5 = patron(suma(*gs))
    p5n = [v / p5[0] for v in p5]
    u_pp = int(round(1 / d / du))
    pico_sec = max(p5n[k] for k in range(int(0.1 * u_pp), int(0.9 * u_pp)) if p5n[k] > p5n[k - 1] and p5n[k] > p5n[k + 1])
    num_sec = sum(1 for k in range(2, u_pp - 2) if p5n[k] > p5n[k - 1] and p5n[k] > p5n[k + 1] and p5n[k] > 0.003)
    teo_sec = (math.sin(nr * math.pi * (1.5 / nr + 0.5 / nr * 0) * 1) / (nr * math.sin(math.pi * 1.5 / nr))) ** 2
    print(f"red de {nr} rendijas: maxima secundario entre principales = {pico_sec:.4f} ; cantidad de secundarios = {num_sec} (esperados N-2 = {nr - 2}) ; cota 1/(N sin(1.5 pi/N))^2 = {teo_sec:.4f}")
    assert num_sec == nr - 2
    peor3 = max(abs(p5n[k] - (sinc2(a * k * du) * (math.sin(nr * math.pi * d * k * du) / (nr * math.sin(math.pi * d * k * du))) ** 2)) for k in range(3, 700, 29) if abs(math.sin(math.pi * d * k * du)) > 1e-3)
    print(f"red: maximo |I FFT - formula| = {peor3:.2e}")
    assert peor3 < 3e-3
    # energia: Parseval
    e_ap = sum(v * v for v in rect(0.0, a))
    e_f = sum(p1) / N
    print(f"Parseval: sum|g|^2 = {e_ap:.1f} ; sum|G|^2 / N = {e_f:.1f}")
    assert abs(e_ap - e_f) / e_ap < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
