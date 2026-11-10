# SPDX-License-Identifier: Apache-2.0
"""B85-C02: conducción estacionaria en una estructura: resistencias en serie, contacto y aleta.

Todo ILUSTRATIVO (propiedades de un aluminio genérico, geometría sintética). No se consultó ninguna tabla de materiales.
Segunda vía: diferencias finitas 1D para la barra y para la aleta.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

K_AL = 150.0       # W/(m K) ilustrativo
A_SEC = 4e-4       # m2 (20 mm x 20 mm)
L_TOT = 0.30       # m
H_C = 800.0        # W/(m2 K) conductancia de contacto ilustrativa
T_CAL, T_FRIA = 320.0, 280.0


def barra_con_contacto():
    r_barra = L_TOT / (K_AL * A_SEC)
    r_cont = 1.0 / (H_C * A_SEC)
    q = (T_CAL - T_FRIA) / (r_barra + r_cont)
    return r_barra, r_cont, q


def barra_dif_finitas(n=60, rc=0.0):
    """Cadena de n tramos con una resistencia de contacto rc en el tramo central; nodos 0..n, extremos fijos."""
    dx = L_TOT / n
    g = K_AL * A_SEC / dx
    arista = [g] * n
    arista[n // 2] = 1.0 / (1.0 / g + rc)
    A = [[0.0] * (n - 1) for _ in range(n - 1)]
    b = [0.0] * (n - 1)
    for i in range(1, n):            # nodo global i -> fila i-1
        gm, gp = arista[i - 1], arista[i]
        A[i - 1][i - 1] = gm + gp
        if i > 1:
            A[i - 1][i - 2] = -gm
        else:
            b[i - 1] += gm * T_CAL
        if i < n - 1:
            A[i - 1][i] = -gp
        else:
            b[i - 1] += gp * T_FRIA
    T = resolver_lineal(A, b)
    return arista[0] * (T_CAL - T[0])


def aleta(h=10.0, p=0.08, n=400):
    """Aleta de longitud L con extremo aislado: analítica (tanh) y diferencias finitas."""
    L, tb, tinf = 0.10, 320.0, 280.0
    m = math.sqrt(h * p / (K_AL * A_SEC))
    q_an = math.sqrt(h * p * K_AL * A_SEC) * (tb - tinf) * math.tanh(m * L)
    dx = L / n
    A = [[0.0] * n for _ in range(n)]
    b = [0.0] * n
    g = K_AL * A_SEC / dx
    for i in range(n):
        A[i][i] = 2 * g + h * p * dx
        if i > 0:
            A[i][i - 1] = -g
        else:
            b[i] += g * tb
        if i < n - 1:
            A[i][i + 1] = -g
        else:
            A[i][i] -= g            # extremo aislado
        b[i] += h * p * dx * tinf
    T = resolver_lineal(A, b)
    q_num = g * (tb - T[0])
    return q_an, q_num, m, math.tanh(m * L) / (m * L)


def calcular():
    rb, rc, q = barra_con_contacto()
    r = dict(r_barra=rb, r_cont=rc, q=q, q_sin_contacto=(T_CAL - T_FRIA) / rb)
    r["t_salto_contacto"] = q * rc
    # contraste numerico con contacto de resistencia rc entre dos mitades
    n = 60
    rc_nodal = rc
    dx = L_TOT / n
    g = K_AL * A_SEC / dx
    # resolver con arista central de resistencia 1/g + rc
    r["q_num"] = barra_dif_finitas(n, rc_nodal)
    r["q_aleta_an"], r["q_aleta_num"], r["m"], r["eta"] = aleta()
    r["k_doble_q"] = (T_CAL - T_FRIA) / (L_TOT / (2 * K_AL * A_SEC) + rc)
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Barra ILUSTRATIVA: k = {K_AL} W/(m K), A = {A_SEC*1e4:.1f} cm2, L = {L_TOT} m, h_contacto = {H_C} W/(m2 K), {T_CAL:.0f} K -> {T_FRIA:.0f} K")
    print(f"R_barra = {r['r_barra']:.3f} K/W ; R_contacto = {r['r_cont']:.3f} K/W")
    print(f"Q con contacto = {r['q']:.4f} W ; sin contacto = {r['q_sin_contacto']:.4f} W ; salto en el contacto = {r['t_salto_contacto']:.3f} K")
    print(f"Diferencias finitas (60 nodos, contacto en el centro): Q = {r['q_num']:.4f} W")
    print(f"Aleta (h = 10 W/(m2 K), p = 0.08 m, L = 0.10 m): m = {r['m']:.3f} 1/m ; eta = {r['eta']:.4f}")
    print(f"  Q analitico = {r['q_aleta_an']:.5f} W ; Q numerico = {r['q_aleta_num']:.5f} W")
    print(f"Con k doble en la barra: Q = {r['k_doble_q']:.4f} W")
    comprobar(abs(r["q"] - r["q_num"]) / r["q"] < 1e-9, "barra: red frente a serie")
    comprobar(abs(r["q_aleta_an"] - r["q_aleta_num"]) / r["q_aleta_an"] < 5e-3, "aleta")
    fin()


if __name__ == "__main__":
    main()
