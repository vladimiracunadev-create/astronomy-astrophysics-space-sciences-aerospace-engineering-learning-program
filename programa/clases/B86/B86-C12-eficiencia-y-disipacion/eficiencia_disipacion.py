#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C12: cadena de eficiencias, calor a disipar y area de radiador de un subsistema de potencia SINTETICO.

Datos consultados (2026-11-10): constante de Stefan-Boltzmann sigma = 5.670374419e-8 W m-2 K-4 (NIST, CODATA 2022).
ILUSTRATIVOS (sinteticos, no medidos): carga util de 100.8 W (B86-C01 en luz); eficiencias de etapa: convertidores 0.92, PCDU 0.95, seguidor del punto de maxima potencia 0.97;
camino de bateria: carga 0.97 y descarga 0.95; emisividad 0.85; temperatura del radiador 300 K; temperatura de sumidero equivalente 220 K (valor ilustrativo que agrupa
espacio profundo, Tierra y Sol sin modelarlos; NO es un balance termico real).
Modelo: P_in = P_out / prod(eta_i); calor de cada etapa = P_in,i - P_out,i; Q = eps sigma A (T^4 - Ts^4).
Segunda via: temperatura del radiador para un area dada por Newton (T^4 = Ts^4 + Q/(eps sigma A)) frente a la inversa cerrada del area.
Tolerancia: balance de energia de la cadena con residuo < 1e-9 W; T de Newton frente a la nominal < 1e-6 K.
"""
from __future__ import annotations
import math, platform

SIGMA = 5.670374419e-8
P_CARGA = 100.8
ETAPAS = [("Convertidores DC-DC", 0.92), ("PCDU (distribucion)", 0.95), ("Seguidor del punto de maxima potencia", 0.97)]
ETA_CARGA, ETA_DESC = 0.97, 0.95
EPS, T_RAD, T_SUM = 0.85, 300.0, 220.0


def cadena(p_out):
    filas = []
    p = p_out
    for nombre, eta in ETAPAS:
        p_in = p / eta
        filas.append((nombre, eta, p_in, p, p_in - p))
        p = p_in
    return filas, p


def area_radiador(q, t=T_RAD, ts=T_SUM, eps=EPS):
    return q / (eps * SIGMA * (t ** 4 - ts ** 4))


def temperatura(q, a, ts=T_SUM, eps=EPS):
    t = 300.0
    for _ in range(100):
        f = eps * SIGMA * a * (t ** 4 - ts ** 4) - q
        df = 4.0 * eps * SIGMA * a * t ** 3
        d = f / df
        t -= d
        if abs(d) < 1e-12:
            break
    return t


def resultados():
    filas, p_array = cadena(P_CARGA)
    calor = sum(f[4] for f in filas)
    eta_total = P_CARGA / p_array
    r = dict(filas=filas, P_array=p_array, Q_cadena=calor, eta_total=eta_total, eta_total_pct=eta_total * 100.0,
             resbal=abs(p_array - P_CARGA - calor))
    # camino de bateria: energia que pasa por la bateria en el eclipse (64.8 W durante 2125.6 s) y calor de ida y vuelta
    e_ecl = 64.8 * 2125.6 / 3600.0
    e_bat_in = e_ecl / ETA_DESC / ETA_CARGA
    r["eta_ciclo_bat"] = ETA_CARGA * ETA_DESC
    r["E_ecl"], r["E_bat_in"], r["Q_bat_Wh"] = e_ecl, e_bat_in, e_bat_in - e_ecl
    r["Q_bat_medio"] = r["Q_bat_Wh"] * 3600.0 / 5792.3
    q_tot = calor + r["Q_bat_medio"]
    r["Q_total"] = q_tot
    a = area_radiador(q_tot)
    r["A_rad"] = a
    r["flujo"] = q_tot / a
    r["T_newton"] = temperatura(q_tot, a)
    r["dT"] = abs(r["T_newton"] - T_RAD)
    r["A280"], r["A320"] = area_radiador(q_tot, 280.0), area_radiador(q_tot, 320.0)
    r["A_eta85"] = area_radiador(calor_con_eta(0.85) + r["Q_bat_medio"])
    r["Q_eta85"] = calor_con_eta(0.85)
    r["T_con_mitad"] = temperatura(q_tot, a / 2.0)
    for k, (n, eta, pi, po, q) in enumerate(filas, 1):
        r[f"e{k}_in"], r[f"e{k}_out"], r[f"e{k}_q"] = pi, po, q
    r["A_eps"] = a * 0.85 / 0.5
    r["A10"] = 10.0 / r["flujo"]
    return r


def calor_con_eta(eta_conv):
    f, p = cadena_con(P_CARGA, eta_conv)
    return p - P_CARGA


def cadena_con(p_out, eta_conv):
    p = p_out
    for nombre, eta in [("c", eta_conv)] + ETAPAS[1:]:
        p = p / eta
    return None, p


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Cadena SINTETICA de potencia en luz: carga util = {P_CARGA} W")
    print(" etapa                                  eta     P_in [W]  P_out [W]  calor [W]")
    for n, eta, pi, po, q in r["filas"]:
        print(f" {n:<38} {eta:5.2f}   {pi:9.3f}  {po:9.3f}  {q:9.3f}")
    print(f"Potencia de ala necesaria = {r['P_array']:.3f} W ; eficiencia total = {r['eta_total_pct']:.2f} % ; calor de la cadena = {r['Q_cadena']:.3f} W ; residuo del balance = {r['resbal']:.1e} W")
    print(f"Camino de bateria en el eclipse: {r['E_ecl']:.2f} Wh a la carga ; {r['E_bat_in']:.2f} Wh de carga ; calor del ciclo = {r['Q_bat_Wh']:.2f} Wh ({r['Q_bat_medio']:.3f} W promedio por orbita)")
    print(f"Calor medio a evacuar = {r['Q_total']:.3f} W")
    print(f"Radiador (eps = {EPS}, T = {T_RAD:.0f} K, sumidero equivalente {T_SUM:.0f} K): A = {r['A_rad']:.4f} m2 ; flujo = {r['flujo']/(1):.1f} W/m2 sobre {r['A_rad']:.4f} m2")
    print(f"Con T = 280 K: A = {r['A280']:.4f} m2 ; con T = 320 K: A = {r['A320']:.4f} m2")
    print(f"Temperatura de Newton para esa area = {r['T_newton']:.6f} K (dif {r['dT']:.1e} K) ; con la mitad del area = {r['T_con_mitad']:.2f} K")
    print(f"Si los convertidores bajan a eta = 0.85: calor de la cadena = {r['Q_eta85']:.3f} W ; A = {r['A_eta85']:.4f} m2")
    assert r["resbal"] < 1e-9
    assert r["dT"] < 1e-6
    assert r["A280"] > r["A_rad"] > r["A320"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
