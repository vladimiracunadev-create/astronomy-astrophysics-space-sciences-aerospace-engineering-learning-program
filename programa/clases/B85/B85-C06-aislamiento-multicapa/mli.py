# SPDX-License-Identifier: Apache-2.0
"""B85-C06: aislamiento multicapa (MLI): N pantallas radiativas entre una cara caliente y una fría.

Consultado: SIGMA (NIST); de NASA SST-SoA Thermal Control: MLI típica de 10 a 20 capas de baja emisividad, y que su
rendimiento cae mucho si se comprime. ILUSTRATIVO: ε, temperaturas, conductancia entre capas.
Segunda vía: red de N nodos resuelta con Newton (sin la fórmula 1/(N+1)).
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from termico_comun import *

TH, TC, EPS = 300.0, 100.0, 0.05     # K, K, - (ilustrativos)


def q_formula(n, eps=EPS, th=TH, tc=TC):
    return SIGMA * (th ** 4 - tc ** 4) / ((n + 1) * (2.0 / eps - 1.0))


def q_red(n, eps=EPS, gc=0.0, th=TH, tc=TC):
    """Red con n pantallas: cada hueco tiene resistencia radiativa (2/eps - 1) y, opcionalmente, conductancia gc [W/m2K]
    entre capas contiguas. Incognitas: temperaturas de las pantallas. Devuelve flujo [W/m2] y temperaturas."""
    if n == 0:
        T = []
    T = [th - (th - tc) * (i + 1) / (n + 1) for i in range(n)]
    R = 2.0 / eps - 1.0

    def flujo(a, b):
        return SIGMA * (a ** 4 - b ** 4) / R + gc * (a - b)

    for _ in range(200):
        nodos = [th] + T + [tc]
        res = [flujo(nodos[i], nodos[i + 1]) - flujo(nodos[i + 1], nodos[i + 2]) for i in range(n)]
        if n == 0 or max(abs(x) for x in res) < 1e-12:
            break
        J = [[0.0] * n for _ in range(n)]
        for i in range(n):
            a, b, cc = nodos[i], nodos[i + 1], nodos[i + 2]
            J[i][i] = -(4 * SIGMA * b ** 3 / R + gc) - (4 * SIGMA * b ** 3 / R + gc)
            if i > 0:
                J[i][i - 1] = 4 * SIGMA * a ** 3 / R + gc
            if i < n - 1:
                J[i][i + 1] = 4 * SIGMA * cc ** 3 / R + gc
        dx = resolver_lineal(J, [-x for x in res])
        T = [T[i] + dx[i] for i in range(n)]
    nodos = [th] + T + [tc]
    return flujo(nodos[0], nodos[1]), T


def calcular():
    r = {"filas": []}
    for n in (0, 1, 5, 10, 20, 40):
        qf = q_formula(n)
        qr, T = q_red(n)
        eeff = qf / (SIGMA * (TH ** 4 - TC ** 4))
        r["filas"].append((n, qf, qr, eeff))
    r["q_sin"] = q_formula(0)
    r["q10"] = q_formula(10)
    r["q20"] = q_formula(20)
    r["q10_comprimida"], r["T10_comp"] = q_red(10, gc=0.05)
    r["q10_red"], r["T10"] = q_red(10)
    r["q_negro"] = SIGMA * (TH ** 4 - TC ** 4)
    r["q_eps_10"] = q_formula(10, eps=0.10)
    r["n_para_5"] = next(n for n in range(0, 400) if q_formula(n) <= 5.0)
    return r


def main():
    r = calcular()
    cabecera()
    print(f"MLI ILUSTRATIVA: eps = {EPS} en todas las caras, T_caliente = {TH:.0f} K, T_fria = {TC:.0f} K, solo radiacion")
    print(f"Flujo entre superficies negras = {r['q_negro']:.2f} W/m2")
    print(f"{'N':>4}{'q formula':>12}{'q red':>12}{'eps_eff':>11}")
    for n, qf, qr, ee in r["filas"]:
        print(f"{n:>4}{qf:>12.5f}{qr:>12.5f}{ee:>11.5f}")
    print(f"Temperaturas de las 10 pantallas (K): " + ", ".join(f"{t:.1f}" for t in r["T10"]))
    print(f"N = 10 con conductancia entre capas gc = 0.05 W/(m2 K) (capas comprimidas): q = {r['q10_comprimida']:.4f} W/m2 (x{r['q10_comprimida']/r['q10']:.2f})")
    print(f"N = 10 con eps = 0.10: q = {r['q_eps_10']:.4f} W/m2")
    print(f"Capas para q <= 5 W/m2 con eps = 0.05: N = {r['n_para_5']}")
    for n, qf, qr, ee in r["filas"]:
        comprobar(abs(qf - qr) / qf < 1e-9, f"formula frente a red N={n}")
    comprobar(abs(r["filas"][0][1] - r["q_negro"] / (2 / EPS - 1)) < 1e-9, "N = 0")
    fin()


if __name__ == "__main__":
    main()
