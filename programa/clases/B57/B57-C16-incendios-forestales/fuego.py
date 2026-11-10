#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C16: deteccion de incendios con dos bandas termicas (3.9 um y 11 um).

Datos: pixeles de 375 m (VIIRS) y 1 km (MODIS) de FIRMS (NASA, consultada 2026-11-09). ILUSTRATIVOS / SINTETICOS: fondo 300 K, fuego 800 K,
fraccion de pixel en llamas 1e-3, sensibilidad termica (NEdT) del canal de 3.9 um de 0.5 K a 300 K y umbral de deteccion de 3 NEdT. Constantes h, c,
k_B del SI. No se simula ningun incendio real ni se usan productos de FIRMS.
Modelo: radiancia mixta L = p B(T_f) + (1 - p) B(T_b) con B de Planck; dos incognitas (p, T_f) resueltas con los canales de 3.9 y 11 um por
biseccion sobre T_f; fraccion minima detectable p_min = 3 NEdL / (B(T_f) - B(T_b)).
Validez: fondo y fuego uniformes dentro de cada parte del pixel, sin atmosfera ni reflexion solar. Tolerancia: ida y vuelta (p, T_f) < 1e-6 relativa.
"""
import math, platform

H, C, KB = 6.62607015e-34, 299792458.0, 1.380649e-23
L3, L11 = 3.9e-6, 11e-6


def B(lam, T):
    x = H * C / (lam * KB * T)
    return 2 * H * C**2 / lam**5 / math.expm1(x)


def mezcla(lam, p, Tf, Tb):
    return p * B(lam, Tf) + (1 - p) * B(lam, Tb)


def resolver(m3, m11, Tb):
    b3, b11 = B(L3, Tb), B(L11, Tb)

    def resid(Tf):
        p = (m3 - b3) / (B(L3, Tf) - b3)
        return m11 - (p * B(L11, Tf) + (1 - p) * b11), p

    lo, hi = 450.0, 1800.0
    flo = resid(lo)[0]
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        fm = resid(mid)[0]
        if (fm > 0) == (flo > 0):
            lo, flo = mid, fm
        else:
            hi = mid
    Tf = 0.5 * (lo + hi)
    return resid(Tf)[1], Tf


def calcular():
    r = {}
    p, Tf, Tb = 1e-3, 800.0, 300.0
    m3, m11 = mezcla(L3, p, Tf, Tb), mezcla(L11, p, Tf, Tb)
    r["L3_fondo"], r["L3_mezcla"] = B(L3, Tb), m3
    r["L11_fondo"], r["L11_mezcla"] = B(L11, Tb), m11
    r["sube_3"] = m3 / B(L3, Tb)
    r["sube_11"] = m11 / B(L11, Tb)
    pr, Tfr = resolver(m3, m11, Tb)
    r["p_rec"], r["Tf_rec"] = pr, Tfr
    r["err_p"], r["err_T"] = abs(pr / p - 1), abs(Tfr / Tf - 1)
    # sensibilidad a un error de 2 K en el fondo
    pe, Te = resolver(m3, m11, Tb + 2.0)
    r["p_con_error"], r["T_con_error"] = pe, Te
    dB = B(L3, Tb + 0.25) - B(L3, Tb - 0.25)  # NEdL ~ dB/dT * 0.5 K
    r["NEdL"] = dB
    r["p_min"] = 3 * dB / (B(L3, Tf) - B(L3, Tb))
    r["area_min_375"] = r["p_min"] * 375.0**2
    r["area_min_1000"] = r["p_min"] * 1000.0**2
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Radiancia de fondo: 3.9 um = {r['L3_fondo']:.4e} ; 11 um = {r['L11_fondo']:.4e} W m^-2 sr^-1 m^-1")
    print(f"Pixel mixto (p = 1e-3, 800 K): 3.9 um sube x{r['sube_3']:.2f} ; 11 um sube x{r['sube_11']:.3f}")
    print(f"Ida y vuelta: p = {r['p_rec']:.6e} (error {r['err_p']:.1e}) ; T_f = {r['Tf_rec']:.4f} K (error {r['err_T']:.1e})")
    print(f"Con 2 K de error en el fondo: p = {r['p_con_error']:.3e} ; T_f = {r['T_con_error']:.1f} K")
    print(f"Fraccion minima detectable = {r['p_min']:.2e} ; area minima: pixel de 375 m = {r['area_min_375']:.1f} m2 ; pixel de 1 km = {r['area_min_1000']:.0f} m2")
    assert r["err_p"] < 1e-6 and r["err_T"] < 1e-6
    assert r["sube_3"] > 1.5 * r["sube_11"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
