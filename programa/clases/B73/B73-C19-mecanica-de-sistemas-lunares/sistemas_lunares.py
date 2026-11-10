#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C19: mecanica de sistemas lunares: esfera de Hill, precesion por J2 y plano de Laplace en Jupiter y Saturno.

Datos consultados (2026-11-10): Jupiter: GM 126.687e6 km3/s2, radio ecuatorial 71 492 km, J2 = 14 736e-6, semieje 778.479e6 km, periodo 4332.589 d
(NASA/NSSDC, Jupiter Fact Sheet, 2024-10-02); Saturno: radio ecuatorial 60 268 km, J2 = 16 298e-6, masa 568.32e24 kg (Saturn Fact Sheet, 2025-03-18), distancia al Sol 1432.0e6 km
(Planetary Fact Sheet, 2025-03-18); GM del Sol 132 712e6 km3/s2 (Sun Fact Sheet); G = 6.67430e-11 (CODATA 2018 citada por el JPL) -> GM_Saturno ~ 3.7931e7 km3/s2;
semiejes de Io, Europa, Ganymede, Callisto 421 800; 671 100; 1 070 400; 1 882 700 km y periodos 1.769138; 3.551181; 7.154553; 16.689017 d (Jovian Satellite Fact Sheet, 2023-12-06);
Titan 1 221 870 km y Iapetus 3 560 850 km (Saturnian Satellite Fact Sheet, 2025-07-22); periodos de precesion apsidal Papsis = 1.333, 1.394, 68.301, 277.921 anos y nodal
Pnode = (0.000), 30.202, 137.812, 577.264 anos de los galileanos (JPL SSD, elementos medios de satelites, J2000, plano de Laplace).
Modelo (formulas clasicas, no consultadas): regresion nodal por J2: dOmega/dt = -(3/2) J2 (R/a)^2 n ; precesion apsidal por J2 (i ~ 0): 3 J2 (R/a)^2 n ;
regresion nodal por el Sol (perturbador circular, i pequena): -(3/4) n_p^2 / n ; radio de Laplace r_L^5 = 2 J2 R^2 a_p^3 GM_planeta/GM_Sol (se define aqui igualando las dos tasas nodales; otras
referencias lo definen con otro factor numerico). Radio de Hill R_H = a_p (GM_p / 3 GM_Sol)^(1/3).
Segunda via: (a) las tasas J2 y solar son iguales en r_L (evaluadas por separado); (b) el periodo de precesion apsidal de Io del JPL (1.333 anos) frente a la circulacion
de la conjuncion Io-Europa de B73-C10 (n_Io - 2 n_Europa con los periodos de la ficha NASA).
No hay datos sinteticos. Tolerancias: igualdad de tasas en r_L < 1e-9 relativo ; Papsis(Io) frente a la circulacion de conjuncion < 0.5 %.
"""
from __future__ import annotations
import json, math, platform, sys

GM_S_SOL = 132712e6
JUP = dict(gm=126.687e6, R=71492.0, J2=14736e-6, a=778.479e6, P=4332.589)
SAT = dict(gm=6.67430e-11 * 568.32e24 / 1e9, R=60268.0, J2=16298e-6, a=1432.0e6)
SAT["P"] = 2 * math.pi * math.sqrt(SAT["a"] ** 3 / GM_S_SOL) / 86400
GAL = [("Io", 421800.0, 1.769138, 1.333, None), ("Europa", 671100.0, 3.551181, 1.394, 30.202), ("Ganymede", 1070400.0, 7.154553, 68.301, 137.812), ("Callisto", 1882700.0, 16.689017, 277.921, 577.264)]
D_ANIO = 365.25


def r_laplace(p):
    return (2 * p["J2"] * p["R"] ** 2 * p["a"] ** 3 * p["gm"] / GM_S_SOL) ** 0.2


def tasa_j2(p, a, n):
    return 1.5 * p["J2"] * (p["R"] / a) ** 2 * n


def tasa_sol(n_p, n):
    return 0.75 * n_p**2 / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    rh_j = JUP["a"] * (JUP["gm"] / (3 * GM_S_SOL)) ** (1 / 3)
    rh_s = SAT["a"] * (SAT["gm"] / (3 * GM_S_SOL)) ** (1 / 3)
    print(f"Radio de Hill: Jupiter = {rh_j:,.0f} km ; Saturno = {rh_s:,.0f} km (con la distancia al Sol de la ficha)")
    rl_j, rl_s = r_laplace(JUP), r_laplace(SAT)
    print(f"Radio de Laplace (igualdad de tasas nodales J2 y solar): Jupiter = {rl_j:,.0f} km ({rl_j / JUP['R']:.1f} R_J ; {rl_j / rh_j:.4f} R_H) ; Saturno = {rl_s:,.0f} km ({rl_s / SAT['R']:.1f} R_S ; {rl_s / rh_s:.4f} R_H)")
    out.update(rhj=rh_j, rhs=rh_s, rlj=rl_j, rls=rl_s, rlj_R=rl_j / JUP["R"], rls_R=rl_s / SAT["R"])
    # segunda via (a): igualdad de tasas en r_L
    n_pk = math.sqrt(GM_S_SOL / JUP["a"] ** 3)  # movimiento medio kepleriano de Jupiter (consistente con r_L)
    n_l = math.sqrt(JUP["gm"] / rl_j**3)
    iguales = abs(tasa_j2(JUP, rl_j, n_l) / tasa_sol(n_pk, n_l) - 1)
    n_p = 2 * math.pi / (JUP["P"] * 86400)
    print(f"Comprobacion en el radio de Laplace de Jupiter (n_p kepleriano de Jupiter): tasa J2 / tasa solar - 1 = {iguales:.1e}")
    out["iguales"] = iguales
    print("Galileanos: precesion por J2 (y J2 + Sol) frente a los periodos del JPL (anos):")
    print(" luna       a/R_J   a/rL    P_apsis J2   P_apsis JPL    P_nodo J2   P_nodo J2+Sol   P_nodo JPL")
    for nom, a, P, pa, pn in GAL:
        n = 2 * math.pi / (P * 86400)  # rad/s
        pas_j2 = 2 * math.pi / (3 * JUP["J2"] * (JUP["R"] / a) ** 2 * n) / 86400 / D_ANIO
        nod_j2 = 2 * math.pi / tasa_j2(JUP, a, n) / 86400 / D_ANIO
        nod_tot = 2 * math.pi / (tasa_j2(JUP, a, n) + tasa_sol(n_p, n)) / 86400 / D_ANIO
        txt_pn = f"{pn:10.3f}" if pn else "         -"
        print(f" {nom:9s} {a / JUP['R']:6.2f}  {a / rl_j:6.3f}  {pas_j2:11.3f}  {pa:11.3f}  {nod_j2:11.3f}  {nod_tot:12.3f}  {txt_pn}")
        out[f"{nom}_aR"], out[f"{nom}_arl"], out[f"{nom}_pasj2"], out[f"{nom}_nodj2"], out[f"{nom}_nodtot"] = a / JUP["R"], a / rl_j, pas_j2, nod_j2, nod_tot
    # Io: periodo apsidal del JPL frente a circulacion de conjuncion
    nIo, nEu = 360 / GAL[0][2], 360 / GAL[1][2]
    circ = 360 / (nIo - 2 * nEu)
    dif = abs(GAL[0][3] * D_ANIO / circ - 1)
    print(f"Io: P_apsis (JPL) = {GAL[0][3]} anos = {GAL[0][3] * D_ANIO:.1f} d ; circulacion de la conjuncion Io-Europa (B73-C10) = {circ:.1f} d ; diferencia = {dif:.2%}")
    out.update(circ=circ, difio=dif, io_pas_d=GAL[0][3] * D_ANIO)
    # Titan y Iapetus
    titan, iapetus = 1221870.0, 3560850.0
    print(f"Saturno: Titan a/r_L = {titan / rl_s:.3f} ; Iapetus a/r_L = {iapetus / rl_s:.3f} ; Titan a/R_H = {titan / rh_s:.4f} ; Iapetus a/R_H = {iapetus / rh_s:.4f}")
    out.update(tit=titan / rl_s, iap=iapetus / rl_s, tit_h=titan / rh_s, iap_h=iapetus / rh_s, cal_h=1882700.0 / rh_j)
    assert iguales < 1e-9 and dif < 0.005
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
