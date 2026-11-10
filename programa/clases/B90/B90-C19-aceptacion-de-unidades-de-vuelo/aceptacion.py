#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C19: niveles de calificacion y aceptacion, danio acumulado y paquete de datos de una unidad de vuelo (SINTETICO).

Aceptacion = calificacion - 3 dB en PSD (diferencia DE EJEMPLO, no de una norma). Grms = sqrt(area). Danio de Miner-Basquin para
vibracion aleatoria: D = (G/G_ref)^b t / t_ref con b = 6 (SINTETICO). Comprobacion: el area numerica del espectro desplazado = 0.5 x area.
Unidades: g2/Hz, g, s. Tolerancia: 1e-9 relativo.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: espectro de calificacion de 20-2000 Hz; unidad de vuelo")
bp = [(20.0, 0.010), (80.0, 0.040), (500.0, 0.040), (2000.0, 0.010)]

def area(bp, factor=1.0):
    a = 0.0
    for (f1, p1), (f2, p2) in zip(bp[:-1], bp[1:]):
        m = math.log(p2 / p1) / math.log(f2 / f1)
        a += factor * (p1 * f1 * math.log(f2 / f1) if abs(m + 1) < 1e-12 else p1 * f1 / (m + 1) * ((f2 / f1) ** (m + 1) - 1))
    return a

Gq = math.sqrt(area(bp))
fac = 10 ** (-3 / 10)
Ga = math.sqrt(area(bp, fac))
print(f"Calificacion: Grms = {Gq:.3f} g ; aceptacion (-3 dB): Grms = {Ga:.3f} g ; cociente = {Ga / Gq:.4f} (10^(-3/20) = {10 ** (-3 / 20):.4f})")
comprobar(abs(Ga / Gq - math.sqrt(fac)) < 1e-12, "el Grms escala con la raiz del factor de PSD")
f = np.geomspace(20, 2000, 2001)
p = np.array([next(p1 * (x / f1) ** (math.log(p2 / p1) / math.log(f2 / f1)) for (f1, p1), (f2, p2) in zip(bp[:-1], bp[1:]) if f1 <= x <= f2) for x in f])
num = float(np.trapezoid(p, f))
print(f"Area numerica = {num:.4f} ; area exacta = {area(bp):.4f}")
comprobar(abs(num - area(bp)) / area(bp) < 1e-2, "area numerica y exacta deben coincidir a 1 %")

b = 6.0
t_q, t_a = 120.0, 60.0                 # s de calificacion (2 min) y de aceptacion (1 min), ejemplo
t_vuelo_ref = 3600.0                   # vida de referencia en el nivel de calificacion (sintetica)
D_acc = (Ga / Gq) ** b * t_a / t_vuelo_ref
D_q = t_q / t_vuelo_ref
print(f"Danio relativo (exponente b = {b:.0f}): calificacion {t_q:.0f} s = {D_q * 100:.2f} % ; aceptacion {t_a:.0f} s a -3 dB = {D_acc * 100:.3f} % de la vida de referencia")
comprobar(abs(D_acc / ((10 ** (-3 / 20)) ** 6 * t_a / t_vuelo_ref) - 1) < 1e-12, "el danio de aceptacion debe ser 10^(-0.9) por el tiempo")
print("Descuento por nivel: -dB -> cociente de danio por segundo")
for db in (0, 1, 3, 6):
    print(f"   {db} -> {10 ** (-db * b / 20):.4f}")
paquete = ["Informe de vibracion de aceptacion", "Registro de termovacio", "Prueba funcional posensayo", "Lista de anomalias cerradas",
           "Registro de configuracion (as-built)", "Certificados de calibracion", "Firma del comite"]
estado = [True, True, True, False, True, True, False]
print("Paquete de datos de aceptacion:")
for it, ok in zip(paquete, estado):
    print(f"   [{'x' if ok else ' '}] {it}")
falt = [it for it, ok in zip(paquete, estado) if not ok]
print(f"Faltan {len(falt)} de {len(paquete)} elementos -> decision: {'NO ACEPTAR todavia' if falt else 'ACEPTAR'}")
comprobar(len(falt) == 2, "faltan dos elementos en el ejemplo")
fin()
