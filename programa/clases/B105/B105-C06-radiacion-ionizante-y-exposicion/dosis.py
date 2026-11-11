#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C06: dosis absorbida, equivalente y efectiva; presupuesto de dosis de una mision SINTETICA.

Relaciones: H_T = w_R D_T (Sv = factor x Gy); E = sum_T w_T H_T. Los factores de ponderacion de tejido son los de ICRP 103 (2007) tal como los
recuerda el autor: pulmon, estomago, colon, medula roja, mama 0.12 c/u; gonadas 0.08; vejiga, esofago, higado, tiroides 0.04 c/u; superficie osea,
cerebro, glandulas salivales, piel 0.01 c/u; resto 0.12. NO se consultaron en la fuente (solo se consulto la pagina de la Publicacion 103, sin la tabla);
el laboratorio verifica que suman 1.
Limites consultados por busqueda (resumen NASA, 2026-11-10; el estandar NASA-STD-3001 no se abrio): limite de carrera 600 mSv de dosis efectiva;
limite de evento de particulas solares (SPE) 250 mSv.
Todo lo demas es SINTETICO/ILUSTRATIVO: tasa de dosis absorbida 0.30 mGy/dia con factor de calidad medio Q = 2.5 (-> 0.75 mSv/dia), mision de
180 dias, incertidumbre lognormal de Q con sigma 0.30 (poblacion de 20000 realizaciones, semilla 105). Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

W_T = {"pulmon": 0.12, "estomago": 0.12, "colon": 0.12, "medula roja": 0.12, "mama": 0.12, "gonadas": 0.08, "vejiga": 0.04, "esofago": 0.04,
       "higado": 0.04, "tiroides": 0.04, "superficie osea": 0.01, "cerebro": 0.01, "g. salivales": 0.01, "piel": 0.01, "resto": 0.12}
LIM_CARRERA, LIM_SPE = 600.0, 250.0  # mSv


def dosis_efectiva(h_t):
    return sum(W_T[k] * h_t[k] for k in W_T)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS/ILUSTRATIVOS: tasa 0.30 mGy/dia, Q = 2.5, mision 180 d; limites 600 y 250 mSv de un resumen NASA (2026-11-10); pesos w_T no consultados")
    print(f"Suma de los w_T = {sum(W_T.values()):.2f} (debe ser 1.00)")
    d_dia, q, dias = 0.30, 2.5, 180
    h_dia = d_dia * q
    h_mision = h_dia * dias
    print(f"Dosis equivalente de referencia: {h_dia:.2f} mSv/dia; en {dias} dias = {h_mision:.0f} mSv")
    rng = np.random.default_rng(105)
    f_t = {k: rng.uniform(0.8, 1.2) for k in W_T}
    h_t = {k: h_mision * f_t[k] for k in W_T}
    e = dosis_efectiva(h_t)
    print(f"Dosis efectiva con dosis de organo variables entre 0.8 y 1.2 de la de referencia: E = {e:.1f} mSv (uniforme = {h_mision:.1f} mSv)")
    print(f"Fraccion del limite de carrera de 600 mSv = {100 * h_mision / LIM_CARRERA:.1f} %; misiones de {dias} d hasta el limite = {LIM_CARRERA / h_mision:.2f}")
    print(f"Dias hasta {LIM_CARRERA:.0f} mSv = {LIM_CARRERA / h_dia:.0f}; fraccion de 250 mSv de un SPE sobre el limite de carrera = {100 * LIM_SPE / LIM_CARRERA:.1f} %")
    qs = 2.5 * np.exp(rng.normal(-0.5 * 0.30 ** 2, 0.30, 20000))
    h = d_dia * qs * dias
    print(f"Incertidumbre de Q lognormal (sigma 0.30): mision {h.mean():.0f} mSv (p5-p95: {np.percentile(h, 5):.0f}-{np.percentile(h, 95):.0f}); P(>{LIM_CARRERA:.0f} mSv en una mision) = {np.mean(h > LIM_CARRERA):.4f}")
    for n in (1, 2, 3, 4):
        print(f"  {n} mision(es) de {dias} d: media {n * h.mean():5.0f} mSv; P(superar 600 mSv) = {np.mean(n * h > LIM_CARRERA):.4f}")
    assert abs(sum(W_T.values()) - 1.0) < 1e-12
    assert abs(h_mision - 135.0) < 1e-9
    assert 0.8 * h_mision < e < 1.2 * h_mision
    assert abs(h.mean() - 135) < 3
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
