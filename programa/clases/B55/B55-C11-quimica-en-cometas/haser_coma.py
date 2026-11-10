#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C11: modelo de Haser de una coma cometaria SINTETICA (molecula padre y fragmento hijo).

Datos: SINTETICOS / ILUSTRATIVOS. Produccion Q = 1.0e28 moleculas s-1, velocidad de expansion v = 0.5 km s-1, vida del padre 1.0e5 s y del hijo 1.0e6 s
(a la distancia heliocentrica ilustrativa del ejemplo). Ningun valor procede de una medicion. Rubin et al. (2019) se consulto solo por su resumen (inventario de elementos y
moleculas de 67P a partir de ROSINA); no se usaron cifras suyas.
Modelo: n_p(r) = Q / (4 pi v r^2) exp(-r / lp) ; n_h(r) = Q / (4 pi v r^2) * lh / (lp - lh) * [exp(-r/lp) - exp(-r/lh)], con lp = v tau_p, lh = v tau_h.
Densidad de columna a distancia proyectada rho: N(rho) = 2 integral_0^inf n(sqrt(rho^2 + z^2)) dz (regla del trapecio en una malla adaptada).
Supuestos: expansion esferica estacionaria y constante; sin colisiones ni gravedad. Validez: ilustrativa, coma exterior.
Tolerancia: N(rho) sin decaimiento vs Q / (4 v rho) a 1e-3 relativo; numero total de padres vs Q tau_p a 1e-3.
"""
from __future__ import annotations
import math, platform

Q = 1.0e28           # s-1
V = 0.5e5            # cm s-1  (0.5 km s-1)
TAU_P, TAU_H = 1.0e5, 1.0e6   # s
LP, LH = V * TAU_P, V * TAU_H  # cm

def n_p(r):
    return Q / (4 * math.pi * V * r * r) * math.exp(-r / LP)

def n_h(r):
    return Q / (4 * math.pi * V * r * r) * LH / (LP - LH) * (math.exp(-r / LP) - math.exp(-r / LH))

def columna(f, rho, zmax_factor=60.0, n=400000):
    """N(rho) = 2 int_0^zmax f(sqrt(rho^2+z^2)) dz con malla en sinh (mas fina cerca de z=0)."""
    zmax = zmax_factor * max(LH, rho)
    u_max = math.asinh(zmax / rho)
    h = u_max / n
    s = 0.0
    for i in range(n + 1):
        u = i * h
        z = rho * math.sinh(u)
        w = 0.5 if i in (0, n) else 1.0
        s += w * f(math.hypot(rho, z)) * rho * math.cosh(u)
    return 2.0 * s * h

def total(f, r1=1.0e5, r2=None, n=200000):
    """numero total de moleculas = int 4 pi r^2 f dr (malla logaritmica)."""
    r2 = r2 or 80 * LH
    a, b = math.log(r1), math.log(r2)
    h = (b - a) / n
    s = 0.0
    for i in range(n + 1):
        r = math.exp(a + i * h)
        w = 0.5 if i in (0, n) else 1.0
        s += w * 4 * math.pi * r ** 3 * f(r)
    return s * h

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"A. Coma SINTETICA: Q = 1e28 s-1 ; v = 0.5 km/s ; vida del padre 1e5 s ; vida del hijo 1e6 s ; escalas l_p = {LP:.3e} cm, l_h = {LH:.3e} cm")
    # prueba sin decaimiento: n = Q/(4 pi v r^2)  =>  N(rho) = Q/(4 v rho)
    sin_dec = lambda r: Q / (4 * math.pi * V * r * r)
    print("B. Prueba analitica sin decaimiento: N(rho) numerico frente a Q/(4 v rho)")
    for rho in (1.0e7, 1.0e8):
        zmax_f = 1.0e4
        # columna con zmax = zmax_f * rho
        u_max = math.asinh(zmax_f)
        n = 200000
        h = u_max / n
        s = 0.0
        for i in range(n + 1):
            u = i * h
            z = rho * math.sinh(u)
            w = 0.5 if i in (0, n) else 1.0
            s += w * sin_dec(math.hypot(rho, z)) * rho * math.cosh(u)
        num = 2.0 * s * h
        ana = Q / (4 * V * rho)
        # la cola truncada vale 2*Q/(4 pi v) * (1/(zmax)) aprox: se compensa en la comparacion
        cola = 2.0 * Q / (4 * math.pi * V) / (zmax_f * rho)
        err = abs(num + cola - ana) / ana
        print(f"   rho = {rho:.1e} cm : N numerica (+cola) = {num + cola:.6e} cm-2 ; analitica = {ana:.6e} cm-2 ; error relativo = {err:.2e}")
        assert err < 1e-3
    # numero total de padres
    Np = total(n_p)
    Np_ana = Q * TAU_P
    e1 = abs(Np - Np_ana) / Np_ana
    Nh = total(n_h)
    Nh_ana = Q * TAU_H * 1.0      # el hijo se produce a razon Q y vive tau_h : N_h = Q tau_h (si todo padre produce un hijo)
    e2 = abs(Nh - Nh_ana) / Nh_ana
    print(f"C. Numero total de padres = {Np:.4e} ; Q tau_p = {Np_ana:.4e} ; error = {e1:.2e}")
    print(f"   Numero total de hijos  = {Nh:.4e} ; Q tau_h = {Nh_ana:.4e} ; error = {e2:.2e}")
    assert e1 < 1e-3
    assert e2 < 1e-2
    print("D. Densidad de columna N(rho) de padre e hijo [cm-2] (coma SINTETICA)")
    print("rho [km]    N_padre        N_hijo         N_hijo/N_padre")
    for rho_km in (1.0e2, 1.0e3, 1.0e4, 1.0e5):
        rho = rho_km * 1e5
        npad = columna(n_p, rho)
        nhij = columna(n_h, rho)
        print(f"{rho_km:8.0e}   {npad:.4e}   {nhij:.4e}   {nhij / npad:.4e}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
