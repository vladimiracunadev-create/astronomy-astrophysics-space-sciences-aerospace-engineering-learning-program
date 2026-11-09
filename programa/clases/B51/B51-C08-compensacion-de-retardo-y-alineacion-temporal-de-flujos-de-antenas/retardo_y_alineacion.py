#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C08: estimacion y compensacion de un retardo entero mas fraccionario entre los flujos de dos antenas.

Datos: ninguna constante fisica. Dos flujos de ruido gaussiano de banda limitada (N = 4096 muestras, 80 % de la banda de Nyquist), retardo verdadero de 37,30 muestras y
relaciones senal-ruido de 1,0 y 2,0 son SINTETICOS e ILUSTRATIVOS (semilla 20261109).
Modelo: y(t) = x(t - D) + ruido; el retardo entero sale del maximo de la correlacion cruzada (por FFT); el fraccionario por (a) interpolacion parabolica del pico y (b) pendiente de la
fase del espectro cruzado (minimos cuadrados ponderados por la amplitud). La compensacion fraccionaria se aplica con una rampa de fase en frecuencia.
Segunda via: las dos estimaciones son independientes entre si; el coeficiente de correlacion tras alinear se compara con el valor analitico 1 / sqrt((1 + 1/s1)(1 + 1/s2)).
Supuestos: retardo constante, retardo circular (muestras periodicas), ruido blanco aditivo. Validez: ilustrativa.
Tolerancia: la parabola dentro de 0,12 y la pendiente de fase dentro de 0,05 muestras del retardo; correlacion tras alinear dentro de 0,02 del valor analitico.
"""
from __future__ import annotations
import cmath, math, platform, random, sys

def fft(a, inv=False):
    n = len(a)
    if n == 1:
        return list(a)
    e = fft(a[0::2], inv); o = fft(a[1::2], inv)
    s = 1 if inv else -1
    t = [cmath.exp(s * 2j * math.pi * k / n) * o[k] for k in range(n // 2)]
    return [e[k] + t[k] for k in range(n // 2)] + [e[k] - t[k] for k in range(n // 2)]

def ifft(a):
    n = len(a)
    return [v / n for v in fft(a, True)]

def compute():
    rng = random.Random(20261109)
    N, D, s1, s2 = 4096, 37.3, 1.0, 2.0
    # senal de banda limitada
    X = [0j] * N
    kmax = int(0.4 * N)
    for k in range(1, kmax):
        c = complex(rng.gauss(0, 1), rng.gauss(0, 1))
        X[k] = c; X[N - k] = c.conjugate()
    x = [v.real for v in ifft(X)]
    px = sum(v * v for v in x) / N
    Xs = fft(x)
    Y = [Xs[k] * cmath.exp(-2j * math.pi * (k if k <= N // 2 else k - N) * D / N) for k in range(N)]
    ys = [v.real for v in ifft(Y)]
    a = [v + rng.gauss(0, math.sqrt(px / s1)) for v in x]
    b = [v + rng.gauss(0, math.sqrt(px / s2)) for v in ys]
    A = fft(a); B = fft(b)
    cross = [B[k] * A[k].conjugate() for k in range(N)]
    cc = [v.real for v in ifft(cross)]
    k0 = max(range(N), key=lambda i: cc[i])
    lag_int = k0 if k0 <= N // 2 else k0 - N
    ym, y0, yp = cc[(k0 - 1) % N], cc[k0], cc[(k0 + 1) % N]
    frac_a = 0.5 * (ym - yp) / (ym - 2 * y0 + yp)
    est_a = lag_int + frac_a
    # (b) pendiente de fase del espectro cruzado alrededor del retardo entero
    num = den = 0.0
    for k in range(1, kmax):
        r = cross[k] * cmath.exp(2j * math.pi * k * lag_int / N)        # quita el retardo entero
        w = abs(cross[k]) ** 2
        phk = cmath.phase(r)
        num += w * phk * k; den += w * k * k
    est_b = lag_int - num / den * N / (2 * math.pi)
    R = dict(N=N, D=D, lag_int=lag_int, est_a=est_a, est_b=est_b, peak=y0 / N)
    # compensacion fraccionaria con la estimacion b
    Bc = [B[k] * cmath.exp(2j * math.pi * (k if k <= N // 2 else k - N) * est_b / N) for k in range(N)]
    bc = [v.real for v in ifft(Bc)]
    def corr(p, q):
        mp = sum(p) / len(p); mq = sum(q) / len(q)
        sp = math.sqrt(sum((u - mp) ** 2 for u in p)); sq = math.sqrt(sum((u - mq) ** 2 for u in q))
        return sum((u - mp) * (v - mq) for u, v in zip(p, q)) / (sp * sq)
    R["rho_antes"] = corr(a, b); R["rho_despues"] = corr(a, bc)
    R["rho_teo"] = 1 / math.sqrt((1 + 1 / s1) * (1 + 1 / s2))
    # solo entero (error fraccionario residual)
    bi = [b[(i + lag_int) % N] for i in range(N)]
    R["rho_entero"] = corr(a, bi)
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"N = {R['N']} muestras ; retardo verdadero = {R['D']} muestras")
    print(f"retardo entero (pico de correlacion cruzada) = {R['lag_int']}")
    print(f"fraccion (a) parabola: retardo = {R['est_a']:.4f} ; (b) pendiente de fase: retardo = {R['est_b']:.4f}")
    assert R["lag_int"] == 37
    assert abs(R["est_a"] - R["D"]) < 0.12 and abs(R["est_b"] - R["D"]) < 0.05
    print(f"coeficiente de correlacion: sin alinear = {R['rho_antes']:+.4f} ; solo retardo entero = {R['rho_entero']:.4f} ; alineado con fraccion = {R['rho_despues']:.4f} ; analitico = {R['rho_teo']:.4f}")
    assert abs(R["rho_despues"] - R["rho_teo"]) < 0.02 and R["rho_entero"] < R["rho_despues"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
