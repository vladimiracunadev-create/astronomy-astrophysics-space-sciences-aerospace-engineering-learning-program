#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C01: clasificacion de cuerpos menores por elementos orbitales, parametro de Tisserand y diametro desde H.

Datos: doce objetos SINTETICOS (SINT-01..SINT-12) con elementos inventados para el ejemplo; no son objetos reales. Los criterios de grupo (Atira, Aten, Apollo, Amor; q < 1.3 au
para ser NEO) y la relacion H <= 22 <-> ~140 m con albedo 0.14 proceden de la pagina NEO Groups de CNEOS/JPL (consultada el 2026-11-09). El semieje de Jupiter (5.2044 au) es un
valor aproximado del autor, no consultado en esta sesion. La formula D = 1329 km / sqrt(p) * 10^(-H/5) es la relacion estandar H-D-albedo (no consultada; se contrasta con el dato de 140 m).
Modelo: q = a(1-e), Q = a(1+e); T_J = aJ/a + 2 cos i sqrt((a/aJ)(1-e^2)). Unidades: au, grados, km, adimensional.
Supuestos: orbitas keplerianas de dos cuerpos; albedo geometrico 0.14 si no se indica otro. Validez: clasificacion didactica; el MOID (C05) no se usa aqui, por lo que no se decide si un objeto es PHA.
Tolerancia: D(H=22, p=0.14) = 140 m +- 2 m; T_J de una orbita circular coplanar en a = aJ igual a 3 con 1e-12; cocientes de diametro con 1e-12.
"""
import math, platform

AJ = 5.2044  # au, aproximado (no consultado)

def grupo(a, e):
    q, Q = a * (1 - e), a * (1 + e)
    if q >= 1.3:
        return "no NEO"
    if a < 1.0:
        return "Atira" if Q < 0.983 else "Aten"
    return "Apollo" if q < 1.017 else "Amor"

def tisserand(a, e, i_deg):
    return AJ / a + 2.0 * math.cos(math.radians(i_deg)) * math.sqrt((a / AJ) * (1 - e * e))

def diametro_km(H, p=0.14):
    return 1329.0 / math.sqrt(p) * 10 ** (-H / 5.0)

OBJ = [  # nombre, a [au], e, i [grados], H
    ("SINT-01", 0.75, 0.20, 5, 21.0), ("SINT-02", 0.90, 0.30, 10, 23.5), ("SINT-03", 1.20, 0.45, 8, 18.0),
    ("SINT-04", 1.50, 0.30, 12, 19.5), ("SINT-05", 1.10, 0.05, 2, 26.0), ("SINT-06", 2.70, 0.15, 10, 15.0),
    ("SINT-07", 2.20, 0.60, 20, 20.5), ("SINT-08", 3.20, 0.05, 3, 13.0), ("SINT-09", 3.50, 0.65, 30, 16.5),
    ("SINT-10", 1.05, 0.10, 1, 22.0), ("SINT-11", 0.98, 0.02, 1, 24.0), ("SINT-12", 0.50, 0.30, 5, 25.0),
]

def calcular():
    cuentas = {}
    filas = []
    for n, a, e, i, H in OBJ:
        g = grupo(a, e)
        cuentas[g] = cuentas.get(g, 0) + 1
        filas.append((n, a, e, i, H, a * (1 - e), a * (1 + e), g, tisserand(a, e, i), diametro_km(H) * 1000))
    return {"filas": filas, "cuentas": cuentas, "D22": diametro_km(22.0) * 1000,
            "TJ_circ": tisserand(AJ, 0.0, 0.0), "razon_alb": diametro_km(20, 0.05) / diametro_km(20, 0.30),
            "TJ09": tisserand(3.5, 0.65, 30), "D20_p05": diametro_km(20, 0.05) * 1000, "D20_p30": diametro_km(20, 0.30) * 1000}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("%-8s %5s %5s %5s %5s %6s %6s %-7s %6s %9s" % ("objeto", "a", "e", "i", "H", "q", "Q", "grupo", "T_J", "D[m]"))
    for f in r["filas"]:
        print("%-8s %5.2f %5.2f %5.0f %5.1f %6.3f %6.3f %-7s %6.3f %9.1f" % f)
    print("Conteo por grupo:", ", ".join("%s=%d" % kv for kv in sorted(r["cuentas"].items())))
    print("D(H=22, p=0.14) = %.1f m (dato de la fuente: ~140 m)" % r["D22"])
    print("D(H=20): p=0.05 -> %.0f m ; p=0.30 -> %.0f m ; cociente = %.4f (sqrt(6) = %.4f)" % (r["D20_p05"], r["D20_p30"], r["razon_alb"], math.sqrt(6)))
    print("T_J de una orbita circular coplanar en a = aJ: %.12f" % r["TJ_circ"])
    assert abs(r["D22"] - 140.0) < 2.0
    assert abs(r["TJ_circ"] - 3.0) < 1e-12
    assert abs(r["razon_alb"] - math.sqrt(6)) < 1e-12
    # casos de frontera analiticos
    assert grupo(0.9, 0.0913) == "Atira" and grupo(0.9, 0.0930) == "Aten" and grupo(0.9, 0.08) == "Atira"  # Q = 0.983 en e = 0.09222
    assert grupo(1.1, 0.0755) == "Apollo" and grupo(1.1, 0.07) == "Amor"                                    # q = 1.017 en e = 0.0755
    assert grupo(1.0, 0.31) == "Apollo" and grupo(2.0, 0.36) == "Amor" and grupo(2.0, 0.34) == "no NEO"     # q = 1.3 en e = 0.35
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
