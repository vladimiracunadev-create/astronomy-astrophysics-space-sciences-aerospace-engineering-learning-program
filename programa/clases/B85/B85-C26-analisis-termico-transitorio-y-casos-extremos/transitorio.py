# SPDX-License-Identifier: Apache-2.0
"""B85-C26: análisis térmico transitorio: constante de tiempo, estabilidad numérica y caso extremo de eclipse y arranque.

Consultado: nada. ILUSTRATIVO y SINTÉTICO: nodo, flujos, órbita, arranque de un instrumento.
Segunda vía: solución analítica exponencial por tramos frente a Euler explícito, Euler implícito y RK4 con distintos pasos.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

C_N, G_N, T_REF = 1000.0, 1.0, 250.0         # J/K, W/K, K
TAU = C_N / G_N


def analitico(t0, q, t):
    teq = T_REF + q / G_N
    return teq + (t0 - teq) * math.exp(-t / TAU)


def explicito(t0, q, t, dt):
    x = t0
    for _ in range(int(round(t / dt))):
        x += dt * (q - G_N * (x - T_REF)) / C_N
    return x


def implicito(t0, q, t, dt):
    x = t0
    for _ in range(int(round(t / dt))):
        x = (x + dt / C_N * (q + G_N * T_REF)) / (1 + dt * G_N / C_N)
    return x


def rk4(t0, q, t, dt):
    x = t0
    f = lambda y: (q - G_N * (y - T_REF)) / C_N
    for _ in range(int(round(t / dt))):
        k1 = f(x); k2 = f(x + 0.5 * dt * k1); k3 = f(x + 0.5 * dt * k2); k4 = f(x + dt * k3)
        x += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return x


def calcular():
    r = {"filas": []}
    q, t0, tf = 40.0, 260.0, 3000.0
    ref = analitico(t0, q, tf)
    r["ref"] = ref
    for dt in (10.0, 100.0, 500.0, 1000.0, 2100.0):
        ex = explicito(t0, q, tf, dt) if tf / dt == int(tf / dt) or True else None
        r["filas"].append((dt, ex, implicito(t0, q, tf, dt), rk4(t0, q, tf, dt)))
    r["dt_critico"] = 2 * TAU
    # caso extremo: orbita fria (eclipse largo) y arranque de un instrumento
    ecl, sol = 2100.0, 3300.0
    q_e, q_s = 5.0, 45.0
    # periodica por tramos
    es, ee = math.exp(-sol / TAU), math.exp(-ecl / TAU)
    teq_s, teq_e = T_REF + q_s / G_N, T_REF + q_e / G_N
    tmax = (teq_s * (1 - es) + es * teq_e * (1 - ee)) / (1 - es * ee)
    tmin = teq_e + (tmax - teq_e) * ee
    r["tmin"], r["tmax"] = tmin, tmax
    # eclipse extendido 1.5x (caso extremo)
    ecl2 = 1.5 * ecl
    ee2 = math.exp(-ecl2 / TAU)
    r["tmin_extremo"] = teq_e + (tmax - teq_e) * ee2
    # arranque: instrumento +30 W desde t=0 con T inicial = tmin; tiempo para llegar al limite 300 K
    q_arr = q_s + 30.0
    teq_arr = T_REF + q_arr / G_N
    r["teq_arranque"] = teq_arr
    limite = 300.0
    r["t_limite"] = (-TAU * math.log((limite - teq_arr) / (tmin - teq_arr))) if teq_arr > limite else float("inf")
    r["tau"] = TAU
    r["t63"] = TAU
    r["t_95"] = -TAU * math.log(0.05)
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Nodo ILUSTRATIVO: C = {C_N:.0f} J/K, G = {G_N} W/K, T_ref = {T_REF:.0f} K ; tau = {r['tau']:.0f} s ; limite de estabilidad de Euler explicito dt < 2 tau = {r['dt_critico']:.0f} s")
    print(f"Escalon de 40 W desde 260 K durante 3000 s: analitico = {r['ref']:.4f} K")
    print(f"{'dt [s]':>8}{'explicito [K]':>16}{'implicito [K]':>16}{'RK4 [K]':>12}")
    for dt, ex, im, rk in r["filas"]:
        print(f"{dt:>8.0f}{ex:>16.4f}{im:>16.4f}{rk:>12.4f}")
    print(f"Orbita periodica (sol 3300 s con 45 W, eclipse 2100 s con 5 W): Tmin = {r['tmin']:.3f} K ; Tmax = {r['tmax']:.3f} K")
    print(f"Eclipse extendido 1.5x: Tmin = {r['tmin_extremo']:.3f} K (baja {r['tmin']-r['tmin_extremo']:.3f} K)")
    print(f"Arranque de un instrumento de 30 W: T de equilibrio = {r['teq_arranque']:.1f} K ; tiempo para alcanzar 300 K = {r['t_limite']:.0f} s")
    print(f"Tiempo de asentamiento al 95 % = {r['t_95']:.0f} s")
    f10 = r["filas"][0]
    comprobar(abs(f10[1] - r["ref"]) < 0.5 and abs(f10[2] - r["ref"]) < 0.5, "pasos pequenos")
    comprobar(abs(f10[3] - r["ref"]) < 1e-6, "RK4")
    comprobar(abs(r["filas"][-1][1] - r["ref"]) > 1.0, "explicito con dt = 2.1 tau se aparta")
    fin()


if __name__ == "__main__":
    main()
