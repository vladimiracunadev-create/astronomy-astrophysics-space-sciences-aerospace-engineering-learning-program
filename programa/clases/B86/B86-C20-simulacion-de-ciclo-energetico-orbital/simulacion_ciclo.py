#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C20: simulacion acoplada del ciclo energetico orbital de un satelite SINTETICO durante 30 dias.

Datos consultados (2026-11-10): GM = 0.39860e6 km3/s2 y radio medio 6371.000 km (NASA/NSSDC) para el periodo y el eclipse (sombra cilindrica) de una orbita de 600 km.
ILUSTRATIVOS (sinteticos): angulo beta que crece linealmente de 0 a 50 grados en 30 dias, ala de un eje (coseno = cos beta) con P_BOL = 286.67 W y factor de fin de vida 0.8858 a 5 anos
(B86-C14, aplicado como degradacion lineal de la potencia entre 0 y 5 anos desde el dia 1500), cargas de 100.8 W en luz y 64.8 W en eclipse (B86-C01), bateria de 259.2 Wh (B86-C05),
eficiencias de carga 0.97 y descarga 0.95, potencia maxima de carga 70 W, SOC inicial 80 %, paso de 10 s; caso B con 45 W adicionales de carga util en luz.
Modelo: balance de energia de la bateria con un bus directo; la generacion que no se puede almacenar se descarta (curtailment).
Segunda via: cierre del balance global (generacion potencial = cargas + perdidas de carga y descarga + generacion descartada + variacion de la energia de la bateria) y energia de una orbita integrada en forma cerrada
para el dia 0 (potencia constante en luz).
Tolerancia: residuo del balance global < 1e-6 Wh; energia generada del dia 0 por simulacion frente a la formula cerrada < 1e-6 Wh.
"""
from __future__ import annotations
import math, platform

MU, RE, H = 398600.0, 6371.0, 600.0
A = RE + H
T = 2.0 * math.pi * math.sqrt(A ** 3 / MU)
DIAS = 30
E_NOM, ETA_C, ETA_D, P_CHG = 259.2, 0.97, 0.95, 70.0
P_BOL, F_EOL5, DIA_INICIO = 286.67, 0.8858, 1500.0
P_LUZ, P_ECL = 100.8, 64.8


def beta(t):
    return math.radians(50.0 * t / (DIAS * 86400.0))


def fraccion_eclipse(b):
    s = math.sqrt(H * H + 2.0 * RE * H) / (A * math.cos(b))
    return 0.0 if abs(b) >= math.asin(RE / A) else math.acos(s) / math.pi


def potencia_ala(t):
    anos = (DIA_INICIO + t / 86400.0) / 365.25
    f = 1.0 - (1.0 - F_EOL5) * anos / 5.0
    return P_BOL * f * math.cos(beta(t))


def simular(p_luz, dt=10.0, soc0=0.8):
    e = soc0 * E_NOM
    r = dict(gen=0.0, carga=0.0, perd_c=0.0, perd_d=0.0, desc=0.0, soc_min=1.0, t_min=0.0, orb_min=0, soc_orbita=[])
    e0 = e
    n_orb = int(DIAS * 86400.0 / T)
    for k in range(n_orb):
        t0 = k * T
        b = beta(t0 + 0.5 * T)
        te = fraccion_eclipse(b) * T
        td = T - te
        t = 0.0
        while t < T - 1e-9:
            h = min(dt, (td if t < td else T) - t)
            tt = t0 + t
            hh = h / 3600.0
            if t < td:
                pg = potencia_ala(tt + 0.5 * h)
                r["gen"] += pg * hh
                r["carga"] += p_luz * hh
                s = pg - p_luz
                if s >= 0.0:
                    pc = min(s, P_CHG, (E_NOM - e) / (ETA_C * hh))
                    e += pc * ETA_C * hh
                    r["perd_c"] += pc * (1.0 - ETA_C) * hh
                    r["desc"] += (s - pc) * hh
                else:
                    dem = -s
                    e -= dem / ETA_D * hh
                    r["perd_d"] += dem * (1.0 / ETA_D - 1.0) * hh
            else:
                r["carga"] += P_ECL * hh
                e -= P_ECL / ETA_D * hh
                r["perd_d"] += P_ECL * (1.0 / ETA_D - 1.0) * hh
            if k >= 1 and e / E_NOM < r["soc_min"]:      # se excluye la orbita 1 (condicion inicial)
                r["soc_min"], r["t_min"], r["orb_min"] = e / E_NOM, tt, k
            t += h
        r["soc_orbita"].append(e / E_NOM)
    r["dE"] = e - e0
    r["e_fin"] = e
    r["n_orb"] = n_orb
    r["resid"] = abs(r["gen"] - (r["carga"] + r["perd_c"] + r["perd_d"] + r["desc"] + r["dE"]))
    return r


def resultados():
    a, b = simular(P_LUZ), simular(P_LUZ + 45.0)
    r = {"a": a, "b": b, "n_orb": a["n_orb"], "T": T}
    for pre, x in (("a", a), ("b", b)):
        r[f"{pre}_soc_min"] = x["soc_min"] * 100.0
        r[f"{pre}_orb_min"] = x["orb_min"] + 1
        r[f"{pre}_dia_min"] = x["t_min"] / 86400.0
        r[f"{pre}_gen"], r[f"{pre}_carga"], r[f"{pre}_desc"] = x["gen"], x["carga"], x["desc"]
        r[f"{pre}_perd"] = x["perd_c"] + x["perd_d"]
        r[f"{pre}_dE"], r[f"{pre}_resid"] = x["dE"], x["resid"]
        r[f"{pre}_soc_fin"] = x["soc_orbita"][-1] * 100.0
        r[f"{pre}_soc_med"] = 100.0 * sum(x["soc_orbita"]) / len(x["soc_orbita"])
        r[f"{pre}_pct_desc"] = x["desc"] / x["gen"] * 100.0
    # primera orbita: energia generada por formula cerrada (potencia constante en luz durante td)
    b0 = beta(0.5 * T)
    td0 = T - fraccion_eclipse(b0) * T
    # la potencia varia muy poco en una orbita: integral exacta de la rampa lineal de cos(beta) se aproxima por el trapecio exacto del integrando
    n = 20000
    h = td0 / n
    s = sum(potencia_ala(k * h) for k in range(1, n)) + 0.5 * (potencia_ala(0.0) + potencia_ala(td0))
    r["E_orb0_cerr"] = s * h / 3600.0
    # simulacion de la primera orbita sola
    e_sim = 0.0
    t = 0.0
    while t < td0 - 1e-9:
        hh = min(10.0, td0 - t)
        e_sim += potencia_ala(t + 0.5 * hh) * hh / 3600.0
        t += hh
    r["E_orb0_sim"] = e_sim
    r["dE_orb0"] = abs(e_sim - r["E_orb0_cerr"])
    r["fe0_pct"] = fraccion_eclipse(b0) * 100.0
    r["fe_fin_pct"] = fraccion_eclipse(beta(DIAS * 86400.0 - 0.5 * T)) * 100.0
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Orbita SINTETICA 600 km: T = {T:.1f} s ; {r['n_orb']} orbitas en {DIAS} dias ; beta de 0 a 50 grados ; eclipse de {r['fe0_pct']:.2f} % a {r['fe_fin_pct']:.2f} %")
    print(" caso                      SOC min [%]  orbita (dia)    SOC fin [%]  SOC medio [%]  gen [Wh]   carga [Wh]  perdidas [Wh]  descartada [Wh] (%)   residuo [Wh]")
    for pre, n in (("a", "A: cargas nominales"), ("b", "B: +45 W de carga util")):
        print(f" {n:<24} {r[pre+'_soc_min']:9.2f}   {r[pre+'_orb_min']:5d} ({r[pre+'_dia_min']:4.1f})  {r[pre+'_soc_fin']:11.2f}  {r[pre+'_soc_med']:12.2f}  {r[pre+'_gen']:9.0f}  {r[pre+'_carga']:10.0f}  {r[pre+'_perd']:12.1f}  {r[pre+'_desc']:10.0f} ({r[pre+'_pct_desc']:4.1f})  {r[pre+'_resid']:.1e}")
    print(f"Energia generada en la primera luz: simulacion = {r['E_orb0_sim']:.6f} Wh ; integral = {r['E_orb0_cerr']:.6f} Wh ; diferencia = {r['dE_orb0']:.1e} Wh")
    assert r["a_resid"] < 1e-6 and r["b_resid"] < 1e-6
    assert r["dE_orb0"] < 1e-6
    assert r["a_soc_min"] > 0.0 and 0.0 < r["b_soc_min"] < r["a_soc_min"]   # SOC fisicamente valido (> 0)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
