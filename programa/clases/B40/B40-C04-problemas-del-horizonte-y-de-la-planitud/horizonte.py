#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C04: horizonte comovil, tamano angular causal en la recombinacion y desvanecimiento de la curvatura.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): k_B, hbar, c, G; au = 149597870700 m (exacta, UAI 2012). Del resumen de Planck 2018 VI (arXiv:1807.06209, solo
resumen, consultado el 2026-11-09): H_0 = 67,4 km/s/Mpc y Omega_m = 0,315. T_0 = 2,7255 K (redondeo de 2,72548 K de Fixsen 2009, solo resumen), N_eff = 3,044 (Bennett et al. 2021, solo resumen).
Son ILUSTRATIVOS: z* = 1090 (valor redondeado adoptado, no leido), |Omega_k| hoy = 1e-3 (un numero para el ejemplo, no una medida) y las energias de 1 MeV y 1e16 GeV.
Modelo: universo FLRW con radiacion, materia, constante cosmologica y curvatura; E(z)^2 = Omega_r (1+z)^4 + Omega_m (1+z)^3 + Omega_L + Omega_k (1+z)^2.
Segunda via: el horizonte analitico de radiacion + materia sin Lambda, eta = 2c/(H_0 sqrt(Omega_m)) [sqrt(a + a_eq) - sqrt(a_eq)] con a_eq = Omega_r/Omega_m (se compara tambien con materia pura, que falla), y la distancia comovil con otra variable de integracion.
Supuestos: neutrinos tratados como radiacion sin masa. Validez: ilustrativa; no ajusta datos.
Tolerancia: horizonte numerico frente al analitico de radiacion + materia, 2 %; dos integraciones entre si, 1e-6 relativo.
"""
from __future__ import annotations
import math, platform, sys

KB = 1.380649e-23
HBAR = 1.054571817e-34
C = 299792458.0
G = 6.67430e-11
AU = 149597870700.0
MPC = AU * 648000 / math.pi * 1e6
EV = 1.602176634e-19
T0 = 2.7255
NEFF = 3.044
H0 = 67.4e3 / MPC                       # 1/s
OM = 0.315
rho_c = 3 * H0 ** 2 / (8 * math.pi * G)          # kg/m^3
u_g = math.pi ** 2 / 15 * (KB * T0) ** 4 / (HBAR ** 3 * C ** 3)    # J/m^3
OG = u_g / C ** 2 / rho_c
OR = OG * (1 + 7 / 8 * (4 / 11) ** (4 / 3) * NEFF)
OK = 0.0
OL = 1 - OM - OR - OK

def e2(z, ok=0.0):
    ol = 1 - OM - OR - ok
    return OR * (1 + z) ** 4 + OM * (1 + z) ** 3 + ol + ok * (1 + z) ** 2

def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3

def chi(z):
    # distancia comovil [Mpc], variable x = ln(1+z)
    return simpson(lambda x: C / (H0 * math.sqrt(e2(math.exp(x) - 1))) * math.exp(x), 0, math.log(1 + z)) / MPC

def chi_lineal(z):
    return simpson(lambda zz: C / (H0 * math.sqrt(e2(zz))), 0, z) / MPC

def eta(z):
    # horizonte de particulas comovil [Mpc]: desde z hasta z grande
    return simpson(lambda x: C / (H0 * math.sqrt(e2(math.exp(x) - 1))) * math.exp(x), math.log(1 + z), math.log(1e12), 40000) / MPC

def desv(z, ok=1e-3):
    # |Omega - 1| (z) = |Omega_k| (1+z)^2 / E^2
    return abs(ok) * (1 + z) ** 2 / e2(z, ok)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Omega_gamma = {OG:.4e} ; Omega_r = {OR:.4e} ; Omega_L = {OL:.4f} ; Mpc = {MPC:.6e} m")
    zs = 1090.0
    e_s = eta(zs)
    x_s = chi(zs)
    x_s2 = chi_lineal(zs)
    teta = e_s / x_s
    a_eq = OR / OM
    e_rm = 2 * C / (H0 * math.sqrt(OM)) * (math.sqrt(1 / (1 + zs) + a_eq) - math.sqrt(a_eq)) / MPC
    e_mat = 2 * C / (H0 * math.sqrt(OM) * math.sqrt(1 + zs)) / MPC
    print(f"{'z':>8} {'chi [Mpc]':>12} {'eta [Mpc]':>12}")
    for z in (10.0, 100.0, 1090.0):
        print(f"{z:8.0f} {chi(z):12.1f} {eta(z):12.2f}")
    print(f"z* = {zs:.0f}: eta* = {e_s:.2f} Mpc ; chi* = {x_s:.1f} Mpc ({x_s2:.1f} con otra variable)")
    print(f"angulo causal eta*/chi* = {teta:.5f} rad = {math.degrees(teta):.3f} grados ; (chi*/eta*)^2 = {(x_s / e_s) ** 2:.0f} parches")
    print(f"z_eq = 1/a_eq - 1 = {1 / a_eq - 1:.0f} ; horizonte analitico radiacion + materia = {e_rm:.2f} Mpc ; cociente numerico/analitico = {e_s / e_rm:.4f}")
    print(f"horizonte de materia pura (sin radiacion) = {e_mat:.2f} Mpc ; cociente numerico/materia = {e_s / e_mat:.4f}")
    t_mev = 1e6 / (KB / EV * T0)
    z_mev = 1e6 / (KB / EV * T0)
    z_gut = 1e25 / (KB / EV * T0)
    d_now = desv(0.0)
    d_mev = desv(z_mev)
    d_gut = desv(z_gut)
    n_nec = 0.5 * math.log(1.0 / d_gut)
    print(f"|Omega - 1| hoy = {d_now:.2e} ; a T = 1 MeV (z = {z_mev:.3e}) = {d_mev:.2e} ; a T = 1e16 GeV (z = {z_gut:.3e}) = {d_gut:.2e}")
    r_rd = desv(z_mev) / desv(z_mev * 10)
    print(f"cociente |Omega-1|(z)/|Omega-1|(10 z) en radiacion = {r_rd:.3f} (esperado 100: proporcional a a^2)")
    print(f"e-pliegues para llevar |Omega - 1| de {d_gut:.1e} a 1 antes de inflar: N = (1/2) ln(1/d) = {n_nec:.1f}")
    assert abs(x_s - x_s2) / x_s < 1e-6
    assert abs(e_s / e_rm - 1) < 0.02
    assert abs(r_rd - 100) < 1.0
    assert 0.5 < math.degrees(teta) < 2.5
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
