#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C07: horizonte sonoro y oscilaciones acusticas barionicas como regla estandar.

Datos: constantes de NIST CODATA 2022 (c, G, k_B, hbar; tabla allascii consultada 2026-11-09); 1 au exacto (IERS TN36, consultada 2026-11-09) para el Mpc;
Omega_m = 0.315, H0 = 67.4 km/s/Mpc y Omega_b h^2 = 0.0224 (resumen de Planck 2018, arXiv:1807.06209, consultado 2026-11-09).
T_CMB = 2.7255 K, N_eff = 3.046 y el desplazamiento de arrastre z_d = 1060 son valores ILUSTRATIVOS (no se consultaron sus fuentes). El resumen de Eisenstein et al. 2005
(arXiv:astro-ph/0501171, consultado 2026-11-09) dice que el pico esta en unos 100 h^-1 Mpc: es la unica comparacion con una observacion.
Modelo: r_s = Int_0^{a_d} c_s da/(a^2 H), c_s = c/sqrt(3(1+R)), R = R0 a, R0 = 3 rho_b/(4 rho_gamma); H con materia, radiacion (fotones + neutrinos) y Lambda plana.
Segunda via: con solo materia y radiacion r_s tiene la forma cerrada (2c/(sqrt(3 Omega_m) H0 sqrt(R0))) ln[(sqrt(R0(a_d+a_eq)) + sqrt(1+R0 a_d))/(sqrt(R0 a_eq) + 1)], derivada aqui.
Ajuste de juguete: xi(r) sintetica con un pico gaussiano, dilatacion alpha = 1,03 y ruido gaussiano ILUSTRATIVO (semilla 20261109).
Supuestos: plano, sin neutrinos masivos, c_s del fluido foton-barion, sin recombinacion detallada. Validez: orientativa (precision ~1 %).
Tolerancia: numerico frente a cerrado, 1e-5; alpha ajustado dentro de 3 sigma de la verdad.
"""
from __future__ import annotations
import math, platform, random

C = 299792458.0
G = 6.67430e-11
KB = 1.380649e-23
HBAR = 1.054571817e-34
AU = 149597870700.0
MPC = AU * 648000 / math.pi * 1e6
H0 = 67.4
OM = 0.315
OBH2 = 0.0224
H = H0 / 100
TCMB = 2.7255
NEFF = 3.046
ZD = 1060.0


def omegas():
    u = math.pi ** 2 / 15 * (KB * TCMB) ** 4 / (HBAR * C) ** 3  # J/m^3
    rho_c1 = 3 * (100e3 / MPC) ** 2 / (8 * math.pi * G) * C ** 2  # J/m^3 para h = 1
    ogh2 = u / rho_c1
    fnu = NEFF * 7.0 / 8.0 * (4.0 / 11.0) ** (4.0 / 3.0)
    orh2 = ogh2 * (1 + fnu)
    return ogh2, orh2


OGH2, ORH2 = omegas()
OR = ORH2 / H ** 2
OL = 1 - OM - OR
R0 = 3 * OBH2 / (4 * OGH2)


def E(a):
    return math.sqrt(OM * a ** -3 + OR * a ** -4 + OL)


def r_s_num(ad, con_lambda=True, n=20000):
    def f(a):
        e = math.sqrt(OM * a ** -3 + OR * a ** -4 + (OL if con_lambda else 0.0))
        return 1 / (a * a * e * math.sqrt(3 * (1 + R0 * a)))
    h = ad / n
    s = f(1e-12) + f(ad)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(i * h)
    return C / (H0 * 1e3) * s * h / 3 * (MPC / MPC)  # Mpc: c/H0 en Mpc * integral adimensional


def r_s_cerrado(ad):
    aeq = OR / OM
    pref = 2 / math.sqrt(R0) / math.sqrt(3 * OM)
    br = math.sqrt(R0 * (ad + aeq)) + math.sqrt(1 + R0 * ad)
    b0 = math.sqrt(R0 * aeq) + 1
    return (C / (H0 * 1e3)) * pref * math.log(br / b0)


def dm(z, n=4000):
    h = z / n
    f = lambda zz: 1 / E(1 / (1 + zz))
    s = f(0) + f(z) + sum((4 if i % 2 else 2) * f(i * h) for i in range(1, n))
    return C / (H0 * 1e3) * s * h / 3


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Omega_gamma h^2 = {OGH2:.4e} ; Omega_r h^2 (con neutrinos) = {ORH2:.4e} ; Omega_r = {OR:.3e} ; Omega_Lambda = {OL:.4f}")
    aeq = OR / OM
    print(f"a_eq = {aeq:.3e} (z_eq = {1 / aeq - 1:.0f}) ; R0 = 3 rho_b/(4 rho_gamma) = {R0:.1f} ; R(z_d) = {R0 / (1 + ZD):.3f}")
    ad = 1 / (1 + ZD)
    rn = r_s_num(ad)
    rc = r_s_cerrado(ad)
    rn0 = r_s_num(ad, con_lambda=False)
    print(f"r_s numerico (con Lambda) = {rn:.3f} Mpc ; sin Lambda = {rn0:.3f} Mpc ; forma cerrada = {rc:.3f} Mpc")
    print(f"dif. relativa numerico(sin Lambda)-cerrado = {abs(rn0 - rc) / rc:.2e} ; efecto de Lambda = {abs(rn - rn0) / rn:.2e}")
    print(f"r_s h = {rn * H:.2f} h^-1 Mpc")
    print(f"{'z':>6} {'D_M [Mpc]':>10} {'D_H [Mpc]':>10} {'D_V [Mpc]':>10} {'D_V/r_s':>8} {'theta=r_s/D_M [deg]':>20}")
    tab = {}
    for z in (0.35, 0.57, 1.0, 2.34):
        d = dm(z)
        dh = C / (H0 * 1e3) / E(1 / (1 + z))
        dv = (z * d * d * dh) ** (1 / 3)
        th = math.degrees(rn / d)
        tab[z] = (d, dh, dv)
        print(f"{z:6.2f} {d:10.1f} {dh:10.1f} {dv:10.1f} {dv / rn:8.3f} {th:20.3f}")
    # sensibilidad: Omega_m +5 % con omega_b y omega_m h^2 fijos NO se reajusta aqui; solo se cambia la geometria
    # ajuste de juguete de alpha
    rng = random.Random(20261109)
    rs_h = rn * H
    xs = [60 + 4 * i for i in range(21)]
    liso = lambda r: (r / 20.0) ** -1.8 * 0.9
    bump = lambda r, a: 0.0035 * math.exp(-0.5 * ((r / a - rs_h) / 8.0) ** 2)
    alpha_t = 1.03
    sg = 0.0006
    datos = [liso(r) + bump(r, alpha_t) + rng.gauss(0, sg) for r in xs]
    best = None
    curva = []
    for k in range(0, 2001):
        al = 0.90 + 0.0001 * k
        chi2 = sum(((d - liso(r) - bump(r, al)) / sg) ** 2 for r, d in zip(xs, datos))
        curva.append((al, chi2))
        if best is None or chi2 < best[1]:
            best = (al, chi2)
    # intervalo de Delta chi2 = 1
    ok = [al for al, c in curva if c <= best[1] + 1]
    sa = 0.5 * (max(ok) - min(ok))
    # Fisher analitico
    e = 1e-5
    fis = sum(((bump(r, alpha_t + e) - bump(r, alpha_t - e)) / (2 * e) / sg) ** 2 for r in xs)
    sf = 1 / math.sqrt(fis)
    print(f"ajuste de alpha: {best[0]:.4f} +/- {sa:.4f} (Delta chi2 = 1) ; Fisher: +/- {sf:.4f} ; verdad {alpha_t} ; chi2_min = {best[1]:.1f} con 20 gl")
    print(f"el 1 % en alpha equivale a {0.01 * rs_h:.2f} h^-1 Mpc en la posicion del pico ({rs_h:.2f} h^-1 Mpc)")
    assert abs(rn0 - rc) / rc < 1e-5
    assert abs(rn - rn0) / rn < 1e-4
    assert 140 < rn < 155
    assert abs(best[0] - alpha_t) < 3 * sa
    assert abs(sa - sf) / sf < 0.15
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
