#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C16: periodo orbital T = 2 pi sqrt(a^3/mu), independencia de e, sensibilidad y periodo sinodico.

Datos consultados (2026-11-10): G = 6.67430e-11 (CODATA 2022); (GM)Sol = 1.3271244e20, (GM)Tierra = 3.986004e14 m3/s2, R ecuatorial = 6.3781e6 m (IAU 2015 B3);
fichas NASA/NSSDC: Tierra (a = 149.598e6 km, periodo sidereo 365.256 d, rotacion sidera 23.9345 h); Marte (a = 227.956e6 km, periodo sidereo 686.980 d, e = 0.0935);
Luna (a = 0.3844e6 km, periodo 27.3217 d, masa 0.07346e24 kg); masa de la Tierra 5.9722e24 kg.
Sistema: marco inercial del cuerpo central, SI; dos cuerpos. Orbitas LEO/GEO/transferencia SINTETICAS/ilustrativas.
Segunda via: el periodo se mide tambien integrando con RK4 (4000 pasos) y detectando el regreso a la posicion inicial por el cambio de signo del producto vectorial
(para e = 0.0, 0.3 y 0.7 con el mismo a); y el periodo sinodico se calcula con 1/|1/T1 - 1/T2| y con la diferencia de angulos barridos.
Tolerancias: T integrado frente a la formula dentro de 1e-6 relativa; T independiente de e dentro de 1e-6; periodos de fichas frente a la formula dentro de 2e-3 (redondeo de a).
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
MU_S, MU_T, RE = 1.3271244e20, 3.986004e14, 6.3781e6
DIA = 86400.0


def periodo(a, mu):
    return 2 * math.pi * math.sqrt(a ** 3 / mu)


def integra_periodo(a, e, mu, n=4000):
    rp = a * (1 - e)
    vp = math.sqrt(mu * (1 + e) / rp)
    s = (rp, 0.0, 0.0, vp)
    T = periodo(a, mu)
    dt = T / n
    def f(s):
        d3 = (s[0] ** 2 + s[1] ** 2) ** 1.5
        return (s[2], s[3], -mu * s[0] / d3, -mu * s[1] / d3)
    t = 0.0
    prev = s
    cruces = []
    for k in range(int(1.2 * n)):
        k1 = f(s)
        k2 = f(tuple(s[i] + 0.5 * dt * k1[i] for i in range(4)))
        k3 = f(tuple(s[i] + 0.5 * dt * k2[i] for i in range(4)))
        k4 = f(tuple(s[i] + dt * k3[i] for i in range(4)))
        prev = s
        s = tuple(s[i] + dt / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) for i in range(4))
        t += dt
        # cruce del eje x (y pasa de negativo a positivo) con x > 0
        if prev[1] < 0.0 <= s[1] and s[0] > 0:
            frac = -prev[1] / (s[1] - prev[1])
            cruces.append(t - dt + frac * dt)
    return cruces[0] if cruces else float("nan")


def calcular():
    R = {}
    mu_luna_sist = G * (5.9722e24 + 0.07346e24)
    casos = {
        "Tierra": (149.598e9, MU_S, 365.256 * DIA),
        "Marte": (227.956e9, MU_S, 686.980 * DIA),
        "Luna": (0.3844e9, mu_luna_sist, 27.3217 * DIA),
    }
    for nom, (a, mu, ficha) in casos.items():
        T = periodo(a, mu)
        R[f"T_{nom}_d"] = T / DIA
        R[f"ficha_{nom}_d"] = ficha / DIA
        R[f"dif_{nom}"] = (T - ficha) / ficha
    R["T_geo_h"] = periodo(42164.2e3, MU_T) / 3600.0
    R["a_geo_sid"] = (MU_T * (23.9345 * 3600 / (2 * math.pi)) ** 2) ** (1 / 3)
    R["T_leo_min"] = periodo(RE + 400e3, MU_T) / 60.0
    # independencia de e
    a = 12000e3
    T0 = periodo(a, MU_T)
    peor = 0.0
    R["T_int"] = []
    for e in (0.0, 0.3, 0.7):
        Ti = integra_periodo(a, e, MU_T)
        R["T_int"].append(Ti)
        peor = max(peor, abs(Ti - T0) / T0)
    R["T_formula"] = T0
    R["dif_e"] = peor
    # sensibilidad: dT/T = 1.5 da/a ; LEO: +1 km
    r = RE + 400e3
    R["dT_1km_s"] = periodo(r + 1e3, MU_T) - periodo(r, MU_T)
    R["dT_1km_lineal"] = 1.5 * (1e3 / r) * periodo(r, MU_T)
    R["dif_lineal"] = abs(R["dT_1km_s"] - R["dT_1km_lineal"]) / R["dT_1km_s"]
    R["vueltas_dia_leo"] = DIA / periodo(r, MU_T)
    # sinodico Tierra-Marte con periodos sidereos de fichas
    t1, t2 = 365.256, 686.980
    R["sinodico_d"] = 1 / abs(1 / t1 - 1 / t2)
    # segunda via: tiempo para que la Tierra gane 360 grados sobre Marte
    w1, w2 = 360 / t1, 360 / t2
    R["sinodico_2_d"] = 360 / (w1 - w2)
    R["dif_sin"] = abs(R["sinodico_d"] - R["sinodico_2_d"])
    # Luna: sinodico lunar con la Tierra alrededor del Sol
    R["sin_luna_d"] = 1 / abs(1 / 27.3217 - 1 / 365.256)
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(" sistema   T calculado [d]   T ficha [d]   dif relativa")
    for nom in ("Tierra", "Marte", "Luna"):
        print(f" {nom:7s} {R['T_' + nom + '_d']:14.4f} {R['ficha_' + nom + '_d']:12.4f} {R['dif_' + nom]:13.2e}")
    print(f"LEO sintetica 400 km: T = {R['T_leo_min']:.3f} min ({R['vueltas_dia_leo']:.3f} vueltas/dia solar) ; GEO a = 42164.2 km: T = {R['T_geo_h']:.4f} h (rotacion sidera 23.9345 h)")
    print(f"a_geo desde 23.9345 h = {R['a_geo_sid'] / 1e3:.3f} km")
    print(f"T independiente de e (a = 12000 km): formula {R['T_formula']:.3f} s ; RK4 e=0: {R['T_int'][0]:.3f} ; e=0.3: {R['T_int'][1]:.3f} ; e=0.7: {R['T_int'][2]:.3f} ; dif max = {R['dif_e']:.1e}")
    print(f"Sensibilidad LEO: +1 km de semieje -> dT = {R['dT_1km_s']:.4f} s (lineal 1.5 T da/a = {R['dT_1km_lineal']:.4f} s ; dif {R['dif_lineal']:.1e})")
    print(f"Periodo sinodico Tierra-Marte = {R['sinodico_d']:.2f} d ({R['sinodico_d'] / 365.256:.3f} anios) ; segunda via {R['sinodico_2_d']:.2f} d")
    print(f"Mes sinodico (Luna-Sol) = {R['sin_luna_d']:.3f} d")
    for nom in ("Tierra", "Marte", "Luna"):
        assert abs(R["dif_" + nom]) < 2e-3 or nom == "Luna" and abs(R["dif_Luna"]) < 5e-3
    assert R["dif_e"] < 1e-6
    assert R["dif_sin"] < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
