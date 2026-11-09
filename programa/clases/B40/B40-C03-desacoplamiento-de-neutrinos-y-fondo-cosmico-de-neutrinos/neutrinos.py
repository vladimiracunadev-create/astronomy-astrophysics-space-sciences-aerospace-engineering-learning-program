#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C03: fondo cosmico de neutrinos, conservacion de la entropia y (4/11)^(1/3).

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): k_B = 1,380649e-23 J/K (exacta), hbar = 1,054571817e-34 J s (exacta), c = 299792458 m/s (exacta), 1 eV = 1,602176634e-19 J,
m_e = 9,1093837139e-31 kg. T_0 = 2,7255 K es el valor redondeado de 2,72548 K que da Fixsen (2009, arXiv:0911.1955, solo resumen, consultado el 2026-11-09). N_eff = 3,044 es el valor del modelo
estandar de Bennett et al. (arXiv:2012.02726, solo resumen, consultado el 2026-11-09). zeta(3) se calcula por serie.
Modelo: entropia comovil conservada del plasma gamma + e+- (integrales de Fermi-Dirac numericas, potencial quimico nulo) con los neutrinos desacoplados, T_nu a = const.
Supuestos: desacoplamiento instantaneo a T ~ 1 MeV, distribuciones de Fermi-Dirac sin distorsion. Validez: el limite instantaneo equivale a N_eff = 3; la
correccion a 3,044 (oscilaciones, QED de temperatura finita) se toma de la fuente y no se calcula aqui.
Tolerancia: cociente T_gamma/T_nu frente a (11/4)^(1/3) a 1e-3 para m/T = 40; n_gamma a 1e-3 frente al valor conocido de unos 411 cm^-3.
"""
from __future__ import annotations
import math, platform, sys

KB = 1.380649e-23
HBAR = 1.054571817e-34
C = 299792458.0
EV = 1.602176634e-19
ME_C2_EV = 9.1093837139e-31 * C ** 2 / EV
T0 = 2.7255
NEFF = 3.044

def zeta3():
    return sum(1.0 / k ** 3 for k in range(1, 200001)) + 1.0 / (2 * 200000 ** 2)

def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3

def entropia_plasma(x):
    """Entropia por volumen (unidades T=1 -> m = x) de fotones + e+e-: s = (rho + P)/T, con T=1."""
    m = x
    def rho(p):
        e = math.sqrt(p * p + m * m)
        return p * p * e / (math.exp(e) + 1)
    def pre(p):
        e = math.sqrt(p * p + m * m)
        return p ** 4 / (3 * e) / (math.exp(e) + 1)
    pmax = 60.0
    g = 4 / (2 * math.pi ** 2)             # 2 spin x 2 (e- y e+)
    r = g * simpson(rho, 0, pmax)
    p = g * simpson(pre, 0, pmax)
    sf = r + p
    sg = 2 * math.pi ** 2 / 45 * 2         # fotones: s = 2 pi^2/45 g T^3 con g = 2
    return sg + sf

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    me_t0 = 0.1                                    # m/T inicial: e+- relativistas, T_nu = T_gamma
    s0 = entropia_plasma(me_t0)                    # en unidades de T_0 = 1 (T = m / x)
    print(f"{'m/T_gamma':>10} {'T_gamma/T_nu':>13} {'(11/4)^(1/3)':>13} {'diferencia':>11}")
    objetivo = (11 / 4) ** (1 / 3)
    res = {}
    for x in (0.1, 1.0, 3.0, 10.0, 40.0):
        # s(T) a^3 = const con T_nu = 1/a: T_nu^3 = s(T)/s0, con T = 0,1/x en unidades de T(x0) = 1
        T = 0.1 / x
        T_nu = (T ** 3 * entropia_plasma(x) / s0) ** (1 / 3) if x != 0.1 else T
        res[x] = T / T_nu if x != 0.1 else 1.0
    for x, r in res.items():
        print(f"{x:10.1f} {r:13.5f} {objetivo:13.5f} {r - objetivo:+11.5f}")
    assert abs(res[40.0] - objetivo) < 1e-3 * objetivo
    # cantidades actuales
    tnu0 = T0 / objetivo
    z3 = zeta3()
    n_gamma = 2 * z3 / math.pi ** 2 * (KB * T0 / (HBAR * C)) ** 3          # m^-3
    n_nu = 3 / 11 * n_gamma                                                    # por especie (nu + nubar)
    fac = 1 + 7 / 8 * (4 / 11) ** (4 / 3) * NEFF
    print(f"T_nu,0 = T_0 (4/11)^(1/3) = {tnu0:.4f} K (T_0 = {T0} K)")
    print(f"n_gamma = {n_gamma * 1e-6:.2f} cm^-3 ; n_nu por especie = {n_nu * 1e-6:.2f} cm^-3 ; total 3 especies = {3 * n_nu * 1e-6:.1f} cm^-3")
    print(f"rho_rad / rho_gamma = 1 + 7/8 (4/11)^(4/3) N_eff = {fac:.4f} (N_eff = {NEFF}) ; con N_eff = 3: {1 + 7 / 8 * (4 / 11) ** (4 / 3) * 3:.4f}")
    print(f"k_B T_nu,0 = {KB * tnu0 / EV * 1e4:.4f} x 1e-4 eV ; m_e c^2 = {ME_C2_EV / 1e6:.5f} MeV")
    assert abs(n_gamma * 1e-6 - 411) < 1.0
    assert abs(n_nu * 1e-6 - 112) < 0.5
    assert abs(tnu0 - 1.9454) < 5e-4
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
