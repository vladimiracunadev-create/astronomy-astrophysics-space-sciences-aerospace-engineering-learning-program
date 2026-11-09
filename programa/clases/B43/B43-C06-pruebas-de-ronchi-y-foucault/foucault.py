#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C06: pruebas de Foucault y Ronchi por trazado exacto de rayos desde el centro de curvatura.

Datos: ILUSTRATIVOS (espejo de R = 2400 mm, D = 200 mm; fuente puntual en el eje a la distancia R del vertice; rejilla de Ronchi de 100 lineas/pulgada = 0,254 mm de periodo; desplazamiento 5 mm). Sin datos medidos.
Modelo: rayos meridionales exactos desde una fuente puntual en (0, R) reflejados por una esfera o un paraboloide; el cruce con el eje da la lectura de la cuchilla de Foucault.
Para el paraboloide la lectura relativa al centro de curvatura es y^2/R (aberracion longitudinal); para la esfera es nula. Ronchi: con la rejilla desplazada d del foco, el haz mide D d/R en la rejilla y el numero de bandas es D d/(R p).
Verificacion independiente: formulas cerradas frente al trazado numerico; el recuento de Ronchi se obtiene trazando los dos rayos de borde.
Supuestos: geometria, sin difraccion; fuente puntual; meridional. Validez: d << R.
Tolerancia: lectura de Foucault, 2 % relativo (tercer orden); bandas de Ronchi, 2 % relativo.
"""
from __future__ import annotations
import math, platform

R = 2400.0; D = 200.0; P = 25.4 / 100

def sag_par(y):
    return y * y / (2 * R)

def sag_esf(y):
    return y * y / (R + math.sqrt(R * R - y * y))

def reflejar(y, sag, dsag):
    z = sag(y)
    n = (-dsag(y), 1.0); nn = math.hypot(*n); n = (n[0] / nn, n[1] / nn)
    d = (y - 0.0, z - R); dn = math.hypot(*d); d = (d[0] / dn, d[1] / dn)
    k = d[0] * n[0] + d[1] * n[1]
    d2 = (d[0] - 2 * k * n[0], d[1] - 2 * k * n[1])
    return (y, z), d2

def cruce_eje(y, sag, dsag):
    p, d = reflejar(y, sag, dsag)
    t = -p[0] / d[0]
    return p[1] + t * d[1]

def dpar(y): return y / R
def desf(y): return y / math.sqrt(R * R - y * y)

def calc():
    r = {}
    zonas = [20.0, 40.0, 60.0, 80.0, 100.0]
    tabla = []
    for y in zonas:
        lp = cruce_eje(y, sag_par, dpar) - R
        le = cruce_eje(y, sag_esf, desf) - R
        tabla.append((y, lp, y * y / R, le))
    r["foucault"] = tabla
    # Ronchi: rayos de borde cruzan el plano a distancia d antes del foco paraxial R/2 (imagen de la fuente en R)
    d = 5.0
    zplano = R - d
    def y_en_plano(y):
        p, dd = reflejar(y, sag_esf, desf)
        t = (zplano - p[1]) / dd[1]
        return p[0] + t * dd[0]
    # la imagen esta en el eje: el haz en el plano mide el doble del cruce
    ancho = abs(y_en_plano(D / 2) - y_en_plano(-D / 2))
    r["ancho_haz_mm"] = ancho
    r["ancho_formula_mm"] = D * d / R
    r["bandas_ronchi"] = ancho / P
    r["bandas_formula"] = D * d / (R * P)
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print("zona y (mm) | lectura paraboloide (mm) | y^2/R (mm) | lectura esfera (mm)")
    for y, lp, f, le in r["foucault"]:
        print(f"{y:.0f} | {lp:.5f} | {f:.5f} | {le:.2e}")
    for k in ("ancho_haz_mm", "ancho_formula_mm", "bandas_ronchi", "bandas_formula"):
        print(f"{k} = {r[k]:.6g}")
    for y, lp, f, le in r["foucault"]:
        assert abs(lp - f) / f < 0.02 and abs(le) < 1e-8
    assert abs(r["bandas_ronchi"] - r["bandas_formula"]) / r["bandas_formula"] < 0.02
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
