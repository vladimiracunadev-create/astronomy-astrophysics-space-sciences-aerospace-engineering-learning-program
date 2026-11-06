#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C23: optimización restringida (Lagrange, KKT y SQP) con verificación.

Datos: (a) transferencia bielíptica con razón de radios R = 13 (valor ILUSTRATIVO) y
tiempo máximo de vuelo Tmax = 1000 unidades de sqrt(r1^3/mu) (límite SINTÉTICO);
(b) problema de ejemplo: mínimo de f = (x-2)^2 + (y-1)^2 sobre la circunferencia
x^2 + y^2 = 1, cuya solución exacta es (2, 1)/sqrt(5) con multiplicador sqrt(5) - 1 (para L = f + lam (g - 1)).
Modelo: (a) minimizar Dv(x) sujeto a T(x) <= Tmax; condiciones KKT: gradiente de
Dv + mu * gradiente de T = 0, mu >= 0, mu (T - Tmax) = 0. (b) minimizar con restricción de
igualdad; Lagrangiano L = f + lam (g - 1); SQP = Newton sobre las condiciones KKT.
Supuestos: órbitas circulares coplanares, impulsos instantáneos (como en C17).
Tolerancia: (a) T(x*) = Tmax a 1e-9, mu > 0, residuo KKT < 1e-8 y coincidencia con el
barrido en malla a 1e-3; (b) SQP converge cuadráticamente a la solución exacta (error
< 1e-12 en 6 iteraciones) y coincide con el barrido angular.
"""
import math, platform

R = 13.0


def dv(x):
    v1 = math.sqrt(2 * x / (1 + x)) - 1
    va = math.sqrt(2 / x - 2 / (1 + x))
    vb = math.sqrt(2 / x - 2 / (x + R))
    v3 = math.sqrt(1 / R) - math.sqrt(2 / R - 2 / (x + R))
    return v1 + abs(vb - va) + abs(v3)


T = lambda x: math.pi * (((1 + x) / 2) ** 1.5 + ((x + R) / 2) ** 1.5)
d = lambda f, x, h=1e-5: (f(x + h) - f(x - h)) / (2 * h)

print(f"Python {platform.python_version()}")
# (a) KKT
Tmax = 1000.0
lo, hi = R, 1e5
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if T(mid) < Tmax:
        lo = mid
    else:
        hi = mid
xs = 0.5 * (lo + hi)
dd, dT = d(dv, xs), d(T, xs)
mu = -dd / dT
print(f"(a) restricción activa: T(x*) = {T(xs):.9f} con x* = {xs:.4f} r1 ; Dv(x*) = {dv(xs):.6f}")
print(f"    gradientes: Dv' = {dd:.4e}, T' = {dT:.4f} ; multiplicador mu = {mu:.4e} (> 0) ; residuo KKT = {dd + mu*dT:.1e}")
grid = min((dv(R + i * 0.01), R + i * 0.01) for i in range(0, 100000) if T(R + i * 0.01) <= Tmax)
print(f"    barrido en malla sobre la región factible: x = {grid[1]:.2f}, Dv = {grid[0]:.6f}")
print(f"    sin restricción (hasta x = 1e4): Dv = {dv(1e4):.6f} con T = {T(1e4):.3e}")
# sensibilidad: derivada del óptimo respecto de Tmax = -mu
def Dv_opt(tm):
    l, h2 = R, 1e6
    for _ in range(200):
        m = 0.5 * (l + h2)
        if T(m) < tm:
            l = m
        else:
            h2 = m
    return dv(0.5 * (l + h2))
sens = (Dv_opt(Tmax + 1) - Dv_opt(Tmax - 1)) / 2
print(f"    sensibilidad dDv*/dTmax = {sens:.4e} ; -mu = {-mu:.4e}")
assert abs(T(xs) - Tmax) < 1e-9 and mu > 0 and abs(dd + mu * dT) < 1e-8
assert abs(grid[1] - xs) < 1e-2 and abs(sens + mu) / mu < 1e-3

# (b) SQP
f = lambda x, y: (x - 2) ** 2 + (y - 1) ** 2
def resolver3(A, b):
    n = 3
    M = [row[:] + [bi] for row, bi in zip(A, b)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i]))
        M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            c = M[r][i] / M[i][i]
            for k in range(i, n + 1):
                M[r][k] -= c * M[i][k]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][k] * x[k] for k in range(i + 1, n))) / M[i][i]
    return x

x, y, lam = 1.0, 1.0, 0.0
ex = (2 / math.sqrt(5), 1 / math.sqrt(5))
print("(b) SQP (Newton sobre KKT) para min f s.t. x^2 + y^2 = 1, desde (1, 1), lam = 0:")
hist = []
for it in range(1, 9):
    gx, gy, g = 2 * x, 2 * y, x * x + y * y - 1
    F = [2 * (x - 2) + lam * gx, 2 * (y - 1) + lam * gy, g]
    W = 2 + 2 * lam
    dx, dy, dl = resolver3([[W, 0, gx], [0, W, gy], [gx, gy, 0]], [-F[0], -F[1], -F[2]])
    x, y, lam = x + dx, y + dy, lam + dl
    e = math.hypot(x - ex[0], y - ex[1])
    hist.append(e)
    print(f"    it {it}: (x, y) = ({x:.10f}, {y:.10f}) lam = {lam:.8f} ; error = {e:.3e} ; |g| = {abs(x*x+y*y-1):.2e}")
    if e < 1e-14:
        break
assert hist[5] < 1e-12 and abs(lam - (math.sqrt(5) - 1)) < 1e-12
th = min((f(math.cos(t), math.sin(t)), t) for t in [2 * math.pi * i / 200000 for i in range(200000)])
print(f"    barrido angular: theta = {th[1]:.5f} rad, f = {th[0]:.8f} ; exacto: f = {f(*ex):.8f}, theta = {math.atan2(1, 2):.5f}")
assert abs(th[0] - f(*ex)) < 1e-8
print("Pruebas superadas.")
