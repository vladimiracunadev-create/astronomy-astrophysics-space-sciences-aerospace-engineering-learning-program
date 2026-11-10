#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C14: cobertura de regolito de un habitat cilindrico (blindaje por densidad superficial y carga frente a la presion interna).

Datos consultados (2026-11-10): gravedad media de la Luna 1.62, Marte 3.73 y la Tierra 9.820 m/s2 (NASA/NSSDC).
ILUSTRATIVOS (sinteticos, no medidos): presion interna 70 kPa, densidad aparente del regolito 1500 kg/m3, densidad superficial de blindaje objetivo 2000 kg/m2,
cilindro de radio interior 4.0 m y longitud 10.0 m. NINGUNO de estos valores es una norma, un requisito ni una propiedad medida de un regolito.
Modelo: espesor t = sigma/rho (no depende de g); presion de la sobrecarga p = rho g t; espesor que equilibraria la presion t_eq = P/(rho g);
volumen de la cubierta V = pi ((r + t)^2 - r^2) L; masa = rho V.
Segunda via: volumen por integracion numerica de anillos finos (Simpson, 2000 intervalos), tolerancia relativa 1e-9.
Unidades SI. Cubierta uniforme que rodea todo el cilindro, sin tapas, sin huecos ni compactacion variable; no es un calculo estructural.
"""
from __future__ import annotations
import math, platform

P_INT, RHO, SIGMA, R, L = 70e3, 1500.0, 2000.0, 4.0, 10.0              # ILUSTRATIVOS
GRAV = {"Luna": 1.62, "Marte": 3.73, "Tierra": 9.820}                   # NASA/NSSDC


def volumen(t):
    return math.pi * ((R + t) ** 2 - R ** 2) * L


def volumen_num(t, n=2000):
    f = lambda r: 2 * math.pi * r * L
    h = t / n
    tot = f(R) + f(R + t)
    for i in range(1, n):
        tot += (4 if i % 2 else 2) * f(R + i * h)
    return tot * h / 3


def calc():
    t = SIGMA / RHO
    v = volumen(t)
    cuerpos = {}
    for n, g in GRAV.items():
        p = RHO * g * t
        cuerpos[n] = dict(p=p, frac=p / P_INT, t_eq=P_INT / (RHO * g), neta=P_INT - p)
    return dict(t=t, v=v, masa=RHO * v, masa_t=RHO * v / 1000, dif=abs(v - volumen_num(t)) / v, cuerpos=cuerpos,
                p_luna=cuerpos["Luna"]["p"], f_luna=cuerpos["Luna"]["frac"], teq_luna=cuerpos["Luna"]["t_eq"], teq_marte=cuerpos["Marte"]["t_eq"],
                teq_tierra=cuerpos["Tierra"]["t_eq"], p_marte=cuerpos["Marte"]["p"], f_marte=cuerpos["Marte"]["frac"], p_tierra=cuerpos["Tierra"]["p"],
                f_tierra=cuerpos["Tierra"]["frac"], neta_luna=cuerpos["Luna"]["neta"], area=2 * math.pi * R * L, masa_aprox=SIGMA * 2 * math.pi * R * L,
                masa_m2=SIGMA)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Habitat ILUSTRATIVO: r = {R} m, L = {L} m; P = {P_INT/1e3:.0f} kPa; rho = {RHO:.0f} kg/m3; blindaje objetivo = {SIGMA:.0f} kg/m2")
    print(f"Espesor de cubierta t = sigma/rho = {r['t']:.4f} m (igual en los tres cuerpos); volumen = {r['v']:.2f} m3; masa = {r['masa_t']:.1f} t")
    print(" cuerpo   sobrecarga [kPa]   fraccion de P   espesor de equilibrio [m]   presion neta hacia arriba [kPa]")
    for n, d in r["cuerpos"].items():
        print(f"{n:7s} {d['p']/1e3:16.3f} {d['frac']:15.4f} {d['t_eq']:27.2f} {d['neta']/1e3:30.2f}")
    print(f"Masa de una cubierta delgada (sigma x area interior) = {r['masa_aprox']/1000:.1f} t; la exacta es {r['masa_t']:.1f} t")
    print(f"Diferencia relativa entre volumen cerrado e integral numerica = {r['dif']:.2e}")
    assert r["dif"] < 1e-9 and r["f_luna"] < r["f_marte"] < r["f_tierra"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
