#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B13-C14: repetibilidad y reproducibilidad (ANOVA de un factor).

Datos: SINTETICOS. p estaciones miden el mismo desfase de reloj (valor
verdadero 12.00 ns) n veces cada una. Cada estacion tiene un sesgo propio
(componente entre estaciones, desviacion sigma_L = 0.40 ns) y un ruido de
repeticion sigma_r = 0.30 ns. Semilla fija.
Modelo: x_ij = mu + L_i + e_ij, L_i ~ N(0, sigma_L^2), e_ij ~ N(0, sigma_r^2).
Estimadores (diseno equilibrado):
  MSW = SSW/(p(n-1)) estima sigma_r^2 (repetibilidad);
  MSB = n SS_medias/(p-1) estima sigma_r^2 + n sigma_L^2;
  s_L^2 = max(0, (MSB - MSW)/n);  s_R^2 = s_r^2 + s_L^2 (reproducibilidad).
Identidad exacta: SS_total = SSB + SSW.
Supuestos: normalidad, independencia, diseno equilibrado.
Tolerancia: identidad 1e-9; con p = 400 estaciones los estimadores recuperan
los valores verdaderos dentro del 10 %.
"""
from __future__ import annotations
import math
import platform
import random
import sys

MU, SL, SR = 12.00, 0.40, 0.30


def anova(datos):
    p, n = len(datos), len(datos[0])
    medias = [sum(g) / n for g in datos]
    gm = sum(medias) / p
    ssw = sum((v - m) ** 2 for g, m in zip(datos, medias) for v in g)
    ssb = n * sum((m - gm) ** 2 for m in medias)
    sst = sum((v - gm) ** 2 for g in datos for v in g)
    msw = ssw / (p * (n - 1))
    msb = ssb / (p - 1)
    sr2 = msw
    sl2 = max(0.0, (msb - msw) / n)
    return dict(ssw=ssw, ssb=ssb, sst=sst, sr=math.sqrt(sr2), sl=math.sqrt(sl2), sR=math.sqrt(sr2 + sl2), gm=gm)


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(14)
    # Estudio pequeno: 8 estaciones x 5 medidas
    p, n = 8, 5
    datos = []
    for _ in range(p):
        li = rng.gauss(0, SL)
        datos.append([MU + li + rng.gauss(0, SR) for _ in range(n)])
    a = anova(datos)
    assert abs(a["sst"] - a["ssb"] - a["ssw"]) < 1e-9
    print(f"8x5: s_r = {a['sr']:.3f} ns ; s_L = {a['sl']:.3f} ns ; s_R = {a['sR']:.3f} ns ; media = {a['gm']:.3f} ns")
    # Estudio grande para comprobar los estimadores
    p, n = 400, 5
    datos = []
    for _ in range(p):
        li = rng.gauss(0, SL)
        datos.append([MU + li + rng.gauss(0, SR) for _ in range(n)])
    b = anova(datos)
    sR_teor = math.hypot(SR, SL)
    print(f"400x5: s_r = {b['sr']:.3f} (verd {SR}) ; s_L = {b['sl']:.3f} (verd {SL}) ; s_R = {b['sR']:.3f} (verd {sR_teor:.3f})")
    assert abs(b["sr"] - SR) / SR < 0.10 and abs(b["sl"] - SL) / SL < 0.10 and abs(b["sR"] - sR_teor) / sR_teor < 0.10
    # Caso determinista: grupos sin ruido, medias 11, 12, 13 -> s_r = 0 y s_L = sqrt(1) = 1
    det = [[11.0] * 4, [12.0] * 4, [13.0] * 4]
    d = anova(det)
    print(f"determinista: s_r = {d['sr']:.3f} ; s_L = {d['sl']:.3f}")
    assert d["sr"] == 0.0 and abs(d["sl"] - 1.0) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("FALLO:", e)
        sys.exit(1)
