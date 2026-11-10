#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B63-C02: masa de un testigo y estrategia de muestreo para cubrir litologias.

Datos: SINTETICOS e ILUSTRATIVOS. Diametro del testigo 13 mm, longitud 60 mm, densidad 2.7 g/cm3 y las
fracciones de area de las litologias son valores propuestos para el ejemplo; no proceden de ninguna mision.
Modelo: (1) masa m = rho * pi * (d/2)^2 * L; (2) probabilidad de capturar al menos una vez una litologia de
fraccion de area p con N muestras independientes, P = 1 - (1 - p)^N, y N minimo para una confianza C;
(3) numero esperado de litologias distintas capturadas con N muestras (coleccionista de cupones generalizado)
contrastado con Monte Carlo (semilla fija).
Sistema de referencia: terreno plano dividido en unidades discretas; muestras independientes y con
reemplazo (aproximacion: ignora el desgaste del punto de muestreo y la accesibilidad).
Tolerancias: masa < 1e-12 relativo; P de Monte Carlo dentro de 0.01 absoluto; esperado dentro de 0.02.
Versiones: se imprimen al ejecutar (solo biblioteca estandar).
"""
from __future__ import annotations
import math, platform, random

D_MM, L_MM, RHO = 13.0, 60.0, 2.7      # mm, mm, g/cm3 (ilustrativos)
FRAC = {"basalto": 0.55, "brecha": 0.25, "evaporita": 0.15, "veta": 0.05}   # sinteticas, suman 1


def masa_testigo_g(d_mm: float = D_MM, l_mm: float = L_MM, rho: float = RHO) -> float:
    vol_cm3 = math.pi * (d_mm / 20.0) ** 2 * (l_mm / 10.0)
    return rho * vol_cm3


def p_captura(p: float, n: int) -> float:
    return 1.0 - (1.0 - p) ** n


def n_minimo(p: float, confianza: float) -> int:
    return math.ceil(math.log(1.0 - confianza) / math.log(1.0 - p))


def esperado_distintas(fr: dict, n: int) -> float:
    return sum(p_captura(p, n) for p in fr.values())


def simula(fr: dict, n: int, rep: int = 40000, semilla: int = 63):
    rng = random.Random(semilla)
    nombres, pesos = list(fr), list(fr.values())
    cuenta = {k: 0 for k in nombres}
    tot = 0
    for _ in range(rep):
        vistos = set(rng.choices(nombres, weights=pesos, k=n))
        tot += len(vistos)
        for v in vistos:
            cuenta[v] += 1
    return {k: cuenta[k] / rep for k in nombres}, tot / rep


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    m = masa_testigo_g()
    print(f"Testigo ilustrativo {D_MM} x {L_MM} mm, rho = {RHO} g/cm3: masa = {m:.3f} g")
    assert abs(m - 2.7 * math.pi * 0.65 ** 2 * 6.0) < 1e-12
    print("Litologias sinteticas (fraccion de area):", FRAC)
    print(" litologia   p     N(90%)  N(95%)  N(99%)")
    for k, p in FRAC.items():
        print(f" {k:10s} {p:5.2f} {n_minimo(p, 0.90):6d} {n_minimo(p, 0.95):7d} {n_minimo(p, 0.99):7d}")
    # prueba analitica: con N_min la confianza se alcanza y con N_min - 1 no
    for p in FRAC.values():
        n = n_minimo(p, 0.95)
        assert p_captura(p, n) >= 0.95 > p_captura(p, n - 1)
    print("Umbral de N minimo comprobado para 95 %.")
    n = 10
    sim, medio = simula(FRAC, n)
    print(f"Con N = {n} muestras: P de captura analitica / Monte Carlo")
    peor = 0.0
    for k, p in FRAC.items():
        a = p_captura(p, n)
        peor = max(peor, abs(a - sim[k]))
        print(f"  {k:10s} {a:.4f}  {sim[k]:.4f}")
    esp = esperado_distintas(FRAC, n)
    print(f"Litologias distintas esperadas: analitico {esp:.4f}, Monte Carlo {medio:.4f}")
    assert peor < 0.01 and abs(esp - medio) < 0.02, (peor, esp, medio)
    print(f"Diferencia maxima de P = {peor:.4f} (< 0.01). Pruebas superadas.")


if __name__ == "__main__":
    main()
