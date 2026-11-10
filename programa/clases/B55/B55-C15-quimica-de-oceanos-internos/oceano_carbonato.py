#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C15: pH de un oceano interno SINTETICO por equilibrio carbonato y balance de carga.

Datos: ILUSTRATIVOS. Constantes de equilibrio K1 = 4.5e-7, K2 = 4.7e-11 y Kw = 1.0e-14 (valores de orden de magnitud para agua cerca de 25 C; NO se consultaron ni se corrigen por
temperatura, presion o salinidad); concentracion de sodio 1.0e-2 mol/kg y CO2 disuelto 1.0e-3 mol/kg (sinteticos). Waite et al. (2017) y Hsu et al. (2015) se consultaron solo
por resumenes truncados (hidrogeno molecular y sales de sodio en el penacho de Encelado); no se uso ninguna cifra suya.
Modelo: balance de carga [Na+] + [H+] = [HCO3-] + 2 [CO3 2-] + [OH-] con [HCO3-] = K1 c / [H+], [CO3 2-] = K1 K2 c / [H+]^2, [OH-] = Kw / [H+]; se resuelve por biseccion en pH.
Supuestos: solucion ideal (actividad = concentracion); CO2 disuelto fijo; solo especies de carbonato y sodio. Validez: ilustrativa, no representa ningun oceano real.
Tolerancia: residuo del balance de carga < 1e-12 mol/kg; caso sin carbonato (c -> 0) frente a la solucion cuadratica a 1e-6 en pH.
"""
from __future__ import annotations
import math, platform

K1, K2, KW = 4.5e-7, 4.7e-11, 1.0e-14

def residuo(ph, na, c):
    h = 10 ** (-ph)
    return na + h - (K1 * c / h + 2 * K1 * K2 * c / h ** 2 + KW / h)

def resolver(na, c, lo=0.0, hi=14.0):
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if residuo(lo, na, c) * residuo(mid, na, c) <= 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    na, c = 1.0e-2, 1.0e-3
    ph = resolver(na, c)
    h = 10 ** (-ph)
    hco3, co3, oh = K1 * c / h, K1 * K2 * c / h ** 2, KW / h
    print("A. Oceano SINTETICO: [Na+] = 1e-2 mol/kg ; CO2 disuelto = 1e-3 mol/kg ; K1 = 4.5e-7 ; K2 = 4.7e-11 ; Kw = 1e-14 (ILUSTRATIVOS)")
    print(f"B. pH = {ph:.4f} ; [H+] = {h:.4e} ; [HCO3-] = {hco3:.4e} ; [CO3 2-] = {co3:.4e} ; [OH-] = {oh:.4e} mol/kg")
    res = abs(residuo(ph, na, c))
    print(f"   residuo del balance de carga = {res:.2e} mol/kg")
    assert res < 1e-12
    # fraccion de especies
    tot = c + hco3 + co3
    print(f"C. Fracciones del carbono disuelto total (CO2 + HCO3- + CO3 2-): CO2 {c / tot:.4f} ; HCO3- {hco3 / tot:.4f} ; CO3 2- {co3 / tot:.4f}")
    # caso sin carbonato: Na + H = Kw/H  =>  H^2 + Na H - Kw = 0
    na2 = 1.0e-3
    ph_num = resolver(na2, 1e-30)
    h_an = (-na2 + math.sqrt(na2 ** 2 + 4 * KW)) / 2.0
    ph_an = -math.log10(h_an)
    print(f"D. Prueba sin carbonato (NaOH puro 1e-3): pH numerico = {ph_num:.6f} ; analitico = {ph_an:.6f}")
    assert abs(ph_num - ph_an) < 1e-6
    print("E. pH frente a la concentracion de CO2 disuelto (Na = 1e-2 mol/kg)")
    print("c(CO2) [mol/kg]   pH")
    previo = 99.0
    for cc in (1e-5, 1e-4, 1e-3, 1e-2, 1e-1):
        p = resolver(na, cc)
        print(f"{cc:12.0e}      {p:.4f}")
        assert p < previo
        previo = p
    print("F. pH frente a [Na+] (CO2 = 1e-3 mol/kg)")
    print("[Na+] [mol/kg]   pH")
    previo = -1.0
    for nn in (1e-4, 1e-3, 1e-2, 1e-1):
        p = resolver(nn, c)
        print(f"{nn:12.0e}      {p:.4f}")
        assert p > previo
        previo = p
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
