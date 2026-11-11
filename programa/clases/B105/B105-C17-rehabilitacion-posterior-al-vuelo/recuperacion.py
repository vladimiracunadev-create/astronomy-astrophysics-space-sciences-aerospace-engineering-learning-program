#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C17: curvas de recuperacion posterior al vuelo, ajuste y tiempos (datos SINTETICOS).

Modelo: variable funcional (por ejemplo, fuerza o equilibrio) como porcentaje del valor previo al vuelo: y(t) = 100 - L e^{-k t}, t en dias desde el aterrizaje;
L = 30 puntos de deficit inicial y k = 0.05 1/dia (semivida 13.9 d) son ILUSTRATIVOS. Mediciones SINTETICAS en t = 1, 3, 7, 14, 30, 60 dias con ruido normal
de DE 1.5 puntos; ajuste log-lineal del deficit D = 100 - y: ln D = ln L - k t. Incertidumbre por bootstrap parametrico (2000 repeticiones). Semilla 105.
No se consultaron datos de rehabilitacion; es un ejercicio de ajuste. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

L, K, SIG = 30.0, 0.05, 1.5
T = np.array([1, 3, 7, 14, 30, 60.0])


def modelo(t, l=L, k=K):
    return 100 - l * np.exp(-k * t)


def ajustar(y):
    d = 100 - y
    ok = d > 0.5
    pen, ord_ = np.polyfit(T[ok], np.log(d[ok]), 1)
    return np.exp(ord_), -pen


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS (semilla 105): deficit inicial 30 puntos, k = 0.05/dia, ruido 1.5 puntos; sin datos de rehabilitacion")
    rng = np.random.default_rng(105)
    y = modelo(T) + rng.normal(0, SIG, T.size)
    print("t [d]:      " + " ".join(f"{t:6.0f}" for t in T))
    print("y [% previo]:" + " ".join(f"{v:6.1f}" for v in y) + "   (modelo: " + " ".join(f"{v:5.1f}" for v in modelo(T)) + ")")
    l_h, k_h = ajustar(y)
    print(f"Ajuste log-lineal: L = {l_h:.1f} (verdad {L:.0f}), k = {k_h:.4f}/dia (verdad {K}); semivida = {np.log(2) / k_h:.1f} d (verdad {np.log(2) / K:.1f})")
    ks, ls = [], []
    for _ in range(2000):
        yb = modelo(T, l_h, k_h) + rng.normal(0, SIG, T.size)
        lb, kb = ajustar(yb)
        ls.append(lb); ks.append(kb)
    ks = np.array(ks); ls = np.array(ls)
    print(f"Bootstrap parametrico: k p2.5-p97.5 = {np.percentile(ks, 2.5):.4f}-{np.percentile(ks, 97.5):.4f}; L p2.5-p97.5 = {np.percentile(ls, 2.5):.1f}-{np.percentile(ls, 97.5):.1f}")
    for p in (50, 90, 95):
        t_p = np.log(L / (100 - p)) / K if (100 - p) < L else 0.0
        print(f"Tiempo para recuperar el {p} % del valor previo (modelo verdadero) = {t_p:5.1f} d; con el ajuste = {np.log(l_h / (100 - p)) / k_h:5.1f} d" if (100 - p) < L else f"  el {p} % ya se cumple al aterrizar")
    t_ic = np.log(l_h / 5.0) / ks
    print(f"Tiempo al 95 % con incertidumbre: mediana {np.median(np.log(ls / 5.0) / ks):.1f} d; p2.5-p97.5 = {np.percentile(np.log(ls / 5.0) / ks, 2.5):.1f}-{np.percentile(np.log(ls / 5.0) / ks, 97.5):.1f} d")
    # una persona lenta: k mitad
    print(f"Con k = {K / 2:.3f}/dia (persona lenta, ilustrativa) el 95 % llega a los {np.log(L / 5.0) / (K / 2):.1f} d")
    assert abs(k_h - K) < 0.02
    assert abs(np.log(2) / K - 13.86) < 0.01
    assert np.percentile(ks, 2.5) < K < np.percentile(ks, 97.5) or abs(k_h - K) < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
