#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B68-C04: dimensionamiento de un montaje de hielos en ultra alto vacio criogenico.

Datos publicados: k_B = 1,380 649e-23 J/K (exacta), u = 1,660 539 068 92e-27 kg, 1 eV = 1,602 176 634e-19 J (NIST CODATA 2022, consultado el 2026-11-09);
parametros de desorcion del CO (E = 1040 K, nu = 8,7e14 ML/s, beta = 0,2 K/s) de Kruczkiewicz et al. (2024, arXiv:2404.02695, consultado el 2026-11-09).
Convencion: 1 ML = 1e15 moleculas cm^-2; 1 Torr = 101325/760 Pa (definicion); 1 mbar = 100 Pa; 1 langmuir = 1e-6 Torr s.
Masas molares convencionales (28,010 g/mol CO; 18,015 g/mol H2O): valores de uso corriente NO consultados en esta sesion.
SINTETICO / ILUSTRATIVO: presiones (1e-11 a 1e-7 mbar), temperatura del gas 300 K, probabilidad de adhesion 1, volumen 20 L, velocidad de bombeo 100 L/s,
area de la muestra 1 cm^2, banda infrarroja gaussiana (pico 0,02 de absorbancia, FWHM 5 cm^-1) y fuerza de banda A = 1,0e-17 cm/molecula (valor ilustrativo, NO consultado).
Modelo: flujo de Hertz-Knudsen Phi = P / sqrt(2 pi m k T); espesor N = ln(10) * integral(absorbancia dnu) / A; camara bien mezclada dn/dt = Q/V - n/tau, tau = V/S.
Referencias independientes: (a) coeficiente de manual 3,51e22 / sqrt(M T) [molec cm^-2 s^-1 por Torr] recordado, no consultado, frente a la derivacion desde CODATA;
(b) integral gaussiana cerrada frente a Simpson; (c) balance de masa: moleculas bombeadas = moleculas depositadas; presion de la camara frente al estado cuasiestacionario Q/S.
Tolerancias: coeficiente < 0,5 %; Simpson < 1e-8 relativa; balance de masa < 1e-3; retraso de bombeo < 10 %.
Unidades: P en mbar, flujo en moleculas cm^-2 s^-1, tiempo en s.
"""
from __future__ import annotations
import math, platform

KB = 1.380649e-23
U = 1.66053906892e-27
TORR = 101325.0 / 760.0
MBAR = 100.0
ML = 1e15
M_MOLAR = {"CO": 28.010, "H2O": 18.015}


def flujo(P_mbar: float, M_gmol: float, T: float = 300.0) -> float:
    """Hertz-Knudsen en moleculas cm^-2 s^-1."""
    m = M_gmol * U
    return P_mbar * MBAR / math.sqrt(2.0 * math.pi * m * KB * T) * 1e-4


def t_monocapa(P_mbar: float, M: float, T: float = 300.0, adhesion: float = 1.0) -> float:
    return ML / (adhesion * flujo(P_mbar, M, T))


def simpson(f, a, b, n=2000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3.0


def espesor_ml(pico, fwhm, A, nu0=2140.0, n=4000):
    sig = fwhm / (2.0 * math.sqrt(2.0 * math.log(2.0)))
    f = lambda nu: pico * math.exp(-0.5 * ((nu - nu0) / sig) ** 2)
    area = simpson(f, nu0 - 8 * sig, nu0 + 8 * sig, n)
    area_cerrada = pico * sig * math.sqrt(2.0 * math.pi)
    N = math.log(10.0) * area / A / ML
    return N, area, area_cerrada


def tpd_camara(E=1040.0, nu=8.7e14, beta=0.2, N0=10.0, T0=10.0, area=1.0, V_l=20.0, S_ls=100.0, dt=0.01):
    """Pelicula de orden cero que se desorbe con rampa; camara bien mezclada. Devuelve (retraso del pico, balance de masa, P pico, T_fin)."""
    V = V_l * 1e3          # cm^3
    S = S_ls * 1e3         # cm^3 s^-1
    tau = V / S
    t, n, N = 0.0, 0.0, N0
    T = T0
    bombeadas = 0.0
    Qpico, npico = 0.0, 0.0
    Tfin = None
    def Q(Ti, Ni):
        return area * ML * nu * math.exp(-E / Ti) if Ni > 0 else 0.0
    while t < 400.0:
        Ti = T0 + beta * t
        q = Q(Ti, N)
        # la pelicula pierde N (ML) a tasa k0; paso con limite para no pasar de cero
        dN = min(N, nu * math.exp(-E / Ti) * dt)
        if N > 0 and dN >= N and Tfin is None:
            Tfin = Ti
        q_eff = dN * area * ML / dt
        # camara: dn/dt = q_eff/V - n/tau (exponencial exacta en el paso)
        n_inf = q_eff * tau / V
        n_new = n_inf + (n - n_inf) * math.exp(-dt / tau)
        bombeadas += S * 0.5 * (n + n_new) * dt
        if q_eff * tau / V > Qpico:
            Qpico = q_eff * tau / V
        if n_new > npico:
            npico = n_new
        N -= dN
        n = n_new
        t += dt
        if N <= 0 and n < 1e-12 * max(npico, 1.0):
            break
    depositadas = N0 * area * ML
    retraso = 1.0 - npico / Qpico
    P_pico_mbar = npico * 1e6 * KB * 300.0 / MBAR  # n cm^-3 -> m^-3 ; P = n k T [Pa] -> mbar
    return retraso, bombeadas / depositadas - 1.0, P_pico_mbar, Tfin


def calcular():
    # (a) coeficiente
    coef_derivado = TORR / math.sqrt(2.0 * math.pi * U * KB) * 1e-4
    coef_manual = 3.51e22
    # (b) tiempos de monocapa
    Ps = (1e-11, 1e-10, 1e-9, 1e-8, 1e-7)
    t_h2o = [(P, t_monocapa(P, M_MOLAR["H2O"])) for P in Ps]
    t_co = [(P, t_monocapa(P, M_MOLAR["CO"])) for P in Ps]
    # langmuir: dosis de 1 L a 1e-6 Torr x 1 s
    P_1L_mbar = 1e-6 * TORR / MBAR
    ML_por_L = flujo(P_1L_mbar, M_MOLAR["CO"]) * 1.0 / ML
    # deposicion de 10 ML de CO por dosificacion de fondo
    t_dep = {P: 10.0 * ML / flujo(P, M_MOLAR["CO"]) for P in (1e-9, 1e-8, 1e-7)}
    # espesor por infrarrojo
    N, area_num, area_cer = espesor_ml(0.02, 5.0, 1.0e-17)
    # TPD con camara
    retraso, balance, P_pico, Tfin = tpd_camara()
    retraso_lento, _, _, _ = tpd_camara(S_ls=10.0)
    return dict(coef_derivado=coef_derivado, coef_manual=coef_manual, t_h2o=t_h2o, t_co=t_co, ML_por_L=ML_por_L, t_dep=t_dep,
                N=N, area_num=area_num, area_cer=area_cer, retraso=retraso, balance=balance, P_pico=P_pico, Tfin=Tfin, retraso_lento=retraso_lento)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Coeficiente de Hertz-Knudsen derivado de CODATA = {r['coef_derivado']:.4e} molec cm^-2 s^-1 Torr^-1 g^0.5 mol^-0.5 K^0.5 ; coeficiente de manual (no consultado) = {r['coef_manual']:.2e} ; dif. = {abs(r['coef_derivado'] / r['coef_manual'] - 1) * 100:.2f} %")
    print("Tiempo para cubrir 1 ML con probabilidad de adhesion 1, gas a 300 K (SINTETICO en P):")
    print(f"{'P [mbar]':>10} {'H2O [s]':>14} {'CO [s]':>14}")
    for (P, th), (_, tc) in zip(r["t_h2o"], r["t_co"]):
        print(f"{P:10.0e} {th:14.4e} {tc:14.4e}")
    print(f"1 langmuir (1e-6 Torr s) de CO a 300 K = {r['ML_por_L']:.3f} ML")
    print("Tiempo para depositar 10 ML de CO por dosificacion de fondo: " + " ; ".join(f"{P:.0e} mbar -> {t:.2f} s" for P, t in r["t_dep"].items()))
    print(f"Espesor por infrarrojo (banda gaussiana SINTETICA, A = 1e-17 cm/molec ilustrativa): area Simpson = {r['area_num']:.6f} cm^-1 ; cerrada = {r['area_cer']:.6f} cm^-1 ; N = {r['N']:.2f} ML")
    print(f"TPD de 10 ML de CO (E = 1040 K, nu = 8.7e14 ML/s, 0.2 K/s) en camara de 20 L: T_fin = {r['Tfin']:.2f} K ; P pico (area 1 cm^2, S = 100 L/s) = {r['P_pico']:.2e} mbar")
    print(f"Retraso del bombeo en el pico: S = 100 L/s -> {r['retraso'] * 100:.2f} % ; S = 10 L/s -> {r['retraso_lento'] * 100:.2f} % ; balance de masa = {r['balance']:.2e}")
    # pruebas
    assert abs(r["coef_derivado"] / r["coef_manual"] - 1) < 0.005
    assert abs(r["area_num"] / r["area_cer"] - 1) < 1e-8
    assert 0.2 < r["ML_por_L"] < 1.0   # 1 L es del orden de una fraccion de ML con adhesion 1
    assert abs(r["balance"]) < 1e-3
    assert 0 < r["retraso"] < 0.10 and r["retraso_lento"] > r["retraso"]
    th = [t for _, t in r["t_h2o"]]
    assert all(a > b for a, b in zip(th, th[1:]))
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
