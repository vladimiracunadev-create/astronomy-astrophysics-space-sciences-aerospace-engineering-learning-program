#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C07: energia convectiva disponible (CAPE) y velocidad maxima de corriente ascendente.

Datos: g = 9.820 m/s^2 (ficha NASA/NSSDC de la Tierra, consulta 2026-11-09). Sondeo de temperatura virtual: SINTETICO (no es una observacion).
Modelo: CAPE = integral de g (Tp - Te)/Te dz entre el nivel de conveccion libre y el de equilibrio (regla del trapecio); w_max = sqrt(2 CAPE) (sin arrastre
ni carga de hidrometeoros: COTA SUPERIOR). Supuestos: parcela no mezclada. Validez: ilustrativa, no pronostica tormentas.
Tolerancia: CAPE numerica frente a la analitica de una diferencia de temperatura constante, 1e-9 relativo.
"""
import math, platform
G = 9.820
print(f"Python {platform.python_version()} (biblioteca estandar)")

def cape(zs, Tp, Te):
    c = 0.0
    for i in range(len(zs) - 1):
        b0 = G * (Tp[i] - Te[i]) / Te[i]; b1 = G * (Tp[i+1] - Te[i+1]) / Te[i+1]
        dz = zs[i+1] - zs[i]
        if b0 > 0 and b1 > 0: c += 0.5 * (b0 + b1) * dz
    return c

# prueba analitica: exceso constante dT = 2 K sobre Te = 280 K entre 2 y 10 km
c_an = G * 2.0 / 280.0 * 8000.0
zs2 = [2000.0 + i * 100.0 for i in range(81)]
c_num = cape(zs2, [282.0] * 81, [280.0] * 81)
print(f"Prueba: CAPE constante = {c_num:.4f} J/kg ; analitica g dT/T H = {c_an:.4f} J/kg")
assert abs(c_num - c_an) / c_an < 1e-9
# sondeo sintetico: ambiente con gradiente 6.5 K/km; parcela seca 9.8 K/km hasta saturar a 1.5 km y luego 5 K/km
zs = [i * 250.0 for i in range(0, 49)]  # 0-12 km
Tp = []
for z in zs:
    Tp.append(303.0 - 9.8e-3 * z if z <= 1500 else 303.0 - 9.8e-3 * 1500 - 5.0e-3 * (z - 1500))
# ambiente con isotermia por encima de 11 km (tropopausa sintetica)
Te = [300.0 - 6.5e-3 * min(z, 11000.0) for z in zs]
c = cape(zs, Tp, Te)
print(f"Sondeo sintetico: CAPE = {c:.1f} J/kg ; w_max (cota) = {math.sqrt(2*c):.1f} m/s")
for rho_nombre, cape_v in [("debil", 500.0), ("moderada", 1500.0), ("fuerte", 3000.0)]:
    print(f"  CAPE {cape_v:6.0f} J/kg ({rho_nombre}): w_max = {math.sqrt(2*cape_v):5.1f} m/s")
# tiempo de ascenso a 10 km con w medio = 0.5 w_max
print(f"Tiempo de ascenso a 10 km con 0.5 w_max: {10000/(0.5*math.sqrt(2*c))/60:.1f} min")
assert c > 0
print("Pruebas superadas.")
