#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C02: ley de gravitacion universal, ensayo de la Luna de Newton y masa de la Tierra.

Datos consultados (2026-11-10): G = 6.67430e-11 m3/(kg s2) con incertidumbre 0.00015e-11 (NIST, CODATA 2022); gn = 9.80665 m/s2 (exacta);
(GM)Tierra = 3.986004e14 m3/s2 y R ecuatorial = 6.3781e6 m (IAU 2015 B3); ficha de la Tierra (NASA/NSSDC): masa 5.9722e24 kg,
radio medio 6371.000 km, g media 9.820 m/s2; ficha de la Luna: a = 0.3844e6 km, T = 27.3217 d.
Sistema: marco inercial geocentrico, SI. Cuerpos puntuales y esfericos homogeneos (Tierra sin rotacion ni achatamiento).
Segunda via: la aceleracion de la Luna se calcula (a) como 4 pi^2 a/T^2 (cinematica) y (b) como GM/a^2 (gravitacion); deben coincidir.
Tolerancias: ley del inverso del cuadrado exacta en la aritmetica (1e-12); a_luna cinematica frente a gravitacional dentro de 2e-2
(la orbita lunar esta perturbada por el Sol y la Tierra y la Luna se mueven en torno al baricentro).
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
G_INC = 0.00015e-11
GN = 9.80665
MU_T = 3.986004e14
RE_ECU = 6.3781e6
RE_MEDIO = 6371.000e3
M_T_FICHA = 5.9722e24
G_FICHA = 9.820
A_LUNA = 0.3844e9
T_LUNA = 27.3217 * 86400.0


def fuerza(g_const, m1, m2, r):
    return g_const * m1 * m2 / r ** 2


def calcular():
    R = {}
    R["g_sup_ecu"] = MU_T / RE_ECU ** 2
    R["g_sup_medio"] = MU_T / RE_MEDIO ** 2
    R["dif_gn"] = (R["g_sup_ecu"] - GN) / GN
    R["dif_ficha"] = (R["g_sup_medio"] - G_FICHA) / G_FICHA
    R["m_tierra"] = MU_T / G
    R["dif_masa"] = (R["m_tierra"] - M_T_FICHA) / M_T_FICHA
    R["inc_masa"] = R["m_tierra"] * G_INC / G
    a_cin = 4 * math.pi ** 2 * A_LUNA / T_LUNA ** 2
    a_grav = MU_T / A_LUNA ** 2
    R["a_luna_cin"] = a_cin
    R["a_luna_grav"] = a_grav
    R["dif_luna"] = abs(a_cin - a_grav) / a_grav
    R["cociente_dist"] = A_LUNA / RE_ECU
    R["g_sobre_a"] = R["g_sup_ecu"] / a_grav
    R["cuadrado"] = R["cociente_dist"] ** 2
    # inverso del cuadrado: duplicar r divide la fuerza por 4
    f1 = fuerza(G, 1.0, M_T_FICHA, RE_ECU)
    f2 = fuerza(G, 1.0, M_T_FICHA, 2 * RE_ECU)
    R["razon_f"] = f1 / f2
    # aceleracion a altitudes
    R["alt_400"] = MU_T / (RE_ECU + 400e3) ** 2
    R["alt_geo"] = MU_T / 42164e3 ** 2
    R["f_1kg_sup"] = f1
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print("g en la superficie terrestre con (GM)T de la IAU (esfera sin rotacion):")
    print(f"  r = 6378.1 km (ecuatorial): g = {R['g_sup_ecu']:.5f} m/s2 ; frente a gn = {R['dif_gn'] * 100:+.3f} %")
    print(f"  r = 6371.000 km (medio)     : g = {R['g_sup_medio']:.5f} m/s2 ; frente a la ficha (9.820) = {R['dif_ficha'] * 100:+.3f} %")
    print(f"Masa de la Tierra = GM/G = {R['m_tierra']:.5e} kg (+/- {R['inc_masa']:.1e} por la incertidumbre de G) ; frente a la ficha {R['dif_masa'] * 100:+.3f} %")
    print("Ensayo de la Luna (a = 384400 km, T = 27.3217 d):")
    print(f"  a cinematica 4 pi^2 a/T^2 = {R['a_luna_cin']:.6e} m/s2")
    print(f"  a gravitacional GM/a^2    = {R['a_luna_grav']:.6e} m/s2 ; diferencia relativa = {R['dif_luna']:.2e}")
    print(f"  g_sup / a_luna = {R['g_sobre_a']:.2f} ; (a_luna/R_T)^2 = {R['cuadrado']:.2f}")
    print(f"Inverso del cuadrado: F(R)/F(2R) = {R['razon_f']:.12f}")
    print(f"Aceleracion a 400 km de altitud: {R['alt_400']:.4f} m/s2 ; a 42164 km del centro: {R['alt_geo']:.4f} m/s2")
    assert abs(R["razon_f"] - 4.0) < 1e-12
    assert abs(R["dif_ficha"]) < 5e-3 and abs(R["dif_masa"]) < 1e-3
    assert R["dif_luna"] < 2e-2
    assert abs(R["g_sobre_a"] / R["cuadrado"] - 1) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
