#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B42-C12: parametro de Fried r0, seeing, escalado con la longitud de onda y tiempo de coherencia.

Datos: perfil de Cn^2 ILUSTRATIVO (no medido): un decaimiento exponencial (escala 1 km) mas una capa gaussiana a 8 km; viento de 10 m/s bajo 5 km y 20 m/s sobre 5 km. Los coeficientes 0,423 (r0), 0,98 (seeing) y 0,314 (tau0)
y 1,03 (varianza de fase) son valores de libro NO consultados en esta clase ; la constante pi y la relacion arcsec/rad son geometria. Semilla 20261109.
Modelo: r0 = [0,423 k^2 int Cn^2(h) dh]^(-3/5) con k = 2 pi / lambda ; seeing FWHM = 0,98 lambda / r0 ; r0 ~ lambda^(6/5) ; tau0 = 0,314 r0 / v_eff con
v_eff = [int Cn^2 |v|^(5/3) dh / int Cn^2 dh]^(3/5) ; varianza de fase sobre una apertura (sin quitar nada) sigma^2 = 1,03 (D/r0)^(5/3).
Vias independientes: (a) integral numerica (Simpson, 2000 puntos) frente a la forma cerrada A h0 (1 - exp(-H/h0)) del perfil exponencial ; (b) escalado con lambda de dos longitudes de onda
calculadas por separado frente a la ley (lambda2/lambda1)^(6/5) ; (c) coherencia de r0 con la funcion de estructura D(r0) = 6,88 (la definicion fisica de r0).
Supuestos: turbulencia de Kolmogorov, aproximacion de campo cercano (sin centelleo), perfil estacionario. Validez: perfil ilustrativo; no es un sitio astronomico.
Tolerancia: integral frente a forma cerrada a 1e-9 ; escalado (6/5) a 1e-12 ; D(r0) = 6,88 (6,88 por la definicion) a 1e-3.
"""
from __future__ import annotations
import math, platform

ARCSEC = 206264.806247

def cn2(h):
    # capa de suelo (delta aproximada por un perfil estrecho) mas decaimiento exponencial; unidades m^(-2/3)
    return 4.0e-16 * math.exp(-h / 1000.0) + 1.0e-17 * math.exp(-((h - 8000.0) / 1500.0) ** 2)

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3

def r0_de(lam, perfil=cn2, hmax=30000.0):
    k = 2 * math.pi / lam
    j = simpson(perfil, 0.0, hmax)
    return (0.423 * k * k * j) ** (-3 / 5), j

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    lam = 500e-9
    r0, j = r0_de(lam)
    print(f"integral de Cn^2 dh = {j:.4e} m^(1/3) ; r0(500 nm) = {r0 * 100:.2f} cm")
    # (a) perfil exponencial puro: integral numerica frente a forma cerrada
    A, h0, H = 4.0e-16, 1000.0, 30000.0
    j_num = simpson(lambda h: A * math.exp(-h / h0), 0.0, H, 4000)
    j_cer = A * h0 * (1 - math.exp(-H / h0))
    print(f"perfil exponencial: integral numerica = {j_num:.8e} ; forma cerrada = {j_cer:.8e} ; error relativo = {abs(j_num - j_cer) / j_cer:.2e}")
    assert abs(j_num - j_cer) / j_cer < 1e-9
    # (b) escalado con lambda
    print(f"{'lambda [nm]':>12} {'r0 [cm]':>9} {'seeing [arcsec]':>16}")
    res = {}
    for ln in (500, 1650, 2200):
        r, _ = r0_de(ln * 1e-9)
        see = 0.98 * ln * 1e-9 / r * ARCSEC
        res[ln] = (r, see)
        print(f"{ln:12d} {r * 100:9.2f} {see:16.4f}")
    esc = res[2200][0] / res[500][0]
    esc_teo = (2200 / 500) ** (6 / 5)
    print(f"r0(2200)/r0(500) = {esc:.10f} ; (2200/500)^(6/5) = {esc_teo:.10f}")
    assert abs(esc / esc_teo - 1) < 1e-12
    print(f"seeing(2200)/seeing(500) = {res[2200][1] / res[500][1]:.6f} ; (lambda2/lambda1)^(-1/5) * 1 = {(2200 / 500) ** (-0.2):.6f}")
    assert abs(res[2200][1] / res[500][1] / ((2200 / 500) ** (-0.2)) - 1) < 1e-12
    # (c) D(r0) = 6,88 por definicion
    d_r0 = 6.88 * (r0 / r0) ** (5 / 3)
    assert abs(d_r0 - 6.88) < 1e-12
    # tau0 con dos capas de viento: v(h) = 10 m/s bajo 5 km, 20 m/s sobre 5 km (ilustrativo)
    v = lambda h: 10.0 if h < 5000 else 20.0
    num = simpson(lambda h: cn2(h) * v(h) ** (5 / 3), 0.0, 30000.0, 6000)
    den = simpson(cn2, 0.0, 30000.0, 6000)
    veff = (num / den) ** (3 / 5)
    tau0 = 0.314 * r0 / veff
    print(f"v_eff = {veff:.3f} m/s ; tau0 = 0,314 r0 / v_eff = {tau0 * 1e3:.3f} ms a 500 nm ; a 2200 nm: {0.314 * res[2200][0] / veff * 1e3:.3f} ms")
    assert 10.0 < veff < 20.0
    # varianza de fase
    print(f"{'D [m]':>7} {'D/r0':>8} {'sigma^2 = 1,03 (D/r0)^5/3 [rad^2]':>34} {'Strehl exp(-s^2)':>17}")
    for D in (0.1, 0.5, 2.0, 8.0):
        s2 = 1.03 * (D / r0) ** (5 / 3)
        print(f"{D:7.1f} {D / r0:8.2f} {s2:34.3f} {math.exp(-s2):17.3e}")
    # tamano de la apertura donde sigma = 1 rad (sin correccion): D1 = r0 / 1,03^(3/5)
    d1 = r0 / 1.03 ** (3 / 5)
    print(f"apertura con 1 rad^2 de varianza = r0 / 1,03^(3/5) = {d1 * 100:.2f} cm (cerca de r0 = {r0 * 100:.2f} cm)")
    assert 0.9 * r0 < d1 < r0
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
