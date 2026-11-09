#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B45-C06: diseno de un espectrografo de rendija con tres vias para la resolucion.

Datos: todos los parametros son ILUSTRATIVOS, no de un instrumento real: telescopio de 4 m a f/10, rendija de 1,0 segundo de arco, colimador de 500 mm, camara de 250 mm,
red de 600 l/mm usada a alpha = 10 grados en orden 1, pixeles de 15 micras y 2048 pixeles. 1 segundo de arco = pi/648000 rad.
Modelo: (1) formula R = (sin a + sin b) f_col / (w cos a); (2) dispersion lineal d cos b/(m f_cam) por tamano de imagen de la rendija; (3) trazado de rayos con diferencia finita de beta y x = f_cam tan(delta beta).
Supuestos: sistema paraxial ideal, sin aberraciones ni ensanchamiento por seeing distinto del ancho de rendija. Validez: orden de magnitud del diseno.
Tolerancia: las tres vias de R coinciden a 1e-3 relativo; muestreo reportado en pixeles por elemento de resolucion.
"""
from __future__ import annotations
import math, platform, sys

ARCSEC = math.pi / 648000
D_TEL = 4.0
F_TEL = 40.0
SLIT_ARCSEC = 1.0
F_COL = 0.500
F_CAM = 0.250
LINEAS_MM = 600
D = 1e-3 / LINEAS_MM
ALPHA = math.radians(10.0)
M = 1
PIX = 15e-6
NPIX = 2048
LAM0 = 550e-9


def beta(lam):
    return math.asin(M * lam / D - math.sin(ALPHA))


def calcular():
    r = {}
    w = F_TEL * SLIT_ARCSEC * ARCSEC
    r["w_um"] = w * 1e6
    r["d_col_mm"] = F_COL / (F_TEL / D_TEL) * 1e3
    b0 = beta(LAM0)
    r["beta0"] = math.degrees(b0)
    r["anam"] = math.cos(ALPHA) / math.cos(b0)
    r["R_formula"] = (math.sin(ALPHA) + math.sin(b0)) * F_COL / (w * math.cos(ALPHA))
    # via 2: dispersion lineal e imagen de la rendija
    disp = D * math.cos(b0) / (M * F_CAM)                      # m de lambda por m en el detector
    wp = w * r["anam"] * F_CAM / F_COL
    r["wp_um"] = wp * 1e6
    r["disp_nm_pix"] = disp * PIX * 1e9
    dlam2 = wp * disp
    r["R_disp"] = LAM0 / dlam2
    # via 3: trazado de rayos con diferencia finita
    dl = 1e-12
    db = beta(LAM0 + dl) - beta(LAM0)
    x_por_lam = F_CAM * math.tan(db) / dl                       # m en detector por m de lambda
    r["R_traza"] = LAM0 / (wp / x_por_lam)
    r["pix_por_res"] = wp / PIX
    r["cobertura_nm"] = NPIX * PIX / x_por_lam * 1e9
    r["dlam_nm"] = LAM0 / r["R_formula"] * 1e9
    r["dv_km_s"] = 299792.458 / r["R_formula"]
    # ensanchar la rendija a 2" dobla el elemento y reduce R a la mitad
    r["R_2arcsec"] = r["R_formula"] / 2
    # rendija para muestreo Nyquist (2 pixeles)
    w_nyq = 2 * PIX / (r["anam"] * F_CAM / F_COL)
    r["slit_nyq_arcsec"] = w_nyq / F_TEL / ARCSEC
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"rendija fisica w = {r['w_um']:.1f} um ; haz colimado = {r['d_col_mm']:.1f} mm ; beta(550 nm) = {r['beta0']:.3f} grados ; factor anamorfico = {r['anam']:.4f}")
    print(f"imagen de la rendija w' = {r['wp_um']:.2f} um = {r['pix_por_res']:.2f} pixeles ; dispersion = {r['disp_nm_pix']:.4f} nm/pixel ; cobertura = {r['cobertura_nm']:.1f} nm")
    print(f"R por formula = {r['R_formula']:.2f} ; por dispersion lineal = {r['R_disp']:.2f} ; por trazado de rayos = {r['R_traza']:.2f}")
    print(f"delta lambda = {r['dlam_nm']:.4f} nm ; delta v = {r['dv_km_s']:.1f} km/s ; con rendija de 2 segundos R = {r['R_2arcsec']:.1f}")
    print(f"rendija para muestreo de 2 pixeles = {r['slit_nyq_arcsec']:.3f} segundos de arco")
    assert abs(r["R_disp"] / r["R_formula"] - 1) < 1e-3
    assert abs(r["R_traza"] / r["R_formula"] - 1) < 1e-3
    assert r["pix_por_res"] > 2
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
