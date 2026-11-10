#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C14: piso de ruido termico y desensibilizacion de un receptor por interferencia (SINTETICO).

N = k T B (k = 1.380649e-23 J/K, exacta por definicion, NIST CODATA 2022, consultada 2026-11-10). Interferencia I: la sensibilidad
se degrada 10 log10(1 + I/N). Aislamiento requerido para I/N <= -6 dB entre un armonico del transmisor y el receptor. Atenuacion de
espacio libre FSPL = 20 log10(4 pi d / lambda). Comprobacion: potencia de ruido gaussiano simulada. Unidades: W, dBm, dB, Hz, K, m.
Tolerancias: Monte Carlo frente a kTB 1 %.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: receptor de 435 MHz, B = 10 kHz, T_sis = 500 K, transmisor de 1 W en el mismo satelite")
k = 1.380649e-23
T, B = 500.0, 10e3
N = k * T * B
dbm = lambda p: 10 * math.log10(p / 1e-3)
print(f"k = {k:.6e} J/K ; N = k T B = {N:.4e} W = {dbm(N):.2f} dBm")
print("Piso de ruido -174 dBm/Hz a 290 K =", f"{dbm(k * 290):.2f} dBm/Hz ; N a 290 K y 10 kHz = {dbm(k * 290 * B):.2f} dBm")
comprobar(abs(dbm(k * 290) + 173.98) < 0.02, "el piso de ruido a 290 K debe ser -174 dBm/Hz")

rng = np.random.default_rng(90)
R = 50.0
n = 4_000_000
v = rng.normal(0, math.sqrt(N * R), n)
Pm = float(np.mean(v**2) / R)
print(f"Monte Carlo (4e6 muestras): potencia media = {Pm:.4e} W ; diferencia con kTB = {abs(Pm - N) / N * 100:.3f} %")
comprobar(abs(Pm - N) / N < 0.01, "el ruido simulado debe tener potencia kTB")

I_dbm = -110.0
I = 1e-3 * 10 ** (I_dbm / 10)
print(f"Interferencia en la entrada = {I_dbm} dBm ; I/N = {dbm(I) - dbm(N):.2f} dB")
des = 10 * math.log10(1 + I / N)
print(f"Desensibilizacion = 10 log10(1 + I/N) = {des:.2f} dB")
margen = 6.0
print(f"Margen de enlace de ejemplo = {margen} dB -> con interferencia = {margen - des:.2f} dB ({'FALLA' if margen - des < 0 else 'CUMPLE'})")
comprobar(margen - des < 0, "la interferencia de ejemplo debe consumir el margen")
print("I/N [dB] -> desensibilizacion [dB]")
for x in (-20, -10, -6, 0, 10, 20):
    print(f"   {x:4d} -> {10 * math.log10(1 + 10 ** (x / 10)):6.2f}")
comprobar(abs(10 * math.log10(1 + 10 ** (-6 / 10)) - 0.97) < 0.01, "a I/N = -6 dB la desensibilizacion es cerca de 1 dB")

# Aislamiento requerido: armonico del transmisor
Ptx = 30.0                               # dBm
supresion = 60.0                         # dBc del armonico
P_arm = Ptx - supresion
N_dbm = dbm(N)
req = P_arm - (N_dbm - 6.0)
print(f"Armonico del transmisor = {P_arm:.0f} dBm ; aislamiento requerido para I/N = -6 dB: {req:.1f} dB")
lam = 299792458.0 / 435e6
for d in (0.1, 0.3, 1.0):
    fspl = 20 * math.log10(4 * math.pi * d / lam)
    print(f"   FSPL a {d} m = {fspl:6.1f} dB (lambda = {lam:.3f} m) -> faltan {req - fspl:6.1f} dB de filtrado/blindaje")
comprobar(req > 80, "el aislamiento requerido de ejemplo debe ser mayor que 80 dB")
fin()
