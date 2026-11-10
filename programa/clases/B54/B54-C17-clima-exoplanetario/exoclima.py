#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C17: clima exoplanetario por temperatura de equilibrio e instalacion estelar.

Datos: S0 = 1361.0 W/m^2 y albedo/T_bb terrestres de la ficha NASA/NSSDC de la Tierra, sigma de NIST CODATA 2022 (consulta 2026-11-09);
limites de la zona habitable solar 0.99 UA (interno) y 1.70 UA (externo) del resumen de Kopparapu et al. (2013, ApJ, arXiv:1301.6674; solo se leyo el resumen).
El planeta, su estrella (luminosidad 0.05 L_sol) y sus albedos son SINTETICOS. Los limites solares NO se transfieren a otra estrella (en el articulo dependen de T_ef): aqui solo
se escala por luminosidad como ejemplo de MECANICA, no como resultado.
Modelo: S = S0 (L/L_sol)/d^2 ; Te = [S (1 - A) f /sigma]^(1/4) con f = 1/4 (redistribucion global), 1/2 (solo el hemisferio diurno redistribuye) o 1 (punto subsolar sin redistribucion).
Tolerancia: Te solar frente a 255.1 K (albedo 0.294) 0.05 K; invariancia S*d^2 1e-12.
"""
import math, platform
SIG, S0 = 5.670374419e-8, 1361.0
print(f"Python {platform.python_version()} (biblioteca estandar)")
def Te(S, A, f=0.25): return (S * (1 - A) * f / SIG) ** 0.25
t = Te(S0, 0.294)
print(f"Tierra: Te = {t:.2f} K")
assert abs(t - 255.12) < 0.05
Sin, Sout = S0 / 0.99 ** 2, S0 / 1.70 ** 2
print(f"Instalacion en 0.99 UA = {Sin:.1f} W/m2 = {Sin/S0:.3f} S_T ; en 1.70 UA = {Sout:.1f} W/m2 = {Sout/S0:.3f} S_T")
L = 0.05
print("Planeta sintetico alrededor de una estrella de L = 0.05 L_sol:")
print(" d [UA]   S/S_T   Te f=1/4 [K]   Te f=1/2 [K]  Te subsolar [K]")
for d in (0.10, 0.15, 0.20, 0.30):
    S = S0 * L / d ** 2
    assert math.isclose(S * d ** 2, S0 * L, rel_tol=1e-12)
    print(f"{d:6.2f} {S/S0:8.3f} {Te(S,0.3):13.1f} {Te(S,0.3,0.5):13.1f} {Te(S,0.3,1.0):15.1f}")
# distancias donde S iguala las instalaciones solares (ejemplo de mecanica)
for nombre, Sx in (("interna", Sin), ("externa", Sout)):
    d = math.sqrt(S0 * L / Sx)
    print(f"Distancia con instalacion '{nombre}' solar para L = 0.05: {d:.3f} UA")
# sensibilidad: duplicar la distancia reduce Te en 2^(-1/2)
assert math.isclose(Te(S0 * L / 0.4 ** 2, 0.3) / Te(S0 * L / 0.2 ** 2, 0.3), 2 ** -0.5, rel_tol=1e-12)
# bloqueo de marea: razon dayside/global
print(f"Razon Te(f=1/2)/Te(f=1/4) = {2**0.25:.4f} ; Te(f=1)/Te(f=1/4) = {4**0.25:.4f}")
print("Pruebas superadas.")
