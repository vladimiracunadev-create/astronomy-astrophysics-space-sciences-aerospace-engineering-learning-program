#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C15: resiliencia de un enlace satelital ante interferencia intencional o accidental: margen de resistencia (SINTETICO, defensivo).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera. No indica como interferir un servicio real.
Texto consultado (2026-11-11, UIT-R, pagina del Departamento de Servicios Espaciales): la UIT ayuda a las administraciones a resolver interferencias perjudiciales que afectan a los
servicios espaciales. NO consultado: el Reglamento de Radiocomunicaciones ni ninguna cifra de resistencia real.
Formulas (no consultadas en una fuente concreta; verificadas con dos caminos de calculo, lineal y en dB): J/S = (P_j G_j / L_j) / (P_s G_s / L_s) con perdida en espacio libre
FSPL = 20 log10(d_km) + 20 log10(f_MHz) + 32.45; ganancia de procesamiento Gp = 10 log10(B_espectro / R_datos); margen de resistencia M = Gp - (J/S) - (Eb/N0)_requerido.
SINTETICO: f = 14000 MHz; senal util: EIRP 55 dBW desde 1000 km; fuente de interferencia: EIRP 35 dBW desde 1500 km; B = 20 MHz, R = 20 kbit/s, (Eb/N0)_req = 10 dB.
Tolerancia: J/S lineal == J/S en dB (1e-9).
"""
import json, math, platform

def fspl(d, f):
    return 20 * math.log10(d) + 20 * math.log10(f) + 32.45

f = 14000.0
eirp_s, d_s = 55.0, 1000.0
eirp_j, d_j = 35.0, 1500.0
B, R, ebn0 = 20e6, 20e3, 10.0
gp = 10 * math.log10(B / R)
js_db = (eirp_j - fspl(d_j, f)) - (eirp_s - fspl(d_s, f))      # la ganancia de la antena receptora es la misma y se cancela
lin = (10 ** (eirp_j / 10) / 10 ** (fspl(d_j, f) / 10)) / (10 ** (eirp_s / 10) / 10 ** (fspl(d_s, f) / 10))
assert abs(10 * math.log10(lin) - js_db) < 1e-9
M = gp - js_db - ebn0
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Enlace SINTETICO, analisis DEFENSIVO; UIT-R consultada el 2026-11-11 (procedimiento, sin cifras).")
print(f"Ganancia de procesamiento Gp = {gp:.2f} dB ; J/S = {js_db:.2f} dB ; margen M = {M:.2f} dB")
print("  EIRP de la interferencia [dBW]   J/S [dB]   margen [dB]   resiste")
for e in (25.0, 35.0, 45.0, 55.0, 65.0):
    js = (e - fspl(d_j, f)) - (eirp_s - fspl(d_s, f))
    m = gp - js - ebn0
    print(f"{e:30.0f} {js:10.2f} {m:12.2f}   {'si' if m >= 0 else 'NO'}")
e_max = gp - ebn0 + (fspl(d_j, f) + eirp_s - fspl(d_s, f))
print(f"EIRP maxima de interferencia tolerable (margen 0): {e_max:.2f} dBW")
js_max = gp - ebn0
assert abs(((e_max - fspl(d_j, f)) - (eirp_s - fspl(d_s, f))) - js_max) < 1e-9
# recuperacion: subir la ganancia de procesamiento duplicando el ancho de banda
gp2 = 10 * math.log10(2 * B / R)
print(f"Duplicar el ancho de banda: Gp = {gp2:.2f} dB (+{gp2 - gp:.2f}) ; margen {gp2 - js_db - ebn0:.2f} dB")
assert abs((gp2 - gp) - 3.0103) < 1e-3
print("CLAVES " + json.dumps({"gp": "%.2f" % gp, "js": "%.2f" % js_db, "M": "%.2f" % M, "emax": "%.2f" % e_max, "jsmax": "%.2f" % js_max, "M2": "%.2f" % (gp2 - js_db - ebn0), "d3": "%.2f" % (gp2 - gp)}))
print("Pruebas superadas.")
