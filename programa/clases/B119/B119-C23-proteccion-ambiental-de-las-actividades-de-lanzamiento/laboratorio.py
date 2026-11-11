#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C23: estequiometria de la combustion de propergoles y emisiones de CO2 por lanzamiento (masa de combustible SINTETICA).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11, nota de legal.un.org): art. IX del Tratado del Espacio Ultraterrestre: cooperacion y consideracion de los intereses de otros Estados; la nota senala que el articulo
trata brevemente la proteccion del medio espacial y de la Tierra frente a materia extraterrestre danina. NO consultado: ninguna norma ambiental de lanzamiento, inventario de emisiones ni estudio de impacto.
Datos quimicos (masas atomicas estandar, no consultadas en una fuente concreta; verificadas con balance de masa): C 12.011, H 1.008, O 15.999 g/mol.
Modelo: querosenos tipo RP-1 representados como C12H26 (APROXIMACION: el combustible real es una mezcla); reaccion completa C12H26 + 18.5 O2 -> 12 CO2 + 13 H2O;
metano: CH4 + 2 O2 -> CO2 + 2 H2O; hidrogeno: 2 H2 + O2 -> 2 H2O. La combustion real en motores es incompleta y rica en combustible: el CO2 calculado es una COTA SUPERIOR del carbono emitido como CO2.
SINTETICO: masa de combustible por lanzamiento = 100 t; 10, 50 y 100 lanzamientos por ano.
Tolerancia: balance de masa (reactivos == productos) a 1e-9 relativo.
"""
import json, platform

M = {"C": 12.011, "H": 1.008, "O": 15.999}
def masa(formula):
    return sum(M[a] * n for a, n in formula.items())
COMBUSTIBLES = {
    "queroseno (C12H26, aproximado)": ({"C": 12, "H": 26}, 18.5, {"C": 12}, 13),
    "metano (CH4)": ({"C": 1, "H": 4}, 2.0, {"C": 1}, 2),
    "hidrogeno (H2)": ({"H": 2}, 0.5, {}, 1),
}
print("Python", platform.python_version(), "(biblioteca estandar)")
print("Combustion completa, cota superior de CO2; masas atomicas estandar (no consultadas); art. IX consultado (2026-11-11); ninguna norma ambiental consultada.")
O2, CO2, H2O = masa({"O": 2}), masa({"C": 1, "O": 2}), masa({"H": 2, "O": 1})
res = {}
for nombre, (f, nO2, c, nH2O) in COMBUSTIBLES.items():
    mf = masa(f)
    react = mf + nO2 * O2
    prod = c.get("C", 0) * CO2 + nH2O * H2O
    assert abs(react - prod) / react < 1e-9, nombre
    co2_kg = c.get("C", 0) * CO2 / mf          # kg CO2 por kg de combustible
    o2_kg = nO2 * O2 / mf                      # kg O2 estequiometrico por kg de combustible
    res[nombre] = (co2_kg, o2_kg)
    print(f"{nombre:32s} M = {mf:7.3f} g/mol ; O2 estequiometrico {o2_kg:6.3f} kg/kg ; CO2 {co2_kg:6.3f} kg/kg ; balance de masa ok")
kq = res["queroseno (C12H26, aproximado)"][0]
COMB_T = 100.0
print(f"Un lanzamiento con {COMB_T:.0f} t de queroseno: CO2 <= {kq * COMB_T:.1f} t")
for n in (10, 50, 100):
    print(f"   {n:3d} lanzamientos/ano: CO2 <= {n * kq * COMB_T:8.0f} t/ano")
print(f"Metano: {res['metano (CH4)'][0] * COMB_T:.1f} t por 100 t ; hidrogeno: 0 t de CO2 (el vapor y otros efectos no se modelan)")
assert abs(kq - 3.1) < 0.01
print("CLAVES " + json.dumps({"kq": "%.3f" % kq, "km": "%.3f" % res["metano (CH4)"][0], "oq": "%.3f" % res["queroseno (C12H26, aproximado)"][1], "t1": "%.1f" % (kq * COMB_T), "t50": "%.0f" % (50 * kq * COMB_T), "mq": "%.3f" % masa({"C": 12, "H": 26})}))
print("Pruebas superadas.")
