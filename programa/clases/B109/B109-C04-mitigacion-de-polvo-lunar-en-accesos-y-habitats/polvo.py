#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B109-C04: polvo que llega al interior tras una cadena de barreras y sedimentacion de Stokes en gravedad lunar.

Datos consultados (2026-11-10): NASA/NSSDC Moon Fact Sheet (g = 1.62 m/s2); Stromgren et al. (2023): dos EVA de dos tripulantes por semana (104 EVA/ano) y la comparacion
CUALITATIVA de que la esclusa clasica abre la escotilla interior con trajes sucios y el suitport-esclusa reduce la entrada de polvo; Gaier (2005, NASA/TM-2005-213610), solo el resumen:
nueve categorias de efectos del polvo en Apollo y que las pruebas en tierra subestimaron su gravedad.
ILUSTRATIVOS / NO CONSULTADOS: masa de polvo por traje y EVA (100 g), eficiencias de cada barrera, fraccion que cruza un suitport (0.03), densidad de grano 3100 kg/m3,
viscosidad del aire 1.8e-5 Pa s, densidad del aire 0.68 kg/m3, altura de caida 1.5 m, g terrestre convencional 9.80665 m/s2.
Modelo 1: residual por traje = m0 * prod(1 - eta_i); anual = residual * 2 trajes * 104 EVA. Incertidumbre: eta_i ~ Beta con media dada y concentracion 20 (semilla 109004, 20000 sorteos).
Segunda via 1: para etapas independientes E[prod(1 - eta_i)] = prod E[1 - eta_i]; la media Monte Carlo debe coincidir con el producto (tolerancia 1 %).
Modelo 2: velocidad de Stokes v = rho_p g d^2 /(18 mu); tiempo de caida h/v; validez: Re = rho_aire v d / mu < 1. Segunda via 2: t_Luna/t_Tierra = g_Tierra/g_Luna (tolerancia 1e-12).
Unidades: masa [g], longitud [m], tiempo [s], velocidad [m/s].
"""
from __future__ import annotations
import math, platform, random

M0 = 100.0  # g por traje y EVA (ILUSTRATIVO)
EVAS, TRAJES = 104, 2
ETAS_A = [("cepillado exterior", 0.60), ("rejilla/alfombra de la esclusa", 0.50), ("aspirado del traje", 0.70)]
ETAS_B = [("cepillado exterior", 0.60)]
CRUCE_SUITPORT = 0.03  # fraccion que cruza el suitport (ILUSTRATIVO)
RHO_P, MU, RHO_A, H = 3100.0, 1.8e-5, 0.68, 1.5
G_LUNA, G_TIERRA = 1.62, 9.80665


def residual(etas, extra=1.0):
    f = extra
    for _, e in etas:
        f *= 1 - e
    return M0 * f


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Masas, eficiencias y propiedades ILUSTRATIVAS; g lunar y cadencia de EVA consultados")
    ra = residual(ETAS_A)
    rb = residual(ETAS_B, CRUCE_SUITPORT)
    print(f"Config A (esclusa clasica, 3 barreras): residual por traje = {ra:.2f} g ; anual = {ra * TRAJES * EVAS / 1000:.3f} kg")
    print(f"Config B (cepillado + suitport):        residual por traje = {rb:.2f} g ; anual = {rb * TRAJES * EVAS / 1000:.3f} kg")
    print(f"Sin barreras: anual = {M0 * TRAJES * EVAS / 1000:.1f} kg")
    rng = random.Random(109004)
    K = 20.0
    n = 20000
    vals = []
    for _ in range(n):
        f = 1.0
        for _, e in ETAS_A:
            f *= 1 - rng.betavariate(K * e, K * (1 - e))
        vals.append(M0 * f * TRAJES * EVAS / 1000)
    vals.sort()
    media = sum(vals) / n
    print(f"Monte Carlo (A): media = {media:.3f} kg/ano ; intervalo 95 % = [{vals[int(0.025 * n)]:.3f}, {vals[int(0.975 * n)]:.3f}] kg/ano")
    analitico = ra * TRAJES * EVAS / 1000
    print(f"Media analitica (producto de medias) = {analitico:.3f} kg/ano")
    assert abs(media - analitico) / analitico < 0.01
    print(" d [um]   v_Luna [mm/s]   t_Luna [min]   t_Tierra [min]   Re_Luna")
    for d_um in (2.0, 10.0, 50.0):
        d = d_um * 1e-6
        vl = RHO_P * G_LUNA * d * d / (18 * MU)
        vt = RHO_P * G_TIERRA * d * d / (18 * MU)
        tl, tt = H / vl / 60, H / vt / 60
        re = RHO_A * vl * d / MU
        print(f"{d_um:7.1f} {vl * 1000:14.4f} {tl:14.1f} {tt:16.1f} {re:10.2e}")
        assert re < 1
        assert abs(tl / tt - G_TIERRA / G_LUNA) < 1e-12
    assert rb < ra
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
