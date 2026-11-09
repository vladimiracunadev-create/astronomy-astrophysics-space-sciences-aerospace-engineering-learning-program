#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B36-C10: tasa de retroceso nuclear de una particula de materia oscura, modulacion anual y limite sin fondo.

Datos: u = 931,494103 MeV, masa del proton 938,272089 MeV y c (NIST CODATA 2022, tabla allascii consultada 2026-11-09). Consultado el 2026-11-09 solo el RESUMEN de XENON1T
(arXiv:1805.12562: 1,0 t x a de exposicion, limite de 4,1e-47 cm^2 a 30 GeV con 90 % CL) y el RESUMEN de la revision de Schumann (arXiv:1903.03026); NO se reproduce ningun analisis.
Ilustrativos y convencionales NO consultados: rho_0 = 0,3 GeV/cm^3, v_0 = 220 km/s, v_E = 232 km/s con +/- 15 km/s anual, v_esc = 544 km/s, A = 131, m_chi = 100 y 30 GeV,
sigma_n = 1e-45 cm^2, umbral de 5 keV, exposicion de 1 t x a. Sin factor de forma nuclear, sin eficiencia, sin fondo.
Modelo: dsigma/dE isotropa en el centro de masa, E_R = (mu^2 v^2/m_N)(1 - cos theta); tasa por nucleo = n_chi sigma_N <v (1 - E_th/E_max)>; sigma_N = sigma_n A^2 (mu_N/mu_n)^2.
Segunda via: el caso estatico (v_E = 0, sin corte) tiene la forma cerrada exp(-E/(E_0 r)), E_0 = m_chi v_0^2/2, r = 4 m_chi m_N/(m_chi + m_N)^2; el limite de Poisson 2,303 sucesos se
comprueba con 40 000 experimentos simulados (semilla 20261109).
Supuestos: halo de Maxwell-Boltzmann estandar, dispersion independiente del espin, sin fondo. Validez: ilustrativa; no es una prediccion para ningun detector real.
Tolerancia: fraccion de exceso MC frente a la forma cerrada, 1 %; cobertura de Poisson, 3 sigma.
"""
from __future__ import annotations
import math, platform, random

C = 299792458.0
U_MEV = 931.49410372
RHO0 = 0.3  # GeV/cm^3
V0 = 220e3  # m/s
VE0 = 232e3
VESC = 544e3
A = 131
KEV = 1e-6  # GeV


def kin(mchi, a=A):
    mn = a * U_MEV / 1000  # GeV
    mu = mchi * mn / (mchi + mn)
    return mn, mu


def emax(v, mchi, mn, mu):
    # v en m/s -> E_max en GeV
    b = v / C
    return 2 * mu * mu * b * b / mn


def sample(rng, n, ve):
    return [(rng.gauss(0, V0 / math.sqrt(2)), rng.gauss(0, V0 / math.sqrt(2)), rng.gauss(0, V0 / math.sqrt(2))) for _ in range(n)]


def rate_weight(vec, ve, mchi, eth, vesc=None):
    mn, mu = kin(mchi)
    s = 0.0
    n = len(vec)
    for (x, y, z) in vec:
        vx, vy, vz = x, y, z + ve  # la Tierra se mueve a -z en el halo: el DM llega con +ve
        v = math.sqrt(vx * vx + vy * vy + vz * vz)
        if vesc is not None and v > vesc:
            continue
        em = emax(v, mchi, mn, mu)
        if em > eth:
            s += v * (1 - eth / em)
    return s / n


def rate_per_kg_day(mchi, sig_n, eth, ve, vec, vesc):
    mn, mu = kin(mchi)
    mup = mchi * 0.938272089 / (mchi + 0.938272089)
    sig_N = sig_n * A * A * (mu / mup) ** 2  # cm^2
    nchi = RHO0 / mchi  # cm^-3
    w = rate_weight(vec, ve, mchi, eth, vesc) * 100.0  # cm/s
    per_nucleus = nchi * sig_N * w  # s^-1
    return per_nucleus, mn


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    N = 200000
    vec = sample(rng, N, 0)
    # 1) caso estatico frente a la exponencial
    mchi = 100.0
    mn, mu = kin(mchi)
    e0r = 0.5 * mchi * (V0 / C) ** 2 * 4 * mchi * mn / (mchi + mn) ** 2  # GeV
    print(f"m_N = {mn:.2f} GeV ; mu = {mu:.2f} GeV ; E_0 r = {e0r * 1e6:.2f} keV")
    base = rate_weight(vec, 0.0, mchi, 0.0)
    print(f"{'E_th [keV]':>10} {'MC R(>E)/R(>0)':>16} {'exp(-E/E0r)':>12}")
    worst = 0.0
    for et in (2, 5, 10, 20, 40):
        r = rate_weight(vec, 0.0, mchi, et * KEV) / base
        t = math.exp(-et * KEV / e0r)
        worst = max(worst, abs(r - t))
        print(f"{et:10d} {r:16.4f} {t:12.4f}")
    # 2) tasa con movimiento de la Tierra y modulacion
    kg_por_gev = 1.78266192e-27
    n_kg = 1.0 / (A * U_MEV / 1000 * kg_por_gev)
    vec2 = sample(rng, N, 0)
    sig_n = 1e-45
    print(f"{'m_chi [GeV]':>11} {'ve [km/s]':>10} {'R(>5keV) [1/(kg d)]':>20}")
    out = {}
    for mc in (30.0, 100.0):
        for nombre, ve in (("junio", VE0 + 15e3), ("diciembre", VE0 - 15e3)):
            per_nuc, mn_ = rate_per_kg_day(mc, sig_n, 5 * KEV, ve, vec2, VESC)
            r = per_nuc * n_kg * 86400
            out[(mc, nombre)] = r
            print(f"{mc:11.0f} {ve / 1e3:10.0f} {r:20.4e}")
    mod = {mc: (out[(mc, "junio")] - out[(mc, "diciembre")]) / (out[(mc, "junio")] + out[(mc, "diciembre")]) for mc in (30.0, 100.0)}
    print(f"modulacion (junio - diciembre)/(junio + diciembre): m=30 GeV: {mod[30.0] * 100:.2f} % ; m=100 GeV: {mod[100.0] * 100:.2f} %")
    # 3) limite sin fondo
    nup = -math.log(0.1)
    expo = 1000.0 * 365.25  # kg d
    print(f"limite superior a 90 % CL sin sucesos observados ni fondo: N = -ln(0.1) = {nup:.4f}")
    for mc in (30.0, 100.0):
        r_prom = 0.5 * (out[(mc, "junio")] + out[(mc, "diciembre")])
        sig90 = nup / (r_prom * expo) * sig_n
        print(f"m_chi = {mc:5.0f} GeV: sucesos esperados con sigma_n = 1e-45 cm^2 en 1 t x a = {r_prom * expo:.1f} ; sigma_90 (sin fondo, sin eficiencia) = {sig90:.2e} cm^2")
    # cobertura
    cuentas0 = 0
    ne = 40000
    for _ in range(ne):
        lim, k, p = math.exp(-nup), 0, 1.0
        while True:
            p *= rng.random()
            if p <= lim:
                break
            k += 1
        cuentas0 += (k == 0)
    fr = cuentas0 / ne
    sg = math.sqrt(0.1 * 0.9 / ne)
    print(f"cobertura: fraccion de experimentos con 0 sucesos si la media es {nup:.3f} = {fr:.4f} (esperado 0.1000 +/- {sg:.4f})")
    assert worst < 0.01
    assert abs(fr - 0.1) < 3 * sg
    assert 0 < mod[100.0] < 0.1 and 0 < mod[30.0] < 0.15
    assert out[(100.0, "junio")] > out[(100.0, "diciembre")]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
