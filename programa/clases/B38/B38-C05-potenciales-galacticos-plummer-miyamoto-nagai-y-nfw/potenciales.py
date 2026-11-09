#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B38-C05: potenciales de Plummer, Miyamoto-Nagai y NFW; velocidad circular, masa encerrada y una orbita.

Datos: GM_sol = 1,3271244e20 m^3/s^2 (UAI, Resolucion B3 de 2015, consultada el 2026-11-09) y 1 kpc = 3,0856775814913673e19 m (648000/pi au con la au exacta; definicion de la UAI NO consultada); de ahi G = 4,30091e-6 kpc (km/s)^2 / Msol.
Los parametros del modelo (disco M = 6e10 Msol, a = 3 kpc, b = 0,28 kpc; bulbo de Plummer M = 1e10 Msol, b = 0,7 kpc; halo NFW rho0 = 8,5e6 Msol/kpc^3, rs = 16 kpc) son ILUSTRATIVOS
(sinteticos) y NO son un ajuste a la Via Lactea. De Navarro, Frenk y White (1996) solo se leyo el resumen (consultado el 2026-11-09).
Modelo: Phi_P = -GM/sqrt(r^2+b^2); Phi_MN = -GM/sqrt(R^2+(a+sqrt(z^2+b^2))^2); Phi_NFW = -4 pi G rho0 rs^3 ln(1+r/rs)/r; M_NFW(<r) = 4 pi rho0 rs^3 [ln(1+x) - x/(1+x)].
Verificacion por dos vias: aceleracion analitica frente a gradiente numerico; densidad de Poisson (Laplaciano numerico) frente a la densidad analitica; leapfrog con conservacion de energia y momento angular.
Supuestos: potencial estatico y axisimetrico. Validez: ilustrativa.
Tolerancia: gradientes a 1e-6 relativo; Laplaciano a 1e-4 relativo; error relativo de energia menor que 1e-4 y de L_z menor que 1e-9 en 1 Gyr.
"""
from __future__ import annotations
import math, platform, sys

KPC = 3.0856775814913673e19
GMSOL = 1.3271244e20
G = GMSOL / KPC / 1e6  # kpc (km/s)^2 / Msol

M_D, A_D, B_D = 6.0e10, 3.0, 0.28
M_B, B_B = 1.0e10, 0.7
RHO0, RS = 8.5e6, 16.0

def phi_plummer(r, m, b):
    return -G * m / math.sqrt(r * r + b * b)

def phi_mn(R, z, m, a, b):
    return -G * m / math.sqrt(R * R + (a + math.sqrt(z * z + b * b)) ** 2)

def phi_nfw(r, rho0, rs):
    return -4 * math.pi * G * rho0 * rs ** 3 * math.log(1 + r / rs) / r

def phi_tot(R, z):
    r = math.sqrt(R * R + z * z)
    return phi_plummer(r, M_B, B_B) + phi_mn(R, z, M_D, A_D, B_D) + phi_nfw(r, RHO0, RS)

def grad(R, z, h=1e-5):
    gR = (phi_tot(R + h, z) - phi_tot(R - h, z)) / (2 * h)
    gz = (phi_tot(R, z + h) - phi_tot(R, z - h)) / (2 * h)
    return gR, gz

def acc_analitica(R, z):
    r = math.sqrt(R * R + z * z)
    # Plummer
    f_b = G * M_B / (r * r + B_B ** 2) ** 1.5
    # Miyamoto-Nagai
    zb = math.sqrt(z * z + B_D ** 2)
    d = (R * R + (A_D + zb) ** 2) ** 1.5
    aR_d = G * M_D * R / d
    az_d = G * M_D * z * (A_D + zb) / (zb * d)
    # NFW: a = G M(<r)/r^2 hacia el centro
    x = r / RS
    m = 4 * math.pi * RHO0 * RS ** 3 * (math.log(1 + x) - x / (1 + x))
    f_h = G * m / r ** 3
    return (f_b * R + aR_d + f_h * R, f_b * z + az_d + f_h * z)

def vcirc(R):
    aR, _ = acc_analitica(R, 0.0)
    return math.sqrt(R * aR)

def laplaciano_esf(phi, r, h=1e-3):
    return (phi(r + h) - 2 * phi(r) + phi(r - h)) / h ** 2 + 2 / r * (phi(r + h) - phi(r - h)) / (2 * h)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"G = {G:.5e} kpc (km/s)^2 / Msol")
    assert abs(G - 4.30091e-6) / 4.30091e-6 < 1e-5
    print(f"{'R [kpc]':>8} {'v_c [km/s]':>11} {'disco':>7} {'bulbo':>7} {'halo':>7}")
    for R in (2, 4, 8, 12, 20, 40):
        r = float(R)
        vb = math.sqrt(G * M_B * r * r / (r * r + B_B ** 2) ** 1.5)
        vd = math.sqrt(G * M_D * r * r / (r * r + (A_D + B_D) ** 2) ** 1.5)
        x = r / RS
        vh = math.sqrt(G * 4 * math.pi * RHO0 * RS ** 3 * (math.log(1 + x) - x / (1 + x)) / r)
        print(f"{R:8d} {vcirc(r):11.2f} {vd:7.1f} {vb:7.1f} {vh:7.1f}")
        assert abs(vcirc(r) ** 2 - vb ** 2 - vd ** 2 - vh ** 2) < 1e-6 * vcirc(r) ** 2
    # gradiente numerico
    peor = 0.0
    for R, z in ((1.0, 0.3), (8.0, 0.0), (8.0, 1.0), (20.0, 5.0)):
        ga = acc_analitica(R, z)
        gn = grad(R, z)
        norma = math.hypot(*ga)
        for x, y in zip(ga, gn):
            peor = max(peor, abs(x - y) / norma)  # las funciones devuelven la magnitud hacia el centro = +grad
    print(f"aceleracion analitica frente a gradiente numerico: diferencia relativa maxima {peor:.2e}")
    assert peor < 1e-6
    # Poisson: densidad Plummer y NFW
    for nombre, phi, rho in (
        ("Plummer", lambda r: phi_plummer(r, M_B, B_B), lambda r: 3 * M_B / (4 * math.pi * B_B ** 3) * (1 + r * r / B_B ** 2) ** -2.5),
        ("NFW", lambda r: phi_nfw(r, RHO0, RS), lambda r: RHO0 / ((r / RS) * (1 + r / RS) ** 2)),
    ):
        peor = 0.0
        for r in (0.5, 2.0, 10.0):
            lap = laplaciano_esf(phi, r)
            peor = max(peor, abs(lap - 4 * math.pi * G * rho(r)) / (4 * math.pi * G * rho(r)))
        print(f"ecuacion de Poisson, {nombre}: error relativo maximo {peor:.2e}")
        assert peor < 1e-4
    # masa encerrada NFW
    for x in (0.5, 1.0, 5.0):
        m = 4 * math.pi * RHO0 * RS ** 3 * (math.log(1 + x) - x / (1 + x))
        # integral numerica de 4 pi r^2 rho
        n = 200000
        r1 = x * RS
        s = 0.0
        for i in range(n):
            r = (i + 0.5) * r1 / n
            s += 4 * math.pi * r * r * RHO0 / ((r / RS) * (1 + r / RS) ** 2) * r1 / n
        assert abs(s - m) / m < 1e-5
    print("masa encerrada NFW: formula frente a integral numerica, acuerdo mejor que 1e-5")
    # orbita leapfrog
    kms_to_kpcgyr = 1e3 * 3.15576e16 / KPC
    R0, z0 = 8.0, 0.5
    vR, vphi, vz = 20.0, 0.9 * vcirc(8.0), 10.0
    x, y, z = R0, 0.0, z0
    vx, vy, vzz = vR, vphi, vz
    dt = 0.5e-3 * kms_to_kpcgyr  # 0,5 Myr en kpc/(km/s)
    # trabajamos en unidades kpc y km/s: tiempo en kpc/(km/s) = 977,8 Myr
    def acc(x, y, z):
        R = math.hypot(x, y)
        aR, az = acc_analitica(R, z)
        return -aR * x / R, -aR * y / R, -az
    def energia():
        R = math.hypot(x, y)
        return 0.5 * (vx * vx + vy * vy + vzz * vzz) + phi_tot(R, z)
    def lz():
        return x * vy - y * vx
    e0, l0 = energia(), lz()
    t_total = 1.0 * 1000.0 / 977.7922216807891  # 1 Gyr en kpc/(km/s)
    n = int(t_total / dt)
    ax, ay, az_ = acc(x, y, z)
    zmax = 0.0
    for _ in range(n):
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay; vzz += 0.5 * dt * az_
        x += dt * vx; y += dt * vy; z += dt * vzz
        ax, ay, az_ = acc(x, y, z)
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay; vzz += 0.5 * dt * az_
        zmax = max(zmax, abs(z))
    de = abs(energia() - e0) / abs(e0)
    dl = abs(lz() - l0) / abs(l0)
    print(f"orbita de 1 Gyr con {n} pasos: error de energia {de:.2e}, de L_z {dl:.2e}, |z|max {zmax:.2f} kpc")
    assert de < 1e-4 and dl < 1e-9
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
