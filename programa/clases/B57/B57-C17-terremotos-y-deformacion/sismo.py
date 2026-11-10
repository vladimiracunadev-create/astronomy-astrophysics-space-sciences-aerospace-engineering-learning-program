#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C17: terremotos y deformacion: momento sismico, deslizamiento y deformacion de la superficie.

Datos: el terremoto de Maule (2010-02-27 06:34:11.530 UTC) tuvo magnitud 8.8 y profundidad de origen de 22.9 km segun el servicio de eventos del USGS
(consultado 2026-11-09). ILUSTRATIVOS: rigidez 30 GPa, falla de 500 km x 100 km, falla de dislocacion tipo tornillo con deslizamiento 4 m y profundidad
de bloqueo 15 km, incidencia 39 grados. La relacion Mw <-> M0 y la formula de la energia son conocidas y NO se consultaron.
Modelo: M0 = 10^(1.5 Mw + 9.1) N m ; deslizamiento medio D = M0/(mu A) ; energia radiada E ~ 10^(1.5 Mw + 4.8) J ; desplazamiento de una falla
de tornillo infinita u(x) = (s/pi) arctan(x/D_b) ; proyeccion a la linea de vision d = u_v cos(theta) - u_e sen(theta) (convencion de la clase).
Validez: medio elastico homogeneo, falla vertical. Tolerancia: ida y vuelta Mw -> M0 -> Mw < 1e-12; derivada numerica de u(x) frente a la analitica < 1e-6.
"""
import math, platform

MU = 30e9
A = 500e3 * 100e3
S_DESL, D_B = 4.0, 15e3
THETA = math.radians(39.0)
LAM = 0.05547


def m0(mw):
    return 10 ** (1.5 * mw + 9.1)


def mw(M0):
    return (math.log10(M0) - 9.1) / 1.5


def u(x):
    return (S_DESL / math.pi) * math.atan(x / D_B)


def calcular():
    r = {}
    r["M0"] = m0(8.8)
    r["Mw_rec"] = mw(r["M0"])
    r["err_ida"] = abs(r["Mw_rec"] - 8.8)
    r["D"] = r["M0"] / (MU * A)
    r["E"] = 10 ** (1.5 * 8.8 + 4.8)
    r["factor_M0_por_unidad"] = m0(9.8) / m0(8.8)
    r["factor_E_por_unidad"] = 10 ** 1.5
    r["factor_M0_por_02"] = m0(9.0) / m0(8.8)
    r["u_lejos"] = u(1e12)
    r["u_ideal"] = S_DESL / 2
    h = 10.0
    num = (u(h) - u(-h)) / (2 * h)
    ana = S_DESL / (math.pi * D_B)
    r["err_deriv"] = abs(num / ana - 1)
    r["u_15km"] = u(15e3)
    r["u_50km"] = u(50e3)
    r["los_v"] = math.cos(THETA)
    r["los_e"] = -math.sin(THETA)
    r["franjas_los"] = 3.0 * math.cos(THETA) / (LAM / 2)
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Mw 8.8: M0 = {r['M0']:.3e} N m ; ida y vuelta Mw = {r['Mw_rec']:.12f} (error {r['err_ida']:.1e})")
    print(f"Deslizamiento medio con 30 GPa y 500 x 100 km = {r['D']:.2f} m ; energia radiada = {r['E']:.2e} J")
    print(f"Una unidad de Mw multiplica M0 por {r['factor_M0_por_unidad']:.1f} y la energia por {r['factor_E_por_unidad']:.1f} ; +0.2 en Mw multiplica M0 por {r['factor_M0_por_02']:.2f}")
    print(f"Falla de tornillo: u(infinito) = {r['u_lejos']:.4f} m (s/2 = {r['u_ideal']:.4f}) ; u(15 km) = {r['u_15km']:.3f} m ; u(50 km) = {r['u_50km']:.3f} m ; error de la derivada = {r['err_deriv']:.1e}")
    print(f"Proyeccion a la LOS (39 grados): vertical x{r['los_v']:.3f} ; este x{r['los_e']:.3f} ; 3 m verticales = {r['franjas_los']:.1f} franjas")
    assert r["err_ida"] < 1e-12
    assert abs(r["u_lejos"] - r["u_ideal"]) < 1e-6
    assert r["err_deriv"] < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
