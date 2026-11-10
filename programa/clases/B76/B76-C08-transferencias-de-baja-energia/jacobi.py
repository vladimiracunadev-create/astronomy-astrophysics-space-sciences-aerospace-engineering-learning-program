#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B76-C08: constante de Jacobi y energia necesaria para abrir los cuellos de L1 y L2.

Datos CONSULTADOS (2026-11-10): constantes de cislunar_lib.py (JPL DE440, NASA/NSSDC). ILUSTRATIVO: orbita de estacionamiento
circular de 200 km de altitud, impulso tangencial prograda en el perigeo, angulo de salida theta (se barre de 0 a 360 grados).
Modelo: CR3BP plano. C = 2*Omega - v^2 (sinodica). Un cuello se abre cuando C <= C(Li). Dv minimo = v_tras - v_circ con v_tras tal
que C = C(Li) en la direccion de salida elegida (velocidad sinodica = inercial - omega x r). La region prohibida se levanta, pero esto
NO es una transferencia de baja energia completa: la baja energia real aprovecha ademas al Sol (no modelado aqui).
Verificaciones: C conservada en una integracion de 5 d (< 1e-8); dv_TLI de Hohmann (C07) como referencia.
"""
from __future__ import annotations
import math, os, platform, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from cislunar_lib import *

H_LEO = 200.0


def c_punto(l):
    return omega2(l)


def estado_sinodico(theta, v_in):
    """Posicion a r (adim) de la Tierra con angulo theta desde el eje +x; velocidad inercial tangencial v_in (adim, prograda)."""
    r = (R_T_EQ + H_LEO) / A_L
    x, y = -MU + r * math.cos(theta), r * math.sin(theta)
    vxi, vyi = -v_in * math.sin(theta), v_in * math.cos(theta)
    # velocidad inercial de la Tierra (alrededor del baricentro): omega x (-mu,0) = (0,-mu)
    vxi, vyi = vxi, vyi + (-MU)
    # velocidad sinodica = inercial - omega x posicion; omega x (x,y) = (-y, x)
    return (x, y, 0.0, vxi + y, vyi - x, 0.0)


def dv_para(c_obj, theta):
    r = (R_T_EQ + H_LEO) / A_L
    v_circ = math.sqrt((1 - MU) / r)  # adim (GM_T = 1-mu)
    lo, hi = v_circ * 0.9, v_circ * 1.6
    f = lambda v: jacobi(estado_sinodico(theta, v)) - c_obj
    # C decrece al aumentar v en el rango util
    if f(lo) < 0:
        return None
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if f(m) > 0:
            lo = m
        else:
            hi = m
    v = 0.5 * (lo + hi)
    return (v - v_circ) * A_L * N_L, v_circ * A_L * N_L, v


def calcular():
    l1, l2, l3 = colineales()
    c1, c2, c3 = c_punto(l1), c_punto(l2), c_punto(l3)
    res = {}
    for nom, c in (("L1", c1), ("L2", c2)):
        mejor = None
        for k in range(360):
            th = math.radians(k)
            d = dv_para(c, th)
            if d and (mejor is None or d[0] < mejor[0]):
                mejor = (d[0], k, d[2])
        res[nom] = mejor
    # integracion de verificacion con dv ligeramente mayor que el de L2
    dv, k, v = res["L2"]
    s0 = estado_sinodico(math.radians(k), v * 1.0005)
    c_ini = jacobi(s0)
    s = propagar_ad(s0, 5 * DIA / T_U, tol=1e-12)
    # referencia Hohmann (C07)
    r1 = R_T_EQ + H_LEO
    at = 0.5 * (r1 + A_L)
    dv_h = math.sqrt(GM_T * (2 / r1 - 1 / at)) - math.sqrt(GM_T / r1)
    return dict(c1=c1, c2=c2, c3=c3, res=res, dC=abs(jacobi(s) - c_ini), dv_h=dv_h, v_circ=dv_para(c1, 0.0)[1] if dv_para(c1, 0.0) else None)


def main():
    r = calcular()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"C(L1) = {r['c1']:.6f} ; C(L2) = {r['c2']:.6f} ; C(L3) = {r['c3']:.6f}  (neck abierto si C <= C(Li))")
    for nom in ("L1", "L2"):
        dv, k, v = r['res'][nom]
        print(f"Salida optima para abrir {nom}: theta = {k} grados ; dv desde LEO 200 km = {dv:.4f} km/s")
    print(f"Referencia Hohmann hasta la distancia lunar (C07) = {r['dv_h']:.4f} km/s")
    print(f"Deriva de C en 5 d de integracion = {r['dC']:.2e}")
    assert r['c1'] > r['c2'] > r['c3'] > 2.9
    assert r['dC'] < 1e-8
    assert abs(r['res']['L1'][0] - r['dv_h']) < 0.1
    assert r['res']['L2'][0] >= r['res']['L1'][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
