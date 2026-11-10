#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C03: temperatura de equilibrio radiativo.

Datos: irradiancia solar S, albedo de Bond A y temperatura de cuerpo negro de las fichas NASA/NSSDC (consulta 2026-11-09);
sigma de Stefan-Boltzmann de NIST CODATA 2022 (5.670374419e-8 W m^-2 K^-4, exacta).
Modelo: Te = [S (1 - A) / (4 sigma)]^(1/4) (esfera isoterma que redistribuye toda la energia). Supuestos: emisividad 1, sin atmosfera ni calor interno.
Validez: cuerpo de rotacion rapida o buen redistribuidor. Tolerancia: Te frente a la T de cuerpo negro de la ficha, 0.3 K (Venus, Marte, Jupiter); en la Tierra la ficha no es autoconsistente con su albedo y se admite 1.5 K, informando la diferencia.
"""
import math, platform
SIG = 5.670374419e-8
F = {  # S [W/m2], A, T_bb de la ficha [K], T superficie/1 bar medida [K]
    "Venus": (2601.3, 0.77, 226.6, 737.0), "Tierra": (1361.0, 0.294, 254.0, 288.0),
    "Marte": (586.2, 0.250, 209.8, 214.0), "Jupiter": (50.26, 0.343, 109.9, 165.0)}
print(f"Python {platform.python_version()} (biblioteca estandar)")
print("planeta   Te calc [K]   T_bb ficha [K]   dif [K]   T observada [K]   Delta = T_obs - Te [K]")
for n, (S, A, Tf, To) in F.items():
    Te = (S * (1 - A) / (4 * SIG)) ** 0.25
    tol = 1.5 if n == 'Tierra' else 0.3  # la ficha terrestre no usa el mismo albedo que lista (ver A implicito abajo)
    assert abs(Te - Tf) < tol, (n, Te, Tf)
    print(f"{n:8s} {Te:11.2f} {Tf:15.1f} {Te-Tf:9.2f} {To:15.1f} {To-Te:20.1f}")
# albedo implicito en la T_bb de la ficha terrestre
S_, A_, Tf_, _ = F['Tierra']
A_imp = 1 - 4 * SIG * Tf_ ** 4 / S_
print(f"Albedo implicito en T_bb = {Tf_} K para la Tierra: {A_imp:.3f} (la ficha lista A = {A_})")
# prueba analitica: balance de potencias absorbida = emitida
S, A = F["Tierra"][:2]
Te = (S * (1 - A) / (4 * SIG)) ** 0.25
absorbida = S * (1 - A) * math.pi / 1.0   # por R^2
emitida = 4 * math.pi * SIG * Te ** 4
assert abs(absorbida - emitida) / emitida < 1e-12
print(f"Balance Tierra: absorbida {S*(1-A)/4:.3f} W/m2 = emitida {SIG*Te**4:.3f} W/m2 (por unidad de superficie)")
# sensibilidad: dTe/dA y dTe/dS
dA = 0.01; dT = (S * (1 - A - dA) / (4 * SIG)) ** 0.25 - Te
print(f"Sensibilidad: +0.01 de albedo baja Te en {-dT:.3f} K (analitica {Te*dA/(4*(1-A)):.3f} K)")
assert abs(-dT - Te * dA / (4 * (1 - A))) < 0.01
# sin redistribucion (lado diurno, subsolar)
Tsub = (S * (1 - A) / SIG) ** 0.25
print(f"Punto subsolar sin redistribucion (limite): {Tsub:.1f} K (= sqrt(2) veces Te)")
print("Pruebas superadas.")
