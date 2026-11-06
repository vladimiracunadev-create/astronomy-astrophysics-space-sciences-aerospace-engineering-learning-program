#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C18: interpolación de Lagrange, fenómeno de Runge y efeméride tabulada.

Datos: (a) f = sin x en [0, 2 pi] (cota de la derivada conocida); (b) función de
Runge 1/(1 + 25 x^2) en [-1, 1]; (c) efeméride SINTÉTICA de una órbita ilustrativa
a = 26 560 km, e = 0.30 (GM de la Tierra = 3.986004e14 m3/s2, valor nominal IAU
2015, Res. B3), tabulada con paso T/24 y generada con la solución de Kepler.
Modelo: polinomio de Lagrange de grado n con n+1 nodos (DLMF 3.3.1-3.3.2) y su error
f(x) - P_n(x) = f^(n+1)(xi)/(n+1)! * omega_{n+1}(x) (DLMF 3.3.5).
Supuestos: datos exactos (sin ruido). Validez: interpolación dentro del intervalo de
los nodos; la extrapolación se muestra como contraejemplo.
Tolerancia: el error real de (a) debe respetar la cota de DLMF 3.3.5 (con
|f^(n+1)| <= 1); con nodos equiespaciados el error de Runge debe crecer con n y con
nodos de Chebyshev decrecer; la extrapolación debe perder precisión de forma
monótona y rápida.
"""
import math, platform


def lagrange(xs, ys, x):
    total = 0.0
    for k in range(len(xs)):
        lk = 1.0
        for j in range(len(xs)):
            if j != k:
                lk *= (x - xs[j]) / (xs[k] - xs[j])
        total += ys[k] * lk
    return total


def omega(xs, x):
    w = 1.0
    for xi in xs:
        w *= (x - xi)
    return w


print(f"Python {platform.python_version()}")

# (a) cota de DLMF 3.3.5 para sin x
print("(a) sin x en [0, 2pi]: error máximo de la interpolación frente a la cota |omega|/(n+1)!")
for n in (2, 4, 6, 8):
    xs = [2 * math.pi * i / n for i in range(n + 1)]
    ys = [math.sin(x) for x in xs]
    pts = [2 * math.pi * i / 1000 for i in range(1001)]
    err = max(abs(math.sin(x) - lagrange(xs, ys, x)) for x in pts)
    cota = max(abs(omega(xs, x)) for x in pts) / math.factorial(n + 1)
    print(f"    n={n}: error = {err:.3e} ; cota = {cota:.3e}")
    assert err <= cota * 1.0000001

# (b) Runge
f = lambda x: 1 / (1 + 25 * x * x)
pts = [-1 + 2 * i / 2000 for i in range(2001)]
eq, ch = {}, {}
print("(b) Runge 1/(1+25x^2): error máximo en [-1, 1]")
for n in (4, 8, 12, 16, 20):
    xe = [-1 + 2 * i / n for i in range(n + 1)]
    xc = [math.cos(math.pi * (2 * i + 1) / (2 * (n + 1))) for i in range(n + 1)]
    eq[n] = max(abs(f(x) - lagrange(xe, [f(v) for v in xe], x)) for x in pts)
    ch[n] = max(abs(f(x) - lagrange(xc, [f(v) for v in xc], x)) for x in pts)
    print(f"    n={n:2d}: equiespaciados = {eq[n]:.3e} ; Chebyshev = {ch[n]:.3e}")
assert eq[20] > eq[12] > eq[8] and ch[20] < ch[12] < ch[8]

# (c) efeméride
GM = 3.986004e14
a, e = 26_560e3, 0.30
b = a * math.sqrt(1 - e * e)
T = 2 * math.pi * math.sqrt(a**3 / GM)
nn = 2 * math.pi / T


def xpos(t):
    M = nn * t
    E = M
    for _ in range(100):
        dE = (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        E -= dE
        if abs(dE) < 1e-15:
            break
    return a * (math.cos(E) - e), b * math.sin(E)


dt = T / 24
tab = [(i * dt, xpos(i * dt)) for i in range(0, 25)]
print(f"(c) efeméride sintética: paso {dt:.1f} s ({dt/60:.1f} min), periodo {T:.1f} s")
for n in (3, 5, 7, 9):
    i0 = 8                                   # nodos centrados en torno a t = 10 dt
    idx = list(range(i0, i0 + n + 1))
    ts = [tab[i][0] for i in idx]
    xs_ = [tab[i][1][0] for i in idx]
    ys_ = [tab[i][1][1] for i in idx]
    tm = [ts[n // 2] + dt * 0.5 + dt * j / 20 for j in range(10)]              # entre nodos centrales
    err = max(math.hypot(lagrange(ts, xs_, t) - xpos(t)[0], lagrange(ts, ys_, t) - xpos(t)[1]) for t in tm)
    print(f"    grado {n}: error máximo de posición entre nodos centrales = {err:10.4f} m")
errs = {}
for n in (3, 5, 7, 9):
    idx = list(range(8, 8 + n + 1))
    ts = [tab[i][0] for i in idx]; xs_ = [tab[i][1][0] for i in idx]; ys_ = [tab[i][1][1] for i in idx]
    tm = [ts[n // 2] + dt * 0.5 + dt * j / 20 for j in range(10)]
    errs[n] = max(math.hypot(lagrange(ts, xs_, t) - xpos(t)[0], lagrange(ts, ys_, t) - xpos(t)[1]) for t in tm)
assert errs[9] < errs[7] < errs[5] < errs[3]
# extrapolación con 6 nodos (i = 8..13): evaluar hacia fuera
idx = list(range(8, 14))
ts = [tab[i][0] for i in idx]; xs_ = [tab[i][1][0] for i in idx]; ys_ = [tab[i][1][1] for i in idx]
print("    extrapolación con 6 nodos (t en pasos desde el último nodo):")
prev = 0
for k in (0.5, 1, 2, 4, 8):
    t = ts[-1] + k * dt
    err = math.hypot(lagrange(ts, xs_, t) - xpos(t)[0], lagrange(ts, ys_, t) - xpos(t)[1])
    print(f"      +{k:>3} pasos: error = {err:.4e} m")
    assert err > prev
    prev = err
print("Pruebas superadas.")
