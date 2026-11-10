# SPDX-License-Identifier: Apache-2.0
"""B85-C11: ciclos térmicos de una órbita baja: oscilación de un nodo y fatiga por Coffin-Manson.

Consultado: nada específico (YEAR y periodo son aritmética). ILUSTRATIVO: nodo, flujos, T_ref, ley de fatiga (N0, ΔT0, n).
Segunda vía: integración numérica del nodo lineal frente a la solución periódica analítica.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

PERIODO, ECLIPSE = 5400.0, 2100.0
G_N, T_REF = 1.5, 240.0           # W/K, K (acoplamiento linealizado)
Q_S, Q_E = 60.0, 10.0             # W
N0, DT0, N_EXP = 1.0e4, 100.0, 2.0   # Coffin-Manson ilustrativo: N = N0 (DT0/DT)^n


def periodica(c_term):
    tau = c_term / G_N
    ts, te = PERIODO - ECLIPSE, ECLIPSE
    teq_s, teq_e = T_REF + Q_S / G_N, T_REF + Q_E / G_N
    es, ee = math.exp(-ts / tau), math.exp(-te / tau)
    # Tmax = teq_s + (Tmin - teq_s) es ; Tmin = teq_e + (Tmax - teq_e) ee
    tmax = (teq_s * (1 - es) + es * teq_e * (1 - ee)) / (1 - es * ee)
    tmin = teq_e + (tmax - teq_e) * ee
    return tmin, tmax, tau, teq_s, teq_e


def numerica(c_term, n_orb=30, dt=1.0):
    t = 260.0
    tmin_o = tmax_o = 0.0
    for _ in range(n_orb):
        tmin_o, tmax_o = 1e9, 0.0
        for s in range(int(PERIODO / dt)):
            q = Q_E if s * dt >= PERIODO - ECLIPSE else Q_S
            t += dt * (q - G_N * (t - T_REF)) / c_term
            tmin_o, tmax_o = min(tmin_o, t), max(tmax_o, t)
    return tmin_o, tmax_o


def ciclos_hasta_falla(dt_k):
    return N0 * (DT0 / dt_k) ** N_EXP


def calcular():
    r = {"filas": []}
    for cth in (500.0, 2000.0, 8000.0, 30000.0):
        tmin, tmax, tau, *_ = periodica(cth)
        r["filas"].append((cth, tau, tmin, tmax, tmax - tmin, ciclos_hasta_falla(tmax - tmin)))
    r["num"] = numerica(2000.0)
    r["ana"] = periodica(2000.0)[:2]
    r["ciclos_anio"] = YEAR / PERIODO
    f = r["filas"][1]
    r["vida_anios"] = f[5] / r["ciclos_anio"]
    r["dano_5_anios"] = 5 * r["ciclos_anio"] / f[5]
    r["dt_para_15_anios"] = DT0 * math.sqrt(N0 / (15 * r["ciclos_anio"]))
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Nodo ILUSTRATIVO: G = {G_N} W/K a {T_REF:.0f} K ; absorbido sol/eclipse = {Q_S:.0f}/{Q_E:.0f} W ; orbita {PERIODO:.0f} s, eclipse {ECLIPSE:.0f} s")
    print(f"{'C [J/K]':>9}{'tau [s]':>10}{'Tmin [K]':>10}{'Tmax [K]':>10}{'DT [K]':>9}{'N hasta falla':>15}")
    for cth, tau, tmin, tmax, d, n in r["filas"]:
        print(f"{cth:>9.0f}{tau:>10.0f}{tmin:>10.2f}{tmax:>10.2f}{d:>9.2f}{n:>15.0f}")
    print(f"Numerica (C = 2000 J/K, 30 orbitas): Tmin = {r['num'][0]:.3f} K, Tmax = {r['num'][1]:.3f} K ; analitica: {r['ana'][0]:.3f} / {r['ana'][1]:.3f} K")
    print(f"Ciclos por anio = {r['ciclos_anio']:.1f} ; vida (Coffin-Manson ILUSTRATIVO) con C = 2000 J/K = {r['vida_anios']:.2f} anios ; dano en 5 anios = {r['dano_5_anios']:.2f}")
    print(f"DT maximo para 15 anios de vida = {r['dt_para_15_anios']:.2f} K")
    comprobar(abs(r["num"][0] - r["ana"][0]) < 0.05 and abs(r["num"][1] - r["ana"][1]) < 0.05, "numerica frente a analitica")
    comprobar(r["filas"][0][4] > r["filas"][-1][4], "mayor inercia, menor DT")
    fin()


if __name__ == "__main__":
    main()
