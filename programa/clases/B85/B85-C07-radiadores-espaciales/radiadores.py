# SPDX-License-Identifier: Apache-2.0
"""B85-C07: radiadores espaciales: área según entorno y eficiencia de aleta.

Consultado: SIGMA (NIST), S0 (NASA/NSSDC), T_BB y albedo (NASA/NSSDC); NASA SST-SoA Thermal Control: un radiador necesita
ε infrarroja alta y α solar baja, y los coatings se oscurecen (usar EOL en el caso caliente).
ILUSTRATIVO: carga, temperatura, ε, α, factores de forma, geometría de la aleta, propiedades del material.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

Q, T_RAD, EPS = 500.0, 290.0, 0.85
ALFA_BOL, ALFA_EOL = 0.10, 0.25
T_FONDO = 3.0       # K ilustrativo (espacio profundo)


def area(q, t, eps, absorbido, t_fondo=T_FONDO):
    """Area [m2] de un radiador de una cara; 'absorbido' en W/m2 sobre su cara (solar + albedo + IR planetario)."""
    neto = eps * SIGMA * (t ** 4 - t_fondo ** 4) - absorbido
    return q / neto, neto


def eficiencia_lineal(t_b, k, t, longitud, eps):
    h = 4 * eps * SIGMA * t_b ** 3
    m = math.sqrt(2 * h / (k * t))
    return math.tanh(m * longitud) / (m * longitud), m


def aleta_numerica(t_b, k, esp, longitud, eps, n=200):
    """Aleta radiativa de dos caras con extremo aislado, por Newton sobre diferencias finitas. Devuelve Q por metro de ancho [W/m]."""
    dx = longitud / n
    T = [t_b] * n
    kk = k * esp / dx
    for _ in range(100):
        F = [0.0] * n
        J = [[0.0] * n for _ in range(n)]
        for i in range(n):
            izq = t_b if i == 0 else T[i - 1]
            F[i] = kk * (izq - T[i]) - (kk * (T[i] - T[i + 1]) if i < n - 1 else 0.0) - 2 * eps * SIGMA * T[i] ** 4 * dx
            J[i][i] = -kk - (kk if i < n - 1 else 0.0) - 8 * eps * SIGMA * T[i] ** 3 * dx
            if i > 0:
                J[i][i - 1] = kk
            if i < n - 1:
                J[i][i + 1] = kk
        dT = resolver_lineal(J, [-f for f in F])
        T = [T[i] + dT[i] for i in range(n)]
        if max(abs(x) for x in dT) < 1e-10:
            break
    return kk * (t_b - T[0]), T[-1]


def calcular():
    r = {}
    r["a_profundo"], _ = area(Q, T_RAD, EPS, 0.0)
    sol_bol = ALFA_BOL * S0 * 0.25
    sol_eol = ALFA_EOL * S0 * 0.25
    ir_alb = 0.2 * (EPS * SIGMA * T_BB_E ** 4 + ALFA_EOL * ALBEDO * S0 * 0.3)  # F = 0.2 ilustrativo
    r["abs_bol"] = sol_bol + 0.2 * (EPS * SIGMA * T_BB_E ** 4 + ALFA_BOL * ALBEDO * S0 * 0.3)
    r["abs_eol"] = sol_eol + ir_alb
    r["a_bol"], r["neto_bol"] = area(Q, T_RAD, EPS, r["abs_bol"])
    r["a_eol"], r["neto_eol"] = area(Q, T_RAD, EPS, r["abs_eol"])
    r["neto_sol_dir"] = EPS * SIGMA * (T_RAD ** 4 - T_FONDO ** 4) - (ALFA_EOL * S0 + ir_alb)
    r["a_T310"], _ = area(Q, 310.0, EPS, r["abs_eol"])
    r["q_por_m2_deep"] = EPS * SIGMA * (T_RAD ** 4 - T_FONDO ** 4)
    # segunda via: potencia que rechaza el area calculada
    r["resid"] = r["a_eol"] * (EPS * SIGMA * (T_RAD ** 4 - T_FONDO ** 4) - r["abs_eol"]) - Q
    # aleta
    k, esp, L = 160.0, 2e-3, 0.30
    r["eta_lin"], r["m"] = eficiencia_lineal(T_RAD, k, esp, L, EPS)
    qn, t_tip = aleta_numerica(T_RAD, k, esp, L, EPS)
    r["q_aleta_num"], r["t_punta"] = qn, t_tip
    r["q_aleta_ideal"] = 2 * EPS * SIGMA * T_RAD ** 4 * L
    r["eta_num"] = qn / r["q_aleta_ideal"]
    qk, _ = aleta_numerica(T_RAD, 1e6, esp, 0.05, EPS, n=60)
    r["eta_k_alta"] = qk / (2 * EPS * SIGMA * T_RAD ** 4 * 0.05)
    return r


def main():
    r = calcular()
    cabecera()
    print(f"Radiador ILUSTRATIVO: Q = {Q:.0f} W a {T_RAD:.0f} K, eps = {EPS}, alfa BOL/EOL = {ALFA_BOL}/{ALFA_EOL}; fondo {T_FONDO:.0f} K")
    print(f"Espacio profundo (sin absorbido): flujo neto = {r['q_por_m2_deep']:.2f} W/m2 -> A = {r['a_profundo']:.4f} m2")
    print(f"Orbita baja, caso caliente BOL: absorbido = {r['abs_bol']:.2f} W/m2, neto = {r['neto_bol']:.2f} W/m2 -> A = {r['a_bol']:.4f} m2")
    print(f"Orbita baja, caso caliente EOL: absorbido = {r['abs_eol']:.2f} W/m2, neto = {r['neto_eol']:.2f} W/m2 -> A = {r['a_eol']:.4f} m2")
    print(f"Con Sol directo EOL: flujo neto = {r['neto_sol_dir']:.2f} W/m2 (negativo: no rechaza nada) ; radiador a 310 K (EOL): A = {r['a_T310']:.4f} m2")
    print(f"Residuo de potencia rechazada = {r['resid']:.2e} W")
    print(f"Aleta (k = 160 W/(m K), e = 2 mm, L = 0.30 m, 290 K en la raiz): m = {r['m']:.3f} 1/m ; eta lineal = {r['eta_lin']:.4f}")
    print(f"  Numerica: Q = {r['q_aleta_num']:.3f} W/m ; ideal = {r['q_aleta_ideal']:.3f} W/m ; eta = {r['eta_num']:.4f} ; T punta = {r['t_punta']:.2f} K")
    print(f"  Prueba con k = 1e6 y L = 0.05 m (casi isoterma): eta = {r['eta_k_alta']:.5f}")
    comprobar(abs(r["resid"]) < 1e-9, "potencia")
    comprobar(r["a_eol"] > r["a_bol"] > r["a_profundo"], "orden de areas")
    comprobar(r["eta_lin"] < r["eta_num"] < r["eta_lin"] + 0.06, "eficiencia de aleta")
    comprobar(abs(r["eta_k_alta"] - 1.0) < 1e-3, "aleta casi isoterma")
    fin()


if __name__ == "__main__":
    main()
