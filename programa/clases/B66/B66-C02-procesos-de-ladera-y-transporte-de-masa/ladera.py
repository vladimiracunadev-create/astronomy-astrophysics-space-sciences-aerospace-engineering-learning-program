#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B66-C02: estabilidad de ladera (pendiente infinita) y alcance de un deslizamiento en tres cuerpos.

Datos consultados (2026-11-09): g de la Tierra (9.820 m/s2) y de Marte (3.73 m/s2), fichas NASA/NSSDC;
Titan: g = GM/R^2 con GM = 8978.13710 km3/s2 y R = 2574.76 km (JPL SSD), calculada aqui.
ILUSTRATIVOS (sinteticos): angulo de friccion interna phi = 35 grados, razon de presion de poros ru = 0 y 0.5, altura de caida H = 500 m,
pendiente beta = 30 grados, coeficiente de friccion dinamica mu = 0.4.
Modelo: (a) FS = (1 - ru) tan(phi) / tan(beta), suelo sin cohesion, pendiente infinita; (b) bloque de Coulomb: aceleracion g (sin b - mu cos b)
en la pendiente y -mu g en el llano. Segunda via: integracion numerica (Euler semi-implicito, dt = 1e-3 s) del mismo bloque.
Supuestos: un solo bloque rigido, mu constante, sin atmosfera ni fluidizacion. Tolerancia: alcance numerico frente al analitico < 0.1 %.
"""
from __future__ import annotations
import math, platform

CUERPOS = {"Tierra": 9.820, "Marte": 3.73, "Titan": 8978.13710e9 / (2574.76e3) ** 2}
PHI, BETA, MU, H = math.radians(35.0), math.radians(30.0), 0.4, 500.0


def fs(phi, beta, ru):
    return (1.0 - ru) * math.tan(phi) / math.tan(beta)


def analitico(g):
    L = H / math.sin(BETA)
    a = g * (math.sin(BETA) - MU * math.cos(BETA))
    v = math.sqrt(2.0 * a * L)
    t1 = math.sqrt(2.0 * L / a)
    x = v * v / (2.0 * MU * g)
    t2 = v / (MU * g)
    return v, t1, x, t2


def numerico(g, dt=1e-3):
    L = H / math.sin(BETA)
    a = g * (math.sin(BETA) - MU * math.cos(BETA))
    s = v = t = 0.0
    while s < L:
        v += a * dt
        s += v * dt
        t += dt
    v_base = v
    x = 0.0
    while v > 0.0:
        v -= MU * g * dt
        if v > 0.0:
            x += v * dt
        t += dt
    return v_base, x


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Angulo critico sin cohesion: beta_c = atan((1-ru) tan phi): ru = 0 -> {math.degrees(math.atan(math.tan(PHI))):.2f} grados ; ru = 0.5 -> {math.degrees(math.atan(0.5 * math.tan(PHI))):.2f} grados")
    for ru in (0.0, 0.5):
        print(f"FS(beta = 30 grados, phi = 35 grados, ru = {ru}) = {fs(PHI, BETA, ru):.4f}  (identico en los tres cuerpos: g se cancela)")
    print("Bloque de Coulomb ILUSTRATIVO: H = 500 m, beta = 30 grados, mu = 0.4")
    print(" cuerpo   g [m/s2]  v_base [m/s]  t_ladera [s]  alcance llano [m]  t_llano [s]  H/L")
    dmax = 0.0
    res = {}
    for nom, g in CUERPOS.items():
        v, t1, x, t2 = analitico(g)
        vn, xn = numerico(g)
        dmax = max(dmax, abs(xn - x) / x, abs(vn - v) / v)
        L_h = H / math.tan(BETA) + x
        res[nom] = (v, t1, x)
        print(f"{nom:7s} {g:9.4f} {v:13.3f} {t1:13.3f} {x:18.3f} {t2:12.3f} {H / L_h:6.4f}")
    print(f"Diferencia relativa maxima numerico frente a analitico = {dmax:.2e}")
    rv = res["Marte"][0] / res["Tierra"][0]
    print(f"v(Marte)/v(Tierra) = {rv:.6f} ; sqrt(gM/gT) = {math.sqrt(CUERPOS['Marte'] / CUERPOS['Tierra']):.6f}")
    assert abs(rv - math.sqrt(CUERPOS["Marte"] / CUERPOS["Tierra"])) < 1e-9
    assert abs(res["Marte"][2] - res["Tierra"][2]) < 1e-6 and abs(res["Titan"][2] - res["Tierra"][2]) < 1e-6
    assert dmax < 1e-3
    assert fs(PHI, BETA, 0.5) < 1.0 < fs(PHI, BETA, 0.0)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
