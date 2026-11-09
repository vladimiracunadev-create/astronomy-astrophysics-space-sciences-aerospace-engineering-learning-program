#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C06: funcion de dispersion puntual (PSF) como |FFT de la pupila|^2, con y sin aberracion.

Datos: ninguna constante fisica. Pupila circular de 32 pixeles de diametro en una malla de 128 x 128 (4 pixeles por lambda/D), 0,10 rad rms de defocus
y la inclinacion de 5 pixeles son ILUSTRATIVOS.
Modelo: PSF(u) = |F{P(x) exp(i phi(x))}|^2 con FFT 2D radix 2, normalizada al pico sin aberracion. Vias independientes: (a) el perfil radial se compara con el patron de Airy
[2 J1(x)/x]^2 con x = pi r / 4 (r en pixeles) ; (b) el cociente de Strehl del pico se compara con la identidad exacta |<exp(i phi)>|^2 sobre la pupila y con la
aproximacion de Marechal exp(-sigma^2) ; (c) un termino lineal en la fase desplaza el pico (teorema del desplazamiento).
Supuestos: pupila uniforme, monocromatica, campo lejano. Validez: muestreo de la pupila en pixeles introduce un error de unos pocos 1e-2 respecto del disco ideal.
Tolerancia: perfil de Airy a 0,02 del pico ; Strehl por pico frente a identidad exacta a 1e-9 ; Parseval a 1e-9.
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

def bessel1(x, m=200):
    h = math.pi / m
    s = 0.0
    for i in range(m + 1):
        t = i * h
        s += math.cos(t - x * math.sin(t)) * (1 if i in (0, m) else (4 if i % 2 else 2))
    return s * h / 3 / math.pi

def airy(x):
    return 1.0 if x == 0 else (2 * bessel1(x) / x) ** 2

def pupila():
    c = N // 2
    pts = []
    for i in range(N):
        fila = []
        for j in range(N):
            r = math.hypot(i - c + 0.5, j - c + 0.5)
            fila.append(1.0 if r <= DP / 2 else 0.0)
        pts.append(fila)
    return pts

def psf(P, phi):
    campo = [[(P[i][j] * cmath.exp(1j * phi[i][j]) if P[i][j] else 0j) for j in range(N)] for i in range(N)]
    f = fft2(campo)
    return [[abs(f[i][j]) ** 2 for j in range(N)] for i in range(N)]

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    P = pupila()
    npix = sum(sum(r) for r in P)
    cero = [[0.0] * N for _ in range(N)]
    p0 = psf(P, cero)
    pico0 = p0[0][0]
    print(f"pixeles de pupila = {npix:.0f} (disco ideal {math.pi * (DP / 2) ** 2:.1f}) ; pico sin aberracion = {pico0:.1f} (= npix^2 = {npix ** 2:.1f})")
    assert abs(pico0 - npix ** 2) < 1e-6 * npix ** 2
    # Parseval
    tot = sum(sum(r) for r in p0)
    print(f"Parseval: sum PSF / N^2 = {tot / N ** 2:.3f} ; sum |P|^2 = {npix:.1f}")
    assert abs(tot / N ** 2 - npix) < 1e-9 * npix
    # perfil de Airy a lo largo del eje (el origen esta en el pixel [0][0])
    print(f"{'r [px]':>7} {'r [lambda/D]':>13} {'PSF/pico':>10} {'Airy':>10}")
    peor = 0.0
    for r in (1, 2, 3, 4, 5, 6, 8, 10, 12):
        v = p0[0][r] / pico0
        x = math.pi * r / (N / DP)
        teo = airy(x)
        peor = max(peor, abs(v - teo))
        print(f"{r:7d} {r / (N / DP):13.2f} {v:10.5f} {teo:10.5f}")
    assert peor < 0.02
    # aberracion de defocus: phi = a * (2 rho^2 - 1) con rms = a / sqrt(3)
    c = N // 2
    a = 0.10 * math.sqrt(3)
    phi = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if P[i][j]:
                rho = math.hypot(i - c + 0.5, j - c + 0.5) / (DP / 2)
                phi[i][j] = a * (2 * rho * rho - 1)
    m = sum(phi[i][j] for i in range(N) for j in range(N) if P[i][j]) / npix
    var = sum((phi[i][j] - m) ** 2 for i in range(N) for j in range(N) if P[i][j]) / npix
    p1 = psf(P, phi)
    s_pico = p1[0][0] / pico0
    s_exacta = abs(sum(cmath.exp(1j * phi[i][j]) for i in range(N) for j in range(N) if P[i][j]) / npix) ** 2
    s_mar = math.exp(-var)
    print(f"sigma_fase (rms) = {math.sqrt(var):.4f} rad ; Strehl por pico = {s_pico:.6f} ; |<exp(i phi)>|^2 = {s_exacta:.6f} ; Marechal exp(-sigma^2) = {s_mar:.6f}")
    assert abs(s_pico - s_exacta) < 1e-9
    assert abs(s_pico - s_mar) < 5e-3
    # desplazamiento por un termino lineal
    sh = 5
    phi_t = [[(2 * math.pi * sh * j / N if P[i][j] else 0.0) for j in range(N)] for i in range(N)]
    p2 = psf(P, phi_t)
    mejor = max(range(N), key=lambda j: p2[0][j])
    print(f"inclinacion de {sh} ciclos por pupila: el pico pasa de la columna 0 a la columna {mejor} (esperado {sh}) ; pico = {p2[0][mejor] / pico0:.6f}")
    assert mejor == sh and abs(p2[0][mejor] / pico0 - 1) < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
