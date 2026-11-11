#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C23: particulas en suspension: sedimentacion de Stokes segun la gravedad y limpieza por filtro de alta eficiencia.

Consultado (OCHMO-TB-002): el resumen lista requisitos de material particulado (V2 6052), de polvo lunar (V2 6053) y de monitoreo de polvo celeste (V2 6153), sin valores.
Relaciones de manual NO consultadas: velocidad de Stokes v = rho_p g d^2/(18 mu), valida con Re = rho_aire v d/mu < 1, e eficiencia de 99.97 % a 0.3 micras como definicion usual de un filtro HEPA.
ILUSTRATIVOS: densidad de particula de 1500 kg/m3, viscosidad del aire de 1.81e-5 Pa s, altura de caida de 2 m, cabina de 100 m3 con 0.6 m3/s por el filtro, gravedades de 9.81, 3.71 y 1.62 m/s2
(sin correccion de Cunningham, que importa bajo ~1 micra).
Verificacion: Re < 1 en los casos mostrados; la sedimentacion escala con g y d^2; la limpieza sigue exp(-k t) con k = Q eta/V + v/h.
"""
from __future__ import annotations
import math
import platform
import numpy as np

RHO_P, MU, RHO_A, H, V, Q = 1500.0, 1.81e-5, 1.2, 2.0, 100.0, 0.6


def v_stokes(d, g):
    return RHO_P * g * d * d / (18 * MU)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: relaciones de manual NO consultadas y valores ILUSTRATIVOS; sin mediciones de polvo real")
    R = {}
    print("Velocidad de caida de Stokes [mm/s] y tiempo para caer 2 m, segun gravedad y diametro:")
    print("   d [um]   g = 9.81 mm/s   t [min]    g = 3.71 mm/s   t [min]   g = 1.62 mm/s   t [min]   Re(9.81)")
    filas = {}
    for d in (1.0, 5.0, 10.0, 50.0):
        dm = d * 1e-6
        fila = []
        for g in (9.81, 3.71, 1.62):
            v = v_stokes(dm, g)
            fila.append((v, H / v / 60))
        re = RHO_A * fila[0][0] * dm / MU
        filas[d] = (fila, re)
        print(f"   {d:6.0f}   {fila[0][0]*1e3:12.4f}   {fila[0][1]:8.1f}   {fila[1][0]*1e3:13.4f}   {fila[1][1]:8.1f}   {fila[2][0]*1e3:13.4f}   {fila[2][1]:8.1f}   {re:8.4f}")
        assert re < 1.0
    R["v10"], R["t10"], R["t10_luna"], R["t50"], R["v10_luna"] = filas[10.0][0][0][0], filas[10.0][0][0][1], filas[10.0][0][2][1], filas[50.0][0][0][1], filas[10.0][0][2][0]
    assert abs(filas[10.0][0][2][0] / filas[10.0][0][0][0] - 1.62 / 9.81) < 1e-12
    assert abs(filas[50.0][0][0][0] / filas[10.0][0][0][0] - 25) < 1e-9
    print("En microgravedad (g ~ 0) la velocidad de Stokes tiende a 0: las particulas no sedimentan y solo las retira el flujo y el filtro")
    eta = 0.9997
    print("Limpieza de la cabina (concentracion C/C0 = exp(-k t)), k = Q eta / V + v / H:")
    print("   caso                         k [1/s]   t al 99 % [min]")
    k_f = Q * eta / V
    casos = {"microgravedad (solo filtro)": k_f,
             "1 g, 10 um (filtro + sedimentacion)": k_f + v_stokes(10e-6, 9.81) / H,
             "Luna, 10 um": k_f + v_stokes(10e-6, 1.62) / H,
             "microgravedad, filtro de 90 %": Q * 0.90 / V}
    for nom, k in casos.items():
        print(f"   {nom:36s} {k:8.5f}   {math.log(100)/k/60:10.1f}")
    R["k_f"], R["t99_f"], R["t99_1g"], R["t99_90"] = k_f, math.log(100) / k_f / 60, math.log(100) / casos["1 g, 10 um (filtro + sedimentacion)"] / 60, math.log(100) / casos["microgravedad, filtro de 90 %"] / 60
    n_ach = Q * 3600 / V
    R["ach"] = n_ach
    print(f"Cambios de aire por hora a traves del filtro: {n_ach:.1f}; fraccion que pasa el filtro en cada paso: {1-eta:.4f}")
    assert R["t99_1g"] < R["t99_f"] < R["t99_90"]
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
