#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C24: metricas de desempeno de la optica adaptativa: cociente de Strehl (tres formas) y energia encerrada.

Datos: pupila circular de 32 pixeles en una malla de 128 x 128 (4 px por lambda/D) y aberraciones SINTETICAS: 11 modos de Zernike de ordenes 2 a 4 (sin inclinacion) con coeficientes gaussianos de desviacion
proporcional a n^(-11/6) y escalados a rms de 0,05, 0,1, 0,3, 0,6 y 1,0 rad ; semilla 20261109. Todo ILUSTRATIVO. Los polinomios de Zernike de Noll se escriben de memoria y se usan solo como base
de aberraciones sinteticas (no se afirma nada sobre su equivalencia con un instrumento real).
Modelo: PSF = |FFT(P exp(i phi))|^2 ; Strehl (a) = pico de la PSF aberrada / pico de la PSF ideal (mismo flujo total por Parseval), (b) = |<exp(i phi)>|^2 (identidad exacta para el pico en el origen),
(c) Marechal exp(-sigma^2), (d) 1 - sigma^2. Energia encerrada EE(r) = flujo dentro de un radio r centrado en el pico / flujo total ; para la pupila ideal se contrasta con 1 - J0(x)^2 - J1(x)^2, x = pi r (r en lambda/D)
(J0 y J1 por la integral de Bessel).
Supuestos: monocromatico, pupila sin obstruccion, malla periodica (la energia fuera de 16 lambda/D se pliega). Validez: Marechal es una aproximacion para sigma <~ 0,5 rad ; la energia encerrada medida en una malla finita sobreestima levemente las alas.
Tolerancia: (a) frente a (b) a 2e-2 en el pico en el origen (la PSF discreta del pico exacto coincide cuando el maximo esta en el pixel central) ; EE ideal frente a la cerrada a 1,5e-2 (el conteo de pixeles en un disco de 2 a 12 pixeles es discreto) ; Marechal a 3e-2 hasta 1,0 rad para esta aberracion sintetica de muchos modos (una aberracion de un solo modo puede apartarse mas).
"""
from __future__ import annotations
import cmath, math, platform, random

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

def bessel(n, x, m=400):
    h = math.pi / m
    s = 0.0
    for i in range(m + 1):
        t = i * h
        s += math.cos(n * t - x * math.sin(t)) * (1 if i in (0, m) else (4 if i % 2 else 2))
    return s * h / 3 / math.pi

def zern_rad(n, m, r):
    s = 0.0
    for k in range((n - m) // 2 + 1):
        s += (-1) ** k * math.factorial(n - k) / (math.factorial(k) * math.factorial((n + m) // 2 - k) * math.factorial((n - m) // 2 - k)) * r ** (n - 2 * k)
    return s

MODOS = [(2, 0, 'c'), (2, 2, 'c'), (2, 2, 's'), (3, 1, 'c'), (3, 1, 's'), (3, 3, 'c'), (3, 3, 's'), (4, 0, 'c'), (4, 2, 'c'), (4, 2, 's'), (4, 4, 'c')]

def zern(n, m, tipo, r, t):
    norm = math.sqrt(n + 1) if m == 0 else math.sqrt(2 * (n + 1))
    ang = 1.0 if m == 0 else (math.cos(m * t) if tipo == 'c' else math.sin(m * t))
    return norm * zern_rad(n, m, r) * ang

def psf(pts, fase):
    campo = [[0j] * N for _ in range(N)]
    for (i, j), ph in zip(pts, fase):
        campo[i][j] = cmath.exp(1j * ph)
    f = fft2(campo)
    return [[abs(f[i][j]) ** 2 for j in range(N)] for i in range(N)]

def ee_curva(p, ci, cj, radios):
    tot = sum(sum(r) for r in p)
    out = []
    for R in radios:
        s = 0.0
        for i in range(N):
            di = min((i - ci) % N, (ci - i) % N)
            for j in range(N):
                dj = min((j - cj) % N, (cj - j) % N)
                if math.hypot(di, dj) <= R:
                    s += p[i][j]
        out.append(s / tot)
    return out

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    c0 = N // 2
    pts = [(i, j) for i in range(N) for j in range(N) if math.hypot(i - c0 + 0.5, j - c0 + 0.5) <= DP / 2]
    npts = len(pts)
    base = [[zern(n, m, t, math.hypot(i - c0 + 0.5, j - c0 + 0.5) / (DP / 2), math.atan2(i - c0 + 0.5, j - c0 + 0.5)) for (n, m, t) in MODOS] for (i, j) in pts]
    coef = [rnd.gauss(0, 1) * n ** (-11 / 6) for (n, _, _) in MODOS]
    fase0 = [sum(c * b for c, b in zip(coef, row)) for row in base]
    mu = sum(fase0) / npts
    s0 = math.sqrt(sum((v - mu) ** 2 for v in fase0) / npts)
    fase0 = [(v - mu) / s0 for v in fase0]       # rms unitario sin piston
    ideal = psf(pts, [0.0] * npts)
    pico_i = ideal[0][0]
    print(f"{'sigma [rad]':>11} {'pico/ideal (a)':>15} {'|<e^i phi>|^2 (b)':>18} {'Marechal (c)':>13} {'1 - sigma^2 (d)':>16} {'|a-b|':>9}")
    res = {}
    for sg in (0.05, 0.1, 0.3, 0.6, 1.0):
        fase = [sg * v for v in fase0]
        p = psf(pts, fase)
        a = max(max(r) for r in p) / pico_i
        a0 = p[0][0] / pico_i
        b = abs(sum(cmath.exp(1j * v) for v in fase) / npts) ** 2
        c = math.exp(-sg * sg)
        d = 1 - sg * sg
        res[sg] = (a, a0, b, c, d, p)
        print(f"{sg:11.2f} {a:15.5f} {b:18.5f} {c:13.5f} {d:16.5f} {abs(a0 - b):9.1e}")
        assert abs(a0 - b) < 1e-9          # el pixel central cumple la identidad exacta
        assert a >= a0 - 1e-12             # el maximo de la PSF nunca es menor que el pixel central
    for sg in (0.05, 0.1, 0.3, 0.6, 1.0):
        assert abs(res[sg][2] - res[sg][3]) < 3e-2, sg
    assert abs(res[1.0][2] - res[1.0][4]) > 0.3        # la expansion de primer orden 1 - sigma^2 ya no vale a 1 rad
    print(f"a 1,0 rad: Marechal - exacta = {res[1.0][3] - res[1.0][2]:+.4f} (con esta aberracion de muchos modos casi gaussiana sigue siendo buena) ; 1 - sigma^2 = {res[1.0][4]:.2f} frente a {res[1.0][2]:.3f} exacta: la expansion de primer orden falla")
    # energia encerrada de la PSF ideal frente a la cerrada
    rad_ld = (0.5, 1.0, 1.22, 2.0, 3.0)
    rad_px = [r * N / DP for r in rad_ld]
    ee_i = ee_curva(ideal, 0, 0, rad_px)
    print(f"{'r [lambda/D]':>12} {'EE malla':>10} {'EE cerrada 1-J0^2-J1^2':>24} {'dif':>9}")
    for r, e in zip(rad_ld, ee_i):
        x = math.pi * r
        teo = 1 - bessel(0, x) ** 2 - bessel(1, x) ** 2
        print(f"{r:12.2f} {e:10.5f} {teo:24.5f} {e - teo:+9.5f}")
        assert abs(e - teo) < 1.5e-2, (r, e, teo)      # a radios de pocos pixeles el conteo de pixeles en un disco es discreto
    # EE de las PSF aberradas en 1 lambda/D y radio de EE 50 %
    print(f"{'sigma [rad]':>11} {'EE(1 lambda/D)':>15} {'EE(2 lambda/D)':>15} {'EE(3 lambda/D)':>15} {'Strehl (a)':>11}")
    for sg in (0.05, 0.3, 0.6, 1.0):
        p = res[sg][5]
        # centro: el maximo de la PSF
        ci, cj = max(((i, j) for i in range(N) for j in range(N)), key=lambda t: p[t[0]][t[1]])
        e = ee_curva(p, ci, cj, [N / DP * 1.0, N / DP * 2.0, N / DP * 3.0])
        print(f"{sg:11.2f} {e[0]:15.4f} {e[1]:15.4f} {e[2]:15.4f} {res[sg][0]:11.4f}")
    e_prev = None
    for sg in (0.05, 0.3, 0.6, 1.0):
        p = res[sg][5]
        ci, cj = max(((i, j) for i in range(N) for j in range(N)), key=lambda t: p[t[0]][t[1]])
        e = ee_curva(p, ci, cj, [N / DP * 1.0])[0]
        if e_prev is not None:
            assert e < e_prev + 1e-9
        e_prev = e
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
