#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C08: geometria y dinamica de las orbitas elipticas.

Datos consultados (2026-11-10): ficha de Marte (NASA/NSSDC): a = 227.956e6 km, e = 0.0935, perihelio 206.650e6 km, afelio 249.261e6 km,
periodo sidereo 686.980 d; (GM)sol = 1.3271244e20 m3/s2 y (GM)Tierra = 3.986004e14 m3/s2, R ecuatorial = 6.3781e6 m (IAU 2015 B3).
ORBITA SINTETICA adicional: tipo Molniya, periapsis a 500 km y apoapsis a 39700 km de altitud (valores ilustrativos), alrededor de la Tierra.
Sistema: marco inercial del cuerpo central, SI. Dos cuerpos puntuales.
Segunda via: la suma de distancias a los dos focos se evalua en 360 puntos (debe ser 2a) y r(nu) = p/(1 + e cos nu) se compara con la
ecuacion de la elipse en coordenadas cartesianas con el foco en el origen (x - c)^2/a^2 + y^2/b^2 = 1, c = a e.
Tolerancias: suma de distancias dentro de 1e-9 relativa; ficha de Marte frente a a(1 -/+ e) dentro de 1e-3 (redondeo de la ficha).
"""
from __future__ import annotations
import math, platform

MU_S, MU_T, RE = 1.3271244e20, 3.986004e14, 6.3781e6


def geometria(a, e):
    return dict(rp=a * (1 - e), ra=a * (1 + e), b=a * math.sqrt(1 - e * e), p=a * (1 - e * e), c=a * e)


def suma_focos(a, e, n=360):
    g = geometria(a, e)
    peor = 0.0
    for k in range(n):
        nu = 2 * math.pi * k / n
        r = g["p"] / (1 + e * math.cos(nu))
        x, y = r * math.cos(nu), r * math.sin(nu)  # foco 1 en el origen
        d2 = math.hypot(x + 2 * g["c"], y)  # el periapsis esta en +x; el foco vacio en -2c
        peor = max(peor, abs(r + d2 - 2 * a) / (2 * a))
    return peor


def cartesiana(a, e, n=360):
    g = geometria(a, e)
    peor = 0.0
    for k in range(n):
        nu = 2 * math.pi * k / n
        r = g["p"] / (1 + e * math.cos(nu))
        x, y = r * math.cos(nu), r * math.sin(nu)
        xc = x + g["c"]  # centro de la elipse en (-c, 0)
        peor = max(peor, abs(xc * xc / a ** 2 + y * y / g["b"] ** 2 - 1))
    return peor


def calcular():
    R = {}
    a_m, e_m = 227.956e9, 0.0935
    g = geometria(a_m, e_m)
    R["rp_marte"], R["ra_marte"] = g["rp"], g["ra"]
    R["dif_rp"] = abs(g["rp"] - 206.650e9) / 206.650e9
    R["dif_ra"] = abs(g["ra"] - 249.261e9) / 249.261e9
    R["b_marte"] = g["b"]
    R["p_marte"] = g["p"]
    R["vp_marte"] = math.sqrt(MU_S * (2 / g["rp"] - 1 / a_m))
    R["va_marte"] = math.sqrt(MU_S * (2 / g["ra"] - 1 / a_m))
    R["area_marte"] = math.pi * a_m * g["b"]
    R["T_marte_d"] = 2 * math.pi * math.sqrt(a_m ** 3 / MU_S) / 86400.0
    R["suma_focos"] = suma_focos(a_m, e_m)
    R["cartesiana"] = cartesiana(a_m, e_m)
    # Molniya-like SINTETICA
    rp, ra = RE + 500e3, RE + 39700e3
    a = 0.5 * (rp + ra)
    e = (ra - rp) / (ra + rp)
    gm = geometria(a, e)
    R["a_mol"], R["e_mol"], R["b_mol"], R["p_mol"] = a, e, gm["b"], gm["p"]
    R["vp_mol"] = math.sqrt(MU_T * (2 / rp - 1 / a))
    R["va_mol"] = math.sqrt(MU_T * (2 / ra - 1 / a))
    R["T_mol_h"] = 2 * math.pi * math.sqrt(a ** 3 / MU_T) / 3600.0
    R["razon_v"] = R["vp_mol"] / R["va_mol"]
    R["razon_r"] = ra / rp
    R["suma_mol"] = suma_focos(a, e)
    R["cart_mol"] = cartesiana(a, e)
    # distancia media en el tiempo: a (1 + e^2/2); media en angulo: b
    R["r_media_tiempo"] = a * (1 + e * e / 2)
    R["r_media_angulo"] = gm["b"]
    # radio en nu = 90
    R["r90"] = gm["p"]
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print("Marte alrededor del Sol (a, e de la ficha NASA/NSSDC):")
    print(f"  perihelio = {R['rp_marte'] / 1e9:.3f}e6 km (ficha 206.650) dif {R['dif_rp']:.1e} ; afelio = {R['ra_marte'] / 1e9:.3f}e6 km (ficha 249.261) dif {R['dif_ra']:.1e}")
    print(f"  b = {R['b_marte'] / 1e9:.3f}e6 km ; p = {R['p_marte'] / 1e9:.3f}e6 km ; area = {R['area_marte']:.5e} m2 ; T = {R['T_marte_d']:.3f} d (ficha 686.980)")
    print(f"  v_peri = {R['vp_marte'] / 1e3:.4f} km/s ; v_afelio = {R['va_marte'] / 1e3:.4f} km/s")
    print(f"  suma de distancias a los focos: error relativo maximo {R['suma_focos']:.1e} ; ecuacion cartesiana: {R['cartesiana']:.1e}")
    print("Orbita tipo Molniya SINTETICA (500 x 39700 km de altitud) alrededor de la Tierra:")
    print(f"  a = {R['a_mol'] / 1e3:.3f} km ; e = {R['e_mol']:.5f} ; b = {R['b_mol'] / 1e3:.3f} km ; p = {R['p_mol'] / 1e3:.3f} km")
    print(f"  v_peri = {R['vp_mol']:.3f} m/s ; v_apo = {R['va_mol']:.3f} m/s ; razon = {R['razon_v']:.5f} = r_a/r_p = {R['razon_r']:.5f}")
    print(f"  T = {R['T_mol_h']:.4f} h")
    print(f"  suma de distancias: {R['suma_mol']:.1e} ; ecuacion cartesiana: {R['cart_mol']:.1e}")
    print(f"  distancia media en el tiempo a(1+e^2/2) = {R['r_media_tiempo'] / 1e3:.3f} km ; en el angulo (b) = {R['r_media_angulo'] / 1e3:.3f} km ; r(nu=90) = p = {R['r90'] / 1e3:.3f} km")
    assert R["dif_rp"] < 1e-3 and R["dif_ra"] < 1e-3
    assert R["suma_focos"] < 1e-9 and R["suma_mol"] < 1e-9
    assert R["cartesiana"] < 1e-9 and R["cart_mol"] < 1e-9
    assert abs(R["razon_v"] - R["razon_r"]) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
