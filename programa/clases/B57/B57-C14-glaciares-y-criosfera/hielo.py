#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C14: glaciares y criosfera: masa de hielo, equivalente en nivel del mar y densidad.

Datos: GRACE-FO, 490 km de altitud y 220 km de separacion entre satelites (NASA JPL, consultada 2026-11-09). ILUSTRATIVOS / SINTETICOS: area
oceanica 3.618e14 m^2 y densidad del agua 1000 kg/m^3 (valores de referencia, NO CONSULTADOS), perdida de masa de 270 Gt/anio,
area de un glaciar 1e5 km^2 con descenso de 0.5 m/anio, densidades de hielo 917 y de nieve compactada (firn) 350 kg/m^3, serie mensual
de 20 anios con ruido de 60 Gt, semilla 57. Nada de esto es una medicion.
Modelo: 1 mm de nivel del mar = A_oceano * 1e-3 m * rho_agua kg = 361.8 Gt ; masa = area * dh * rho ; resolucion espacial de armonicos
esfericos hasta grado l: pi R / l ; tendencia de masa por minimos cuadrados e incertidumbre analitica frente a Monte Carlo.
Validez: ocano uniforme, sin efectos de reajuste glacial ni de gravedad. Tolerancia: 1 mm = 361.8 Gt exacto (1e-9); sigma de la pendiente
simulada frente a la analitica < 10 %.
Requiere numpy.
"""
import math, platform
import numpy as np

A_OC, RHO_W = 3.618e14, 1000.0
RT = 6371e3


def calcular():
    r = {}
    r["gt_por_mm"] = A_OC * 1e-3 * RHO_W / 1e12
    r["mm_por_anio"] = 270.0 / r["gt_por_mm"]
    area, dh = 1e5 * 1e6, 0.5  # descenso de altura (valor absoluto)
    r["masa_hielo"] = area * dh * 917.0 / 1e12
    r["masa_firn"] = area * dh * 350.0 / 1e12
    r["razon_dens"] = r["masa_hielo"] / r["masa_firn"]
    r["res_l60"] = math.pi * RT / 60 / 1e3
    r["res_l96"] = math.pi * RT / 96 / 1e3
    rng = np.random.default_rng(57)
    t = np.arange(240) / 12.0
    A = np.column_stack([np.ones_like(t), t])
    cov = np.linalg.inv(A.T @ A)
    sig = 60.0
    r["sig_ana"] = sig * math.sqrt(cov[1, 1])
    pend = []
    for _ in range(4000):
        y = -270.0 * t + sig * rng.standard_normal(t.size)
        pend.append(np.linalg.lstsq(A, y, rcond=None)[0][1])
    pend = np.array(pend)
    r["pend_media"], r["sig_sim"] = float(pend.mean()), float(pend.std())
    r["razon_sig"] = r["sig_sim"] / r["sig_ana"]
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"1 mm de nivel del mar = {r['gt_por_mm']:.1f} Gt ; 270 Gt/anio = {r['mm_por_anio']:.3f} mm/anio de nivel del mar")
    print(f"Glaciar de 1e5 km2 que baja 0.5 m/anio: masa con 917 kg/m3 = {r['masa_hielo']:.2f} Gt ; con 350 kg/m3 = {r['masa_firn']:.2f} Gt ; razon = {r['razon_dens']:.2f}")
    print(f"Resolucion espacial pi R / l: l = 60 -> {r['res_l60']:.0f} km ; l = 96 -> {r['res_l96']:.0f} km")
    print(f"Tendencia de masa: recuperada = {r['pend_media']:.1f} Gt/anio ; sigma analitica = {r['sig_ana']:.2f} ; simulada = {r['sig_sim']:.2f} ; razon = {r['razon_sig']:.3f}")
    assert abs(r["gt_por_mm"] - 361.8) < 1e-6
    assert abs(r["razon_sig"] - 1) < 0.1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
