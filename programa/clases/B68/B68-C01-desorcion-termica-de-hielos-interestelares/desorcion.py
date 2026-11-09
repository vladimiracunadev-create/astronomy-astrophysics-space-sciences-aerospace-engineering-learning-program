#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B68-C01: desorcion termica de hielos (Polanyi-Wigner de orden cero y uno) y TPD.

Datos: energias de enlace E [K] y factores preexponenciales nu [ML s^-1] de capa multiple y orden cero tomados de la Tabla 3 de
Kruczkiewicz et al. (2024, A&A, arXiv:2404.02695), consultada el 2026-11-09: CO (1040 K; 8,7e14), CH3OH (5531 K; 8,8e16) y H2O amorfa (6638 K; 8,7e17).
Tambien se usa el valor de CO de Minissale et al. (2022) tal como lo cita esa tabla (1390 K; 9,14e14 s^-1) y el de Fraser et al. (2001, resumen):
E = 5773 K, A = 1e30 molec cm^-2 s^-1. Convencion del curso: 1 ML = 1e15 moleculas cm^-2 (convencion, no medida).
SINTETICO / ILUSTRATIVO: el espesor inicial (10 ML), el factor de primer orden (1e13 s^-1) y la escala de 1e6 anos. No se simula ninguna nube real.
Modelo: k0(T) = nu exp(-E/T) [ML s^-1] (orden cero); rampa lineal T = T0 + beta t con beta = 0,2 K s^-1 (la de ese estudio).
Referencias independientes: (a) integral cerrada con la integral exponencial E1 (fraccion continua); (b) RK4 en T; (c) tiempo isotermico N0/k0.
Supuestos: especie pura, capa multiple, nu independiente de T. Tolerancias: T_fin cerrado frente a RK4 < 1e-3 K; aproximacion de Redhead < 5 %.
Unidades: temperatura en K, tiempo en s, espesor en ML.
"""
from __future__ import annotations
import math, platform

SEC_ANIO = 365.25 * 86400.0


def e1(x: float) -> float:
    """Integral exponencial E1(x) para x >= 1 por fraccion continua (Lentz modificado)."""
    b = x + 1.0
    c = 1.0 / 1e-300
    d = 1.0 / b
    h = d
    for i in range(1, 300):
        an = -i * i
        b += 2.0
        d = 1.0 / (an * d + b)
        c = b + an / c
        de = c * d
        h *= de
        if abs(de - 1.0) < 1e-15:
            break
    return h * math.exp(-x)


def k0(T: float, E: float, nu: float) -> float:
    return nu * math.exp(-E / T)


def F(T: float, E: float) -> float:
    """Primitiva de exp(-E/T): F = T exp(-E/T) - E E1(E/T)."""
    return T * math.exp(-E / T) - E * e1(E / T)


def t_fin_cerrado(N0: float, E: float, nu: float, beta: float, T0: float = 10.0) -> float:
    """Temperatura en que se agota una pelicula de orden cero: N0 = (nu/beta) [F(T) - F(T0)]."""
    objetivo = N0 * beta / nu + F(T0, E)
    lo, hi = T0, 400.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F(mid, E) < objetivo:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def t_fin_rk4(N0: float, E: float, nu: float, beta: float, T0: float = 10.0, dT: float = 0.002) -> float:
    """dN/dT = -(nu/beta) exp(-E/T) integrado con RK4; devuelve T donde N cruza 0 (interpolacion lineal)."""
    f = lambda T: -(nu / beta) * math.exp(-E / T)
    T, N = T0, N0
    while N > 0 and T < 400.0:
        k1 = f(T); k2 = f(T + dT / 2); k3 = f(T + dT / 2); k4 = f(T + dT)
        Nn = N + dT / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
        if Nn <= 0:
            return T + dT * N / (N - Nn)
        T, N = T + dT, Nn
    return T


def primer_orden_pico(E: float, nu1: float, beta: float, T0: float = 8.0, dT: float = 0.001):
    """TPD de primer orden: dtheta/dT = -(nu1/beta) exp(-E/T) theta; devuelve T del maximo de la tasa."""
    th, T = 1.0, T0
    mejor, Tp = 0.0, T0
    while T < 300.0 and th > 1e-12:
        r = (nu1 / beta) * math.exp(-E / T) * th
        if r > mejor:
            mejor, Tp = r, T
        # paso exacto del factor (exponencial) en el subintervalo, con k evaluada en el centro
        k = (nu1 / beta) * math.exp(-E / (T + dT / 2))
        th *= math.exp(-k * dT)
        T += dT
    return Tp


def redhead(Tp: float, nu1: float, beta: float) -> float:
    """E [K] = Tp (ln(nu1 Tp / beta) - 3,46) para primer orden."""
    return Tp * (math.log(nu1 * Tp / beta) - 3.46)


def T_para_vida(E: float, nu: float, t_s: float, N_ML: float = 1.0) -> float:
    """T tal que N_ML / k0(T) = t_s en orden cero."""
    return E / math.log(nu * t_s / N_ML)


def calcular():
    par = {"CO": (1040.0, 8.7e14), "CH3OH": (5531.0, 8.8e16), "H2O (amorfa)": (6638.0, 8.7e17)}
    beta, N0 = 0.2, 10.0
    tpd = []
    for nom, (E, nu) in par.items():
        Tc = t_fin_cerrado(N0, E, nu, beta)
        Tr = t_fin_rk4(N0, E, nu, beta)
        tpd.append((nom, E, nu, Tc, Tr, abs(Tc - Tr)))
    # tiempo isotermico (orden cero) de 1 ML de CO a distintas T
    iso = [(T, 1.0 / k0(T, 1040.0, 8.7e14)) for T in (15.0, 20.0, 25.0, 30.0)]
    # sensibilidad de T_fin del CO a E (+-10 %) y a beta
    E, nu = par["CO"]
    sens = {"E-10%": t_fin_cerrado(N0, 0.9 * E, nu, beta), "E": t_fin_cerrado(N0, E, nu, beta), "E+10%": t_fin_cerrado(N0, 1.1 * E, nu, beta)}
    beta_x = {b: t_fin_cerrado(N0, E, nu, b) for b in (0.02, 0.2, 2.0)}
    # Redhead: se genera una TPD de primer orden sintetica y se recupera E
    E_sint, nu1 = 1040.0, 1e13
    Tp = primer_orden_pico(E_sint, nu1, beta)
    E_rec = redhead(Tp, nu1, beta)
    # vida de 1 ML en 1e6 anos: dos juegos de parametros del CO de la tabla de Kruczkiewicz
    T_kru = T_para_vida(1040.0, 8.7e14, 1e6 * SEC_ANIO)
    T_min = T_para_vida(1390.0, 9.14e14, 1e6 * SEC_ANIO)
    # agua con los parametros de Fraser (nu = 1e30 cm^-2 s^-1 = 1e15 ML s^-1)
    T_fra = T_para_vida(5773.0, 1e15, 1e6 * SEC_ANIO)
    return dict(tpd=tpd, iso=iso, sens=sens, beta_x=beta_x, Tp=Tp, E_rec=E_rec, E_sint=E_sint, T_kru=T_kru, T_min=T_min, T_fra=T_fra,
                e1_chk=(e1(2.0), e1(10.0)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"E1(2) = {r['e1_chk'][0]:.10f} (tabulado 0.0489005107) ; E1(10) = {r['e1_chk'][1]:.6e} (tabulado 4.156969e-06)")
    print("TPD de orden cero, 10 ML, beta = 0.2 K/s (parametros de Kruczkiewicz 2024, Tabla 3)")
    print(f"{'especie':>14} {'E [K]':>7} {'nu [ML/s]':>10} {'T_fin cerrado [K]':>18} {'T_fin RK4 [K]':>14} {'|dif| [K]':>10}")
    for nom, E, nu, Tc, Tr, d in r["tpd"]:
        print(f"{nom:>14} {E:7.0f} {nu:10.2e} {Tc:18.4f} {Tr:14.4f} {d:10.2e}")
    print("Tiempo isotermico de 1 ML de CO (E = 1040 K, nu = 8.7e14 ML/s):")
    for T, t in r["iso"]:
        print(f"  T = {T:4.0f} K -> t = {t:.3e} s")
    s = r["sens"]
    print(f"Sensibilidad de T_fin del CO a E: -10 % -> {s['E-10%']:.2f} K ; nominal -> {s['E']:.2f} K ; +10 % -> {s['E+10%']:.2f} K")
    print("T_fin del CO segun beta: " + " ; ".join(f"{b:g} K/s -> {t:.2f} K" for b, t in r["beta_x"].items()))
    print(f"Primer orden SINTETICO (E = {r['E_sint']:.0f} K, nu = 1e13 s^-1): T_pico = {r['Tp']:.3f} K ; E por Redhead = {r['E_rec']:.1f} K ; error = {abs(r['E_rec'] / r['E_sint'] - 1) * 100:.2f} %")
    print(f"T con vida de 1 ML = 1e6 anos (SINTETICO): CO Kruczkiewicz = {r['T_kru']:.2f} K ; CO Minissale (1390 K) = {r['T_min']:.2f} K ; H2O Fraser = {r['T_fra']:.1f} K")
    # pruebas
    assert abs(r["e1_chk"][0] - 0.0489005107) < 1e-9 and abs(r["e1_chk"][1] / 4.156969e-06 - 1) < 1e-5
    for nom, E, nu, Tc, Tr, d in r["tpd"]:
        assert d < 1e-3, nom
    assert s["E-10%"] < s["E"] < s["E+10%"]
    b = r["beta_x"]
    assert b[0.02] < b[0.2] < b[2.0]
    assert abs(r["E_rec"] / r["E_sint"] - 1) < 0.05
    assert r["T_min"] > r["T_kru"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
