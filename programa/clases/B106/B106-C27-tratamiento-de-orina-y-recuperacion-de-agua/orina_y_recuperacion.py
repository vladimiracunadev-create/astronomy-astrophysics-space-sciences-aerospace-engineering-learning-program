#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C27: recuperacion de agua de la orina: concentracion de la salmuera, precipitacion de sulfato de calcio y energia de destilacion.

Consultado (OCHMO-TB-002): en la ISS el ensamble de destilacion de orina tuvo acumulacion de sulfato de calcio por el aumento de calcio urinario en microgravedad; se redujo la tasa de recuperacion
para evitar la precipitacion, se cambiaron los productos de pretratamiento para permitir una recuperacion mayor y un procesador de salmuera permitio recuperar mas del 90 % del agua.
ILUSTRATIVOS (no consultados): calcio de 2 mmol/L y sulfato de 3 mmol/L en la orina pretratada, producto de solubilidad de CaSO4·2H2O de 3.1e-5 mol2/L2 (valor de manual; sin
coeficientes de actividad), orina de 1.5 L/dia por persona (C10), calor latente de 2.26 MJ/kg y un factor de recuperacion de calor de 10 en la compresion de vapor.
Modelo: con recuperacion r el factor de concentracion es CF = 1/(1 - r) y el producto ionico se multiplica por CF^2; precipita si IP > Ksp.
Verificacion: r_max = 1 - sqrt(IP0/Ksp) se comprueba con IP(r_max) = Ksp; la masa se conserva (agua recuperada + salmuera = orina).
"""
from __future__ import annotations
import math
import platform
import numpy as np

KSP, LV = 3.1e-5, 2.26e6


def r_max(ca, so4):
    ip0 = ca * so4
    return 1 - math.sqrt(ip0 / KSP)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: concentraciones, Ksp y factores ILUSTRATIVOS (valores de manual no consultados); el limite por sulfato de calcio y el procesador de salmuera son los de OCHMO-TB-002 (consultado)")
    R = {}
    casos = [("calcio 2, sulfato 3 mmol/L", 2e-3, 3e-3), ("pretratamiento con menos sulfato (1)", 2e-3, 1e-3), ("calcio y sulfato bajos (0.5 y 0.6)", 0.5e-3, 0.6e-3), ("calcio 4, sulfato 3", 4e-3, 3e-3)]
    print("Recuperacion maxima antes de precipitar CaSO4 segun la composicion de la orina pretratada:")
    print("   caso                                    IP0 [mol2/L2]   IP0/Ksp   r_max")
    for nom, ca, so4 in casos:
        ip0 = ca * so4
        r = r_max(ca, so4)
        print(f"   {nom:38s} {ip0:12.2e}   {ip0/KSP:7.3f}   {max(r,0):6.3f}")
        R[nom] = (ip0, r)
        if r > 0:
            assert abs(ip0 / (1 - r) ** 2 - KSP) / KSP < 1e-9
    R["r_a"], R["r_b"], R["r_c"], R["r_d"] = R[casos[0][0]][1], R[casos[1][0]][1], R[casos[2][0]][1], R[casos[3][0]][1]
    print("Evolucion del producto ionico con la recuperacion (calcio 2, sulfato 3 mmol/L): IP/Ksp = IP0 CF^2 / Ksp")
    ip0 = 2e-3 * 3e-3
    for r in (0.0, 0.3, 0.5, 0.56, 0.7, 0.9):
        cf = 1 / (1 - r)
        print(f"   r = {r:4.2f}: CF = {cf:5.2f}; IP/Ksp = {ip0*cf**2/KSP:7.2f} {'PRECIPITA' if ip0*cf**2 > KSP else ''}")
    R["ratio90"] = ip0 * (1 / (1 - 0.9)) ** 2 / KSP
    # dos etapas en serie: orina + procesador de salmuera con pretratamiento mejor en la segunda
    crew, vol = 4, 1.5
    orina = crew * vol
    r1, r2 = 0.746, 0.65
    rt = r1 + (1 - r1) * r2
    agua1 = orina * r1
    sal1 = orina - agua1
    agua2 = sal1 * r2
    sal2 = sal1 - agua2
    R.update(orina=orina, rt=rt, sal2=sal2, agua=agua1 + agua2)
    print(f"Dos etapas en serie con {orina:.1f} L/dia de orina: la primera (r = {r1}) recupera {agua1:.2f} L, la de salmuera (r = {r2}) {agua2:.2f} L -> total {agua1+agua2:.2f} L ({100*rt:.1f} %), salmuera final {sal2:.2f} L")
    assert abs((agua1 + agua2 + sal2) - orina) < 1e-9 and rt > 0.9
    e_wh = LV / 3600.0
    cop = 10.0
    P_w = 6.0 * (LV / cop) / 86400.0 * 1.0
    R.update(e_wh=e_wh, P_w=P_w, agua_kg=agua1 + agua2)
    print(f"Energia: evaporar 1 kg exige {e_wh:.0f} Wh sin recuperar calor y {e_wh/cop:.0f} Wh con factor {cop:.0f}; para {agua1+agua2:.2f} kg/dia: {(agua1+agua2)*e_wh/cop/24:.1f} W con recuperacion y {(agua1+agua2)*e_wh/24:.0f} W sin ella")
    R["P_con"], R["P_sin"] = (agua1 + agua2) * e_wh / cop / 24, (agua1 + agua2) * e_wh / 24
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
