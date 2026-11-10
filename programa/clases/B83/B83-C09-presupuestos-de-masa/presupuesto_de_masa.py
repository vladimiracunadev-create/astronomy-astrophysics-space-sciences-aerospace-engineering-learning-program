#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C09: presupuesto de masa con reserva por madurez, margen e incertidumbre.

Datos: SINTETICOS (diez subsistemas de ESTRELLA-S con masa estimada actual CBE, categoria de madurez y reservas de crecimiento
inventadas: comercial 5 %, modificado 10 %, nuevo 20 %, en desarrollo 30 %). Limite de masa de lanzamiento 80 kg: asignacion
sintetica. g0 = 9.80665 m/s2 (NASA/NSSDC, 2026-11-10). Delta-v = 150 m/s e Isp = 220 s: SINTETICOS. Modelo: MEV = CBE (1 + g);
propelente por la ecuacion del cohete; incertidumbre con distribucion triangular (CBE*0.98, CBE*(1+g/2), CBE*(1+2g)), 20000
muestras, semilla 83009. Segunda via del propelente: biseccion numerica de la ecuacion del cohete. Tolerancia: 1e-9 kg.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

RESERVA = {"comercial": 0.05, "modificado": 0.10, "nuevo": 0.20, "en desarrollo": 0.30}
SUBS = [("Estructura", 14.0, "modificado"), ("Carga util", 18.0, "nuevo"), ("Control de actitud", 3.5, "comercial"),
        ("Paneles solares", 6.0, "comercial"), ("Bateria", 4.5, "comercial"), ("Computadora de a bordo", 1.8, "modificado"),
        ("Comunicaciones", 2.4, "modificado"), ("Termico", 2.2, "nuevo"), ("Propulsion (seco)", 3.0, "comercial"),
        ("Arnes electrico", 4.0, "en desarrollo")]
LIMITE_KG = 80.0
DV, ISP = 150.0, 220.0


def prop_cerrado(m_seco):
    return m_seco * (math.exp(DV / (G0 * ISP)) - 1.0)


def prop_biseccion(m_seco):
    lo, hi = 0.0, m_seco
    for _ in range(200):
        mp = 0.5 * (lo + hi)
        if G0 * ISP * math.log((m_seco + mp) / m_seco) < DV: lo = mp
        else: hi = mp
    return 0.5 * (lo + hi)


def calcular():
    cbe = np.array([s[1] for s in SUBS]); g = np.array([RESERVA[s[2]] for s in SUBS])
    mev = cbe * (1 + g)
    seco_cbe, seco_mev = cbe.sum(), mev.sum()
    p_cbe, p_mev = prop_cerrado(seco_cbe), prop_cerrado(seco_mev)
    tot_cbe, tot_mev = seco_cbe + p_cbe, seco_mev + p_mev
    rng = np.random.default_rng(83009)
    N = 20000
    M = rng.triangular(cbe * 0.98, cbe * (1 + g / 2), cbe * (1 + 2 * g), size=(N, len(cbe)))
    seco = M.sum(axis=1); tot = seco + seco * (math.exp(DV / (G0 * ISP)) - 1.0)
    return dict(n=len(SUBS), seco_cbe=seco_cbe, seco_mev=seco_mev, reserva=seco_mev - seco_cbe, reserva_pct=100 * (seco_mev - seco_cbe) / seco_cbe,
                p_cbe=p_cbe, p_mev=p_mev, p_bis=prop_biseccion(seco_mev), tot_cbe=tot_cbe, tot_mev=tot_mev,
                margen_kg=LIMITE_KG - tot_mev, margen_pct=100 * (LIMITE_KG - tot_mev) / LIMITE_KG,
                mc_media=float(tot.mean()), mc_p95=float(np.percentile(tot, 95)), mc_p_ok=100.0 * float((tot <= LIMITE_KG).mean()),
                mev=mev, cbe=cbe, mayor=SUBS[int(np.argmax(mev - cbe))][0], exp=DV / (G0 * ISP))


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 10 subsistemas; limite 80 kg; dv = 150 m/s; Isp = 220 s; g0 = 9.80665 m/s2 (NASA/NSSDC)")
    print(f"{'subsistema':24s} {'CBE kg':>8s} {'madurez':>14s} {'reserva':>8s} {'MEV kg':>8s}")
    for (n, m, c), mev in zip(SUBS, V["mev"]):
        print(f"{n:24s} {m:8.2f} {c:>14s} {RESERVA[c]*100:7.0f}% {mev:8.3f}")
    print(f"Masa seca CBE = {V['seco_cbe']:.3f} kg ; MEV = {V['seco_mev']:.3f} kg ; reserva = {V['reserva']:.3f} kg ({V['reserva_pct']:.2f} %)")
    print(f"Propelente (ecuacion del cohete): sobre CBE {V['p_cbe']:.3f} kg ; sobre MEV {V['p_mev']:.6f} kg ; biseccion {V['p_bis']:.6f} kg")
    print(f"Masa de lanzamiento: CBE {V['tot_cbe']:.3f} kg ; MEV {V['tot_mev']:.3f} kg ; limite {LIMITE_KG:.1f} kg ; margen {V['margen_kg']:.3f} kg ({V['margen_pct']:.2f} %)")
    print(f"Monte Carlo (20000, semilla 83009): media {V['mc_media']:.3f} kg ; P95 {V['mc_p95']:.3f} kg ; P(masa <= limite) = {V['mc_p_ok']:.1f} %")
    comprobar(abs(V["p_mev"] - V["p_bis"]) < 1e-9, "propelente por formula y por biseccion")
    comprobar(V["tot_mev"] < LIMITE_KG, "la masa MEV cabe en el limite")
    comprobar(V["mc_media"] < V["tot_mev"], "la media simulada queda bajo el MEV (el MEV es conservador)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
