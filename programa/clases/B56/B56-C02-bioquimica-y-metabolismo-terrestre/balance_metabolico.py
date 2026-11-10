#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B56-C02: balance atomico y energia libre de fotosintesis y respiracion.

Datos: h, c, N_A y e de NIST (CODATA 2022, consultados 2026-11-09). Energias libres
estandar de formacion a 298,15 K (kJ/mol): CO2(g) -394,36; H2O(l) -237,13; glucosa(ac)
-917,2; O2 = 0. Son valores de TABLA DE LIBRO DE TEXTO recordados por el autor y NO
consultados en esta sesion; se usan como ILUSTRATIVOS. La longitud de onda de 680 nm y las
48 fotones por glucosa son valores didacticos ilustrativos, no consultados.
Modelo: Delta G = sum(nu_i G_f,i). Eficiencia = Delta G / energia de los fotones absorbidos.
Supuestos: condiciones estandar (1 M, 1 bar), sin correccion por pH ni concentraciones.
Validez: solo estandar; no representa una celula. Tolerancia: balance atomico exacto;
Hess y simetria con 1e-9 kJ/mol.
"""
from __future__ import annotations
import math
import platform
import re
import sys

H = 6.62607015e-34
C = 299792458.0
NA = 6.02214076e23
GF = {"CO2": -394.36, "H2O": -237.13, "C6H12O6": -917.2, "O2": 0.0}
FOTO = ({"CO2": 6, "H2O": 6}, {"C6H12O6": 1, "O2": 6})
RESP = (FOTO[1], FOTO[0])


def atomos(formula):
    d = {}
    for el, n in re.findall(r"([A-Z][a-z]?)(\d*)", formula):
        d[el] = d.get(el, 0) + int(n or 1)
    return d


def cuenta(lado):
    tot = {}
    for f, nu in lado.items():
        for el, n in atomos(f).items():
            tot[el] = tot.get(el, 0) + nu * n
    return tot


def delta_g(rx):
    reac, prod = rx
    return sum(nu * GF[f] for f, nu in prod.items()) - sum(nu * GF[f] for f, nu in reac.items())


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    for nombre, rx in (("fotosintesis", FOTO), ("respiracion", RESP)):
        assert cuenta(rx[0]) == cuenta(rx[1]), f"{nombre} no esta balanceada"
    dg_f, dg_r = delta_g(FOTO), delta_g(RESP)
    assert abs(dg_f + dg_r) < 1e-9, "la reaccion inversa debe invertir el signo"
    # Prueba independiente de Hess: ruta por componentes elementales
    ruta = 6 * (-GF["CO2"]) + 6 * (-GF["H2O"]) + GF["C6H12O6"]
    assert abs(ruta - dg_f) < 1e-9
    print("Balance atomico:", cuenta(FOTO[0]))
    print(f"Delta G fotosintesis = {dg_f:.1f} kJ/mol glucosa ; respiracion = {dg_r:.1f} kJ/mol")
    lam = 680e-9
    e_foton = H * C / lam * NA / 1000.0  # kJ por mol de fotones
    efic = dg_f / (48 * e_foton)
    print(f"Energia de un mol de fotones a 680 nm = {e_foton:.1f} kJ ; eficiencia con 48 fotones = {efic * 100:.1f} %")
    assert 0 < efic < 1
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
