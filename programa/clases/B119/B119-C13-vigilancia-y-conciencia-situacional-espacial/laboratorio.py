#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C13: vigilancia del entorno orbital: duracion de un paso sobre un sensor y cribado de pares por altitud (todo SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11): art. VI del Convenio de Registro (UNOOSA): los Estados partes, en especial los que tienen medios de rastreo, ayudan a identificar objetos que causan
dano o son peligrosos. NO consultado: ningun catalogo ni red real de vigilancia, ni su politica de datos.
Geometria (no consultada en una fuente concreta; verificada con el caso limite epsilon = 90 grados): angulo central de visibilidad
lambda = arccos(R cos(eps) / (R + h)) - eps; duracion maxima de paso = 2 lambda / n, con n = sqrt(GM / (R+h)^3).
Constantes estandar: R = 6378.137 km, GM = 398600.4418 km^3/s^2. SINTETICO: h = 550 km, elevacion minima eps = 10 grados; 2000 objetos con altitudes circulares uniformes en 400-1200 km; umbral de 10 km.
Semilla 119. Tolerancia: pares filtrados == pares de fuerza bruta (exacto).
"""
import json, math, platform, random

R, GM = 6378.137, 398600.4418
h, eps = 550.0, math.radians(10.0)
lam = math.acos(R * math.cos(eps) / (R + h)) - eps
n = math.sqrt(GM / (R + h) ** 3)
dur = 2 * lam / n
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Sensor y objetos SINTETICOS; art. VI del Convenio de Registro consultado (2026-11-11); ningun catalogo real consultado.")
print(f"Orbita de {h:.0f} km: periodo {2 * math.pi / n / 60:.2f} min ; angulo central {math.degrees(lam):.2f} deg ; paso maximo {dur:.0f} s = {dur / 60:.2f} min")
# caso limite: eps = 90 deg -> lambda = 0
lim = math.acos(R * math.cos(math.pi / 2) / (R + h)) - math.pi / 2
assert abs(lim) < 1e-12
# fraccion de la orbita visible
frac = 2 * lam / (2 * math.pi)
print(f"Fraccion de la orbita en vista (si la traza pasa por el cenit): {frac:.4f}")
# deteccion: Pd por paso y numero de pasos
pd = 0.6
for k in (1, 3, 5):
    print(f"  Pd por paso {pd}: P(al menos una deteccion en {k} pasos) = {1 - (1 - pd) ** k:.4f}")
# cribado por altitud
rng = random.Random(119)
N = 2000
alt = sorted(rng.uniform(400, 1200) for _ in range(N))
umbral = 10.0
fuerza = sum(1 for i in range(N) for j in range(i + 1, N) if abs(alt[i] - alt[j]) <= umbral)
filtrado = 0
j0 = 0
for i in range(N):
    j = i + 1
    while j < N and alt[j] - alt[i] <= umbral:
        filtrado += 1
        j += 1
total_pares = N * (N - 1) // 2
print(f"Pares totales {total_pares} ; con altitudes a menos de {umbral:.0f} km: {fuerza} (fuerza bruta) = {filtrado} (barrido ordenado) ; reduccion {total_pares / fuerza:.1f}x")
assert fuerza == filtrado
print("CLAVES " + json.dumps({"T": "%.2f" % (2 * math.pi / n / 60), "lam": "%.2f" % math.degrees(lam), "dur": "%.0f" % dur, "durm": "%.2f" % (dur / 60), "frac": "%.4f" % frac, "p3": "%.4f" % (1 - (1 - pd) ** 3), "pares": total_pares, "fb": fuerza, "red": "%.1f" % (total_pares / fuerza)}))
print("Pruebas superadas.")
