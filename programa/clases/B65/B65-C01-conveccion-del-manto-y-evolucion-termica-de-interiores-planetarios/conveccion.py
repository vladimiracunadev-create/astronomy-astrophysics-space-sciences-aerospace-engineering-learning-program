#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B65-C01: conveccion del manto y evolucion termica parametrizada.

Datos: ninguna constante consultada. Todos los parametros del manto (alfa, rho, g, kappa, k, eta, E, calor radiactivo) son ILUSTRATIVOS
(sinteticos, de orden de magnitud terrestre); no se ajusta ningun cuerpo real.
Modelo: (1) Rayleigh critico de Rayleigh-Benard con fronteras libres: minimo numerico de Ra(k) = (pi^2 + k^2)^3 / k^2 frente a 27 pi^4 / 4.
(2) Evolucion termica parametrizada: C dT/dt = H(t) - Q(T), Q = A k (T - Ts)/d * (Ra/Ra_c)^beta, viscosidad de Arrhenius; RK4 frente al
estado estacionario hallado por biseccion (H constante).
Supuestos: manto de una capa bien mezclada, beta = 1/3, flujo basal y calor latente omitidos. Validez: solo ilustrativa.
Tolerancia: Ra_c numerico frente a analitico < 1e-6 relativo; T(t largo) frente a T_estacionaria < 1e-2 K.
"""
from __future__ import annotations
import math, platform

# ---------------- (1) Rayleigh critico -----------------
def ra_k(k):
    return (math.pi**2 + k**2) ** 3 / k**2

def minimo(f, a, b, n=200):
    """Busqueda de seccion aurea del minimo de f en [a, b]."""
    g = (math.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    for _ in range(n):
        if f(c) < f(d):
            b = d
        else:
            a = c
        c, d = b - g * (b - a), a + g * (b - a)
    return (a + b) / 2

kmin = minimo(ra_k, 0.5, 6.0)
rac_num = ra_k(kmin)
rac_ana = 27 * math.pi**4 / 4
kmin_ana = math.pi / math.sqrt(2)

# ---------------- (2) Numero de Rayleigh del manto ilustrativo -----------------
ALFA, RHO, G, KAPPA, KCOND = 3.0e-5, 4000.0, 10.0, 1.0e-6, 4.0   # K^-1, kg m^-3, m s^-2, m^2 s^-1, W m^-1 K^-1
D, RP = 2.9e6, 6.371e6                                           # m (espesor del manto, radio)
TS = 273.0                                                        # K
E_ACT, R_GAS, ETA_REF, T_REF = 3.0e5, 8.314, 1.0e21, 1600.0     # J/mol, J/mol/K, Pa s, K (ilustrativos)
BETA = 1.0 / 3.0
C_TERM = 7.0e27 * 1.0                                             # J/K capacidad termica efectiva (ILUSTRATIVA)

def eta(T):
    return ETA_REF * math.exp(E_ACT / R_GAS * (1.0 / T - 1.0 / T_REF))

def rayleigh(T, Tcore=None):
    dT = (T - TS) if Tcore is None else (Tcore - TS)
    return ALFA * RHO * G * dT * D**3 / (KAPPA * eta(T))

def flujo_total(T):
    """Potencia que sale del manto [W]: A k dT/d (Ra/Rac)^beta, con A = 4 pi R^2."""
    area = 4 * math.pi * RP**2
    nu = (rayleigh(T) / rac_ana) ** BETA
    return area * KCOND * (T - TS) / D * nu

H0 = 30e12     # W calor radiactivo hoy-equivalente (ILUSTRATIVO)
def calor(t, decae):
    return H0 * (math.exp(-math.log(2) * t / (2.5e9 * 3.156e7)) if decae else 1.0)

def rk4(T0, t_fin, dt, decae):
    T, t = T0, 0.0
    f = lambda t, T: (calor(t, decae) - flujo_total(T)) / C_TERM
    while t < t_fin:
        k1 = f(t, T); k2 = f(t + dt/2, T + dt/2*k1); k3 = f(t + dt/2, T + dt/2*k2); k4 = f(t + dt, T + dt*k3)
        T += dt/6*(k1 + 2*k2 + 2*k3 + k4); t += dt
    return T

def estacionaria():
    lo, hi = TS + 10.0, 4000.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if flujo_total(mid) < H0:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Ra critico (fronteras libres): numerico = {rac_num:.6f} en k = {kmin:.6f} ; analitico 27 pi^4/4 = {rac_ana:.6f} en k = {kmin_ana:.6f}")
    err = abs(rac_num - rac_ana) / rac_ana
    print(f"Error relativo = {err:.2e}")
    ra0 = rayleigh(2000.0, Tcore=2000.0)
    print(f"Ra del manto ilustrativo (T = 1600 K, dT = 1327 K): {rayleigh(1600.0, Tcore=1600.0):.3e} ; Ra/Rac = {rayleigh(1600.0, Tcore=1600.0)/rac_ana:.3e}")
    print(f"Viscosidad a 1500 K / 1600 K / 1700 K: {eta(1500.0):.2e} / {eta(1600.0):.2e} / {eta(1700.0):.2e} Pa s")
    # exponente beta recuperado por dos temperaturas
    q1, q2 = flujo_total(1500.0), flujo_total(1700.0)
    print(f"Potencia de salida a 1500 K = {q1/1e12:.2f} TW ; a 1700 K = {q2/1e12:.2f} TW")
    Tss = estacionaria()
    print(f"Estado estacionario con H = {H0/1e12:.0f} TW constante: T_ss = {Tss:.3f} K")
    dt = 3.156e7 * 5.0e6  # 5 Ma
    for T0 in (2200.0, 1300.0):
        Tf = rk4(T0, 15.0e9 * 3.156e7, dt, decae=False)
        print(f"RK4 desde {T0:.0f} K tras 15 Ga: T = {Tf:.3f} K ; |T - T_ss| = {abs(Tf - Tss):.4f} K")
    Td = rk4(2200.0, 4.5e9 * 3.156e7, dt, decae=True)
    print(f"Con calor radiactivo decreciente (vida media 2.5 Ga, ilustrativa) tras 4.5 Ga desde 2200 K: T = {Td:.1f} K")
    ok = err < 1e-6 and abs(rk4(2200.0, 15.0e9*3.156e7, dt, False) - Tss) < 1e-2 and abs(rk4(1300.0, 15.0e9*3.156e7, dt, False) - Tss) < 1e-2
    assert ok
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
