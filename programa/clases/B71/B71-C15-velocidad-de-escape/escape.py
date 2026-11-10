#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C15: velocidad de escape v_esc = sqrt(2 mu/r), contraste con las fichas y efecto de la rotacion.

Datos consultados (2026-11-10): G = 6.67430e-11 (CODATA 2022); (GM)Tierra = 3.986004e14, (GM)Sol = 1.3271244e20 m3/s2, R ecuatorial = 6.3781e6 m (IAU 2015 B3);
fichas NASA/NSSDC: Tierra (radio medio 6371.000 km, radio ecuatorial 6378.137 km, rotacion sidera 23.9345 h, escape 11.186 km/s, a = 149.598e6 km, velocidad orbital media 29.78 km/s);
Marte (masa 0.64169e24 kg, radio medio 3389.5 km, escape 5.03 km/s); Luna (masa 0.07346e24 kg, radio medio 1737.4 km, escape 2.38 km/s).
mu de Marte y la Luna se DERIVAN aqui como G*M. Sistema: marco inercial del cuerpo, SI; superficie esferica sin atmosfera.
Segunda via: la velocidad de escape se obtiene tambien integrando con RK4 una trayectoria radial lanzada con v = 1.05 v_esc y con v = 0.95 v_esc
(la primera debe alejarse de forma indefinida y la segunda debe regresar); se mide el radio maximo alcanzado hasta un tiempo largo.
Tolerancias: v_esc calculada frente a la ficha dentro de 5e-3 relativa (redondeo de la ficha); sqrt(2) v_c exacto 1e-12; radio maximo y velocidad final por RK4 (paso 20 s) frente a la energia dentro de 1e-4 y 1e-5 relativas.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
MU_T, MU_S, RE = 3.986004e14, 1.3271244e20, 6.3781e6
CUERPOS = {  # mu, radio, escape ficha [m/s]
    "Tierra": (MU_T, 6378.137e3, 11186.0),
    "Marte": (G * 0.64169e24, 3389.5e3, 5030.0),
    "Luna": (G * 0.07346e24, 1737.4e3, 2380.0),
}
T_SIDEREO = 23.9345 * 3600.0
AU_M = 149.598e9


def v_esc(mu, r):
    return math.sqrt(2 * mu / r)


def radio_max(mu, r0, v0, t_max, dt):
    """Lanzamiento radial; integra x'' = -mu/x^2 con RK4 hasta t_max y devuelve el radio maximo."""
    x, v, t, xmax = r0, v0, 0.0, r0
    f = lambda x, v: (v, -mu / (x * x))
    while t < t_max:
        k1 = f(x, v)
        k2 = f(x + 0.5 * dt * k1[0], v + 0.5 * dt * k1[1])
        k3 = f(x + 0.5 * dt * k2[0], v + 0.5 * dt * k2[1])
        k4 = f(x + dt * k3[0], v + dt * k3[1])
        x += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        v += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        t += dt
        xmax = max(xmax, x)
        if x < r0 * 0.99:
            break
    return xmax, x, v


