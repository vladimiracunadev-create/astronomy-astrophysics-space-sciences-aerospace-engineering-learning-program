#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C01: leyes de Kepler comprobadas con datos de fichas y con una integracion numerica.

Datos consultados (2026-11-10): fichas NASA/NSSDC de la Tierra (a = 149.598e6 km, T = 365.256 d), de Marte (a = 227.956e6 km,
e = 0.0935, T = 686.980 d) y de la Luna (a = 0.3844e6 km, T = 27.3217 d); constante nominal (GM)sol = 1.3271244e20 m3/s2 y
(GM)Tierra = 3.986004e14 m3/s2 (IAU 2015 B3). Sistema: marco inercial del cuerpo central, SI (m, s). Dos cuerpos puntuales.
Segunda via: la 2.a ley se comprueba integrando r'' = -mu r/|r|^3 con RK4 (paso T/4000), no con la formula de la elipse.
Datos de la integracion: orbita SINTETICA con a y e de Marte (0.0935) alrededor del Sol; no es una efemeride.
Tolerancias: areas iguales en 1e-6 relativa; 3.a ley (cociente a^3/T^2 Tierra/Marte) dentro de 1e-3 por el redondeo de las fichas.
"""
from __future__ import annotations
import math, platform

AU_KM = 149.598e6
DIA = 86400.0
MU_SOL = 1.3271244e20
MU_TIERRA = 3.986004e14
DATOS = {  # a [m], T [s]
    "Tierra": (149.598e9, 365.256 * DIA),
    "Marte": (227.956e9, 686.980 * DIA),
    "Luna": (0.3844e9, 27.3217 * DIA),
}
E_MARTE = 0.0935


def constante(a, t):
    return a ** 3 / t ** 2


def gm_estimado(a, t):
    return 4.0 * math.pi ** 2 * a ** 3 / t ** 2


def rk4(r, v, mu, dt):
    def acc(p):
        d = math.hypot(*p)
        return (-mu * p[0] / d ** 3, -mu * p[1] / d ** 3)
    a1 = acc(r)
    k1r, k1v = v, a1
    r2 = (r[0] + 0.5 * dt * k1r[0], r[1] + 0.5 * dt * k1r[1]); v2 = (v[0] + 0.5 * dt * k1v[0], v[1] + 0.5 * dt * k1v[1])
    k2r, k2v = v2, acc(r2)
    r3 = (r[0] + 0.5 * dt * k2r[0], r[1] + 0.5 * dt * k2r[1]); v3 = (v[0] + 0.5 * dt * k2v[0], v[1] + 0.5 * dt * k2v[1])
    k3r, k3v = v3, acc(r3)
    r4 = (r[0] + dt * k3r[0], r[1] + dt * k3r[1]); v4 = (v[0] + dt * k3v[0], v[1] + dt * k3v[1])
    k4r, k4v = v4, acc(r4)
    rn = tuple(r[i] + dt / 6.0 * (k1r[i] + 2 * k2r[i] + 2 * k3r[i] + k4r[i]) for i in range(2))
    vn = tuple(v[i] + dt / 6.0 * (k1v[i] + 2 * k2v[i] + 2 * k3v[i] + k4v[i]) for i in range(2))
    return rn, vn


def areas_iguales(a, e, mu, n_pasos=4000, n_sectores=8):
    """Area barrida (regla del triangulo r x dr /2) en n_sectores intervalos de igual tiempo; periapsis en +x."""
    rp = a * (1 - e)
    vp = math.sqrt(mu * (1 + e) / rp)
    t = 2 * math.pi * math.sqrt(a ** 3 / mu)
    dt = t / n_pasos
    r, v = (rp, 0.0), (0.0, vp)
    areas = [0.0] * n_sectores
    por = n_pasos // n_sectores
    for k in range(n_pasos):
        rn, vn = rk4(r, v, mu, dt)
        areas[k // por] += 0.5 * abs(r[0] * rn[1] - r[1] * rn[0])
        r, v = rn, vn
    return areas, math.hypot(r[0] - rp, r[1]), t


def calcular():
    R = {}
    for nom, (a, t) in DATOS.items():
        R["k_" + nom] = constante(a, t)
    R["razon_tm"] = R["k_Tierra"] / R["k_Marte"]
    R["gm_sol_t"] = gm_estimado(*DATOS["Tierra"])
    R["gm_sol_m"] = gm_estimado(*DATOS["Marte"])
    R["err_sol_t"] = abs(R["gm_sol_t"] - MU_SOL) / MU_SOL
    R["err_sol_m"] = abs(R["gm_sol_m"] - MU_SOL) / MU_SOL
    R["gm_tierra_luna"] = gm_estimado(*DATOS["Luna"])
    R["err_luna"] = abs(R["gm_tierra_luna"] - MU_TIERRA) / MU_TIERRA
    a, t = DATOS["Marte"]
    areas, cierre, per = areas_iguales(a, E_MARTE, MU_SOL)
    R["areas"] = areas
    R["disp_areas"] = (max(areas) - min(areas)) / (sum(areas) / len(areas))
    R["cierre_m"] = cierre
    R["periodo_num_d"] = per / DIA
    rp, ra = a * (1 - E_MARTE), a * (1 + E_MARTE)
    R["vp_va"] = (math.sqrt(MU_SOL * (1 + E_MARTE) / rp)) / (math.sqrt(MU_SOL * (1 - E_MARTE) / ra))
    R["ra_rp"] = ra / rp
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print("3.a ley: a^3/T^2 [m3/s2] (fichas NASA/NSSDC)")
    for nom in DATOS:
        print(f"  {nom:7s} {R['k_' + nom]:.6e}")
    print(f"  cociente Tierra/Marte = {R['razon_tm']:.6f}")
    print("GM = 4 pi^2 a^3/T^2 frente al nominal IAU 2015:")
    print(f"  Sol (Tierra) {R['gm_sol_t']:.7e} m3/s2 ; error relativo {R['err_sol_t']:.2e}")
    print(f"  Sol (Marte)  {R['gm_sol_m']:.7e} m3/s2 ; error relativo {R['err_sol_m']:.2e}")
    print(f"  Tierra (Luna) {R['gm_tierra_luna']:.6e} m3/s2 ; error relativo {R['err_luna']:.2e}")
    print("2.a ley: orbita SINTETICA a = 227.956e9 m, e = 0.0935 (RK4, 4000 pasos, 8 sectores de igual tiempo)")
    print("  areas [1e18 m2]: " + " ".join(f"{x / 1e18:.5f}" for x in R["areas"]))
    print(f"  dispersion relativa (max-min)/media = {R['disp_areas']:.2e}")
    print(f"  periodo de la integracion = {R['periodo_num_d']:.3f} d ; cierre de la orbita = {R['cierre_m']:.3e} m")
    print(f"  v_peri/v_afelio = {R['vp_va']:.6f} ; r_afelio/r_peri = {R['ra_rp']:.6f}")
    assert abs(R["razon_tm"] - 1) < 1e-3
    assert R["err_sol_t"] < 1e-3 and R["err_sol_m"] < 1e-3
    assert R["disp_areas"] < 1e-6
    assert abs(R["vp_va"] - R["ra_rp"]) < 1e-12
    assert R["cierre_m"] < 1e3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
