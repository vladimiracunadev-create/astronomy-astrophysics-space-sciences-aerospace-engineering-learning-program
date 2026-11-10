#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C37: compuestos y aglomerantes con regolito: relacion resistencia-porosidad de Ryshkewitch, cotas de rigidez y masa de ligante.

DATOS SINTETICOS (generados aqui con semilla 84037, NO medidos): 24 resistencias a compresion de ladrillos de un compuesto de regolito simulado con porosidad P entre 0,05 y 0,45,
sigma = sigma0 exp(-b P) con sigma0 = 110 MPa y b = 5,8 (verdaderos) y ruido lognormal de 8 %.
DATOS ILUSTRATIVOS (no consultados): fase de regolito E_f = 60 GPa y ligante E_m = 5 GPa con fraccion de regolito V_f = 0,60; densidad de particula del regolito 3100 kg/m3,
densidad del ligante 2000 kg/m3; ladrillo de 0,20 x 0,10 x 0,05 m con fraccion volumetrica de ligante 0,30 y porosidad residual 0,10.
Ajuste: regresion lineal de ln sigma frente a P (minimos cuadrados) -> b y sigma0 con errores tipicos; intervalo de prediccion al 95 % con t = 2,074 (22 g.l.; valor de tablas recordado, no consultado).
Cotas de rigidez: Voigt (iso-deformacion) E_V = V_f E_f + (1 - V_f) E_m y Reuss (iso-tension) E_R = 1/(V_f/E_f + (1 - V_f)/E_m). Segunda via: el ajuste debe recuperar el valor verdadero
dentro de 3 errores tipicos; E_R <= E_V.
"""
from __future__ import annotations
import math, platform, random

SIG0, B = 110.0, 5.8


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(84037)
    P = [0.05 + 0.40 * i / 23 for i in range(24)]
    S = [SIG0 * math.exp(-B * p) * math.exp(0.08 * rng.gauss(0, 1)) for p in P]
    print("24 resistencias SINTETICAS: sigma0 = 110 MPa, b = 5,8 (verdaderos), ruido lognormal de 8 %")
    y = [math.log(s) for s in S]
    n = len(P)
    mx, my = sum(P) / n, sum(y) / n
    sxx = sum((p - mx) ** 2 for p in P)
    sxy = sum((p - mx) * (v - my) for p, v in zip(P, y))
    pend = sxy / sxx
    ic = my - pend * mx
    res = [v - (ic + pend * p) for p, v in zip(P, y)]
    s2 = sum(r * r for r in res) / (n - 2)
    se_pend = math.sqrt(s2 / sxx)
    se_ic = math.sqrt(s2 * (1 / n + mx ** 2 / sxx))
    r2 = 1 - sum(r * r for r in res) / sum((v - my) ** 2 for v in y)
    b_aj, s0_aj = -pend, math.exp(ic)
    print(f"Ajuste de Ryshkewitch: b = {b_aj:.3f} +/- {se_pend:.3f} ; sigma0 = {s0_aj:.2f} MPa (ln sigma0 = {ic:.4f} +/- {se_ic:.4f}) ; R2 = {r2:.4f} ; desviacion residual en ln = {math.sqrt(s2):.4f}")
    assert abs(b_aj - B) < 3 * se_pend and abs(ic - math.log(SIG0)) < 3 * se_ic
    print("Prediccion (media y intervalo de prediccion al 95 %) segun la porosidad:")
    for p in (0.10, 0.20, 0.25, 0.35, 0.45):
        m = ic + pend * p
        se = math.sqrt(s2 * (1 + 1 / n + (p - mx) ** 2 / sxx))
        print(f"  P = {p:.2f}: sigma = {math.exp(m):7.2f} MPa  [{math.exp(m - 2.074 * se):7.2f}, {math.exp(m + 2.074 * se):7.2f}]  (verdadera {SIG0 * math.exp(-B * p):7.2f})")
    ef, em, vf = 60.0, 5.0, 0.60
    ev = vf * ef + (1 - vf) * em
    er = 1 / (vf / ef + (1 - vf) / em)
    print(f"Cotas de rigidez con V_f = {vf}: Voigt = {ev:.2f} GPa ; Reuss = {er:.2f} GPa ; la rigidez real esta entre ambas (E_R <= E <= E_V)")
    assert er <= ev
    print("Rigidez frente a la fraccion de regolito (Voigt / Reuss, GPa):")
    for v in (0.3, 0.5, 0.6, 0.7, 0.8):
        print(f"  V_f = {v:.1f}: Voigt = {v * ef + (1 - v) * em:6.2f} ; Reuss = {1 / (v / ef + (1 - v) / em):6.2f}")
    vol = 0.20 * 0.10 * 0.05
    m_lig = 0.30 * vol * 2000.0
    # fraccion de volumen del regolito = 1 - ligante - porosidad
    v_reg = 1 - 0.30 - 0.10
    m_reg = v_reg * vol * 3100.0
    print(f"Ladrillo de {vol * 1e3:.1f} L: regolito = {m_reg:.3f} kg ; ligante = {m_lig:.3f} kg ; masa total = {m_reg + m_lig:.3f} kg ; ligante = {m_lig / (m_reg + m_lig) * 100:.1f} % de la masa")
    print(f"Para 1000 ladrillos: ligante a transportar desde la Tierra (si no hay ligante in situ) = {1000 * m_lig:.0f} kg ; regolito local = {1000 * m_reg:.0f} kg")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
