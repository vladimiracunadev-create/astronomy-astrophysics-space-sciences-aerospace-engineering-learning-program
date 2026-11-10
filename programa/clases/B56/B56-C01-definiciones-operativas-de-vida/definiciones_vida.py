#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C01: matriz de casos limite y coincidencia entre definiciones de vida.

Datos: SINTETICOS e ILUSTRATIVOS. Las seis propiedades (0/1) de cada caso las asigna el
autor de la clase como simplificacion didactica; no son mediciones ni una taxonomia
aceptada. Las definiciones D1 a D4 son reglas booleanas inventadas para el ejercicio, salvo
que D1 imita la frase de trabajo de la NASA ("sistema autosostenido capaz de evolucion
darwiniana", consultada el 2026-11-09 en astrobiology.nasa.gov/about).
Modelo: cada definicion es una funcion booleana de las propiedades. Se mide el acuerdo entre
pares con la proporcion de coincidencias y con el kappa de Cohen.
Supuestos: casos independientes; propiedades binarias. Validez: solo para esta lista de
8 casos. Tolerancia: igualdad exacta (aritmetica con fracciones).
"""
from __future__ import annotations
import platform
import sys
from fractions import Fraction

PROP = ("met", "repr", "evol", "limite", "homeo", "crece")
CASOS = {
    "bacteria":        (1, 1, 1, 1, 1, 1),
    "mula":            (1, 0, 0, 1, 1, 1),
    "virion libre":    (0, 0, 1, 1, 0, 0),
    "llama":           (1, 1, 0, 0, 0, 1),
    "cristal":         (0, 1, 0, 0, 0, 1),
    "prion":           (0, 1, 1, 0, 0, 0),
    "espora latente":  (0, 0, 1, 1, 0, 0),
    "ARN in vitro":    (0, 1, 1, 0, 0, 1),
}


def d1(p):  # autosostenido (metabolismo y limite) y evolucion darwiniana
    return int(p["met"] and p["limite"] and p["evol"])


def d2(p):  # lista de comprobacion: al menos 4 de 6
    return int(sum(p.values()) >= 4)


def d3(p):  # fisiologica
    return int(p["met"] and p["homeo"] and p["crece"])


def d4(p):  # solo evolutiva
    return int(p["repr"] and p["evol"])


DEFS = {"D1": d1, "D2": d2, "D3": d3, "D4": d4}


def kappa_marginales(a, b):
    n = len(a)
    po = Fraction(sum(x == y for x, y in zip(a, b)), n)
    pa, pb = Fraction(sum(a), n), Fraction(sum(b), n)
    pe = pa * pb + (1 - pa) * (1 - pb)
    return (po - pe) / (1 - pe) if pe != 1 else Fraction(1)


def kappa_tabla(a, b):
    t11 = sum(x == 1 and y == 1 for x, y in zip(a, b))
    t10 = sum(x == 1 and y == 0 for x, y in zip(a, b))
    t01 = sum(x == 0 and y == 1 for x, y in zip(a, b))
    t00 = sum(x == 0 and y == 0 for x, y in zip(a, b))
    den = (t11 + t10) * (t10 + t00) + (t11 + t01) * (t01 + t00)
    return Fraction(2 * (t11 * t00 - t10 * t01), den) if den else Fraction(1)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    veredictos = {k: [] for k in DEFS}
    for nombre, v in CASOS.items():
        p = dict(zip(PROP, v))
        fila = {k: f(p) for k, f in DEFS.items()}
        for k in DEFS:
            veredictos[k].append(fila[k])
        print(f"{nombre:15s} " + " ".join(f"{k}={fila[k]}" for k in DEFS))
    claves = list(DEFS)
    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):
            a, b = veredictos[claves[i]], veredictos[claves[j]]
            k1, k2 = kappa_marginales(a, b), kappa_tabla(a, b)
            assert k1 == k2, "las dos formas del kappa deben coincidir"
            acuerdo = sum(x == y for x, y in zip(a, b))
            print(f"{claves[i]}-{claves[j]}: acuerdo {acuerdo}/8 ; kappa = {float(k1):.3f}")
    # Prueba 2: una definicion consigo misma da kappa 1 o indefinido (=1 por convencion)
    assert kappa_tabla(veredictos["D1"], veredictos["D1"]) == 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
