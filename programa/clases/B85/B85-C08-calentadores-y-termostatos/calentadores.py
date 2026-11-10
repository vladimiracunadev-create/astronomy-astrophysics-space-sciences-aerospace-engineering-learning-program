# SPDX-License-Identifier: Apache-2.0
"""B85-C08: calentadores y termostatos: potencia de supervivencia, histéresis y ciclo de trabajo.

Consultado: SIGMA (NIST); de NASA SST-SoA Thermal Control: los calentadores son sobre todo resistivos tipo Kapton, se usan
para mantener baterías y se controlan con termostato o sensor. ILUSTRATIVO: caja, capacidad, potencias, órbita, umbrales.
Segunda vía: balance de energía integrado en el tiempo; ciclo de trabajo frente a potencia media necesaria.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

C_TERM, AREA, EPS = 1500.0, 0.06, 0.8     # J/K, m2, -
Q_SOL, Q_ECL = 23.0, 3.0                   # W absorbidos (sol / eclipse)
P_H = 20.0                                 # W del calentador
T_ON, T_OFF = 278.0, 283.0                 # K (histeresis)
PERIODO, ECLIPSE = 5400.0, 2100.0          # s
DT = 1.0


def simular(n_orb=4, p_h=P_H, t_on=T_ON, t_off=T_OFF):
    t = 300.0
    on = False
    e_h = e_in = e_out = 0.0
    tmin, tmax = 1e9, 0.0
    tiempo_on = 0.0
    hist = []
    for orb in range(n_orb):
        e_h = e_in = e_out = 0.0
        tiempo_on = 0.0
        tmin, tmax = 1e9, 0.0
        t_ini = t
        for s in range(int(PERIODO / DT)):
            tt = s * DT
            q_abs = Q_ECL if tt >= PERIODO - ECLIPSE else Q_SOL
            if t <= t_on:
                on = True
            elif t >= t_off:
                on = False
            p = p_h if on else 0.0
            perdida = EPS * SIGMA * AREA * t ** 4
            t += DT * (q_abs + p - perdida) / C_TERM
            e_h += p * DT
            e_in += q_abs * DT
            e_out += perdida * DT
            tiempo_on += DT if (on and p_h > 0) else 0.0
            tmin, tmax = min(tmin, t), max(tmax, t)
        hist.append((t_ini, t))
    return dict(e_h=e_h, e_in=e_in, e_out=e_out, tmin=tmin, tmax=tmax, duty=tiempo_on / PERIODO, t_ini=hist[-1][0], t_fin=hist[-1][1])


def calcular():
    r = {}
    r["p_mant"] = EPS * SIGMA * AREA * T_ON ** 4 - Q_ECL
    r["p_mant_280"] = EPS * SIGMA * AREA * 280.0 ** 4 - Q_ECL
    r["t_sol_eq"] = ((Q_SOL) / (EPS * SIGMA * AREA)) ** 0.25
    r["t_ecl_eq"] = ((Q_ECL) / (EPS * SIGMA * AREA)) ** 0.25
    r["sim"] = simular()
    s = r["sim"]
    r["cierre_energia"] = (s["e_in"] + s["e_h"] - s["e_out"]) - C_TERM * (s["t_fin"] - s["t_ini"])
    r["potencia_media_heater"] = s["e_h"] / PERIODO
    r["sim_sin_heater"] = simular(p_h=0.0)
    r["sim_15W"] = simular(p_h=15.0)
    r["sim_10W"] = simular(p_h=10.0)
    return r


def main():
    r = calcular()
    cabecera()
    s = r["sim"]
    print(f"Caja ILUSTRATIVA: C = {C_TERM:.0f} J/K, A = {AREA} m2, eps = {EPS}; absorbido sol/eclipse = {Q_SOL}/{Q_ECL} W; calentador {P_H:.0f} W")
    print(f"Termostato: ON a {T_ON:.0f} K, OFF a {T_OFF:.0f} K; orbita {PERIODO:.0f} s con eclipse de {ECLIPSE:.0f} s; paso {DT:.0f} s")
    print(f"Potencia para mantener {T_ON:.0f} K en eclipse = {r['p_mant']:.2f} W ; para 280 K = {r['p_mant_280']:.2f} W")
    print(f"Equilibrio sin calentador: sol {r['t_sol_eq']:.2f} K ; eclipse {r['t_ecl_eq']:.2f} K")
    print(f"Cuarta orbita con calentador de {P_H:.0f} W: Tmin = {s['tmin']:.2f} K ; Tmax = {s['tmax']:.2f} K ; ciclo de trabajo = {s['duty']*100:.2f} % ; energia calentador = {s['e_h']:.0f} J ({r['potencia_media_heater']:.3f} W medios)")
    print(f"Cierre de energia = {r['cierre_energia']:.3e} J")
    for nombre, k in (("sin calentador", "sim_sin_heater"), ("15 W", "sim_15W"), ("10 W", "sim_10W")):
        x = r[k]
        print(f"  {nombre:<15}: Tmin = {x['tmin']:.2f} K ; ciclo de trabajo = {x['duty']*100:.2f} %")
    comprobar(abs(r["cierre_energia"]) < 1e-6 * s["e_out"], "cierre de energia")
    comprobar(s["tmin"] > T_ON - 2.0, "el calentador debe sostener el minimo")
    comprobar(r["sim_sin_heater"]["tmin"] < T_ON, "sin calentador baja del minimo")
    fin()


if __name__ == "__main__":
    main()
