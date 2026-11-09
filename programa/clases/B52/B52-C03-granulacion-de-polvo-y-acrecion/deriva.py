#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B52-C03: numero de Stokes, deriva radial y crecimiento del polvo en un disco sintetico.

Datos consultados el 2026-11-09: G, k_B y m_p de NIST (CODATA 2022); (GM)_sol nominal de la IAU 2015 (Resolucion B3).
La unidad astronomica (1.495978707e11 m) NO se consulto en esta sesion.
Datos ILUSTRATIVOS (sinteticos): disco de la clase B52-C02 (Sigma = 1e4 kg/m^2 (r/ua)^-1.5, T = 280 K (r/ua)^-0.5, mu = 2.3);
granos compactos de densidad 1000 kg/m^3; razon polvo/gas Z = 0.01; velocidad relativa de colision constante dv = 10 m/s.
La formula de la deriva v_r = -2 St eta v_K/(1+St^2) y la ley de Epstein St = pi a rho_s/(2 Sigma) NO se consultaron en una fuente
(se verifican aqui contra la ecuacion de movimiento).
Sistema de referencia: plano medio, simetria axial; unidades SI.
Via 1: v_r de la formula. Via 2: estado estacionario de las ecuaciones locales (de Hill) de una particula con arrastre, integradas con RK4 (no usa la formula cerrada).
Tolerancias: formula frente a ecuaciones 1e-3 relativo; deriva acoplada: cambio de paso (h y h/2) menor de 1e-6 relativo.
"""
from __future__ import annotations
import math, platform

G = 6.67430e-11
K_B = 1.380649e-23
M_P = 1.67262192595e-27
GM = 1.3271244e20
UA = 1.495978707e11
ANIO = 365.25 * 86400.0
MU, S1, P, T1 = 2.3, 1.0e4, 1.5, 280.0
RHO_S, Z, DV = 1000.0, 0.01, 10.0


def sigma(x): return S1 * x ** (-P)
def temp(x): return T1 * x ** (-0.5)
def cs(x): return math.sqrt(K_B * temp(x) / (MU * M_P))
def omega(x): return math.sqrt(GM / (x * UA) ** 3)
def vk(x): return math.sqrt(GM / (x * UA))
def hr(x): return cs(x) / omega(x) / (x * UA)
def rho_gas(x): return sigma(x) / (math.sqrt(2 * math.pi) * cs(x) / omega(x))


DLNP = -P - 0.25 - 1.5   # d ln P / d ln r con P ~ Sigma c_s Omega (Sigma ~ r^-1.5, c_s ~ r^-0.25, Omega ~ r^-1.5)


def eta(x):
    return -0.5 * hr(x) ** 2 * DLNP


def stokes(a, x):
    return math.pi * a * RHO_S / (2.0 * sigma(x))


def vr_formula(st, x):
    return -2.0 * st * eta(x) * vk(x) / (1.0 + st * st)


def vr_ecuaciones(st, x):
    """Estado estacionario de las ecuaciones locales (de Hill) de una particula con arrastre, integradas con RK4.
    Variables: v_r y D = v_phi - v_K. d v_r/dt = 2 Omega D - v_r/t_s ; dD/dt = -(Omega/2) v_r - (D - D_gas)/t_s, con D_gas = -eta v_K."""
    om = omega(x)
    ts = st / om
    dg = -eta(x) * vk(x)
    f = lambda y: [2.0 * om * y[1] - y[0] / ts, -0.5 * om * y[0] - (y[1] - dg) / ts]
    y = [0.0, 0.0]
    h = min(ts, 1.0 / om) * 0.02
    t = 0.0
    tfin = 60.0 * max(ts, 1.0 / om)
    while t < tfin:
        k1 = f(y)
        k2 = f([y[0] + 0.5 * h * k1[0], y[1] + 0.5 * h * k1[1]])
        k3 = f([y[0] + 0.5 * h * k2[0], y[1] + 0.5 * h * k2[1]])
        k4 = f([y[0] + h * k3[0], y[1] + h * k3[1]])
        y = [y[0] + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), y[1] + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])]
        t += h
    return y[0]


def deriva_acoplada(a0, x0, t_fin, n):
    """Integra (ln r, a): d r/dt = v_r(St), da/dt = rho_d dv/(4 rho_s), con paso fijo (RK4) y n pasos."""
    def f(y):
        lx, a = y
        x = math.exp(lx)
        st = stokes(a, x)
        return [vr_formula(st, x) / (x * UA), Z * rho_gas(x) * DV / (4.0 * RHO_S)]
    y = [math.log(x0), a0]
    h = t_fin / n
    for _ in range(n):
        k1 = f(y)
        k2 = f([y[0] + 0.5 * h * k1[0], y[1] + 0.5 * h * k1[1]])
        k3 = f([y[0] + 0.5 * h * k2[0], y[1] + 0.5 * h * k2[1]])
        k4 = f([y[0] + h * k3[0], y[1] + h * k3[1]])
        y = [y[0] + h / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]), y[1] + h / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])]
    return math.exp(y[0]), y[1]


def tiempo_de_deriva(a, x0, x1, n=4000):
    """Tiempo para ir de x0 a x1 con tamano fijo a (integral de dr / |v_r|, regla del punto medio en ln r)."""
    a_, b_ = math.log(x1), math.log(x0)
    h = (b_ - a_) / n
    s = 0.0
    for i in range(n):
        x = math.exp(a_ + (i + 0.5) * h)
        s += h * x * UA / abs(vr_formula(stokes(a, x), x))
    return s


def calcular():
    x = 5.0
    filas = []
    for st in (1e-3, 1e-2, 0.1, 1.0, 10.0):
        vf, ve = vr_formula(st, x), vr_ecuaciones(st, x)
        filas.append((st, vf, ve))
    t_deriva = tiempo_de_deriva(0.01, 30.0, 1.0)
    t_fin = 2.0e3 * ANIO
    r1, a1 = deriva_acoplada(1e-4, 30.0, t_fin, 400)
    r2, a2 = deriva_acoplada(1e-4, 30.0, t_fin, 800)
    return dict(x=x, eta=eta(x), filas=filas, t_deriva=t_deriva, r1=r1, a1=a1, r2=r2, a2=a2, t_fin=t_fin,
                st30=stokes(0.01, 30.0), st1=stokes(0.01, 1.0), vmax=eta(x) * vk(x))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Disco sintetico de B52-C02; r = {r['x']:.0f} ua: eta = {r['eta']:.3e} ; v_K = {vk(r['x']):.0f} m/s ; eta v_K = {r['vmax']:.2f} m/s")
    print(f"{'St':>8} {'v_r formula [m/s]':>20} {'v_r ecuaciones [m/s]':>22} {'dif. rel.':>10}")
    for st, vf, ve in r["filas"]:
        print(f"{st:8.0e} {vf:20.5f} {ve:22.5f} {abs(ve / vf - 1):10.2e}")
    print(f"Grano de 1 cm: St = {r['st30']:.3f} a 30 ua y {r['st1']:.5f} a 1 ua ; tiempo de deriva de 30 a 1 ua (tamano fijo) = {r['t_deriva'] / ANIO:.0f} anios")
    print(f"Deriva acoplada con crecimiento (a0 = 0.1 mm, 30 ua, {r['t_fin'] / ANIO:.0f} anios): paso h -> r = {r['r1']:.6f} ua, a = {r['a1'] * 100:.5f} cm ; paso h/2 -> r = {r['r2']:.6f} ua, a = {r['a2'] * 100:.5f} cm")
    for st, vf, ve in r["filas"]:
        assert abs(ve / vf - 1) < 1e-3, (st, vf, ve)
    assert abs(r["r1"] / r["r2"] - 1) < 1e-6 and abs(r["a1"] / r["a2"] - 1) < 1e-6
    assert r["filas"][3][1] < 0 and abs(abs(r["filas"][3][1]) - r["vmax"]) / r["vmax"] < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
