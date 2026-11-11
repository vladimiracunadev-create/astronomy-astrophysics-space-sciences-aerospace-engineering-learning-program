#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B126-C02: preferencias de liquidacion y retorno de una cartera de riesgo SINTETICA.

CONTENIDO EDUCATIVO: no es asesoria financiera, legal ni de inversion.
Consultado (2026-11-11): el listado de documentos modelo de la NVCA (certificado de incorporacion, acuerdo de compra de acciones,
derechos de inversionistas, etc.; solo la LISTA de la pagina, los textos NO se leyeron). La mecanica de preferencia 1x con o sin
participacion NO se consulto en una fuente primaria: se verifica con dos vias de calculo.
ILUSTRATIVOS (sinteticos): inversion de 10 M USD por el 20 % post-money, valores de salida de 5 a 100 M USD, la distribucion de
multiplos de una empresa [0; 0,5; 2; 5; 20; 100]x con probabilidades [0,45; 0,25; 0,15; 0,10; 0,045; 0,005], una cartera de 25 empresas.
Modelo: sin dividendos, sin deuda, sin otras clases de acciones, 1x de preferencia.
Pruebas: (1) las partes suman la salida; (2) via analitica de max() frente a decision de conversion por busqueda;
(3) media de la cartera: exacta (25 x 2,325 / 25) frente a Monte Carlo (20000 carteras, semilla 126) dentro de 0,03x;
(4) P(multiplo de cartera < 1) exacta por convolucion frente a Monte Carlo dentro de 0,01.
"""
from __future__ import annotations
import platform, random

INV, PCT = 10.0, 0.20   # millones de USD
SALIDAS = [5.0, 10.0, 20.0, 40.0, 100.0]


def no_part(S):
    pref = min(S, INV)
    conv = PCT * S
    return max(pref, conv)


def part(S):
    pref = min(S, INV)
    return pref + PCT * (S - pref)


def no_part_busqueda(S):
    # via 2: elegir entre dos acciones posibles
    opciones = {"cobrar_preferencia": min(S, INV), "convertir": PCT * S}
    return max(opciones.values())


MULT = [0.0, 0.5, 2.0, 5.0, 20.0, 100.0]
PROB = [0.45, 0.25, 0.15, 0.10, 0.045, 0.005]
N = 25


def exacta_p_menor_1():
    unidades = [0, 1, 4, 10, 40, 200]            # multiplos en unidades de 0,5x
    dist = {0: 1.0}
    for _ in range(N):
        nueva = {}
        for s, p in dist.items():
            for u, q in zip(unidades, PROB):
                nueva[s + u] = nueva.get(s + u, 0.0) + p * q
        dist = nueva
    limite = N * 1.0 / 0.5                       # multiplo de cartera 1x = N unidades de 1x -> 50 unidades
    return sum(p for s, p in dist.items() if s < limite)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS (ilustrativos); de la NVCA solo se consulto el listado de documentos (2026-11-11).")
    print(f"Inversion {INV:.0f} M USD por {PCT:.0%} post-money, preferencia 1x. Salidas en M USD")
    print(" salida  sin_part  con_part   resto_fund(sin)  resto_fund(con)  inv_%salida(sin)")
    for S in SALIDAS:
        a, b = no_part(S), part(S)
        assert abs(a - no_part_busqueda(S)) < 1e-12
        assert 0 <= a <= S and 0 <= b <= S
        print(f" {S:6.1f}  {a:8.2f}  {b:8.2f}   {S-a:14.2f}   {S-b:14.2f}   {a/S:12.1%}")
    cruce = INV / PCT
    print(f"Salida de cruce (convertir = preferencia, sin participacion) = {cruce:.1f} M USD")
    assert abs(no_part(cruce) - INV) < 1e-12
    # cartera
    media = sum(m * p for m, p in zip(MULT, PROB))
    rnd = random.Random(126)
    TRIALS = 20000
    mult_c = []
    top_share = []
    for _ in range(TRIALS):
        xs = rnd.choices(MULT, PROB, k=N)
        tot = sum(xs)
        mult_c.append(tot / N)
        top_share.append(max(xs) / tot if tot > 0 else 0.0)
    mc_media = sum(mult_c) / TRIALS
    mc_p1 = sum(1 for m in mult_c if m < 1.0) / TRIALS
    ex_p1 = exacta_p_menor_1()
    mult_c.sort()
    print(f"Multiplo esperado por empresa (exacto) = {media:.3f}x ; Monte Carlo de cartera = {mc_media:.3f}x")
    print(f"P(multiplo de cartera < 1x): exacta = {ex_p1:.4f} ; Monte Carlo = {mc_p1:.4f}")
    print(f"Percentiles del multiplo de cartera (MC): P10 = {mult_c[int(.1*TRIALS)]:.2f}x  P50 = {mult_c[int(.5*TRIALS)]:.2f}x  P90 = {mult_c[int(.9*TRIALS)]:.2f}x")
    print(f"Participacion media del mayor exito en el retorno total (MC) = {sum(top_share)/TRIALS:.1%}")
    assert abs(mc_media - media) < 0.03 and abs(mc_p1 - ex_p1) < 0.01
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
