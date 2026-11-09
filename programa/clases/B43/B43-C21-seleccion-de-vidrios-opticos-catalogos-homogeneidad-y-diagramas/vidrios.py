#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C21: seleccion de vidrios opticos: Sellmeier, numero de Abbe, doblete acromatico y homogeneidad.

Datos: coeficientes de Sellmeier de N-BK7 y F2 (SCHOTT) tal como los reproduce la base de datos refractiveindex.info (archivos database/data/specs/schott/optical/N-BK7.yml y F2.yml, catalogo SCHOTT Zemax 2017-01-20b, CC0),
leidos el 2026-11-09 por una pagina web de GitHub: N-BK7 B = (1,03961212; 0,231792344; 1,01046945), C = (0,00600069867; 0,0200179144; 103,560653) um^2, n_d = 1,5168, V_d = 64,17; F2 B = (1,34533359; 0,209073176; 0,937357162),
C = (0,00997743871; 0,0470450767; 111,886764) um^2, n_d = 1,62004, V_d = 36,37; dilatacion de N-BK7 7,1e-6/K (243-343 K). Longitudes de onda de las lineas d, F y C: 587,5618, 486,1327 y 656,2725 nm (valores de uso general, no consultados aqui).
ILUSTRATIVOS: el doblete de 1000 mm y la no homogeneidad de 2e-6 en 30 mm.
Modelo: n^2 - 1 = sum B_i l^2/(l^2 - C_i); V_d = (n_d - 1)/(n_F - n_C); doblete acromatico con phi_1/V_1 + phi_2/V_2 = 0 y phi_1 + phi_2 = 1/f; OPD = delta n x t.
Verificacion independiente: n_d y V_d calculados frente a los valores tabulados del archivo; la acromatizacion se comprueba evaluando la potencia del doblete en F y C con las formas (n-1) K_i.
Supuestos: lente delgada, temperatura de 293 K, sin absorcion. Validez: dentro del intervalo de Sellmeier 0,32-2,5 um.
Tolerancia: n_d a 1e-4 de la tabla, V_d a 0,02; acromatizacion 1e-12 relativo.
"""
from __future__ import annotations
import math, platform

BK7 = ((1.03961212, 0.231792344, 1.01046945), (0.00600069867, 0.0200179144, 103.560653))
F2 = ((1.34533359, 0.209073176, 0.937357162), (0.00997743871, 0.0470450767, 111.886764))
LD, LF, LC = 0.5875618, 0.4861327, 0.6562725

def n(g, lam_um):
    l2 = lam_um ** 2
    return math.sqrt(1 + sum(b * l2 / (l2 - c) for b, c in zip(*g)))

def abbe(g):
    return (n(g, LD) - 1) / (n(g, LF) - n(g, LC))

def calc():
    r = {}
    r["nd_BK7"] = n(BK7, LD); r["Vd_BK7"] = abbe(BK7); r["nd_F2"] = n(F2, LD); r["Vd_F2"] = abbe(F2)
    r["n_550_BK7"] = n(BK7, 0.55); r["n_550_F2"] = n(F2, 0.55)
    V1, V2 = r["Vd_BK7"], r["Vd_F2"]
    f = 1000.0
    p1 = (1 / f) * V1 / (V1 - V2); p2 = -(1 / f) * V2 / (V1 - V2)
    r["f1_mm"] = 1 / p1; r["f2_mm"] = 1 / p2
    K1 = p1 / (r["nd_BK7"] - 1); K2 = p2 / (r["nd_F2"] - 1)
    pot = lambda lam: (n(BK7, lam) - 1) * K1 + (n(F2, lam) - 1) * K2
    r["f_d_mm"] = 1 / pot(LD); r["f_F_mm"] = 1 / pot(LF); r["f_C_mm"] = 1 / pot(LC)
    r["f_436_mm"] = 1 / pot(0.4358343)
    r["delta_F_C_doblete_mm"] = r["f_F_mm"] - r["f_C_mm"]
    # lente sencilla de BK7
    K = (1 / f) / (r["nd_BK7"] - 1)
    r["delta_F_C_simple_mm"] = 1 / ((n(BK7, LF) - 1) * K) - 1 / ((n(BK7, LC) - 1) * K)
    r["f_sobre_Vd_mm"] = f / V1
    # homogeneidad
    r["OPD_nm"] = 2e-6 * 30.0 * 1e6
    r["residual_acromatico"] = abs(p1 / V1 + p2 / V2) / abs(p1 / V1)
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        print(f"{k} = {v:.8g}")
    assert abs(r["nd_BK7"] - 1.5168) < 1e-4 and abs(r["nd_F2"] - 1.62004) < 1e-4
    assert abs(r["Vd_BK7"] - 64.17) < 0.02 and abs(r["Vd_F2"] - 36.37) < 0.02
    assert abs(r["delta_F_C_doblete_mm"]) < 0.02 * abs(r["delta_F_C_simple_mm"])
    assert r["residual_acromatico"] < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
