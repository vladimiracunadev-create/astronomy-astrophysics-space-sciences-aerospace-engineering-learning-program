# SPDX-License-Identifier: Apache-2.0
"""B85-C15: electrificación superficial: potencial flotante por balance de corrientes en órbita baja y en eclipse geoestacionario.

Consultado: constantes SI exactas (e, k_B); NASA-HDBK-4002B solo la ficha (alcance: cuándo la carga puede ser un problema).
ILUSTRATIVO y NO CONSULTADO: densidades, temperaturas del plasma, masas, velocidad orbital, geometría y el modelo de corrientes
(electrones maxwellianos retardados; iones por velocidad de ram en LEO y OML atractivo en GEO), sin emisión secundaria ni fotoemisión.
Segunda vía: Newton frente a bisección sobre el mismo balance.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

M_E, M_P = 9.1093837015e-31, 1.67262192369e-27   # kg
EPS0 = 8.8541878128e-12


def j_e0(n, te_ev):
    return E_Q * n * math.sqrt(E_Q * te_ev / (2 * math.pi * M_E))


def leo(n=1e11, te_ev=0.1, v_orb=7670.0):
    ji = E_Q * n * v_orb
    je0 = j_e0(n, te_ev)
    v = te_ev * math.log(ji / je0)           # V negativo cuando ji < je0
    return v, ji, je0


def geo(n=1e6, te_ev=5000.0, ti_ev=10000.0):
    je0 = j_e0(n, te_ev)
    ji0 = E_Q * n * math.sqrt(E_Q * ti_ev / (2 * math.pi * M_P))
    f = lambda v: je0 * math.exp(v / te_ev) - ji0 * (1 - v / ti_ev)
    df = lambda v: je0 / te_ev * math.exp(v / te_ev) + ji0 / ti_ev
    v_b = biseccion(f, -1e6, 0.0)
    v_n = newton(f, df, -1000.0)
    return v_b, v_n, je0, ji0


def tiempo_carga(c_area, v, j):
    return c_area * abs(v) / j


def calcular():
    r = {}
    r["v_leo"], r["ji"], r["je0"] = leo()
    r["v_leo_te02"] = leo(te_ev=0.2)[0]
    r["v_leo_n1e10"] = leo(n=1e10)[0]
    r["v_geo_b"], r["v_geo_n"], r["je0_geo"], r["ji0_geo"] = geo()
    r["v_geo_te2k"] = geo(te_ev=2000.0, ti_ev=4000.0)[0]
    r["c_kapton"] = EPS0 * 3.4 / 1e-3
    r["t_carga_geo"] = tiempo_carga(r["c_kapton"], r["v_geo_b"], r["je0_geo"])
    r["c_kapton_25"] = EPS0 * 3.4 / 25e-6
    r["e_kapton_1kv"] = 1000.0 / 25e-6      # V/m con 1 kV a traves de 25 um
    r["residuo_geo"] = r["je0_geo"] * math.exp(r["v_geo_b"] / 5000.0) - r["ji0_geo"] * (1 - r["v_geo_b"] / 10000.0)
    r["residuo_leo"] = r["je0"] * math.exp(r["v_leo"] / 0.1) - r["ji"]
    return r


def main():
    r = calcular()
    cabecera()
    print("Plasma ILUSTRATIVO (no consultado). Modelo: corrientes de electrones maxwellianos retardados y de iones; sin emision secundaria ni fotoemision")
    print(f"LEO (n = 1e11 m-3, Te = 0.1 eV, v_ram = 7670 m/s): J_i = {r['ji']:.3e} A/m2 ; J_e0 = {r['je0']:.3e} A/m2 ; V_flotante = {r['v_leo']:.3f} V")
    print(f"  Con Te = 0.2 eV: V = {r['v_leo_te02']:.3f} V ; con n = 1e10 m-3: V = {r['v_leo_n1e10']:.3f} V (la densidad no cambia V: ambas corrientes escalan con n)")
    print(f"GEO eclipse (n = 1e6 m-3, Te = 5 keV, Ti = 10 keV): J_e0 = {r['je0_geo']:.3e} A/m2 ; J_i0 = {r['ji0_geo']:.3e} A/m2")
    print(f"  V_flotante biseccion = {r['v_geo_b']:.1f} V ; Newton = {r['v_geo_n']:.1f} V ; residuo = {r['residuo_geo']:.2e} A/m2")
    print(f"  Con Te = 2 keV, Ti = 4 keV: V = {r['v_geo_te2k']:.1f} V")
    print(f"Capacidad de un dielectrico de 1 mm (eps_r = 3.4) = {r['c_kapton']:.3e} F/m2 ; tiempo de carga a ese potencial = {r['t_carga_geo']:.3f} s")
    print(f"Campo de 1 kV a traves de 25 um = {r['e_kapton_1kv']:.2e} V/m")
    comprobar(abs(r["v_geo_b"] - r["v_geo_n"]) < 1e-3, "Newton frente a biseccion")
    comprobar(abs(r["residuo_leo"]) < 1e-12 * r["je0"], "balance LEO")
    comprobar(r["v_leo"] < 0 and r["v_geo_b"] < r["v_leo"], "signos y orden")
    fin()


if __name__ == "__main__":
    main()
