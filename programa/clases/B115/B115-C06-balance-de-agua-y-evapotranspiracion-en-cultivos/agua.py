#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B115-C06: evapotranspiracion de un cultivo en camara (Penman-Monteith tipo FAO-56) y balance de agua del modulo.

CONSULTADO (FAO-56, capitulo 2, pagina consultada el 2026-11-10): variables y unidades de la ecuacion (ETo en mm/dia, Rn y G en
MJ m-2 d-1, T a 2 m, u2, es, ea, pendiente Delta, constante psicrometrica gamma), definicion de Kc = ETc/ETo y cultivo de
referencia (0.12 m de altura, resistencia superficial de 70 s/m, albedo 0.23). La ecuacion misma aparecia solo como imagen en esa
pagina: se usa la forma estandar conocida, NO consultada aqui, y el laboratorio la verifica con la forma general de Monteith.
SINTETICO/ILUSTRATIVO: camara a 23 C, HR 60 %, u2 = 0.5 m/s, 300 umol m-2 s-1 durante 16 h (de B115-C02), fraccion neta
absorbida 0.7, Kc = 1.0, 8.4 m2 de cultivo (de B115-C05), recuperacion del condensado 95 %, agua del producto 94 %,
produccion 468 g/dia. Unidades: mm/dia = L m-2 d-1, MJ m-2 d-1, kPa, L/dia. Solo numpy y la biblioteca estandar.
Verificacion: (1) con deficit de vapor nulo, ETo = 0.408 * Delta/(Delta+gamma*(1+0.34 u2)) * Rn (termino radiativo); (2) la
forma de FAO coincide con la de Monteith con r_s = 70 s/m y r_a = 208/u2 dentro del 3 %; (3) el termino radiativo no supera Rn/lambda (el total si puede, por el aire seco).
"""
from __future__ import annotations
import math
import platform
import numpy as np

LAMBDA = 2.45      # MJ/kg, calor latente de vaporizacion (valor estandar, no consultado)
CP = 1.013e-3      # MJ kg-1 K-1


def es_kpa(t):
    return 0.6108 * math.exp(17.27 * t / (t + 237.3))


def delta_pend(t):
    return 4098.0 * es_kpa(t) / (t + 237.3) ** 2


def gamma_psic(p_kpa):
    return 0.665e-3 * p_kpa


def eto_fao(rn, g, t, u2, rh, p=101.3):
    es = es_kpa(t)
    ea = es * rh
    d, gm = delta_pend(t), gamma_psic(p)
    rad = 0.408 * d * (rn - g)
    aer = gm * 900.0 / (t + 273.0) * u2 * (es - ea)
    return (rad + aer) / (d + gm * (1 + 0.34 * u2)), rad / (d + gm * (1 + 0.34 * u2)), aer / (d + gm * (1 + 0.34 * u2))


def et_monteith(rn, g, t, u2, rh, rs, p=101.3):
    """Forma general de Penman-Monteith con r_a = 208/u2 (s/m) y resistencia superficial rs (s/m)."""
    es = es_kpa(t)
    ea = es * rh
    d = delta_pend(t)
    gm = CP * p / (0.622 * LAMBDA)
    rho = 3.486 * p / (1.01 * (t + 273.0))
    ra = 208.0 / u2
    num = d * (rn - g) + 86400.0 * rho * CP * (es - ea) / ra
    return num / (LAMBDA * (d + gm * (1 + rs / ra)))


def rn_dia(ppfd, horas, absorbida=0.7, e_mol=204.5):
    """Energia neta absorbida de la luz de cultivo (MJ m-2 d-1): DLI * energia por mol * fraccion absorbida."""
    dli = ppfd * horas * 3600.0 / 1e6
    return dli * e_mol / 1000.0 * absorbida


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: variables de FAO-56 (consultadas); camara, luz, area, recuperacion y agua del producto SINTETICOS/ILUSTRATIVOS")
    t, rh, u2, ppfd, horas = 23.0, 0.60, 0.5, 300.0, 16.0
    rn = rn_dia(ppfd, horas)
    es = es_kpa(t)
    print(f"es = {es:.3f} kPa; ea = {es*rh:.3f} kPa; Delta = {delta_pend(t):.4f} kPa/C; gamma = {gamma_psic(101.3):.4f} kPa/C")
    print(f"Rn = {rn:.2f} MJ/m2/dia (DLI {ppfd*horas*3600/1e6:.2f} mol/m2/d x 0.2045 MJ/mol x 0.7)")
    eto, rad, aer = eto_fao(rn, 0.0, t, u2, rh)
    print(f"ETo (FAO) = {eto:.3f} mm/dia = {rad:.3f} (radiativo) + {aer:.3f} (aerodinamico) mm/dia")

    print("Verificaciones")
    eto0, rad0, aer0 = eto_fao(rn, 0.0, t, u2, 1.0)
    eq = 0.408 * delta_pend(t) / (delta_pend(t) + gamma_psic(101.3) * (1 + 0.34 * u2)) * rn
    print(f"   (1) deficit nulo: ETo = {eto0:.3f} mm/dia; termino radiativo = {eq:.3f} mm/dia")
    assert abs(eto0 - eq) < 1e-9 and abs(aer0) < 1e-12
    m = et_monteith(rn, 0.0, t, u2, rh, 70.0)
    err = abs(m - eto) / eto
    print(f"   (2) Monteith general con rs = 70 s/m y ra = 208/u2: {m:.3f} mm/dia; diferencia con FAO = {err*100:.2f} %")
    assert err < 0.03
    cota = rn / LAMBDA
    print(f"   (3) cota de energia radiativa Rn/lambda = {cota:.3f} mm/dia; termino radiativo = {rad:.3f}; ETo/cota = {eto/cota:.2f} "
          f"(el aire seco aporta calor sensible: ETo puede superar la cota)")
    assert rad <= cota

    print("Efecto de la humedad y del aire (u2) sobre ETo [mm/dia]")
    print("   u2[m/s] \\ HR     40 %    60 %    80 %    95 %")
    for u in (0.2, 0.5, 1.0, 2.0):
        print(f"   {u:7.1f}      " + " ".join(f"{eto_fao(rn, 0.0, t, u, h)[0]:7.3f}" for h in (0.4, 0.6, 0.8, 0.95)))
    print("Efecto de la resistencia superficial (cultivo de la camara frente al de referencia de 70 s/m), forma general de Monteith")
    for rs in (30.0, 70.0, 120.0):
        print(f"   rs = {rs:5.0f} s/m -> ETc = {et_monteith(rn, 0.0, t, u2, rh, rs):.3f} mm/dia")

    kc, area, rec, agua_prod, prod_g = 1.0, 8.4, 0.95, 0.94, 468.0
    etc = kc * eto
    transp = etc * area
    recup = transp * rec
    incorporada = prod_g / 1000.0 * agua_prod
    print(f"Balance de agua diario del modulo de {area} m2 (Kc = {kc}):")
    print(f"   transpirada = {transp:.2f} L/dia; recuperada por condensado = {recup:.2f} L/dia; no recuperada = {transp-recup:.2f} L/dia")
    print(f"   incorporada en el producto = {incorporada:.2f} L/dia ({prod_g:.0f} g/dia de masa fresca con 94 % de agua, ilustrativo)")
    rep = transp - recup + incorporada
    print(f"   reposicion necesaria = {rep:.2f} L/dia = {rep/area:.3f} L/m2/dia; sin condensador serian {transp+incorporada:.2f} L/dia")
    assert abs(rep - ((transp - recup) + incorporada)) < 1e-12

    rng = np.random.default_rng(115)
    vals = []
    for _ in range(2000):
        tt = rng.normal(23.0, 1.0)
        hh = rng.uniform(0.50, 0.80)
        uu = rng.uniform(0.2, 1.0)
        pp = ppfd * rng.uniform(0.9, 1.1)
        vals.append(eto_fao(rn_dia(pp, horas), 0.0, tt, uu, hh)[0])
    vals = np.array(vals)
    p5, p50, p95 = np.percentile(vals, [5, 50, 95])
    print(f"Monte Carlo (2000 casos, semilla 115; T ~ N(23, 1) C, HR 50-80 %, u2 0.2-1.0 m/s, luz +-10 %): "
          f"ETo mediana {p50:.3f}, intervalo 5-95 % [{p5:.3f}; {p95:.3f}] mm/dia")
    print(f"   Reposicion con los extremos: {(p5*area*(1-rec)+incorporada):.2f} a {(p95*area*(1-rec)+incorporada):.2f} L/dia")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
