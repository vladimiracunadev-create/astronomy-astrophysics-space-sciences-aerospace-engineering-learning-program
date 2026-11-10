#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C01: radiacion solar reflejada y radiacion terrestre emitida (ley de Planck).

Datos: constantes h, c, k_B del SI (valores exactos de la redefinicion de 2019; no se consulto una pagina en esta sesion) y
parametros ILUSTRATIVOS: T_sol = 5772 K, T_tierra = 288 K, radio solar 6.957e8 m, 1 UA = 1.495978707e11 m, reflectancia 0.30
(superficie lambertiana), angulo cenital solar 30 grados. No hay datos observados: todo es modelo.
Modelo: radiancia espectral de Planck B(lambda,T) [W m^-2 sr^-1 m^-1]; irradiancia solar en la Tierra E = pi B(lambda,T_sol) (R_sol/d)^2;
radiancia reflejada L_r = rho E cos(theta)/pi; radiancia emitida L_e = B(lambda,288 K) (emisividad 1).
Sistema de referencia: radiancia en el tope de la atmosfera, sin atmosfera. Validez: ilustrativa; el Sol no es un cuerpo negro exacto.
Tolerancia: integral de pi B frente a sigma T^4 < 0.2 %; maximo de Planck frente a la ley de Wien < 0.5 %.
"""
import math, platform

H = 6.62607015e-34
C = 299792458.0
KB = 1.380649e-23
SIGMA = 2 * math.pi**5 * KB**4 / (15 * H**3 * C**2)  # derivada de las constantes anteriores
T_SOL, T_TIERRA = 5772.0, 288.0
R_SOL, UA = 6.957e8, 1.495978707e11
RHO, THETA = 0.30, math.radians(30.0)


def planck(lam, T):
    """Radiancia espectral [W m^-2 sr^-1 m^-1]; lam en metros."""
    x = H * C / (lam * KB * T)
    if x > 700:
        return 0.0
    return 2 * H * C**2 / lam**5 / math.expm1(x)


def integral_pi_b(T, lmin=0.02e-6, lmax=2000e-6, n=40000):
    """Integral de pi B dlambda con malla logaritmica y regla del trapecio en ln(lambda)."""
    a, b = math.log(lmin), math.log(lmax)
    dx = (b - a) / n
    s = 0.0
    for i in range(n + 1):
        lam = math.exp(a + i * dx)
        f = math.pi * planck(lam, T) * lam
        s += f * (0.5 if i in (0, n) else 1.0)
    return s * dx


def pico(T):
    lo, hi = 0.05e-6, 200e-6
    for _ in range(200):  # busqueda de seccion dorada
        m1, m2 = lo + (hi - lo) * 0.382, lo + (hi - lo) * 0.618
        if planck(m1, T) < planck(m2, T):
            lo = m1
        else:
            hi = m2
    return 0.5 * (lo + hi)


def e_sol(lam):
    return math.pi * planck(lam, T_SOL) * (R_SOL / UA) ** 2


def l_refl(lam):
    return RHO * e_sol(lam) * math.cos(THETA) / math.pi


def calcular():
    r = {}
    r["sigma"] = SIGMA
    for nombre, T in (("sol", T_SOL), ("tierra", T_TIERRA)):
        r["err_" + nombre] = abs(integral_pi_b(T) / (SIGMA * T**4) - 1.0)
        r["pico_" + nombre] = pico(T) * 1e6
        r["wien_" + nombre] = 2.897771955e-3 / T * 1e6
        r["errw_" + nombre] = abs(r["pico_" + nombre] / r["wien_" + nombre] - 1.0)
    r["Lr_vis"] = l_refl(0.55e-6)
    r["Le_vis"] = planck(0.55e-6, T_TIERRA)
    r["Lr_tir"] = l_refl(11e-6)
    r["Le_tir"] = planck(11e-6, T_TIERRA)
    lo, hi = 1e-6, 20e-6  # cruce de reflejada y emitida (biseccion)
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if l_refl(mid) > planck(mid, T_TIERRA):
            lo = mid
        else:
            hi = mid
    r["cruce"] = lo * 1e6
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"sigma derivada = {r['sigma']:.6e} W m^-2 K^-4")
    for n in ("sol", "tierra"):
        print(f"{n}: integral pi*B vs sigma T^4: error relativo = {r['err_'+n]:.2e} ; maximo de Planck = {r['pico_'+n]:.4f} um ; Wien = {r['wien_'+n]:.4f} um")
    print(f"0.55 um: reflejada = {r['Lr_vis']:.4e} ; emitida = {r['Le_vis']:.3e} W m^-2 sr^-1 m^-1")
    print(f"11 um: reflejada = {r['Lr_tir']:.3e} ; emitida = {r['Le_tir']:.4e} W m^-2 sr^-1 m^-1")
    print(f"Longitud de onda de cruce (reflejada = emitida) = {r['cruce']:.2f} um")
    assert r["err_sol"] < 2e-3 and r["err_tierra"] < 2e-3
    assert r["errw_sol"] < 5e-3 and r["errw_tierra"] < 5e-3
    assert r["Lr_vis"] > 1e6 * r["Le_vis"] and r["Le_tir"] > 100 * r["Lr_tir"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
