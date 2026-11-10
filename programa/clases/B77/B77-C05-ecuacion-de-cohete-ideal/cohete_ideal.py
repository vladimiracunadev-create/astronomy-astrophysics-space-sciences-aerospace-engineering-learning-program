#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C05: ecuacion de cohete ideal y su integracion numerica.

Datos consultados (2026-11-10): Delta_v = V_eq ln(m_f/m_e) = Isp g0 ln(MR); con gravedad Delta_v = V_eq ln(MR) - g0 t_b (NASA Glenn, Ideal Rocket Equation;
la pagina usa 'm_f' para la masa inicial y 'm_e' para la vacia); g0 = 9.80665 m/s2 (NIST CODATA 2022). El ejemplo de la pagina: Isp ~ 350 s, Delta_u ~ 25 000 ft/s (7620 m/s), MR ~ 10.
ILUSTRATIVOS (sinteticos): Isp = 350 s, masa inicial 100 000 kg, masa final 10 000 kg, empuje constante 1.5 MN, g constante.
Sistema: eje vertical local, Tierra plana con g = g0 constante, SI.
Modelo: dv/dt = F/m - g, dm/dt = -F/(Isp g0), integrado con RK4; comparado con la forma cerrada.
Segunda via: despejar MR para un Delta_v dado y recuperar el Delta_v.
Tolerancias: integracion frente a forma cerrada 1e-9 relativa (RK4 con 20000 pasos); ida y vuelta de MR 1e-12.
"""
import math, platform

G0, ISP = 9.80665, 350.0
M0, MF, F = 100000.0, 10000.0, 1.5e6


def dv_ideal(isp, mr):
    return isp * G0 * math.log(mr)


def mr_para(dv, isp):
    return math.exp(dv / (isp * G0))


def integra(n=20000):
    mdot = F / (ISP * G0)
    tb = (M0 - MF) / mdot
    dt = tb / n
    v, m = 0.0, M0

    def a(m_):
        return F / m_ - G0
    for _ in range(n):
        k1v = a(m); k2v = a(m - 0.5 * dt * mdot); k3v = k2v; k4v = a(m - dt * mdot)
        v += dt * (k1v + 2 * k2v + 2 * k3v + k4v) / 6
        m -= dt * mdot
    return v, tb


def calcular():
    r = {}
    r["c"] = ISP * G0
    r["mr"] = M0 / MF
    r["dv_ideal"] = dv_ideal(ISP, r["mr"])
    v, tb = integra()
    r["tb"], r["v_num"] = tb, v
    r["dv_grav"] = r["dv_ideal"] - G0 * tb
    r["err"] = abs(v - r["dv_grav"]) / r["dv_grav"]
    r["perdida_g"] = G0 * tb
    r["mr_ida_vuelta"] = abs(mr_para(r["dv_ideal"], ISP) - r["mr"]) / r["mr"]
    # el ejemplo de la pagina de la NASA Glenn: 25 000 ft/s
    dv_p = 25000 * 0.3048
    r["dv_pagina"] = dv_p
    r["mr_pagina"] = mr_para(dv_p, 350.0)
    r["frac_prop_pagina"] = 1 - 1 / r["mr_pagina"]
    r["tabla"] = [(isp, dv_ideal(isp, r["mr"])) for isp in (250.0, 300.0, 350.0, 450.0)]
    r["tmr"] = [(mr, dv_ideal(ISP, mr)) for mr in (2.0, 5.0, 10.0, 20.0)]
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Cohete SINTETICO: Isp = {ISP} s (c = {r['c']:.2f} m/s), m0 = {M0:.0f} kg, mf = {MF:.0f} kg (MR = {r['mr']:.1f}), F = {F/1e6} MN")
    print(f"Delta_v ideal = {r['dv_ideal']:.3f} m/s; tiempo de combustion = {r['tb']:.2f} s; perdida g0 tb = {r['perdida_g']:.2f} m/s")
    print(f"Delta_v con gravedad (cerrada) = {r['dv_grav']:.3f} m/s; integracion RK4 = {r['v_num']:.3f} m/s; error relativo = {r['err']:.2e}")
    print("Delta_v ideal para MR = 10 segun Isp: " + "; ".join(f"{i:.0f} s -> {d:.0f} m/s" for i, d in r["tabla"]))
    print("Delta_v ideal para Isp = 350 s segun MR: " + "; ".join(f"MR {m:.0f} -> {d:.0f} m/s" for m, d in r["tmr"]))
    print(f"Ejemplo de la pagina: Delta_u = 25000 ft/s = {r['dv_pagina']:.0f} m/s con Isp = 350 s da MR = {r['mr_pagina']:.2f} (la pagina dice ~10); propelente = {r['frac_prop_pagina']*100:.1f} % de la masa inicial")
    print(f"Ida y vuelta Delta_v -> MR: error relativo = {r['mr_ida_vuelta']:.1e}")
    assert r["err"] < 1e-9
    assert r["mr_ida_vuelta"] < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
