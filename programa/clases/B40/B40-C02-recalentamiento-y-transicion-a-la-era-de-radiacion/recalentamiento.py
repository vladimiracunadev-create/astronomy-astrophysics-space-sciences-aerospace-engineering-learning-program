#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C02: recalentamiento perturbativo, del inflaton oscilante a la radiacion.

Datos: ninguna constante fisica. La tasa de decaimiento Gamma = 0,01 m, la densidad inicial (H_0 = 0,3 m) y g* = 106,75 (valor tipico del modelo estandar de particulas,
usado aqui como numero ILUSTRATIVO) son supuestos. Unidades: M_pl reducida = 1, tiempo en 1/m.
Modelo: d(rho_phi)/dt = -(3H + Gamma) rho_phi ; d(rho_r)/dt = -4H rho_r + Gamma rho_phi ; 3H^2 = rho_phi + rho_r (un campo oscilante promedia w = 0).
Segunda via: rho_r a^4 = integral de Gamma rho_phi a^4 dt por cuadratura de los valores guardados. Estimacion analitica: 3 Gamma^2 = (pi^2/30) g* T_rh^4.
Supuestos: decaimiento perturbativo, sin resonancia parametrica ni termalizacion explicita. Validez: ilustrativa.
Tolerancia: las dos vias de rho_r a^4 a 1e-3 relativo; la densidad en la igualdad dentro de un factor 5 de 3 Gamma^2.
"""
from __future__ import annotations
import math, platform, sys

GAM = 0.01
GSTAR = 106.75

def deriv(s):
    rp, rr, a = s
    h = math.sqrt((rp + rr) / 3.0)
    return (-(3 * h + GAM) * rp, -4 * h * rr + GAM * rp, h * a)

def rk4(s, dt):
    k1 = deriv(s)
    k2 = deriv(tuple(x + 0.5 * dt * k for x, k in zip(s, k1)))
    k3 = deriv(tuple(x + 0.5 * dt * k for x, k in zip(s, k2)))
    k4 = deriv(tuple(x + dt * k for x, k in zip(s, k3)))
    return tuple(x + dt / 6 * (a + 2 * b + 2 * c + d) for x, a, b, c, d in zip(s, k1, k2, k3, k4))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    h0 = 0.3
    s = (3 * h0 * h0, 0.0, 1.0)
    dt = 0.01
    t = 0.0
    ts, pts = [0.0], [(s[0] * s[2] ** 4 * GAM)]
    t_eq = None
    t_hg = None
    rho_eq = None
    rr_max = (0.0, 0.0)
    rows = {}
    pasos = int(900 / dt)
    for i in range(pasos):
        s = rk4(s, dt)
        t += dt
        rp, rr, a = s
        h = math.sqrt((rp + rr) / 3)
        ts.append(t); pts.append(GAM * rp * a ** 4)
        if rr > rr_max[0]:
            rr_max = (rr, t)
        if t_hg is None and h <= GAM:
            t_hg = t; rows['H=Gamma'] = (t, rp, rr, a)
        if t_eq is None and rr >= rp:
            t_eq = t; rho_eq = rp + rr; rows['rho_r=rho_phi'] = (t, rp, rr, a)
        if i + 1 in (int(10 / dt), int(300 / dt), pasos):
            rows[f't={t:.0f}'] = (t, rp, rr, a)
    # segunda via: cuadratura trapezoidal de Gamma rho_phi a^4
    integral = 0.0
    for k in range(1, len(ts)):
        integral += 0.5 * (pts[k] + pts[k - 1]) * (ts[k] - ts[k - 1])
    rr_a4_rk = s[1] * s[2] ** 4
    rel = abs(rr_a4_rk - integral) / integral
    print(f"{'instante':>16} {'t [1/m]':>9} {'rho_phi':>11} {'rho_r':>11} {'a':>10}")
    for k, (tt, rp, rr, a) in rows.items():
        print(f"{k:>16} {tt:9.2f} {rp:11.3e} {rr:11.3e} {a:10.3e}")
    teo = 3 * GAM ** 2
    t_rh = (90 / (math.pi ** 2 * GSTAR)) ** 0.25 * math.sqrt(GAM)
    print(f"densidad total en la igualdad = {rho_eq:.3e} ; 3 Gamma^2 = {teo:.3e} ; cociente = {rho_eq / teo:.3f}")
    print(f"T_rh = (90/(pi^2 g*))^(1/4) sqrt(Gamma) = {t_rh:.4f} M_pl (con Gamma = 0,01 m; solo escala adimensional)")
    print(f"maximo de rho_r = {rr_max[0]:.3e} en t = {rr_max[1]:.2f}/m ; rho_r al final / rho_total = {s[1] / (s[0] + s[1]):.6f}")
    print(f"rho_r a^4: Runge-Kutta = {rr_a4_rk:.6e} ; cuadratura = {integral:.6e} ; error relativo = {rel:.2e}")
    assert rel < 1e-3
    assert 0.2 < rho_eq / teo < 5
    assert s[1] / (s[0] + s[1]) > 0.999
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
