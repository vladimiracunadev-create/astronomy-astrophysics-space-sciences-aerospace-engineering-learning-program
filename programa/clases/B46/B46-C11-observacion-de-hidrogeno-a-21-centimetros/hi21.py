#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B46-C11: velocidad terminal de HI con curva plana y densidad de columna optica delgada.

Datos: h, k, c de NIST CODATA 2022 (consultada 2026-11-09). La frecuencia 1420.405751768 MHz y la longitud de onda 21.106 cm se consultaron en
Wikipedia (Hydrogen line) el 2026-11-09; esa pagina da la tasa de transicion como 2,9e-15 s^-1, y el valor mas preciso A10 = 2,8843e-15 s^-1 es de
la literatura y NO se consulto aqui. R0 = 8,5 kpc, V0 = 220 km/s y la curva plana son ILUSTRATIVOS (valores historicos de la UAI, no consultados).
Modelo: v_r(R) = V0 R0 sin(l) (1/R - 1/R0) para curva plana; maximo en la tangente R = R0 sin(l), v_t = V0 (1 - sin l). N_HI = 32 pi k nu^2/(3 h c^3 A10) integral T_B dv.
Se compara con el coeficiente conocido 1,8224e18 cm^-2 por K km/s y con la integral numerica de un perfil gaussiano.
Supuestos: optica delgada, T_s >> 0,07 K, movimiento circular. Validez: orientativa.
Tolerancia: maximo numerico de v_r frente al analitico dentro de 0,01 km/s; coeficiente de columna dentro del 1,5 % de 1,8224e18.
"""
from __future__ import annotations
import math, platform
H, K, C = 6.62607015e-34, 1.380649e-23, 299792458.0
NU, A10 = 1420.405751768e6, 2.8843e-15
R0, V0 = 8.5, 220.0

def vr(R, l):
    return V0 * R0 * math.sin(l) * (1 / R - 1 / R0)

def calc():
    filas = []
    for ld in (15, 30, 45, 60):
        l = math.radians(ld)
        Rmin = R0 * math.sin(l) - 0.3          # la linea de vision no baja de R0 sin l; se busca en una ventana
        Rs = [Rmin + i * 1e-4 for i in range(int((R0 - Rmin) / 1e-4))]
        Rs = [R for R in Rs if R >= R0 * math.sin(l)]
        best = max(range(len(Rs)), key=lambda i: vr(Rs[i], l))
        filas.append((ld, Rs[best], vr(Rs[best], l), V0 * (1 - math.sin(l)), R0 * math.sin(l)))
    coef = 32 * math.pi * K * NU ** 2 / (3 * H * C ** 3 * A10)       # m^-2 por (K m/s)
    coef_cm = coef * 1e3 / 1e4                                       # cm^-2 por (K km/s)
    # perfil gaussiano T=50 K, sigma 8 km/s : integral numerica
    sig, T0 = 8.0, 50.0
    vs = [-100 + i * 0.01 for i in range(20001)]
    integ = sum(T0 * math.exp(-0.5 * (v / sig) ** 2) for v in vs) * 0.01
    integ_ana = T0 * sig * math.sqrt(2 * math.pi)
    return dict(filas=filas, coef_cm=coef_cm, integ=integ, integ_ana=integ_ana, N=coef_cm * integ, lam=C / NU * 100,
                dv_kHz=NU * 1.0e3 / C / 1e3)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print(f"{'l [grados]':>10} {'R max [kpc]':>12} {'v_r max [km/s]':>15} {'V0(1-sin l)':>12} {'R0 sin l':>9}")
    for ld, R, v, va, Rt in r["filas"]:
        print(f"{ld:10d} {R:12.3f} {v:15.3f} {va:12.3f} {Rt:9.3f}")
    print(f"coeficiente de columna = {r['coef_cm']:.4e} cm^-2 por K km/s (referencia 1.8224e18)")
    print(f"integral T dv: numerica = {r['integ']:.2f} K km/s ; analitica = {r['integ_ana']:.2f} K km/s ; N_HI = {r['N']:.3e} cm^-2")
    print(f"1 km/s equivale a {r['dv_kHz']:.3f} kHz a 1420.405752 MHz")
    for ld, R, v, va, Rt in r["filas"]:
        assert abs(v - va) < 0.01 and abs(R - Rt) < 2e-4
    assert abs(r["coef_cm"] / 1.8224e18 - 1) < 0.015
    assert abs(r["integ"] / r["integ_ana"] - 1) < 1e-6
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
