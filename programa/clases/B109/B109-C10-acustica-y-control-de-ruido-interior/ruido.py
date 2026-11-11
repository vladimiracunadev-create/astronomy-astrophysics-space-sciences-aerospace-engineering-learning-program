#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C10: presupuesto de ruido de una cabina (suma de fuentes, campo reverberante de Sabine y comparacion con limites).

Datos consultados (2026-11-10; resumen tecnico OCHMO-TB-035 Rev C, derivado de NASA-STD-3001 Vol. 2 Rev D): limite de ruido peligroso < 85 dBA sin importar la duracion [V2 6077];
ruido continuo en areas de trabajo limitado por la curva NC-50 (70 dB a 63 Hz, 45 dB a 8 kHz; 50 dB a 1.5 kHz segun el resumen) [V2 6078] y en areas de sueno por NC-40 si la mision supera 30 dias [V2 6079];
Spacelab (STS-40): 68 dBA de media diaria, hasta 75.5 dBA y 84 dBA con el ergometro, con problemas de comunicacion; el limite de dosis 100 equivale a 85 dBA durante 8 h (ruido de lanzamiento).
Burke, Howard y Kessler (2022): volumen habitable ~127 m3.
ILUSTRATIVOS / NO CONSULTADOS: niveles de potencia sonora de las fuentes (ventilador 58 dBA x2, bomba 55, compresor 62), coeficiente medio de absorcion 0.20, superficie equivalente 6 V^(2/3),
factor de directividad Q = 2 (fuente junto a una pared), tasa de intercambio de 3 dB para la dosis, objetivo de diseno de 50 dBA, valores por banda de NC-40 y NC-50 (no consultados; no se usan).
Modelo: A = alpha S; T60 = 0.161 V / A (Sabine); R = A / (1 - alpha); Lp(r) = Lw + 10 log10(Q/(4 pi r^2) + 4/R); suma energetica de fuentes.
Segunda via: N fuentes iguales suman 10 log10 N (1e-9); a la distancia critica r_c = sqrt(Q R /(16 pi)) el campo directo iguala al reverberante, asi que Lp = Lw + 10 log10(8/R) (1e-9);
a gran distancia Lp -> Lw + 10 log10(4/R).
Unidades: nivel de presion sonora [dBA re 20 uPa]; potencia sonora [dBA re 1 pW]; volumen [m3]; area [m2]; distancia [m]; tiempo [s o h].
"""
from __future__ import annotations
import math, platform

V = 127.0
ALPHA = 0.20
Q = 2.0
FUENTES = {"ventilador 1": 58.0, "ventilador 2": 58.0, "bomba de agua": 55.0, "compresor de esclusa": 62.0}
LIM_PELIGROSO = 85.0
OBJETIVO = 50.0
TASA = 3.0


def suma_db(xs):
    return 10 * math.log10(sum(10 ** (x / 10) for x in xs))


def lp(lw, r, rcte):
    return lw + 10 * math.log10(Q / (4 * math.pi * r * r) + 4 / rcte)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Fuentes, absorcion y objetivo ILUSTRATIVOS; limites y niveles de Spacelab del resumen OCHMO-TB-035 Rev C; V = 127 m3 (Burke et al. 2022)")
    s_tot = 6 * V ** (2 / 3)
    a = ALPHA * s_tot
    t60 = 0.161 * V / a
    rcte = a / (1 - ALPHA)
    rc = math.sqrt(Q * rcte / (16 * math.pi))
    print(f"S = {s_tot:.1f} m2 ; A = {a:.1f} m2 ; T60 = {t60:.2f} s ; R = {rcte:.1f} m2 ; distancia critica = {rc:.2f} m")
    lw_tot = suma_db(FUENTES.values())
    print(f"Potencia sonora total = {lw_tot:.1f} dBA")
    assert abs(suma_db([58.0, 58.0]) - (58.0 + 10 * math.log10(2))) < 1e-9
    print(" distancia a las fuentes [m]   Lp total [dBA]   margen frente al objetivo de 50 dBA [dB]   margen frente al limite de 85 dBA [dB]")
    for r in (1.0, 2.0, 3.0, 5.0):
        niv = suma_db([lp(lw, r, rcte) for lw in FUENTES.values()])
        print(f"{r:25.1f} {niv:16.1f} {OBJETIVO - niv:41.1f} {LIM_PELIGROSO - niv:38.1f}")
    lim_lejos = lw_tot + 10 * math.log10(4 / rcte)
    print(f"Campo reverberante (r grande): Lp -> {lim_lejos:.1f} dBA")
    assert abs(lp(60.0, rc, rcte) - (60.0 + 10 * math.log10(8 / rcte))) < 1e-9
    print("Efecto de bajar 5 dB cada ventilador (53 dBA):")
    f2 = dict(FUENTES); f2["ventilador 1"] = 53.0; f2["ventilador 2"] = 53.0
    n1 = suma_db([lp(lw, 3.0, rcte) for lw in FUENTES.values()])
    n2 = suma_db([lp(lw, 3.0, rcte) for lw in f2.values()])
    print(f"   Lp a 3 m: {n1:.1f} -> {n2:.1f} dBA (ahorro {n1 - n2:.1f} dB)")
    f3 = dict(FUENTES); f3["compresor de esclusa"] = 52.0
    n3 = suma_db([lp(lw, 3.0, rcte) for lw in f3.values()])
    print(f"Efecto de bajar 10 dB el compresor (52 dBA): Lp a 3 m: {n1:.1f} -> {n3:.1f} dBA (ahorro {n1 - n3:.1f} dB)")
    assert n1 - n3 > n1 - n2
    print("Referencias publicadas (resumen OCHMO): Spacelab 68 dBA (media diaria), 75.5 dBA (max. diario), 84 dBA (con ergometro) ; limite peligroso 85 dBA")
    # dosis ilustrativa (3 dB de intercambio)
    perfil = [(16.0, 50.0), (6.0, 62.0), (2.0, 72.0)]  # horas, dBA (ILUSTRATIVO)
    dosis = sum(100 * h / (8 * 2 ** ((85 - L) / TASA)) for h, L in perfil)
    leq = 10 * math.log10(sum(h * 10 ** (L / 10) for h, L in perfil) / sum(h for h, _ in perfil))
    print(f"Dosis ilustrativa de un dia (16 h a 50, 6 h a 62, 2 h a 72 dBA; intercambio 3 dB) = {dosis:.1f} % ; Leq 24 h = {leq:.1f} dBA")
    assert abs(100 * 8 / (8 * 2 ** 0) - 100) < 1e-9
    assert dosis < 100
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
