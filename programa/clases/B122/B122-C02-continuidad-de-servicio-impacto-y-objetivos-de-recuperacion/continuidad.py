#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B122-C02: analisis de impacto en la continuidad (BIA), disponibilidad, RTO y RPO de un servicio SINTETICO.

CONTENIDO EDUCATIVO Y DEFENSIVO: no es asesoria legal, regulatoria, financiera ni de seguridad. Datos SINTETICOS (inventados).
Marco conceptual (solo ficha y resumen consultados el 2026-11-11): NIST SP 800-34 Rev. 1 (2010), guia de planificacion de contingencias.
Definiciones: disponibilidad A = MTBF/(MTBF+MTTR); RTO = tiempo objetivo de recuperacion; RPO = perdida maxima de datos tolerable
medida en tiempo; MTD (tiempo maximo tolerable de interrupcion) >= RTO + tiempo de recuperacion de trabajo (WRT).
Servicio sintetico: enlace de telemetria; MTBF = 720 h, MTTR = 4 h; costo de impacto 1.5 kUSD(ficticios)/h creciente con la interrupcion.
Unidades: horas, kUSD ficticios (sin valor real), adimensional. Sistema de referencia: reloj desde el inicio de la interrupcion.
Tolerancias: A simulada (50 anos simulados, semilla 122) vs analitica < 0.0005; impacto numerico vs cerrado < 0.5 %.
"""
from __future__ import annotations
import math, platform, random

MTBF, MTTR = 720.0, 4.0
C0, K = 1.5, 0.25  # kUSD/h inicial y crecimiento por hora (impacto = C0 + K t), ficticio
RTO, WRT, MTD = 6.0, 2.0, 8.0


def disponibilidad():
    return MTBF / (MTBF + MTTR)


def simular_disponibilidad(anios, seed):
    rng = random.Random(seed)
    horizonte = anios * 8760.0
    t, caido = 0.0, 0.0
    cortes = []
    while t < horizonte:
        t += rng.expovariate(1 / MTBF)
        d = rng.expovariate(1 / MTTR)
        if t >= horizonte:
            break
        d = min(d, horizonte - t)
        caido += d
        cortes.append(d)
        t += d
    return 1 - caido / horizonte, cortes


def impacto_acumulado(t):
    """Integral de (C0 + K s) ds de 0 a t = C0 t + K t^2/2 (kUSD ficticios)."""
    return C0 * t + K * t * t / 2


def impacto_numerico(t, n=100000):
    h = t / n
    return sum((C0 + K * (i + 0.5) * h) * h for i in range(n))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("DATOS SINTETICOS: MTBF 720 h, MTTR 4 h, costos ficticios en kUSD sin valor real.")
    a = disponibilidad()
    print(f"Disponibilidad analitica A = {a:.5f} ; indisponibilidad anual = {(1 - a) * 8760:.2f} h")
    a_sim, cortes = simular_disponibilidad(50, 122)
    frac = sum(1 for d in cortes if d > RTO) / len(cortes)
    print(f"Simulacion de 50 anos: A = {a_sim:.5f} ; cortes = {len(cortes)} ; fraccion de cortes con duracion > RTO ({RTO} h) = {frac:.3f}")
    print(f"Fraccion teorica de cortes > RTO (exponencial) = exp(-RTO/MTTR) = {math.exp(-RTO / MTTR):.3f}")
    assert abs(a - a_sim) < 0.0005
    print(f"MTD = {MTD} h ; RTO + WRT = {RTO + WRT} h ; condicion RTO + WRT <= MTD: {RTO + WRT <= MTD}")
    print("Impacto acumulado de una interrupcion de t horas (cerrado | numerico), kUSD ficticios:")
    for t in (1, 2, 4, 6, 8, 12):
        c, n = impacto_acumulado(t), impacto_numerico(t)
        assert abs(c - n) / c < 0.005
        print(f"  t={t:2d} h : {c:7.2f} | {n:7.2f}")
    print("Cuantas veces al ano se espera superar MTD:", f"{(8760 / (MTBF + MTTR)) * math.exp(-MTD / MTTR):.3f}")
    rpo_ok = {"copia cada 1 h": 1.0, "copia cada 6 h": 6.0, "copia cada 24 h": 24.0}
    RPO = 4.0
    print(f"RPO = {RPO} h (ilustrativo):")
    for k, v in rpo_ok.items():
        print(f"  {k}: perdida maxima {v} h -> {'cumple' if v <= RPO else 'NO cumple'}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
