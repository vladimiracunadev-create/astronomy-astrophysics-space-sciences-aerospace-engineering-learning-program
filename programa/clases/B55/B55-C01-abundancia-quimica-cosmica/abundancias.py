#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B55-C01: de abundancias logaritmicas (log eps) a fracciones en numero y en masa (X, Y, Z).

Datos: las masas atomicas de H, C, N y O se calculan con las masas isotopicas relativas y las composiciones isotopicas del NIST
(Atomic Weights and Isotopic Compositions, consultado el 2026-11-09); las de He, Mg, Si, Ca y Fe son los pesos atomicos estandar del NIST
(He 4.002602, Mg 24.305 como punto medio del intervalo [24.304, 24.307], Si 28.085 como punto medio de [28.084, 28.086], Ca 40.078, Fe 55.845).
Los valores de log eps de la mezcla son ILUSTRATIVOS (redondeados para el ejemplo; NO son los valores de Asplund et al. 2009, de los que solo se leyo el resumen).
Modelo: log eps_i = log10(N_i / N_H) + 12 ; fraccion en masa X_i = N_i m_i / sum_j N_j m_j.
Supuestos: mezcla de solo 8 elementos (no es una composicion completa); sin tener en cuenta moleculas ni granos. Validez: ilustrativa.
Tolerancia: suma de fracciones en masa = 1 a 1e-12; ida y vuelta log eps -> X -> log eps a 1e-10 dex; X por dos caminos de calculo a 1e-12.
"""
from __future__ import annotations
import math, platform

# ---- masas atomicas (u) ----
ISO = {  # elemento: [(masa relativa, abundancia isotopica)]  (NIST)
    "H": [(1.00782503223, 0.999885), (2.01410177812, 0.000115)],
    "C": [(12.0, 0.9893), (13.00335483507, 0.0107)],
    "N": [(14.00307400443, 0.99636), (15.00010889888, 0.00364)],
    "O": [(15.99491461957, 0.99757), (16.99913175650, 0.00038), (17.99915961286, 0.00205)],
}
PESO = {"He": 4.002602, "Mg": 24.305, "Si": 28.085, "Ca": 40.078, "Fe": 55.845}  # pesos estandar NIST

def masa(el):
    if el in ISO:
        tot = sum(w for _, w in ISO[el])
        return sum(m * w for m, w in ISO[el]) / tot
    return PESO[el]

# ---- mezcla ILUSTRATIVA (log eps; H = 12 por definicion) ----
LOGEPS = {"H": 12.00, "He": 10.90, "C": 8.40, "N": 7.80, "O": 8.70, "Mg": 7.55, "Si": 7.50, "Fe": 7.50}

def numero(logeps):
    return {el: 10 ** (v - 12.0) for el, v in logeps.items()}   # N_i / N_H

def masas(logeps):
    n = numero(logeps)
    w = {el: n[el] * masa(el) for el in n}
    s = sum(w.values())
    return {el: w[el] / s for el in w}

def logeps_desde_masas(frac):
    n_rel = {el: frac[el] / masa(el) for el in frac}
    return {el: 12.0 + math.log10(n_rel[el] / n_rel["H"]) for el in frac}

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Masas atomicas usadas [u]: " + ", ".join(f"{e} {masa(e):.5f}" for e in LOGEPS))
    n = numero(LOGEPS)
    suma_n = sum(n.values())
    f_num = {e: n[e] / suma_n for e in n}
    X = masas(LOGEPS)
    print("A. Mezcla ILUSTRATIVA: log eps, fraccion en numero y fraccion en masa")
    print("elem   log_eps   N/N_H          frac_numero   frac_masa")
    for e in LOGEPS:
        print(f"{e:>4}   {LOGEPS[e]:6.2f}   {n[e]:.4e}   {f_num[e]:.6e}   {X[e]:.6e}")
    Xh, Yh = X["H"], X["He"]
    Z = 1.0 - Xh - Yh
    print(f"B. X = {Xh:.5f} ; Y = {Yh:.5f} ; Z (suma de los demas) = {Z:.6f} ; Z/X = {Z / Xh:.6f}")
    # numeros de carbono y oxigeno
    co = 10 ** (LOGEPS["C"] - LOGEPS["O"])
    print(f"C. C/O en numero = {co:.4f} ; O/H = {n['O']:.3e} ; (C/O) en masa = {X['C'] / X['O']:.4f}")
    # pruebas
    s_masas = sum(X.values())
    assert abs(s_masas - 1.0) < 1e-12, s_masas
    ida_vuelta = logeps_desde_masas(X)
    err_iv = max(abs(ida_vuelta[e] - LOGEPS[e]) for e in LOGEPS)
    assert err_iv < 1e-10, err_iv
    # segundo camino: Y/X por formula cerrada (n_He/n_H * m_He/m_H)
    yx_cerrada = (n["He"] / n["H"]) * (masa("He") / masa("H"))
    err_yx = abs(Yh / Xh - yx_cerrada)
    assert err_yx < 1e-12, err_yx
    print(f"D. Suma de fracciones en masa = {s_masas:.15f} ; error ida y vuelta = {err_iv:.2e} dex ; Y/X = {Yh / Xh:.6f} (cerrada {yx_cerrada:.6f})")
    # sensibilidad: +0.1 dex de O cambia Z
    L2 = dict(LOGEPS); L2["O"] += 0.10
    X2 = masas(L2)
    print(f"E. Sensibilidad: +0.10 dex en O => Z pasa de {Z:.6f} a {1 - X2['H'] - X2['He']:.6f}")
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
