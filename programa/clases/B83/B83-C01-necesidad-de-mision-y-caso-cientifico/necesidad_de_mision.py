#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B83-C01: de un objetivo cientifico a un requisito de medicion y priorizacion de objetivos.

Datos: SINTETICOS (objetivos, pesos, puntajes y tamano de rasgo de ejemplo). Constante consultada: RE (NASA/NSSDC, 2026-11-10).
Sistema: geometria al nadir sobre una Tierra esferica de radio RE; altura 550 km. Modelo: limite de difraccion de Rayleigh
(theta = 1.22 lambda / D) y criterio de muestreo GSD <= rasgo/2 (supuesto del ejemplo). Tolerancias: segunda via exacta a 1e-9.
"""
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from sistemas_comun import *

OBJ = ["O1 Cobertura de cultivos", "O2 Cambio de costa", "O3 Hielo estacional", "O4 Calidad del aire"]
CRIT = ["Valor cientifico", "Madurez de la medicion", "Costo (inverso)"]
PESOS = np.array([0.5, 0.3, 0.2])
PUNT = np.array([[8, 6, 6], [7, 8, 7], [9, 4, 5], [5, 6, 8]], dtype=float)   # SINTETICO, escala 0-10


def calcular():
    lam, rasgo, ancho = 550e-9, 10.0, 30e3
    gsd = rasgo / 2.0
    D = 1.22 * lam * (H_KM * 1e3) / gsd
    theta = 1.22 * lam / D
    gsd_via2 = theta * H_KM * 1e3
    pix = ancho / gsd
    esc = PUNT @ PESOS
    esc2 = np.array([sum(PUNT[i, j] * PESOS[j] for j in range(3)) for i in range(4)])
    rng = np.random.default_rng(83001)
    W = rng.dirichlet(PESOS * 20.0, size=10000)
    gana = np.argmax(PUNT @ W.T, axis=0)
    frec = np.bincount(gana, minlength=4) / 10000.0
    k = int(np.argmax(esc))
    return dict(lam_nm=lam * 1e9, rasgo=rasgo, gsd=gsd, D_cm=D * 100, theta_urad=theta * 1e6, gsd_via2=gsd_via2, pix=pix,
                s1=esc[0], s2=esc[1], s3=esc[2], s4=esc[3], ganador=OBJ[k], f1=frec[0] * 100, f2=frec[1] * 100,
                f3=frec[2] * 100, f4=frec[3] * 100, fg=frec[k] * 100, esc=esc, esc2=esc2, k=k)


def main():
    V = calcular()
    print(cabecera())
    print("Datos SINTETICOS: rasgo 10 m, ancho de franja 30 km, h = 550 km, lambda = 550 nm; constantes NASA/NSSDC (2026-11-10)")
    print(f"GSD requerido = rasgo/2 = {V['gsd']:.2f} m ; apertura minima D = {V['D_cm']:.2f} cm ; theta = {V['theta_urad']:.3f} urad")
    print(f"segunda via: GSD = theta*h = {V['gsd_via2']:.6f} m ; pixeles por franja = {V['pix']:.0f}")
    print("Puntaje ponderado (pesos 0.5/0.3/0.2):")
    for o, s in zip(OBJ, V["esc"]):
        print(f"  {o:28s} {s:.2f}")
    print(f"Ganador: {V['ganador']}")
    print("Sensibilidad (10000 pesos Dirichlet, semilla 83001), frecuencia de ser el primero [%]:")
    for o, f in zip(OBJ, [V["f1"], V["f2"], V["f3"], V["f4"]]):
        print(f"  {o:28s} {f:.1f}")
    comprobar(abs(V["gsd_via2"] - V["gsd"]) < 1e-9, "GSD por segunda via")
    comprobar(np.allclose(V["esc"], V["esc2"], atol=1e-12), "puntaje con dot y con bucles")
    comprobar(abs(V["f1"] + V["f2"] + V["f3"] + V["f4"] - 100) < 1e-9, "las frecuencias suman 100 %")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
