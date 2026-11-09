#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C19: seguridad y mantenimiento: concentracion de luz solar, equilibrio de una montura y cobertura de polvo.

Datos: del texto de la Resolucion B3 de la UAI de 2015 (arXiv:1510.07674, PDF leido el 2026-11-09): irradiancia solar total nominal S_N = 1361 W/m^2 y radio solar nominal R_N = 6,957e8 m.
au = 149597870700 m (definicion). sigma de Stefan-Boltzmann = 5,670374419e-8 W/m^2/K^4 (NIST CODATA 2022, consultada el 2026-11-09). ILUSTRATIVOS: telescopio D = 200 mm, f/5, reflectancia 0,90, pupila del ojo 7 mm,
contrapeso (4 kg a 0,35 m del eje frente a un tubo de 7 kg con su centro a 0,20 m), polvo de 20 um de diametro con 100 particulas por mm^2. Semilla 20261109.
Modelo: potencia P = S pi (D/2)^2 R; diametro del disco solar en el foco = F x (2 R_N/au); irradiancia en el foco = P/area; temperatura de equilibrio de un absorbente negro que irradia por una cara T = (q/sigma)^(1/4).
Equilibrio: m_c r_c = m_t r_t. Polvo: cobertura f = 1 - exp(-n pi d^2/4) frente a una simulacion en una malla de 200 x 200 pixeles de 10 um.
Supuestos: sin atmosfera, absorbente ideal, polvo opaco y no solapado salvo por azar. Validez: demostrativa del peligro, no es un procedimiento: nunca se debe apuntar un telescopio al Sol sin un filtro solar certificado en la apertura.
Tolerancia: cobertura simulada frente a la formula, 15 % relativo; equilibrio, 1e-12.
"""
from __future__ import annotations
import math, platform, random

SN = 1361.0; RN = 6.957e8; AU = 149597870700.0; SIGMA = 5.670374419e-8
D = 0.200; F = 1.0; REFL = 0.90; PUPILA = 0.007

def calc():
    r = {}
    ang = 2 * RN / AU
    r["diam_solar_mrad"] = ang * 1e3; r["diam_solar_arcmin"] = math.degrees(ang) * 60
    area = math.pi * (D / 2) ** 2
    r["potencia_W"] = SN * area * REFL
    dimg = F * ang
    r["disco_mm"] = dimg * 1e3
    q = r["potencia_W"] / (math.pi * (dimg / 2) ** 2)
    r["irradiancia_foco_kWm2"] = q / 1e3
    r["concentracion"] = q / SN
    r["T_equilibrio_K"] = (q / SIGMA) ** 0.25
    r["razon_ojo"] = (D / PUPILA) ** 2
    r["OD5_transmision"] = 1e-5
    r["potencia_ojo_filtro_mW"] = SN * math.pi * (PUPILA / 2) ** 2 * 1e-5 * 1e3
    r["balance_contrapeso_kg"] = 7.0 * 0.20 / 0.35
    r["desbalance_dado_kgm"] = abs(4.0 * 0.35 - 7.0 * 0.20)
    # polvo
    n = 100.0; dd = 0.020
    f_teo = 1 - math.exp(-n * math.pi * dd ** 2 / 4)
    rng = random.Random(20261109)
    L = 2.0; px = 0.010; M = int(L / px)
    mapa = [[False] * M for _ in range(M)]
    npart = int(n * L * L)
    rad = dd / 2
    for _ in range(npart):
        cx = rng.uniform(0, L); cy = rng.uniform(0, L)
        i0 = int((cx - rad) / px) - 1; i1 = int((cx + rad) / px) + 1
        j0 = int((cy - rad) / px) - 1; j1 = int((cy + rad) / px) + 1
        for i in range(max(0, i0), min(M, i1 + 1)):
            for j in range(max(0, j0), min(M, j1 + 1)):
                if ((i + 0.5) * px - cx) ** 2 + ((j + 0.5) * px - cy) ** 2 <= rad * rad:
                    mapa[i][j] = True
    cub = sum(sum(1 for v in fila if v) for fila in mapa) / (M * M)
    r["cobertura_teorica"] = f_teo; r["cobertura_sim"] = cub; r["particulas"] = npart
    r["perdida_reflectancia"] = REFL * f_teo
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        print(f"{k} = {v:.6g}")
    assert abs(r["diam_solar_arcmin"] - 31.95) < 0.05
    assert abs(r["cobertura_sim"] / r["cobertura_teorica"] - 1) < 0.15
    assert abs(r["balance_contrapeso_kg"] - 4.0) < 1e-12 and r["desbalance_dado_kgm"] < 1e-12
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
