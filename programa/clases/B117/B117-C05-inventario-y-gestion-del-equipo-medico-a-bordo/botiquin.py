#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B117-C05: seleccion de un botiquin SINTETICO bajo limites de masa y volumen, y riesgo de desabastecimiento.

CONTENIDO EDUCATIVO: no es una lista de equipo medico ni consejo medico u operativo; no sustituye formacion ni supervision profesional.
Datos consultados (2026-11-10): resumen del Integrated Medical Model de la NASA (Myers et al., NTRS 20140016998): el IMM estima de forma
probabilistica 100 condiciones medicas y sus metricas permiten estimar el contenido optimo de un botiquin bajo restricciones de masa y volumen
o de nivel de riesgo aceptable. El IMM no se uso para obtener ningun numero de este laboratorio.
ILUSTRATIVOS (sinteticos, no medidos): los 8 articulos GENERICOS (masa, volumen, eventos esperados por mision, peso de gravedad),
los topes de 4000 g y 6000 cm3, el maximo de 3 unidades por articulo (1 el equipo de RCP) y la demanda de Poisson.
Modelo: beneficio(i, k) = w_i E[min(N_i, k)], N_i ~ Poisson(mu_i); P(desabastecimiento) = P(N_i > k).
Unidades: g, cm3, eventos por mision de 180 d (ilustrativo). Escala de DP: 10 g y 10 cm3.
Tolerancias: DP frente a busqueda exhaustiva: igualdad del beneficio dentro de 1e-9; Monte Carlo (20000 misiones, semilla 117)
frente a Poisson analitico < 0.01 en P(N > k).
"""
from __future__ import annotations
import itertools, math, platform, random

ITEMS = [  # nombre, masa g, volumen cm3, mu, peso, kmax
    ("vendas y apositos", 40, 80, 2.0, 1.0, 3),
    ("analgesico generico", 30, 40, 3.0, 1.0, 3),
    ("antiseptico", 60, 100, 1.5, 1.0, 3),
    ("hemostatico", 120, 200, 0.4, 5.0, 3),
    ("antibiotico generico", 100, 120, 0.6, 4.0, 3),
    ("pulsioximetro", 80, 150, 1.0, 3.0, 3),
    ("botella de oxigeno", 900, 1500, 0.1, 20.0, 3),
    ("equipo de RCP", 2400, 3000, 0.02, 50.0, 1),
]
M_MAX, V_MAX = 4000, 6000


def pois_pmf(j, mu):
    return math.exp(-mu) * mu ** j / math.factorial(j)


def p_ge(j, mu):
    return 1.0 - sum(pois_pmf(i, mu) for i in range(j))


def e_min(k, mu):
    return sum(p_ge(j, mu) for j in range(1, k + 1))


def beneficio(i, k):
    return ITEMS[i][4] * e_min(k, ITEMS[i][3])


def p_falta(i, k):
    return p_ge(k + 1, ITEMS[i][3])


def dp_optimo():
    um, uv = 10, 10
    mc, vc = M_MAX // um, V_MAX // uv
    n = len(ITEMS)
    best = [[0.0] * (vc + 1) for _ in range(mc + 1)]
    elec = [[[0] * (vc + 1) for _ in range(mc + 1)] for _ in range(n)]
    for i in range(n):
        nom, m, v, mu, w, kmax = ITEMS[i]
        mi, vi = math.ceil(m / um), math.ceil(v / uv)
        nuevo = [fila[:] for fila in best]
        for a in range(mc + 1):
            for b in range(vc + 1):
                for k in range(1, kmax + 1):
                    if a >= k * mi and b >= k * vi:
                        val = best[a - k * mi][b - k * vi] + beneficio(i, k)
                        if val > nuevo[a][b] + 1e-12:
                            nuevo[a][b] = val
                            elec[i][a][b] = k
        best = nuevo
    a, b = mc, vc
    cuenta = [0] * n
    for i in range(n - 1, -1, -1):
        k = elec[i][a][b]
        cuenta[i] = k
        a -= k * math.ceil(ITEMS[i][1] / um)
        b -= k * math.ceil(ITEMS[i][2] / uv)
    return best[mc][vc], cuenta


def exhaustivo():
    mejor, mejor_c = -1.0, None
    rangos = [range(0, it[5] + 1) for it in ITEMS]
    for c in itertools.product(*rangos):
        m = sum(c[i] * ITEMS[i][1] for i in range(len(ITEMS)))
        v = sum(c[i] * ITEMS[i][2] for i in range(len(ITEMS)))
        if m > M_MAX or v > V_MAX:
            continue
        b = sum(beneficio(i, c[i]) for i in range(len(ITEMS)) if c[i])
        if b > mejor + 1e-12:
            mejor, mejor_c = b, c
    return mejor, list(mejor_c)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Articulos GENERICOS y SINTETICOS (ilustrativos); solo el concepto del IMM de la NASA es consultado.")
    print(f"Limites: masa {M_MAX} g, volumen {V_MAX} cm3; eventos esperados por mision de 180 d (ilustrativo)")
    b_dp, c_dp = dp_optimo()
    b_ex, c_ex = exhaustivo()
    print(f"Beneficio optimo DP = {b_dp:.6f} ; busqueda exhaustiva = {b_ex:.6f} ; selecciones iguales: {c_dp == c_ex}")
    print(" articulo                 k   masa[g]  vol[cm3]  mu    P(falta)")
    mt = vt = 0
    for i, k in enumerate(c_dp):
        nom, m, v, mu, w, kmax = ITEMS[i]
        mt += k * m
        vt += k * v
        pf = p_falta(i, k)
        print(f"{nom:24s} {k:2d} {k * m:9d} {k * v:9d} {mu:5.2f} {pf:9.4f}")
    print(f"Total: masa = {mt} g ({mt / M_MAX:.1%}); volumen = {vt} cm3 ({vt / V_MAX:.1%})")
    # Monte Carlo
    rng = random.Random(117)
    reps, err = 20000, 0.0
    for i, k in enumerate(c_dp):
        mu = ITEMS[i][3]
        L = math.exp(-mu)
        cnt = 0
        for _ in range(reps):
            n, p = 0, 1.0
            while True:
                p *= rng.random()
                if p <= L:
                    break
                n += 1
            if n > k:
                cnt += 1
        err = max(err, abs(cnt / reps - p_falta(i, k)))
    print(f"Error maximo Monte Carlo - Poisson en P(falta) = {err:.4f}")
    # duplicar la duracion de la mision: mu x 2 con el mismo botiquin
    print("Mision del doble de duracion (mu x 2) con el mismo botiquin:")
    for i, k in enumerate(c_dp):
        mu2 = 2 * ITEMS[i][3]
        print(f"  {ITEMS[i][0]:24s} P(falta) {p_falta(i, k):.4f} -> {p_ge(k + 1, mu2):.4f}")
    assert abs(b_dp - b_ex) < 1e-9
    assert mt <= M_MAX and vt <= V_MAX
    assert err < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
