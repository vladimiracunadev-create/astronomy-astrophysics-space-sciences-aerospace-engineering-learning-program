#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C04: de la ecuación de segundo orden al sistema de primer orden.

Datos: GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m
(valores nominales IAU 2015, Res. B3). Altitud 400 km: dato ILUSTRATIVO.
Modelo: r'' = -GM r/|r|^3 en el plano, reducido al vector de estado
s = (x, y, vx, vy) con s' = F(s). Solución exacta de la órbita circular:
x = a cos(n t), y = a sin(n t), n = sqrt(GM/a^3).
Comprobaciones: (1) el campo F evaluado en la solución exacta coincide con la
derivada numérica de la solución; (2) la energía específica y el momento
angular específico son constantes sobre la solución; (3) un oscilador lineal
x' = A x tiene valores propios +-i w (periodo 2 pi / w).
Supuestos: dos cuerpos, masa del satélite despreciable, plano inercial.
Validez: sin atmósfera ni achatamiento. Tolerancia: 1e-7 relativa (derivada
numérica con h = 0.5 s); 1e-12 para las constantes del movimiento.
"""
import math, platform

GM, RE = 3.986004e14, 6.3781e6
a = RE + 400e3
n = math.sqrt(GM / a**3)


def F(s):
    x, y, vx, vy = s
    r3 = (x * x + y * y) ** 1.5
    return (vx, vy, -GM * x / r3, -GM * y / r3)


def exacta(t):
    return (a * math.cos(n * t), a * math.sin(n * t), -a * n * math.sin(n * t), a * n * math.cos(n * t))


t, h = 1500.0, 0.5
num = [(p - q) / (2 * h) for p, q in zip(exacta(t + h), exacta(t - h))]
cam = F(exacta(t))
maxrel = max(abs(u - v) / max(abs(v), 1e-30) for u, v in zip(num, cam))
print(f"derivada numerica vs F(s): error relativo maximo = {maxrel:.2e}")
assert maxrel < 1e-7

def eps_h(s):
    x, y, vx, vy = s
    return 0.5 * (vx * vx + vy * vy) - GM / math.hypot(x, y), x * vy - y * vx

e0, h0 = eps_h(exacta(0.0))
for tt in (0.0, 1000.0, 3000.0, 5553.6):
    e, hh = eps_h(exacta(tt))
    assert abs(e - e0) / abs(e0) < 1e-12 and abs(hh - h0) / abs(h0) < 1e-12
print(f"energia especifica = {e0:.6e} J/kg;  h = {h0:.6e} m2/s  (constantes sobre la solucion)")

# oscilador: x'' = -w^2 x  ->  A = [[0,1],[-w^2,0]] ; polinomio caracteristico l^2 + w^2 = 0
w = 2.0
tr, det = 0.0, w * w
disc = tr * tr - 4 * det
lam = complex(tr / 2, math.sqrt(-disc) / 2)
print(f"oscilador w = {w}: valores propios {lam} y {lam.conjugate()}; periodo {2*math.pi/abs(lam.imag):.6f}")
assert abs(lam.imag - w) < 1e-12
v = math.sqrt(GM / a)
print(f"a = {a/1e3:.1f} km, v circular = {v:.2f} m/s, periodo = {2*math.pi/n:.1f} s, vector de estado inicial = {exacta(0.0)}")
print(f"Python {platform.python_version()}")
print("Pruebas superadas.")
