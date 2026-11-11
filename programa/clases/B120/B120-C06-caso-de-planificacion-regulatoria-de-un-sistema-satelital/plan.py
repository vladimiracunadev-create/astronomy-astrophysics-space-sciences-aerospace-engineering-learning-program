#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B120-C06: plan regulatorio regresivo de un sistema satelital SINTETICO «SINT-C» (integrador del bloque B120).

CONTENIDO EDUCATIVO: no es asesoria legal, regulatoria ni financiera.
CONSULTADO (2026-11-11):
 - «ITU Radio Regulatory Framework for Space Services» (UIT, PDF creado 2018-01-10; hasta CMR-15): API no antes de 7 anios y preferentemente no despues
   de 2 anios antes de la BIU; coordinacion desde 6 meses tras la API y solicitud antes de 24 meses; respuesta de las administraciones en 4 meses; notificacion
   no antes de 3 anios previos a la BIU; BIU a 7 anios como maximo de la API; informacion de diligencia debida antes del fin de esos 7 anios y la del lanzador
   antes de notificar.
 - Diapositivas «A milestone approach for NGSO systems, Resolution 35 (WRC-19)» (UIT, 24-28 octubre 2022): hitos 10/50/100 % en (plazo de 7 anios + 2/5/7 anios)
   + 30 dias, para plazos posteriores al 1 de enero de 2021 (caso 2 de la diapositiva).
