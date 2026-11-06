#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C22: métodos implícitos en un problema rígido no lineal con solución conocida.

Datos SINTÉTICOS (solución fabricada): y*(t) = 2 + cos t es la solución exacta de
y' = y*'(t) - k (y^3 - y*(t)^3), k = 1000 1/s (relajación muy rápida hacia y*).
El jacobiano df/dy = -3 k y^2 vale entre -3e3 y -2.7e4 1/s para y entre 1 y 3.
Modelo: problema rígido escalar; condición inicial y(0) = 3 (sobre la solución lenta)
para medir órdenes, y y(0) = 3.5 (con transitorio) para comparar el amortiguamiento.
Métodos: Euler implícito (orden 1), BDF2 (orden 2; primer paso con Euler implícito),
regla trapezoidal (orden 2, A-estable pero no L-estable) y RK4 explícito; cada paso
implícito se resuelve con Newton con jacobiano analítico (tolerancia 1e-13).
Supuestos: escalar, f suave. Validez: Newton converge desde la predicción anterior.
Tolerancia: orden observado de Euler implícito en [0.9, 1.15]; de BDF2 y trapezoidal
en [1.85, 2.2]; RK4 explícito con h = 0.01 debe divergir (|y| > 1e6); con la
condición y(0) = 3.5 el amortiguamiento de BDF2 debe superar al del trapezoidal.
"""
import math, platform

k = 1000.0
ys = lambda t: 2 + math.cos(t)
dys = lambda t: -math.sin(t)
f = lambda t, y: dys(t) - k * (y**3 - ys(t) ** 3)
fy = lambda t, y: -3 * k * y * y


def newton(g, dg, x0, tol=1e-13):
    x = x0
    for it in range(1, 50):
        dx = g(x) / dg(x)
        x -= dx
        if abs(dx) < tol * max(1.0, abs(x)):
            return x, it
    raise RuntimeError("Newton no converge")


def euler_impl(h, N, y0):
    y, t, its = y0, 0.0, 0
    for _ in range(N):
        tn = t + h
        y, it = newton(lambda z: z - y - h * f(tn, z), lambda z: 1 - h * fy(tn, z), y)
        t, its = tn, its + it
    return y, its / N


def bdf2(h, N, y0, traza=None):
    yprev = y0
    y, _ = newton(lambda z: z - yprev - h * f(h, z), lambda z: 1 - h * fy(h, z), yprev)
    t = h
    its = 0
    for _ in range(N - 1):
        tn = t + h
        a, b = y, yprev
        y_new, it = newton(lambda z: z - (4 * a - b) / 3 - (2 * h / 3) * f(tn, z),
                           lambda z: 1 - (2 * h / 3) * fy(tn, z), y)
        yprev, y, t = y, y_new, tn
        its += it
        if traza is not None:
            traza.append(abs(y - ys(t)))
    return y, its / max(1, N - 1)


def trapezoidal(h, N, y0, traza=None):
    y, t, its = y0, 0.0, 0
    for _ in range(N):
        tn = t + h
        fo = f(t, y)
        y, it = newton(lambda z: z - y - 0.5 * h * (fo + f(tn, z)), lambda z: 1 - 0.5 * h * fy(tn, z), y)
        t, its = tn, its + it
        if traza is not None:
            traza.append(abs(y - ys(t)))
    return y, its / N


def rk4_explicito(h, N, y0):
    y, t = y0, 0.0
    for _ in range(N):
        k1 = f(t, y); k2 = f(t + h / 2, y + h / 2 * k1); k3 = f(t + h / 2, y + h / 2 * k2); k4 = f(t + h, y + h * k3)
        y += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += h
        if abs(y) > 1e12:
            return float("inf")
    return y


print(f"Python {platform.python_version()}")
tf = 2.0
print(f"y*(2) = {ys(tf):.12f}; |J| entre {3*k:.0f} y {27*k:.0f} 1/s; h = 0.01 -> h|J| = {0.01*3*k:.0f} a {0.01*27*k:.0f}")
ords = {}
for nombre, met in (("Euler implícito", euler_impl), ("BDF2", bdf2), ("trapezoidal", trapezoidal)):
    errs, its_ = [], []
    for N in (100, 200, 400, 800):
        y, its = met(tf / N, N, ys(0.0))
        errs.append(abs(y - ys(tf))); its_.append(its)
    p = [math.log2(errs[i] / errs[i + 1]) for i in range(3)]
    ords[nombre] = p
    print(f"{nombre:16s} errores (N=100..800): " + " ".join(f"{e:.3e}" for e in errs) + " | órdenes " + " ".join(f"{q:.2f}" for q in p) + f" | Newton {its_[0]:.1f} it/paso")
assert 0.9 < ords["Euler implícito"][-1] < 1.15
assert 1.85 < ords["BDF2"][-1] < 2.2 and 1.85 < ords["trapezoidal"][-1] < 2.2
yr = rk4_explicito(0.01, 200, ys(0.0))
print(f"RK4 explícito con h = 0.01: y(2) = {yr} (divergió)")
assert yr == float("inf") or abs(yr) > 1e6
# límite de estabilidad explícito: h < 2.785/|J|max
print(f"límite explícito aproximado de RK4: h < {2.785/(27*k):.2e} s -> {math.ceil(tf/(2.785/(27*k)))} pasos para llegar a t = 2")

# transitorio: y(0) = 3.5, h = 0.01
tb, tt = [], []
bdf2(0.01, 200, 3.5, tb)
trapezoidal(0.01, 200, 3.5, tt)
yb, _ = euler_impl(0.01, 200, 3.5)
print(f"transitorio (y0 = 3.5, h = 0.01): Euler implícito |y - y*| en t=2: {abs(yb - ys(tf)):.2e}")
print(f"  BDF2: máx|y - y*| en la mitad final = {max(tb[100:]):.2e} ; trapezoidal: {max(tt[100:]):.2e}")
assert max(tb[100:]) < max(tt[100:])
print("Pruebas superadas.")
