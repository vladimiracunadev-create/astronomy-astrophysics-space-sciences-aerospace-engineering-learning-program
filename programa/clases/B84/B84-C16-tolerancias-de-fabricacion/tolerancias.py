#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C16: apilamiento de tolerancias (peor caso, RSS y Monte Carlo) y capacidad.

DATOS ILUSTRATIVOS (no consultados): un hueco G = A - (B + C + D + E) entre una caja y cuatro piezas apiladas:
  A = 100,00 +/- 0,10 mm (alojamiento); B = 20,00 +/- 0,05; C = 30,00 +/- 0,05; D = 25,00 +/- 0,08; E = 20,00 +/- 0,05 mm.
  Hueco nominal G = 100 - 95 = 5,00 mm. Requisito ILUSTRATIVO: G >= 4,70 mm (hueco minimo) y <= 5,30 mm.
Modelo: peor caso: tol_G = sum |tol_i| ; RSS: tol_G = sqrt(sum tol_i^2); Monte Carlo (200000 muestras, semilla 84016) con cada dimension normal con
sigma_i = tol_i/3 (el rango de tolerancia = +/- 3 sigma: Cp = 1 por dimension) y, como segunda condicion, sigma_i = tol_i/4 (Cp = 1,33).
Segunda via: la desviacion tipica del hueco de Monte Carlo debe coincidir con la RSS dividida por 3 (resultado exacto para suma de normales independientes)
dentro de 1 %; el indice de capacidad Cpk = min(USL - mu, mu - LSL)/(3 sigma).
Unidades: mm. Tolerancias: |sigma_MC - sigma_RSS/3| / sigma < 1 %.
"""
from __future__ import annotations
import math, platform, random

DIM = {"A": (100.00, 0.10, +1), "B": (20.00, 0.05, -1), "C": (30.00, 0.05, -1), "D": (25.00, 0.08, -1), "E": (20.00, 0.05, -1)}
LSL, USL = 4.70, 5.30


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    nom = sum(s * v for v, t, s in DIM.values())
    wc = sum(t for v, t, s in DIM.values())
    rss = math.sqrt(sum(t * t for v, t, s in DIM.values()))
    print("Cadena ILUSTRATIVA: G = A - (B + C + D + E); requisito 4,70 <= G <= 5,30 mm")
    print(f"Hueco nominal = {nom:.3f} mm")
    print(f"Peor caso: G = {nom:.3f} +/- {wc:.3f}  -> [{nom - wc:.3f}, {nom + wc:.3f}] mm  ({'cumple' if nom - wc >= LSL and nom + wc <= USL else 'NO cumple'} el requisito)")
    print(f"RSS:        G = {nom:.3f} +/- {rss:.4f}  -> [{nom - rss:.4f}, {nom + rss:.4f}] mm  ({'cumple' if nom - rss >= LSL and nom + rss <= USL else 'NO cumple'})")
    print(f"Contribucion de cada dimension a la varianza (RSS):")
    for k, (v, t, s) in DIM.items():
        print(f"  {k}: tol = {t:.2f} mm -> {t * t / (rss * rss) * 100:5.1f} % de la varianza")
    for div, nombre in ((3.0, "Cp = 1,00 (sigma = tol/3)"), (4.0, "Cp = 1,33 (sigma = tol/4)")):
        rng = random.Random(84016)
        n = 200000
        s1 = s2 = 0.0
        fuera = 0
        for _ in range(n):
            g = sum(s * rng.gauss(v, t / div) for v, t, s in DIM.values())
            s1 += g
            s2 += g * g
            if g < LSL or g > USL:
                fuera += 1
        mu = s1 / n
        sd = math.sqrt(s2 / n - mu * mu)
        sd_teo = rss / div
        cpk = min(USL - mu, mu - LSL) / (3 * sd)
        print(f"Monte Carlo {nombre}: media = {mu:.4f} mm, sigma = {sd:.5f} mm (teorica {sd_teo:.5f}), Cpk = {cpk:.3f}, fuera de requisito = {fuera} de {n} ({fuera / n * 100:.4f} %)")
        assert abs(sd - sd_teo) / sd_teo < 0.01
    # Efecto de ajustar la dimension D a +/- 0,04
    DIM["D"] = (25.00, 0.04, -1)
    rss2 = math.sqrt(sum(t * t for v, t, s in DIM.values()))
    print(f"Si D se mecaniza a +/- 0,04 mm: RSS = {rss2:.4f} mm (antes {rss:.4f}); peor caso = {sum(t for v, t, s in DIM.values()):.3f} mm")
    assert abs(rss - math.sqrt(0.10 ** 2 + 0.05 ** 2 * 3 + 0.08 ** 2)) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
