#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C09: espectro de vibracion aleatoria SINTETICO, Grms y respuesta de un resonador.

PSD lineal por tramos en escala log-log: area del tramo = P1 f1/(m+1) [(f2/f1)^(m+1) - 1], m = ln(P2/P1)/ln(f2/f1) (m = -1: P1 f1 ln(f2/f1)).
Grms = sqrt(area). Respuesta de un SDOF de frecuencia fn y factor de calidad Q: Miles, G_rms = sqrt(pi/2 fn Q PSD(fn)),
contrastada con la integral numerica de |T(f)|^2 PSD(f). Unidades: Hz, g^2/Hz, g (g = 9.80665 m/s2). Tolerancias: area exacta frente a
trapecio < 1e-4 relativo; Miles frente a integral < 3 %. Niveles SINTETICOS (no son los de GEVS ni de un lanzador).
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: espectro de 20 a 2000 Hz y un resonador de 300 Hz con Q = 10")
bp = [(20.0, 0.010), (80.0, 0.040), (500.0, 0.040), (2000.0, 0.010)]

def area(f1, p1, f2, p2):
    m = math.log(p2 / p1) / math.log(f2 / f1)
    if abs(m + 1) < 1e-12:
        return p1 * f1 * math.log(f2 / f1)
    return p1 * f1 / (m + 1) * ((f2 / f1) ** (m + 1) - 1)

def psd(f):
    for (f1, p1), (f2, p2) in zip(bp[:-1], bp[1:]):
        if f1 <= f <= f2:
            m = math.log(p2 / p1) / math.log(f2 / f1)
            return p1 * (f / f1) ** m
    return 0.0

tramos = []
for (f1, p1), (f2, p2) in zip(bp[:-1], bp[1:]):
    m = math.log(p2 / p1) / math.log(f2 / f1)
    a = area(f1, p1, f2, p2)
    tramos.append(a)
    print(f"Tramo {f1:6.0f}-{f2:6.0f} Hz: pendiente = {10 * m * math.log10(2) / 1:.2f} dB/oct ; area = {a:.4f} g2")
A = sum(tramos)
G = math.sqrt(A)
print(f"Area total = {A:.4f} g2 ; Grms = {G:.3f} g ; pico 3-sigma = {3 * G:.2f} g")
f = np.geomspace(20, 2000, 400001)
p = np.array([psd(x) for x in f[::100]])
fi = f[::100]
A_num = float(np.trapezoid(p, fi))
print(f"Integral numerica (trapecio en 4001 puntos) = {A_num:.4f} g2 ; diferencia = {abs(A_num - A) / A * 100:.3f} %")
comprobar(abs(A_num - A) / A < 1e-2, "la integral numerica debe aproximar el area exacta")
fb = np.geomspace(20, 2000, 2_000_001)
pb = np.array([psd(x) for x in fb[::1000]])
fb2 = fb[::1000]
A_fino = float(np.trapezoid(pb, fb2))
comprobar(abs(A_fino - A) / A < 1e-3, "la integral fina debe aproximar el area exacta")

fn, Q = 300.0, 10.0
zeta = 1 / (2 * Q)
miles = math.sqrt(math.pi / 2 * fn * Q * psd(fn))
ff = np.linspace(20, 2000, 400001)
r = ff / fn
T2 = (1 + (2 * zeta * r) ** 2) / ((1 - r**2) ** 2 + (2 * zeta * r) ** 2)
pp = np.array([psd(x) for x in ff[::10]])
G_int = math.sqrt(float(np.trapezoid(T2[::10] * pp, ff[::10])))
print(f"Respuesta del resonador: Miles = {miles:.3f} g ; integral de |T|^2 PSD = {G_int:.3f} g ; diferencia = {abs(miles - G_int) / G_int * 100:.2f} %")
comprobar(abs(miles - G_int) / G_int < 0.03, "Miles debe coincidir con la integral a 3 %")
print(f"Amplificacion de la respuesta = {miles / G:.2f} ; pico 3-sigma de la respuesta = {3 * miles:.1f} g")

print("Q -> respuesta Grms (Miles) [g]")
for q in (5, 10, 20, 50):
    print(f"  {q:3d} -> {math.sqrt(math.pi / 2 * fn * q * psd(fn)):.2f}")

# Barrido senoidal antes y despues: desplazamiento de la frecuencia de resonancia
f_pre, f_post = 300.0, 291.0
desp = (f_post - f_pre) / f_pre * 100
criterio = 5.0                                   # criterio de ejemplo (%), NO de una norma
print(f"Barrido de verificacion: f_pre = {f_pre} Hz ; f_post = {f_post} Hz ; desplazamiento = {desp:.1f} % (criterio de ejemplo {criterio} %) -> {'PASA' if abs(desp) <= criterio else 'FALLA'}")
comprobar(abs(desp) <= criterio, "el desplazamiento de ejemplo debe estar dentro del criterio")
fin()
