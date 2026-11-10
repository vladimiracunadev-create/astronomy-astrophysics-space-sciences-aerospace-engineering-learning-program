#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C12: insolacion, ley del inverso del cuadrado y atenuacion de Beer-Lambert.

Datos: irradiancia solar a 1 UA (1361.0 W/m^2) y semiejes mayores de las fichas NASA/NSSDC (consulta 2026-11-09); irradiancias de Venus (2601.3) y Marte (586.2)
de las mismas fichas se usan como referencia independiente. Opacidades tau: SINTETICAS e ILUSTRATIVAS.
Modelo: S(d) = S0 / d^2 (d en UA); transmision T = exp(-tau/mu), mu = cos(chi); insolacion diaria media Q = (S/pi)(h0 sin(phi) sin(delta) + cos(phi) cos(delta) sin(h0)).
Supuestos: orbita circular al semieje, sin refraccion, atmosfera plano-paralela. Tolerancia: S de Venus y Marte frente a la ficha 0.1 %; Q ecuatorial equinoccial frente a S/pi 1e-12.
"""
import math, platform
S0 = 1361.0
A = {"Venus": (0.72333199, 2601.3), "Tierra": (1.0, 1361.0), "Marte": (1.52366231, 586.2)}
print(f"Python {platform.python_version()} (biblioteca estandar)")
for n, (a, Sf) in A.items():
    S = S0 / a ** 2
    d = abs(S - Sf) / Sf
    print(f"{n:7s} a = {a:.8f} UA: S = {S:8.2f} W/m2 (ficha {Sf}; dif. {d*100:.3f} %)")
    assert d < 1e-3, n
def Q(S, lat, dec):
    ph, de = math.radians(lat), math.radians(dec)
    x = -math.tan(ph) * math.tan(de)
    h0 = math.pi if x <= -1 else (0.0 if x >= 1 else math.acos(x))
    return S / math.pi * (h0 * math.sin(ph) * math.sin(de) + math.cos(ph) * math.cos(de) * math.sin(h0))
assert math.isclose(Q(S0, 0.0, 0.0), S0 / math.pi, rel_tol=1e-12)
assert math.isclose(Q(S0, 90.0, 0.0), 0.0, abs_tol=1e-9)
print("Insolacion diaria media Q [W/m2] (S = 1361, Tierra, declinacion 0 y +23.44 grados):")
for lat in (0, 30, 60, 90):
    print(f"  lat {lat:2d}: equinoccio {Q(S0, lat, 0.0):7.2f}   solsticio {Q(S0, lat, 23.44):7.2f}")
# Beer-Lambert: integracion numerica de dI/ds = -k I frente a exp(-tau)
tau, chi = 0.3, 60.0
mu = math.cos(math.radians(chi))
n = 100000; I = 1.0; h = tau / mu / n
for _ in range(n):
    I -= I * h
print(f"Beer-Lambert (tau = {tau}, chi = {chi} grados): numerico = {I:.6f} ; analitico = {math.exp(-tau/mu):.6f}")
assert abs(I - math.exp(-tau / mu)) < 1e-4
print("tau   chi   transmision   fraccion absorbida")
for t, c in [(0.1, 0), (0.1, 60), (1.0, 0), (1.0, 60), (5.0, 0)]:
    T = math.exp(-t / math.cos(math.radians(c)))
    print(f"{t:4.1f} {c:5d} {T:12.4f} {1-T:14.4f}")
print("Pruebas superadas.")
