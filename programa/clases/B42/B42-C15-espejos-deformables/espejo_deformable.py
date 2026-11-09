#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C15: espejo deformable con funciones de influencia gaussianas y error de ajuste de una pantalla de Kolmogorov.

Datos: r0 = 0,16 m, malla de 64 x 64 con paso de 0,02 m (L = 1,28 m), pasos de actuadores de 4, 8 y 16 pixeles (8, 16 y 32 cm) y acoplamiento entre vecinos del 15 % son ILUSTRATIVOS.
10 FFT (20 pantallas independientes), semilla 20261109. El coeficiente 0,023 de la PSD es el de libro de texto, NO consultado aqui. No es el catalogo de un espejo real.
Modelo: la superficie del espejo es s(x) = sum_k c_k g(x - x_k), g gaussiana con exp(-d^2 / (2 w^2)) = 0,15 en la distancia d entre actuadores ; red cuadrada y condiciones periodicas
(coherentes con la pantalla FFT), de modo que A^T A es bloque-circulante y se invierte con una FFT 2D sobre la red de actuadores (otra via: se verifica residuo A^T(s - A c) = 0).
El error de ajuste es la varianza residual de s - A c (sin pistón). Se contrasta con la ley de escala sigma^2 ~ (d / r0)^(5/3): el cociente entre pasos consecutivos debe ser 2^(5/3) = 3,17.
Supuestos: sin histeresis ni acoplamiento mecanico real, sin carrera limitada, pupila sin borde. Validez: ilustrativa de la teoria de ajuste.
Tolerancia: residuo normal a 1e-9 ; cociente de varianzas entre pasos a 25 % de 2^(5/3).
"""
from __future__ import annotations
import cmath, math, platform, random

N = 64
DX = 0.02
R0 = 0.16

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

def ifft2(g):
    n, m = len(g), len(g[0])
    c = [[v.conjugate() for v in r] for r in g]
    f = fft2(c)
    return [[f[i][j].conjugate() / (n * m) for j in range(m)] for i in range(n)]

def pantallas(rnd):
    df = 1.0 / (N * DX)
    g = [[0j] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            fy = (i if i < N // 2 else i - N) * df
            fx = (j if j < N // 2 else j - N) * df
            f = math.hypot(fx, fy)
            if f > 0:
                a = math.sqrt(0.023 * R0 ** (-5 / 3) * f ** (-11 / 3)) * df
                g[i][j] = a * complex(rnd.gauss(0, 1), rnd.gauss(0, 1))
    f = fft2(g)
    return [[f[i][j].real for j in range(N)] for i in range(N)], [[f[i][j].imag for j in range(N)] for i in range(N)]

def gauss_periodica(p, w):
    # influencia de un actuador en el origen, periodica
    g = [[0.0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            di = min(i, N - i)
            dj = min(j, N - j)
            g[i][j] = math.exp(-(di * di + dj * dj) / (2 * w * w))
    return g

CACHE = {}

def preparar(p, w):
    if p in CACHE:
        return CACHE[p]
    n = N // p
    g = gauss_periodica(p, w)
    # A^T A como funcion del desplazamiento entre actuadores: autocorrelacion de g muestreada en la red
    ata = [[0.0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            tot = 0.0
            for di in range(N):
                gi = g[di]
                gj = g[(di - a * p) % N]
                for dj in range(N):
                    tot += gi[dj] * gj[(dj - b * p) % N]
            ata[a][b] = tot
    F = fft2([[complex(v) for v in r] for r in ata])
    CACHE[p] = (g, ata, F)
    return CACHE[p]

def ajustar(s, p, w):
    n = N // p
    g, ata, F = preparar(p, w)
    # A^T s: para cada actuador, correlacion cruzada de s con la influencia (suma sobre toda la malla periodica)
    rhs = [[0.0] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            tot = 0.0
            for i in range(N):
                gi = g[(i - a * p) % N]
                si = s[i]
                for j in range(N):
                    tot += si[j] * gi[(j - b * p) % N]
            rhs[a][b] = tot
    R = fft2([[complex(v) for v in r] for r in rhs])
    mn = min(abs(F[i][j]) for i in range(n) for j in range(n))
    C = ifft2([[R[i][j] / F[i][j] for j in range(n)] for i in range(n)])
    c = [[C[i][j].real for j in range(n)] for i in range(n)]
    return c, g, rhs, ata, mn

def superficie(c, g, p):
    n = len(c)
    surf = [[0.0] * N for _ in range(N)]
    for a in range(n):
        for b in range(n):
            ca = c[a][b]
            for i in range(N):
                gi = g[(i - a * p) % N]
                row = surf[i]
                for j in range(N):
                    row[j] += ca * gi[(j - b * p) % N]
    return surf

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rnd = random.Random(20261109)
    scr = []
    for _ in range(10):              # 10 FFT = 20 pantallas
        scr.extend(pantallas(rnd))
    print(f"pantallas = {len(scr)} ; r0 = {R0} m = {R0 / DX:.1f} px")
    res = {}
    var_s = []
    for s in scr:
        m = sum(sum(r) for r in s) / (N * N)
        var_s.append(sum((v - m) ** 2 for r in s for v in r) / (N * N))
    print(f"varianza de la pantalla (sin piston, malla periodica) = {sum(var_s) / len(var_s):.3f} rad^2")
    print(f"{'paso [px]':>9} {'paso [cm]':>9} {'d/r0':>6} {'actuadores':>10} {'sigma^2 residual':>17} {'mu = s2/(d/r0)^(5/3)':>22}")
    for p in (4, 8, 16):
        w = p / math.sqrt(2 * math.log(1 / 0.15))
        acum = 0.0
        for k, s in enumerate(scr):
            c, g, rhs, ata, mn = ajustar(s, p, w)
            surf = superficie(c, g, p)
            m = sum(sum(r) for r in s) / (N * N)
            ms = sum(sum(r) for r in surf) / (N * N)
            acum += sum(((s[i][j] - m) - (surf[i][j] - ms)) ** 2 for i in range(N) for j in range(N)) / (N * N)
            if k == 0:
                # residuo normal: A^T (s - A c) = 0 (via independiente)
                n = N // p
                res_n = 0.0
                for a in range(n):
                    for b in range(n):
                        tot = 0.0
                        for i in range(N):
                            for j in range(N):
                                tot += (s[i][j] - surf[i][j]) * g[(i - a * p) % N][(j - b * p) % N]
                        res_n = max(res_n, abs(tot))
                escala = max(abs(rhs[a][b]) for a in range(n) for b in range(n))
                assert res_n / escala < 1e-9, (p, res_n, escala)
        v = acum / len(scr)
        res[p] = v
        x = (p * DX / R0) ** (5 / 3)
        print(f"{p:9d} {p * DX * 100:9.0f} {p * DX / R0:6.2f} {(N // p) ** 2:10d} {v:17.4f} {v / x:22.4f}")
    esperado = 2 ** (5 / 3)
    for a, b in ((4, 8), (8, 16)):
        q = res[b] / res[a]
        print(f"cociente de varianzas residuales paso {b}/paso {a} = {q:.3f} ; 2^(5/3) = {esperado:.3f}")
        assert abs(q / esperado - 1) < 0.25, (a, b, q)
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