def calcular():
    R = {}
    for nom, (mu, rad, ficha) in CUERPOS.items():
        v = v_esc(mu, rad)
        R[f"v_{nom}"] = v
        R[f"ficha_{nom}"] = ficha
        R[f"dif_{nom}"] = (v - ficha) / ficha
    R["vc_rasante_T"] = math.sqrt(MU_T / 6378.137e3)
    R["raiz2_dif"] = abs(R["v_Tierra"] - math.sqrt(2) * R["vc_rasante_T"]) / R["v_Tierra"]
    # Sol a 1 UA
    R["v_esc_sol_1ua"] = v_esc(MU_S, AU_M)
    R["v_orb_tierra"] = math.sqrt(MU_S / AU_M)
    R["ficha_v_orb"] = 29780.0
    R["dif_v_orb"] = (R["v_orb_tierra"] - 29780.0) / 29780.0
    R["dv_sol"] = R["v_esc_sol_1ua"] - R["v_orb_tierra"]
    # rotacion: velocidad ecuatorial
    R["v_rot"] = 2 * math.pi * 6378.137e3 / T_SIDEREO
    R["v_rot_lat28"] = R["v_rot"] * math.cos(math.radians(28.5))
    R["ahorro_pct"] = R["v_rot"] / R["v_Tierra"] * 100
    # escape desde altitud
    R["v_esc_400"] = v_esc(MU_T, RE + 400e3)
    R["v_esc_geo"] = v_esc(MU_T, 42164e3)
    # verificacion por integracion (Tierra, desde el radio ecuatorial): sin atmosfera
    mu, r0 = MU_T, 6378.137e3
    ve = v_esc(mu, r0)
    t_max = 10 * 86400.0
    xm_arriba, x_a, v_a = radio_max(mu, r0, ve * 1.05, t_max, 20.0)
    xm_abajo, x_b, v_b = radio_max(mu, r0, ve * 0.95, t_max, 20.0)
    R["rmax_arriba_km"] = xm_arriba / 1e3
    R["x_a_final_ok"] = x_a > 5 * r0
    R["rmax_abajo_km"] = xm_abajo / 1e3
    R["v_final_arriba"] = v_a
    R["v_final_teo"] = math.sqrt((ve * 1.05) ** 2 - 2 * mu / r0 + 2 * mu / x_a)
    R["dif_v_final"] = abs(v_a - R["v_final_teo"]) / R["v_final_teo"]
    R["vinf_105"] = math.sqrt((ve * 1.05) ** 2 - 2 * mu / r0)
    # radio maximo teorico para la v ligeramente menor: r = r0 / (1 - v^2 r0/(2 mu))
    vv = ve * 0.95
    R["rmax_teo_km"] = r0 / (1 - vv * vv * r0 / (2 * mu)) / 1e3
    R["dif_rmax"] = abs(R["rmax_abajo_km"] - R["rmax_teo_km"]) / R["rmax_teo_km"]
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(" cuerpo   v_esc calculada [m/s]   ficha NASA [m/s]   diferencia relativa")
    for nom in CUERPOS:
        print(f" {nom:7s} {R['v_' + nom]:14.2f} {R['ficha_' + nom]:18.0f} {R['dif_' + nom]:18.2e}")
    print(f"sqrt(2) v_circular rasante (Tierra) = {math.sqrt(2) * R['vc_rasante_T']:.3f} m/s ; dif = {R['raiz2_dif']:.1e}")
    print(f"Sol a 1 UA: v_esc = {R['v_esc_sol_1ua']:.1f} m/s ; v_orbital = {R['v_orb_tierra']:.1f} m/s (ficha 29780, dif {R['dif_v_orb']:.1e}) ; falta {R['dv_sol']:.1f} m/s")
    print(f"Rotacion terrestre (ecuador, T sidereo 23.9345 h): {R['v_rot']:.2f} m/s = {R['ahorro_pct']:.2f} % de v_esc ; a 28.5 grados de latitud (ilustrativa): {R['v_rot_lat28']:.2f} m/s")
    print(f"Escape desde 400 km de altitud: {R['v_esc_400']:.2f} m/s ; desde la distancia geoestacionaria: {R['v_esc_geo']:.2f} m/s")
    print("Integracion radial RK4 (10 d, sin atmosfera, desde el radio ecuatorial):")
    print(f"  v = 1.05 v_esc: radio alcanzado en 10 d = {R['rmax_arriba_km']:.0f} km (sigue alejandose) ; v final = {R['v_final_arriba']:.2f} m/s ; por energia = {R['v_final_teo']:.2f} m/s ; dif = {R['dif_v_final']:.1e} ; v_inf = {R['vinf_105']:.1f} m/s")
    print(f"  v = 0.95 v_esc: radio maximo = {R['rmax_abajo_km']:.0f} km ; teorico = {R['rmax_teo_km']:.0f} km ; dif = {R['dif_rmax']:.1e}")
    for nom in CUERPOS:
        assert abs(R["dif_" + nom]) < 5e-3
    assert R["raiz2_dif"] < 1e-12
    assert R["dif_rmax"] < 1e-4
    assert R["dif_v_final"] < 1e-5
    assert R["x_a_final_ok"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
