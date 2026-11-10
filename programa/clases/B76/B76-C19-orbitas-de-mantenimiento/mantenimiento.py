#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C19: crecimiento de errores en una NRHO y mantenimiento por apuntamiento a la posicion de la revolucion siguiente.

Datos CONSULTADOS (2026-11-10): constantes de cislunar_lib.py (JPL DE440, NASA/NSSDC); referencia publicada para contexto (Davis, Khoury, Howell y
Sweeney, NASA NTRS 20200000733): periodo medio 6.56 d. NO se consultaron presupuestos reales de mantenimiento: los resultados no son un presupuesto de mision.
ILUSTRATIVOS (sinteticos): error inicial de insercion en el apolune de (1.0, 1.0, 1.0) km en posicion y (1.0, 1.0, 1.0) mm/s en velocidad; 5 revoluciones;
error de ejecucion del impulso: 2 % de la magnitud con direccion aleatoria (semilla 76019).
Modelo: la NRHO del laboratorio B76-C05 (CR3BP, correccion diferencial) se importa y se usa como referencia; el estado de referencia en cada apolune es el
inicial (orbita periodica). En cada apolune se resuelve un impulso 3D dv tal que la posicion tras un periodo sea la de referencia (Jacobiana 3x3 por
diferencias finitas, paso 1e-6 adimensional de velocidad). Sin Sol, sin excentricidad lunar, sin navegacion: solo mecanica del CR3BP.
Tolerancias: sin control, cada cociente de desviaciones sucesivas debe ser menor que el mayor autovalor de la monodromia (la perturbacion solo proyecta en parte sobre el modo inestable); con control la desviacion
tras cada revolucion queda por debajo de 1 km.
"""
from __future__ import annotations
import importlib.util, math, os, platform, random, sys
import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, ".."))
from cislunar_lib import *

spec = importlib.util.spec_from_file_location("nrho", os.path.join(AQUI, "..", "B76-C05-orbitas-nrho", "nrho.py"))
nrho = importlib.util.module_from_spec(spec)
spec.loader.exec_module(nrho)

KM = 1.0 / A_L
V_MMS = 1e-6 / (A_L * N_L * 1e3)  # 1 mm/s en velocidad adimensional (m/s -> km/s -> adim)


def desv(a, b):
    return math.dist(a[:3], b[:3]) * A_L


def jacobiana(s, T):
    base = propagar_ad(s, T, tol=1e-13)
    j = np.zeros((3, 3))
    d = 1e-6
    for k in range(3):
        sp = list(s)
        sp[3 + k] += d
        f = propagar_ad(tuple(sp), T, tol=1e-13)
        j[:, k] = [(f[i] - base[i]) / d for i in range(3)]
    return j, base


def calcular():
    x0, vy0, th = nrho.corregir(1.0213, -0.1818, -0.1)
    ref = (x0, 0.0, -0.1818, 0.0, vy0, 0.0)
    T = 2 * th
    m = nrho.monodromia(ref, T)
    lam = float(max(abs(np.linalg.eigvals(m))))
    err0 = (ref[0] + 1.0 * KM, ref[1] + 1.0 * KM, ref[2] + 1.0 * KM, ref[3] + V_MMS, ref[4] + V_MMS, ref[5] + V_MMS)
    # sin control
    s = err0
    sin_ctrl = [desv(s, ref)]
    for _ in range(4):
        s = propagar_ad(s, T, tol=1e-13)
        sin_ctrl.append(desv(s, ref))
    # con control
    rng = random.Random(76019)
    s = err0
    con_ctrl, dvs = [desv(s, ref)], []
    for k in range(4):
        j, _ = jacobiana(s, T)
        pos_ref = np.array(ref[:3])
        fin = np.array(propagar_ad(s, T, tol=1e-13)[:3])
        dv = np.linalg.solve(j, pos_ref - fin)
        mag = np.linalg.norm(dv)
        ruido = np.array([rng.gauss(0, 1) for _ in range(3)])
        ruido = ruido / np.linalg.norm(ruido) * 0.02 * mag
        dv_real = dv + ruido
        s = (s[0], s[1], s[2], s[3] + dv_real[0], s[4] + dv_real[1], s[5] + dv_real[2])
        s = propagar_ad(s, T, tol=1e-13)
        dvs.append(mag * A_L * N_L * 1e3)       # m/s
        con_ctrl.append(desv(s, ref))
    return dict(lam=lam, T=T * T_U / DIA, sin=sin_ctrl, con=con_ctrl, dvs=dvs, vms=V_MMS)


def main():
    r = calcular()
    print(f"Python {platform.python_version()} ; numpy {np.__version__} ; semilla 76019 ; datos SINTETICOS")
    print(f"NRHO de B76-C05: periodo = {r['T']:.4f} d ; mayor autovalor de la monodromia = {r['lam']:.4f}")
    print("Desviacion de posicion respecto a la referencia en cada apolune [km]:")
    print(" rev   sin control   con control   dv aplicado antes de la rev [m/s]")
    for k in range(5):
        dv = f"{r['dvs'][k]:.5f}" if k < 4 else "-"
        print(f"{k:3d}   {r['sin'][k]:11.3f}   {r['con'][k]:11.4f}   {dv}")
    cocientes = [r['sin'][k + 1] / r['sin'][k] for k in range(4)]
    print("Cociente de desviaciones sucesivas sin control = " + ", ".join(f"{c:.2f}" for c in cocientes))
    print(f"Delta-v total de 4 correcciones = {sum(r['dvs']):.5f} m/s")
    assert r['sin'][4] > 3 * r['sin'][0] and max(cocientes) < r['lam']
    assert all(c < 1.0 for c in r['con'][1:])
    assert r['lam'] > 1.5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
