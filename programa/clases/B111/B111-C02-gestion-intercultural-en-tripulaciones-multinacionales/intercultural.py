#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B111-C02: diversidad, endogrupo y riesgo de malentendido en una tripulacion SINTETICA.

TODO es SINTETICO: seis miembros ficticios (M1..M6) de tres grupos ficticios (G1, G2, G3), con cuatro puntuaciones de
orientacion de trabajo ficticias (escala 0-100) y una proficiencia de idioma ficticia (probabilidad de entender bien
un elemento critico de un mensaje). No son datos de Hofstede ni de ningun pais; no describen a nadie.
Calculos: (a) indice de diversidad de Blau 1 - sum(p_g^2); (b) distancia euclidiana normalizada entre perfiles;
(c) indice de endogrupo: fraccion observada de interacciones dentro del grupo frente a la esperada con mezcla al azar
sum(p_g^2) (observada sintetica = 0.62); (d) probabilidad de un error no detectado en un mensaje de n elementos con
repeticion de lectura (readback): cada elemento se entiende mal con prob 1-p, y la repeticion lo detecta con prob d.
P_no_detectado = 1 - (1 - (1-p)(1-d))^n. Segunda via: Monte Carlo (semilla 112, 200000 mensajes) con tolerancia 0.005.
Supuestos: elementos independientes, deteccion independiente por elemento, sin ruido de canal.
"""
from __future__ import annotations
import math, platform, random

MIEMBROS = {  # grupo, perfil de 4 dimensiones (SINTETICO), proficiencia p
    "M1": ("G1", (80, 30, 55, 60), 0.99),
    "M2": ("G1", (75, 35, 50, 65), 0.98),
    "M3": ("G2", (35, 70, 60, 40), 0.93),
    "M4": ("G2", (30, 75, 65, 45), 0.90),
    "M5": ("G3", (55, 50, 20, 85), 0.85),
    "M6": ("G3", (50, 55, 25, 80), 0.88),
}


def blau(grupos):
    n = len(grupos)
    return 1.0 - sum((grupos.count(g) / n) ** 2 for g in set(grupos))


def distancia(p, q):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p, q))) / (100.0 * math.sqrt(len(p)))


def p_no_detectado(p, d, n):
    return 1.0 - (1.0 - (1.0 - p) * (1.0 - d)) ** n


def montecarlo(p, d, n, rng, m=200000):
    c = 0
    for _ in range(m):
        for _ in range(n):
            if rng.random() > p and rng.random() > d:
                c += 1
                break
    return c / m


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    grupos = [v[0] for v in MIEMBROS.values()]
    esperado = sum((grupos.count(g) / len(grupos)) ** 2 for g in set(grupos))
    print(f"Tripulacion SINTETICA de {len(MIEMBROS)} miembros en {len(set(grupos))} grupos ficticios")
    print(f"Indice de diversidad de Blau = {blau(grupos):.4f}")
    print("Distancia normalizada entre perfiles (0 = igual, 1 = maxima):")
    nombres = list(MIEMBROS)
    print("      " + " ".join(f"{n:>6s}" for n in nombres))
    dmax, dmin_inter = 0.0, 9.0
    for a in nombres:
        fila = []
        for b in nombres:
            dd = distancia(MIEMBROS[a][1], MIEMBROS[b][1])
            fila.append(dd)
            if a != b and MIEMBROS[a][0] != MIEMBROS[b][0]:
                dmin_inter = min(dmin_inter, dd)
            dmax = max(dmax, dd)
        print(f"{a:>5s} " + " ".join(f"{x:6.3f}" for x in fila))
    print(f"Distancia maxima = {dmax:.3f}")
    obs = 0.62
    print(f"Endogrupo: esperado con mezcla al azar = {esperado:.4f} ; observado SINTETICO = {obs:.2f} ; razon = {obs / esperado:.3f}")
    rng = random.Random(112)
    print("Malentendido no detectado (n = 5 elementos criticos, deteccion por repeticion d):")
    print("  miembro   p     d     P analitica   P Monte Carlo   diferencia")
    dif_max = 0.0
    for nom in ("M1", "M4", "M5"):
        p = MIEMBROS[nom][2]
        for d in (0.0, 0.8):
            pa = p_no_detectado(p, d, 5)
            pm = montecarlo(p, d, 5, rng)
            dif_max = max(dif_max, abs(pa - pm))
            print(f"  {nom:>6s}  {p:.2f}  {d:.1f}  {pa:12.5f}  {pm:14.5f}  {abs(pa - pm):10.5f}")
    print(f"Diferencia maxima analitica/Monte Carlo = {dif_max:.5f}")
    assert abs(blau(grupos) - (1 - 3 * (1 / 3) ** 2)) < 1e-12
    assert dif_max < 0.005
    assert p_no_detectado(0.9, 0.8, 5) < p_no_detectado(0.9, 0.0, 5)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
