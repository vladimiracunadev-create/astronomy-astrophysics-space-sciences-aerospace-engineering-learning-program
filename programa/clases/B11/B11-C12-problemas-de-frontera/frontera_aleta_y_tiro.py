#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C12: problemas de frontera por diferencias finitas y por tiro.

Datos: (a) aleta térmica SINTÉTICA de longitud L = 1 m con m = 2 1/m,
T_amb = 250 K, T(0) = 300 K, T(L) = 270 K. (b) tiro vertical con GM de la Tierra =
3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m (valores nominales IAU 2015,
Res. B3); T = 300 s y altura final 1000 km son datos SINTÉTICOS de ejemplo.
Modelo: (a) theta'' = m^2 theta, theta = T - T_amb, con solución exacta
theta(x) = [theta0 sinh(m (L-x)) + thetaL sinh(m x)] / sinh(m L).
(b) r'' = -GM / r^2, r(0) = R, r(T) = R + h; se busca v0 = r'(0).
Métodos: (a) diferencias finitas centrales (DLMF 3.4.6; sistema tridiagonal por
el algoritmo de Thomas) y tiro lineal con RK4 (dos disparos); (b) tiro no lineal
con método de la secante e integración RK4.
Supuestos: coeficientes constantes en (a); movimiento radial sin atmósfera en (b).
Tolerancia: (a) razón de errores al duplicar N en [3.5, 4.5] (orden 2); tiro
lineal con error < 1e-9 K; (b) residuo de la frontera < 1e-6 m y acuerdo con la
integración de paso mitad a 1e-6 m/s.
"""
import math, platform

m, L, Ta, T0, T1 = 2.0, 1.0, 250.0, 300.0, 270.0
th0, thL = T0 - Ta, T1 - Ta
exacta = lambda x: (th0 * math.sinh(m * (L - x)) + thL * math.sinh(m * x)) / math.sinh(m * L)


def diferencias_finitas(N):
    h = L / N
    n = N - 1
    a = [1.0] * n
    b = [-(2 + (m * h) ** 2)] * n
    c = [1.0] * n
    d = [0.0] * n
    d[0] -= th0
    d[-1] -= thL
    for i in range(1, n):                      # algoritmo de Thomas
        w = a[i] / b[i - 1]
        b[i] -= w * c[i - 1]
        d[i] -= w * d[i - 1]
    x = [0.0] * n
    x[-1] = d[-1] / b[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]
    return [th0] + x + [thL]


def rk4_sis(f, y, a, b, N):
    h = (b - a) / N
    t = a
    for _ in range(N):
        k1 = f(t, y); k2 = f(t + h / 2, [u + h / 2 * k for u, k in zip(y, k1)])
        k3 = f(t + h / 2, [u + h / 2 * k for u, k in zip(y, k2)]); k4 = f(t + h, [u + h * k for u, k in zip(y, k3)])
        y = [u + h * (p + 2 * q + 2 * r + w) / 6 for u, p, q, r, w in zip(y, k1, k2, k3, k4)]
        t += h
    return y


print(f"Python {platform.python_version()}")
# (a) diferencias finitas
errs = []
for N in (10, 20, 40, 80):
    th = diferencias_finitas(N)
    e = max(abs(th[i] - exacta(i * L / N)) for i in range(N + 1))
    errs.append(e)
    print(f"(a) diferencias finitas N={N:3d}: error máximo = {e:.4e} K ; T(L/2) = {Ta + th[N//2]:.5f} K")
razones = [errs[i] / errs[i + 1] for i in range(3)]
print("    razones:", " ".join(f"{q:.3f}" for q in razones))
assert all(3.5 < q < 4.5 for q in razones)
print(f"    exacto T(L/2) = {Ta + exacta(L/2):.5f} K")

# (a) tiro lineal: theta(L; s) = A + B s con s = theta'(0)
f = lambda x, y: [y[1], m * m * y[0]]
A = rk4_sis(f, [th0, 0.0], 0, L, 200)[0]
B = rk4_sis(f, [th0, 1.0], 0, L, 200)[0] - A
s = (thL - A) / B
chk = rk4_sis(f, [th0, s], 0, L, 200)[0]
s_ex = (-th0 * m * math.cosh(m * L) + thL * m) / math.sinh(m * L)
print(f"(a) tiro lineal: theta'(0) = {s:.9f} K/m (exacto {s_ex:.9f}); theta(L) = {chk:.9f} (objetivo {thL})")
assert abs(s - s_ex) < 1e-6 and abs(chk - thL) < 1e-9

# (b) tiro no lineal
GM, R = 3.986004e14, 6.3781e6
Tf, h_obj = 300.0, 1.0e6
g = lambda t, y: [y[1], -GM / y[0] ** 2]


def r_final(v0, N=3000):
    return rk4_sis(g, [R, v0], 0, Tf, N)[0]


def secante(N):
    v1, v2 = 4500.0, 5000.0
    f1, f2 = r_final(v1, N) - (R + h_obj), r_final(v2, N) - (R + h_obj)
    for _ in range(50):
        v3 = v2 - f2 * (v2 - v1) / (f2 - f1)
        v1, f1, v2 = v2, f2, v3
        f2 = r_final(v2, N) - (R + h_obj)
        if abs(f2) < 1e-9:
            break
    return v2, f2


v0, res = secante(3000)
v0b, _ = secante(6000)
v_est = h_obj / Tf + 0.5 * (GM / R**2) * Tf
print(f"(b) tiro no lineal: v0 = {v0:.6f} m/s ; residuo r(T) - (R + h) = {res:.2e} m")
print(f"    con paso mitad: v0 = {v0b:.6f} m/s ; estimación con g constante: {v_est:.3f} m/s")
assert abs(res) < 1e-6 and abs(v0 - v0b) < 1e-6 and abs(v0 - v_est) / v0 < 0.1
print("Pruebas superadas.")
