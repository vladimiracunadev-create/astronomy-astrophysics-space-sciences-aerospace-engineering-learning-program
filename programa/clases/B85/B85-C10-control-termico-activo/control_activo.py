# SPDX-License-Identifier: Apache-2.0
"""B85-C10: control térmico activo: lazo PI con calentador, saturación y antiwindup.

Consultado: de NASA SST-SoA Thermal Control: lazos de fluido con calentadores y control PID por zonas; calentadores controlados por termostato o sensor.
ILUSTRATIVO: nodo, ganancias, potencia máxima, perturbación.
Segunda vía: polos del lazo lineal (ζ y ωn) frente a la simulación, y valores finales analíticos.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

C_N, G_N = 1500.0, 0.30        # J/K, W/K (acoplamiento linealizado al sumidero)
T_SUM = 250.0                  # K
T_SET = 283.0
P_MAX = 30.0
DT = 1.0


def simular(kp, ki, antiwindup=True, p_max=P_MAX, t_fin=6000.0, t_pert=3000.0, d_sum=-10.0):
    t = T_SUM
    integral = 0.0
    hist = []
    for k in range(int(t_fin / DT)):
        ts = k * DT
        sumidero = T_SUM + (d_sum if ts >= t_pert else 0.0)
        e = T_SET - t
        u_sin = kp * e + ki * integral
        u = min(max(u_sin, 0.0), p_max)
        if not antiwindup or u == u_sin or (u_sin > p_max and e < 0) or (u_sin < 0 and e > 0):
            integral += e * DT
        t += DT * (-G_N * (t - sumidero) + u) / C_N
        hist.append((ts, t, u))
    return hist


def metricas(hist, t_ini=0.0, t_fin=3000.0):
    tramo = [h for h in hist if t_ini <= h[0] < t_fin]
    pico = max(h[1] for h in tramo)
    sobre = pico - T_SET
    liquida = next((h[0] for h in tramo if abs(h[1] - T_SET) < 0.5 and all(abs(x[1] - T_SET) < 0.5 for x in tramo if x[0] >= h[0])), None)
    return pico, sobre, liquida


def calcular():
    r = {}
    kp, ki = 20.0, 0.05
    r["kp"], r["ki"] = kp, ki
    r["p_final_esperada"] = G_N * (T_SET - T_SUM)
    r["p_final_pert"] = G_N * (T_SET - (T_SUM - 10.0))
    h = simular(kp, ki)
    r["h"] = h
    r["pico"], r["sobre"], r["t_liq"] = metricas(h)
    r["t_antes"] = h[2999][1]
    r["u_antes"] = h[2999][2]
    r["t_fin"] = h[-1][1]
    r["u_fin"] = h[-1][2]
    r["error_final"] = T_SET - h[-1][1]
    # polos del lazo lineal sin saturacion
    wn = math.sqrt(ki / C_N)
    zeta = (G_N + kp) / (2 * math.sqrt(C_N * ki))
    r["wn"], r["zeta"] = wn, zeta
    # saturacion con y sin antiwindup (Kp bajo, Ki alto)
    r["con_aw"] = metricas(simular(2.0, 0.5, True, t_fin=3000.0), 0, 3000.0)
    r["sin_aw"] = metricas(simular(2.0, 0.5, False, t_fin=3000.0), 0, 3000.0)
    r["con_aw_pmax"] = max(x[2] for x in simular(20.0, 0.05, True, t_fin=3000.0))
    # potencia de pico en el arranque
    r["u_pico"] = max(x[2] for x in h)
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Nodo ILUSTRATIVO: C = {C_N:.0f} J/K, G = {G_N} W/K, sumidero {T_SUM:.0f} K, consigna {T_SET:.0f} K, calentador maximo {P_MAX:.0f} W")
    print(f"PI: Kp = {r['kp']} W/K, Ki = {r['ki']} W/(K s) ; polos lineales: wn = {r['wn']:.5f} rad/s, zeta = {r['zeta']:.2f}")
    print(f"Potencia de regimen esperada = G (Tset - Tsum) = {r['p_final_esperada']:.2f} W ; tras bajar el sumidero 10 K = {r['p_final_pert']:.2f} W")
    print(f"Antes de la perturbacion (t = 3000 s): T = {r['t_antes']:.4f} K ; P = {r['u_antes']:.3f} W")
    print(f"Pico = {r['pico']:.3f} K ; sobreimpulso = {r['sobre']:.3f} K ; tiempo de asentamiento (+-0.5 K) = {r['t_liq']:.0f} s ; P maxima = {r['u_pico']:.2f} W")
    print(f"Final (t = 6000 s): T = {r['t_fin']:.4f} K ; P = {r['u_fin']:.3f} W ; error = {r['error_final']:.2e} K")
    print(f"Kp = 2, Ki = 0.5 con saturacion: sobreimpulso con antiwindup = {r['con_aw'][1]:.3f} K ; sin antiwindup = {r['sin_aw'][1]:.3f} K")
    comprobar(abs(r["u_antes"] - r["p_final_esperada"]) < 0.05, "potencia de regimen antes")
    comprobar(abs(r["u_fin"] - r["p_final_pert"]) < 0.05, "potencia de regimen tras la perturbacion")
    comprobar(abs(r["error_final"]) < 1e-2, "error nulo")
    comprobar(r["sin_aw"][1] > r["con_aw"][1], "el antiwindup reduce el sobreimpulso")
    comprobar(r["u_pico"] <= P_MAX + 1e-9, "saturacion")
    fin()


if __name__ == "__main__":
    main()
