#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C07: incertidumbre y limite de deteccion de un dosimetro personal por conteo (datos SINTETICOS).

Modelo: el dosimetro acumula N cuentas = Poisson(s H + B) con sensibilidad s = 200 cuentas/mSv y fondo B = 50 cuentas en el periodo (ILUSTRATIVOS).
Estimador H = (N - B_est)/s con B_est medido en un dosimetro de control con la misma Poisson; incertidumbre sigma_H = sqrt(N + B_est)/s (aprox.
poissoniana). Limite critico y de deteccion de Currie (1968) en cuentas: L_C = 1.645 sqrt(2 B), L_D = 2.71 + 4.65 sqrt(B) (formulas recordadas por el
autor, NO consultadas en la fuente aqui; se verifican por simulacion). Todo SINTETICO, semilla 105. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

S, B = 200.0, 50.0


def estimar(h_real, rng, n):
    cuentas = rng.poisson(S * h_real + B, n)
    fondo = rng.poisson(B, n)
    h = (cuentas - fondo) / S
    sigma = np.sqrt(cuentas + fondo) / S
    return h, sigma


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): sensibilidad 200 cuentas/mSv, fondo 50 cuentas; formulas de Currie no consultadas en la fuente")
    rng = np.random.default_rng(105)
    n = 20000
    print("Estimacion de H con 20000 repeticiones por dosis verdadera:")
    for h_real in (0.0, 0.1, 0.5, 2.0, 10.0, 50.0):
        h, sg = estimar(h_real, rng, n)
        cubre = np.mean(np.abs(h - h_real) <= 1.96 * sg)
        print(f"  H = {h_real:5.1f} mSv: media {h.mean():7.3f}, DE {h.std():6.3f} mSv, sigma formal media {sg.mean():6.3f}; cobertura 95 % = {cubre:.3f}")
    lc = 1.645 * np.sqrt(2 * B)
    ld = 2.71 + 4.65 * np.sqrt(B)
    print(f"Currie: L_C = {lc:.1f} cuentas = {lc / S:.3f} mSv; L_D = {ld:.1f} cuentas = {ld / S:.3f} mSv")
    h0, _ = estimar(0.0, rng, 200000)
    fa = np.mean(h0 * S > lc)
    h_ld, _ = estimar(ld / S, rng, 200000)
    det = np.mean(h_ld * S > lc)
    print(f"Simulacion: falsas alarmas con H = 0 y umbral L_C = {fa:.4f} (objetivo 0.05); deteccion con H = L_D/s = {det:.3f} (objetivo 0.95)")
    # recalibracion: pendiente por minimos cuadrados con 6 dosis de referencia
    dosis = np.array([1, 2, 5, 10, 20, 50.0])
    y = rng.poisson(S * dosis + B) - rng.poisson(B)
    sest = (dosis @ y) / (dosis @ dosis)
    print(f"Calibracion con 6 dosis de referencia: s estimada = {sest:.2f} cuentas/mSv (verdad {S:.0f})")
    assert abs(lc - 16.45) < 0.01 and abs(ld - 35.6) < 0.1
    assert abs(fa - 0.05) < 0.01
    assert abs(det - 0.95) < 0.02
    assert abs(sest - S) < 5
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
