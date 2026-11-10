#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C10: espectro de respuesta al choque (SRS) de un pulso semisenoidal SINTETICO.

SRS de aceleracion absoluta de un resonador de un grado de libertad (Q = 10) excitado en su base: z'' + 2 zeta w z' + w^2 z = -a(t),
absoluta = 2 zeta w z' + w^2 z. Integracion RK4. Pulso: a(t) = A sin(pi t / T), 0 <= t <= T, con A = 200 g y T = 1 ms.
Comprobaciones independientes: a baja frecuencia SRS ~ w DV con DV = 2 A T / pi (cambio de velocidad del pulso); a alta frecuencia SRS -> ~A.
Unidades: Hz, g, s, m/s. Tolerancias: baja frecuencia 5 %, alta frecuencia dentro de [A, 1.2 A].
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: semisenoidal de 200 g y 1 ms; resonador de Q = 10")
G0 = 9.80665
A, T = 200.0, 1.0e-3
Q = 10.0
zeta = 1 / (2 * Q)

def pulso(t):
    return A * G0 * math.sin(math.pi * t / T) if 0 <= t <= T else 0.0

def srs_punto(fn):
    w = 2 * math.pi * fn
    dt = min(1 / (fn * 200), T / 400)
    t_fin = T + 3 / fn + 5 / (zeta * w) * 0.2
    n = int(t_fin / dt)
    z, v = 0.0, 0.0
    pico = 0.0
    def f(t, z, v):
        return v, -pulso(t) - 2 * zeta * w * v - w * w * z
    t = 0.0
    for _ in range(n):
        k1 = f(t, z, v)
        k2 = f(t + dt / 2, z + dt / 2 * k1[0], v + dt / 2 * k1[1])
        k3 = f(t + dt / 2, z + dt / 2 * k2[0], v + dt / 2 * k2[1])
        k4 = f(t + dt, z + dt * k3[0], v + dt * k3[1])
        z += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        v += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        t += dt
        pico = max(pico, abs(2 * zeta * w * v + w * w * z))
    return pico / G0

DV = 2 * A * G0 * T / math.pi
print(f"Cambio de velocidad del pulso DV = 2 A T / pi = {DV:.4f} m/s")
fr = [10, 20, 50, 100, 200, 400, 800, 1000, 2000, 5000, 10000]
srs = {}
print("fn [Hz]   SRS [g]   SRS/A   w DV [g] (asintota baja)")
for fn in fr:
    srs[fn] = srs_punto(fn)
    asint = 2 * math.pi * fn * DV / G0
    print(f"{fn:7d}  {srs[fn]:8.2f}  {srs[fn] / A:6.3f}  {asint:9.2f}")
b = srs[10]
asb = 2 * math.pi * 10 * DV / G0
# Respuesta analitica de un impulso de cambio de velocidad DV (el pulso es corto frente al periodo de 10 Hz): pico de la aceleracion absoluta
w10 = 2 * math.pi * 10
wd = w10 * math.sqrt(1 - zeta**2)
tt = np.linspace(0, 0.3, 300001)
z = -(DV / wd) * np.exp(-zeta * w10 * tt) * np.sin(wd * tt)
zd = -(DV / wd) * np.exp(-zeta * w10 * tt) * (wd * np.cos(wd * tt) - zeta * w10 * np.sin(wd * tt))
imp = float(np.max(np.abs(2 * zeta * w10 * zd + w10**2 * z))) / G0
print(f"Baja frecuencia (10 Hz): SRS = {b:.2f} g ; w DV (sin amortiguamiento) = {asb:.2f} g ; impulso analitico amortiguado = {imp:.2f} g")
print(f"  diferencia SRS frente al impulso analitico = {abs(b - imp) / imp * 100:.2f} % ; frente a w DV = {abs(b - asb) / asb * 100:.2f} %")
comprobar(abs(b - imp) / imp < 0.02, "a baja frecuencia el SRS debe seguir la respuesta a un impulso de cambio de velocidad DV")
comprobar(b < asb, "el amortiguamiento reduce el pico respecto de w DV")
alta = srs[10000]
print(f"Alta frecuencia (10 kHz): SRS = {alta:.2f} g = {alta / A:.3f} A")
comprobar(A <= alta <= 1.2 * A, "a alta frecuencia el SRS debe acercarse a la amplitud del pulso")
mx = max(srs, key=srs.get)
print(f"Maximo del SRS = {srs[mx]:.2f} g en {mx} Hz ({srs[mx] / A:.3f} A)")
comprobar(srs[mx] <= 2.0 * A, "el maximo del SRS de una semisenoidal con Q = 10 no debe superar 2 A")
print("SRS en 1000 Hz para otro Q")
for q in (5, 10, 20):
    zeta = 1 / (2 * q)
    print(f"  Q = {q:2d}: {srs_punto(1000):.2f} g")
fin()
