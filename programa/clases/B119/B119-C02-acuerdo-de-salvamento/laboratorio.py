#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C02: donde puede caer una capsula de retorno de emergencia y a quien hay que notificar (caso SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11): la pagina de UNOOSA del Acuerdo sobre la Luna (art. 12) remite al art. 5 del Acuerdo de Salvamento para objetos hallados
fuera de su lugar previsto. El texto del Acuerdo de Salvamento NO se pudo consultar (la pagina de UNOOSA devolvio 404): su contenido (notificacion, auxilio,
devolucion de personal y de objetos, gastos a cargo de la autoridad de lanzamiento) se cita solo como NO consultado.
Modelo (geometria, no consultada en fuente concreta): aterrizaje uniforme sobre la superficie esferica con |latitud| <= i; fraccion del area de una banda
|lat| <= i = sin(i). Inclinacion ilustrativa i = 51.6 deg. "Estado X" SINTETICO: banda de latitud 20 a 30 deg N (no corresponde a ningun pais real).
Unidades: grados, radianes; probabilidades adimensionales. Semilla 119; N = 400000. Tolerancia: Monte Carlo vs analitico < 3 sigma binomial.
"""
import json, math, platform, random

I = math.radians(51.6)
LAT1, LAT2 = math.radians(20.0), math.radians(30.0)
rng = random.Random(119)
N = 400000

def lat_uniforme_en_banda():
    # superficie uniforme en la banda: sin(lat) uniforme en [-sin i, sin i]
    return math.asin(rng.uniform(-math.sin(I), math.sin(I)))

dentro = 0
for _ in range(N):
    phi = lat_uniforme_en_banda()
    if LAT1 <= phi <= LAT2:
        dentro += 1
p_mc = dentro / N
p_an = (math.sin(LAT2) - math.sin(LAT1)) / (2 * math.sin(I))
sigma = math.sqrt(p_an * (1 - p_an) / N)
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Aterrizaje SINTETICO uniforme en |lat| <= 51.6 deg; Estado X sintetico = banda 20-30 N; Acuerdo de Salvamento NO consultado (404).")
print(f"Probabilidad de caer en el Estado X: Monte Carlo {p_mc:.5f} ; analitica {p_an:.5f} ; sigma {sigma:.5f}")
assert abs(p_mc - p_an) < 3 * sigma

# varios eventos independientes: probabilidad de que al menos uno caiga en el Estado X
for k in (1, 5, 10):
    print(f"  {k:2d} retornos de emergencia: P(al menos uno cae en X) = {1 - (1 - p_an) ** k:.4f}")
p10 = 1 - (1 - p_an) ** 10
# Fraccion de la superficie terrestre alcanzable (banda) y del total
frac_banda = math.sin(I)
print(f"Fraccion de la superficie terrestre alcanzable desde i=51.6: {frac_banda:.4f}")
assert abs(frac_banda - 0.7837) < 1e-3
print("CLAVES " + json.dumps({"p_mc": f"{p_mc:.5f}", "p_an": f"{p_an:.5f}", "p10": f"{p10:.4f}", "banda": f"{frac_banda:.4f}", "p5": f"{1-(1-p_an)**5:.4f}"}))
print("Pruebas superadas.")