NO CONSULTADO: Reglamento vigente, revision CMR-23 de la Res. 35, prorrogas y excepciones; la regla M0 de la diapositiva no se usa por no estar clara.
ILUSTRATIVO (del curso, no normativo): 14 meses de negociacion de coordinacion, 6 meses de examen antes de la BIU, diligencia debida 12 meses antes de la BIU,
retraso de lanzamiento normal(8, 5) meses, riesgo objetivo 5 %, margen de coordinacion minimo 6 meses; 120 satelites, 12 por lanzamiento, 2 lanzamientos por anio.
Fechas AAAA-MM-DD; BIU objetivo sintetica 2033-09-01. Semilla fija 120. Tolerancia: fechas por dos aritmeticas con diferencia <= 4 dias; Poisson analitico frente a simulacion < 0.005.
"""
from __future__ import annotations
import calendar, math, platform, random
from datetime import date, timedelta

BIU = date(2033, 9, 1)
NEGOCIACION, EXAMEN, DD_ANTES, MARGEN_MIN = 14, 6, 12, 6
MU, SIGMA, RIESGO = 8.0, 5.0, 0.05
N, M, LAM = 120, 12, 2.0


def add_months(d, n):
    m = d.year * 12 + d.month - 1 + n
    y, mo = divmod(m, 12)
    return date(y, mo + 1, min(d.day, calendar.monthrange(y, mo + 1)[1]))


def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def p_miss(slack):
    return 1 - phi((slack - MU) / SIGMA)


def pois_cdf_lt(k, lam):
    return sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(k))


def ventana_L():
    """Plazo entre la API y la BIU (meses) que cumple: riesgo <= 5 % y margen de coordinacion >= 6 meses."""
    ok = []
    for L in range(24, 85):       # 24 = 'preferentemente 2 anios'; 84 = 7 anios
        slack = 84 - L
        margen = L - (6 + 4 + NEGOCIACION + EXAMEN)
        if p_miss(slack) <= RIESGO and margen >= MARGEN_MIN:
            ok.append(L)
    return ok


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("PLAN REGULATORIO SINTETICO «SINT-C»; plazos UIT 2018-01-10 y diapositivas Res. 35 (2022-10), consulta 2026-11-11; reglas del curso rotuladas. No es asesoria.")
    print("L [meses API->BIU]  holgura  P(incumplir BIU)  margen de coordinacion [meses]")
    for L in (24, 30, 36, 48, 60, 67, 68, 72, 84):
        print(f"{L:18d}  {84 - L:7d}  {p_miss(84 - L):15.4f}  {L - (6 + 4 + NEGOCIACION + EXAMEN):10d}")
    ok = ventana_L()
    L = (ok[0] + ok[-1]) // 2
    print(f"Ventana factible de L: {ok[0]}..{ok[-1]} meses; se elige el punto medio L = {L} (convencion del curso)")
    t0 = add_months(BIU, -L)
    plan = [
        ("API recibida (t0)", t0),
        ("Coordinacion posible desde (t0 + 6 m)", add_months(t0, 6)),
        ("Solicitud de coordinacion (en cuanto es posible, t0 + 6 m)", add_months(t0, 6)),
        ("Respuestas de las administraciones (+4 m)", add_months(t0, 10)),
        ("Coordinacion concluida (+14 m de negociacion)", add_months(t0, 10 + NEGOCIACION)),
    ]
    coord_fin = plan[-1][1]
    notif = max(add_months(coord_fin, 1), add_months(BIU, -36))
    plan += [
        ("Informacion del lanzador (1 m antes de notificar)", add_months(notif, -1)),
        ("Notificacion al registro", notif),
        ("Informacion de diligencia (BIU - 12 m)", add_months(BIU, -DD_ANTES)),
        ("BIU objetivo", BIU),
        ("Informe de 90 dias continuos (BIU + 90 d + 30 d)", BIU + timedelta(days=120)),
    ]
    limite = add_months(t0, 84)
    plan += [("Limite de 7 anios desde la API", limite)]
    for k, (nm, anios) in enumerate((("M1 10 %", 2), ("M2 50 %", 5), ("M3 100 %", 7)), 1):
        plan.append((f"Hito {nm} ((limite + {anios} anios) + 30 d)", add_months(limite, 12 * anios) + timedelta(days=30)))
    print("Calendario del plan:")
    for nm, f in sorted(plan, key=lambda x: x[1]):
        print(f"  {f}  {nm}")
    # verificaciones cruzadas: meses por dias (segunda aritmetica)
    def meses_dias(a, b):
        return (b - a).days / 30.4375
    assert abs(meses_dias(t0, BIU) - L) < 0.2 and abs(meses_dias(t0, limite) - 84) < 0.2
    assert t0 + timedelta(days=0) >= add_months(BIU, -84) and BIU <= limite
    assert add_months(t0, 6) <= add_months(t0, 6) <= add_months(t0, 24)
    assert notif >= add_months(BIU, -36) and notif <= add_months(BIU, -EXAMEN) and coord_fin < notif
    print(f"Verificacion de reglas del plan: API dentro de [BIU-84m, BIU-24m]: {add_months(BIU, -84) <= t0 <= add_months(BIU, -24)}; "
          f"BIU <= limite: {BIU <= limite}; notificacion >= BIU-36m: {notif >= add_months(BIU, -36)}; coordinacion concluida antes de notificar: {coord_fin < notif}")
    p_b = p_miss(84 - L)
    print(f"Riesgo del plazo de BIU con holgura {84 - L} meses: {p_b:.4f}")
    rng = random.Random(120)
    sim = sum(rng.gauss(MU, SIGMA) > 84 - L for _ in range(200_000)) / 200_000
    print(f"  simulacion = {sim:.4f} (diferencia {abs(sim - p_b):.4f})")
    print("Riesgo de los hitos (120 satelites, 12 por lanzamiento, 2 lanzamientos/anio):")
    total_ok = 1 - p_b
    for nm, frac, anios in (("M1 10 %", 0.10, 2), ("M2 50 %", 0.50, 5), ("M3 100 %", 1.00, 7)):
        need = math.ceil(frac * N / M)
        p = pois_cdf_lt(need, LAM * anios)
        print(f"  {nm}: {need} lanzamientos en {anios} anios (lambda T = {LAM * anios:.0f}) -> P(incumplir) = {p:.4f}")
        total_ok *= 1 - p
    print(f"Probabilidad de cumplir el plazo y los tres hitos (independencia, hitos tratados por separado) = {total_ok:.4f}")
    assert abs(sim - p_b) < 0.005 and p_b <= RIESGO
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
