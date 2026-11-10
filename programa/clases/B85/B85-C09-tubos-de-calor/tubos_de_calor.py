# SPDX-License-Identifier: Apache-2.0
"""B85-C09: tubo de calor: límite capilar y efecto de la inclinación en tierra.

Consultado: G_E (NASA/NSSDC); NASA SST-SoA Thermal Control menciona los tubos de calor como medio pasivo de transporte (sin cifras).
ILUSTRATIVO y NO CONSULTADO: propiedades del amoníaco a 20 °C, geometría de la mecha, longitudes.
Segunda vía: Q_max por bisección del balance de presiones frente a la fórmula cerrada.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

# fluido (amoniaco, 20 C) ilustrativo
SIG, RHO_L, MU_L, H_FG = 0.0213, 610.0, 1.4e-4, 1.186e6
RHO_V, MU_V = 6.7, 9.5e-6
# mecha y tubo ilustrativos
R_EFF, K_PERM, A_W = 50e-6, 1e-10, 2.0e-5
R_VAP = 2.5e-3
L_EF = 0.40          # m (longitud efectiva)
COS_T = 1.0


def dp_cap():
    return 2 * SIG * COS_T / R_EFF


def coef_liquido():
    return MU_L * L_EF / (RHO_L * K_PERM * A_W * H_FG)       # Pa/W


def coef_vapor():
    return 8 * MU_V * L_EF / (math.pi * R_VAP ** 4 * RHO_V * H_FG)   # Pa/W (laminar, Poiseuille)


def dp_gravedad(elev):
    return RHO_L * G_E * elev


def q_max(elev=0.0):
    return (dp_cap() - dp_gravedad(elev)) / (coef_liquido() + coef_vapor())


def q_max_biseccion(elev=0.0):
    f = lambda q: dp_cap() - dp_gravedad(elev) - q * (coef_liquido() + coef_vapor())
    return biseccion(f, 0.0, 1e4)


def calcular():
    r = {}
    r["dp_cap"] = dp_cap()
    r["f_l"], r["f_v"] = coef_liquido(), coef_vapor()
    r["q0"] = q_max(0.0)
    r["q0_bis"] = q_max_biseccion(0.0)
    r["merito"] = RHO_L * SIG * H_FG / MU_L
    r["filas"] = [(e, dp_gravedad(e), q_max(e)) for e in (0.0, 0.002, 0.005, 0.010, 0.020)]
    r["elev_cero"] = dp_cap() / (RHO_L * G_E)
    r["q_r_doble"] = (2 * SIG * COS_T / (R_EFF * 2) ) / (coef_liquido() + coef_vapor())
    r["q_largo"] = dp_cap() / ((coef_liquido() + coef_vapor()) * 2)
    r["frac_vapor"] = coef_vapor() / (coef_liquido() + coef_vapor())
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Tubo ILUSTRATIVO (amoniaco 20 C, valores no consultados): r_eff = {R_EFF*1e6:.0f} um, K = {K_PERM:.0e} m2, A_mecha = {A_W*1e6:.0f} mm2, L_ef = {L_EF} m")
    print(f"Presion capilar maxima = {r['dp_cap']:.1f} Pa ; coef. liquido = {r['f_l']:.5f} Pa/W ; coef. vapor = {r['f_v']:.2e} Pa/W")
    print(f"Q_max (horizontal, g -> 0) = {r['q0']:.2f} W ; por biseccion = {r['q0_bis']:.2f} W ; numero de merito = {r['merito']:.3e} W/m2")
    print(f"{'elevacion[mm]':>14}{'dP_g[Pa]':>11}{'Q_max[W]':>11}")
    for e, dg, q in r["filas"]:
        print(f"{e*1e3:>14.1f}{dg:>11.2f}{q:>11.2f}")
    print(f"Elevacion que anula el transporte = {r['elev_cero']*1e3:.1f} mm")
    print(f"Radio efectivo doble: Q_max = {r['q_r_doble']:.2f} W ; longitud efectiva doble: Q_max = {r['q_largo']:.2f} W ; fraccion de caida en el vapor = {r['frac_vapor']*100:.3f} %")
    comprobar(abs(r["q0"] - r["q0_bis"]) < 1e-6, "biseccion")
    comprobar(r["filas"][0][2] > r["filas"][-1][2], "la elevacion reduce Q_max")
    fin()


if __name__ == "__main__":
    main()
