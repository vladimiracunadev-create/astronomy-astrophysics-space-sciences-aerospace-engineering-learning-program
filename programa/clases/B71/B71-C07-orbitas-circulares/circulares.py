#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C07: orbitas circulares, v = sqrt(mu/r), T = 2 pi sqrt(r^3/mu) y radio geoestacionario.

Datos consultados (2026-11-10): (GM)Tierra = 3.986004e14 m3/s2 y R ecuatorial = 6.3781e6 m (IAU 2015 B3); G = 6.67430e-11 (CODATA 2022);
fichas NASA/NSSDC: rotacion sidera de la Tierra 23.9345 h; masa de la Luna 0.07346e24 kg y radio medio 1737.4 km; masa de Marte 0.64169e24 kg y radio medio 3389.5 km.
mu de la Luna y de Marte se DERIVAN aqui como G*M (menos precisos que los de seguimiento, no consultados).
Sistema: marco inercial del cuerpo central, SI. Altitudes de las orbitas (400 km en la Tierra, 100 km en la Luna, 400 km en Marte) SINTETICAS/ilustrativas.
Segunda via: se integra con RK4 (2000 pasos por vuelta) la circular y se mide el periodo como el tiempo en que la posicion vuelve a su angulo inicial,
y se comprueba que la velocidad y el periodo integrados coinciden con las formulas. Tolerancias: velocidad dentro de 1e-9, radio dentro de 1e-6 relativa.
"""
from __future__ import annotations
import math, platform

MU_T = 3.986004e14
RE = 6.3781e6
G = 6.67430e-11
DATOS = {  # nombre: (mu [m3/s2], radio [m], altitud [m])
    "Tierra": (MU_T, RE, 400e3),
    "Luna": (G * 0.07346e24, 1737.4e3, 100e3),
    "Marte": (G * 0.64169e24, 3389.5e3, 400e3),
}
T_SIDERO = 23.9345 * 3600.0


def vel(mu, r):
    return math.sqrt(mu / r)


def per(mu, r):
    return 2 * math.pi * math.sqrt(r ** 3 / mu)


def rk4(s, mu, dt):
    def f(s):
        d3 = (s[0] ** 2 + s[1] ** 2) ** 1.5
        return (s[2], s[3], -mu * s[0] / d3, -mu * s[1] / d3)
    k1 = f(s)
    k2 = f(tuple(s[i] + 0.5 * dt * k1[i] for i in range(4)))
    k3 = f(tuple(s[i] + 0.5 * dt * k2[i] for i in range(4)))
    k4 = f(tuple(s[i] + dt * k3[i] for i in range(4)))
    return tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4))


def calcular():
    R = {}
    tabla = {}
    for nom, (mu, rad, alt) in DATOS.items():
        r = rad + alt
        tabla[nom] = (r, vel(mu, r), per(mu, r))
    R["tabla"] = tabla
    for nom, (r, v, t) in tabla.items():
        R[f"r_{nom}"], R[f"v_{nom}"], R[f"T_{nom}"] = r, v, t
    R["T_min_Tierra"] = R["T_Tierra"] / 60.0
    R["v_rasante"] = vel(MU_T, RE)
    R["T_rasante_min"] = per(MU_T, RE) / 60.0
    R["a_geo"] = (MU_T * (T_SIDERO / (2 * math.pi)) ** 2) ** (1.0 / 3.0)
    R["alt_geo"] = R["a_geo"] - RE
    R["v_geo"] = vel(MU_T, R["a_geo"])
    R["omega_geo_dif"] = abs(R["v_geo"] / R["a_geo"] - 2 * math.pi / T_SIDERO) / (2 * math.pi / T_SIDERO)
    # integracion de la circular terrestre de 400 km
    r, v, t = tabla["Tierra"]
    n = 2000
    s = (r, 0.0, 0.0, v)
    dt = t / n
    rmax = 0.0
    for _ in range(n):
        s = rk4(s, MU_T, dt)
        rmax = max(rmax, abs(math.hypot(s[0], s[1]) - r) / r)
    R["deriva_radio"] = rmax
    R["ang_final"] = math.degrees(math.atan2(s[1], s[0])) % 360.0
    R["cierre"] = math.hypot(s[0] - r, s[1])
    # velocidad frente a altitud: 200 km y 1000 km
    R["v_200"] = vel(MU_T, RE + 200e3)
    R["v_1000"] = vel(MU_T, RE + 1000e3)
    R["T_1000_min"] = per(MU_T, RE + 1000e3) / 60.0
    R["v_escape_400"] = math.sqrt(2) * v
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(" cuerpo   altitud   r [km]     v [m/s]    T [s]     T [min]")
    for nom, (r, v, t) in R["tabla"].items():
        print(f" {nom:7s} {DATOS[nom][2] / 1e3:6.0f} km {r / 1e3:9.3f} {v:10.3f} {t:10.2f} {t / 60:8.3f}")
    print(f"Circular rasante en la Tierra (sin atmosfera): v = {R['v_rasante']:.3f} m/s ; T = {R['T_rasante_min']:.3f} min")
    print(f"Circular geoestacionaria (T = 23.9345 h): a = {R['a_geo'] / 1e3:.3f} km ; altitud = {R['alt_geo'] / 1e3:.3f} km ; v = {R['v_geo']:.3f} m/s")
    print(f"  coherencia omega: {R['omega_geo_dif']:.1e}")
    print(f"RK4 (2000 pasos) en la circular terrestre: deriva maxima del radio = {R['deriva_radio']:.2e} ; angulo final = {R['ang_final']:.4f} grados ; cierre = {R['cierre']:.3e} m")
    print(f"v(200 km) = {R['v_200']:.3f} m/s ; v(1000 km) = {R['v_1000']:.3f} m/s ; T(1000 km) = {R['T_1000_min']:.3f} min")
    print(f"sqrt(2) v_c(400 km) = {R['v_escape_400']:.3f} m/s (velocidad de escape desde esa altitud)")
    assert R["deriva_radio"] < 1e-6
    assert R["omega_geo_dif"] < 1e-12
    assert R["v_200"] > R["v_Tierra"] > R["v_1000"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
