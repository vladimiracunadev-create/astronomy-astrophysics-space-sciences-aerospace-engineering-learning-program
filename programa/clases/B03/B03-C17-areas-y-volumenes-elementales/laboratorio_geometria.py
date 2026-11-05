#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B03-C17: áreas y volúmenes de esferas y elipsoides con datos de la NASA y la IAU.

Datos PUBLICADOS: radio medio volumétrico del Sol 695 700 km, masa 1,9884e30 kg, volumen
1,412e18 km3 y densidad 1408 kg/m3 (NASA Sun Fact Sheet, 9-may-2024); radios nominales
terrestres ecuatorial 6,3781e6 m y polar 6,3568e6 m (IAU 2015 B3), volumen terrestre 1,08321e12
km3 y radio medio 6371 km (NASA Earth Fact Sheet); radio medio de la Luna 1737,4 km (NASA Moon);
irradiancia nominal 1361 W/m2 (IAU). Modelo: esfera V = 4/3 pi r^3, A = 4 pi r^2; elipsoide de
revolución achatado V = 4/3 pi a^2 c. Supuestos: cuerpos lisos y homogéneos en forma. Validez:
orden de 0,2 % para el Sol y 1e-5 para la Tierra. Tolerancias: 0,2 % (Sol), 1e-4 (Tierra).
"""
from __future__ import annotations

import math
import platform

R_SOL_KM = 695_700.0
M_SOL = 1.9884e30
V_SOL_NASA_KM3 = 1.412e18
RHO_SOL_NASA = 1408.0
RE_M, RP_M = 6.3781e6, 6.3568e6
V_TIERRA_NASA_KM3 = 1.08321e12
R_TIERRA_KM, R_LUNA_KM = 6371.0, 1737.4
S_NOMINAL = 1361.0


def v_esfera(r: float) -> float:
    return 4.0 / 3.0 * math.pi * r ** 3


def a_esfera(r: float) -> float:
    return 4.0 * math.pi * r ** 2


def v_elipsoide_achatado(a: float, c: float) -> float:
    return 4.0 / 3.0 * math.pi * a * a * c


def pruebas() -> None:
    assert abs(v_esfera(1.0) - 4.18879020) < 1e-7 and abs(a_esfera(1.0) - 4 * math.pi) < 1e-12
    assert abs(v_esfera(2.0) / v_esfera(1.0) - 8) < 1e-12           # doble radio -> 8 veces el volumen
    assert abs(a_esfera(2.0) / a_esfera(1.0) - 4) < 1e-12           # doble radio -> 4 veces el área
    assert abs(v_elipsoide_achatado(5.0, 5.0) - v_esfera(5.0)) < 1e-9
    v_sol = v_esfera(R_SOL_KM)
    assert abs(v_sol - V_SOL_NASA_KM3) / V_SOL_NASA_KM3 < 0.002, v_sol
    rho = M_SOL / (v_sol * 1e9)
    assert abs(rho - RHO_SOL_NASA) / RHO_SOL_NASA < 0.002, rho
    v_t = v_elipsoide_achatado(RE_M, RP_M) / 1e9                     # m3 -> km3
    assert abs(v_t - V_TIERRA_NASA_KM3) / V_TIERRA_NASA_KM3 < 1e-4, v_t


def main() -> int:
    pruebas()
    print(f"python {platform.python_version()} | pruebas OK")
    v_sol = v_esfera(R_SOL_KM)
    print(f"V_Sol = {v_sol:.4e} km3 (NASA 1,412e18; dif. {abs(v_sol - V_SOL_NASA_KM3) / V_SOL_NASA_KM3 * 100:.2f} %)")
    print(f"Densidad media del Sol = {M_SOL / (v_sol * 1e9):.0f} kg/m3 (NASA 1408)")
    v_t = v_elipsoide_achatado(RE_M, RP_M) / 1e9
    print(f"V_Tierra (elipsoide nominal) = {v_t:.5e} km3 (NASA 1,08321e12)")
    print(f"Tierras que caben en el Sol: {v_sol / v_esfera(R_TIERRA_KM):.3e}; en la Tierra caben {v_esfera(R_TIERRA_KM) / v_esfera(R_LUNA_KM):.1f} Lunas")
    p = S_NOMINAL * math.pi * (R_TIERRA_KM * 1e3) ** 2
    print(f"Potencia interceptada por la Tierra: {p:.4e} W (S x pi R^2)")
    print(f"Área de la sección solar / terrestre: {(R_SOL_KM / R_TIERRA_KM) ** 2:.0f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
