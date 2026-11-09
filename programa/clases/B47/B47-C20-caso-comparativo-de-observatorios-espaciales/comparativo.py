#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B47-C20: caso comparativo de observatorios espaciales, cobertura espectral, limite de difraccion y matriz de decision con sensibilidad.

Datos: h, c y e (eV) de NIST CODATA 2022 (allascii.txt, consultada el 2026-11-09); GM_Tierra y R_ecuatorial de la UAI B3 de 2015 (consultada el 2026-11-09). CONSULTADOS SOLO EN RESUMEN
(2026-11-09): JWST (Gardner et al., arXiv:astro-ph/0606175): 6,6 m, 50 K, 0,6 a 29 micrometros; GALEX (Martin et al., arXiv:astro-ph/0411302): 1350-1750 y 1750-2750 angstrom;
NuSTAR (Harrison et al., arXiv:1301.7307): 3 a 79 keV, orbita de unos 600 km; Fermi LAT (Atwood et al., arXiv:0902.1089): de menos de 20 MeV a mas de 300 GeV, campo de 2,4 sr.
ILUSTRATIVOS (no son evaluaciones de esos observatorios): los tres CONCEPTOS A, B y C de la matriz de decision, sus puntuaciones de 1 a 5 y los pesos.
Modelo: (1) energia y longitud de onda de los bordes de banda y decadas cubiertas; (2) FWHM de difraccion 1,028 lambda/D con D = 6,6 m a 2 micrometros; (3) fraccion de oclusion
asin(R/a)/pi de una orbita a 600 km; (4) suma ponderada de puntuaciones y analisis de sensibilidad con 20000 vectores de pesos aleatorios (semilla 20261109, uniformes normalizados).
Supuestos: los intervalos de banda son los de los resumenes, no los de cada instrumento; los conceptos son hipoteticos. Validez: ilustrativa; no es un ranking de misiones reales.
Tolerancia: ida y vuelta lambda -> E -> lambda, 1e-12; pesos normalizados suman 1.
"""
from __future__ import annotations
import math, platform, random

H = 6.62607015e-34
C = 299792458.0
EV = 1.602176634e-19
GM = 3.986004e14
RE = 6.3781e6
ARCSEC = math.pi / 180 / 3600


def e_ev(lam_m):
    return H * C / lam_m / EV


def lam_de_e(e):
    return H * C / (e * EV)


BANDAS = {
    "JWST (0,6-29 um)": (0.6e-6, 29e-6),
    "GALEX (135-275 nm)": (135e-9, 275e-9),
    "NuSTAR (3-79 keV)": (lam_de_e(79e3), lam_de_e(3e3)),
    "Fermi LAT (20 MeV-300 GeV)": (lam_de_e(300e9), lam_de_e(20e6)),
}
CRIT = ["resolucion", "cobertura", "coste", "riesgo", "cadencia"]
PESOS = [0.30, 0.25, 0.20, 0.15, 0.10]
CONC = {"A gran telescopio frio": [5, 4, 1, 2, 2], "B constelacion pequena": [2, 3, 5, 4, 5], "C telescopio de rayos X": [4, 2, 3, 3, 3]}


def calc():
    r = {"bandas": {}}
    for k, (lo, hi) in BANDAS.items():
        e1, e2 = e_ev(hi), e_ev(lo)
        ida_vuelta = abs(lam_de_e(e2) - lo) / lo
        r["bandas"][k] = (lo, hi, e1, e2, math.log10(hi / lo), ida_vuelta)
    r["dif"] = 1.028 * 2e-6 / 6.6 / ARCSEC
    a = RE + 600e3
    r["ocu"] = math.asin(RE / a) / math.pi
    r["per"] = 2 * math.pi * math.sqrt(a ** 3 / GM) / 60
    r["base"] = {k: sum(w * s for w, s in zip(PESOS, v)) for k, v in CONC.items()}
    rng = random.Random(20261109)
    gana = {k: 0 for k in CONC}
    n = 20000
    for _ in range(n):
        w = [rng.random() for _ in CRIT]
        sw = sum(w)
        w = [x / sw for x in w]
        pts = {k: sum(wi * si for wi, si in zip(w, v)) for k, v in CONC.items()}
        gana[max(pts, key=pts.get)] += 1
    r["gana"] = {k: v / n for k, v in gana.items()}
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, (lo, hi, e1, e2, dec, err) in r["bandas"].items():
        print(f"{k:28s} lambda {lo:.4e} a {hi:.4e} m ; E {e1:.4e} a {e2:.4e} eV ; {dec:.2f} decadas")
        assert err < 1e-12
    print(f"FWHM de difraccion de un espejo de 6,6 m a 2 um = {r['dif']:.4f} arcsec")
    print(f"orbita de 600 km: periodo = {r['per']:.3f} min ; oclusion maxima = {r['ocu']:.4f} ; eficiencia maxima = {1-r['ocu']:.4f}")
    print("pesos:", dict(zip(CRIT, PESOS)), "suma =", round(sum(PESOS), 12))
    for k, v in r["base"].items():
        print(f"concepto {k:26s} puntuacion = {v:.3f} ; gana en {r['gana'][k]*100:.1f} % de los pesos aleatorios")
    assert abs(sum(PESOS) - 1) < 1e-12
    assert abs(sum(r["gana"].values()) - 1) < 1e-12
    assert max(r["base"], key=r["base"].get) in r["gana"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
