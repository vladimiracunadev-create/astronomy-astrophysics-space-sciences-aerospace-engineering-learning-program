#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B28-C09: latencia de una alerta, tasa de falsas alarmas y factor de pruebas.

Datos: ninguna constante fisica. Contexto: GW150914 tuvo una tasa de falsas alarmas estimada menor que 1 por 203 000 anios
(arXiv:1602.03837, resumen); BAYESTAR produce mapas de localizacion en segundos (arXiv:1508.03634, resumen); en GW170817 el destello
gamma llego ~1.7 s despues de la fusion (arXiv:1710.05833, resumen). Las latencias de cada etapa, la tasa base de candidatos
(1000 por dia sobre rho = 4) y los umbrales son ILUSTRATIVOS (sinteticos).
Modelo: (1) latencia total = suma de etapas; (2) probabilidad de al menos una falsa alarma en un tiempo T: 1 - exp(-FAR T);
(3) cola de los candidatos de ruido P(rho > x) = exp(-(x^2 - rho0^2)/2) (2 grados de libertad), con tasa FAR(x) = R0 exp(-(x^2 - rho0^2)/2);
umbral para un FAR dado: x = sqrt(rho0^2 - 2 ln(FAR/R0)), contrastado por Monte Carlo (semilla fija); (4) factor de pruebas:
p_global = 1 - (1 - p)^N.
Supuestos: ruido estacionario, candidatos independientes. Validez: orientativa.
Tolerancia: la fraccion Monte Carlo sobre el umbral dentro de 5 desviaciones de Poisson de la esperada.
"""
from __future__ import annotations
import math
import platform
import random
import sys


def sigma_de_p(p):
    lo, hi = 0.0, 40.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if 0.5 * math.erfc(mid / math.sqrt(2)) > p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def umbral(far_dia, r0_dia, rho0):
    return math.sqrt(rho0 ** 2 - 2 * math.log(far_dia / r0_dia))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    etapas = [("deteccion y transferencia de datos", 10.0), ("busqueda y disparo", 20.0), ("localizacion rapida", 10.0), ("revision y envio", 30.0)]
    acum = 0.0
    print(f"{'etapa (ilustrativa)':<36} {'dt [s]':>7} {'acumulado [s]':>14}")
    for nombre, dt in etapas:
        acum += dt
        print(f"{nombre:<36} {dt:7.1f} {acum:14.1f}")
    print(f"latencia total = {acum:.1f} s ; el destello gamma de GW170817 llego 1.7 s despues de la fusion (S)")
    far_anio = 1 / 203000
    for t_anio in (1.0, 5.0, 100.0):
        p = 1 - math.exp(-far_anio * t_anio)
        print(f"FAR = 1/203000 por anio: P(al menos una falsa alarma en {t_anio:g} anios) = {p:.3e} = {sigma_de_p(p):.2f} sigma (una cola)")
    assert abs(sigma_de_p(0.5 * math.erfc(5 / math.sqrt(2))) - 5.0) < 1e-9
    r0, rho0 = 1000.0, 4.0
    for nombre, far in (("1 por dia", 1.0), ("1 por mes", 1 / 30.0), ("1 por anio", 1 / 365.25)):
        print(f"FAR = {nombre:<10}: umbral rho = {umbral(far, r0, rho0):.3f}")
    # Monte Carlo
    rng = random.Random(20261109)
    n = 2_000_000
    x = umbral(1.0, r0, rho0)
    p_esp = 1.0 / r0
    cuenta = sum(1 for _ in range(n) if math.sqrt(rho0 ** 2 - 2 * math.log(1 - rng.random())) > x)
    esp = n * p_esp
    print(f"Monte Carlo: {n} candidatos, umbral {x:.3f}: {cuenta} sobre el umbral (esperados {esp:.0f} +/- {math.sqrt(esp):.0f})")
    assert abs(cuenta - esp) < 5 * math.sqrt(esp), "cola del ruido"
    # factor de pruebas
    p = 1e-3
    for ntr in (1, 10, 100, 1000):
        pg = 1 - (1 - p) ** ntr
        print(f"p local = {p:g}, {ntr:4d} pruebas: p global = {pg:.4f} ({sigma_de_p(pg):.2f} sigma)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    sys.exit(main())
