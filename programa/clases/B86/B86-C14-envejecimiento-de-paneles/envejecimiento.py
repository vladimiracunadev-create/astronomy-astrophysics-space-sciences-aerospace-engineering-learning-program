#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C14: envejecimiento de un ala solar SINTETICA (radiacion, ciclado termico, contaminacion y fallas de cadenas).

Datos consultados (2026-11-10): el capitulo de potencia del estado del arte de la NASA lista el rendimiento a lo largo de la vida (envejecimiento, radiacion y contaminacion)
como factor de diseno pero NO da cifras de degradacion; por eso TODAS las tasas de esta clase son ilustrativas. Periodo de la orbita: GM = 0.39860e6 km3/s2 y radio 6371 km (NASA/NSSDC).
ILUSTRATIVOS (sinteticos, no medidos): radiacion 1.5 %/ano (exponencial), ciclado termico 0.4 % por cada 10000 ciclos (lineal), contaminacion y UV 0.5 %/ano (lineal),
20 cadenas en paralelo con tasa de falla de 0.002 /ano cada una, vida de 5 y 10 anos, potencia requerida al fin de vida 176.38 W (B86-C01), potencia BOL de partida 243.67 W / 0.85.
Modelo: f(t) = exp(-a_rad t) (1 - a_ter n_ciclos/1e4) (1 - a_con t) N_cad(t)/N con N_cad = N exp(-lambda_c t) esperado.
Segunda via: Monte Carlo de las fallas de cadenas (semilla 20261110, 200000 ensayos) frente a la esperanza cerrada.
Tolerancia: fraccion de cadenas vivas Monte Carlo frente a la esperada < 4 desviaciones tipicas binomiales.
"""
from __future__ import annotations
import math, platform, random

MU, RE, H = 398600.0, 6371.0, 600.0
T_ORB = 2.0 * math.pi * math.sqrt((RE + H) ** 3 / MU)
CICLOS_ANO = 365.25 * 86400.0 / T_ORB
A_RAD, A_TER, A_CON, NCAD, LCAD = 0.015, 0.004, 0.005, 20, 0.002
P_REQ, P_BOL = 176.38, 243.67 / 0.85


def factores(t):
    rad = math.exp(-A_RAD * t)
    ter = 1.0 - A_TER * (CICLOS_ANO * t) / 1e4
    con = 1.0 - A_CON * t
    cad = math.exp(-LCAD * t)
    return rad, ter, con, cad, rad * ter * con * cad


def montecarlo(t, n=200000, semilla=20261110):
    rng = random.Random(semilla)
    vivas = 0
    for _ in range(n):
        for _ in range(NCAD):
            if rng.expovariate(LCAD) > t:
                vivas += 1
    return vivas / (n * NCAD)


def resultados():
    r = dict(ciclos_ano=CICLOS_ANO)
    for t in (1, 5, 10):
        rad, ter, con, cad, tot = factores(float(t))
        r[f"rad{t}"], r[f"ter{t}"], r[f"con{t}"], r[f"cad{t}"], r[f"f{t}"] = rad, ter, con, cad, tot
        r[f"P{t}"] = P_BOL * tot
        r[f"f{t}_pct"] = tot * 100.0
    r["margen5"] = (r["P5"] - P_REQ) / P_REQ * 100.0
    r["margen10"] = (r["P10"] - P_REQ) / P_REQ * 100.0
    # potencia BOL necesaria para cerrar P_REQ al fin de vida
    r["Pbol_req5"] = P_REQ / r["f5"]
    r["Pbol_req10"] = P_REQ / r["f10"]
    r["sobre5_pct"] = (r["Pbol_req5"] / P_REQ - 1.0) * 100.0
    r["sobre10_pct"] = (r["Pbol_req10"] / P_REQ - 1.0) * 100.0
    # vida a la que P cruza P_REQ (biseccion)
    lo, hi = 0.0, 40.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if P_BOL * factores(m)[4] > P_REQ:
            lo = m
        else:
            hi = m
    r["vida_util"] = 0.5 * (lo + hi)
    # Monte Carlo de cadenas
    esp = math.exp(-LCAD * 10.0)
    mc = montecarlo(10.0)
    sig = math.sqrt(esp * (1.0 - esp) / (200000 * NCAD))
    r["cad_esp10"], r["cad_mc10"], r["z_mc"] = esp, mc, (mc - esp) / sig
    # sensibilidad: tasa de radiacion doble
    rad2 = math.exp(-2 * A_RAD * 10.0)
    r["f10_rad2"] = rad2 * r["ter10"] * r["con10"] * r["cad10"]
    r["f10_rad2_pct"] = r["f10_rad2"] * 100.0
    r["f5sq"] = r["f5"] ** 2
    r["Pbol"] = P_BOL
    r["ciclos10"] = CICLOS_ANO * 10.0
    r["perd_ter10"] = A_TER * r["ciclos10"] / 1e4 * 100.0
    r["cad_viva"] = NCAD * r["cad_esp10"]
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Ala SINTETICA: P_BOL = {P_BOL:.2f} W ; requisito al fin de vida = {P_REQ} W ; ciclos termicos por ano = {r['ciclos_ano']:.0f}")
    print(" t [a]   radiacion  ciclado   contam.   cadenas   total [%]   P [W]")
    for t in (1, 5, 10):
        print(f" {t:5d}  {r[f'rad{t}']:9.4f}  {r[f'ter{t}']:8.4f}  {r[f'con{t}']:8.4f}  {r[f'cad{t}']:8.4f}  {r[f'f{t}_pct']:9.2f}  {r[f'P{t}']:7.2f}")
    print(f"Margen sobre el requisito: 5 anos = {r['margen5']:.1f} % ; 10 anos = {r['margen10']:.1f} %")
    print(f"P_BOL necesaria para cerrar el requisito: 5 anos = {r['Pbol_req5']:.2f} W (+{r['sobre5_pct']:.1f} %) ; 10 anos = {r['Pbol_req10']:.2f} W (+{r['sobre10_pct']:.1f} %)")
    print(f"La potencia cruza el requisito a los {r['vida_util']:.2f} anos")
    print(f"Cadenas vivas a 10 anos: esperado = {r['cad_esp10']:.5f} ; Monte Carlo = {r['cad_mc10']:.5f} ; z = {r['z_mc']:+.2f}")
    print(f"Con la tasa de radiacion duplicada, el factor a 10 anos baja de {r['f10_pct']:.2f} % a {r['f10_rad2']*100:.2f} %")
    assert abs(r["z_mc"]) < 4.0
    assert r["f1"] > r["f5"] > r["f10"]
    assert abs(P_BOL * factores(r["vida_util"])[4] - P_REQ) < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
