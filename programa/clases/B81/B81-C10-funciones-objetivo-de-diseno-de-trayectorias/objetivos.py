#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C10: funciones objetivo (delta-v, tiempo, masa de carga util, coste) para una espiral de bajo empuje.

Datos: g0 = 9,80665 m/s^2 (valor convencional; no consultado en esta sesion). Sin otras fuentes: todo es SINTETICO e ILUSTRATIVO.
Problema: una nave de masa inicial m0 = 1000 kg debe aportar dv = 4000 m/s (espiral, aceleracion constante a) con propulsion electrica de Isp = 3000 s.
Variable de diseno: aceleracion a [m/s^2]. Tiempo t = dv/a (aceleracion constante, masa de propelente despreciada en el tiempo).
Potencia del propulsor P = m0 a ve/(2 eta) con ve = g0 Isp y eta = 0,6; masa del sistema de potencia = alfa P con alfa = 25 kg/kW (ILUSTRATIVO).
Carga util = m0 exp(-dv/ve) - alfa P. Objetivo compuesto: J(a) = -carga_util + lambda t (lambda = 0,5 kg/dia, ILUSTRATIVO: coste de operar un dia, en kg equivalentes).
Optimo analitico: a* = sqrt(2 eta lambda' dv/(alfa m0 ve)) con lambda' = lambda/86400 (kg/s).
Segunda via: minimizacion numerica por seccion aurea. Tambien se muestran los optimos de otros objetivos (tiempo minimo con tope de potencia, carga util maxima).
Tolerancias: a* numerico frente a analitico < 1e-6 relativo.
"""
from __future__ import annotations
import math, platform

G0 = 9.80665
M0, DV, ISP, ETA, ALFA, LAM = 1000.0, 4000.0, 3000.0, 0.6, 25.0 / 1000.0, 0.5 / 86400.0  # ALFA en kg/W
VE = G0 * ISP


def carga_util(a):
    P = M0 * a * VE / (2 * ETA)
    return M0 * math.exp(-DV / VE) - ALFA * P


def tiempo_d(a):
    return DV / a / 86400.0


def J(a):
    return -carga_util(a) + LAM * DV / a


def seccion_aurea(f, lo, hi, tol=1e-14):
    g = (math.sqrt(5) - 1) / 2
    c, d = hi - g * (hi - lo), lo + g * (hi - lo)
    fc, fd = f(c), f(d)
    while hi - lo > tol * (abs(c) + abs(d)):
        if fc < fd:
            hi, d, fd = d, c, fc
            c = hi - g * (hi - lo); fc = f(c)
        else:
            lo, c, fc = c, d, fd
            d = lo + g * (hi - lo); fd = f(d)
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS: m0 = {M0:.0f} kg, dv = {DV:.0f} m/s, Isp = {ISP:.0f} s, eta = {ETA}, alfa = {ALFA*1e3:.0f} kg/kW, lambda = {LAM*86400:.1f} kg/dia")
    print(f"Fraccion de propelente = {1 - math.exp(-DV/VE):.4f} ; masa final sin sistema de potencia = {M0*math.exp(-DV/VE):.2f} kg")
    print("  a [m/s^2]    t [d]    P [kW]   carga util [kg]   J [kg]")
    for a in (1e-4, 3e-4, 1e-3, 3e-3, 1e-2):
        P = M0 * a * VE / (2 * ETA) / 1000
        print(f"  {a:9.1e}  {tiempo_d(a):8.1f}  {P:7.2f}  {carga_util(a):14.2f}  {J(a):9.2f}")
    a_an = math.sqrt(2 * ETA * LAM * DV / (ALFA * M0 * VE))
    a_num = seccion_aurea(J, 1e-5, 1e-1)
    print(f"Optimo del objetivo compuesto: a* analitico = {a_an:.6e} m/s^2 ; numerico = {a_num:.6e} ; diferencia relativa = {abs(a_an-a_num)/a_an:.1e}")
    print(f"  -> t = {tiempo_d(a_an):.1f} d ; carga util = {carga_util(a_an):.2f} kg ; P = {M0*a_an*VE/(2*ETA)/1000:.2f} kW")
    # otros objetivos
    Pmax = 5000.0  # W (ILUSTRATIVO)
    a_pmax = Pmax * 2 * ETA / (M0 * VE)
    print(f"Tiempo minimo con P <= {Pmax:.0f} W: a = {a_pmax:.3e} m/s^2, t = {tiempo_d(a_pmax):.1f} d, carga util = {carga_util(a_pmax):.2f} kg")
    a_cero = (M0 * math.exp(-DV / VE)) / (ALFA * M0 * VE / (2 * ETA))
    print(f"Carga util nula en a = {a_cero:.3e} m/s^2 ; maxima carga util cuando a -> 0 ({M0*math.exp(-DV/VE):.2f} kg), pero t -> infinito")
    for lam in (0.1, 0.5, 2.0):
        l2 = lam / 86400
        aa = math.sqrt(2 * ETA * l2 * DV / (ALFA * M0 * VE))
        print(f"  lambda = {lam:3.1f} kg/dia -> a* = {aa:.3e} m/s^2, t* = {tiempo_d(aa):7.1f} d, carga util = {carga_util(aa):7.2f} kg")
    assert abs(a_an - a_num) / a_an < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
