#!/usr/bin/env python3
"""B104-C02: requisitos de tripulacion como cadena trazable y dimensionado lineal de consumibles.
Tasas por persona y dia ILUSTRATIVAS (no son las de un estandar de NASA, que no se consulto)."""
import sys
import numpy as np

# Tasas ILUSTRATIVAS [kg por persona y dia]
TASA = {"oxigeno": 0.84, "agua_potable": 2.5, "alimento_seco": 0.62}
MARGEN = 0.10   # margen de contingencia ilustrativo

print(f"Python {sys.version.split()[0]}; numpy {np.__version__}")
print("MODELO ILUSTRATIVO: tasas por persona y dia inventadas para el ejemplo; margen de contingencia 10 %")


def masa(n, dias, cierre_agua=0.0):
    base = {k: v * n * dias for k, v in TASA.items()}
    base["agua_potable"] *= (1 - cierre_agua)
    return {k: v * (1 + MARGEN) for k, v in base.items()}


print("\nTripulantes | dias | oxigeno [kg] | agua [kg] | alimento [kg] | total [kg]")
for n, d in [(2, 8), (4, 30), (4, 180), (6, 900)]:
    m = masa(n, d)
    print(f"{n:6d} {d:10d} {m['oxigeno']:12.1f} {m['agua_potable']:10.1f} {m['alimento_seco']:12.1f} {sum(m.values()):10.1f}")

# Linealidad en n y d
assert abs(sum(masa(4, 30).values()) - 2 * sum(masa(2, 30).values())) < 1e-9
assert abs(sum(masa(4, 60).values()) - 2 * sum(masa(4, 30).values())) < 1e-9

# Reciclado de agua: masa del equipo vs ahorro
M_HW, cierre, n = 400.0, 0.90, 4     # kg de equipo (ILUSTRATIVO), fraccion reciclada, tripulantes
d_eq = M_HW / (n * TASA["agua_potable"] * (1 + MARGEN) * cierre)
print(f"\nPunto de equilibrio del reciclador (equipo {M_HW:.0f} kg, cierre {cierre:.0%}, {n} tripulantes): {d_eq:.1f} dias")
for d in (30, d_eq, 180, 900):
    sin = masa(n, d)['agua_potable']
    con = masa(n, d, cierre)['agua_potable'] + M_HW
    print(f"  {d:7.1f} dias: agua sin reciclar {sin:8.1f} kg; con reciclador (incl. equipo) {con:8.1f} kg; ahorro {sin-con:8.1f} kg")
assert abs(masa(n, d_eq)['agua_potable'] - (masa(n, d_eq, cierre)['agua_potable'] + M_HW)) < 1e-6

# Matriz de trazabilidad (SINTETICA)
req = {
    "R1 oxigeno suficiente": ("analisis", True),
    "R2 agua suficiente": ("analisis", True),
    "R3 alimento suficiente": ("analisis", True),
    "R4 espacio de descanso": ("inspeccion", True),
    "R5 abortar en 10 min": ("ensayo", False),
}
sin_verif = [k for k, (m, ok) in req.items() if not ok]
print(f"\nRequisitos: {len(req)}; sin verificacion cerrada: {sin_verif}")
assert len(sin_verif) == 1
print("Pruebas superadas.")
