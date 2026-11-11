#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B110-C01: fuga por un orificio, tiempo de reserva T_Res y segmentacion del volumen.

CONSULTADO (2026-11-10): presion minima de referencia de la ISS 490 mmHg (9,5 psia) y regla de retirada con T_Res <= 10 min
(Tobias y McMillan, SpaceOps 2023); intervalo nominal de presion de la ISS 96,5-102,7 kPa (14,0-14,9 psia) y el caso de una fuga de
0,45 kg/dia que tardaria 146 dias en bajar de 102,7 a 96,5 kPa en marzo de 2011 (Schaezler et al., AIAA); volumen habitable de la ISS
de unos 30.000 ft3 (Tobias y McMillan); orificio de unos 2 mm de la Soyuz MS-09 (avisos NASA, agosto de 2018).
ILUSTRATIVOS (sinteticos): volumen de cabina 100 m3, P0 = 101,0 kPa, T = 293,15 K, Cd = 0,8, aire gas ideal (R_esp = 287,05 J/(kg K), gamma = 1,4),
diametros de orificio, resolucion del manometro (1 mmHg) e intervalo de lectura.
Modelo: flujo estrangulado (el exterior es vacio) y cabina isoterma => dP/dt = -P/tau con tau = V/(Cd A psi sqrt(gamma R T)).
T_Res = (P/|dP/dt|) ln(P/P_min). Contenido educativo: NO es un procedimiento operativo.
Tolerancias: analitico frente a integracion numerica < 1e-3 relativa (Euler: el error baja con el paso); Monte Carlo con semilla fija.
"""
from __future__ import annotations
import math, platform, random

R_ESP, GAMMA, T = 287.05, 1.4, 293.15
MMHG = 101325.0 / 760.0  # Pa por mmHg (definicion de atmosfera normal y torr)
P0, P_MIN = 101.0e3, 490.0 * MMHG
CD = 0.8
PSI = (2.0 / (GAMMA + 1.0)) ** ((GAMMA + 1.0) / (2.0 * (GAMMA - 1.0)))


def tau(v, d):
    a = math.pi * d * d / 4.0
    return v / (CD * a * PSI * math.sqrt(GAMMA * R_ESP * T))


def t_res(p, dpdt_abs, pmin=P_MIN):
    return p / dpdt_abs * math.log(p / pmin)


def integra(v, d, p0, pmin, dt=1.0):
    """Balance de masa completo m = P V/(R T), dm/dt = -Cd A P sqrt(gamma/(R T)) psi (Euler con paso pequeno)."""
    a = math.pi * d * d / 4.0
    m = p0 * v / (R_ESP * T)
    t = 0.0
    while True:
        p = m * R_ESP * T / v
        if p <= pmin:
            return t
        mdot = CD * a * p * math.sqrt(GAMMA / (R_ESP * T)) * PSI
        m -= mdot * dt
        t += dt


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    v = 100.0
    print(f"Cabina ILUSTRATIVA V = {v} m3, P0 = {P0/1e3:.1f} kPa = {P0/MMHG:.1f} mmHg, P_min = {P_MIN/1e3:.2f} kPa (490 mmHg)")
    print(f"psi (flujo estrangulado, gamma = 1.4) = {PSI:.4f}")
    print(" d [mm]   tau [h]   T_Res [h]   T_Res numerico [h]   dif relativa")
    maxdif = 0.0
    for dmm in (2, 10, 50, 100):
        d = dmm / 1000.0
        ta = tau(v, d)
        tr = t_res(P0, P0 / ta)
        tn = integra(v, d, P0, P_MIN, dt=max(0.01, ta / 2e6))
        dif = abs(tr - tn) / tr
        maxdif = max(maxdif, dif)
        print(f"{dmm:6d} {ta/3600:9.3f} {tr/3600:10.3f} {tn/3600:16.3f} {dif:14.2e}")
    # diametro para el que T_Res = 10 min
    lo, hi = 1e-4, 5.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if t_res(P0, P0 / tau(v, mid)) > 600.0:
            lo = mid
        else:
            hi = mid
    print(f"Diametro del orificio con T_Res = 10 min (regla de retirada): {1000*lo:.1f} mm")
    # segmentacion: leak en un volumen que se aisla; T_Res es proporcional al volumen que alimenta la fuga
    d = 0.010
    print("Segmentacion con orificio de 10 mm (fuga en el volumen que alimenta el orificio):")
    for vv in (100.0, 60.0, 30.0, 10.0):
        print(f"  V = {vv:5.0f} m3  T_Res = {t_res(P0, P0/tau(vv, d))/60:8.1f} min")
    # medicion con manometro: dos lecturas separadas dt, resolucion 1 mmHg, orificio de 10 mm
    rng = random.Random(110)
    ta = tau(v, d)
    verdad = t_res(P0, P0 / ta)
    res = []
    for dtl in (30.0, 120.0, 600.0):
        errs = []
        for _ in range(2000):
            pa = P0 * math.exp(0.0) / MMHG
            pb = P0 * math.exp(-dtl / ta) / MMHG
            qa = round(pa + rng.uniform(-0.5, 0.5))
            qb = round(pb + rng.uniform(-0.5, 0.5))
            if qa <= qb:
                continue
            est = (qa - qb) * MMHG / dtl
            errs.append(t_res(qa * MMHG, est) / verdad)
        errs.sort()
        res.append((dtl, errs[len(errs) // 2], errs[int(0.05 * len(errs))], errs[int(0.95 * len(errs))], len(errs)))
    print(f"Estimacion de T_Res con dos lecturas (verdad {verdad/60:.1f} min); cociente estimado/verdad:")
    for dtl, med, p5, p95, n in res:
        print(f"  intervalo {dtl:5.0f} s: mediana {med:6.2f}  [P5 {p5:6.2f}; P95 {p95:6.2f}]  ({n} validas de 2000)")
    # consistencia con el dato de tendencia de la ISS (consultado): 0,45 kg/dia, 102,7 -> 96,5 kPa en 146 dias
    vol_iss = 30000.0 * 0.3048 ** 3
    m_gas = 102.7e3 * vol_iss / (R_ESP * T)
    dias = math.log(102.7 / 96.5) * m_gas / 0.45
    print(f"Consistencia con Schaezler et al.: V = {vol_iss:.0f} m3 -> masa de aire {m_gas:.0f} kg; 0.45 kg/dia tarda {dias:.0f} dias (publicado: 146)")
    assert maxdif < 1e-3, maxdif
    assert abs(t_res(P0, P0 / tau(v, 0.01)) - tau(v, 0.01) * math.log(P0 / P_MIN)) < 1e-6
    assert 100 < dias < 190
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
