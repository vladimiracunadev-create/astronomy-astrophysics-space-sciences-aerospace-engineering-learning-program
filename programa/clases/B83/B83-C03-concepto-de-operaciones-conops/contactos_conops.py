#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C03: contactos con una estacion de tierra para un CONOPS.

Constantes: RE y GM de NASA/NSSDC (consultadas 2026-11-10). Velocidad de rotacion terrestre 7.2921159e-5 rad/s: valor estandar
NO consultado. SINTETICOS: orbita circular de 550 km, inclinacion 97.6 deg, nodo ascendente en 0 en t = 0, estacion a 40 deg N,
0 deg E en Tierra esferica, elevacion minima 10 deg, 3 dias, paso de 5 s. Sistema: inercial geocentrico de ejemplo -> fijo a la
Tierra rotando alrededor de z. Modelo: dos cuerpos, sin J2 ni refraccion. Segunda via: duracion analitica de un pase cenital
2*lambda/n (sin rotacion terrestre): la simulacion debe quedar por debajo y a menos del 25 % por debajo.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

OMEGA_E = 7.2921159e-5
INC = math.radians(97.6)
LAT = math.radians(40.0)
ELEV_MIN = 10.0
DIAS = 3
PASO = 5.0


def calcular():
    a = RE_KM + H_KM
    n = math.sqrt(GM_KM3S2 / a ** 3)
    T = 2 * math.pi / n
    t = np.arange(0.0, DIAS * 86400.0, PASO)
    u = n * t
    x, y, z = a * np.cos(u), a * np.sin(u) * math.cos(INC), a * np.sin(u) * math.sin(INC)
    th = OMEGA_E * t
    xe, ye = x * np.cos(th) + y * np.sin(th), -x * np.sin(th) + y * np.cos(th)
    g = RE_KM * np.array([math.cos(LAT), 0.0, math.sin(LAT)])
    ghat = g / np.linalg.norm(g)
    d = np.stack([xe - g[0], ye - g[1], z - g[2]])
    rho = np.linalg.norm(d, axis=0)
    elev = np.degrees(np.arcsin((ghat[:, None] * d).sum(axis=0) / rho))
    vis = elev >= ELEV_MIN
    e = np.diff(vis.astype(int))
    ini = np.where(e == 1)[0] + 1
    fin = np.where(e == -1)[0] + 1
    if vis[0]: ini = np.r_[0, ini]
    if vis[-1]: fin = np.r_[fin, len(vis)]
    dur = (fin - ini) * PASO / 60.0
    huecos = (t[ini[1:]] - t[fin[:-1]]) / 3600.0
    dur_analit = 2 * semiangulo_pase(H_KM, ELEV_MIN) / n / 60.0
    return dict(T_min=T / 60, n_pases=len(dur), pases_dia=len(dur) / DIAS, dur_media=float(dur.mean()), dur_max=float(dur.max()),
                dur_analit=dur_analit, cont_dia=float(dur.sum()) / DIAS, gap_max=float(huecos.max()), dur=dur,
                util=float((dur >= 5.0).sum()), n_corto=int((dur < 5.0).sum()))


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: h = 550 km, i = 97.6 deg, estacion a 40 N, elevacion minima 10 deg, 3 dias, paso 5 s; RE y GM de NASA/NSSDC")
    print(f"Periodo = {V['T_min']:.2f} min")
    print(f"Pases en {DIAS} d = {V['n_pases']} ({V['pases_dia']:.2f} por dia) ; duracion media = {V['dur_media']:.2f} min ; maxima = {V['dur_max']:.2f} min")
    print("Duraciones [min]: " + " ".join(f"{x:.1f}" for x in V["dur"]))
    print(f"Pase cenital analitico (sin rotacion terrestre) = {V['dur_analit']:.2f} min")
    print(f"Tiempo de contacto diario = {V['cont_dia']:.2f} min ; hueco maximo entre pases = {V['gap_max']:.2f} h ; pases de al menos 5 min = {V['util']:.0f}")
    comprobar(V["dur_max"] <= V["dur_analit"] * 1.001, "ningun pase supera al cenital analitico")
    comprobar(V["dur_max"] >= 0.75 * V["dur_analit"], "el mejor pase simulado se acerca al analitico")
    comprobar(V["n_pases"] >= 6, "hay pases en 3 dias")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
