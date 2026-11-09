#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B61-C07: espaciado de anillos de una cuenca y energia de un gran impacto.

Datos: SINTETICOS/ILUSTRATIVOS. Relacion de espaciado radial entre anillos (2.0 +- 0.3) D^0.5, con D el diametro del
  anillo en km, segun el resumen de Pike y Spudis (1987) leido en una pagina de catalogo de USGS/Springer a traves de
  una busqueda web (consultada el 2026-11-09; el articulo NO se leyo). Cuenca inicial de 300 km, espesor de corteza
  40 km, mu = 0.55, K1 = 1.0, U = 17 km/s, densidad del proyectil 2800 kg/m3, g = 1.62 m/s2 son parametros de ejemplo.
  Ningun anillo real se usa; no se compara con Orientale ni con otra cuenca.
Modelo (SI salvo donde se indica): (1) recurrencia radial: r_(n+1) = r_n + c sqrt(D_n) con D_n = 2 r_n en km, c = 2.0;
  se contrasta con una progresion geometrica de razon sqrt(2) para el diametro. (2) Estimacion de c por minimos
  cuadrados a partir de anillos sinteticos con ruido gaussiano de 0.3 en c (semilla 20261109). (3) Inversion del
  escalado de C01, R = K1 a (g a/U^2)^(-mu/(2+mu)), por biseccion para hallar el diametro del proyectil a partir del
  diametro transitorio de la cuenca (D_t = D_anillo_principal / 1.0, SUPUESTO ilustrativo) y su energia cinetica.
  (4) propagacion Monte Carlo de la incertidumbre de mu (0.45-0.65 uniforme) a la energia.
Tolerancias: minimos cuadrados recupera c a 0.05; inversion con residuo < 1e-9 relativo.
Limites: sin relajacion viscosa, sin cambio de reologia con la temperatura, sin ley de ensanchamiento para cuencas.
"""
from __future__ import annotations
import math, platform, random

MU, K1, U, RHO_P, G = 0.55, 1.0, 17000.0, 2800.0, 1.62


def anillos(d0_km, c, n):
    r = d0_km / 2
    out = [d0_km]
    for _ in range(n):
        D = 2 * r
        r = r + c * math.sqrt(D)
        out.append(2 * r)
    return out


def radio_trans(a, mu):
    return K1 * a * (G * a / U**2) ** (-mu / (2.0 + mu))


def inferir_a(R, mu):
    lo, hi = 1.0, 1e6
    for _ in range(300):
        mid = math.sqrt(lo * hi)
        if radio_trans(mid, mu) < R:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def energia(a):
    m = RHO_P * 4 / 3 * math.pi * a**3
    return 0.5 * m * U**2


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    ring = anillos(300.0, 2.0, 3)
    print("Anillos SINTETICOS (c=2.0, desde 300 km): " + ", ".join(f"{d:.1f}" for d in ring) + " km")
    print("Razones sucesivas: " + ", ".join(f"{b/a:.3f}" for a, b in zip(ring[:-1], ring[1:])) + "  (sqrt(2)=1.414)")
    geo = [300.0 * math.sqrt(2) ** k for k in range(4)]
    print("Progresion geometrica sqrt(2):  " + ", ".join(f"{d:.1f}" for d in geo) + " km")
    # estimacion de c
    rng = random.Random(20261109)
    obs = []
    d = 300.0
    r = d / 2
    pares = []
    for _ in range(40):
        c_i = rng.gauss(2.0, 0.3)
        D = 2 * r
        r_new = r + c_i * math.sqrt(D)
        pares.append((math.sqrt(D), r_new - r))
        r = r_new if r_new < 2000 else 150.0
    num = sum(x * y for x, y in pares)
    den = sum(x * x for x, y in pares)
    c_est = num / den
    print(f"c estimado por minimos cuadrados (40 espaciados sinteticos, sigma 0.3) = {c_est:.3f} ; verdadero 2.0")
    assert abs(c_est - 2.0) < 0.05
    # energia
    print("Inversion del escalado (cuenca principal de diametro D_p, supuesto D_t = D_p):")
    print(f"{'D_p [km]':>9} {'a [km]':>9} {'E [J]':>11} {'E [Mt TNT]':>12}")
    for Dp in (300.0, 600.0, 1000.0):
        R = Dp / 2 * 1000
        a = inferir_a(R, MU)
        assert abs(radio_trans(a, MU) / R - 1) < 1e-9
        E = energia(a)
        print(f"{Dp:9.0f} {a/1000:9.1f} {E:11.3e} {E/4.184e15:12.3e}")
    # Monte Carlo en mu para 300 km
    es = []
    for _ in range(4000):
        mu = rng.uniform(0.45, 0.65)
        es.append(math.log10(energia(inferir_a(150e3, mu))))
    es.sort()
    print(f"Propagacion de mu en U(0.45,0.65) para D_p=300 km: log10 E [J] mediana {es[len(es)//2]:.2f} ; "
          f"percentiles 5-95 % = {es[int(0.05*len(es))]:.2f}-{es[int(0.95*len(es))]:.2f}")
    # excavacion vs corteza
    for Dp in (300.0, 600.0, 1000.0):
        z = 0.1 * Dp / 2 * 2 / 2  # profundidad de excavacion ~ 0.1 D_t, ILUSTRATIVO
        z = 0.1 * Dp
        print(f"D_p={Dp:.0f} km: profundidad de excavacion ILUSTRATIVA (0.1 D) = {z:.0f} km ; corteza ilustrativa 40 km -> {'excava el manto' if z > 40 else 'queda en la corteza'}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
