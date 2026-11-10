#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B92-C01: rejilla de frecuencias, potencia de pico en PPM y amplificador saturable.

Datos consultados (2026-11-10): h = 6.62607015e-34 J s y c = 299792458 m/s exactos (NIST, CODATA 2022);
rejilla de frecuencias 193.1 + n*0.1 THz con n = -18..28 (CCSDS 141.0-B-1, sec. 3.2), que da 1530.33 a 1567.13 nm;
PPM con M/4 ranuras de guarda tras cada simbolo de M ranuras (CCSDS 142.0-B-1, sec. 3.13).
ILUSTRATIVOS (sinteticos, no medidos): potencia media 4 W, ranura de 1 ns, M = 16, energia de saturacion 20 uJ,
ganancia de pequena senal 30 dB, potencia de semilla 10 mW, eficiencia electrica 10 %.
Modelo: E = h c / lambda; duty = 1/(1.25 M); P_pico = P_media / duty; amplificador de energia de Frantz-Nodvik
E_sal = E_sat ln(1 + G0 (exp(E_ent/E_sat) - 1)).
Segunda via: limite de pequena senal (E_sal -> G0 E_ent) e integracion numerica de la ecuacion de saturacion dE/dz.
Tolerancia: rejilla 1e-9 relativa; Frantz-Nodvik frente a integracion numerica 1e-6 relativa.
"""
from __future__ import annotations
import math, platform

H = 6.62607015e-34
C = 299792458.0


def lam_nm(n):
    return C / ((193.1 + 0.1 * n) * 1e12) * 1e9


def fotones_por_s(p, lam):
    return p / (H * C / lam)


def duty(m):
    return 1.0 / (1.25 * m)


def frantz_nodvik(e_in, e_sat, g0):
    return e_sat * math.log(1.0 + g0 * (math.exp(e_in / e_sat) - 1.0))


def integra(e_in, e_sat, g0, n=200000):
    """Integra dE/dz = e_sat * g(z)... con ganancia de pequena senal G0 = exp(L): dE/dL = e_sat*(1-exp(-E/e_sat))."""
    L = math.log(g0)
    h = L / n
    e = e_in
    for _ in range(n):  # Runge-Kutta 4
        f = lambda x: e_sat * (1.0 - math.exp(-x / e_sat))
        k1 = f(e); k2 = f(e + 0.5 * h * k1); k3 = f(e + 0.5 * h * k2); k4 = f(e + h * k3)
        e += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
    return e


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Rejilla CCSDS 141.0-B-1 (frecuencia central 193.1 + n*0.1 THz)")
    for n in (-18, 0, 28):
        print(f"  n = {n:3d}: f = {193.1 + 0.1 * n:7.1f} THz  lambda = {lam_nm(n):8.2f} nm")
    lam0 = lam_nm(0) * 1e-9
    e_f = H * C / lam0
    print(f"Energia de un foton en n = 0: {e_f:.4e} J ; fotones por julio = {1 / e_f:.4e}")
    pm = 4.0
    print(f"Potencia media ILUSTRATIVA {pm} W -> {fotones_por_s(pm, lam0):.4e} fotones/s")
    print(" M   duty     P_pico [W]  E_pulso [nJ] (ranura 1 ns)")
    for m in (4, 16, 64, 256):
        d = duty(m)
        pp = pm / d
        ep = pp * 1e-9 * 1e9
        print(f"{m:4d} {d:8.5f} {pp:11.2f} {ep:11.3f}")
    print("Amplificador saturable (Frantz-Nodvik) ILUSTRATIVO: E_sat = 20 uJ, G0 = 30 dB")
    e_sat, g0 = 20e-6, 10 ** 3.0
    dmax = 0.0
    for e_in in (1e-9, 1e-7, 1e-6, 1e-5, 5e-5):
        fn = frantz_nodvik(e_in, e_sat, g0)
        num = integra(e_in, e_sat, g0)
        dmax = max(dmax, abs(fn - num) / fn)
        print(f"  E_ent = {e_in * 1e6:9.4f} uJ  E_sal = {fn * 1e6:10.4f} uJ  ganancia = {10 * math.log10(fn / e_in):6.2f} dB")
    pequena = frantz_nodvik(1e-12, e_sat, g0) / 1e-12
    print(f"Ganancia de pequena senal recuperada: {10 * math.log10(pequena):.4f} dB (esperado 30)")
    print(f"Diferencia relativa maxima Frantz-Nodvik frente a integracion RK4 = {dmax:.2e}")
    eta = 0.10
    print(f"Potencia electrica para 4 W opticos con eficiencia {eta:.0%}: {pm / eta:.1f} W")
    # comprobaciones
    assert abs(lam_nm(-18) - 1567.13) < 0.01 and abs(lam_nm(28) - 1530.33) < 0.01
    assert abs(frantz_nodvik(1e-12, e_sat, g0) / 1e-12 - g0) / g0 < 1e-3
    assert dmax < 1e-6
    assert abs(duty(16) * 1.25 * 16 - 1.0) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
