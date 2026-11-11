#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C09: coordinacion del espectro: perdida en espacio libre e interferencia sobre un receptor satelital (SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11, UIT-R, pagina del Departamento de Servicios Espaciales; WebFetch): el Reglamento de Radiocomunicaciones se aplica a sistemas espaciales; la UIT
examina y publica las notificaciones de asignaciones de frecuencia, fija requisitos de coordinacion, inscribe las asignaciones en el Registro Internacional de Frecuencias (MIFR)
y ayuda a resolver interferencias perjudiciales. NO consultado: el Reglamento de Radiocomunicaciones, sus apendices ni los criterios numericos de coordinacion.
Formulas (no consultadas en una fuente concreta; verificadas con el caso GEO): FSPL[dB] = 20 log10(d[km]) + 20 log10(f[MHz]) + 32.45; N = k T B.
Criterio ILUSTRATIVO: I/N <= -12.2 dB (equivale a un 6 % de aumento de temperatura de ruido); es un valor comun en la literatura, aqui solo didactico.
SINTETICO: interferente con EIRP 20 dBW hacia el receptor víctima de ganancia 40 dBi; frecuencia 12000 MHz; T = 150 K; B = 36 MHz.
Tolerancias: FSPL del enlace GEO (35786 km, 12 GHz) = 205.1 dB a 0.1 dB.
"""
import json, math, platform

K = 1.380649e-23
def fspl(d_km, f_mhz):
    return 20 * math.log10(d_km) + 20 * math.log10(f_mhz) + 32.45

f, T, B = 12000.0, 150.0, 36e6
N_dBW = 10 * math.log10(K * T * B)
eirp_i, g_rx = 20.0, 40.0
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Enlaces SINTETICOS; UIT-R consultada el 2026-11-11 (procedimientos, no cifras); criterio I/N = -12.2 dB ILUSTRATIVO.")
g = fspl(35786.0, f)
print(f"Control: FSPL GEO a 12 GHz = {g:.2f} dB (esperado 205.1)")
assert abs(g - 205.1) < 0.1
print(f"Ruido N = k T B = {N_dBW:.2f} dBW")
print("  separacion al interferente [km]   FSPL [dB]   I [dBW]   I/N [dB]   cumple (<= -12.2)")
res = {}
for d in (500.0, 2000.0, 10000.0, 36000.0, 80000.0):
    L = fspl(d, f)
    I = eirp_i + g_rx - L
    inr = I - N_dBW
    res[d] = inr
    print(f"{d:25.0f} {L:12.2f} {I:9.2f} {inr:10.2f}   {'si' if inr <= -12.2 else 'NO'}")
# distancia minima para cumplir el criterio: despejar d
dmin = 10 ** ((eirp_i + g_rx - N_dBW + 12.2 - 20 * math.log10(f) - 32.45) / 20)
print(f"Distancia minima para cumplir I/N <= -12.2 dB: {dmin:.0f} km")
assert abs(fspl(dmin, f) - (eirp_i + g_rx - N_dBW + 12.2)) < 1e-9
# duplicar la distancia da +6.02 dB de perdida
dif = fspl(2000.0, f) - fspl(1000.0, f)
print(f"Duplicar la distancia: +{dif:.2f} dB")
assert abs(dif - 6.0206) < 1e-3
print("CLAVES " + json.dumps({"N": "%.2f" % N_dBW, "geo": "%.2f" % g, "dmin": "%.0f" % dmin, "i500": "%.1f" % res[500.0], "i36": "%.1f" % res[36000.0], "dif": "%.2f" % dif}))
print("Pruebas superadas.")
