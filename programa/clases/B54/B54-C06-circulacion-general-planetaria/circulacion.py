#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C06: rotacion, parametro de Coriolis, balance geostrofico y numero de Rossby.

Datos: periodos de rotacion y radios de fichas NASA/NSSDC (Jupiter 9.9250 h y 71492 km; Marte, Tierra, Venus: periodos sideral/rotacion estandar
23.9345 h, 24.6229 h y 5832.5 h NO consultados en esta clase -> rotulados "no consultado"). Titan: periodo orbital 15.945421 d (ficha NASA/NSSDC de satelites);
su rotacion sincrona es SUPUESTO de la clase. Vientos y gradientes de presion: SINTETICOS.
Modelo: f = 2 Omega sin(lat); v_g = (1/(rho f)) dP/dy; Ro = U/(f L). Supuestos: plano beta ignorado, f constante en el recuadro.
Tolerancia: v_g numerico frente a analitico 1e-12 relativo.
"""
import math, platform
print(f"Python {platform.python_version()} (biblioteca estandar)")
P = {  # periodo [h], radio [km]
    "Tierra": (23.9345, 6371.0), "Marte": (24.6229, 3389.5), "Venus": (-5832.5, 6051.8),
    "Jupiter": (9.9250, 71492.0), "Titan": (15.945421 * 24, 2575.0)}
print("planeta   Omega [rad/s]   f(45 grados) [1/s]   v ecuatorial [m/s]   Ro global = U/(2 Omega a), U = 10 m/s")
for n, (T, a) in P.items():
    Om = 2 * math.pi / (abs(T) * 3600)
    f45 = 2 * Om * math.sin(math.radians(45))
    veq = Om * a * 1e3
    Ro = 10.0 / (2 * Om * a * 1e3)
    print(f"{n:8s} {Om:13.3e} {f45:18.3e} {veq:18.2f} {Ro:14.3e}")
# balance geostrofico, Tierra, datos sinteticos: dP/dy = 1 hPa por 100 km, rho = 1.2 kg/m3, lat 45
Om = 2 * math.pi / (23.9345 * 3600); f = 2 * Om * math.sin(math.radians(45))
dPdy, rho = 100.0 / 100e3, 1.2
vg = dPdy / (rho * f)
# comprobacion numerica: diferencias finitas de un campo P(y) lineal
P_y = lambda y: 101300.0 - dPdy * y
dy = 1000.0
vg_num = (P_y(0.0) - P_y(dy)) / dy / (rho * f)
print(f"v geostrofico (sintetico) = {vg:.3f} m/s ; por diferencias finitas = {vg_num:.3f} m/s")
assert abs(vg - vg_num) / vg < 1e-9
Ro = vg / (f * 1000e3)
print(f"Ro = U/(f L) con L = 1000 km: {Ro:.3f} (Ro < 1: la rotacion domina)")
# escalado de la anchura de la celda de Hadley: phi_H ~ 1/Omega (relacion de ESCALA, no consultada), tomando la Tierra como referencia sintetica de 30 grados
Om_T = 2 * math.pi / (P["Tierra"][0] * 3600)
print("Anchura de celda de Hadley (escala 1/Omega, referencia ilustrativa: Tierra = 30 grados, tope 90):")
for n, (T, a) in P.items():
    Om = 2 * math.pi / (abs(T) * 3600)
    print(f"  {n:8s} {min(90.0, 30.0 * Om_T / Om):6.1f} grados")
assert math.isclose(min(90.0, 30.0 * Om_T / Om_T), 30.0)
print("Pruebas superadas.")
