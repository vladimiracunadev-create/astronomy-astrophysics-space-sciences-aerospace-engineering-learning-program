#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B75-C08: criterio de Tisserand para cadenas de sobrevuelos (orbitas coplanares, planetas en orbita circular).

Datos consultados (2026-11-10): semiejes de las fichas NASA/NSSDC (Venus 108.210e6, Tierra 149.598e6, Marte 227.956e6, Jupiter 778.479e6 km). GM_sol = 1.32712440e11 km3/s2 (estandar, no consultado).
ILUSTRATIVO: la orbita inicial es la elipse de Hohmann Tierra-Marte (C01) vista desde la Tierra; los v_inf elegidos de 2 a 6 km/s son del ejercicio.
Modelo: Tisserand T = a_p/a + 2 sqrt((a/a_p)(1 - e^2)) (a_p = semieje del planeta, orbitas coplanares) con T = 3 - (v_inf/V_p)^2 en el cruce con la orbita del planeta;
un sobrevuelo conserva v_inf y por tanto T (limite de conicas empalmadas, planeta en orbita circular).
Pruebas: (1) T calculado con (a, e) igual a 3 - (v_inf/V_p)^2 con v_inf desde los vectores (tol. 1e-9); (2) T se conserva tras 200 sobrevuelos de giro aleatorio con semilla fija (tol. 1e-9).
"""
import math, platform, random
MU = 1.32712440e11
AU = 149597870.7
A = {"Venus": 108.210e6, "Tierra": 149.598e6, "Marte": 227.956e6, "Jupiter": 778.479e6}


def tisserand(a, e, ap):
    return ap / a + 2 * math.sqrt(a / ap * (1 - e * e))


def elem(r, v):
    rn = math.hypot(*r); v2 = v[0] ** 2 + v[1] ** 2
    eps = 0.5 * v2 - MU / rn
    a = -MU / (2 * eps)
    h = r[0] * v[1] - r[1] * v[0]
    e = math.sqrt(max(0.0, 1 + 2 * eps * h * h / MU**2))
    return a, e


def q_para(T, ra):
    """perihelio q (en unidades del radio del planeta) con T dado y afelio ra (unidades del radio del planeta)."""
    f = lambda q: 2 / (ra + q) + 2 * math.sqrt(2 * ra * q / (ra + q)) - T
    lo, hi = 1e-6, min(1.0, ra)
    if f(lo) * f(hi) > 0: return None
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if f(lo) * f(m) <= 0: hi = m
        else: lo = m
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    AE, AM = A["Tierra"], A["Marte"]
    at = 0.5 * (AE + AM); e = (AM - AE) / (AM + AE)
    vp = math.sqrt(MU * (2 / AE - 1 / at)); VE = math.sqrt(MU / AE)
    vinf = vp - VE
    T0 = tisserand(at, e, AE)
    print(f"Elipse de Hohmann Tierra-Marte: a = {at/AU:.4f} au ; e = {e:.4f} ; v_inf (Tierra) = {vinf:.4f} km/s ; T_Tierra = {T0:.5f} ; 3-(v_inf/V)^2 = {3-(vinf/VE)**2:.5f}")
    assert abs(T0 - (3 - (vinf / VE) ** 2)) < 1e-9
    print("Tisserand respecto a la Tierra para v_inf = 2, 3, 4, 6 km/s y orbitas que cruzan la Tierra con afelio dado:")
    print(" v_inf [km/s]   T      afelio [au]   perihelio [au]   semieje [au]   periodo [anios]")
    for vi in (2.0, 3.0, 4.0, 6.0):
        T = 3 - (vi / VE) ** 2
        for ra_au in (1.2, 1.524, 2.0, 5.2):
            ra = ra_au * AU / AE
            q = q_para(T, ra)
            if q is None:
                print(f"{vi:10.1f} {T:8.4f} {ra_au:11.3f}   (inalcanzable con este v_inf)")
                continue
            a_ = 0.5 * (ra + q) * AE / AU
            print(f"{vi:10.1f} {T:8.4f} {ra_au:11.3f} {q*AE/AU:15.4f} {a_:14.4f} {a_**1.5:14.3f}")
    # Prueba 2: 200 sobrevuelos aleatorios (semilla fija) en la Tierra
    random.seed(75)
    r = [AE, 0.0]
    v = [0.4, VE + 3.0]
    a, ee = elem(r, v); T = tisserand(a, ee, AE); Tmax = 0.0
    for _ in range(200):
        VE_v = [0.0, VE]
        vin = [v[0] - VE_v[0], v[1] - VE_v[1]]
        d = random.uniform(-1.5, 1.5)
        c, s = math.cos(d), math.sin(d)
        vout = [c * vin[0] - s * vin[1], s * vin[0] + c * vin[1]]
        v = [vout[0] + VE_v[0], vout[1] + VE_v[1]]
        a2, e2 = elem(r, v)
        Tmax = max(Tmax, abs(tisserand(a2, e2, AE) - T))
    print(f"Prueba 2: 200 sobrevuelos de giro aleatorio (semilla 75): max |T - T0| = {Tmax:.2e}")
    assert Tmax < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
