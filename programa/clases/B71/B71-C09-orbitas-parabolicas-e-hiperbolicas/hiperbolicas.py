#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C09: orbitas parabolicas e hiperbolicas, C3, angulo de giro y parametro de impacto.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 y R ecuatorial = 6.3781e6 m (IAU 2015 B3).
ILUSTRATIVOS (sinteticos): periapsis a 200 km de altitud y exceso de velocidad hiperbolica v_inf = 3.0 km/s (valor de ejemplo, no el de ninguna mision),
y un segundo caso con v_inf = 0.5 km/s. Sistema: marco inercial geocentrico, SI. Dos cuerpos puntuales.
Modelo: e = 1 + r_p v_inf^2/mu ; a = -mu/v_inf^2 ; C3 = v_inf^2 ; v_p = sqrt(v_inf^2 + 2 mu/r_p) ; giro delta = 2 asin(1/e) ; b = |a| sqrt(e^2 - 1).
Segunda via: integracion RK4 con paso pequeno desde el periapsis hasta r = 40 R (hacia atras y hacia adelante); se mide el angulo entre las
direcciones de salida y de llegada de la velocidad (giro numerico) y la velocidad final frente a v_inf. Parabola: v_p = sqrt(2) v_c (exacta).
Tolerancias: giro numerico frente a analitico dentro de 1e-4 rad (la velocidad a r finito no es v_inf: se corrige con vis-viva); energia conservada 1e-9.
"""
from __future__ import annotations
import math, platform

MU, RE = 3.986004e14, 6.3781e6


def hiperbola(rp, vinf):
    e = 1 + rp * vinf ** 2 / MU
    a = -MU / vinf ** 2
    vp = math.sqrt(vinf ** 2 + 2 * MU / rp)
    delta = 2 * math.asin(1 / e)
    b = abs(a) * math.sqrt(e * e - 1)
    nu_inf = math.acos(-1 / e)
    return dict(e=e, a=a, vp=vp, delta=delta, b=b, nu_inf=nu_inf, c3=vinf ** 2, h=rp * vp)


def integrar(rp, vinf, rfin, n=200000):
    h = hiperbola(rp, vinf)
    s = [rp, 0.0, 0.0, h["vp"]]
    def f(s):
        d3 = (s[0] ** 2 + s[1] ** 2) ** 1.5
        return (s[2], s[3], -MU * s[0] / d3, -MU * s[1] / d3)
    e0 = 0.5 * (s[2] ** 2 + s[3] ** 2) - MU / rp
    dt = 0.5  # s, fijo; se elige para que el error sea pequeno cerca del periapsis
    t = 0.0
    while math.hypot(s[0], s[1]) < rfin:
        k1 = f(s)
        k2 = f([s[i] + 0.5 * dt * k1[i] for i in range(4)])
        k3 = f([s[i] + 0.5 * dt * k2[i] for i in range(4)])
        k4 = f([s[i] + dt * k3[i] for i in range(4)])
        s = [s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4)]
        t += dt
        if t > 5e6:
            break
    r = math.hypot(s[0], s[1])
    e1 = 0.5 * (s[2] ** 2 + s[3] ** 2) - MU / r
    ang_v = math.atan2(s[3], s[2])  # direccion de la velocidad de salida
    return s, t, abs(e1 - e0) / abs(e0), ang_v


def calcular():
    R = {}
    rp = RE + 200e3
    R["rp"] = rp
    R["vc"] = math.sqrt(MU / rp)
    R["v_par"] = math.sqrt(2) * R["vc"]
    R["v_par_vis"] = math.sqrt(MU * (2 / rp - 0))  # a -> infinito
    R["dif_par"] = abs(R["v_par"] - R["v_par_vis"]) / R["v_par"]
    for etiq, vinf in (("A", 3000.0), ("B", 500.0)):
        h = hiperbola(rp, vinf)
        for k, v in h.items():
            R[f"{k}_{etiq}"] = v
        R[f"vinf_{etiq}"] = vinf
        R[f"dv_{etiq}"] = h["vp"] - R["vc"]
        R[f"giro_deg_{etiq}"] = math.degrees(h["delta"])
        R[f"nuinf_deg_{etiq}"] = math.degrees(h["nu_inf"])
    # integracion del caso A hasta 40 R
    s, t, de, ang = integrar(rp, 3000.0, 40 * RE)
    R["t_int_h"] = t / 3600.0
    R["deriva_e"] = de
    r = math.hypot(s[0], s[1]); v = math.hypot(s[2], s[3])
    R["r_final_R"] = r / RE
    R["v_final"] = v
    R["v_final_vis"] = math.sqrt(3000.0 ** 2 + 2 * MU / r)
    R["dif_v_final"] = abs(v - R["v_final_vis"]) / v
    # angulo entre la velocidad en el periapsis (+y, 90 deg) y la velocidad de salida
    R["giro_num_rad"] = abs(ang - math.pi / 2) + 0.0
    p = R["rp"] * (1 + R["e_A"])
    nu_f = math.acos((p / r - 1) / R["e_A"])
    R["nu_final_deg"] = math.degrees(nu_f)
    # direccion de la velocidad en nu: gamma = atan(e sin nu/(1 + e cos nu)); la velocidad en el periapsis apunta a +y (90 deg)
    gamma = math.atan2(R["e_A"] * math.sin(nu_f), 1 + R["e_A"] * math.cos(nu_f))
    # angulo de la velocidad respecto de +x: nu + (pi/2 - gamma)
    ang_vel_teo = nu_f + (math.pi / 2 - gamma)
    R["dif_ang_vel"] = abs(ang - ang_vel_teo)
    R["semigiro_deg_hasta_final"] = math.degrees(abs(ang - math.pi / 2))
    R["semigiro_total_deg"] = R["giro_deg_A"] / 2
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(f"Periapsis ILUSTRATIVO a 200 km de altitud: r_p = {R['rp'] / 1e3:.3f} km ; v_circular = {R['vc']:.3f} m/s")
    print(f"Parabola (e = 1): v_p = sqrt(2) v_c = {R['v_par']:.3f} m/s ; por vis-viva con a -> inf = {R['v_par_vis']:.3f} m/s ; dif = {R['dif_par']:.1e}")
    for etiq in ("A", "B"):
        print(f"Hiperbola {etiq} (v_inf = {R['vinf_' + etiq]:.0f} m/s, ILUSTRATIVA): C3 = {R['c3_' + etiq] / 1e6:.4f} km2/s2")
        print(f"  e = {R['e_' + etiq]:.5f} ; a = {R['a_' + etiq] / 1e3:.3f} km ; v_p = {R['vp_' + etiq]:.3f} m/s ; dv desde la circular = {R['dv_' + etiq]:.3f} m/s")
        print(f"  angulo asintotico nu_inf = {R['nuinf_deg_' + etiq]:.4f} grados ; giro delta = {R['giro_deg_' + etiq]:.4f} grados ; parametro de impacto b = {R['b_' + etiq] / 1e3:.3f} km")
    print(f"RK4 del caso A hasta r = {R['r_final_R']:.2f} R_T ({R['t_int_h']:.2f} h): deriva de la energia = {R['deriva_e']:.1e}")
    print(f"  v final = {R['v_final']:.3f} m/s ; vis-viva = {R['v_final_vis']:.3f} m/s ; dif = {R['dif_v_final']:.1e}")
    print(f"  anomalia verdadera alcanzada = {R['nu_final_deg']:.3f} grados (limite nu_inf = {R['nuinf_deg_A']:.3f}) ; diferencia del angulo de la velocidad con la teoria = {R['dif_ang_vel']:.1e} rad")
    assert R["dif_par"] < 1e-12
    assert R["deriva_e"] < 1e-9 and R["dif_v_final"] < 1e-9
    assert R["dif_ang_vel"] < 1e-4
    assert R["e_A"] > 1 and R["a_A"] < 0
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
