#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B11-C01: ¿una función dada es solución de una ecuación diferencial?

Datos: GM de la Tierra = 3.986004e14 m3/s2 y radio ecuatorial 6.3781e6 m
(valores nominales de la Resolución B3 de la IAU, 2015). Altitud 400 km: dato
ILUSTRATIVO (no es una misión concreta). Constantes k, w: SINTÉTICAS.
Modelo: se evalúa el RESIDUO de cada ecuación, (lado izquierdo) - (lado
derecho), sustituyendo la solución candidata; la derivada se aproxima con
cociente central (DLMF 3.4.6 con t = 0).
Supuestos: funciones suaves; derivada segunda con diferencia central de 3 puntos.
Validez: h ~ 1e-3 para escalas de tiempo ~1 (h = 1 s para la órbita).
Tolerancia: residuo relativo < 1e-5 para soluciones correctas; un candidato
incorrecto debe producir residuo relativo > 1e-2 (la prueba debe poder fallar).
"""
import math, platform


def d1(f, t, h):
    return (f(t + h) - f(t - h)) / (2 * h)


def d2(f, t, h):
    return (f(t + h) - 2 * f(t) + f(t - h)) / h**2


GM, RE = 3.986004e14, 6.3781e6
a = RE + 400e3
n = math.sqrt(GM / a**3)                      # movimiento medio, rad/s
k, w = 0.3, 2.0


def res_decaimiento(t):
    return d1(lambda s: 5 * math.exp(-k * s), t, 1e-3) + k * 5 * math.exp(-k * t)


def res_oscilador(t):
    return d2(lambda s: math.cos(w * s), t, 1e-3) + w**2 * math.cos(w * t)


def res_orbita(t):
    x = lambda s: a * math.cos(n * s)
    return d2(x, t, 1.0) + GM * x(t) / a**3


def res_incorrecto(t):
    return d2(lambda s: math.cos(3 * s), t, 1e-3) + 4 * math.cos(3 * t)


casos = [
    ("y' = -k y ; y = 5 exp(-k t)", res_decaimiento, k * 5 * math.exp(-k * 2.0), 2.0, True),
    ("y'' + w^2 y = 0 ; y = cos(w t)", res_oscilador, w**2, 1.3, True),
    ("orbita circular x'' = -GM x/r^3", res_orbita, GM / a**2, 1234.0, True),
    ("INCORRECTO y = cos(3t), y''+4y=0", res_incorrecto, 4.0, 1.3, False),
]

print(f"Python {platform.python_version()}")
for nombre, res, escala, t, debe_ser_solucion in casos:
    r = res(t)
    rel = abs(r) / escala
    print(f"{nombre:34s} residuo = {r: .3e}  relativo = {rel:.2e}")
    if debe_ser_solucion:
        assert rel < 1e-5, f"residuo demasiado grande en {nombre}"
    else:
        assert rel > 1e-2, "la prueba no detecta el candidato incorrecto"
print(f"a = {a/1e3:.1f} km; n = {n:.6e} rad/s; periodo = {2*math.pi/n:.1f} s = {2*math.pi/n/60:.2f} min")
print("Pruebas superadas.")
