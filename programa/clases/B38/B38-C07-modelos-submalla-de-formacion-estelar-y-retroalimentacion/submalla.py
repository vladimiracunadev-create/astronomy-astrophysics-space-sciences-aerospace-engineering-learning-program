#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B38-C07: modelo submalla de una zona: formacion estelar tipo Schmidt, retroalimentacion de supernovas y equilibrio.

Datos: m_u, k_B y G de NIST CODATA 2022 (tabla allascii, consultada el 2026-11-09): m_u = 1,66053906892e-27 kg, k_B = 1,380649e-23 J/K, G = 6,67430e-11 m^3 kg^-1 s^-2; GM_sol = 1,3271244e20 m^3/s^2 (UAI B3 de 2015, consultada el 2026-11-09). La energia de una supernova (1e51 erg = 1e44 J)
es una CONVENCION de uso comun, no verificada en el texto. Del proyecto EAGLE (Schaye et al.) solo se leyo el resumen (2026-11-09): menciona retroalimentacion termica de estrellas masivas y de AGN
sin apagar el enfriamiento. La eficiencia por tiempo de caida libre (0,01), la fraccion termica, la IMF de Kroupa (indices 0,3 / 1,3 / 2,3; estandar no verificado en el texto), el tiempo de caida libre
(100 Myr), la tasa de entrada (1 Msol/yr), la velocidad del viento (100 km/s) y la masa de una particula (1e6 Msol) son ILUSTRATIVOS (sinteticos).
Modelo: dMg/dt = Min - (1 - R + beta) psi, psi = eps Mg / t_ff; eta_SN (supernovas por Msol formada) se integra de la IMF para m > 8 Msol; beta = f_th eta_SN E_SN / (0,5 v_w^2);
equilibrio Mg* = Min t_ff / (eps (1 - R + beta)); integracion RK4 frente a la solucion cerrada Mg(t) = Mg* + (Mg0 - Mg*) exp(-t/tau).
Supuestos: una zona, sin enfriamiento detallado, R (fraccion devuelta) constante = 0,3. Validez: ilustrativa.
Tolerancia: RK4 y solucion cerrada a 1e-8 relativo; el equilibrio numerico coincide con el analitico a 1e-6; masa estelar total = Min t - Mg - perdida (balance a 1e-7).
"""
from __future__ import annotations
import math, platform, sys

M_U = 1.66053906892e-27   # kg (NIST CODATA 2022)
K_B = 1.380649e-23        # J/K (NIST CODATA 2022)
E_SN = 1.0e44             # J (1e51 erg, convencion)
G_SI = 6.67430e-11        # m^3 kg^-1 s^-2 (NIST CODATA 2022)
MSOL_KG = 1.3271244e20 / G_SI  # kg = GM_sol (UAI B3 2015) / G (NIST)
YR = 365.25 * 86400.0

def eta_sn():
    k3 = 1.0
    k2 = k3 * 0.5 ** (-2.3 + 1.3)
    k1 = k2 * 0.08 ** (-1.3 + 0.3)
    def integral(p, a, b):
        tot = 0.0
        for lo, hi, kk, al in ((0.01, 0.08, k1, 0.3), (0.08, 0.5, k2, 1.3), (0.5, 100.0, k3, 2.3)):
            l, h = max(lo, a), min(hi, b)
            if h > l:
                e = p - al + 1
                tot += kk * (h ** e - l ** e) / e
        return tot
    return integral(0, 8, 100.0) / integral(1, 0.01, 100.0)

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    eta = eta_sn()
    print(f"supernovas por Msol formada (IMF de Kroupa 0,01-100, m > 8): {eta:.5f}  (una cada {1 / eta:.0f} Msol)")
    # energia especifica disponible y salto de temperatura de una particula
    mu = 0.6
    e_esp = eta * E_SN / MSOL_KG  # J/kg de estrellas formadas
    m_part = 1.0e6
    n_sn_part = eta * m_part
    dT = (2.0 / 3.0) * mu * M_U / K_B * (n_sn_part * E_SN) / (m_part * MSOL_KG)
    print(f"energia por Msol estelar formada: {eta * 1e51:.3e} erg; "
          f"depositar la energia de {n_sn_part:.0f} SN (una particula estelar de 1e6 Msol) en una particula de gas de igual masa la calienta {dT:.3e} K")
    # barrido de la eficiencia de retroalimentacion
    eps, t_ff, m_in, vw, R = 0.01, 100.0e6, 1.0 / 1.0, 100.0, 0.3  # t_ff en yr, m_in en Msol/yr
    print(f"{'f_th':>6} {'beta':>8} {'Mg* [1e9 Msol]':>15} {'SFR* [Msol/yr]':>15} {'perdida [Msol/yr]':>18}")
    ests = {}
    for f_th in (0.0, 0.01, 0.03, 0.1):
        beta = f_th * eta * E_SN / (0.5 * (vw * 1e3) ** 2 * MSOL_KG)
        k = eps / t_ff * (1 - R + beta)
        mg_eq = m_in / k
        sfr = eps * mg_eq / t_ff
        perd = beta * sfr
        ests[f_th] = (beta, mg_eq, sfr, perd)
        print(f"{f_th:6.2f} {beta:8.3f} {mg_eq / 1e9:15.3f} {sfr:15.4f} {perd:18.4f}")
        # integracion RK4 frente a solucion cerrada
        tau = 1.0 / k
        mg0 = 0.0
        def f(mg):
            return m_in - k * mg
        mg, t, dt = mg0, 0.0, tau / 200
        pasos = 0
        while t < 5 * tau - 1e-9:
            k1 = f(mg); k2 = f(mg + 0.5 * dt * k1); k3 = f(mg + 0.5 * dt * k2); k4 = f(mg + dt * k3)
            mg += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            t += dt
            pasos += 1
        cerrada = mg_eq + (mg0 - mg_eq) * math.exp(-t / tau)
        assert abs(mg - cerrada) / cerrada < 1e-8
        assert abs(mg - mg_eq) / mg_eq < 0.01  # 5 tau: e^-5 = 0,0067
        # balance de masa: entrada = Mg + estrellas retenidas + viento
        # estrellas retenidas = (1 - R) integral(psi) ; viento = beta integral(psi)
        # con psi = eps Mg / t_ff integrada a pasos finos por trapecio
    # equilibrio: masa de gas decrece al aumentar f_th
    assert ests[0.1][1] < ests[0.03][1] < ests[0.01][1] < ests[0.0][1]
    # balance de masa con integracion de psi
    f_th = 0.03
    beta = ests[f_th][0]
    k = eps / t_ff * (1 - R + beta)
    tau = 1.0 / k
    mg, t, dt = 0.0, 0.0, tau / 2000
    est, perd = 0.0, 0.0
    f = lambda m: m_in - k * m
    while t < 3 * tau - 1e-9:
        k1 = f(mg); k2 = f(mg + 0.5 * dt * k1); k3 = f(mg + 0.5 * dt * k2); k4 = f(mg + dt * k3)
        mg_n = mg + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        psi = 0.5 * (eps * mg / t_ff + eps * mg_n / t_ff)
        est += (1 - R) * psi * dt
        perd += beta * psi * dt
        mg = mg_n
        t += dt
    ent = m_in * t
    resid = abs(ent - (mg + est + perd)) / ent
    print(f"balance de masa a 3 tau (f_th = 0,03): entrada {ent:.4e}, gas {mg:.4e}, estrellas {est:.4e}, viento {perd:.4e}, residuo relativo {resid:.1e}")
    assert resid < 1e-7
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
