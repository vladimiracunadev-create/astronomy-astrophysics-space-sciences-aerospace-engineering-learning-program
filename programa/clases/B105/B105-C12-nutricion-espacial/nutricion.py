#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B105-C12: balance energetico y masa de provisiones de una tripulacion SINTETICA (modelo didactico).

Metabolismo basal: ecuacion de Mifflin-St Jeor (kcal/dia) = 10 w + 6.25 h - 5 a + 5 (hombre) o - 161 (mujer), con w en kg, h en cm, a en anios
(coeficientes recordados por el autor; NO consultados en la fuente aqui). Gasto total = BMR x PAL; PAL (nivel de actividad) 1.6 (ILUSTRATIVO).
Atwater: 4 kcal/g proteina y carbohidrato, 9 kcal/g grasa. Reparto energetico 15/30/55 % (proteina/grasa/carbohidrato), ilustrativo.
Agua: regla de 1 mL por kcal (ILUSTRATIVA, no una norma). Masa de alimento: energia / densidad energetica (4 kcal/g de alimento en base seca, ilustrativa)
por un factor de empaque 1.3 (ilustrativo). Cambio de masa corporal: 7700 kcal por kg (aproximacion didactica). Tripulacion SINTETICA de 4, mision de 180 dias,
semilla 105. Ninguna cifra es una especificacion de ninguna agencia. Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

KCAL_G = {"proteina": 4.0, "grasa": 9.0, "carbohidrato": 4.0}
REPARTO = {"proteina": 0.15, "grasa": 0.30, "carbohidrato": 0.55}


def bmr(w, h, a, hombre):
    return 10 * w + 6.25 * h - 5 * a + (5 if hombre else -161)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS SINTETICOS/ILUSTRATIVOS (semilla 105): tripulacion de 4; ecuacion y factores no consultados en una fuente")
    tripu = [(75, 178, 40, True), (68, 172, 38, True), (62, 165, 35, False), (58, 160, 42, False)]
    pal = 1.6
    total = 0.0
    print("tripulante | BMR [kcal/d] | gasto total [kcal/d]")
    for i, (w, h, a, m) in enumerate(tripu, 1):
        b = bmr(w, h, a, m)
        print(f"   {i}       |   {b:7.1f}   |   {b * pal:7.1f}")
        total += b * pal
    print(f"Energia diaria de la tripulacion = {total:.0f} kcal; media {total / 4:.0f} kcal/persona")
    e1 = bmr(*tripu[0]) * pal
    print("Reparto del tripulante 1 (gramos/dia): " + ", ".join(f"{k} {e1 * REPARTO[k] / KCAL_G[k]:.1f}" for k in REPARTO))
    check = sum(e1 * REPARTO[k] for k in REPARTO)
    print(f"  suma de energia por macronutrientes = {check:.1f} kcal (debe igualar {e1:.1f})")
    print(f"Agua con la regla de 1 mL/kcal para la tripulacion = {total / 1000:.2f} L/dia")
    dias = 180
    kcal_mision = total * dias
    masa_alim = kcal_mision / 4.0 / 1000 * 1.3
    print(f"Mision de {dias} dias: {kcal_mision / 1e6:.3f} Mkcal; masa de alimento con empaque = {masa_alim:.0f} kg ({masa_alim / 4 / dias * 1000:.0f} g por persona y dia)")
    rng = np.random.default_rng(105)
    pals = rng.normal(1.6, 0.15, 20000).clip(1.2, None)
    base = sum(bmr(*t) for t in tripu)
    masa = base * pals * dias / 4.0 / 1000 * 1.3
    print(f"Con PAL ~ N(1.6, 0.15): masa de alimento media {masa.mean():.0f} kg, p5-p95 = {np.percentile(masa, 5):.0f}-{np.percentile(masa, 95):.0f} kg; margen para cubrir el p95 = {np.percentile(masa, 95) - masa_alim:.0f} kg")
    for ingesta in (1.0, 0.9, 0.8):
        deficit = (1 - ingesta) * e1
        dm = deficit * dias / 7700
        print(f"Ingesta del {100 * ingesta:.0f} % del gasto del tripulante 1: deficit {deficit:.0f} kcal/d; cambio de masa en {dias} d = -{dm:.1f} kg ({100 * dm / tripu[0][0]:.1f} % de su masa)")
    assert abs(bmr(75, 178, 40, True) - 1667.5) < 1e-9
    assert abs(check - e1) < 1e-9
    assert abs(sum(REPARTO.values()) - 1) < 1e-12
    assert abs(masa.mean() - masa_alim) / masa_alim < 0.02
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
