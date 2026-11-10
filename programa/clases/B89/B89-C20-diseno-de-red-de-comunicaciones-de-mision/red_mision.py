#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B89-C20. Diseno de una red de comunicaciones de mision SINTETICA: enlace directo a la Tierra frente a relevo,
volumen de datos por dia y verificacion de requisitos por fase. Todo SINTETICO (equipo, distancias de fase, requisitos).
k, c: NIST CODATA 2022 (consultadas). UA redondeada ILUSTRATIVA."""
import math, sys

C = 299_792_458.0
K = 1.380649e-23
UA = 1.495978707e11

def db(x):
    return 10 * math.log10(x)

def tasa_max(d, f, pt_w, gt_dbi, gr_dbi, tsis, req_db, margen_db, perd_otras_db=1.0):
    pire = db(pt_w) + gt_dbi - 1.0
    fspl = 20 * math.log10(4 * math.pi * d * f / C)
    cn0 = pire - fspl - perd_otras_db + gr_dbi - db(tsis) - db(K)
    return 10 ** ((cn0 - req_db - margen_db) / 10)

DIRECTO = dict(f=8.4e9, pt_w=100.0, gt_dbi=46.0, gr_dbi=68.0, tsis=25.0, req_db=3.5, margen_db=3.0)
REQ_GBIT_DIA = 30.0
HORAS_DIA = 8.0

def volumen_dia(d, horas=HORAS_DIA):
    return tasa_max(d, **DIRECTO) * horas * 3600 / 1e9   # Gbit

def integrar(n):
    """Volumen total en 100 dias con distancia creciente 1.0 a 2.5 UA, regla del trapecio con n pasos."""
    dias = 100.0
    def v(t):
        d = (1.0 + 1.5 * t / dias) * UA
        return volumen_dia(d)
    h = dias / n
    return h * (0.5 * v(0) + sum(v(i * h) for i in range(1, n)) + 0.5 * v(dias))

def calcular():
    R = {"fases": {}}
    for nombre, ua in (("crucero 0.5 UA", 0.5), ("cercana 1.0 UA", 1.0), ("media 1.5 UA", 1.5), ("lejana 2.5 UA", 2.5)):
        rb = tasa_max(ua * UA, **DIRECTO)
        vol = volumen_dia(ua * UA)
        R["fases"][nombre] = (rb, vol, vol / REQ_GBIT_DIA)
    # relevo: rover -> orbitador UHF, 2 pasadas por sol de 8 min a 2 Mbit/s; orbitador -> Tierra como en la fase 'media'
    R["rover_gbit"] = 2 * 8 * 60 * 2e6 / 1e9
    R["relevo_tierra"] = volumen_dia(1.5 * UA)
    R["relevo_util"] = min(R["rover_gbit"], R["relevo_tierra"])
    # integracion numerica convergente
    R["integral"] = {n: integrar(n) for n in (10, 100, 1000)}
    R["conv"] = abs(R["integral"][1000] - R["integral"][100]) / R["integral"][1000]
    R["req"] = REQ_GBIT_DIA
    return R

def main():
    R = calcular()
    print(sys.version.split()[0], "(biblioteca estandar)")
    print("SINTETICO: directo a Tierra, X 8.4 GHz, 100 W, Gt 46 dBi, Gr 68 dBi, T 25 K, Eb/N0 req 3.5 dB, margen 3 dB, 8 h/dia")
    print(f"Requisito sintetico: {R['req']:.1f} Gbit/dia")
    print(f"{'fase':18s}{'tasa [kbit/s]':>15s}{'volumen [Gbit/dia]':>20s}{'razon al requisito':>20s}{'cumple':>8s}")
    for k, (rb, vol, rz) in R["fases"].items():
        print(f"{k:18s}{rb/1e3:15.1f}{vol:20.3f}{rz:20.2f}{'si' if rz >= 1 else 'no':>8s}")
    print(f"Relevo: rover -> orbitador = {R['rover_gbit']:.3f} Gbit/sol ; orbitador -> Tierra (1.5 UA) = {R['relevo_tierra']:.3f} Gbit/dia ; util = {R['relevo_util']:.3f}")
    for n, v in R["integral"].items():
        print(f"Volumen en 100 dias (trapecio, {n:4d} pasos) = {v:.2f} Gbit")
    print(f"Convergencia 100 -> 1000 pasos = {R['conv']:.2e}")
    assert R["conv"] < 1e-3
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
