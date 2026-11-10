# SPDX-License-Identifier: Apache-2.0
"""B85-C28: protección pasiva: espesor de blindaje por dosis, probabilidad de perforación por micrometeoroides y masa mínima.

Todo SINTÉTICO e ILUSTRATIVO: curva de atenuación de dosis, flujo de partículas F(≥d) = F1 d^-k, límite balístico, límites de dosis y de probabilidad.
Consultado: nada. Segunda vía: espesor por bisección frente a la inversa analítica; probabilidad de perforación por Monte Carlo frente a Poisson.
"""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

SEMILLA = 20261110
D0, LAM_MM = 1000.0, 3.0         # Gy/anio sin blindaje (sintetico), longitud de atenuacion en mm de Al
MATERIALES = {"aluminio": (2700.0, 1.0), "polietileno": (950.0, 2.2)}   # (densidad kg/m3, factor de atenuacion relativo a Al por mm), SINTETICO
F1, K_FL = 10.0, 2.0             # impactos/(m2 anio) de d >= 100 um; exponente (sinteticos)
C_BAL, B_BAL = 1.0, 0.9          # d_critico = C * t^B (mm), SINTETICO
AREA = 0.5                       # m2
ANIOS = 5.0
LIM_DOSIS = 100.0                # Gy en la mision (ilustrativo)
LIM_PROB = 1.0e-3                # probabilidad de perforacion (ilustrativa)


def dosis(t_mm, mat="aluminio"):
    return D0 * ANIOS * math.exp(-t_mm * MATERIALES[mat][1] / LAM_MM)


def t_dosis(limite, mat="aluminio"):
    return -LAM_MM / MATERIALES[mat][1] * math.log(limite / (D0 * ANIOS))


def p_perfora(t_mm):
    d_c = C_BAL * t_mm ** B_BAL                # mm
    flujo = F1 * (d_c / 0.1) ** (-K_FL)        # impactos/(m2 anio) con d >= d_c
    return 1 - math.exp(-flujo * AREA * ANIOS), flujo


def t_perfora(limite):
    return biseccion(lambda t: p_perfora(t)[0] - limite, 0.01, 50.0)


def masa(t_mm, mat="aluminio"):
    return MATERIALES[mat][0] * t_mm * 1e-3 * AREA


def mc_perfora(t_mm, n=200000):
    rng = random.Random(SEMILLA)
    lam = p_perfora(t_mm)[1] * AREA * ANIOS
    # Poisson por Monte Carlo: probabilidad de al menos un evento, con Bernoulli por tramos pequenos
    p = lam / 100.0
    hit = 0
    for _ in range(n // 100):
        if any(rng.random() < p for _ in range(100)):
            hit += 1
    return hit / (n // 100)


def calcular():
    r = {"filas": []}
    for t in (0.5, 1.0, 2.0, 4.0, 6.0, 8.0):
        d = dosis(t)
        p, fl = p_perfora(t)
        r["filas"].append((t, d, p, masa(t)))
    r["t_dosis"] = t_dosis(LIM_DOSIS)
    r["t_dosis_bis"] = biseccion(lambda t: dosis(t) - LIM_DOSIS, 0.0, 30.0)
    r["t_perf"] = t_perfora(LIM_PROB)
    r["t_dis"] = max(r["t_dosis"], r["t_perf"])
    r["gobierna"] = "dosis" if r["t_dosis"] >= r["t_perf"] else "perforacion"
    r["m_al"] = masa(r["t_dis"], "aluminio")
    # polietileno: espesor equivalente por dosis; la perforacion se mantiene con el mismo espesor fisico
    t_pe = t_dosis(LIM_DOSIS, "polietileno")
    r["t_pe"] = max(t_pe, r["t_perf"])
    r["m_pe"] = masa(r["t_pe"], "polietileno")
    r["p_mc"] = mc_perfora(3.0)
    r["p_poisson"] = p_perfora(3.0)[0]
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Datos SINTETICOS: dosis sin blindaje {D0:.0f} Gy/anio, atenuacion exp(-t/{LAM_MM} mm Al) ; F(>=100 um) = {F1:.0e} /(m2 anio), exponente {K_FL}; limites {LIM_DOSIS:.0f} Gy y P = {LIM_PROB:.0e}; area {AREA} m2, mision {ANIOS:.0f} anios")
    print(f"{'t [mm]':>7}{'dosis [Gy]':>12}{'P perfora':>12}{'masa Al [kg]':>14}")
    for t, d, p, m in r["filas"]:
        print(f"{t:>7.1f}{d:>12.2f}{p:>12.3e}{m:>14.3f}")
    print(f"Espesor por dosis = {r['t_dosis']:.3f} mm (biseccion {r['t_dosis_bis']:.3f} mm) ; por perforacion = {r['t_perf']:.3f} mm ; gobierna {r['gobierna']}")
    print(f"Diseno de aluminio: {r['t_dis']:.3f} mm -> {r['m_al']:.3f} kg ; polietileno (factor 2.2 por mm): {r['t_pe']:.3f} mm -> {r['m_pe']:.3f} kg")
    print(f"Prob. de perforacion a 3 mm: Poisson = {r['p_poisson']:.4e} ; Monte Carlo = {r['p_mc']:.4e}")
    comprobar(abs(r["t_dosis"] - r["t_dosis_bis"]) < 1e-6, "espesor por dosis")
    comprobar(abs(p_perfora(r["t_perf"])[0] - LIM_PROB) / LIM_PROB < 1e-6, "espesor por perforacion")
    comprobar(abs(r["p_mc"] - r["p_poisson"]) < 0.01, "Monte Carlo frente a Poisson")
    comprobar(r["m_pe"] < r["m_al"], "el polietileno pesa menos con estos datos sinteticos")
    fin()


if __name__ == "__main__":
    main()
