#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C10: escala de Palermo calculada, energia cinetica de un impacto y categorias de la escala de Torino.

Datos: cinco casos SINTETICOS (diametro, densidad, velocidad, probabilidad de impacto y tiempo hasta el evento inventados). La formula de Palermo PS = log10(PI / (fB DT)), con fB = 0.03 E^(-4/5)
sucesos por anio (E en megatones de TNT) y DT los anios hasta el evento, y la descripcion de la escala de Torino (niveles 0-10 y colores) proceden de las paginas de CNEOS/JPL consultadas el 2026-11-09.
La conversion 1 Mt = 4.184e15 J es el valor convencional del autor (no consultado). Las densidades y velocidades son ilustrativas.
Modelo: E = (1/2) m v^2 con m = rho pi D^3 / 6 (esfera). Unidades: m, kg/m^3, km/s, Mt, anios.
Supuestos: sin entrada atmosferica ni fragmentacion; escala de Torino solo descrita (su tabla de decision no se codifica). Validez: ilustrativa.
Tolerancia: PS = 0 cuando PI = fB DT y PS = -2 cuando PI = 0.01 fB DT con 1e-12; E de una esfera de 100 m, 3000 kg/m^3 y 20 km/s igual a la cuenta manual con 1e-9 relativo.
"""
import math, platform

MT = 4.184e15

def energia_mt(D, rho, v_kms):
    m = rho * math.pi * D ** 3 / 6.0
    return 0.5 * m * (v_kms * 1e3) ** 2 / MT

def fondo(E):
    return 0.03 * E ** -0.8

def palermo(PI, E, DT):
    return math.log10(PI / (fondo(E) * DT))

def banda_palermo(ps):
    if ps < -2: return "sin consecuencias probables"
    if ps < 0: return "merece vigilancia"
    return "merece atencion"

def torino_color(n):
    if n == 0: return "blanco"
    if n == 1: return "verde"
    if 2 <= n <= 4: return "amarillo"
    if 5 <= n <= 7: return "naranja"
    if 8 <= n <= 10: return "rojo"
    raise ValueError(n)

CASOS = [  # nombre, D [m], rho [kg/m3], v [km/s], PI, DT [anios]
    ("SINT-1", 140.0, 2600.0, 20.0, 1e-4, 30),
    ("SINT-2", 50.0, 2600.0, 15.0, 1e-3, 10),
    ("SINT-3", 470.0, 2600.0, 20.0, 1e-2, 13),
    ("SINT-4", 20.0, 3000.0, 18.0, 1e-5, 5),
    ("SINT-5", 1000.0, 2600.0, 20.0, 1e-6, 50),
]

def calcular():
    filas = []
    for n, D, rho, v, PI, DT in CASOS:
        E = energia_mt(D, rho, v)
        ps = palermo(PI, E, DT)
        filas.append((n, D, v, PI, DT, E, fondo(E), ps, banda_palermo(ps)))
    E0 = energia_mt(100.0, 3000.0, 20.0)
    ps0 = palermo(fondo(E0) * 7, E0, 7)
    ps2 = palermo(0.01 * fondo(E0) * 7, E0, 7)
    return {"filas": filas, "E100": E0, "ps0": ps0, "ps2": ps2, "colores": [(n, torino_color(n)) for n in range(11)],
            "E_manual": 0.5 * (3000.0 * math.pi * 100.0 ** 3 / 6.0) * (2e4) ** 2 / 4.184e15}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("%-7s %7s %6s %9s %5s %11s %12s %8s  %s" % ("caso", "D[m]", "v", "PI", "DT", "E[Mt]", "fB[1/anio]", "Palermo", "banda"))
    for f in r["filas"]:
        print("%-7s %7.0f %6.1f %9.0e %5d %11.4g %12.4g %8.2f  %s" % f)
    print("Esfera de 100 m, 3000 kg/m3, 20 km/s: E = %.6f Mt (cuenta manual %.6f)" % (r["E100"], r["E_manual"]))
    print("PS cuando PI = fB DT: %.12f ; cuando PI = 0.01 fB DT: %.12f" % (r["ps0"], r["ps2"]))
    print("Torino (niveles -> color):", ", ".join("%d=%s" % c for c in r["colores"]))
    assert abs(r["ps0"]) < 1e-12 and abs(r["ps2"] + 2) < 1e-12
    assert abs(r["E100"] / r["E_manual"] - 1) < 1e-9
    assert [c for _, c in r["colores"]].count("amarillo") == 3 and [c for _, c in r["colores"]].count("naranja") == 3 and [c for _, c in r["colores"]].count("rojo") == 3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
