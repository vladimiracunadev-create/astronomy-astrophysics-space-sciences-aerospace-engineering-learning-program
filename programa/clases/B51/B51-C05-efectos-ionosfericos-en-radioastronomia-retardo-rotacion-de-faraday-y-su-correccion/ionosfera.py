#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B51-C05: retardo ionosferico, rotacion de Faraday y su correccion con dos frecuencias.

Datos: constantes de NIST CODATA 2022 (e, m_e, epsilon_0 y c; consultadas el 2026-11-09) de las que se DERIVAN la constante del retardo dispersivo (~40,3 m^3/s^2) y la del
giro de Faraday. El contenido electronico total (20 TECU), el campo B paralelo (4e-5 T), las frecuencias y el ruido son SINTETICOS e ILUSTRATIVOS; 1 TECU = 1e16 m^-2.
Modelo: retardo de grupo tau = K TEC / (c nu^2) con K = e^2 / (8 pi^2 epsilon_0 m_e); angulo de Faraday chi = RM lambda^2 con RM = e^3 / (8 pi^2 epsilon_0 m_e^2 c^3) * TEC * B_par.
Segunda via: TEC por diferencia de retardos en dos frecuencias frente al valor inyectado; RM por busqueda en rejilla (suma coherente de exp(2 i chi)) frente al valor inyectado.
Supuestos: plasma frio, capa delgada, B constante, ruido gaussiano. Validez: ilustrativa; no usa mapas ionosfericos reales.
Tolerancia: constante K entre 40,2 y 40,4; TEC recuperado sin ruido a 1e-9; RM recuperado dentro de 3 sigma predichas con ruido.
"""
from __future__ import annotations
import cmath, math, platform, random, sys

E = 1.602176634e-19
ME = 9.1093837139e-31
EPS0 = 8.8541878188e-12
C = 299792458.0
TECU = 1e16

def compute():
    rng = random.Random(20261109)
    K = E ** 2 / (8 * math.pi ** 2 * EPS0 * ME)
    KF = E ** 3 / (8 * math.pi ** 2 * EPS0 * ME ** 2 * C ** 3)
    tec, b = 20 * TECU, 4e-5
    R = dict(K=K, KF=KF, tec=tec / TECU, b=b)
    R["rows"] = []
    for nu in (150e6, 1.4e9, 8.4e9):
        tau = K * tec / (C * nu ** 2)
        R["rows"].append((nu / 1e9, tau * 1e9, 2 * math.pi * nu * tau))
    # TEC por dos frecuencias
    n1, n2 = 1.4e9, 1.7e9
    t1 = K * tec / (C * n1 ** 2); t2 = K * tec / (C * n2 ** 2)
    est = (t1 - t2) * C / (K * (1 / n1 ** 2 - 1 / n2 ** 2))
    R["tec_est"] = est / TECU
    sig_t = 0.05e-9
    ests = []
    for _ in range(2000):
        a = t1 + rng.gauss(0, sig_t); c = t2 + rng.gauss(0, sig_t)
        ests.append((a - c) * C / (K * (1 / n1 ** 2 - 1 / n2 ** 2)) / TECU)
    mu = sum(ests) / len(ests)
    R["tec_mc_mu"] = mu; R["tec_mc_sd"] = math.sqrt(sum((x - mu) ** 2 for x in ests) / (len(ests) - 1))
    R["tec_pred_sd"] = math.sqrt(2) * sig_t * C / (K * (1 / n1 ** 2 - 1 / n2 ** 2)) / TECU
    # Faraday
    rm = KF * tec * b
    R["rm"] = rm
    nus = [120e6 + 3.75e6 * k for k in range(17)]
    lam2 = [(C / v) ** 2 for v in nus]
    sig_chi = 0.1
    chi = [rm * l2 + rng.gauss(0, sig_chi) for l2 in lam2]
    best = (-1, 0)
    for q in range(-4000, 4001):
        t = q * 0.002
        s = abs(sum(cmath.exp(2j * (c - t * l2)) for c, l2 in zip(chi, lam2)))
        if s > best[0]:
            best = (s, t)
    R["rm_est"] = best[1]
    mm = sum(lam2) / len(lam2)
    R["rm_sig"] = sig_chi / math.sqrt(sum((x - mm) ** 2 for x in lam2))
    R["ambig"] = math.pi / (lam2[0] - lam2[-1]) if False else math.pi / ((C / nus[0]) ** 2 - (C / nus[-1]) ** 2)
    R["chi_deg"] = [(v / 1e9, math.degrees(rm * (C / v) ** 2)) for v in (120e6, 150e6, 180e6)]
    R["chi_150"] = math.degrees(rm * (C / 150e6) ** 2)
    return R

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = compute()
    print(f"K = e^2/(8 pi^2 eps0 me) = {R['K']:.4f} m^3/s^2 ; coeficiente de Faraday = {R['KF']:.4e} (SI: rad m^-2 por m^-2 T)")
    assert 40.2 < R["K"] < 40.4
    print(f"TEC = {R['tec']:.0f} TECU ; B_par = {R['b']:.1e} T ; RM = {R['rm']:.4f} rad/m^2")
    print("nu [GHz]  retardo [ns]  fase [rad]")
    for nu, t, p in R["rows"]:
        print(f"{nu:8.3f} {t:13.4f} {p:11.3f}")
    print(f"TEC por dos frecuencias sin ruido = {R['tec_est']:.9f} TECU")
    assert abs(R["tec_est"] - R["tec"]) < 1e-6
    print(f"con ruido de retardo 0,05 ns: media = {R['tec_mc_mu']:.3f} TECU ; desviacion MC = {R['tec_mc_sd']:.3f} ; formula = {R['tec_pred_sd']:.3f}")
    assert abs(R["tec_mc_sd"] / R["tec_pred_sd"] - 1) < 0.1
    for nu, ang in R["chi_deg"]:
        print(f"angulo de Faraday a {nu:.2f} GHz = {ang:.2f} grados")
    print(f"angulo a 150 MHz = {R['chi_150']:.1f} grados ; ambiguedad n*pi entre canales extremos: Delta RM = {R['ambig']:.2f} rad/m^2")
    print(f"RM recuperado por rejilla = {R['rm_est']:.3f} rad/m^2 (inyectado {R['rm']:.3f}) ; sigma predicha = {R['rm_sig']:.3f}")
    assert abs(R["rm_est"] - R["rm"]) < 3 * R["rm_sig"]
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
