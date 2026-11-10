# SPDX-License-Identifier: Apache-2.0
"""B85-C25: sensores térmicos: termistor NTC (modelo β), sensor de platino (Callendar-Van Dusen), cuantización y autocalentamiento.

Consultado: de NASA SST-SoA Thermal Control, que los calentadores se controlan con termostato o sensor, sin especificar sensores.
ILUSTRATIVO y NO CONSULTADO: β = 3950 K, R0 = 10 kΩ, A y B de platino (IEC 60751 no consultada), divisor, ADC de 12 bits, constante de disipación.
Segunda vía: inversión de ida y vuelta y solución cuadrática cerrada del platino.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

R0, T0, BETA = 10000.0, 298.15, 3950.0
VREF, R_FIJA, BITS_ADC = 3.3, 10000.0, 12
A_PT, B_PT, R0_PT = 3.9083e-3, -5.775e-7, 100.0
DISIP = 1.5e-3                               # W/K constante de disipacion ILUSTRATIVA


def r_ntc(t):
    return R0 * math.exp(BETA * (1.0 / t - 1.0 / T0))


def t_ntc(r):
    return 1.0 / (1.0 / T0 + math.log(r / R0) / BETA)


def codigo(t):
    r = r_ntc(t)
    v = VREF * r / (r + R_FIJA)             # NTC en la rama baja del divisor
    n = 2 ** BITS_ADC
    return min(n - 1, int(v / VREF * n)), v


def t_desde_codigo(k):
    n = 2 ** BITS_ADC
    v = (k + 0.5) / n * VREF
    r = R_FIJA * v / (VREF - v)
    return t_ntc(r)


def r_pt(tc):
    return R0_PT * (1 + A_PT * tc + B_PT * tc * tc)


def t_pt(r):
    disc = A_PT ** 2 - 4 * B_PT * (1 - r / R0_PT)
    return (-A_PT + math.sqrt(disc)) / (2 * B_PT)


def calcular():
    r = {"filas": []}
    for t in (200.0, 250.0, 298.15, 350.0, 400.0):
        k, v = codigo(t)
        k2, _ = codigo(t + 0.001)
        sens = (k2 - k) / 0.001 if k2 != k else 0.0
        res = 1.0 / (r_ntc(t) * 0 + max(1e-12, abs((codigo(t + 1.0)[0] - codigo(t - 1.0)[0]) / 2.0)))
        r["filas"].append((t, r_ntc(t), v, k, res))
    r["ida_vuelta"] = max(abs(t_ntc(r_ntc(t)) - t) for t in (200.0, 250.0, 300.0, 350.0, 400.0))
    r["autocal"] = []
    for t in (250.0, 300.0, 350.0):
        rr = r_ntc(t)
        i = VREF / (rr + R_FIJA)
        p = i * i * rr
        r["autocal"].append((t, p * 1e6, p / DISIP))
    r["pt"] = [(tc, r_pt(tc)) for tc in (0.0, 50.0, 100.0, 150.0)]
    r["pt_inv"] = max(abs(t_pt(r_pt(tc)) - tc) for tc in (0.0, 50.0, 100.0, 150.0))
    # presupuesto de error en 300 K: cuantizacion + autocalentamiento + tolerancia de beta (1 %) + referencia (0.1 %)
    t = 300.0
    kq = abs(t_desde_codigo(codigo(t)[0]) - t)
    e_cuant = 0.5 * abs(t_desde_codigo(codigo(t)[0] + 1) - t_desde_codigo(codigo(t)[0]))
    rr = r_ntc(t)
    e_auto = (VREF / (rr + R_FIJA)) ** 2 * rr / DISIP
    r_alt = R0 * math.exp(BETA * 1.01 * (1.0 / t - 1.0 / T0))
    e_beta = abs(t_ntc(r_alt) - t)
    e_ref = 0.001 * 300.0 * 0.5
    r["error"] = dict(cuantizacion=e_cuant, autocalentamiento=e_auto, beta=e_beta, referencia=e_ref)
    r["rss"] = math.sqrt(sum(v * v for v in r["error"].values()))
    r["redondeo_ida_vuelta"] = kq
    return r


def main():
    r = calcular()
    cabecera()
    print(f"NTC ILUSTRATIVO: R0 = {R0:.0f} ohm a {T0} K, beta = {BETA:.0f} K ; divisor con {R_FIJA:.0f} ohm y Vref = {VREF} V ; ADC de {BITS_ADC} bits")
    print(f"{'T [K]':>7}{'R [ohm]':>14}{'V [V]':>9}{'codigo':>8}{'paso [K/cuenta]':>17}")
    for t, rr, v, k, res in r["filas"]:
        print(f"{t:>7.2f}{rr:>14.1f}{v:>9.4f}{k:>8d}{res:>17.4f}")
    print(f"Ida y vuelta T -> R -> T: error maximo = {r['ida_vuelta']:.2e} K")
    print("Autocalentamiento: " + "; ".join(f"{t:.0f} K: {p:.1f} uW -> {d*1e3:.2f} mK" for t, p, d in r["autocal"]))
    print("Platino (A = 3.9083e-3, B = -5.775e-7, no consultados): " + "; ".join(f"{tc:.0f} C: {rr:.3f} ohm" for tc, rr in r["pt"]) + f" ; error de la inversa = {r['pt_inv']:.1e} C")
    print("Presupuesto de error a 300 K: " + "; ".join(f"{k} = {v:.4f} K" for k, v in r["error"].items()) + f" ; RSS = {r['rss']:.4f} K")
    comprobar(r["ida_vuelta"] < 1e-9, "ida y vuelta")
    comprobar(r["pt_inv"] < 1e-9, "inversa de platino")
    comprobar(abs(r_pt(0.0) - 100.0) < 1e-12, "R(0 C)")
    fin()


if __name__ == "__main__":
    main()
