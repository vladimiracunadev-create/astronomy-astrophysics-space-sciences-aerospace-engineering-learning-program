#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C25: recursos espaciales: ecuacion del cohete y precio maximo de un propergol obtenido en el espacio (caso de negocio SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera; no es una valoracion de ningun proyecto.
Texto consultado (2026-11-11): Acuerdo sobre la Luna, art. 11 (UNOOSA): los recursos naturales de la Luna son patrimonio comun de la humanidad, sin propiedad en el lugar y con un regimen internacional futuro;
art. II del Tratado del Espacio Ultraterrestre (nota legal.un.org): sin apropiacion nacional. NO consultados: los Acuerdos Artemis, las leyes nacionales sobre recursos espaciales ni su interpretacion;
cualquier referencia a ellos se rotula "no consultado".
Fisica (no consultada en una fuente concreta; verificada por inversion): ecuacion de Tsiolkovsky: m0/mf = exp(dv / (Isp g0)), g0 = 9.80665 m/s^2.
SINTETICO: carga util de 1000 kg; dv = 3800 m/s (cifra ilustrativa); Isp = 450 s; coste de lanzamiento a orbita baja 2500 u.m./kg (unidades monetarias sinteticas); estructura = 10 % del propergol.
Idea: el propergol producido en el espacio ahorra el lanzamiento de la masa de propergol desde la Tierra; el precio maximo que un comprador pagaria por kg en el deposito
es el ahorro por kg de propergol (cota teorica, sin transporte ni margen).
Tolerancia: la masa inicial recalculada desde la razon de masas coincide con la original (1e-9 relativo).
"""
import json, math, platform

G0 = 9.80665
carga, dv, isp = 1000.0, 3800.0, 450.0
coste_kg, f_est = 2500.0, 0.10
razon = math.exp(dv / (isp * G0))
# masa de propergol: m0 = carga + estructura + prop ; estructura = f_est * prop ; mf = carga + estructura
# m0/mf = razon -> prop = (razon - 1) * mf ; mf = carga + f_est * prop
# prop = (razon - 1) * (carga + f_est * prop) -> prop (1 - (razon - 1) f_est) = (razon - 1) carga
den = 1 - (razon - 1) * f_est
assert den > 0
prop = (razon - 1) * carga / den
mf = carga + f_est * prop
m0 = mf + prop
assert abs(m0 / mf - razon) / razon < 1e-9
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Caso SINTETICO; arts. 11 (Luna) y II (tratado) consultados 2026-11-11; Acuerdos Artemis y leyes nacionales NO consultados.")
print(f"Razon de masas exp(dv/(Isp g0)) = {razon:.4f} ; propergol {prop:.0f} kg ; masa inicial {m0:.0f} kg ; masa seca {mf:.0f} kg")
coste_tierra = m0 * coste_kg
print(f"Lanzar todo desde la Tierra: {coste_tierra / 1e6:.2f} M u.m.")
# con propergol comprado en el espacio: solo se lanza la carga y la estructura vacia
masa_lanzada = mf
coste_ahorro = prop * coste_kg
print(f"Con el propergol obtenido en el espacio, se lanza solo {masa_lanzada:.0f} kg: ahorro {coste_ahorro / 1e6:.2f} M u.m. = {coste_kg:.0f} u.m. por kg de propergol")
for precio in (500.0, 1500.0, 2500.0, 3500.0):
    ahorro_neto = prop * (coste_kg - precio)
    print(f"   precio del propergol en el deposito {precio:6.0f} u.m./kg -> ahorro neto {ahorro_neto / 1e6:6.2f} M u.m. ({'conviene' if ahorro_neto > 0 else 'no conviene'})")
# sensibilidad al Isp
for i in (350.0, 450.0, 465.0):
    r = math.exp(dv / (i * G0)); d = 1 - (r - 1) * f_est
    print(f"   Isp {i:5.0f} s: " + (f"propergol {(r - 1) * carga / d:7.0f} kg" if d > 0 else "inviable con esta fraccion estructural"))
print("CLAVES " + json.dumps({"r": "%.4f" % razon, "prop": "%.0f" % prop, "m0": "%.0f" % m0, "ct": "%.2f" % (coste_tierra / 1e6), "ah": "%.2f" % (coste_ahorro / 1e6), "pk": "%.0f" % coste_kg, "mf": "%.0f" % mf}))
print("Pruebas superadas.")
