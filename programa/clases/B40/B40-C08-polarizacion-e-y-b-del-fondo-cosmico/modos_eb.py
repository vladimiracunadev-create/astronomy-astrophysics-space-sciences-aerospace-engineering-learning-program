#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C08: descomposicion E/B de un mapa de polarizacion en la aproximacion de cielo plano y fuga E -> B por una mascara.

Datos: ninguna constante fisica. Los mapas son campos gaussianos SINTETICOS (semilla 20261109) en una malla de 32 x 32 con condiciones periodicas; el filtro gaussiano y la mascara son ILUSTRATIVOS.
La descomposicion E/B en esferas y su paridad estan descritas en Zaldarriaga y Seljak (arXiv:astro-ph/9609170, solo resumen, consultado el 2026-11-09); aqui solo se usa la version plana.
Modelo: en Fourier, Q(l) = -(E cos 2phi - B sin 2phi), U(l) = -(E sin 2phi + B cos 2phi) con phi el angulo de l; la inversa es una rotacion. DFT bidimensional directa (sin FFT).
Supuestos: cielo plano periodico, modos l = 0 y de Nyquist anulados (el angulo de l no es simetrico en Nyquist). Validez: ilustrativa; el cielo curvo exige armonicos de espin 2.
Tolerancia: B recuperado de un mapa de E puro, 1e-10 de la amplitud; Parseval a 1e-9; la mascara apodizada fuga menos que la dura.
"""
from __future__ import annotations
import cmath, math, platform, random, sys

N = 32
W = [[cmath.exp(-2j * math.pi * ((i * j) % N) / N) for j in range(N)] for i in range(N)]

def dft1(v, sign):
    if sign < 0:
        return [sum(v[j] * W[i][j] for j in range(N)) for i in range(N)]
    return [sum(v[j] * W[i][j].conjugate() for j in range(N)) / N for i in range(N)]

def dft2(a, sign):
    r = [dft1(row, sign) for row in a]
    cols = [dft1([r[i][j] for i in range(N)], sign) for j in range(N)]
    return [[cols[j][i] for j in range(N)] for i in range(N)]

def freq(i):
    return i if i <= N // 2 else i - N

def angulos():
    c2 = [[0.0] * N for _ in range(N)]; s2 = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            lx, ly = freq(i), freq(j)
            l2 = lx * lx + ly * ly
            if l2:
                c2[i][j] = (lx * lx - ly * ly) / l2
                s2[i][j] = 2 * lx * ly / l2
    return c2, s2

C2, S2 = angulos()

def campo(rng, sig=4.0):
    x = [[rng.gauss(0, 1) for _ in range(N)] for _ in range(N)]
    f = dft2(x, -1)
    for i in range(N):
        for j in range(N):
            l2 = freq(i) ** 2 + freq(j) ** 2
            nyq = abs(freq(i)) == N // 2 or abs(freq(j)) == N // 2
            f[i][j] *= math.exp(-l2 / (2 * sig * sig)) if (l2 and not nyq) else 0.0
    return f

def a_qu(E, B):
    Q = [[-(E[i][j] * C2[i][j] - B[i][j] * S2[i][j]) for j in range(N)] for i in range(N)]
    U = [[-(E[i][j] * S2[i][j] + B[i][j] * C2[i][j]) for j in range(N)] for i in range(N)]
    return Q, U

def a_eb(Q, U):
    E = [[-(Q[i][j] * C2[i][j] + U[i][j] * S2[i][j]) for j in range(N)] for i in range(N)]
    B = [[-(-Q[i][j] * S2[i][j] + U[i][j] * C2[i][j]) for j in range(N)] for i in range(N)]
    return E, B

def real(a):
    mx = max(abs(a[i][j].imag) for i in range(N) for j in range(N))
    return [[a[i][j].real for j in range(N)] for i in range(N)], mx

def pot(f):
    return sum(abs(f[i][j]) ** 2 for i in range(N) for j in range(N))

def mascara(apod):
    m = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            d = max(abs(i - N // 2), abs(j - N // 2))      # distancia de Chebyshev al centro
            if d <= 8:
                m[i][j] = 1.0
            elif apod and d < 8 + apod:
                m[i][j] = math.cos(0.5 * math.pi * (d - 8) / apod) ** 2
    return m

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    Ef = campo(rng); Bf = campo(rng)
    zero = [[0j] * N for _ in range(N)]
    # prueba 1: E puro
    Qf, Uf = a_qu(Ef, zero)
    Q, imq = real(dft2(Qf, +1)); U, imu = real(dft2(Uf, +1))
    Qr = dft2([[complex(v) for v in r] for r in Q], -1); Ur = dft2([[complex(v) for v in r] for r in U], -1)
    Er, Br = a_eb(Qr, Ur)
    ex = max(abs(Er[i][j] - Ef[i][j]) for i in range(N) for j in range(N))
    bx = max(abs(Br[i][j]) for i in range(N) for j in range(N))
    amp = max(abs(Ef[i][j]) for i in range(N) for j in range(N))
    print(f"E puro: parte imaginaria maxima de Q,U = {max(imq, imu):.1e} ; |E recuperado - E| max = {ex:.1e} ; |B recuperado| max = {bx:.1e} (amplitud de E {amp:.2f})")
    assert max(imq, imu) < 1e-10 and ex < 1e-10 * max(1.0, amp) and bx < 1e-10 * max(1.0, amp)
    # prueba 2: B puro
    Qf2, Uf2 = a_qu(zero, Bf)
    Q2, _ = real(dft2(Qf2, +1)); U2, _ = real(dft2(Uf2, +1))
    Er2, Br2 = a_eb(dft2([[complex(v) for v in r] for r in Q2], -1), dft2([[complex(v) for v in r] for r in U2], -1))
    e2 = max(abs(Er2[i][j]) for i in range(N) for j in range(N))
    b2 = max(abs(Br2[i][j] - Bf[i][j]) for i in range(N) for j in range(N))
    print(f"B puro: |E recuperado| max = {e2:.1e} ; |B recuperado - B| max = {b2:.1e}")
    assert e2 < 1e-10 * max(1.0, amp) and b2 < 1e-10 * max(1.0, amp)
    # Parseval
    pq = pot(Qr) + pot(Ur); pe = pot(Er) + pot(Br)
    print(f"Parseval: suma |Q|^2 + |U|^2 = {pq:.6e} ; suma |E|^2 + |B|^2 = {pe:.6e} ; cociente = {pq / pe:.12f}")
    assert abs(pq / pe - 1) < 1e-9
    # fuga por mascara
    print(f"{'mascara':>22} {'fraccion de pixeles':>20} {'fuga sum B^2 / sum E^2':>24}")
    fugas = {}
    for nombre, ap in (("dura (sin apodizar)", 0), ("apodizada 6 pixeles", 6)):
        m = mascara(ap)
        Qm = [[complex(Q[i][j] * m[i][j]) for j in range(N)] for i in range(N)]
        Um = [[complex(U[i][j] * m[i][j]) for j in range(N)] for i in range(N)]
        Em, Bm = a_eb(dft2(Qm, -1), dft2(Um, -1))
        fugas[nombre] = pot(Bm) / pot(Em)
        fp = sum(sum(r) for r in m) / (N * N)
        print(f"{nombre:>22} {fp:20.4f} {fugas[nombre]:24.4f}")
    a, b = fugas["dura (sin apodizar)"], fugas["apodizada 6 pixeles"]
    assert a > b > 0
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
