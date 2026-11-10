#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C13: energia durante el eclipse y cierre del ciclo de carga orbita a orbita (modelo de energia SINTETICO).

Datos consultados (2026-11-10): GM = 0.39860e6 km3/s2 y radio medio 6371.000 km (NASA/NSSDC) para el periodo y el eclipse de una orbita de 600 km con beta = 0.
ILUSTRATIVOS (sinteticos, no medidos): bateria de 259.2 Wh (B86-C05), eficiencias de carga 0.97 y de descarga 0.95, potencia maxima de carga 70 W,
cargas de 100.8 W en luz y 64.8 W en eclipse (B86-C01), generacion del ala 243.67 W (caso nominal) y 110 W (caso degradado), SOC inicial 80 %, 40 orbitas.
Modelo: balance de energia con paso de 5 s; en la luz la bateria recibe min(excedente, 70 W) hasta SOC = 100 %; en el eclipse entrega P_e / eta_d.
Segunda via: balance por orbita en forma cerrada (energia de eclipse desde la bateria; energia recuperable en la luz) y deficit por orbita del caso degradado.
Tolerancia: SOC periodico del caso nominal con variacion < 1e-9 entre orbitas; pendiente simulada del caso degradado frente al deficit cerrado < 1e-6 Wh por orbita.
"""
from __future__ import annotations
import math, platform

MU, RE, H = 398600.0, 6371.0, 600.0
A = RE + H
T = 2.0 * math.pi * math.sqrt(A ** 3 / MU)
TE = math.asin(RE / A) / math.pi * T
TD = T - TE
E_NOM, ETA_C, ETA_D, P_CHG = 259.2, 0.97, 0.95, 70.0
P_LUZ, P_ECL = 100.8, 64.8


def simular(p_gen, soc0=0.8, orbitas=40, dt=5.0):
    e = soc0 * E_NOM
    soc_ini = []
    t_pleno = None
    for k in range(orbitas):
        soc_ini.append(e / E_NOM)
        t = 0.0
        while t < T - 1e-9:
            h = min(dt, (TD if t < TD else T) - t)
            if t < TD:
                exc = p_gen - P_LUZ
                if exc > 0.0:
                    pc = min(exc, P_CHG)
                    e = min(E_NOM, e + pc * ETA_C * h / 3600.0)
                else:
                    e += exc / ETA_D * h / 3600.0
            else:
                e -= P_ECL / ETA_D * h / 3600.0
            if e <= 0.0:
                return soc_ini, k, 0.0
            t += h
    return soc_ini, None, e / E_NOM


def resultados():
    r = dict(T=T, Te=TE, Td=TD)
    r["E_ecl"] = P_ECL * TE / 3600.0
    r["E_bat_ecl"] = r["E_ecl"] / ETA_D
    r["DoD_ecl"] = r["E_bat_ecl"] / E_NOM
    r["t_recarga"] = r["E_bat_ecl"] / (P_CHG * ETA_C) * 3600.0
    r["frac_luz"] = r["t_recarga"] / TD
    s1, fallo1, fin1 = simular(243.67)
    r["soc_nom"] = s1
    r["soc_nom_ini"], r["soc_nom_fin"] = s1[0], s1[-1]
    r["dsoc_nom"] = abs(s1[-1] - s1[-2])
    r["soc_max_nom"] = max(s1)
    s2, fallo2, fin2 = simular(110.0)
    r["soc_deg"] = s2
    r["fallo_orbita"] = fallo2
    r["recarga_deg"] = (110.0 - P_LUZ) * ETA_C * TD / 3600.0     # Wh por orbita (excedente 9.2 W)
    r["deficit_orb"] = r["E_bat_ecl"] - r["recarga_deg"]            # Wh por orbita
    r["pend_sim"] = (s2[1] - s2[2]) * E_NOM if len(s2) > 2 else 0.0
    r["dif_pend"] = abs(r["pend_sim"] - r["deficit_orb"])
    r["orb_agota"] = (s2[0] * E_NOM) / r["deficit_orb"] if r["deficit_orb"] > 0 else math.inf
    r["gen_min"] = P_LUZ + (r["E_bat_ecl"] * 3600.0 / (ETA_C * TD))   # W de ala minima para cerrar el ciclo
    r["ecl_pct"] = 100.0 * TE / T
    r["s0_nom"] = s1[0]
    r["fallo_nom"] = fallo1
    r["DoD_ecl_pct"] = r["DoD_ecl"] * 100.0
    r["frac_luz_pct"] = r["frac_luz"] * 100.0
    for k, i in (("n1", 0), ("n2", 1), ("n3", 2), ("n40", 39)):
        r[k] = s1[i] * 100.0
    r["t_recarga2"] = 2.0 * r["t_recarga"]
    r["def5"] = r["E_bat_ecl"] - 5.0 * ETA_C * TD / 3600.0
    r["gen120"] = 120.0 + r["E_bat_ecl"] * 3600.0 / (ETA_C * TD)
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Orbita SINTETICA 600 km, beta = 0: T = {T:.1f} s ; eclipse = {TE:.1f} s ({r['ecl_pct']:.2f} %) ; luz = {TD:.1f} s")
    print(f"Energia del eclipse a la carga = {r['E_ecl']:.2f} Wh ; desde la bateria = {r['E_bat_ecl']:.2f} Wh ; DoD por eclipse = {r['DoD_ecl']*100:.2f} %")
    print(f"Tiempo de recarga a {P_CHG:.0f} W = {r['t_recarga']:.0f} s ({r['frac_luz']*100:.1f} % de la luz)")
    print("Caso nominal (ala 243.67 W): SOC al inicio de cada orbita (orbitas 1, 2, 3, 40):", ", ".join(f"{r['soc_nom'][k]*100:.3f} %" for k in (0, 1, 2, 39)))
    print(f"  variacion del SOC entre las dos ultimas orbitas = {r['dsoc_nom']:.2e} ; SOC maximo = {r['soc_max_nom']*100:.3f} %")
    print("Caso degradado (ala 110 W): SOC al inicio de las orbitas 1, 2, 3, 10:", ", ".join(f"{r['soc_deg'][k]*100:.3f} %" for k in (0, 1, 2, 9)) if len(r["soc_deg"]) > 9 else "agotada antes de la orbita 10")
    print(f"  deficit por orbita (cerrado) = {r['deficit_orb']:.4f} Wh ; pendiente simulada = {r['pend_sim']:.4f} Wh ; diferencia = {r['dif_pend']:.1e} Wh")
    print(f"  la bateria se agota hacia la orbita {r['orb_agota']:.1f} ; (la simulacion la agota en la orbita {r['fallo_orbita']})")
    print(f"Generacion minima del ala para cerrar el ciclo (con cargas de luz) = {r['gen_min']:.2f} W")
    assert r["fallo_nom"] is None and r["dsoc_nom"] < 1e-9
    assert r["dif_pend"] < 1e-6
    assert r["fallo_orbita"] is not None
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
