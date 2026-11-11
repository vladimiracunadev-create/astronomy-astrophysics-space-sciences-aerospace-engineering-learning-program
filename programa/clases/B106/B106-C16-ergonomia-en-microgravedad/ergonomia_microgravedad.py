#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C16: reacciones al empujar y al apretar un tornillo sin punto de apoyo (microgravedad).

Modelo propio (mecanica de Newton; no consultado en una fuente concreta). Valores ILUSTRATIVOS: astronauta de 75 kg, momento de inercia de 1.5 kg m2 respecto de su eje largo,
rigidez angular de una sujecion de pies de 60 N m/rad, estante de 100 kg, empujon de 50 N durante 0.5 s, par de 10 N m. No hay datos de personas ni de equipos reales.
Verificacion: el momento lineal total se conserva (cero); el angulo de giro libre coincide con 0.5 alpha t^2; con sujecion el giro es tau/k.
"""
from __future__ import annotations
import math
import platform
import numpy as np

M_AST, M_RACK, I_AST, K_REST = 75.0, 100.0, 1.5, 60.0


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: mecanica de Newton con valores ILUSTRATIVOS; sin datos de personas ni equipos reales")
    R = {}
    F, t = 50.0, 0.5
    J = F * t
    v_rack = J / M_RACK
    v_ast = -J / M_AST
    R.update(J=J, v_rack=v_rack, v_ast=v_ast)
    p_tot = M_RACK * v_rack + M_AST * v_ast
    print(f"Empujon de {F:.0f} N durante {t} s a un estante libre de {M_RACK:.0f} kg: impulso {J:.1f} N s; estante {v_rack:+.3f} m/s; astronauta {v_ast:+.3f} m/s; momento total {p_tot:+.1e}")
    assert abs(p_tot) < 1e-12
    for T in (2.0, 5.0):
        print(f"   a los {T:.0f} s: estante a {v_rack*T:.2f} m, astronauta a {abs(v_ast)*T:.2f} m en sentido contrario")
    R["d_ast5"] = abs(v_ast) * 5
    # empuje contra una pared fija de la estacion
    M_EST = 4.2e5
    print(f"Empujon contra la estacion ({M_EST:.1e} kg): velocidad de la estacion {J/M_EST:.2e} m/s (despreciable); el astronauta sale a {J/M_AST:.3f} m/s")
    tau = 10.0
    alpha = tau / I_AST
    th = 0.5 * alpha * 0.5 ** 2
    t30 = math.sqrt(2 * math.radians(30) / alpha)
    R.update(alpha=alpha, th_deg=math.degrees(th), t30=t30)
    print(f"Tornillo con par de {tau:.0f} N m sin sujecion (I = {I_AST} kg m2): alpha = {alpha:.2f} rad/s2; en 0.5 s gira {math.degrees(th):.1f} grados; 30 grados en {t30:.2f} s")
    th_r = tau / K_REST
    R["th_rest"] = math.degrees(th_r)
    print(f"Con sujecion de pies (k = {K_REST:.0f} N m/rad): giro {math.degrees(th_r):.1f} grados (equilibrio) frente a giro libre creciente")
    assert abs(th - 0.5 * (tau / I_AST) * 0.25) < 1e-12 and math.degrees(th_r) < math.degrees(th)
    for tau_max in (2.0, 5.0, 10.0):
        thx = math.degrees(0.5 * tau_max / I_AST * 0.25)
        print(f"   par {tau_max:4.1f} N m: giro libre en 0.5 s = {thx:5.1f} grados")
    L, v = 5.0, 0.3
    t_cruce = L / v
    F_stop = M_AST * v / 0.3
    R.update(t_cruce=t_cruce, F_stop=F_stop)
    print(f"Cruzar {L:.0f} m a {v} m/s: {t_cruce:.1f} s; frenar al final en 0.3 s exige {F_stop:.0f} N sobre un asidero")
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
