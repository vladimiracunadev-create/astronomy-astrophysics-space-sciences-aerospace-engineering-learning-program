#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C32: sitios de calibracion terrestres: calibracion vicaria, presupuesto de incertidumbre y deriva.

Datos: SINTETICOS / ILUSTRATIVOS. Sitio desertico hipotetico de reflectancia 0.35 (incertidumbre 2 %), irradiancia solar de la banda 1550 W m^-2 um^-1 (valor ilustrativo,
no consultado), cenital solar 30 grados, transmitancia atmosferica 0.85 (incertidumbre 3 %), ancho de banda 0.06 um, ganancia verdadera del sensor 0.040 W m^-2 sr^-1 um^-1 por
cuenta y desfase 2.0, ruido de 0.8 cuentas (DN) por observacion, 40 pasadas sobre el sitio, deriva de la ganancia de -0.30 % por anio durante 10 anios; semilla fija 57.
Modelo: radiancia esperada L = rho E cos(theta) T / pi ; cuentas DN = (L - desfase_L)/ganancia ; regresion de L esperada contra DN para estimar ganancia y desfase ;
incertidumbre combinada u = sqrt(u_rho^2 + u_T^2) (suma cuadratica de componentes independientes) ; deriva por regresion lineal de la ganancia estimada por anio.
Validez: sitio estable y lambertiano, errores independientes. Tolerancia: ganancia recuperada dentro de 1 %; incertidumbre combinada simulada frente a la analitica < 5 %.
Requiere numpy.
"""
import math, platform
import numpy as np

E, COS, T0 = 1550.0, math.cos(math.radians(30.0)), 0.85
U_RHO, U_T = 0.02, 0.03
G_VERD, OFF_VERD = 0.040, 2.0 * 0.040
SIG_DN = 0.8


def radiancia(rho, T=T0):
    return rho * E * COS * T / math.pi


def calcular():
    r = {}
    rng = np.random.default_rng(57)
    rho = 0.35
    L0 = radiancia(rho)
    r["L0"] = L0
    r["desfase_verd"] = OFF_VERD
    r["u_comb_ana"] = math.sqrt(U_RHO**2 + U_T**2)
    # incertidumbre combinada de L por Monte Carlo
    rr = rho * (1 + U_RHO * rng.standard_normal(200000))
    tt = T0 * (1 + U_T * rng.standard_normal(200000))
    Ls = radiancia(rr, tt)
    r["u_comb_sim"] = float(Ls.std() / Ls.mean())
    r["razon_u"] = r["u_comb_sim"] / r["u_comb_ana"]
    # calibracion con 40 pasadas con reflectancia efectiva variable (varias fechas, nubes finas, cambios de geometria)
    cos_var = np.cos(np.radians(rng.uniform(15, 55, 40)))
    Lp = rho * E * cos_var * T0 / math.pi
    dn = (Lp - OFF_VERD) / G_VERD + SIG_DN * rng.standard_normal(40)
    A = np.column_stack([dn, np.ones(40)])
    g, off = np.linalg.lstsq(A, Lp, rcond=None)[0]
    r["ganancia"], r["desfase"] = float(g), float(off)
    r["err_g_pct"] = (g / G_VERD - 1) * 100
    # deriva: ganancia estimada cada anio (10 anios) con 40 pasadas por anio
    anios = np.arange(10)
    gs = []
    for y in anios:
        gv = G_VERD * (1 - 0.003 * y)
        cv = np.cos(np.radians(rng.uniform(15, 55, 40)))
        Lq = rho * E * cv * T0 / math.pi
        dnq = (Lq - OFF_VERD) / gv + SIG_DN * rng.standard_normal(40)
        gs.append(np.linalg.lstsq(np.column_stack([dnq, np.ones(40)]), Lq, rcond=None)[0][0])
    gs = np.array(gs)
    pend = np.polyfit(anios, gs / gs[0], 1)[0]
    r["deriva_pct_anio"] = float(pend * 100)
    # la incertidumbre del sitio (u_comb) enmascara la deriva si no se mantiene constante
    r["deriva_verdadera"] = -0.30
    r["u_g_ana_pct"] = SIG_DN / (math.sqrt(40) * np.std((rho * E * cos_var * T0 / math.pi - OFF_VERD) / G_VERD)) * 100
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"Radiancia esperada del sitio (rho = 0.35) = {r['L0']:.3f} W m^-2 sr^-1 um^-1")
    print(f"Incertidumbre combinada de la radiancia esperada: analitica = {r['u_comb_ana']*100:.3f} % ; Monte Carlo = {r['u_comb_sim']*100:.3f} % ; razon = {r['razon_u']:.3f}")
    print(f"Calibracion con 40 pasadas: ganancia = {r['ganancia']:.5f} (verdadera 0.04000) ; error = {r['err_g_pct']:+.3f} % ; desfase = {r['desfase']:.4f} (verdadero {OFF_VERD:.4f})")
    print(f"Deriva estimada de la ganancia = {r['deriva_pct_anio']:+.3f} %/anio (verdadera {r['deriva_verdadera']:+.2f} %/anio)")
    assert abs(r["err_g_pct"]) < 1.0
    assert abs(r["razon_u"] - 1) < 0.05
    assert abs(r["deriva_pct_anio"] - r["deriva_verdadera"]) < 0.15
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
