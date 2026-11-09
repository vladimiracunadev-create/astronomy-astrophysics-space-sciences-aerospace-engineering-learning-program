#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B40-C01: inflacion con un campo escalar V = m^2 phi^2 / 2, e-pliegues y aproximacion de rodadura lenta.

Datos: ninguna constante fisica. El potencial cuadratico, la condicion inicial phi_i = 16 M_pl y la masa (que solo fija la escala del tiempo: se toma m = 1) son
ILUSTRATIVOS. Unidades: M_pl (masa de Planck reducida) = 1, tiempo en unidades de 1/m, phi en unidades de M_pl.
Modelo: phi'' + 3 H phi' + phi = 0, 3 H^2 = phi'^2/2 + phi^2/2, integrado con Runge-Kutta de cuarto orden (paso 0,005); el numero de e-pliegues es N = integral de H dt hasta
epsilon = phi'^2 / (2 H^2) = 1. Se compara con la rodadura lenta N = (phi_i^2 - phi_e^2)/4 con phi_e = sqrt(2).
Supuestos: universo plano, un solo campo, sin radiacion ni materia. Validez: ilustrativa; no es un modelo ajustado a datos.
Tolerancia: N numerico frente a la rodadura lenta, 1,5 e-pliegues (la rodadura lenta pierde exactitud al final); Hdot = -phi'^2/2 a 1e-6 relativo.
"""
from __future__ import annotations
import math, platform, sys

def hubble(p, v):
    return math.sqrt((0.5 * v * v + 0.5 * p * p) / 3.0)

def deriv(s):
    p, v, n = s
    h = hubble(p, v)
    return (v, -3 * h * v - p, h)

def rk4(s, dt):
    k1 = deriv(s)
    k2 = deriv(tuple(a + 0.5 * dt * b for a, b in zip(s, k1)))
    k3 = deriv(tuple(a + 0.5 * dt * b for a, b in zip(s, k2)))
    k4 = deriv(tuple(a + dt * b for a, b in zip(s, k3)))
    return tuple(a + dt / 6 * (b + 2 * c + 2 * d + e) for a, b, c, d, e in zip(s, k1, k2, k3, k4))

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    phi_i = 16.0
    h0 = hubble(phi_i, 0.0)
    v0 = -phi_i / (3 * h0)              # rodadura lenta: 3 H phi' = -V'
    s = (phi_i, v0, 0.0)
    dt = 0.005
    t = 0.0
    marcas = {10: None, 20: None, 40: None, 60: None}
    h_prev = hubble(s[0], s[1])
    max_err_hdot = 0.0
    eps = 0.0
    while True:
        s2 = rk4(s, dt)
        h1 = hubble(s2[0], s2[1])
        hdot_num = (h1 - h_prev) / dt
        hdot_teo = -0.5 * (0.5 * (s[1] + s2[1])) ** 2
        if t > 1.0 and t < 15:
            max_err_hdot = max(max_err_hdot, abs(hdot_num - hdot_teo) / abs(hdot_teo))
        for k in marcas:
            if marcas[k] is None and s2[2] >= k:
                marcas[k] = (s2[0], t + dt)
        s = s2; h_prev = h1; t += dt
        eps = s[1] ** 2 / (2 * h1 ** 2)
        if eps >= 1.0:
            break
    n_tot = s[2]
    phi_e = s[0]
    n_sr = (phi_i ** 2 - 2.0) / 4.0
    print(f"{'N transcurrido':>16} {'phi [M_pl]':>12} {'t [1/m]':>10} {'phi rod. lenta':>16}")
    for k, (p, tt) in marcas.items():
        p_sr = math.sqrt(phi_i ** 2 - 4 * k)
        print(f"{k:16d} {p:12.4f} {tt:10.3f} {p_sr:16.4f}")
        assert abs(p - p_sr) < (0.05 if k <= 40 else 0.3)
    print(f"fin de la inflacion (epsilon = 1): phi_e = {phi_e:.4f} M_pl, t = {t:.3f}/m")
    print(f"e-pliegues numericos N = {n_tot:.3f} ; rodadura lenta (phi_i^2 - 2)/4 = {n_sr:.3f} ; diferencia = {n_tot - n_sr:+.3f}")
    # observables de rodadura lenta para N restantes
    for nn in (50, 60):
        ns = 1 - 2.0 / nn; r = 8.0 / nn
        print(f"N = {nn}: n_s = 1 - 2/N = {ns:.4f}, r = 8/N = {r:.4f}")
    print(f"max |Hdot_num - Hdot_teo| / |Hdot_teo| = {max_err_hdot:.2e}")
    assert abs(n_tot - n_sr) < 1.5
    assert abs(phi_e - math.sqrt(2)) < 0.5
    assert max_err_hdot < 1e-6
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
