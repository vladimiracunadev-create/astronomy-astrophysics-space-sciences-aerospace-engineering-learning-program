#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C10: fuerza de agarre de una herramienta con friccion en cuatro entornos de gravedad.

Datos consultados (2026-11-10): gravedad media de la Tierra 9.820, Marte 3.73 y la Luna 1.62 m/s2 (NASA/NSSDC). La microgravedad orbital se toma como g = 0 (idealizacion).
ILUSTRATIVOS (sinteticos, no medidos): herramienta de 2.0 kg, coeficiente de friccion 0.5, dos dedos, radio de agarre 0.02 m, par de reaccion de 2.0 N m,
aceleracion del brazo 0.5 m/s2 en la direccion de la gravedad, factor de seguridad 2.
Modelo: por dedo, la carga lineal es W/2 con W = m (g + a) y la carga tangencial por el par es tau/(2 r); el dedo resiste si hypot(W/2, tau/(2r)) <= mu F.
F_min = hypot(W/2, tau/(2 r)) / mu; F_diseno = 2 F_min. Segunda via: biseccion sobre F con el criterio de friccion (tolerancia 1e-9 N).
Unidades SI. Contacto puntual con friccion de Coulomb, sin deformacion ni dinamica del agarre.
"""
from __future__ import annotations
import math, platform

M, MU, R, TAU, A, FS = 2.0, 0.5, 0.02, 2.0, 0.5, 2.0              # ILUSTRATIVOS
ENTORNOS = {"Tierra": 9.820, "Marte": 3.73, "Luna": 1.62, "Orbita": 0.0}   # g: NASA/NSSDC; orbita = idealizacion


def demanda(g, tau=TAU):
    w = M * (g + A)
    return math.hypot(w / 2.0, tau / (2.0 * R)), w


def f_min(g, tau=TAU):
    return demanda(g, tau)[0] / MU


def f_biseccion(g, tau=TAU):
    lo, hi = 0.0, 1e6
    d = demanda(g, tau)[0]
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if MU * mid >= d:
            hi = mid
        else:
            lo = mid
    return hi


def calc():
    res = {}
    for n, g in ENTORNOS.items():
        d, w = demanda(g)
        res[n] = dict(g=g, w=w, carga=w / 2.0, tang=TAU / (2 * R), fmin=f_min(g), fdis=FS * f_min(g))
    dif = max(abs(f_min(g) - f_biseccion(g)) for g in ENTORNOS.values())
    solo_peso = M * (ENTORNOS["Tierra"] + A) / (2 * MU)
    sin_par = {n: f_min(g, 0.0) for n, g in ENTORNOS.items()}
    return dict(res=res, dif=dif, solo_peso=solo_peso, sin_par=sin_par, f_tierra=res["Tierra"]["fmin"], f_luna=res["Luna"]["fmin"], f_orbita=res["Orbita"]["fmin"],
                f_marte=res["Marte"]["fmin"], tang=res["Tierra"]["tang"], razon=res["Luna"]["fmin"] / res["Tierra"]["fmin"], fdis_t=res["Tierra"]["fdis"],
                sp_tierra=sin_par["Tierra"], sp_luna=sin_par["Luna"], sp_orbita=sin_par["Orbita"], w_tierra=res["Tierra"]["w"], w_luna=res["Luna"]["w"])


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Herramienta ILUSTRATIVA: m = {M} kg, mu = {MU}, r = {R} m, par = {TAU} N m, a = {A} m/s2, factor de seguridad {FS}")
    print(" entorno   g [m/s2]  W [N]   carga/dedo [N]  tangencial/dedo [N]  F_min [N]  F_diseno [N]")
    for n, d in r["res"].items():
        print(f"{n:8s} {d['g']:8.3f} {d['w']:7.3f} {d['carga']:15.3f} {d['tang']:19.3f} {d['fmin']:10.3f} {d['fdis']:12.3f}")
    print("F_min sin par de reaccion: " + "; ".join(f"{n} {v:.3f} N" for n, v in r["sin_par"].items()))
    print(f"Diferencia maxima formula frente a biseccion = {r['dif']:.2e} N")
    assert r["dif"] < 1e-9 and r["f_luna"] < r["f_tierra"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
