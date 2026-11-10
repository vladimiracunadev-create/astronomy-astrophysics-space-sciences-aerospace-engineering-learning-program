#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C13: margen de emisiones conducidas frente a un limite SINTETICO, en dBuV, con incertidumbre de medida.

Emisiones de un convertidor conmutado (armonicos de 100 kHz) y una espuria. Limite sintetico: 94 dBuV hasta 100 kHz y descenso
de 20 dB/decada. Margen = L - E - U, U = incertidumbre de medida sintetica de 3 dB. Suma de fuentes: incoherente (potencia) y
coherente (peor caso). Conversion dBuV -> dBm en 50 ohm comprobada con P = V^2/R. Unidades: Hz, dBuV, dBm, V. Tolerancia: 1e-9 dB.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: armonicos de 100 kHz, limite de ejemplo, U = 3 dB")
U = 3.0

def limite(f):
    return 94.0 if f <= 1e5 else 94.0 - 20 * math.log10(f / 1e5)

def emision(k):
    base = 80.0 - 20 * math.log10(k)                 # armonico k de 100 kHz decae 20 dB/decada
    if k == 4:
        base += 9.0                                   # espuria de 400 kHz (resonancia del filtro, sintetica)
    return base

print("f [kHz]   E [dBuV]   L [dBuV]   margen = L - E - U [dB]")
filas = []
for k in range(1, 11):
    f = k * 1e5
    E, L = emision(k), limite(f)
    m = L - E - U
    filas.append((f, E, L, m))
    print(f"{f / 1e3:7.0f}   {E:8.2f}   {L:8.2f}   {m:8.2f}  {'' if m >= 6 else ('(margen < 6 dB)' if m >= 0 else '(EXCEDE)')}")
peor = min(filas, key=lambda r: r[3])
print(f"Margen peor = {peor[3]:.2f} dB en {peor[0] / 1e3:.0f} kHz")
comprobar(all(r[3] >= 0 for r in filas), "ningun armonico debe exceder el limite de ejemplo")
comprobar(peor[0] == 4e5, "el peor margen debe estar en la espuria de 400 kHz")

# dBuV -> V -> dBm en 50 ohm
def dbuv_a_dbm(x):
    return x - 107.0                                 # relacion para 50 ohm

for x in (60.0, 80.0, 94.0):
    V = 1e-6 * 10 ** (x / 20)
    P = V**2 / 50.0
    dbm = 10 * math.log10(P / 1e-3)
    print(f"{x:5.1f} dBuV = {V * 1e3:9.4f} mV = {P * 1e9:10.4f} nW = {dbm:7.3f} dBm (formula {dbuv_a_dbm(x):7.3f})")
    comprobar(abs(dbm - dbuv_a_dbm(x)) < 0.02, "la conversion a dBm debe coincidir a 0.02 dB")

# Suma de dos fuentes de 70 dBuV
a = b = 70.0
Vi = math.sqrt((10 ** (a / 20)) ** 2 + (10 ** (b / 20)) ** 2)
Vc = 10 ** (a / 20) + 10 ** (b / 20)
print(f"Dos fuentes de 70 dBuV: suma incoherente = {20 * math.log10(Vi):.3f} dBuV (+3.01 dB) ; suma coherente = {20 * math.log10(Vc):.3f} dBuV (+6.02 dB)")
comprobar(abs(20 * math.log10(Vi) - 73.0103) < 1e-3 and abs(20 * math.log10(Vc) - 76.0206) < 1e-3, "las sumas deben dar +3.01 y +6.02 dB")
# Monte Carlo de fases aleatorias: el promedio de potencia coincide con la suma incoherente
rng = np.random.default_rng(90)
ph = rng.uniform(0, 2 * np.pi, 1_000_000)
v = np.abs(1 + np.exp(1j * ph))
print(f"Fases aleatorias (Monte Carlo): potencia media = {np.mean(v**2):.4f} (incoherente 2.0000) ; maximo = {v.max():.4f} (coherente 2.0000)")
comprobar(abs(np.mean(v**2) - 2.0) < 0.01, "la potencia media con fases aleatorias debe ser la incoherente")
print("Efecto de la incertidumbre: margen minimo con U = 0, 3, 6 dB")
for u in (0.0, 3.0, 6.0):
    print(f"   U = {u:3.1f} dB -> margen peor = {min(r[2] - r[1] for r in filas) - u:.2f} dB")
fin()
