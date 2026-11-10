#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C05: energia orbital especifica epsilon = v^2/2 - mu/r = -mu/(2a), vis-viva y conservacion.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 y R ecuatorial = 6.3781e6 m (IAU 2015 B3).
Sistema: marco inercial geocentrico, SI. Dos cuerpos puntuales.
ORBITAS SINTETICAS (ilustrativas): circular a 400 km de altitud; de transferencia con periapsis a 200 km y apoapsis a 35786 km de altitud (GTO).
Segunda via: la energia a lo largo de una integracion RK4 (4000 pasos por vuelta) debe coincidir con -mu/(2a) y la velocidad de vis-viva con la integrada.
Tolerancias: deriva relativa de la energia en una vuelta < 1e-9; vis-viva frente a integracion dentro de 1e-6 relativa.
"""
from __future__ import annotations
import math, platform

MU = 3.986004e14
RE = 6.3781e6


def eps(v, r):
    return 0.5 * v * v - MU / r


def vis_viva(r, a):
    return math.sqrt(MU * (2.0 / r - 1.0 / a))


def rk4(s, dt):
    def f(s):
        d3 = (s[0] ** 2 + s[1] ** 2) ** 1.5
        return (s[2], s[3], -MU * s[0] / d3, -MU * s[1] / d3)
    k1 = f(s)
    k2 = f(tuple(s[i] + 0.5 * dt * k1[i] for i in range(4)))
    k3 = f(tuple(s[i] + 0.5 * dt * k2[i] for i in range(4)))
    k4 = f(tuple(s[i] + dt * k3[i] for i in range(4)))
    return tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4))


def calcular():
    R = {}
    rc = RE + 400e3
    R["a_circ"] = rc
    R["eps_circ"] = -MU / (2 * rc)
    R["v_circ"] = math.sqrt(MU / rc)
    R["ek_circ"] = 0.5 * R["v_circ"] ** 2
    R["ep_circ"] = -MU / rc
    R["eps_circ_dir"] = eps(R["v_circ"], rc)
    rp, ra = RE + 200e3, RE + 35786e3
    a = 0.5 * (rp + ra)
    R["rp"], R["ra"], R["a_gto"] = rp, ra, a
    R["eps_gto"] = -MU / (2 * a)
    R["vp"], R["va"] = vis_viva(rp, a), vis_viva(ra, a)
    R["eps_p"], R["eps_a"] = eps(R["vp"], rp), eps(R["va"], ra)
    R["dif_pa"] = abs(R["eps_p"] - R["eps_a"]) / abs(R["eps_gto"])
    t = 2 * math.pi * math.sqrt(a ** 3 / MU)
    R["T"] = t
    n = 4000
    s = (rp, 0.0, 0.0, R["vp"])
    dmax = 0.0
    vis_err = 0.0
    for k in range(n):
        s = rk4(s, t / n)
        r = math.hypot(s[0], s[1])
        e = eps(math.hypot(s[2], s[3]), r)
        dmax = max(dmax, abs(e - R["eps_gto"]) / abs(R["eps_gto"]))
        vis_err = max(vis_err, abs(vis_viva(r, a) - math.hypot(s[2], s[3])) / vis_viva(r, a))
    R["deriva"] = dmax
    R["vis_err"] = vis_err
    # energia de ligadura frente a la de una orbita circular de radio a
    R["eps_sup_reposo"] = -MU / RE
    R["dv_leo_gto"] = R["vp"] - math.sqrt(MU / rp)
    R["de_leo_gto"] = R["eps_gto"] - (-MU / (2 * rp))
    R["eps_escape"] = 0.0
    R["falta_gto"] = -R["eps_gto"]
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print("Orbita circular SINTETICA a 400 km de altitud:")
    print(f"  r = a = {R['a_circ'] / 1e3:.3f} km ; v = {R['v_circ']:.3f} m/s")
    print(f"  Ek = {R['ek_circ'] / 1e6:.4f} MJ/kg ; Ep = {R['ep_circ'] / 1e6:.4f} MJ/kg ; epsilon = {R['eps_circ_dir'] / 1e6:.4f} MJ/kg = -mu/(2a) = {R['eps_circ'] / 1e6:.4f} MJ/kg")
    print("Orbita de transferencia SINTETICA (periapsis 200 km, apoapsis 35786 km de altitud):")
    print(f"  a = {R['a_gto'] / 1e3:.3f} km ; T = {R['T']:.2f} s ; v_p = {R['vp']:.3f} m/s ; v_a = {R['va']:.3f} m/s")
    print(f"  epsilon = -mu/(2a) = {R['eps_gto'] / 1e6:.5f} MJ/kg ; en el periapsis {R['eps_p'] / 1e6:.5f} ; en el apoapsis {R['eps_a'] / 1e6:.5f}")
    print(f"  diferencia relativa periapsis-apoapsis = {R['dif_pa']:.2e}")
    print(f"  RK4 (4000 pasos): deriva maxima de epsilon = {R['deriva']:.2e} ; error maximo de vis-viva = {R['vis_err']:.2e}")
    print(f"  energia que falta para escapar = {R['falta_gto'] / 1e6:.4f} MJ/kg")
    print(f"  epsilon de un cuerpo en reposo en el ecuador = {R['eps_sup_reposo'] / 1e6:.3f} MJ/kg")
    assert abs(R["eps_circ"] - R["eps_circ_dir"]) < 1e-6 * abs(R["eps_circ"])
    assert R["dif_pa"] < 1e-12
    assert R["deriva"] < 1e-9 and R["vis_err"] < 1e-6
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
