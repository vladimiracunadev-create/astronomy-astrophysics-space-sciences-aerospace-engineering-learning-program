# SPDX-License-Identifier: Apache-2.0
"""B85-C17: criogenia de instrumentos: cargas parásitas, potencia de un criorrefrigerador y enfriamiento.

Consultado: SIGMA (NIST); NASA SST-SoA Thermal Control: criorrefrigeradores bajan a ~100 K o menos (puntas frías de 77 a 150 K en su tabla)
y los TEC se limitan por debajo de ~130 K. ILUSTRATIVO y SINTÉTICO: temperaturas, MLI, soportes, conductividad, masa, calor específico,
fracción de Carnot.
Segunda vía: integrador del enfriamiento (RK4) con capacidad constante frente a la solución analítica C ΔT / Q.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

TH = 300.0
A_MLI, N_CAPAS, EPS_CAPA = 0.5, 20, 0.05       # m2, -, -
K0, K1 = 0.1, 0.0035                           # k(T) = K0 + K1 T  [W/(m K)] ilustrativo (soporte tipo laminado)
N_SOP, A_SOP, L_SOP = 4, 20e-6, 0.05           # soportes: numero, m2 cada uno, m
Q_CABLE = 0.04                                 # W (arnes) a 80 K, ilustrativo
MASA, C0 = 5.0, 900.0                          # kg, J/(kg K) a 300 K
ETA_CARNOT = 0.10                              # fraccion de Carnot ilustrativa


def q_mli(tc):
    q_neg = SIGMA * (TH ** 4 - tc ** 4)
    return A_MLI * q_neg / ((N_CAPAS + 1) * (2 / EPS_CAPA - 1))


def q_soportes(tc):
    integral = K0 * (TH - tc) + 0.5 * K1 * (TH ** 2 - tc ** 2)
    return N_SOP * A_SOP / L_SOP * integral


def q_parasita(tc):
    return q_mli(tc) + q_soportes(tc) + Q_CABLE * (TH - tc) / (TH - 80.0)


def potencia_entrada(tc, q):
    cop = tc / (TH - tc)
    return q / (ETA_CARNOT * cop)


def cap_termica(t):
    return MASA * C0 * (t / 300.0) ** 1.5


def enfriar(q_cooler, t0=300.0, t_obj=80.0, c_const=None, paso=10.0):
    """Tiempo [s] hasta t_obj con un enfriador de potencia constante q_cooler y parasitas q_parasita(T); RK4 en T."""
    t, tiempo = t0, 0.0
    dt = paso
    while t > t_obj and tiempo < 1e8:
        def f(x):
            c = c_const if c_const else cap_termica(x)
            par = q_parasita(x) if c_const is None else 0.0
            return -(q_cooler - par) / c
        k1 = f(t); k2 = f(t + 0.5 * dt * k1); k3 = f(t + 0.5 * dt * k2); k4 = f(t + dt * k3)
        t += dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        tiempo += dt
    return tiempo


def calcular():
    r = {"filas": []}
    for tc in (20.0, 50.0, 80.0, 120.0, 150.0):
        q = q_parasita(tc)
        r["filas"].append((tc, q_mli(tc), q_soportes(tc), q, potencia_entrada(tc, q)))
    r["q80"] = q_parasita(80.0)
    r["p80"] = potencia_entrada(80.0, r["q80"])
    r["t_cool_5W"] = enfriar(5.0)
    r["t_cool_2W"] = enfriar(2.0)
    # prueba del integrador: capacidad constante y sin parasitas
    r["t_rk4_const"] = enfriar(5.0, c_const=2000.0, paso=10.0)
    r["t_analitico_const"] = 2000.0 * (300.0 - 80.0) / 5.0
    r["carnot_80"] = 80.0 / (TH - 80.0)
    r["p_igual_carnot"] = r["q80"] / r["carnot_80"]
    r["q80_sin_mli"] = SIGMA * 0.8 * A_MLI * (TH ** 4 - 80.0 ** 4)    # superficie desnuda, eps = 0.8
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Instrumento ILUSTRATIVO: MLI {N_CAPAS} capas (eps {EPS_CAPA}) sobre {A_MLI} m2, {N_SOP} soportes de {A_SOP*1e6:.0f} mm2 x {L_SOP*100:.0f} cm, entorno a {TH:.0f} K, fraccion de Carnot {ETA_CARNOT}")
    print(f"{'Tc [K]':>7}{'Q_MLI [W]':>11}{'Q_soportes [W]':>16}{'Q_total [W]':>13}{'P_entrada [W]':>15}")
    for tc, qm, qs, qt, p in r["filas"]:
        print(f"{tc:>7.0f}{qm:>11.4f}{qs:>16.4f}{qt:>13.4f}{p:>15.2f}")
    print(f"A 80 K: carga parasita = {r['q80']:.4f} W ; potencia de entrada = {r['p80']:.2f} W ; con refrigerador de Carnot ideal = {r['p_igual_carnot']:.3f} W")
    print(f"Superficie desnuda (eps = 0.8) a 80 K: {r['q80_sin_mli']:.2f} W frente a {r['q80']:.4f} W con MLI y soportes")
    print(f"Enfriamiento 300 K -> 80 K con un enfriador de 5 W: {r['t_cool_5W']/3600:.2f} h ; con 2 W: {r['t_cool_2W']/3600:.2f} h")
    print(f"Prueba del integrador (C constante 2000 J/K, 5 W): RK4 = {r['t_rk4_const']:.0f} s ; analitico = {r['t_analitico_const']:.0f} s")
    comprobar(abs(r["t_rk4_const"] - r["t_analitico_const"]) <= 10.0, "integrador")
    comprobar(r["t_cool_2W"] > r["t_cool_5W"], "mas potencia, menos tiempo")
    comprobar(all(r["filas"][i][3] > r["filas"][i + 1][3] for i in range(4)), "la carga baja con Tc mas alta")
    fin()


if __name__ == "__main__":
    main()
