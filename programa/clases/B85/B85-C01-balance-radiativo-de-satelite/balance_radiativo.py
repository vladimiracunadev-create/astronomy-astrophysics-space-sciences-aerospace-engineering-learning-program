# SPDX-License-Identifier: Apache-2.0
"""B85-C01: balance radiativo de un satélite esférico (caso caliente y frío) y de una placa.

Consultado: SIGMA (NIST), S0, ALBEDO, T_BB_E, R_E (NASA/NSSDC). ILUSTRATIVO: geometría, α, ε, órbita, disipación.
Modelo: nodo isotermo, superficie gris difusa (ε infrarroja = α infrarroja), cuerpo esférico.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

RADIO, ALT = 0.5, 500e3       # m (ilustrativo)
ALFA, EPS, Q_INT = 0.30, 0.80, 50.0  # ilustrativo; W


def temperatura_equilibrio(q_abs, area, eps):
    return (q_abs / (eps * SIGMA * area)) ** 0.25


def casos(alfa=ALFA, eps=EPS, q_int=Q_INT):
    area = 4 * math.pi * RADIO ** 2
    a_proy = math.pi * RADIO ** 2
    f = factor_forma_esfera_tierra(ALT)
    m_ir = SIGMA * T_BB_E ** 4
    sol = alfa * S0 * a_proy
    alb = alfa * ALBEDO * S0 * f * area      # cota superior: exitancia subsolar sobre todo el casquete visible
    ir = eps * m_ir * f * area
    t_caliente = temperatura_equilibrio(sol + alb + ir + q_int, area, eps)
    t_frio = temperatura_equilibrio(ir + q_int, area, eps)
    return dict(area=area, a_proy=a_proy, f=f, m_ir=m_ir, sol=sol, alb=alb, ir=ir,
                t_caliente=t_caliente, t_frio=t_frio)


def calcular():
    r = casos()
    # segunda via: raiz del balance por biseccion
    def resid(t, q):
        return EPS * SIGMA * r["area"] * t ** 4 - q
    q_c = r["sol"] + r["alb"] + r["ir"] + Q_INT
    r["t_biseccion"] = biseccion(lambda t: resid(t, q_c), 100.0, 500.0)
    r["t_sol_solo"] = (S0 / (4 * SIGMA)) ** 0.25          # esfera negra, solo Sol
    r["t_sol_solo_num"] = temperatura_equilibrio(S0 * r["a_proy"], r["area"], 1.0)
    r["t_placa_1cara"] = (ALFA * S0 / (EPS * SIGMA)) ** 0.25
    r["t_placa_2caras"] = (ALFA * S0 / (2 * EPS * SIGMA)) ** 0.25
    r["t_alfa_09"] = casos(alfa=0.9)["t_caliente"]
    r["t_q200"] = casos(q_int=200.0)["t_frio"]
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Esfera ILUSTRATIVA: r = {RADIO} m, h = {ALT/1e3:.0f} km, alfa = {ALFA}, eps = {EPS}, Q_int = {Q_INT} W")
    print(f"Area total = {r['area']:.4f} m2 ; area proyectada = {r['a_proy']:.4f} m2 ; F(esfera->Tierra) = {r['f']:.4f}")
    print(f"M_IR = sigma*T_BB^4 = {r['m_ir']:.2f} W/m2 (T_BB = {T_BB_E} K)")
    print(f"Caso caliente: Sol {r['sol']:.1f} W + albedo {r['alb']:.1f} W + IR {r['ir']:.1f} W + interna {Q_INT} W -> T = {r['t_caliente']:.2f} K")
    print(f"Caso frio (eclipse): IR {r['ir']:.1f} W + interna {Q_INT} W -> T = {r['t_frio']:.2f} K")
    print(f"Biseccion (caso caliente) T = {r['t_biseccion']:.4f} K")
    print(f"Esfera negra solo Sol: T = {r['t_sol_solo']:.2f} K (formula) ; {r['t_sol_solo_num']:.2f} K (balance)")
    print(f"Placa al Sol: una cara {r['t_placa_1cara']:.2f} K ; dos caras {r['t_placa_2caras']:.2f} K")
    print(f"Sensibilidad: alfa = 0.9 -> T caliente {r['t_alfa_09']:.2f} K ; Q_int = 200 W -> T frio {r['t_q200']:.2f} K")
    comprobar(abs(r["t_caliente"] - r["t_biseccion"]) < 1e-6, "biseccion distinta")
    comprobar(abs(r["t_sol_solo"] - r["t_sol_solo_num"]) < 1e-9, "esfera negra")
    comprobar(r["t_caliente"] > r["t_frio"], "caliente > frio")
    fin()


if __name__ == "__main__":
    main()
