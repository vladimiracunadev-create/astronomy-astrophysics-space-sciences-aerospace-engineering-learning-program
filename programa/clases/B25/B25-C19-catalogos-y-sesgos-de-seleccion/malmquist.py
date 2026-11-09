#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B25-C19: sesgo de Malmquist en un catalogo limitado por flujo y correccion con 1/Vmax.

Datos: ninguno observado. Poblacion SINTETICA: galaxias con densidad numerica uniforme y magnitudes absolutas
M ~ Normal(M0 = -20,0; sigma = 1,0) (valores ILUSTRATIVOS), observadas hasta una magnitud aparente limite
m_lim = 17,0. Semilla fija (random.Random).
Modelo: m = M + 5 log10(d/10 pc); se detecta si m <= m_lim. La fraccion detectada a la distancia d es
Phi(a) con a = (M_lim(d) - M0)/sigma, M_lim(d) = m_lim - 5 log10(d/10 pc); la magnitud media de las detectadas
a esa distancia es M0 - sigma phi(a)/Phi(a) (normal truncada, phi y Phi: densidad y distribucion normal).
Estimador 1/Vmax: cada galaxia pesa 1/Vmax con Vmax = (4pi/3) d_max^3 y d_max = 10 pc * 10^((m_lim - M)/5)
(sin limite superior de volumen).
Supuestos: sin extincion, sin correccion K, sin evolucion, cielo completo, completitud ideal.
Validez: demostracion del sesgo y de su correccion en un caso sin ruido.
Tolerancias: 4 sigma (cascarones) y 3 sigma (1/Vmax) estadisticas de la muestra Monte Carlo.
"""
from __future__ import annotations
import math
import platform
import random
import sys

M0, SIG, M_LIM = -20.0, 1.0, 17.0


def phi(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2 * math.pi)


def Phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def m_lim_abs(d_mpc):
    return M_LIM - 5 * math.log10(d_mpc * 1e6 / 10.0)


def media_teorica(d_mpc):
    a = (m_lim_abs(d_mpc) - M0) / SIG
    return M0 - SIG * phi(a) / Phi(a), Phi(a)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(25)
    dmax_sim = 800.0  # Mpc: esfera de simulacion
    n = 400000
    muestras = []
    for _ in range(n):
        d = dmax_sim * rng.random() ** (1 / 3)
        M = rng.gauss(M0, SIG)
        m = M + 5 * math.log10(d * 1e6 / 10.0)
        if m <= M_LIM:
            muestras.append((d, M))
    # Prueba 1: en tres cascarones de distancia, media y fraccion detectada frente a la teoria
    print("cascaron (Mpc) | N detectadas | <M> MC | <M> teoria | fraccion detectada MC | teoria")
    for lo, hi in ((90.0, 110.0), (190.0, 210.0), (290.0, 310.0)):
        sel = [M for d, M in muestras if lo <= d < hi]
        d_c = 0.5 * (lo + hi)
        mt, ft = media_teorica(d_c)
        media = sum(sel) / len(sel)
        err = SIG / math.sqrt(len(sel))
        # fraccion detectada MC: detectadas / esperadas en el cascaron (volumen)
        esperadas = n * (hi ** 3 - lo ** 3) / dmax_sim ** 3
        f_mc = len(sel) / esperadas
        print(f"  {lo:5.0f}-{hi:5.0f}    {len(sel):9d}   {media:7.3f}   {mt:7.3f}      {f_mc:7.3f}          {ft:7.3f}")
        assert abs(media - mt) < 4 * err + 0.01, "magnitud media del cascaron"
        assert abs(f_mc / ft - 1) < 0.08, "fraccion detectada"
    # Prueba 2: 1/Vmax recupera la magnitud media de la poblacion para M tan debil como -17 (completa)
    tot_w = sum_w = 0.0
    dmax_total = lambda M: 10e-6 * 10 ** ((M_LIM - M) / 5)  # en Mpc
    vmax = lambda M: min(dmax_total(M), dmax_sim) ** 3
    muestras_ok = [(d, M) for d, M in muestras if M < M0 + 2 * SIG]  # galaxias lo bastante brillantes para ser completas
    for d, M in muestras_ok:
        w = 1.0 / vmax(M)
        tot_w += w
        sum_w += w * M
    m_pesada = sum_w / tot_w
    m_sin_peso = sum(M for d, M in muestras_ok) / len(muestras_ok)
    # media teorica de la poblacion truncada a M < M0 + 2 sigma
    b = 2.0
    media_trunc = M0 - SIG * (phi(b) - 0.0) / (Phi(b))  # normal truncada por arriba: M0 - sigma phi(b)/Phi(b)
    var_w = sum((1.0 / vmax(M)) ** 2 * (M - m_pesada) ** 2 for d, M in muestras_ok) / tot_w ** 2
    sig_w = math.sqrt(var_w)
    print(f"media poblacional (M < M0 + 2 sigma) = {media_trunc:.3f} ; sin pesos = {m_sin_peso:.3f} ; con 1/Vmax = {m_pesada:.3f} +- {sig_w:.3f}")
    assert abs(m_pesada - media_trunc) < 3 * sig_w, "1/Vmax"
    assert abs(m_sin_peso - media_trunc) > 0.05, "el sesgo sin pesos debe verse"
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
