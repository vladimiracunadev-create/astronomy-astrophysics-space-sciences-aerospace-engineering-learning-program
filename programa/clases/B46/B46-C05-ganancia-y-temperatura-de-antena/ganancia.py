#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C05: area efectiva, sensibilidad en K/Jy y dilucion del haz.

Datos: k y c de NIST CODATA 2022 (consultada 2026-11-09). Diametro 25 m, eficiencia 0,6, frecuencia 1,4 GHz, fuente gaussiana de
15 arcmin y T_B = 50 K son ILUSTRATIVOS. 1 Jy = 1e-26 W m^-2 Hz^-1 (definicion).
Modelo: Gamma = A_e/(2 k) en K/Jy; T_A = S Gamma para una fuente puntual; T_A = (1/Omega_A) integral T_B P dOmega por integracion numerica
2D de una fuente y un haz gaussianos, frente a la dilucion analitica T_B theta_s^2/(theta_s^2 + theta_b^2).
Supuestos: haz gaussiano, plano del cielo, fuente centrada. Validez: orientativa.
Tolerancia: integral numerica dentro del 0,1 % de la analitica.
"""
from __future__ import annotations
import math, platform
K, C = 1.380649e-23, 299792458.0

def calc():
    D, eta, nu = 25.0, 0.6, 1.4e9
    lam = C / nu
    Ae = eta * math.pi * D ** 2 / 4
    gam = Ae / (2 * K) * 1e-26
    omega_geo = lam ** 2 / (math.pi * D ** 2 / 4)
    theta_b = math.radians(30.3 / 60)   # FWHM del haz (ilustrativo, de C03)
    ts = math.radians(15 / 60)
    sb, ss = theta_b / 2.3548200450309493, ts / 2.3548200450309493
    Tb = 50.0
    # integral 2D en coordenadas cartesianas (rad)
    L, n = 6 * max(sb, ss), 400
    h = 2 * L / n
    num = den = 0.0
    for i in range(n):
        x = -L + (i + 0.5) * h
        for j in range(n):
            y = -L + (j + 0.5) * h
            r2 = x * x + y * y
            p = math.exp(-r2 / (2 * sb * sb))
            num += Tb * math.exp(-r2 / (2 * ss * ss)) * p
            den += p
    ta_num = num / den
    ta_ana = Tb * ss ** 2 / (ss ** 2 + sb ** 2)
    S = 2 * K * Tb * (2 * math.pi * ss ** 2) / lam ** 2 / 1e-26   # Jy, via Rayleigh-Jeans
    om_g = 2 * math.pi * sb ** 2
    ta_pt = Tb * (2 * math.pi * ss ** 2) / om_g
    return dict(Ae=Ae, gam=gam, omega_geo=omega_geo, om_g=om_g, ta_num=ta_num, ta_ana=ta_ana, S=S, ta_pt=ta_pt, eta=eta, lam=lam,
                Sjy_1K=1 / gam, ss_arcmin=math.degrees(ss) * 60)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"A_e = {r['Ae']:.2f} m^2 ; Gamma = {r['gam']:.4f} K/Jy ; 1 K equivale a {r['Sjy_1K']:.2f} Jy")
    print(f"flujo de la fuente de 15 arcmin con 50 K = {r['S']:.2f} Jy")
    print(f"T_A numerica = {r['ta_num']:.4f} K ; analitica (dilucion) = {r['ta_ana']:.4f} K ; aproximacion de fuente puntual = {r['ta_pt']:.4f} K")
    print(f"Omega_A = lambda^2/A_geom = {r['omega_geo']*1e5:.3f}e-5 sr ; Omega gaussiano del haz = {r['om_g']*1e5:.3f}e-5 sr")
    assert abs(r["ta_num"] / r["ta_ana"] - 1) < 1e-3
    assert abs(r["gam"] / (r["Ae"] / (2 * K) * 1e-26) - 1) < 1e-12
    assert r["ta_pt"] > r["ta_ana"]
    assert abs(r["omega_geo"] / r["om_g"] - 1) < 0.1
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
