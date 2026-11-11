#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B117-C04: oxigenacion SIMULADA frente a la atmosfera de la cabina (gas alveolar y curva de Severinghaus).

CONTENIDO EDUCATIVO: no es un criterio diagnostico ni consejo medico; no sustituye formacion ni supervision profesional.
Datos consultados (2026-11-10): Schaezler y Cook, ICES-2015-146 (NASA NTRS 20150010425): la EEI mantiene una presion parcial de O2 de
146 a 178 mmHg y una presion total de 724 a 770.5 mmHg. Se usan los extremos y un punto central (760 mmHg, ppO2 160 mmHg dentro del rango).
Relaciones estandar NO consultadas en una fuente concreta: ecuacion del gas alveolar PAO2 = FiO2 (Pb - PH2O) - PaCO2/RQ;
curva de Severinghaus SaO2 = 1 / (23400/(P^3 + 150 P) + 1).
ILUSTRATIVOS (sinteticos, no medidos): PH2O = 47 mmHg, RQ = 0.8, PaCO2 basal = 40 mmHg, gradiente alveolo-arterial = 10 mmHg,
presiones de los escenarios de fuga (600 mmHg), CO2 inspirado, hipoventilacion (PaCO2 = 60), constante de tiempo de la fuga 48 h,
umbral de alerta PAO2 = 60 mmHg. Unidades: mmHg y h. La fuga se modela con FiO2 constante (sin reposicion de O2).
Tolerancias: curva de Severinghaus en P = 26.8 mmHg igual a 0.50 con 0.01; tiempo de fuga numerico frente a analitico < 1e-6 h.
"""
from __future__ import annotations
import math, platform

PH2O, RQ, PACO2_0, AA = 47.0, 0.8, 40.0, 10.0
TAU_FUGA, UMBRAL = 48.0, 60.0


def pao2(fio2, pb, paco2):
    return fio2 * (pb - PH2O) - paco2 / RQ


def sao2(p):
    return 1.0 / (23400.0 / (p ** 3 + 150.0 * p) + 1.0)


def presion_critica(fio2, paco2):
    return PH2O + (UMBRAL + paco2 / RQ) / fio2


def tiempo_fuga_analitico(p0, fio2, paco2):
    return TAU_FUGA * math.log(p0 / presion_critica(fio2, paco2))


def tiempo_fuga_numerico(p0, fio2, paco2):
    lo, hi = 0.0, 500.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if pao2(fio2, p0 * math.exp(-mid / TAU_FUGA), paco2) > UMBRAL:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Cabina CONSULTADA (EEI): Pb 724-770.5 mmHg, ppO2 146-178 mmHg. Escenarios de fuga e hipoventilacion ILUSTRATIVOS.")
    escen = [
        ("nominal (760; 160)", 760.0, 160.0, 40.0),
        ("extremo bajo (724; 146)", 724.0, 146.0, 40.0),
        ("extremo alto (770.5; 178)", 770.5, 178.0, 40.0),
        ("fuga a 600 mmHg", 600.0, 600.0 * 160.0 / 760.0, 40.0),
        ("CO2 elevado (PaCO2 48)", 760.0, 160.0, 48.0),
        ("fuga + hipoventilacion", 600.0, 600.0 * 160.0 / 760.0, 60.0),
    ]
    print(" escenario                  Pb    ppO2   FiO2    PaCO2  PAO2    PaO2   SaO2")
    sa = {}
    for nom, pb, ppo2, pc in escen:
        fio2 = ppo2 / pb
        a = pao2(fio2, pb, pc)
        ao = a - AA
        s = sao2(ao)
        sa[nom] = (a, s)
        print(f"{nom:26s} {pb:6.1f} {ppo2:6.1f} {fio2:6.4f} {pc:6.1f} {a:6.1f} {ao:7.1f} {s:6.3f}")
    p_star = sao2(26.8)
    print(f"Severinghaus en PO2 = 26.8 mmHg: SaO2 = {p_star:.4f} (P50 esperada ~0.50)")
    fio2 = 160.0 / 760.0
    pc = presion_critica(fio2, 40.0)
    ta = tiempo_fuga_analitico(760.0, fio2, 40.0)
    tn = tiempo_fuga_numerico(760.0, fio2, 40.0)
    print(f"Fuga con tau = {TAU_FUGA:.0f} h y FiO2 = {fio2:.4f}: Pb critica = {pc:.1f} mmHg ; t analitico = {ta:.4f} h ; t numerico = {tn:.4f} h")
    mono = all(sao2(p + 1) > sao2(p) for p in range(10, 200))
    print(f"Curva de Severinghaus monotona creciente en 10-200 mmHg: {mono}")
    assert abs(p_star - 0.5) < 0.01
    assert abs(ta - tn) < 1e-6
    assert mono
    assert sa["nominal (760; 160)"][0] > sa["extremo bajo (724; 146)"][0] > sa["fuga a 600 mmHg"][0] > sa["fuga + hipoventilacion"][0]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
