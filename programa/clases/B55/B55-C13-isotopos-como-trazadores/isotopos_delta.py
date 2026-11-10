#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C13: notacion delta, mezcla de reservorios y fraccionamiento dependiente de la masa.

Datos (NIST, Atomic Weights and Isotopic Compositions, consultado el 2026-11-09): masas atomicas relativas de O-16 (15.99491461957), O-17 (16.99913175650), O-18 (17.99915961286);
composiciones isotopicas de H-1 (0.999885), H-2 (0.000115), O-16 (0.99757), O-17 (0.00038), O-18 (0.00205). Las razones de REFERENCIA del script se calculan con esas composiciones
y NO son el estandar internacional de agua oceanica (VSMOW), que no se consulto. Las muestras, concentraciones y fraccionamientos son SINTETICOS.
Modelo: delta = (R_muestra / R_ref - 1) * 1000 [permil] ; mezcla de dos reservorios con concentraciones C1, C2: se mezclan los NUMEROS de atomos de cada isotopo y se vuelve a delta ;
exponente de fraccionamiento dependiente de la masa beta = (1/m16 - 1/m17) / (1/m16 - 1/m18) ; delta' = 1000 ln(1 + delta/1000) ; Delta'17O = delta'17 - beta delta'18.
Supuestos: fraccionamiento de tipo ley de potencias; reservorios sin cambios de concentracion. Validez: ilustrativa.
Tolerancia: mezcla exacta vs formula ponderada por concentracion a 1e-9 permil; Delta'17O de una muestra fraccionada con el mismo beta igual a cero a 1e-9 permil.
"""
from __future__ import annotations
import math, platform

M16, M17, M18 = 15.99491461957, 16.99913175650, 17.99915961286
A16, A17, A18 = 0.99757, 0.00038, 0.00205
R17_REF, R18_REF = A17 / A16, A18 / A16
RD_REF = 0.000115 / 0.999885
BETA = (1 / M16 - 1 / M17) / (1 / M16 - 1 / M18)

def delta(r, ref):
    return (r / ref - 1.0) * 1000.0

def lnd(d):
    return 1000.0 * math.log(1.0 + d / 1000.0)

def mezcla(d1, c1, d2, c2, f):
    """fraccion f del reservorio 1; c = atomos del isotopo pesado + ligero ~ concentracion total; delta en relacion a R_ref con R pequena."""
    # numero de atomos ligeros ~ concentracion total; numero de pesados = R * ligeros
    r1 = RD_REF * (1 + d1 / 1000.0); r2 = RD_REF * (1 + d2 / 1000.0)
    n_l = f * c1 + (1 - f) * c2
    n_p = f * c1 * r1 + (1 - f) * c2 * r2
    return delta(n_p / n_l, RD_REF)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"A. Razones de REFERENCIA (de las composiciones NIST; no son VSMOW): 17O/16O = {R17_REF:.6e} ; 18O/16O = {R18_REF:.6e} ; D/H = {RD_REF:.6e}")
    print(f"B. Exponente de fraccionamiento dependiente de la masa beta = (1/m16 - 1/m17)/(1/m16 - 1/m18) = {BETA:.6f}")
    # muestra SINTETICA con delta18 conocido y fraccionamiento exactamente mass-dependent
    print("C. Muestras SINTETICAS fraccionadas con beta: delta'18 prescrito, delta'17 = beta delta'18 => Delta'17O = 0")
    print("delta18 [permil]  delta17 [permil]  Delta'17O [permil]")
    for d18 in (-20.0, -5.0, 5.0, 12.0, 30.0):
        l18 = lnd(d18)
        l17 = BETA * l18
        d17 = 1000.0 * (math.exp(l17 / 1000.0) - 1.0)
        D17 = lnd(d17) - BETA * lnd(d18)
        print(f"{d18:12.2f}      {d17:12.4f}      {D17:14.3e}")
        assert abs(D17) < 1e-9
    # un exceso de 17O (no dependiente de la masa), SINTETICO
    d18, d17 = 10.0, 5.80 + 0.0
    D = lnd(d17) - BETA * lnd(d18)
    print(f"D. Muestra SINTETICA con delta17 = {d17} y delta18 = {d18} permil : Delta'17O = {D:.4f} permil (no dependiente de la masa si es distinto de cero)")
    # mezcla D/H
    print("E. Mezcla de dos reservorios SINTETICOS de D/H (delta en permil respecto de la referencia NIST)")
    d1, c1, d2, c2 = -200.0, 1.0, 1500.0, 0.2
    print("f(res.1)   delta mezcla (exacto)   formula ponderada por c   lineal en f")
    for f in (0.0, 0.25, 0.5, 0.75, 1.0):
        ex = mezcla(d1, c1, d2, c2, f)
        w = f * c1 / (f * c1 + (1 - f) * c2)
        pond = w * d1 + (1 - w) * d2
        lin = f * d1 + (1 - f) * d2
        print(f"{f:7.2f}   {ex:14.6f}        {pond:14.6f}          {lin:10.4f}")
        assert abs(ex - pond) < 1e-9, (f, ex, pond)
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
