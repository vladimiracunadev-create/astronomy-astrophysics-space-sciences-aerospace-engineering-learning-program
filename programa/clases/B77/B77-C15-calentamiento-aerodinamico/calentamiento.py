#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B77-C15: calentamiento aerodinamico de punto de remanso (Sutton-Graves) a lo largo de una entrada balistica.

Datos consultados (2026-11-10): diapositivas TFAWS 2012 (lectura con PyMuPDF): q_s = k sqrt(rho/R_n) V^3 con k = 1.7415e-4 (Tierra), SI, y el ejemplo resuelto:
rho = 3.1459e-4 kg/m3, V = 3.535 km/s, R_n = 1 m -> q = 13.6 W/cm2; emisividad 0.8, sigma = 5.67e-8 -> T_w = 1316 K en equilibrio radiativo.
Registro NTRS de Sutton y Graves (NASA TR R-376, 1971; solo el registro). rho0 = 1.217 kg/m3 y H = 8.5 km (NASA/NSSDC Earth Fact Sheet).
ILUSTRATIVOS (sinteticos): entrada de C14 (v_E = 7800 m/s, gamma_E = 5 grados, trayectoria recta, sin gravedad), beta = 100, 300, 1000 kg/m2,
radios de nariz R_n = 0.3, 1.0 m, emisividad 0.8. Se desprecia el calentamiento radiativo del gas y la correccion de pared caliente.
Sistema: plano vertical local, SI; el flujo q esta en W/m2 (1 W/cm2 = 1e4 W/m2).
Modelo: v(h) = v_E exp(-K e^(-h/H)); q(h) = k sqrt(rho/R_n) v^3; T_w = (q/(eps sigma))^(1/4); Q = integral q dt = integral q dh/(v sin gamma).
Segunda via: maximo analitico en e^(-h/H) = 1/(6K) con v_pico = v_E e^(-1/6), y carga Q ~ k sqrt(rho0/R_n) H v_E^2 [sqrt(pi/(2K)) - 2 sqrt(x_E)]/sin gamma (x_E = e^(-120 km/H) corrige el inicio a 120 km); el ejemplo de TFAWS como prueba de unidades.
Tolerancias: ejemplo TFAWS 0.5 % en q y 0.2 % en T_w; pico numerico frente a analitico 1e-3; carga Q 1 %.
"""
import math, platform

RHO0, H = 1.217, 8500.0
K_SG, SIGMA, EPS = 1.7415e-4, 5.67e-8, 0.8
VE, GAM = 7800.0, math.radians(5.0)


def flujo(rho, v, rn):
    return K_SG * math.sqrt(rho / rn) * v ** 3


def temp_eq(q):
    return (q / (EPS * SIGMA)) ** 0.25


def perfil(beta, rn, n=20000):
    s = math.sin(GAM)
    K = RHO0 * H / (2 * beta * s)
    hmax, hmin = 120e3, 0.0
    dh = (hmax - hmin) / n
    qpk, hpk, Q, prev = 0.0, 0.0, 0.0, None
    for i in range(n + 1):
        h = hmax - i * dh
        x = math.exp(-h / H)
        v = VE * math.exp(-K * x)
        q = flujo(RHO0 * x, v, rn)
        if q > qpk:
            qpk, hpk = q, h
        integrando = q / (v * s)
        if prev is not None:
            Q += 0.5 * (prev + integrando) * dh
        prev = integrando
    xa = 1 / (6 * K)
    q_an = flujo(RHO0 * xa, VE * math.exp(-1 / 6), rn)
    xe = math.exp(-120e3 / H)
    Q_an = K_SG * math.sqrt(RHO0 / rn) * H * VE ** 2 * (math.sqrt(math.pi / (2 * K)) - 2 * math.sqrt(xe)) / s
    return dict(beta=beta, rn=rn, K=K, q_pico=qpk, h_pico=hpk, q_an=q_an, h_an=H * math.log(6 * K), Q=Q, Q_an=Q_an, T=temp_eq(qpk))


def calcular():
    r = {}
    q_t = flujo(3.1459e-4, 3535.0, 1.0)
    r["tfaws_q"], r["tfaws_T"] = q_t / 1e4, temp_eq(q_t)
    r["err_q_tfaws"] = abs(r["tfaws_q"] - 13.6) / 13.6
    r["err_T_tfaws"] = abs(r["tfaws_T"] - 1316.0) / 1316.0
    r["casos"] = [perfil(b, rn) for b in (100.0, 300.0, 1000.0) for rn in (0.3, 1.0)]
    r["err_pico"] = max(abs(c["q_pico"] - c["q_an"]) / c["q_an"] for c in r["casos"])
    r["err_Q"] = max(abs(c["Q"] - c["Q_an"]) / c["Q_an"] for c in r["casos"])
    return r


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calcular()
    print(f"Prueba con el ejemplo de TFAWS 2012: q = {r['tfaws_q']:.2f} W/cm2 (publicado 13.6; error {r['err_q_tfaws']:.1e}); T_w = {r['tfaws_T']:.1f} K (publicado 1316; error {r['err_T_tfaws']:.1e})")
    print(f"Entrada SINTETICA (v_E = {VE:.0f} m/s, gamma_E = 5 grados), nariz R_n y beta ILUSTRATIVOS; epsilon = {EPS}")
    print(" beta   R_n [m]   q_pico [W/cm2]  h_pico num/analit. [km]   T_w [K]   Q [MJ/m2] num / analit.")
    for c in r["casos"]:
        print(f"  {c['beta']:5.0f}  {c['rn']:5.1f}  {c['q_pico']/1e4:12.1f}  {c['h_pico']/1e3:9.2f}/{c['h_an']/1e3:6.2f}  {c['T']:9.0f}  {c['Q']/1e6:8.2f} / {c['Q_an']/1e6:6.2f}")
    print(f"Errores relativos maximos: pico {r['err_pico']:.1e}; carga termica {r['err_Q']:.1e}")
    assert r["err_q_tfaws"] < 5e-3 and r["err_T_tfaws"] < 2e-3
    assert r["err_pico"] < 1e-3 and r["err_Q"] < 1e-2
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
