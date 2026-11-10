#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C21: identificacion de peligros (HAZID) con palabras guia y riesgo estimado para terceros.

Datos: SINTETICOS. Seis nodos de una campana de lanzamiento de ejemplo, siete palabras guia (No, Mas, Menos, Parte de, Ademas de,
Otro que, Temprano/Tarde), doce peligros identificados con severidad S (1-4) y verosimilitud L (1-5) inventadas; indice de riesgo = S x L
(alto >= 12, medio 6-11, bajo < 6: convencion del ejemplo). Modelo de riesgo para terceros: Ec = Pf x rho x Ac x (1 - refugio) con
probabilidad de falla Pf, densidad de poblacion rho (personas/km2) y area de baja efectiva Ac (km2), inventados para dos trayectorias
(sobre tierra y sobre el mar). Umbral de aceptacion SINTETICO: Ec <= 1e-4 (no es el de ninguna autoridad; no consultado). Incertidumbre:
Pf y rho lognormales con factor de error 3 y 5 (sigma = ln(FE)/1.645). Metodo 1: Monte Carlo de 200000 muestras (semilla 83021).
Segunda via: P(Ec > umbral) analitica con la distribucion lognormal del producto (funcion error). Tolerancia: 0.3 puntos porcentuales.
Sin constantes fisicas.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

NODOS = ["Preparacion en tierra", "Carga de propelente", "Integracion con el lanzador", "Ascenso", "Separacion", "Aborto y terminacion de vuelo"]
GUIAS = ["No", "Mas", "Menos", "Parte de", "Ademas de", "Otro que", "Temprano/Tarde"]
# nodo (indice), palabra guia (indice), peligro, S, L
PELIGROS = [(1, 0, "Sin ventilacion de vapores de propelente", 4, 2), (1, 1, "Sobrepresion del tanque en la carga", 4, 2),
            (1, 4, "Contaminante en la linea de propelente", 3, 2), (0, 5, "Conector equivocado en la integracion electrica", 2, 3),
            (2, 3, "Fijacion parcial del adaptador", 4, 1), (3, 1, "Carga aerodinamica mayor que la prevista", 4, 2),
            (3, 6, "Corte de motor tardio", 3, 2), (3, 0, "Sin guiado durante el ascenso", 4, 1), (4, 6, "Separacion temprana", 3, 2),
            (4, 5, "Separacion con velocidad relativa equivocada", 2, 3), (5, 0, "Sin comando de terminacion de vuelo", 4, 1),
            (0, 2, "Presion de nitrogeno baja en pruebas", 1, 3)]
TRAYECTORIAS = {"sobre tierra": dict(pf=0.03, rho=20.0, ac=0.005, refugio=0.5),
                "sobre el mar": dict(pf=0.03, rho=0.2, ac=0.005, refugio=0.5)}
UMBRAL_EC = 1e-4
FE_PF, FE_RHO = 3.0, 5.0


def nivel(i): return "alto" if i >= 12 else ("medio" if i >= 6 else "bajo")


def ec(d): return d["pf"] * d["rho"] * d["ac"] * (1 - d["refugio"])


def p_excede(d, mc=True, n=200000):
    sp, sr = math.log(FE_PF) / 1.645, math.log(FE_RHO) / 1.645
    mu = math.log(ec(d)); s = math.sqrt(sp ** 2 + sr ** 2)
    anal = 0.5 * (1 - math.erf((math.log(UMBRAL_EC) - mu) / (s * math.sqrt(2))))
    rng = np.random.default_rng(83021)
    pf = rng.lognormal(math.log(d["pf"]), sp, n); rho = rng.lognormal(math.log(d["rho"]), sr, n)
    e = pf * rho * d["ac"] * (1 - d["refugio"])
    return float((e > UMBRAL_EC).mean()), anal


def calcular():
    ind = [s * l for *_, s, l in PELIGROS]
    niv = [nivel(i) for i in ind]
    V = dict(n_nodos=len(NODOS), n_guias=len(GUIAS), n_celdas=len(NODOS) * len(GUIAS), n_pel=len(PELIGROS),
             cobertura=100 * len({(n, g) for n, g, *_ in PELIGROS}) / (len(NODOS) * len(GUIAS)), n_alto=niv.count("alto"),
             n_medio=niv.count("medio"), n_bajo=niv.count("bajo"), mayor=PELIGROS[int(np.argmax(ind))][2], ind_max=max(ind),
             nodos_cubiertos=len({n for n, *_ in PELIGROS}))
    for k, d in TRAYECTORIAS.items():
        key = "t" if k == "sobre tierra" else "m"
        V[f"ec_{key}"] = ec(d); pm, pa = p_excede(d)
        V[f"pmc_{key}"] = 100 * pm; V[f"pan_{key}"] = 100 * pa; V[f"ok_{key}"] = ec(d) <= UMBRAL_EC
    V["dif"] = max(abs(V["pmc_t"] - V["pan_t"]), abs(V["pmc_m"] - V["pan_m"]))
    V["indices"] = ind; V["niveles"] = niv
    return V


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: 6 nodos x 7 palabras guia; 12 peligros; Ec = Pf x rho x Ac x (1 - refugio); umbral del ejemplo 1e-4 (no consultado)")
    for (n, g, t, s, l), i, nv in zip(PELIGROS, V["indices"], V["niveles"]):
        print(f"  [{NODOS[n][:16]:16s} | {GUIAS[g]:14s}] S{s} L{l} indice {i:2d} {nv:5s} {t}")
    print(f"Celdas del HAZID: {V['n_celdas']} ; peligros: {V['n_pel']} ; cobertura {V['cobertura']:.1f} % ; nodos con peligros: {V['nodos_cubiertos']} de {V['n_nodos']}")
    print(f"Niveles: alto {V['n_alto']}, medio {V['n_medio']}, bajo {V['n_bajo']} ; mayor indice {V['ind_max']}: {V['mayor']}")
    for k in ("sobre tierra", "sobre el mar"):
        key = "t" if k == "sobre tierra" else "m"
        print(f"Trayectoria {k:13s}: Ec = {V[f'ec_{key}']:.3e} ; umbral 1e-4 -> {'CUMPLE' if V[f'ok_{key}'] else 'NO CUMPLE'} ; P(Ec > umbral) MC {V[f'pmc_{key}']:.2f} % ; analitica {V[f'pan_{key}']:.2f} %")
    comprobar(V["dif"] < 0.3, "Monte Carlo y probabilidad analitica")
    comprobar(not V["ok_t"] and V["ok_m"], "tierra no cumple y mar cumple")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
