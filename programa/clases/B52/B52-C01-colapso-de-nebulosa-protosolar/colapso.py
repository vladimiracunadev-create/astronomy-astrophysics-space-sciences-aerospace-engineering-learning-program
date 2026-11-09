#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C01: masa de Jeans, tiempo de caida libre y radio centrifugo de una nebulosa en colapso.

Datos consultados el 2026-11-09: G, k_B y m_p de NIST (CODATA 2022); (GM)_sol nominal de la IAU 2015 (Resolucion B3).
La unidad astronomica (1.495978707e11 m) NO se consulto en esta sesion: se usa solo para expresar resultados.
Datos ILUSTRATIVOS (sinteticos, no medidos): T = 10 K, mu = 2.33, M = 1 M_sol, R0 = 3000 ua, Omega = 5e-14 s^-1; la densidad sale de M y R0.
Sistema de referencia: inercial centrado en el centro de masa de la nube; unidades SI.
Modelo: esfera uniforme y isoterma. Jeans: M_J = (5kT/(G mu m_p))^(3/2) (3/(4 pi rho))^(1/2) (convencion de esfera uniforme).
Caida libre: t_ff = sqrt(3 pi / (32 G rho)); segunda via: integracion RK4 de r'' = -GM/r^2 con paso adaptativo.
Radio centrifugo: r_c = j^2/(GM), j = Omega R0^2; segunda via: integracion RK4 en 2D del periastro de la orbita.
Tolerancias: t_ff numerico frente al analitico 1e-4 relativo; periastro numerico frente al analitico 1e-3 relativo.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11          # NIST CODATA 2022
K_B = 1.380649e-23       # NIST (exacto)
M_P = 1.67262192595e-27  # NIST
GM_SOL = 1.3271244e20    # IAU 2015 B3, m^3 s^-2 (nominal)
UA = 1.495978707e11      # m (no consultada)
ANIO = 365.25 * 86400.0

T, MU = 10.0, 2.33
M_NUBE = GM_SOL / G
R0 = 3000.0 * UA
OMEGA = 5.0e-14


def masa_jeans(T, rho):
    cs2 = K_B * T / (MU * M_P)
    return (5.0 * cs2 / G) ** 1.5 * math.sqrt(3.0 / (4.0 * math.pi * rho))


def t_caida_libre_analitico(rho):
    return math.sqrt(3.0 * math.pi / (32.0 * G * rho))


def rk4(f, y, h):
    k1 = f(y)
    k2 = f([a + 0.5 * h * b for a, b in zip(y, k1)])
    k3 = f([a + 0.5 * h * b for a, b in zip(y, k2)])
    k4 = f([a + h * b for a, b in zip(y, k3)])
    return [a + h / 6.0 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(y, k1, k2, k3, k4)]


def t_caida_libre_numerico(gm, r0, fin=1e-4):
    f = lambda y: [y[1], -gm / y[0] ** 2]
    y, t = [r0, 0.0], 0.0
    while y[0] > fin * r0:
        h = 2e-3 * math.sqrt(y[0] ** 3 / gm)
        y = rk4(f, y, h)
        t += h
    return t


def periastro_numerico(gm, r0, v0):
    f = lambda y: [y[2], y[3], -gm * y[0] / (y[0] ** 2 + y[1] ** 2) ** 1.5, -gm * y[1] / (y[0] ** 2 + y[1] ** 2) ** 1.5]
    y, t, rmin = [r0, 0.0, 0.0, v0], 0.0, r0
    P = 2 * math.pi * math.sqrt((0.5 * r0) ** 3 / gm)
    while t < 1.2 * P / 2 + 0.0:
        r = math.hypot(y[0], y[1])
        h = 2e-3 * math.sqrt(r ** 3 / gm)
        y = rk4(f, y, h)
        t += h
        rmin = min(rmin, math.hypot(y[0], y[1]))
    return rmin


def calcular():
    rho_nube = 3.0 * M_NUBE / (4.0 * math.pi * R0 ** 3)
    mj = masa_jeans(T, rho_nube)
    n_equiv = rho_nube / (MU * M_P)
    tff = t_caida_libre_analitico(rho_nube)
    tff_num = t_caida_libre_numerico(GM_SOL, R0)
    j = OMEGA * R0 ** 2
    rc = j ** 2 / GM_SOL
    v0 = OMEGA * R0
    en = 0.5 * v0 ** 2 - GM_SOL / R0
    a = -GM_SOL / (2.0 * en)
    e = math.sqrt(max(0.0, 1.0 + 2.0 * en * j ** 2 / GM_SOL ** 2))
    q_an = a * (1.0 - e)
    q_num = periastro_numerico(GM_SOL, R0, v0)
    return dict(n_equiv=n_equiv, mj=mj, m_nube=M_NUBE, rho_nube=rho_nube, tff=tff, tff_num=tff_num, j=j, rc=rc, q_an=q_an, q_num=q_num, e=e,
                colapsa=M_NUBE > mj, cs=math.sqrt(K_B * T / (MU * M_P)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    ms = GM_SOL / G
    print(f"Datos ilustrativos: T = {T} K, mu = {MU}, M = {r['m_nube'] / ms:.3f} M_sol, R0 = {R0 / UA:.0f} ua, Omega = {OMEGA:.1e} s^-1")
    print(f"Velocidad del sonido isoterma c_s = {r['cs']:.1f} m/s")
    print(f"Densidad media de la nube = {r['rho_nube']:.3e} kg/m^3 (n = {r['n_equiv']:.2e} particulas/m^3) ; masa de Jeans = {r['mj'] / ms:.3f} M_sol")
    print(f"Cociente M/M_J = {r['m_nube'] / r['mj']:.2f} ; colapsa (M > M_J): {r['colapsa']}")
    print(f"Tiempo de caida libre: analitico = {r['tff'] / ANIO:.4f} anios ; RK4 = {r['tff_num'] / ANIO:.4f} anios ; dif. relativa = {abs(r['tff_num'] / r['tff'] - 1):.2e}")
    print(f"Momento angular especifico j = {r['j']:.3e} m^2/s ; radio centrifugo r_c = j^2/(GM) = {r['rc'] / UA:.2f} ua")
    print(f"Excentricidad de la orbita de caida e = {r['e']:.6f}")
    print(f"Periastro: analitico = {r['q_an'] / UA:.4f} ua ; RK4 = {r['q_num'] / UA:.4f} ua ; r_c/2 = {r['rc'] / 2 / UA:.4f} ua")
    assert r["colapsa"]
    assert abs(r["tff_num"] / r["tff"] - 1) < 1e-4
    assert abs(r["q_num"] / r["q_an"] - 1) < 1e-3
    assert abs(r["q_an"] / (r["rc"] / 2) - 1) < 1e-2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
