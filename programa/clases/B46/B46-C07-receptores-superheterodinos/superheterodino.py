#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C07: mezcla, frecuencia imagen y rechazo de imagen (simulacion con muestreo).

Datos: ninguno externo. Frecuencias (f_s = 1000, f_LO = 100, f_FI = 20, en unidades arbitrarias), errores de amplitud y fase del mezclador de
rechazo de imagen y la semilla no se refieren a un instrumento real: son ILUSTRATIVOS.
Modelo: producto de un tono de radio por el oscilador local; la componente a f_FI se mide con el algoritmo de Goertzel. Tanto f_LO + f_FI como
f_LO - f_FI caen en la FI. Rechazo de imagen: IRR = (1 + 2 g cos(phi) + g^2)/(1 - 2 g cos(phi) + g^2) (potencia), contra la suma fasorial directa.
Supuestos: mezclador ideal multiplicativo, filtro FI ideal, sin ruido. Validez: orientativa.
Tolerancia: amplitud de FI 0,5 dentro de 1e-3; IRR formula frente a fasores dentro de 1e-9.
"""
from __future__ import annotations
import math, platform

FS, FLO, FIF, N = 1000.0, 100.0, 20.0, 5000

def goertzel(x, f):
    w = 2 * math.pi * f / FS
    c = 2 * math.cos(w)
    s1 = s2 = 0.0
    for v in x:
        s0 = v + c * s1 - s2
        s2, s1 = s1, s0
    re = s1 - s2 * math.cos(w)
    im = s2 * math.sin(w)
    return 2 * math.hypot(re, im) / len(x)

def mezcla(frf):
    return [math.cos(2 * math.pi * frf * k / FS) * math.cos(2 * math.pi * FLO * k / FS) for k in range(N)]

def irr_formula(g, phi):
    return (1 + 2 * g * math.cos(phi) + g * g) / (1 - 2 * g * math.cos(phi) + g * g)

def irr_fasores(g, phi):
    # senal: se suma 1 + g e^{i phi}; imagen: 1 - g e^{i phi}
    s = abs(1 + g * complex(math.cos(phi), math.sin(phi))) ** 2
    i = abs(1 - g * complex(math.cos(phi), math.sin(phi))) ** 2
    return s / i

def calc():
    out = {}
    for nombre, f in (("senal", FLO + FIF), ("imagen", FLO - FIF), ("fuera", 250.0)):
        x = mezcla(f)
        out[nombre] = (f, goertzel(x, FIF), goertzel(x, f + FLO))
    irr = []
    for g, ph in ((1.0, 0.0), (1.02, math.radians(1.0)), (1.05, math.radians(3.0)), (1.2, math.radians(10.0))):
        if g == 1.0 and ph == 0.0:
            continue
        irr.append((g, ph, irr_formula(g, ph), irr_fasores(g, ph), 10 * math.log10(irr_formula(g, ph)),
                    10 * math.log10(4 / ((g - 1) ** 2 + ph ** 2))))
    return dict(m=out, irr=irr, frecimg=FLO - FIF)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'tono':<7} {'f_RF':>6} {'amplitud en FI (20)':>20} {'amplitud en suma':>17}")
    for k, (f, a, b) in r["m"].items():
        print(f"{k:<7} {f:6.1f} {a:20.4f} {b:17.4f}")
    print(f"{'g':>5} {'phi [grados]':>13} {'IRR formula':>12} {'IRR fasores':>12} {'IRR [dB]':>9} {'aprox. 4/(dg^2+phi^2) [dB]':>27}")
    for g, ph, a, b, db, ap in r["irr"]:
        print(f"{g:5.2f} {math.degrees(ph):13.1f} {a:12.2f} {b:12.2f} {db:9.2f} {ap:27.2f}")
    assert abs(r["m"]["senal"][1] - 0.5) < 1e-3 and abs(r["m"]["imagen"][1] - 0.5) < 1e-3
    assert r["m"]["fuera"][1] < 1e-3
    for g, ph, a, b, db, ap in r["irr"]:
        assert abs(a / b - 1) < 1e-9
    assert abs(r["irr"][0][4] - r["irr"][0][5]) < 0.1
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
