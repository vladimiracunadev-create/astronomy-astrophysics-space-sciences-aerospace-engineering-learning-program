#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B79-C08: tobera convergente-divergente ideal (isentropica, 1D, gas ideal con gamma constante).

Consultado (2026-11-10): NASA Glenn, tobera CD: subsonico antes de la garganta y supersonico despues; relaciones isentropicas.
ESTANDAR (no consultado): flujo masico bloqueado m = p0 At sqrt(g/(R T0)) (2/(g+1))^((g+1)/(2(g-1))); empuje F = m Ve + (pe - pa) Ae;
coeficiente de empuje Cf; impulso especifico Isp = F/(m g0) con g0 = 9.80665 m/s2 (valor convencional).
ILUSTRATIVOS (sinteticos, no medidos): gas con gamma = 1.2 y R = 350 J/(kg K); p0 = 5.0e6 Pa; T0 = 3000 K; At = 0.010 m2; Ae/At = 10 y 25;
presion ambiente pa = 101325 Pa (nivel del mar, ilustrativa) y 0 (vacio).
Via 2: Ve por energia sqrt(2 cp (T0 - Te)); flujo masico en la salida rho_e Ve Ae frente a la garganta; Cf por formula cerrada frente a F/(p0 At).
Tolerancias: diferencias entre vias < 1e-10 relativas.
"""
import math, platform

G, R, P0, T0, AT, PA = 1.2, 350.0, 5.0e6, 3000.0, 0.010, 101325.0
CP = G * R / (G - 1)
G0 = 9.80665


def area_ratio(M):
    return (1 / M) * ((2 / (G + 1)) * (1 + 0.5 * (G - 1) * M * M)) ** ((G + 1) / (2 * (G - 1)))


def mach_sup(ar):
    lo, hi = 1.0, 50.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if area_ratio(mid) < ar:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Tobera ILUSTRATIVA: gamma = {G}, R = {R} J/(kg K), p0 = {P0:.2e} Pa, T0 = {T0} K, At = {AT} m2")
    mdot = P0 * AT * math.sqrt(G / (R * T0)) * (2 / (G + 1)) ** ((G + 1) / (2 * (G - 1)))
    tg = T0 * 2 / (G + 1)
    pg = P0 * (2 / (G + 1)) ** (G / (G - 1))
    print(f"Garganta: T* = {tg:.1f} K, p* = {pg:.0f} Pa, a* = {math.sqrt(G * R * tg):.2f} m/s ; m = {mdot:.3f} kg/s")
    print(" Ae/At   Me      pe [Pa]   Te [K]   Ve [m/s]   m(salida) [kg/s]   F(pa) [kN]   F(vacio) [kN]   Cf(pa)   Isp(pa) [s]")
    peor = 0.0
    for eps in (10.0, 25.0):
        Me = mach_sup(eps)
        f = 1 + 0.5 * (G - 1) * Me * Me
        te = T0 / f
        pe = P0 * f ** (-G / (G - 1))
        ve1 = Me * math.sqrt(G * R * te)
        ve2 = math.sqrt(2 * CP * (T0 - te))
        rho_e = pe / (R * te)
        m_sal = rho_e * ve1 * eps * AT
        F = mdot * ve1 + (pe - PA) * eps * AT
        Fv = mdot * ve1 + pe * eps * AT
        cf_cerr = math.sqrt(2 * G * G / (G - 1) * (2 / (G + 1)) ** ((G + 1) / (G - 1)) * (1 - (pe / P0) ** ((G - 1) / G))) + (pe - PA) / P0 * eps
        cf = F / (P0 * AT)
        peor = max(peor, abs(ve1 - ve2) / ve1, abs(m_sal - mdot) / mdot, abs(cf - cf_cerr) / cf)
        print(f" {eps:5.1f}  {Me:.4f}  {pe:9.0f}  {te:7.1f}  {ve1:8.2f}     {m_sal:8.3f}       {F / 1e3:8.2f}      {Fv / 1e3:8.2f}      {cf:.4f}   {F / (mdot * G0):7.2f}")
    print(f"Diferencia maxima entre vias (Ve, m, Cf) = {peor:.2e}")
    # regimenes segun la contrapresion para Ae/At = 10
    eps = 10.0
    Me = mach_sup(eps)
    f = 1 + 0.5 * (G - 1) * Me * Me
    pe = P0 * f ** (-G / (G - 1))
    pshock = pe * (2 * G * Me * Me - (G - 1)) / (G + 1)
    # rama subsonica isentropica con garganta M = 1
    lo, hi = 1e-6, 1.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if area_ratio(mid) > eps:
            lo = mid
        else:
            hi = mid
    ms = 0.5 * (lo + hi)
    psub = P0 * (1 + 0.5 * (G - 1) * ms * ms) ** (-G / (G - 1))
    print(f"Contrapresiones para Ae/At = 10: diseno pe = {pe:.0f} Pa ; choque en la salida pb = {pshock:.0f} Pa ; limite subsonico bloqueado pb = {psub:.0f} Pa")
    print(f" Con pa = {PA:.0f} Pa (> pe): tobera sobreexpandida, pa/pe = {PA / pe:.2f}")
    assert peor < 1e-10
    assert abs(area_ratio(1.0) - 1.0) < 1e-12
    print("Pruebas superadas.")


main()
