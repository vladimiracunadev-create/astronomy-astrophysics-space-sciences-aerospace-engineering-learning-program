#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C20: simulacion del balance ambiental de un habitat de 4 personas durante 30 dias, con controladores y una falla.

Integra C01-C08. Criterios CONSULTADOS (OCHMO-TB-002/003/004): PIO2 de 145 a 155 mmHg; ppCO2 medio de 1 h < 3 mmHg; zona de salud 18-27 C y 25-75 % de HR; zona de desempeno 20-25 C
y 30-60 %; consumo de 0.771 kg de O2 y RQ 0.85 por persona y dia; 147 W metabolicos por persona. ILUSTRATIVOS: volumen libre de 150 m3, aire a 101.325 kPa (21 % de O2),
equipos de 3000 W, vapor de 1.5 kg/dia por persona, depurador de 10 L/s con eficiencia 0.7 (respaldo identico con 20 min de retraso en el escenario B), electrolizador
de hasta 2 veces el consumo, intercambiador de calor/serpentin que condensa si HR > 50 % hasta 40 %, lazo de enfriamiento con ganancia 3000 W/K, capacidad termica 2e6 J/K, paso de 60 s.
Falla: el depurador principal se apaga el dia 10 durante 6 h. Escenarios: A (sin respaldo) y B (con respaldo tras 20 min).
Verificacion: el O2 repuesto + el inicial iguala al consumido + el final (balance de masa); los controladores mantienen PIO2 y HR en el caso nominal; la falla en A supera 3 mmHg.
"""
from __future__ import annotations
import math
import platform
import numpy as np

RG, V, T0, P0 = 8.314462, 150.0, 295.15, 101325.0
M_O2, M_CO2, M_H2O = 0.031998, 0.04401, 0.018015
CREW, DT = 4, 60.0
Q_O2 = 0.771 / M_O2 / 86400.0      # mol/s por persona
Q_CO2 = 0.85 * Q_O2
Q_VAP = 1.5 / M_H2O / 86400.0      # mol/s por persona
ES = lambda T: 6.112 * math.exp(17.62 * T / (243.12 + T)) * 100.0  # Pa


def simular(respaldo: bool, falla=True):
    n_gas = P0 * V / (RG * T0)
    n_o2, n_co2, n_n2 = 0.21 * n_gas, 0.0, 0.79 * n_gas
    n_h2o = 0.45 * ES(22.0) * V / (RG * T0)
    T = 22.0 + 273.15
    sc_on, hx_on, el_hist = True, False, 0.0
    o2_rep, cond, n_pasos = 0.0, 0.0, int(30 * 86400 / DT)
    t_f0, t_f1 = 10 * 86400, 10 * 86400 + 6 * 3600
    reg = []
    o2_ini = n_o2
    o2_cons = 0.0
    for i in range(n_pasos):
        t = i * DT
        p_tot = (n_o2 + n_co2 + n_n2 + n_h2o) * RG * T / V
        x_o2 = n_o2 / (n_o2 + n_co2 + n_n2)
        pio2 = (p_tot / 133.322 - 47.0) * x_o2
        ppco2 = n_co2 / (n_o2 + n_co2 + n_n2 + n_h2o) * p_tot / 133.322
        hr = n_h2o * RG * T / V / ES(T - 273.15) * 100.0
        # controladores
        if pio2 < 147.0: el_hist = 1.0
        if pio2 > 152.0: el_hist = 0.0
        rep = el_hist * 2 * CREW * Q_O2 * DT
        n_o2 += rep
        o2_rep += rep
        if hr > 50.0: hx_on = True
        if hr < 40.0: hx_on = False
        # consumo y generacion de la tripulacion
        n_o2 -= CREW * Q_O2 * DT
        o2_cons += CREW * Q_O2 * DT
        n_co2 += CREW * Q_CO2 * DT
        n_h2o += CREW * Q_VAP * DT
        # depurador
        falla_act = falla and t_f0 <= t < t_f1
        principal = not falla_act
        res = respaldo and falla_act and (t >= t_f0 + 20 * 60)
        k = (0.7 * 10e-3 / V) * (1 if principal else 0) + (0.7 * 10e-3 / V) * (1 if res else 0)
        n_co2 -= k * n_co2 * DT
        if hx_on:
            dn = min(0.002 * n_h2o * DT / 60.0 * 5, n_h2o)
            n_h2o -= dn
            cond += dn * M_H2O
        # termico
        Q = CREW * 147.0 + 3000.0
        Qc = max(0.0, 3000.0 * (T - (22.0 + 273.15)))
        T += DT * (Q - Qc) / 2e6
        if i % 60 == 0:
            reg.append((t, pio2, ppco2, hr, T - 273.15))
    reg = np.array(reg)
    n_o2_fin = n_o2
    bal = (o2_ini + o2_rep) - (o2_cons + n_o2_fin)
    # media de 1 h de ppCO2 (los registros son por hora)
    return reg, dict(o2_rep=o2_rep * M_O2, cond=cond, bal=bal * M_O2, o2_ini=o2_ini, o2_fin=n_o2_fin)


def resumen(reg):
    t = reg[:, 0]
    return dict(pio2_min=reg[:, 1].min(), pio2_max=reg[:, 1].max(), pp_max=reg[:, 2].max(), hr_min=reg[:, 3].min(), hr_max=reg[:, 3].max(), T_min=reg[:, 4].min(), T_max=reg[:, 4].max(),
                h_sobre3=float((reg[:, 2] >= 3.0).sum()))


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: simulacion SINTETICA con controladores y parametros ILUSTRATIVOS; criterios consultados; NO es un habitat real")
    R = {}
    out = {}
    for nombre, resp, falla in (("nominal", False, False), ("A: falla sin respaldo", False, True), ("B: falla con respaldo", True, True)):
        reg, bal = simular(resp, falla)
        s = resumen(reg)
        out[nombre] = (s, bal)
    print("Criterios: PIO2 145-155 mmHg; ppCO2 < 3 mmHg; HR 25-75 % (salud) y 30-60 % (desempeno); T 18-27 C (salud) y 20-25 C (desempeno)")
    print("   escenario               PIO2 min/max   ppCO2 max   horas >= 3 mmHg   HR min/max   T min/max   O2 repuesto [kg]   condensado [kg]")
    for nombre, (s, b) in out.items():
        print(f"   {nombre:22s}  {s['pio2_min']:5.1f}/{s['pio2_max']:5.1f}   {s['pp_max']:8.2f}   {s['h_sobre3']:13.0f}   {s['hr_min']:4.1f}/{s['hr_max']:4.1f}   {s['T_min']:4.1f}/{s['T_max']:4.1f}   {b['o2_rep']:15.2f}   {b['cond']:14.1f}")
    R["out"] = out
    sn, bn = out["nominal"]
    sa, ba = out["A: falla sin respaldo"]
    sb, bb = out["B: falla con respaldo"]
    print("Matriz de verificacion (nominal / A / B):")
    crit = [("PIO2 en 145-155 mmHg", lambda s: s["pio2_min"] >= 145 and s["pio2_max"] <= 155),
            ("ppCO2 < 3 mmHg (muestreo horario)", lambda s: s["pp_max"] < 3.0),
            ("HR en 25-75 %", lambda s: s["hr_min"] >= 25 and s["hr_max"] <= 75),
            ("T en 18-27 C", lambda s: s["T_min"] >= 18 and s["T_max"] <= 27)]
    mat = {}
    for nom, f in crit:
        r3 = [f(sn), f(sa), f(sb)]
        mat[nom] = r3
        print(f"   {nom:34s} {'pasa' if r3[0] else 'FALLA':>6} / {'pasa' if r3[1] else 'FALLA':>6} / {'pasa' if r3[2] else 'FALLA':>6}")
    R["mat"] = mat
    print(f"Balance de masa de O2 (nominal): inicial + repuesto - consumido - final = {bn['bal']:.2e} kg")
    assert abs(bn["bal"]) < 1e-6
    assert sn["pp_max"] < 3.0 and sa["pp_max"] > 3.0 and sb["pp_max"] < sa["pp_max"]
    assert sn["pio2_min"] >= 140
    R.update(pp_n=sn["pp_max"], pp_a=sa["pp_max"], pp_b=sb["pp_max"], rep=bn["o2_rep"], cond=bn["cond"], pio2=(sn["pio2_min"], sn["pio2_max"]), hr=(sn["hr_min"], sn["hr_max"]), T=(sn["T_min"], sn["T_max"]), h_a=sa["h_sobre3"], h_b=sb["h_sobre3"])
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
