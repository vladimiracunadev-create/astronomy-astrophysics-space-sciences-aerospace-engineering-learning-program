#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B26-C21: combinacion de restricciones gaussianas sobre Omega_m y prueba de consistencia.

Datos (valores PUBLICADOS en resumenes, consultados 2026-11-09): Planck 2018 Omega_m = 0.315 +/- 0.007
(arXiv:1807.06209, LCDM base); Pantheon+ Omega_m = 0.334 +/- 0.018 (SNe solas, LCDM plano, arXiv:2202.04077);
DESI 2024 BAO Omega_m = 0.295 +/- 0.015 (arXiv:2404.03002). Se usan como si fueran medidas independientes y
gaussianas: es un EJERCICIO de tecnica (no una combinacion publicada); no son independientes ni estan
obtenidas bajo exactamente las mismas hipotesis. El caso con correlacion rho es SINTETICO.
Modelo: L(Om) = prod N(Om; mu_i, s_i). Media ponderada mu = sum(mu_i/s_i^2)/sum(1/s_i^2), s = 1/sqrt(sum 1/s_i^2);
chi^2_min = sum (mu_i - mu)^2/s_i^2 con n-1 grados de libertad. Con correlacion: s^2 = 1/(1^T C^-1 1).
Supuestos: gaussianidad, independencia (salvo el ejemplo con rho). Validez: ilustrativa.
Tolerancia: 1e-4 entre la rejilla y la forma cerrada; 1e-12 en los casos exactos.
"""
from __future__ import annotations
import math
import platform
import sys

MED = [("Planck 2018", 0.315, 0.007), ("Pantheon+ (SNe)", 0.334, 0.018), ("DESI 2024 (BAO)", 0.295, 0.015)]


def combina(med):
    w = [1 / s ** 2 for _, _, s in med]
    mu = sum(wi * m for wi, (_, m, _) in zip(w, med)) / sum(w)
    return mu, 1 / math.sqrt(sum(w))


def chi2(med, mu):
    return sum(((m - mu) / s) ** 2 for _, m, s in med)


def rejilla(med, lo=0.2, hi=0.45, n=50000):
    best, bx = -1e300, None
    for i in range(n + 1):
        x = lo + (hi - lo) * i / n
        lnl = -0.5 * chi2(med, x)
        if lnl > best:
            best, bx = lnl, x
    # anchura por Delta chi2 = 1 alrededor del optimo
    c0 = chi2(med, bx)
    dentro = [lo + (hi - lo) * i / n for i in range(n + 1) if chi2(med, lo + (hi - lo) * i / n) <= c0 + 1]
    return bx, 0.5 * (max(dentro) - min(dentro))


def sigma_correlada(s1, s2, rho):
    c = [[s1 * s1, rho * s1 * s2], [rho * s1 * s2, s2 * s2]]
    det = c[0][0] * c[1][1] - c[0][1] ** 2
    inv = [[c[1][1] / det, -c[0][1] / det], [-c[1][0] / det, c[0][0] / det]]
    return 1 / math.sqrt(sum(inv[i][j] for i in range(2) for j in range(2)))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    mu, s = combina(MED)
    bx, bs = rejilla(MED)
    assert abs(bx - mu) < 1e-4 and abs(bs / s - 1) < 1e-2, "rejilla != forma cerrada"
    c2 = chi2(MED, mu)
    dof = len(MED) - 1
    p = math.exp(-c2 / 2)             # supervivencia de chi^2 con 2 grados de libertad (exacta)
    print(f"combinado: Omega_m = {mu:.4f} +/- {s:.4f} (rejilla: {bx:.4f} +/- {bs:.4f})")
    print(f"chi2_min = {c2:.2f} para {dof} grados de libertad ; p = {p:.3f}")
    for i in range(3):
        for j in range(i + 1, 3):
            (n1, m1, s1), (n2, m2, s2) = MED[i], MED[j]
            print(f"  {n1} vs {n2}: diferencia = {abs(m1 - m2):.3f} ; {abs(m1 - m2) / math.hypot(s1, s2):.2f} sigma")
    assert abs(sigma_correlada(0.018, 0.015, 0.0) - 1 / math.sqrt(1 / 0.018 ** 2 + 1 / 0.015 ** 2)) < 1e-12
    for rho in (0.0, 0.5, 0.9):
        print(f"  Pantheon+ y DESI con correlacion {rho}: sigma combinada = {sigma_correlada(0.018, 0.015, rho):.5f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
