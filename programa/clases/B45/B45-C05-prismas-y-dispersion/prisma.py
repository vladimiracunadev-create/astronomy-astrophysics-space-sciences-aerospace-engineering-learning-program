#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C05: indice de Sellmeier, desviacion minima y dispersion de un prisma.

Datos: coeficientes de Sellmeier del vidrio BK7 tal como los lista la pagina Sellmeier equation de Wikipedia (consultada el 2026-11-09): B1 = 1,03961212, B2 = 0,231792344,
B3 = 1,01046945, C1 = 6,00069867e-3, C2 = 2,00179144e-2 y C3 = 1,03560653e2 (micras al cuadrado). La pagina no da n a 587,6 nm; el valor se calcula aqui. Angulo de vertice 60 grados y base de
50 mm son valores ILUSTRATIVOS. No se ha consultado el catalogo del fabricante.
Modelo: n^2 = 1 + sum B_i l^2/(l^2 - C_i); desviacion minima n = sin((A+D)/2)/sin(A/2); poder de resolucion R = b |dn/dl|.
Supuestos: prisma isosceles en desviacion minima, haz colimado, sin absorcion. Validez: rango 0,3 a 2,5 micras de la forma de Sellmeier.
Tolerancia: dD/dl analitica frente a diferencia finita a 1e-6 relativo; indice a 587,6 nm entre 1,5160 y 1,5175.
"""
from __future__ import annotations
import math, platform, sys

B = (1.03961212, 0.231792344, 1.01046945)
Cc = (6.00069867e-3, 2.00179144e-2, 1.03560653e2)
A = math.radians(60.0)
BASE = 0.050


def n_of(l_um):
    l2 = l_um ** 2
    return math.sqrt(1 + sum(b * l2 / (l2 - c) for b, c in zip(B, Cc)))


def dn_dl(l_um):
    """Derivada analitica en 1/micra."""
    l2 = l_um ** 2
    d = sum(b * (-2 * l_um * c) / (l2 - c) ** 2 for b, c in zip(B, Cc))
    return d / (2 * n_of(l_um))


def dmin(l_um):
    return 2 * math.asin(n_of(l_um) * math.sin(A / 2)) - A


def calcular():
    r = {}
    r["nd"] = n_of(0.5876)
    r["nF"] = n_of(0.4861)
    r["nC"] = n_of(0.6563)
    r["abbe"] = (r["nd"] - 1) / (r["nF"] - r["nC"])
    r["tabla"] = [(l, n_of(l / 1000), math.degrees(dmin(l / 1000))) for l in (400, 450, 500, 550, 600, 650, 700)]
    l = 0.55
    h = 1e-5
    r["dD_num"] = (dmin(l + h) - dmin(l - h)) / (2 * h)            # rad por micra
    n = n_of(l)
    D = dmin(l)
    r["dD_ana"] = dn_dl(l) * 2 * math.sin(A / 2) / math.cos((A + D) / 2)
    r["dn_dl_550"] = dn_dl(l) * 1e3                                 # por mm... (1/micra -> 1e3 por mm)
    r["R550"] = BASE * abs(dn_dl(l)) * 1e6                          # b en m, dn/dl en 1/m
    r["dlam_nm"] = 550 / r["R550"]
    r["razon"] = abs(dn_dl(0.40)) / abs(dn_dl(0.70))
    r["disp_mrad_nm"] = abs(r["dD_ana"]) * 1e-3 * 1e3             # rad/micra -> mrad/nm
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"n(587,6 nm) = {r['nd']:.5f} ; n(486,1) = {r['nF']:.5f} ; n(656,3) = {r['nC']:.5f} ; numero de Abbe = {r['abbe']:.2f}")
    print(f"{'lambda (nm)':>12} {'n':>9} {'D min (grados)':>15}")
    for l, n, d in r["tabla"]:
        print(f"{l:12d} {n:9.5f} {d:15.4f}")
    print(f"dD/dlambda en 550 nm: numerica {r['dD_num']:.6e} ; analitica {r['dD_ana']:.6e} rad/micra ({r['disp_mrad_nm']:.4f} mrad/nm)")
    print(f"R = b |dn/dl| con b = 50 mm: {r['R550']:.0f} ; delta lambda = {r['dlam_nm']:.3f} nm")
    print(f"cociente |dn/dl| 400 nm / 700 nm = {r['razon']:.2f}")
    assert 1.5160 < r["nd"] < 1.5175
    assert abs(r["dD_num"] / r["dD_ana"] - 1) < 1e-6
    assert r["razon"] > 3
    assert 50 < r["abbe"] < 70
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
