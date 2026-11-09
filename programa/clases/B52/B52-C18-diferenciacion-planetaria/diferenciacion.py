#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C18: calor radiactivo de un cuerpo en regimen adiabatico y energia gravitatoria liberada al diferenciarse.

Datos consultados el 2026-11-09: G, la constante de masa atomica u = 1.66053906892e-27 kg y el electronvoltio 1.602176634e-19 J de NIST (CODATA 2022);
(GM)_Tierra y radio ecuatorial terrestre 6.3781e6 m nominales de la IAU 2015 (Resolucion B3).
Datos ILUSTRATIVOS (sinteticos, NO consultados): vida media del 26Al 0.717 Ma, energia por decaimiento 3.12 MeV, razon inicial 26Al/27Al = 5e-5,
fraccion en masa de Al 0.01, calor especifico 1000 J/(kg K); densidades del modelo de dos capas: nucleo 11000 kg/m^3 y manto 4500 kg/m^3.
Sistema de referencia: cuerpo esferico de simetria radial (Tierra-like: masa e radio de la IAU, el radio es el ecuatorial); SI.
Parte A (calor): dT/dt = H0 exp(-lambda t)/c (sin perdidas: cota superior). Analitica T = T0 + H0/(lambda c)(1 - exp(-lambda t)) frente a RK4.
Parte B (energia): U de un cuerpo homogeneo -3GM^2/(5R) y de un cuerpo de dos capas con la misma masa y radio: cierre analitico frente a integracion de Simpson de -G m(r) dm / r.
Tolerancias: ODE 1e-9 relativo; energia 1e-6 relativo.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
U_KG = 1.66053906892e-27
EV = 1.602176634e-19
GM_T, R_T = 3.986004e14, 6.3781e6
M_T = GM_T / G
T_MEDIA, E_DEC, RAZON, X_AL, CP = 0.717e6 * 365.25 * 86400.0, 3.12e6 * EV, 5e-5, 0.01, 1000.0
LAMBDA = math.log(2.0) / T_MEDIA
RHO_C, RHO_M = 11000.0, 4500.0


def h0():
    n27 = X_AL / (27.0 * U_KG)
    return RAZON * n27 * LAMBDA * E_DEC  # W/kg


def delta_t(t):
    return h0() / (LAMBDA * CP) * (1.0 - math.exp(-LAMBDA * t))


def rk4_t(t_fin, n=2000):
    f = lambda t, T: h0() * math.exp(-LAMBDA * t) / CP
    T, t, h = 0.0, 0.0, t_fin / n
    for _ in range(n):
        k1 = f(t, T); k2 = f(t + h / 2, T + h / 2 * k1); k3 = f(t + h / 2, T + h / 2 * k2); k4 = f(t + h, T + h * k3)
        T += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        t += h
    return T


def radio_nucleo():
    rho_bar = M_T / (4.0 / 3.0 * math.pi * R_T ** 3)
    return R_T * ((rho_bar - RHO_M) / (RHO_C - RHO_M)) ** (1.0 / 3.0), rho_bar


def u_dos_capas_analitica(rc):
    d = RHO_C - RHO_M
    interior = -(16 * math.pi ** 2 * G / 15) * RHO_C ** 2 * rc ** 5
    exterior = -(16 * math.pi ** 2 * G / 3) * RHO_M * (RHO_M * (R_T ** 5 - rc ** 5) / 5 + d * rc ** 3 * (R_T ** 2 - rc ** 2) / 2)
    return interior + exterior


def u_numerica(rc, n=200000):
    rho = lambda r: RHO_C if r < rc else RHO_M
    # masa acumulada por integracion exacta por tramos de Simpson sobre r (n par)
    h = R_T / n
    def masa(r):
        if r <= rc:
            return 4.0 / 3.0 * math.pi * RHO_C * r ** 3
        return 4.0 / 3.0 * math.pi * (RHO_C * rc ** 3 + RHO_M * (r ** 3 - rc ** 3))
    f = lambda r: 0.0 if r == 0 else -G * masa(r) * 4.0 * math.pi * rho(r) * r
    # integral por tramos para respetar la discontinuidad en rc
    def simpson(a, b, m):
        hh = (b - a) / m
        s = f(a) + f(b)
        for i in range(1, m):
            s += (4 if i % 2 else 2) * f(a + i * hh)
        return s * hh / 3.0
    # evitar rho discontinuo en los extremos: se evalua el interior con rho_c y el exterior con rho_m
    fi = lambda r: 0.0 if r == 0 else -G * masa(r) * 4.0 * math.pi * RHO_C * r
    fe = lambda r: -G * masa(r) * 4.0 * math.pi * RHO_M * r
    def simp(fun, a, b, m):
        hh = (b - a) / m
        s = fun(a) + fun(b)
        for i in range(1, m):
            s += (4 if i % 2 else 2) * fun(a + i * hh)
        return s * hh / 3.0
    return simp(fi, 0.0, rc, n // 2) + simp(fe, rc, R_T, n // 2)


def calcular():
    t_total = 10 * T_MEDIA
    rc, rho_bar = radio_nucleo()
    u_hom = -3.0 * G * M_T ** 2 / (5.0 * R_T)
    u_an = u_dos_capas_analitica(rc)
    u_num = u_numerica(rc)
    return dict(h0=h0(), dT_an=delta_t(t_total), dT_num=rk4_t(t_total), dT_inf=h0() / (LAMBDA * CP), frac1=delta_t(T_MEDIA) / delta_t(t_total), rc=rc, rho_bar=rho_bar,
                u_hom=u_hom, u_an=u_an, u_num=u_num, du=u_hom - u_an, dT_grav=(u_hom - u_an) / (M_T * CP))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Parte A (ilustrativa): H0 = {r['h0']:.3e} W/kg ; aumento adiabatico maximo H0/(lambda c) = {r['dT_inf']:.0f} K")
    print(f"  tras 10 vidas medias: analitico = {r['dT_an']:.3f} K ; RK4 = {r['dT_num']:.3f} K ; dif. rel. = {abs(r['dT_num'] / r['dT_an'] - 1):.1e}")
    print(f"  fraccion del calor liberada en una vida media = {r['frac1']:.4f}")
    print(f"Parte B: cuerpo con M = {M_T:.4e} kg y R = {R_T / 1e3:.1f} km ; densidad media = {r['rho_bar']:.1f} kg/m^3 ; radio del nucleo = {r['rc'] / 1e3:.1f} km ({r['rc'] / R_T:.3f} R)")
    print(f"  U homogeneo = {r['u_hom']:.4e} J ; U dos capas analitica = {r['u_an']:.4e} J ; Simpson = {r['u_num']:.4e} J ; dif. rel. = {abs(r['u_num'] / r['u_an'] - 1):.1e}")
    print(f"  energia liberada por la diferenciacion = {-(r['u_an'] - r['u_hom']):.4e} J ; calentamiento medio si todo fuera calor = {r['dT_grav']:.0f} K")
    assert abs(r["dT_num"] / r["dT_an"] - 1) < 1e-9
    assert abs(r["u_num"] / r["u_an"] - 1) < 1e-6
    assert r["u_an"] < r["u_hom"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
