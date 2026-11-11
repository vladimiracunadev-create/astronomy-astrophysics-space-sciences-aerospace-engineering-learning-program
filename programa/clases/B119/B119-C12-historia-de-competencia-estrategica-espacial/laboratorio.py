#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B119-C12: cronologia de la competencia estrategica espacial y el rezago del derecho (intervalos calculados con dos metodos).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
Fechas CONSULTADAS (2026-11-11): COPUOS ad hoc 1958-12-13 y permanente 1959-12-12 (resumen de busqueda UNOOSA); Tratado del Espacio Ultraterrestre aprobado 1966-12-19, abierto a firma
1967-01-27, en vigor 1967-10-10 (nota legal.un.org); Convenio de Registro aprobado 1974-11-12 (UNOOSA); Acuerdo sobre la Luna aprobado 1979-12-05 (UNOOSA).
Fechas NO CONSULTADAS en esta sesion (hechos historicos conocidos, a verificar en fuente primaria): Sputnik 1 (1957-10-04), Explorer 1 (1958-01-31), Gagarin (1961-04-12), Apollo 11 (1969-07-20).
Verificacion: diferencia de fechas con datetime.date y con un numero de dia juliano calculado a mano (algoritmo de Fliegel-Van Flandern); deben coincidir exactamente.
Unidades: dias, anos (dias/365.2425). Sin modelo de causalidad: solo cronologia.
"""
import datetime as dt, json, platform

EV = [
    ("Sputnik 1 (no consultada)", dt.date(1957, 10, 4)),
    ("Explorer 1 (no consultada)", dt.date(1958, 1, 31)),
    ("COPUOS ad hoc (consultada)", dt.date(1958, 12, 13)),
    ("COPUOS permanente (consultada)", dt.date(1959, 12, 12)),
    ("Gagarin (no consultada)", dt.date(1961, 4, 12)),
    ("OST aprobado (consultada)", dt.date(1966, 12, 19)),
    ("OST en vigor (consultada)", dt.date(1967, 10, 10)),
    ("Apollo 11 (no consultada)", dt.date(1969, 7, 20)),
    ("Convenio de Registro aprobado (consultada)", dt.date(1974, 11, 12)),
    ("Acuerdo sobre la Luna aprobado (consultada)", dt.date(1979, 12, 5)),
]

def jdn(y, m, d):  # numero de dia juliano (calendario gregoriano), Fliegel-Van Flandern
    return (1461 * (y + 4800 + (m - 14) // 12)) // 4 + (367 * (m - 2 - 12 * ((m - 14) // 12))) // 12 - (3 * ((y + 4900 + (m - 14) // 12) // 100)) // 4 + d - 32075

def dias(a, b):
    x = (b - a).days
    y = jdn(b.year, b.month, b.day) - jdn(a.year, a.month, a.day)
    assert x == y
    return x

print("Python", platform.python_version(), "(biblioteca estandar)")
print("Cronologia: fechas marcadas 'consultada' vienen de UNOOSA/legal.un.org (2026-11-11); las otras NO se consultaron.")
t0 = EV[0][1]
for n, f in EV:
    d = dias(t0, f)
    print(f"{n:46s} {f.isoformat()}  +{d:6d} d = {d / 365.2425:6.2f} anos desde Sputnik 1")
a = dias(EV[0][1], EV[6][1]) / 365.2425
b = dias(EV[0][1], EV[9][1]) / 365.2425
c = dias(EV[0][1], EV[2][1]) / 30.436875
print(f"Sputnik 1 -> OST en vigor: {a:.2f} anos ; Sputnik 1 -> Acuerdo sobre la Luna aprobado: {b:.2f} anos ; Sputnik 1 -> COPUOS ad hoc: {c:.1f} meses")
trat = [EV[5][1], EV[8][1], EV[9][1]]
inter = [dias(trat[i], trat[i + 1]) / 365.2425 for i in range(2)]
print(f"Entre OST, Registro y Luna (aprobaciones): {inter[0]:.2f} y {inter[1]:.2f} anos ; media {sum(inter) / 2:.2f}")
assert 10.0 < a < 10.1
print("CLAVES " + json.dumps({"a": "%.2f" % a, "b": "%.2f" % b, "c": "%.1f" % c, "i1": "%.2f" % inter[0], "i2": "%.2f" % inter[1], "m": "%.2f" % (sum(inter) / 2), "dias_ost": dias(EV[0][1], EV[6][1])}))
print("Pruebas superadas.")
