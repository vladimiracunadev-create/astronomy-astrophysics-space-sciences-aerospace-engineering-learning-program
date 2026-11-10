#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C01: conservacion de masa en un conducto y en un deposito.

Datos ILUSTRATIVOS (sinteticos, no medidos): areas de un conducto [0.010, 0.006, 0.004, 0.008] m2, rho = 1.225 kg/m3, u de entrada = 20 m/s,
aire con gamma = 1.4 y R = 287.05 J/(kg K), T0 = 300 K, p0 = 101325 Pa; deposito V = 0.5 m3.
Consultado (2026-11-10): NASA Glenn, flujo masico m = rho A V y continuidad. Relaciones isentropicas estandar (no consultadas en esta clase).
Modelo A: flujo estacionario incompresible 1D, u_i = m / (rho A_i).
Modelo B: flujo isentropico compresible, mismo m: se resuelve M_i por biseccion y se comprueba que rho A u = m en cada seccion.
Modelo C: deposito con entrada m_in constante y salida m_out = c rho; integracion de Euler frente a la solucion exacta.
Tolerancias: balance de masa 1e-9 relativa (A y B); deposito 5e-3 relativa con dt = 0.01 s.
"""
import math, platform

AREAS = [0.010, 0.006, 0.004, 0.008]
RHO, U1 = 1.225, 20.0
GAM, R, T0, P0 = 1.4, 287.05, 300.0, 101325.0


def flujo_isentropico(M, a):
    """Flujo masico por area [kg/(s m2)] en funcion del Mach con p0, T0 dados."""
    t = T0 / (1 + 0.5 * (GAM - 1) * M * M)
    p = P0 * (T0 / t) ** (-GAM / (GAM - 1))
    rho = p / (R * t)
    return rho * M * math.sqrt(GAM * R * t)


def mach_para(mdot, a):
    lo, hi = 1e-6, 1.0  # rama subsonica
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if flujo_isentropico(mid, a) * a < mdot:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    mdot = RHO * AREAS[0] * U1
    print(f"Conducto ILUSTRATIVO: m = rho A1 u1 = {mdot:.5f} kg/s")
    print(" seccion  A [m2]    u [m/s]   rho*A*u [kg/s]")
    for i, a in enumerate(AREAS, 1):
        u = mdot / (RHO * a)
        print(f"   {i}     {a:.4f}   {u:8.3f}   {RHO * a * u:.5f}")
        assert abs(RHO * a * u - mdot) / mdot < 1e-9
    print("Segunda via: flujo isentropico compresible (aire), mismo m")
    mdot_c = flujo_isentropico(0.15, AREAS[0]) * AREAS[0]
    print(f" m = {mdot_c:.5f} kg/s (M1 = 0.15)")
    print(" seccion   M       rho [kg/m3]   u [m/s]   rho*A*u [kg/s]  rho/rho1")
    rho1 = None
    for i, a in enumerate(AREAS, 1):
        M = mach_para(mdot_c, a)
        t = T0 / (1 + 0.5 * (GAM - 1) * M * M)
        p = P0 * (T0 / t) ** (-GAM / (GAM - 1))
        rho = p / (R * t)
        u = M * math.sqrt(GAM * R * t)
        if rho1 is None:
            rho1 = rho
        print(f"   {i}    {M:.4f}   {rho:.4f}      {u:7.2f}    {rho * a * u:.5f}      {rho / rho1:.4f}")
        assert abs(rho * a * u - mdot_c) / mdot_c < 1e-9
    # deposito
    V, c, m_in, rho0 = 0.5, 0.2, 0.30, 1.0
    rho_eq = m_in / c
    dt, T = 0.01, 5.0
    rho = rho0
    for _ in range(int(round(T / dt))):
        rho += dt * (m_in - c * rho) / V
    exacta = rho_eq + (rho0 - rho_eq) * math.exp(-c * T / V)
    err = abs(rho - exacta) / exacta
    print(f"Deposito ILUSTRATIVO V = {V} m3, m_in = {m_in} kg/s, m_out = {c} rho:")
    print(f" rho(5 s) Euler = {rho:.6f} ; exacta = {exacta:.6f} ; error relativo = {err:.2e}")
    assert err < 5e-3
    print("Pruebas superadas.")


main()
