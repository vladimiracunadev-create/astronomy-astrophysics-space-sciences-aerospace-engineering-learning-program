#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B63-C06: marco bayesiano de decision liberar/retener (modelo didactico, no el protocolo oficial).

Datos: SINTETICOS e ILUSTRATIVOS. La probabilidad previa de peligro (1e-3), la sensibilidad de cada prueba
(0.90), su especificidad (0.95) y los costos (retener = 1, liberar con peligro = 1e5, unidades arbitrarias)
son valores propuestos para el ejemplo. NO son parametros del protocolo de evaluacion de seguridad de muestras
de Marte (de ese trabajo solo se leyo el resumen) ni de ninguna autoridad; no sirven para decidir nada real.
Modelo: teorema de Bayes con k pruebas negativas independientes dado el estado real:
    P(H | k negativas) = P(H) (1-s)^k / [ P(H)(1-s)^k + (1-P(H)) e^k ]    (s sensibilidad, e especificidad)
Decision por perdida esperada: se libera si P(H|datos) * C_liberar_peligro < C_retener. Se contrasta con Monte
Carlo (semilla fija) y se calcula el k minimo para liberar.
Sistema de referencia: probabilidades adimensionales; pruebas condicionalmente independientes.
Validez: didactica; ignora correlacion entre pruebas, fondos abioticos y errores de procedimiento.
Tolerancias: posterior analitico por Bayes explicito < 1e-12; Monte Carlo dentro de 3 sigma.
Versiones: se imprimen al ejecutar (solo biblioteca estandar).
"""
from __future__ import annotations
import math, platform, random

PRIOR, SENS, ESP = 1e-3, 0.90, 0.95
C_RET, C_LIB = 1.0, 1e5


def posterior(prior: float, sens: float, esp: float, k: int) -> float:
    num = prior * (1 - sens) ** k
    return num / (num + (1 - prior) * esp ** k)


def k_minimo(prior, sens, esp, c_ret, c_lib, kmax=50):
    for k in range(kmax + 1):
        if posterior(prior, sens, esp, k) * c_lib < c_ret:
            return k
    return None


def montecarlo(prior, sens, esp, k, n=3_000_000, semilla=63):
    """Frecuencia de H entre las muestras con k negativas (prior alto para tener estadistica)."""
    rng = random.Random(semilla)
    neg = hay = 0
    for _ in range(n):
        h = rng.random() < prior
        if all((rng.random() >= sens) if h else (rng.random() < esp) for _ in range(k)):
            neg += 1
            hay += h
    return hay / neg, neg


def main() -> None:
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Parametros sinteticos: prior = {PRIOR:g}, sensibilidad = {SENS}, especificidad = {ESP}, costos retener/liberar-con-peligro = {C_RET:g}/{C_LIB:g}")
    print("  k   P(H | k negativas)   perdida esperada de liberar   decision")
    for k in range(0, 6):
        p = posterior(PRIOR, SENS, ESP, k)
        le = p * C_LIB
        print(f"  {k}   {p:18.3e}   {le:26.3f}   {'liberar' if le < C_RET else 'retener'}")
    k0 = k_minimo(PRIOR, SENS, ESP, C_RET, C_LIB)
    print(f"k minimo para liberar con estos costos = {k0}")
    assert posterior(PRIOR, SENS, ESP, k0) * C_LIB < C_RET <= posterior(PRIOR, SENS, ESP, k0 - 1) * C_LIB
    # prueba analitica: Bayes en razon de verosimilitudes (odds) equivale a la formula directa
    odds0 = PRIOR / (1 - PRIOR)
    for k in range(1, 5):
        odds = odds0 * ((1 - SENS) / ESP) ** k
        assert abs(odds / (1 + odds) - posterior(PRIOR, SENS, ESP, k)) < 1e-12
    print("Forma de razon de momios (odds) coincide con la formula directa (< 1e-12).")
    # Monte Carlo con prior alto (0.2) y k = 2 para tener estadistica suficiente
    pa = posterior(0.2, SENS, ESP, 2)
    pm, neg = montecarlo(0.2, SENS, ESP, 2)
    sigma = math.sqrt(pa * (1 - pa) / neg)
    print(f"Contraste Monte Carlo (prior 0.2, k = 2, {neg} casos con 2 negativas): analitico = {pa:.5f}, simulado = {pm:.5f}, 3 sigma = {3 * sigma:.5f}")
    assert abs(pm - pa) < 3 * sigma
    # sensibilidad del k minimo a la sensibilidad de la prueba
    print("k minimo segun la sensibilidad de cada prueba:")
    for s in (0.5, 0.7, 0.9, 0.99):
        print(f"  s = {s:4.2f}  ->  k = {k_minimo(PRIOR, s, ESP, C_RET, C_LIB)}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
