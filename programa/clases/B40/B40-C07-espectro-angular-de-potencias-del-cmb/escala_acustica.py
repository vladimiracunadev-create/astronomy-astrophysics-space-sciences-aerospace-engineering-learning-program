#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C07: escala acustica del CMB y transformada de Legendre entre C(theta) y C_l.

Datos: constantes de NIST CODATA 2022 (consultadas el 2026-11-09): k_B, hbar, c, G; au = 149597870700 m. Del resumen de Planck 2018 VI (arXiv:1807.06209, solo resumen, consultado el
2026-11-09): H_0 = 67,4 km/s/Mpc, Omega_m = 0,315, Omega_b h^2 = 0,0224, Omega_c h^2 = 0,120 y 100 theta_* = 1,0411 +- 0,0003. T_0 = 2,7255 K (Fixsen 2009, solo resumen) y N_eff = 3,044
(Bennett et al. 2021, solo resumen). z_* = 1090 es un valor redondeado ADOPTADO y el espectro de juguete C_l (meseta mas oscilacion coseno) es ILUSTRATIVO.
Modelo: theta_* = r_s(z_*) / D_M(z_*) con r_s = integral de c_s dz / H, c_s = c / sqrt(3 (1 + R)), R = 3 rho_b / (4 rho_gamma); C(theta) = sum (2l+1)/(4 pi) C_l P_l(cos theta) y su
inversa C_l = 2 pi integral de C(x) P_l(x) dx por cuadratura de Gauss-Legendre.
Supuestos: universo plano, plasma fotones-bariones sin retroceso, recombinacion instantanea en z_*. Validez: ilustrativa; no es un codigo de Boltzmann.
Tolerancia: theta_* frente al valor de Planck, 1 % ; ida y vuelta de C_l a 1e-9 relativo.
"""
from __future__ import annotations
import math, platform, sys

KB = 1.380649e-23; HBAR = 1.054571817e-34; C = 299792458.0; G = 6.67430e-11
AU = 149597870700.0; MPC = AU * 648000 / math.pi * 1e6
T0 = 2.7255; NEFF = 3.044
H_ = 0.674; H0 = H_ * 100e3 / MPC
OM = 0.315; OBH2 = 0.0224
rho_c = 3 * H0 ** 2 / (8 * math.pi * G)
OG = math.pi ** 2 / 15 * (KB * T0) ** 4 / (HBAR ** 3 * C ** 3) / C ** 2 / rho_c
OR = OG * (1 + 7 / 8 * (4 / 11) ** (4 / 3) * NEFF)
OL = 1 - OM - OR
OB = OBH2 / H_ ** 2

def hz(z):
    return H0 * math.sqrt(OR * (1 + z) ** 4 + OM * (1 + z) ** 3 + OL)

def simpson(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3

def gauss_legendre(n):
    xs, ws = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, x
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
            dp = n * (x * p1 - p0) / (x * x - 1)
            dx = p1 / dp
            x -= dx
            if abs(dx) < 1e-15:
                break
        p0, p1 = 1.0, x
        for k in range(2, n + 1):
            p0, p1 = p1, ((2 * k - 1) * x * p1 - (k - 1) * p0) / k
        dp = n * (x * p1 - p0) / (x * x - 1)
        xs.append(x); ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws

def legendre_all(x, lmax):
    out = [1.0, x]
    for l in range(2, lmax + 1):
        out.append(((2 * l - 1) * x * out[-1] - (l - 1) * out[-2]) / l)
    return out

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    zs = 1090.0
    dm = simpson(lambda x: C / hz(math.exp(x) - 1) * math.exp(x), 0, math.log(1 + zs), 20000) / MPC
    def cs(z):
        r = 3 * OB / (4 * OG) / (1 + z)
        return C / math.sqrt(3 * (1 + r))
    rs = simpson(lambda x: cs(math.exp(x) - 1) / hz(math.exp(x) - 1) * math.exp(x), math.log(1 + zs), math.log(1e10), 40000) / MPC
    th = rs / dm
    la = math.pi / th
    print(f"Omega_b = {OB:.5f} ; R(z*) = {3 * OB / (4 * OG) / (1 + zs):.4f} ; D_M(z*) = {dm:.1f} Mpc ; r_s(z*) = {rs:.2f} Mpc")
    print(f"100 theta_* = {100 * th:.4f} (Planck 2018 VI: 1.0411 +- 0.0003) ; diferencia relativa = {(100 * th / 1.0411 - 1) * 100:+.2f} % ; l_A = pi/theta_* = {la:.1f}")
    assert abs(100 * th / 1.0411 - 1) < 0.01
    # espectro de juguete: D_l = l(l+1)C_l/2pi = 1 + 3 cos^2(pi l / l_A), con picos en l = n l_A
    lmax = 700
    def cl(l):
        d = 1.0 + 3.0 * math.cos(math.pi * l / la) ** 2
        return 2 * math.pi * d / (l * (l + 1)) if l >= 2 else 0.0
    cls = [cl(l) for l in range(lmax + 1)]
    xs, ws = gauss_legendre(800)
    cth = []
    for x in xs:
        p = legendre_all(x, lmax)
        cth.append(sum((2 * l + 1) / (4 * math.pi) * cls[l] * p[l] for l in range(2, lmax + 1)))
    err = 0.0
    # recuperacion eficiente: acumular los P_l una vez por nodo
    rec = [0.0] * (lmax + 1)
    for x, w, c in zip(xs, ws, cth):
        p = legendre_all(x, lmax)
        for l in range(2, lmax + 1):
            rec[l] += 2 * math.pi * w * c * p[l]
    for l in range(2, lmax + 1):
        err = max(err, abs(rec[l] - cls[l]) / cls[l])
    print(f"{'l':>5} {'C_l entrada':>13} {'C_l recuperado':>15} {'D_l = l(l+1)C_l/2pi':>20}")
    for l in (2, 10, 100, 302, 450, 604, 700):
        print(f"{l:5d} {cls[l]:13.6e} {rec[l]:15.6e} {l * (l + 1) * cls[l] / 2 / math.pi:20.4f}")
    d = [l * (l + 1) * cls[l] / 2 / math.pi for l in range(lmax + 1)]
    picos = [l for l in range(3, lmax) if d[l] > d[l - 1] and d[l] > d[l + 1]]
    print(f"picos del espectro de juguete en l = {picos} (esperado n l_A = {la:.0f}, {2 * la:.0f}); maximo error relativo de la ida y vuelta = {err:.2e}")
    assert err < 1e-9
    assert abs(picos[0] - la) < 2 and abs(picos[1] - 2 * la) < 3
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
