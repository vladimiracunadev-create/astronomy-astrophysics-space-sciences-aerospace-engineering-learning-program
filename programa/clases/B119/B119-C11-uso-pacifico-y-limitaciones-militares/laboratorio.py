#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C11: art. IV del Tratado del Espacio Ultraterrestre como arbol de decision y su verificacion exhaustiva (actividades SINTETICAS).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Texto consultado (2026-11-11, nota de legal.un.org): art. IV: los Estados no colocan en orbita, en cuerpos celestes ni en el espacio objetos con armas nucleares u otras de destruccion
masiva; la Luna y otros cuerpos celestes se usan exclusivamente con fines pacificos, aunque se admite personal militar para investigacion cientifica y el equipo necesario para
la exploracion pacifica. Acuerdo sobre la Luna (UNOOSA, art. 3): sin bases militares, ensayos de armas ni maniobras militares en la Luna.
NO consultado: interpretaciones doctrinales sobre armas convencionales en orbita ni la practica de los Estados; el modelo NO opina sobre ellas ("no regulado por el art. IV" = fuera de lo modelado).
Modelo: ubicacion in {orbita, cuerpo_celeste, espacio_otro}, wmd, instalacion_militar (base, ensayo o maniobra), personal_militar_ciencia.
Dos implementaciones independientes (arbol y lista de reglas) deben coincidir en las 3*2*2*2 = 24 combinaciones.
"""
import itertools, json, platform

def arbol(loc, wmd, inst, pers):
    if wmd:
        return "prohibido"
    if loc == "cuerpo_celeste":
        if inst:
            return "prohibido"
        return "condicionado" if pers else "permitido"
    return "fuera_art_IV"

REGLAS = [
    (lambda l, w, i, p: w, "prohibido"),
    (lambda l, w, i, p: l == "cuerpo_celeste" and i, "prohibido"),
    (lambda l, w, i, p: l == "cuerpo_celeste" and p, "condicionado"),
    (lambda l, w, i, p: l == "cuerpo_celeste", "permitido"),
    (lambda l, w, i, p: True, "fuera_art_IV"),
]
def lista(loc, wmd, inst, pers):
    for cond, res in REGLAS:
        if cond(loc, wmd, inst, pers):
            return res

print("Python", platform.python_version(), "(biblioteca estandar)")
print("Actividades SINTETICAS; art. IV parafraseado de legal.un.org (consultada 2026-11-11); armas convencionales en orbita: NO consultado.")
cuenta = {}
coinciden = 0
total = 0
for loc, w, i, p in itertools.product(["orbita", "cuerpo_celeste", "espacio_otro"], [0, 1], [0, 1], [0, 1]):
    a, b = arbol(loc, w, i, p), lista(loc, w, i, p)
    total += 1
    coinciden += a == b
    cuenta[a] = cuenta.get(a, 0) + 1
print("Combinaciones:", total, " coinciden:", coinciden)
for k in ("prohibido", "condicionado", "permitido", "fuera_art_IV"):
    print(f"  {k:13s} {cuenta.get(k, 0):2d}")
assert coinciden == total == 24
# actividades de ejemplo
EJ = {
    "ADM en orbita": ("orbita", 1, 0, 0),
    "Base militar en la Luna": ("cuerpo_celeste", 0, 1, 0),
    "Cientificos militares en la Luna": ("cuerpo_celeste", 0, 0, 1),
    "Telescopio civil en un asteroide": ("cuerpo_celeste", 0, 0, 0),
    "Satelite de observacion en orbita": ("orbita", 0, 0, 0),
}
for n, a in EJ.items():
    print(f"  {n:34s} -> {arbol(*a)}")
assert arbol(*EJ["ADM en orbita"]) == "prohibido" and arbol(*EJ["Cientificos militares en la Luna"]) == "condicionado"
print("CLAVES " + json.dumps({"proh": cuenta["prohibido"], "cond": cuenta["condicionado"], "perm": cuenta["permitido"], "fuera": cuenta["fuera_art_IV"], "tot": total}))
print("Pruebas superadas.")
