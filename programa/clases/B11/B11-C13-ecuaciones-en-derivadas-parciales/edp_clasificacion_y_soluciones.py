#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C13: clasificación de EDP y comprobación de soluciones exactas.

Datos: placa SINTÉTICA de espesor L = 0.05 m y difusividad térmica
alpha = 1.0e-6 m2/s (orden de magnitud de un material aislante; valor de
ejemplo, no de un material concreto). Velocidad de advección c = 2.0 m/s (sintética).
Modelo: ecuaciones del calor u_t = alpha u_xx, de onda u_tt = c2 u_xx,
de Laplace u_xx + u_yy = 0 y de advección u_t + c u_x = 0, cada una con una
solución exacta por separación de variables o por traslación.
Método: residuo de la EDP con diferencias centrales de tres puntos (DLMF 3.4.6),
paso h pequeño, más clasificación por el discriminante B^2 - 4AC de
A u_xx + B u_xy + C u_yy.
Supuestos: funciones suaves. Validez: h ~ 1e-4 de la escala espacial.
Tolerancia: residuo relativo < 1e-5 en las soluciones correctas; el candidato
incorrecto debe dar residuo relativo > 1e-2 (la prueba debe poder fallar).
"""
import math, platform

alpha, L = 1.0e-6, 0.05
pi = math.pi


def d1(f, v, h):
    return (f(v + h) - f(v - h)) / (2 * h)


def d2(f, v, h):
    return (f(v + h) - 2 * f(v) + f(v - h)) / h**2


def clasifica(A, B, C):
    d = B * B - 4 * A * C
    return "hiperbólica" if d > 0 else ("parabólica" if d == 0 else "elíptica")


print(f"Python {platform.python_version()}")
print("Clasificación (A, B, C de A u_xx + B u_xy + C u_yy):")
for nombre, (A, B, C) in (("calor (u_t = a u_xx)", (1, 0, 0)), ("onda (u_tt = c2 u_xx)", (-1, 0, 1)), ("Laplace", (1, 0, 1))):
    print(f"  {nombre:24s} B^2-4AC = {B*B-4*A*C:+d} -> {clasifica(A, B, C)}")
assert clasifica(1, 0, 0) == "parabólica" and clasifica(-1, 0, 1) == "hiperbólica" and clasifica(1, 0, 1) == "elíptica"

# calor
u = lambda x, t: math.sin(pi * x / L) * math.exp(-alpha * pi**2 * t / L**2)
u_mal = lambda x, t: math.sin(pi * x / L) * math.exp(-alpha * pi * t / L**2)   # falta un pi
x0, t0 = 0.013, 80.0
ht, hx = 0.5, 1e-4
res = lambda U: d1(lambda t: U(x0, t), t0, ht) - alpha * d2(lambda x: U(x, t0), x0, hx)
escala = alpha * (pi / L) ** 2 * abs(u(x0, t0))
print(f"calor, solución correcta : residuo relativo = {abs(res(u))/escala:.2e}")
print(f"calor, candidato erróneo : residuo relativo = {abs(res(u_mal))/escala:.2e}")
assert abs(res(u)) / escala < 1e-5 and abs(res(u_mal)) / escala > 1e-2
print(f"  contorno u(0,t) = {u(0, 50.0):.1e}, u(L,t) = {u(L, 50.0):.1e}; u(L/2, 0) = {u(L/2, 0):.3f}")
tau = L**2 / (pi**2 * alpha)
print(f"  tiempo de difusión del modo fundamental tau = L^2/(pi^2 alpha) = {tau:.1f} s ; u(L/2, tau) = {u(L/2, tau):.5f} (1/e = {1/math.e:.5f})")
assert abs(u(L / 2, tau) - 1 / math.e) < 1e-12

# onda
c = 3.0
w = lambda x, t: math.sin(pi * x / L) * math.cos(c * pi * t / L)
resw = d2(lambda t: w(x0, t), 0.004, 1e-5) - c**2 * d2(lambda x: w(x, 0.004), x0, 1e-5)
escw = c**2 * (pi / L) ** 2
print(f"onda, residuo relativo   = {abs(resw)/escw:.2e}")
assert abs(resw) / escw < 1e-5

# Laplace
lap = lambda x, y: math.sin(pi * x / L) * math.sinh(pi * y / L)
reslap = d2(lambda x: lap(x, 0.02), 0.013, 1e-5) + d2(lambda y: lap(0.013, y), 0.02, 1e-5)
print(f"Laplace, residuo relativo= {abs(reslap)/((pi/L)**2*abs(lap(0.013, 0.02))):.2e}")
assert abs(reslap) / ((pi / L) ** 2 * abs(lap(0.013, 0.02))) < 1e-5

# advección
cc = 2.0
adv = lambda x, t: math.exp(-((x - cc * t) ** 2))
resa = d1(lambda t: adv(0.7, t), 0.3, 1e-5) + cc * d1(lambda x: adv(x, 0.3), 0.7, 1e-5)
print(f"advección, residuo abs   = {resa:.2e} (u_t = {d1(lambda t: adv(0.7, t), 0.3, 1e-5):+.5f})")
assert abs(resa) < 1e-8
print("Pruebas superadas.")
