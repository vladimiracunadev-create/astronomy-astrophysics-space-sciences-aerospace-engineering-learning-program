#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B35-C09: espectros de potencia, funciones de estructura, intermitencia de una cascada multiplicativa y helicidad cruzada de series sinteticas.

Datos: ninguna constante fisica ni dato observado. Las series son SINTETICAS (fases aleatorias con semilla 20261109) y los pendientes (-5/3 de Kolmogorov, -3/2 de Iroshnikov-Kraichnan), el parametro
del modelo p (0.7) y las correlaciones son ILUSTRATIVOS; no se analiza ninguna medicion del viento solar.
Modelo: (1) serie periodica de N = 4096 puntos con amplitudes de Fourier gaussianas de varianza k^-alpha; espectro promediado en 40 realizaciones y ajuste de la pendiente en log-log (FFT propia, radix 2);
(2) funcion de estructura de segundo orden S2(l) = <(x(i+l) - x(i))^2> ~ l^(alpha-1) (valida para 1 < alpha < 3) y curtosis de los incrementos (3 para un campo gaussiano);
(3) cascada binomial (modelo p) de 12 niveles: sum(mu^q) = (p^q + (1-p)^q)^n exacta y curtosis de las medidas por caja 2^n S4/S2^2; (4) helicidad cruzada sigma_c = 2<v b>/(<v^2>+<b^2>).
Supuestos: campo estacionario y periodico; amplitudes gaussianas independientes. Validez: ilustrativa.
Tolerancia: pendiente espectral con error < 0.06; exponente de S2 igual al de la suma discreta con error < 0.03 (y a alpha-1 con error < 0.12 por el dominio finito); curtosis gaussiana entre 2.7 y 3.3; sumas de la cascada a 1e-9 relativo; sigma_c a 0.02 del valor analitico.
"""
from __future__ import annotations
import cmath, math, platform, random, sys

def fft(a):
    n = len(a)
    if n == 1:
        return a[:]
    par = fft(a[0::2]); imp = fft(a[1::2])
    out = [0j] * n
    for k in range(n // 2):
        t = cmath.exp(-2j * math.pi * k / n) * imp[k]
        out[k] = par[k] + t
        out[k + n // 2] = par[k] - t
    return out

def sintetizar(N, alpha, rng):
    X = [0j] * N
    for k in range(1, N // 2):
        s = k ** (-alpha / 2) / math.sqrt(2)
        c = complex(rng.gauss(0, s), rng.gauss(0, s))
        X[k] = c
        X[N - k] = c.conjugate()
    # inversa por la FFT de la conjugada
    y = fft([z.conjugate() for z in X])
    return [z.real / N for z in y]

def ajuste(xs, ys):
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    return sum((a - mx) * (b - my) for a, b in zip(xs, ys)) / sum((a - mx) ** 2 for a in xs)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    N, R = 4096, 40
    print(f"{'alpha':>7} {'pendiente espectral':>20} {'zeta2 medido':>13} {'alpha-1':>8} {'curtosis(l=4)':>14} {'curtosis(l=64)':>15}")
    for alpha in (5 / 3, 3 / 2):
        P = [0.0] * (N // 2)
        ls = [4, 8, 16, 32, 64]
        S2 = {l: 0.0 for l in ls}
        S4 = {l: 0.0 for l in ls}
        for _ in range(R):
            x = sintetizar(N, alpha, rng)
            F = fft([complex(v) for v in x])
            for k in range(1, N // 2):
                P[k] += abs(F[k]) ** 2
            for l in ls:
                d = [x[(i + l) % N] - x[i] for i in range(N)]
                S2[l] += sum(u * u for u in d) / N
                S4[l] += sum(u ** 4 for u in d) / N
        ks = list(range(4, 400))
        sl = ajuste([math.log(k) for k in ks], [math.log(P[k] / R) for k in ks])
        z2 = ajuste([math.log(l) for l in ls], [math.log(S2[l] / R) for l in ls])
        ku = {l: (S4[l] / R) / (S2[l] / R) ** 2 for l in ls}
        print(f"{alpha:7.4f} {sl:20.4f} {z2:13.4f} {alpha-1:8.4f} {ku[4]:14.3f} {ku[64]:15.3f}")
        assert abs(sl + alpha) < 0.06
        zp = ajuste([math.log(l) for l in ls], [math.log(sum(k ** (-alpha) * (1 - math.cos(2 * math.pi * k * l / N)) for k in range(1, N // 2))) for l in ls])
        print(f"        pendiente de S2 prevista por la suma discreta (dominio finito): {zp:.4f}")
        assert abs(z2 - zp) < 0.03 and abs(z2 - (alpha - 1)) < 0.12
        assert all(2.7 < ku[l] < 3.3 for l in ls)
    # cascada binomial
    p = 0.7
    mu = [1.0]
    print(f"{'nivel n':>8} {'sum mu^2':>12} {'analitico':>12} {'sum mu^4':>12} {'analitico':>12} {'curtosis':>10} {'analitica':>10}")
    for n in range(1, 13):
        mu = [m * f for m in mu for f in (p, 1 - p)]
        s2 = sum(m ** 2 for m in mu); s4 = sum(m ** 4 for m in mu)
        a2 = (p ** 2 + (1 - p) ** 2) ** n; a4 = (p ** 4 + (1 - p) ** 4) ** n
        ku = 2 ** n * s4 / s2 ** 2
        ka = 2 ** n * a4 / a2 ** 2
        if n in (1, 2, 4, 8, 12):
            print(f"{n:8d} {s2:12.6e} {a2:12.6e} {s4:12.6e} {a4:12.6e} {ku:10.3f} {ka:10.3f}")
        assert abs(s2 / a2 - 1) < 1e-9 and abs(s4 / a4 - 1) < 1e-9 and abs(ku / ka - 1) < 1e-9
        assert abs(sum(mu) - 1) < 1e-12
    # helicidad cruzada: b = c v + ruido (varianzas 1)
    c, sr = 0.8, 0.6
    n = 100000
    v = [rng.gauss(0, 1) for _ in range(n)]
    b = [c * x + rng.gauss(0, sr) for x in v]
    sc = 2 * sum(x * y for x, y in zip(v, b)) / (sum(x * x for x in v) + sum(y * y for y in b))
    sc_an = 2 * c / (1 + c * c + sr * sr)
    print(f"helicidad cruzada: medida {sc:.4f} ; analitica {sc_an:.4f}")
    assert abs(sc - sc_an) < 0.02
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
