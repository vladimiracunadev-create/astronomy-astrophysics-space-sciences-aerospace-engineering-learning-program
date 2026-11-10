#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C16: potencia de un generador radioisotopico termoelectrico (tipo MMRTG) frente a las cifras publicadas por la NASA.

Datos consultados (2026-11-10): hoja tecnica del MMRTG (NASA/DOE): 110 W electricos al inicio, 72 W estimados a 17 anos, eficiencia de sistema 6 %, 2.8 W/kg, ~2000 W termicos, 768 termopares;
JPL Publication 15-6 (2015): degradacion del termopar ~0.8 %/ano, degradacion por decaimiento del Pu-238 ~0.8 %/ano, 250 W termicos por modulo GPHS, 8 modulos y 4.8 kg de dioxido de plutonio
con ~71 % de Pu-238 en peso (pagina de preguntas frecuentes de la NASA); N_A = 6.02214076e23 /mol es exacto en el SI y NO se consulto en esta clase.
NO CONSULTADOS (valores de manual, ilustrativos): vida media del Pu-238 = 87.7 anos, masa molar 238.05 g/mol, energia alfa media 5.59 MeV, 1 eV = 1.602176634e-19 J.
Modelo: P(t) = P0 exp(-ln2 t / T_half) (1 - d_te)^t.
Segunda via: (a) la degradacion total implicita en 72 W a 17 anos se despeja y se compara con la suma de las dos tasas de la NASA; (b) la potencia termica del plutonio se estima desde la actividad
(lambda N E_alfa) y se compara con las 2000 W de la hoja.
Tolerancia: ninguna comprobacion de acuerdo con la NASA se impone; el laboratorio REPORTA las diferencias. Solo se verifican identidades internas (t = 0, vida media, 8 x 250 W).
"""
from __future__ import annotations
import math, platform

P0, T17, P17 = 110.0, 17.0, 72.0
ETA_NASA, W_KG, P_TERM = 0.06, 2.8, 2000.0
T_HALF, D_TE = 87.7, 0.008
M_PUO2, FRAC_PU238, M_MOLAR = 4.8e3, 0.71, 238.05          # g, fraccion, g/mol
N_A, E_ALFA_MEV, EV = 6.02214076e23, 5.59, 1.602176634e-19
YEAR = 365.25 * 86400.0


def potencia(t, d_te=D_TE, t_half=T_HALF):
    return P0 * math.exp(-math.log(2.0) * t / t_half) * (1.0 - d_te) ** t


def d_te_para_72():
    lo, hi = 0.0, 0.2
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if potencia(T17, m) > P17:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


def resultados():
    r = {}
    r["P17_modelo"] = potencia(17.0)
    r["P0_chk"] = potencia(0.0)
    r["decaimiento_anual"] = 1.0 - math.exp(-math.log(2.0) / T_HALF)
    r["P_half"] = potencia(T_HALF, D_TE, T_HALF) / P0
    r["f17"] = r["P17_modelo"] / P0
    r["dif17"] = r["P17_modelo"] - P17
    r["dif17_pct"] = r["dif17"] / P17 * 100.0
    r["d_te_72"] = d_te_para_72()
    r["d_total_72"] = 1.0 - (P17 / P0) ** (1.0 / T17)
    r["d_total_modelo"] = 1.0 - (r["P17_modelo"] / P0) ** (1.0 / T17)
    # ejemplo conservador de la NASA: 107 We y 4.8 %/ano de degradacion total
    r["P17_conserv"] = 107.0 * (1.0 - 0.048) ** 17
    # energia entregada en 17 anos
    n = 17000
    e = sum(potencia((k + 0.5) / 1000.0) * (1.0 / 1000.0) for k in range(n))      # W*ano
    r["E17_kWh"] = e * YEAR / 3600.0 / 1000.0
    # termico y eficiencia
    r["Pterm_GPHS"] = 8 * 250.0
    r["eta_110"] = P0 / P_TERM
    r["eta_modelo_vs_nasa"] = ETA_NASA
    r["masa_kg"] = P0 / W_KG
    # potencia termica del plutonio por actividad
    m_pu238 = M_PUO2 * FRAC_PU238          # 'en peso' segun la NASA: se toma como masa de Pu-238
    r["m_pu238_g"] = m_pu238
    lam = math.log(2.0) / (T_HALF * YEAR)
    n_at = m_pu238 / M_MOLAR * N_A
    act = lam * n_at
    r["A_Bq"] = act
    r["Pterm_act"] = act * E_ALFA_MEV * 1e6 * EV
    r["dif_term_pct"] = (r["Pterm_act"] - P_TERM) / P_TERM * 100.0
    r["A_PBq"] = act / 1e15
    r["Wg"] = r["Pterm_act"] / m_pu238
    r["d_te_72_pct"] = r["d_te_72"] * 100.0
    r["decaimiento_anual_pct"] = r["decaimiento_anual"] * 100.0
    for t in (0, 5, 10, 30):
        r[f"P_t{t}"] = potencia(float(t))
    r["d_total_72_pct"] = r["d_total_72"] * 100.0
    r["d_total_modelo_pct"] = r["d_total_modelo"] * 100.0
    r["eta_110_pct"] = r["eta_110"] * 100.0
    r["dec17"] = math.exp(-math.log(2.0) * 17.0 / T_HALF)
    r["te17"] = (1.0 - D_TE) ** 17
    r["dec10"] = math.exp(-math.log(2.0) * 10.0 / T_HALF)
    r["P17_d15"] = potencia(17.0, 0.015)
    r["Pcons10"] = 107.0 * (1.0 - 0.048) ** 10
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Modelo: P(t) = {P0:.0f} W exp(-ln2 t/{T_HALF}) (1-{D_TE})^t ; decaimiento = {r['decaimiento_anual']*100:.3f} %/ano ; termopar = {D_TE*100:.1f} %/ano")
    print(" t [a]   P modelo [W]")
    for t in (0, 5, 10, 17, 30):
        print(f" {t:5d}  {potencia(float(t)):10.2f}")
    print(f"A 17 anos: modelo = {r['P17_modelo']:.2f} W ; hoja de la NASA = {P17:.0f} W ; diferencia = {r['dif17']:+.2f} W ({r['dif17_pct']:+.1f} %)")
    print(f"Degradacion anual total implicita: NASA (72 W) = {r['d_total_72']*100:.3f} %/ano ; modelo = {r['d_total_modelo']*100:.3f} %/ano ; termopar necesario para 72 W = {r['d_te_72']*100:.3f} %/ano")
    print(f"Ejemplo conservador (107 W, 4.8 %/ano): {r['P17_conserv']:.2f} W a 17 anos")
    print(f"Energia entregada en 17 anos (modelo) = {r['E17_kWh']:.0f} kWh")
    print(f"Termico: 8 modulos x 250 W = {r['Pterm_GPHS']:.0f} W (hoja: ~2000 W) ; eficiencia 110/2000 = {r['eta_110']*100:.1f} % (hoja: 6 %) ; masa 110/2.8 = {r['masa_kg']:.1f} kg")
    print(f"Pu-238: {r['m_pu238_g']:.0f} g ; actividad = {r['A_PBq']:.3f} PBq ; potencia termica por actividad = {r['Pterm_act']:.0f} W ({r['dif_term_pct']:+.1f} % frente a 2000 W) ; {r['Wg']:.3f} W/g")
    assert abs(r["P0_chk"] - P0) < 1e-12
    assert abs(r["P_half"] - 0.5 * (1.0 - D_TE) ** T_HALF) < 1e-12
    assert r["Pterm_GPHS"] == 2000.0
    assert r["d_te_72"] > D_TE, "la degradacion del termopar implicita en 72 W supera la tasa de 0.8 %/ano"
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
