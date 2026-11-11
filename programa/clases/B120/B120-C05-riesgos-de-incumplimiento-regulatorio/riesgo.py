#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B120-C05: riesgo de incumplimiento de un plazo de puesta en servicio y de un hito de despliegue (SINTETICO).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
CONSULTADO (2026-11-11):
 - «ITU Radio Regulatory Framework for Space Services» (UIT, PDF creado 2018-01-10; hasta CMR-15): la puesta en servicio notificada no puede superar 7 anios
   desde la API (No. 11.44); si la informacion de diligencia debida llega incompleta o tarde, la red se cancela.
 - «A milestone approach for NGSO systems, Resolution 35 (WRC-19)» (diapositivas UIT, 30.o Seminario Mundial, 24-28 octubre 2022): hitos M1 10 %, M2 50 %,
   M3 100 % de los satelites del sistema a 2, 5 y 7 anios del plazo de puesta en servicio; el incumplimiento de un hito reduce el numero de satelites del sistema
   (con una excepcion en el resuelve 12). Nota de la UIT del 2020-01-30 sobre la CMR-19: el enfoque busca evitar el acaparamiento de espectro.
NO CONSULTADO: el texto de la Resolucion 35 (ni su revision de la CMR-23), los limites de reduccion, las prorrogas y excepciones, el costo real de una cancelacion.
SINTETICO / ILUSTRATIVO: holgura de 12 meses; retraso de lanzamiento normal(8, 5) meses; sistema de 300 satelites; 20 satelites por lanzamiento; 1.2 lanzamientos por
anio durante 2 anios; valor de 1.0 unidad de valor (UV) por satelite en el sistema (no es dinero real).
Tolerancias: probabilidad simulada frente a analitica < 0.005 (200000 repeticiones, semilla fija 120); perdida esperada < 0.5 UV.
"""
from __future__ import annotations
import math, platform, random


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def p_retraso(slack, mu, sigma):
    """P(retraso > holgura) con retraso normal (analitico)."""
    return 1 - phi((slack - mu) / sigma)


def pois_pmf(k, lam):
    return math.exp(-lam) * lam ** k / math.factorial(k)


def knuth_poisson(rng, lam):
    L, k, p = math.exp(-lam), 0, 1.0
    while True:
        p *= rng.random()
        if p <= L:
            return k
        k += 1


def p_hito(n_sat, frac, por_lanzamiento, lam_t):
    """P(no alcanzar el hito) = P(K < ceil(frac n / m)) con K ~ Poisson(lam_t) (analitico)."""
    need = math.ceil(frac * n_sat / por_lanzamiento)
    return sum(pois_pmf(k, lam_t) for k in range(need)), need


def perdida_esperada(n_sat, frac, por_lanzamiento, lam_t):
    need = math.ceil(frac * n_sat / por_lanzamiento)
    return sum(pois_pmf(k, lam_t) * (n_sat - por_lanzamiento * k) for k in range(need))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("RIESGO SINTETICO; plazos y hitos de documentos UIT 2018-01-10 y 2022-10 (consulta 2026-11-11); no es asesoria legal, regulatoria ni financiera.")
    slack, mu, sigma = 12.0, 8.0, 5.0
    n, frac, m, lam, T = 300, 0.10, 20, 1.2, 2.0
    rng = random.Random(120)
    reps = 200_000
    p_a = p_retraso(slack, mu, sigma)
    p_mc = sum(rng.gauss(mu, sigma) > slack for _ in range(reps)) / reps
    print(f"Plazo de BIU: holgura {slack} meses, retraso normal({mu}, {sigma}) meses")
    print(f"  P(incumplir) analitica = {p_a:.4f} ; simulada = {p_mc:.4f} ; diferencia = {abs(p_a - p_mc):.4f}")
    print("  Sensibilidad al retraso medio (analitica):")
    for mm in (4.0, 6.0, 8.0, 10.0, 12.0):
        print(f"    media {mm:4.1f} meses -> P = {p_retraso(slack, mm, sigma):.4f}")
    p_h, need = p_hito(n, frac, m, lam * T)
    rng2 = random.Random(121)
    falla, perdida = 0, 0.0
    for _ in range(reps):
        k = knuth_poisson(rng2, lam * T)
        if m * k < frac * n:
            falla += 1
            perdida += n - m * k
    p_h_mc, loss_mc = falla / reps, perdida / reps
    loss_a = perdida_esperada(n, frac, m, lam * T)
    print(f"Hito M1 ({frac:.0%} de {n} satelites = {math.ceil(frac * n)}; {need} lanzamientos de {m}) en {T} anios con {lam} lanzamientos/anio")
    print(f"  P(incumplir M1) analitica = {p_h:.4f} ; simulada = {p_h_mc:.4f} ; diferencia = {abs(p_h - p_h_mc):.4f}")
    print(f"  Perdida esperada por reduccion (UV): analitica = {loss_a:.2f} ; simulada = {loss_mc:.2f}")
    p_any = 1 - (1 - p_a) * (1 - p_h)
    print(f"P(incumplir al menos uno) suponiendo independencia = {p_any:.4f}")
    print("Reserva de holgura necesaria para P(BIU) <= 5 %:", f"{mu + 1.6449 * sigma:.1f} meses (z95 = 1.6449)")
    assert abs(p_a - p_mc) < 0.005 and abs(p_h - p_h_mc) < 0.005 and abs(loss_a - loss_mc) < 0.5
    assert abs(p_retraso(mu + 1.6449 * sigma, mu, sigma) - 0.05) < 1e-4
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
