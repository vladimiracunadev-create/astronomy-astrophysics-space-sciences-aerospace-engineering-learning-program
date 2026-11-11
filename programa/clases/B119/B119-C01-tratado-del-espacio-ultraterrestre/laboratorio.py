#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C01: el Tratado del Espacio Ultraterrestre como matriz de reglas comprobables (misiones SINTETICAS).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11): nota de la Biblioteca Audiovisual de la ONU (legal.un.org/avl/ha/tos/tos.html): arts. I, II, III, IV, VI, VIII, IX, XI
(parafraseados); no discute los arts. V ni VII. Aprobado por la Asamblea General el 19-12-1966 (res. 2222 (XXI)); en vigor el 10-10-1967.
SINTETICO: las tres misiones y sus atributos son inventados; no describen ningun operador real.
Modelo: seis atributos booleanos por mision (wmd, soberania, privado, autorizado, registrado, informado) y cinco reglas:
IV (sin ADM en orbita), II (sin reclamo de soberania), VI (si es privado, autorizado y supervisado), VIII (registrado), XI (informa).
Tolerancia: enumeracion exhaustiva de 2**6 combinaciones == recuento analitico (exacto).
"""
import itertools, json, platform

ATTR = ["wmd", "soberania", "privado", "autorizado", "registrado", "informado"]

def reglas(m):
    return {"IV": not m["wmd"], "II": not m["soberania"], "VI": (not m["privado"]) or m["autorizado"],
            "VIII": m["registrado"], "XI": m["informado"]}

MISIONES = {
    "A_agencia": dict(wmd=0, soberania=0, privado=0, autorizado=0, registrado=1, informado=1),
    "B_privada_sin_licencia": dict(wmd=0, soberania=0, privado=1, autorizado=0, registrado=1, informado=1),
    "C_reclamo_y_sin_registro": dict(wmd=0, soberania=1, privado=0, autorizado=0, registrado=0, informado=1),
}

print("Python", platform.python_version(), "(biblioteca estandar)")
print("Misiones SINTETICAS; texto del tratado parafraseado de la nota de legal.un.org (consultada 2026-11-11).")
print(" mision                       IV   II   VI  VIII   XI  cumple/5")
cumple = {}
for nombre, m in MISIONES.items():
    r = reglas(m)
    cumple[nombre] = sum(r.values())
    print(f"{nombre:26s}" + "".join(f"{'si' if r[k] else 'NO':>5s}" for k in ["IV", "II", "VI", "VIII", "XI"]) + f"   {cumple[nombre]}")

n_conf = 0
for bits in itertools.product([0, 1], repeat=6):
    m = dict(zip(ATTR, bits))
    if all(reglas(m).values()):
        n_conf += 1
n_total = 2 ** len(ATTR)
analitico = 1 * 1 * 3 * 1 * 1  # wmd=0, soberania=0, (privado,autorizado) en 3 de 4, registrado=1, informado=1
print(f"Combinaciones conformes: {n_conf} de {n_total} (analitico {analitico}); fraccion {n_conf / n_total:.4f}")
assert n_conf == analitico == 3
assert cumple["A_agencia"] == 5 and cumple["B_privada_sin_licencia"] == 4 and cumple["C_reclamo_y_sin_registro"] == 3
print("CLAVES " + json.dumps({"n_conf": n_conf, "n_total": n_total, "frac": "0.0469", "a": cumple["A_agencia"], "b": cumple["B_privada_sin_licencia"], "c": cumple["C_reclamo_y_sin_registro"]}))
print("Pruebas superadas.")
