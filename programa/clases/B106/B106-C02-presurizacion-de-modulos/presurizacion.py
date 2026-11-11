#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C02: presurizacion de un modulo cilindrico: esfuerzo de aro, espesor minimo y despresurizacion por un orificio.

Modelo propio (no consultado en una fuente concreta): cilindro de pared delgada, sigma = P r / t; factor de seguridad 2; aleacion de aluminio con
limite elastico ILUSTRATIVO de 276 MPa y densidad 2800 kg/m3; flujo estrangulado de gas ideal por un orificio con coeficiente de descarga
ILUSTRATIVO 0.6; vaciado isotermo (conservador en el tiempo de aviso: ignora el enfriamiento). Umbrales CONSULTADOS (OCHMO-TB-003): presion total
de 34.5 kPa (5.0 psia) a 103 kPa para exposicion indefinida y ebullismo a 6.27 kPa. No hay datos de ningun modulo real.
Verificacion: la integracion numerica (RK4) coincide con la solucion exponencial; el espesor escala con la presion.
"""
from __future__ import annotations
import math
import platform
import numpy as np

GAMMA, RG, M_AIRE = 1.4, 8.314462, 0.02897
RAD, SIGY, RHO, SF = 2.0, 276e6, 2800.0, 2.0
V, T0, CD = 100.0, 293.15, 0.6


def espesor(P, r=RAD, sig=SIGY, sf=SF):
    return P * r * sf / sig


def tau(d, V=V, T=T0, cd=CD):
    A = math.pi * d * d / 4
    psi = (2 / (GAMMA + 1)) ** ((GAMMA + 1) / (2 * (GAMMA - 1)))
    Rs = RG / M_AIRE
    return V / (cd * A * math.sqrt(GAMMA * Rs * T) * psi)


def rk4(p0, k, t_end, dt):
    p = p0
    for _ in range(int(round(t_end / dt))):
        f = lambda x: -k * x
        k1 = f(p); k2 = f(p + dt / 2 * k1); k3 = f(p + dt / 2 * k2); k4 = f(p + dt * k3)
        p += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return p


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: modelo propio con valores ILUSTRATIVOS (276 MPa, Cd 0.6); umbrales de presion consultados; ningun modulo real")
    R = {}
    print(f"Cilindro de radio {RAD} m, factor de seguridad {SF}, limite elastico {SIGY/1e6:.0f} MPa (ilustrativo)")
    print("  presion [kPa]   sigma con t=1.5 mm [MPa]   t minimo [mm]   masa de pared [kg/m]")
    for P in (34.5e3, 70.3e3, 101.325e3):
        t = espesor(P)
        m = 2 * math.pi * RAD * t * RHO
        print(f"   {P/1e3:9.1f}       {P*RAD/1.5e-3/1e6:12.1f}              {t*1e3:7.3f}        {m:8.2f}")
    R["t101"] = espesor(101.325e3) * 1e3
    R["t345"] = espesor(34.5e3) * 1e3
    R["m101"] = 2 * math.pi * RAD * espesor(101.325e3) * RHO
    assert abs(espesor(101.325e3) / espesor(34.5e3) - 101.325 / 34.5) < 1e-9
    print(f"Esfera de igual radio: espesor {espesor(101.325e3)/2*1e3:.3f} mm (la mitad que el cilindro)")
    print(f"Modulo de {V:.0f} m3 a {T0-273.15:.0f} C, Cd = {CD}: constante de tiempo tau = V/(Cd A c) y tiempos hasta los umbrales")
    print("  diametro [mm]   tau [h]   a 34.5 kPa [h]   a 6.27 kPa [h]")
    P0 = 101.325
    filas = {}
    for d in (1e-3, 3e-3, 10e-3, 30e-3):
        ta = tau(d)
        t345 = ta * math.log(P0 / 34.5)
        t627 = ta * math.log(P0 / 6.27)
        filas[d] = (ta, t345, t627)
        print(f"   {d*1e3:8.0f}      {ta/3600:9.3f}   {t345/3600:12.3f}   {t627/3600:12.3f}")
    R["tau10"], R["t345_10"], R["t345_1"] = filas[10e-3][0] / 3600, filas[10e-3][1] / 3600, filas[1e-3][1] / 3600
    R["tau30"], R["t345_30_min"] = filas[30e-3][0] / 3600, filas[30e-3][1] / 60
    ta = tau(10e-3)
    p_num = rk4(P0, 1 / ta, ta * 1.0, ta / 2000)
    p_an = P0 * math.exp(-1.0)
    R["err_rk4"] = abs(p_num - p_an)
    print(f"Control: RK4 tras 1 tau da {p_num:.6f} kPa frente a {p_an:.6f} kPa (diferencia {abs(p_num-p_an):.2e} kPa)")
    assert abs(p_num - p_an) < 1e-8
    assert filas[30e-3][0] < filas[10e-3][0] < filas[1e-3][0]
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
