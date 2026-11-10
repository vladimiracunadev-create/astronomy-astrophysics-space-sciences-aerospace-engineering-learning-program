#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B57-C13: aerosoles: espesor optico, exponente de Angstrom y transmitancia.

Datos: SINTETICOS. AOD(550 nm) = 0.30 y exponente de Angstrom 1.3 (ILUSTRATIVOS; la ley AOD = beta lambda^-alpha es una relacion conocida,
NO CONSULTADA en esta sesion). Ruido de medicion de 0.01 en AOD, semilla fija 57, 20000 ensayos. Dispersion simple sobre oceano oscuro con
albedo de dispersion 0.95 y funcion de fase 0.15 (ILUSTRATIVOS).
Modelo: tau(lambda) = beta lambda^-alpha ; alpha = -ln(tau1/tau2)/ln(l1/l2) ; transmitancia directa T = exp(-tau/mu) (Beer-Lambert) con mu = cos(cenital);
reflectancia por dispersion simple rho = w0 tau P /(4 mu_s mu_v) valida para tau << 1; propagacion de errores de alpha:
sigma_alpha = sqrt((s1/t1)^2 + (s2/t2)^2)/ln(l2/l1).
Validez: capa homogenea, sin absorcion de gases. Tolerancia: alpha recuperado exacto sin ruido; desviacion simulada frente a la analitica < 3 %.
Requiere numpy.
"""
import math, platform
import numpy as np

BETA_L = 0.55
TAU550, ALPHA = 0.30, 1.3
L1, L2 = 0.44, 0.87
SIGMA = 0.01


def tau(lam, alpha=ALPHA, t550=TAU550):
    return t550 * (lam / BETA_L) ** (-alpha)


def calcular():
    r = {}
    t1, t2 = tau(L1), tau(L2)
    r["tau_440"], r["tau_870"] = t1, t2
    r["alpha_rec"] = -math.log(t1 / t2) / math.log(L1 / L2)
    r["sig_alpha_ana"] = math.sqrt((SIGMA / t1) ** 2 + (SIGMA / t2) ** 2) / math.log(L2 / L1)
    rng = np.random.default_rng(57)
    a = -np.log((t1 + SIGMA * rng.standard_normal(20000)) / (t2 + SIGMA * rng.standard_normal(20000))) / math.log(L1 / L2)
    r["alpha_media"], r["sig_alpha_sim"] = float(a.mean()), float(a.std())
    r["razon"] = r["sig_alpha_sim"] / r["sig_alpha_ana"]
    for z in (0, 30, 60, 75):
        mu = math.cos(math.radians(z))
        r[f"T_{z}"] = math.exp(-TAU550 / mu)
    # dispersion simple: linealidad en tau
    w0, P, mus, muv = 0.95, 0.15, math.cos(math.radians(30)), math.cos(math.radians(20))
    r["rho_01"] = w0 * 0.1 * P / (4 * mus * muv)
    r["rho_02"] = w0 * 0.2 * P / (4 * mus * muv)
    r["rho_exacta_01"] = 1 - math.exp(-0.1 / mus) * math.exp(-0.1 / muv)  # solo para comparar el orden de magnitud de la extincion
    return r


def main():
    print(f"Python {platform.python_version()} ; numpy {np.__version__}")
    r = calcular()
    print(f"AOD sintetico: 440 nm = {r['tau_440']:.4f} ; 870 nm = {r['tau_870']:.4f} ; alpha recuperado = {r['alpha_rec']:.6f}")
    print(f"sigma de alpha: analitica = {r['sig_alpha_ana']:.4f} ; simulada = {r['sig_alpha_sim']:.4f} ; razon = {r['razon']:.3f} ; media simulada = {r['alpha_media']:.3f}")
    print("Transmitancia directa con AOD(550) = 0.30: " + " ; ".join(f"cenital {z}: {r['T_'+str(z)]:.3f}" for z in (0, 30, 60, 75)))
    print(f"Reflectancia por dispersion simple: tau 0.1 -> {r['rho_01']:.5f} ; tau 0.2 -> {r['rho_02']:.5f} (razon {r['rho_02']/r['rho_01']:.3f})")
    assert abs(r["alpha_rec"] - ALPHA) < 1e-12
    assert abs(r["razon"] - 1) < 0.03
    assert abs(r["rho_02"] / r["rho_01"] - 2) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
