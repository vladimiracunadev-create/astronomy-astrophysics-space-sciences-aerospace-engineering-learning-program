#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B31-C16: criterio de Hillas, neutrinos del decaimiento de piones y numero de eventos esperados.

Datos: c, e y la masa del muon (105.658 3755 MeV) (NIST CODATA 2022, tabla allascii.txt), consultados 2026-11-09. La masa del pion cargado (139.57 MeV), los campos y tamanos de las fuentes
(tres fuentes genericas), el flujo (phi_0 = 1e-18 GeV^-1 cm^-2 s^-1 sr^-1 a 100 TeV con indice 2), el area efectiva (10 m^2 = 1e5 cm^2), el angulo solido (2 pi sr), el tiempo
(10 anios) y el fondo (3 eventos) son ILUSTRATIVOS (sinteticos); no se describe ningun detector ni fuente real.
Modelo: criterio de Hillas E_max = Z beta c B R (en eV, con B en T y R en m); decaimiento pi+ -> mu+ nu_mu en el reposo del pion con E_nu* = (m_pi^2 - m_mu^2)/(2 m_pi) y fraccion media
de energia que lleva el neutrino en el laboratorio <E_nu>/E_pi = (1 - m_mu^2/m_pi^2)/2, verificada por Monte Carlo (decaimiento isotropo y boost con gamma = 1000); numero esperado de eventos
N = T Omega Int A_eff(E) phi(E) dE para un flujo de potencias; probabilidad de observar al menos n eventos con un fondo b (Poisson).
Supuestos: aceleracion maxima ideal, area efectiva constante. Validez: orden de magnitud.
Tolerancia: fraccion media de Monte Carlo dentro de 0.5 % de la analitica; N numerico (Simpson en ln E) frente al analitico a 1e-6.
"""
from __future__ import annotations
import math
import platform
import random
import sys

C = 299792458.0
MMU = 105.6583755
MPI = 139.57


def poisson_cola(n, mu):
    """P(N >= n) para N ~ Poisson(mu)."""
    s = 0.0
    t = math.exp(-mu)
    for k in range(n):
        s += t
        t *= mu / (k + 1)
    return 1 - s


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"{'fuente (ilustrativa)':<22} {'B [T]':>9} {'R [m]':>9} {'beta':>6} {'E_max proton [eV]':>18} {'E_max hierro (Z = 26) [eV]':>28}")
    for nombre, b, r, beta in (("A: choque pequeno", 1e-9, 1e17, 0.01), ("B: choque grande", 3e-10, 3e19, 0.05), ("C: jet compacto", 1e-5, 1e15, 1.0)):
        emax = beta * C * b * r
        print(f"{nombre:<22} {b:9.1e} {r:9.1e} {beta:6.2f} {emax:18.3e} {26 * emax:28.3e}")
    # pion
    estar = (MPI ** 2 - MMU ** 2) / (2 * MPI)
    r2 = (MMU / MPI) ** 2
    print(f"decaimiento pi+ -> mu+ nu en reposo: E_nu* = {estar:.3f} MeV ; fraccion media lab <E_nu>/E_pi = (1 - m_mu^2/m_pi^2)/2 = {(1 - r2) / 2:.4f}")
    rng = random.Random(20261109)
    gam = 1000.0
    beta = math.sqrt(1 - 1 / gam ** 2)
    n = 200000
    s = 0.0
    for _ in range(n):
        ct = 2 * rng.random() - 1
        s += gam * estar * (1 + beta * ct)
    media = s / n / (gam * MPI)
    print(f"Monte Carlo ({n} decaimientos, gamma = {gam:.0f}): <E_nu>/E_pi = {media:.5f} ; analitica = {(1 - r2) / 2:.5f} ; cociente = {media / ((1 - r2) / 2):.5f}")
    assert abs(media / ((1 - r2) / 2) - 1) < 5e-3
    # eventos esperados: phi = phi0 (E/E0)^-2 en GeV^-1 cm^-2 s^-1 sr^-1, E0 = 1e5 GeV
    phi0, e0 = 1e-18, 1e5
    aeff, omega, t_s = 1e5, 2 * math.pi, 10 * 3.15576e7
    e1, e2 = 1e5, 1e7
    ana = t_s * omega * aeff * phi0 * e0 ** 2 * (1 / e1 - 1 / e2)
    pasos = 20000
    h = (math.log(e2) - math.log(e1)) / pasos
    f = lambda le: math.exp(le) * phi0 * (math.exp(le) / e0) ** -2         # integrando E phi(E) dlnE
    ssum = f(math.log(e1)) + f(math.log(e2))
    for i in range(1, pasos):
        ssum += (4 if i % 2 else 2) * f(math.log(e1) + i * h)
    num = t_s * omega * aeff * ssum * h / 3
    print(f"eventos esperados entre 100 TeV y 10 PeV (A_eff = 1e5 cm^2 = 10 m^2, 10 anios, 2 pi sr): analitico = {ana:.4f} ; Simpson en ln E = {num:.4f}")
    assert abs(num / ana - 1) < 1e-6
    mu_b = 3.0
    print(f"{'n observados':>12} {'P(N >= n | fondo = 3)':>23} {'P(N >= n | fondo + senal)':>27}")
    for nn in (3, 5, 8, 12):
        print(f"{nn:12d} {poisson_cola(nn, mu_b):23.5f} {poisson_cola(nn, mu_b + ana):27.5f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
