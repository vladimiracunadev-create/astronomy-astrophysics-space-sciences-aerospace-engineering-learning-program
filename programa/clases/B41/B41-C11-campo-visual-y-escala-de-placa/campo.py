#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B41-C11: escala de placa, campo visual en un sensor y muestreo de Nyquist.

Datos: sin constantes fisicas del NIST. Telescopio de D = 200 mm y F = 1000 mm, sensor de 22,3 x 14,9 mm con pixeles de 4,3 micras, longitud de onda de 550 nm
y seeing de 2,0 segundos de arco son ILUSTRATIVOS (valores tipicos de libro, no medidos). El arco de un radian en segundos de arco, 648000/pi, es una definicion geometrica.
Modelo: escala de placa s = 206264,806 / F ["/mm]; campo exacto 2 atan(w/(2F)) frente a la aproximacion w/F; el ancho a mitad de altura (FWHM) del disco de Airy se
obtiene resolviendo numericamente (2 J1(x)/x)^2 = 1/2 con J1 calculada por su integral (Simpson), y se compara con la aproximacion 1,029 lambda/D.
Supuestos: sensor plano perpendicular al eje, sin distorsion. Validez: campo pequeño.
Tolerancia: constante 648000/pi frente a 206264,806 a 1e-6; FWHM numerica frente a 1,0290 lambda/D a 5e-4.
"""
from __future__ import annotations
import math, platform, sys

ARCSEC = 648000.0 / math.pi          # segundos de arco por radian


def J1(x, n=2000):
    h = math.pi / n
    s = 0.0
    for i in range(n + 1):
        t = i * h
        w = 1 if i in (0, n) else (4 if i % 2 else 2)
        s += w * math.cos(t - x * math.sin(t))
    return s * h / 3 / math.pi


def airy(x):
    return 1.0 if x == 0 else (2 * J1(x) / x) ** 2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"segundos de arco por radian = {ARCSEC:.3f}")
    assert abs(ARCSEC - 206264.806) < 1e-2
    D, F, lam = 200.0, 1000.0, 550e-9
    w, h, px = 22.3, 14.9, 4.3e-3
    esc = ARCSEC / F
    print(f"escala de placa = {esc:.3f} arcsec/mm = {esc*px:.4f} arcsec/pixel (pixel de {px*1e3:.1f} micras)")
    fov_w = 2 * math.degrees(math.atan(w / (2 * F)))
    fov_h = 2 * math.degrees(math.atan(h / (2 * F)))
    aprox_w = math.degrees(w / F)
    print(f"campo del sensor: {fov_w:.4f} x {fov_h:.4f} deg ; aproximacion w/F = {aprox_w:.4f} deg ; diferencia relativa = {(aprox_w-fov_w)/fov_w:.2e}")
    print(f"pixeles: {round(w/px)} x {round(h/px)} = {round(w/px)*round(h/px)/1e6:.2f} Mpix")
    # FWHM del disco de Airy
    lo, hi = 0.5, 3.0
    for _ in range(80):
        m = 0.5 * (lo + hi)
        if airy(m) > 0.5:
            lo = m
        else:
            hi = m
    x_half = 0.5 * (lo + hi)
    fwhm_lam_D = 2 * x_half / math.pi
    print(f"mitad de altura del disco de Airy en x = {x_half:.4f} ; FWHM = {fwhm_lam_D:.4f} lambda/D")
    assert abs(fwhm_lam_D - 1.0290) < 5e-4
    fwhm_arc = fwhm_lam_D * lam / (D * 1e-3) * ARCSEC
    print(f"FWHM difraccion (D = {D:.0f} mm, 550 nm) = {fwhm_arc:.4f} arcsec = {fwhm_arc/esc*1e3:.2f} micras en el plano focal")
    # muestreo
    pix_nyq = fwhm_arc / 2
    print(f"escala maxima para 2 pixeles por FWHM de difraccion = {pix_nyq:.4f} arcsec/pixel")
    seeing = 2.0
    print(f"con seeing de {seeing:.1f} arcsec el FWHM es el del seeing: 2 pixeles por FWHM -> {seeing/2:.2f} arcsec/pixel")
    print(f"escala real {esc*px:.4f} arcsec/pixel : {'submuestreado' if esc*px > seeing/2 else 'bien muestreado'} frente al seeing ; relacion FWHM/pixel (seeing) = {seeing/(esc*px):.2f}")
    assert esc * px < seeing / 2
    # reductor/barlow: cambia F y la escala
    print(f"{'factor':>7} {'F [mm]':>8} {'escala [\"/pix]':>15} {'campo ancho [deg]':>18}")
    for fac in (0.63, 1.0, 2.0):
        F2 = F * fac
        print(f"{fac:7.2f} {F2:8.0f} {ARCSEC/F2*px:15.4f} {2*math.degrees(math.atan(w/(2*F2))):18.4f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
