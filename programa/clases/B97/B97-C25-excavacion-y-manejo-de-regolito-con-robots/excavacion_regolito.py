#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C25: fuerza de excavacion, limite de traccion y productividad de una excavadora robotica en tres gravedades.

Datos consultados (2026-11-10): gravedad media de la Tierra 9.820, Marte 3.73 y la Luna 1.62 m/s2 (NASA/NSSDC).
ILUSTRATIVOS (sinteticos, no medidos): excavadora de 100 kg, coeficiente de friccion de reaccion 0.6, ancho de cuchara 0.40 m, longitud de corte 1.0 m,
cohesion 1.0 kPa, factores de capacidad N_c = 8 y N_gamma = 5, densidad aparente 1500 kg/m3, velocidad de corte 0.05 m/s, acarreo de 50 m a 0.30 m/s, 15 s de descarga.
Ninguno es una propiedad real de un regolito ni de una maquina.
Modelo: fuerza de corte por unidad de ancho F = w d (c N_c + 0.5 rho g d N_gamma); la maquina solo puede reaccionar con mu m g (peso x friccion); profundidad maxima d: F(d) = mu m g
(ecuacion cuadratica); volumen por ciclo = w d L; ciclo = L/v_corte + 2 D/v_acarreo + t_descarga; productividad = masa del ciclo / tiempo del ciclo.
Segunda via: la profundidad maxima por biseccion frente a la solucion cuadratica cerrada (tolerancia 1e-9 m).
Unidades SI. Corte plano de profundidad constante, sin llenado parcial de la cuchara ni desgaste, y sin variaciones del suelo.
"""
from __future__ import annotations
import math, platform

GRAV = {"Tierra": 9.820, "Marte": 3.73, "Luna": 1.62}                                 # NASA/NSSDC
MASA, MU, W, LCORTE, C, NC, NG, RHO = 100.0, 0.6, 0.40, 1.0, 1000.0, 8.0, 5.0, 1500.0   # ILUSTRATIVOS
V_CORTE, DIST, V_ACARREO, T_DESC = 0.05, 50.0, 0.30, 15.0


def fuerza(d, g):
    return W * d * (C * NC + 0.5 * RHO * g * d * NG)


def d_cuadratica(g, masa):
    f0 = MU * masa * g
    a, b = 0.5 * W * RHO * g * NG, W * C * NC
    return (-b + math.sqrt(b * b + 4 * a * f0)) / (2 * a)


def d_biseccion(g, masa):
    lo, hi = 0.0, 5.0
    f0 = MU * masa * g
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if fuerza(mid, g) > f0:
            hi = mid
        else:
            lo = mid
    return lo


def productividad(d, t_extra=0.0):
    vol = W * d * LCORTE
    t = LCORTE / V_CORTE + 2 * DIST / V_ACARREO + T_DESC + t_extra
    return vol, RHO * vol, t, RHO * vol / t * 3600


def calc():
    res = {}
    for n, g in GRAV.items():
        d = d_cuadratica(g, MASA)
        res[n] = dict(g=g, f0=MU * MASA * g, dmax=d, dmax_b=d_biseccion(g, MASA), f_cohes=W * C * NC * 0.05, f_5cm=fuerza(0.05, g), prod=productividad(d))
    dif = max(abs(v["dmax"] - v["dmax_b"]) for v in res.values())
    masa_luna_5cm = next(m for m in range(100, 5000, 5) if d_cuadratica(GRAV["Luna"], m) >= 0.05)
    p5 = productividad(0.05)
    return dict(res=res, dif=dif, masa_luna_5cm=masa_luna_5cm, d_tierra=res["Tierra"]["dmax"], d_marte=res["Marte"]["dmax"], d_luna=res["Luna"]["dmax"],
                f0_luna=res["Luna"]["f0"], f0_tierra=res["Tierra"]["f0"], f0_marte=res["Marte"]["f0"], f5_luna=res["Luna"]["f_5cm"], f5_tierra=res["Tierra"]["f_5cm"],
                vol5=p5[0], masa5=p5[1], t_ciclo=p5[2], prod5=p5[3], prod_luna=res["Luna"]["prod"][3], prod_tierra=res["Tierra"]["prod"][3], t_corte=LCORTE / V_CORTE,
                t_acarreo=2 * DIST / V_ACARREO, ciclos_t=1000.0 / p5[1])


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Excavadora ILUSTRATIVA: {MASA:.0f} kg, mu = {MU}, cuchara {W} m, corte {LCORTE} m; suelo c = {C:.0f} Pa, N_c = {NC}, N_gamma = {NG}, rho = {RHO:.0f} kg/m3")
    print(" cuerpo   reaccion max mu m g [N]   fuerza a 5 cm [N]   profundidad maxima [m]   (biseccion)   productividad a d_max [kg/h]")
    for n, v in r["res"].items():
        print(f"{n:7s} {v['f0']:22.1f} {v['f_5cm']:19.1f} {v['dmax']:22.5f} {v['dmax_b']:13.5f} {v['prod'][3]:24.2f}")
    print(f"Ciclo a 5 cm: corte {r['t_corte']:.0f} s + acarreo {r['t_acarreo']:.0f} s + descarga {T_DESC:.0f} s = {r['t_ciclo']:.0f} s; masa por ciclo = {r['masa5']:.2f} kg; productividad = {r['prod5']:.2f} kg/h")
    print(f"Ciclos para mover 1 t a 5 cm: {r['ciclos_t']:.0f}; masa minima de la excavadora para cortar 5 cm en la Luna = {r['masa_luna_5cm']} kg")
    print(f"Diferencia maxima entre solucion cuadratica y biseccion = {r['dif']:.2e} m")
    assert r["dif"] < 1e-9 and r["d_luna"] < r["d_marte"] < r["d_tierra"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
