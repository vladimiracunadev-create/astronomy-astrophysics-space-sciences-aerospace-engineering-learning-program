#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C10: asignacion de lineas observadas a un catalogo y probabilidad de coincidencias por azar.

Datos: (i) las 15 lineas mas intensas de H2CO entre 140 y 310 GHz del catalogo JPL (etiqueta 30004, version 2, nov. 1997;
https://spec.jpl.nasa.gov/ftp/pub/catalog/c030004.cat; consultado el 2026-11-09) con frecuencia en MHz; (ii) un espectro "observado" **SINTETICO** construido en el script:
lineas de H2CO desplazadas por v_LSR = 5.0 km/s y ruido de frecuencia gaussiano de 0.15 MHz, mas 3 lineas "de otra especie" inventadas. Ninguna es una observacion.
Modelo: una linea observada nu_o se asigna a la linea de catalogo i si |nu_o - nu_i (1 - v/c)| < tolerancia, con v recuperado por minimos cuadrados con las lineas asignadas.
Coincidencias por azar: el numero esperado es N_obs * (2 w rho) con rho = densidad de lineas de catalogo (lineas/MHz) en la banda; se comprueba con un Monte Carlo (semilla fija).
Supuestos: catalogo de una sola especie y 15 lineas; las lineas observadas no se mezclan. Validez: ilustrativa.
Tolerancia: v recuperado a 0.1 km/s del valor inyectado; probabilidad Monte Carlo vs 1 - exp(-2 w rho) a 15 % relativo.
"""
from __future__ import annotations
import math, platform, random

C_KMS = 299792.458
# (frecuencia MHz) -- JPL 30004 v2, H2CO
H2CO = [140839.502, 145602.949, 150498.334, 211211.468, 218222.192, 218475.632, 218760.066, 225697.775,
        281526.929, 290623.405, 291237.780, 291380.488, 291384.264, 291948.060, 300836.635]
F_LO, F_HI = 140000.0, 310000.0
V_INY = 5.0          # km/s (SINTETICO)
SIG_F = 0.15         # MHz (ruido de frecuencia SINTETICO)
INTRUSAS = [160123.4, 190456.7, 250789.1]   # lineas inventadas de "otra especie"

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(777)
    obs = [f * (1.0 - V_INY / C_KMS) + rng.gauss(0.0, SIG_F) for f in H2CO if f not in (291384.264,)] + INTRUSAS
    obs.sort()
    print(f"A. Espectro SINTETICO: {len(obs)} lineas ({len(H2CO) - 1} de H2CO desplazadas {V_INY} km/s + {len(INTRUSAS)} intrusas)")
    # asignacion en dos pasos: (1) ventana de +-8 km/s en torno a v = 0 y v robusto por mediana ; (2) ventana de +-0.6 MHz con ese v
    def vel(o, c):
        return C_KMS * (1.0 - o / c)
    previas = []
    for o in obs:
        mejor = min(H2CO, key=lambda c: abs(vel(o, c)))
        if abs(vel(o, mejor)) < 8.0:
            previas.append(vel(o, mejor))
    previas.sort()
    v = previas[len(previas) // 2]
    asign = []
    for o in obs:
        mejor = min(H2CO, key=lambda c: abs(o - c * (1.0 - v / C_KMS)))
        if abs(o - mejor * (1.0 - v / C_KMS)) < 0.6:
            asign.append((o, mejor))
    num = sum(c * c * (1.0 - o / c) for o, c in asign)
    den = sum(c * c for o, c in asign)
    v = C_KMS * num / den
    print(f"B. Asignadas {len(asign)} de {len(obs)} lineas ; v recuperada = {v:.3f} km/s (inyectada {V_INY}) ; no asignadas = {len(obs) - len(asign)}")
    print("nu_obs [MHz]   nu_cat [MHz]   residuo [MHz]")
    for o, c in asign:
        print(f"{o:12.3f}   {c:12.3f}   {o - c * (1 - v / C_KMS):7.3f}")
    assert abs(v - V_INY) < 0.1, v
    assert len(asign) == len(H2CO) - 1
    print("   no asignadas:", ", ".join(f"{o:.1f}" for o in obs if all(o != a[0] for a in asign)))
    # coincidencias por azar
    rho = len(H2CO) / (F_HI - F_LO)    # lineas por MHz
    print("C. Coincidencias por azar: P(al menos una linea de catalogo dentro de +-w de una frecuencia aleatoria)")
    print("w [MHz]   P analitica 1-exp(-2 w rho)   P Monte Carlo (200000 puntos)")
    rng2 = random.Random(31415)
    cat = sorted(H2CO)
    for w in (0.25, 0.6, 2.0, 10.0):
        hits = 0
        n = 200000
        import bisect
        for _ in range(n):
            x = rng2.uniform(F_LO, F_HI)
            i = bisect.bisect_left(cat, x)
            d = min(abs(x - cat[j]) for j in (max(i - 1, 0), min(i, len(cat) - 1)))
            if d < w:
                hits += 1
        p_mc = hits / n
        p_an = 1.0 - math.exp(-2.0 * w * rho)
        print(f"{w:6.2f}   {p_an:12.5f}                {p_mc:12.5f}")
        assert abs(p_mc - p_an) / p_an < 0.15, (w, p_mc, p_an)
    n_falsas = len(INTRUSAS) * (1.0 - math.exp(-2.0 * 0.6 * rho))
    print(f"D. Falsos positivos esperados entre las {len(INTRUSAS)} intrusas con w = 0.6 MHz: {n_falsas:.4f} (densidad {rho * 1000:.4f} lineas por GHz)")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
