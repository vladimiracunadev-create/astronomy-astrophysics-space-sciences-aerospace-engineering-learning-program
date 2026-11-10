# SPDX-License-Identifier: Apache-2.0
"""B85-C20: presupuesto térmico de una carga útil: disipación por modo, capacidad del radiador, calentadores y margen.

Consultado: SIGMA (NIST), S0 (NASA/NSSDC). ILUSTRATIVO y SINTÉTICO: unidades de la carga, disipaciones, modos, rango de temperatura,
área del radiador, propiedades ópticas, entorno absorbido, política de margen. Ningún requisito de proyecto.
Segunda vía: dimensionado inverso del área por bisección frente a la fórmula cerrada; suma de unidades por dos caminos.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

# modo: dict unidad -> W disipados (SINTETICOS)
UNIDADES = ["detector", "procesador", "fuente", "actuadores", "conversion"]
MODOS = {
    "supervivencia": [0.0, 0.0, 0.0, 0.0, 2.0],
    "espera": [4.0, 6.0, 0.0, 0.0, 3.0],
    "nominal": [12.0, 18.0, 25.0, 6.0, 10.0],
    "pico": [12.0, 24.0, 40.0, 10.0, 16.0],
}
A_RAD, EPS, ALFA_EOL = 0.60, 0.85, 0.25
T_MAX_OP, T_MIN_SUP = 303.0, 253.0          # K: limite superior de operacion y minimo de supervivencia (ilustrativos)
ABS_CAL, ABS_FRIO = 131.19, 5.0             # W/m2 absorbidos (caliente EOL, frio) SINTETICOS (valor de B85-C07 como orden de magnitud)
MARGEN_DIS = 0.20                           # 20 % de margen de desarrollo sobre la disipacion (politica ILUSTRATIVA)
Q_CAL_INT = 0.0


def capacidad(a, t, absorbido):
    return a * (EPS * SIGMA * t ** 4 - absorbido)


def area_inversa(q, t, absorbido):
    return biseccion(lambda a: capacidad(a, t, absorbido) - q, 1e-3, 100.0)


def calcular():
    r = {"modos": []}
    for m, v in MODOS.items():
        dis = sum(v)
        r["modos"].append((m, dis, dis * (1 + MARGEN_DIS)))
    r["cap_cal"] = capacidad(A_RAD, T_MAX_OP, ABS_CAL)
    r["cap_frio"] = capacidad(A_RAD, T_MIN_SUP, ABS_FRIO)
    r["margenes"] = [(m, d, dm, r["cap_cal"] - dm, (r["cap_cal"] - dm) / r["cap_cal"] * 100) for m, d, dm in r["modos"]]
    r["gobierna"] = min(r["margenes"], key=lambda x: x[3])
    # calentador de supervivencia: perdida a T_min menos disipacion de supervivencia
    d_sup = r["modos"][0][1]
    r["calentador"] = max(0.0, r["cap_frio"] - d_sup)
    r["calentador_con_margen"] = r["calentador"] * 1.25
    # area minima para el modo pico con margen
    pico_m = r["modos"][3][2]
    r["a_min_pico"] = pico_m / (EPS * SIGMA * T_MAX_OP ** 4 - ABS_CAL)
    r["a_min_pico_bis"] = area_inversa(pico_m, T_MAX_OP, ABS_CAL)
    r["sum_unidades"] = sum(sum(v) for v in MODOS.values())
    r["sum_modos"] = sum(d for _, d, _ in r["modos"])
    # temperatura maxima que alcanza el radiador en modo pico con margen
    r["t_pico"] = ((pico_m / A_RAD + ABS_CAL) / (EPS * SIGMA)) ** 0.25
    r["dt_a_limite"] = T_MAX_OP - r["t_pico"]
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Carga ILUSTRATIVA y SINTETICA; radiador {A_RAD} m2, eps = {EPS}; limites {T_MIN_SUP:.0f}-{T_MAX_OP:.0f} K ; absorbido caliente {ABS_CAL} W/m2, frio {ABS_FRIO} W/m2 ; margen de disipacion {MARGEN_DIS*100:.0f} %")
    print(f"{'modo':<14}" + "".join(f"{u:>12}" for u in UNIDADES) + f"{'total [W]':>11}{'con margen':>12}")
    for (m, v), (_, d, dm) in zip(MODOS.items(), r["modos"]):
        print(f"{m:<14}" + "".join(f"{x:>12.1f}" for x in v) + f"{d:>11.1f}{dm:>12.1f}")
    print(f"Capacidad del radiador a {T_MAX_OP:.0f} K (caso caliente EOL) = {r['cap_cal']:.2f} W ; a {T_MIN_SUP:.0f} K (frio) = {r['cap_frio']:.2f} W")
    for m, d, dm, mar, pct in r["margenes"]:
        print(f"  {m:<14}: margen de potencia = {mar:+.2f} W ({pct:+.1f} % de la capacidad)")
    print(f"Modo que gobierna el caso caliente: {r['gobierna'][0]} ; T del radiador en pico con margen = {r['t_pico']:.2f} K ({r['dt_a_limite']:.2f} K bajo el limite)")
    print(f"Calentador de supervivencia = {r['calentador']:.2f} W ({r['calentador_con_margen']:.2f} W con 25 % de margen)")
    print(f"Area minima del radiador para el pico con margen = {r['a_min_pico']:.4f} m2 (biseccion {r['a_min_pico_bis']:.4f} m2)")
    print(f"Suma de unidades = {r['sum_unidades']:.1f} W ; suma de modos = {r['sum_modos']:.1f} W")
    comprobar(abs(r["a_min_pico"] - r["a_min_pico_bis"]) < 1e-9, "area inversa")
    comprobar(abs(r["sum_unidades"] - r["sum_modos"]) < 1e-9, "suma por dos caminos")
    comprobar(r["gobierna"][0] == "pico", "gobierna el pico")
    fin()


if __name__ == "__main__":
    main()
