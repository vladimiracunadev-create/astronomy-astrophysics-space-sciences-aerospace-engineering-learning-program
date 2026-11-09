#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B61-C02: geometria de un crater simple y balance de volumen.

Datos: SINTETICOS/ILUSTRATIVOS. Relacion profundidad/diametro d/D = 0.20, factor de ensanchamiento
  D_aparente = 1.25 D_transitorio, abultamiento (bulking) del material 1.15 y espesor de brecha de relleno
  son parametros de ejemplo, NO consultados ni medidos; no describen ningun crater real.
Modelo (unidades SI, metros; eje de simetria vertical): el bol es un casquete esferico de profundidad d y
  diametro D. Volumen analitico V = pi d (3 R^2 + d^2)/6 con R = D/2. Segunda via: integracion numerica
  (regla del punto medio, 20 000 anillos) del perfil del casquete z(r) = -(d - (rho - sqrt(rho^2 - r^2))), con rho = (R^2 + d^2)/(2 d).
Balance: el relleno de brecha (lente) ocupa una fraccion f del bol aparente; se halla por biseccion la
  profundidad residual y se comprueba el cierre del volumen. El abultamiento b da un volumen minimo de eyecta (b-1)*V_t.
Tolerancias: volumen numerico frente a analitico 1e-6 relativo; balance de masa 1e-12.
"""
from __future__ import annotations
import math, platform


def volumen_casquete(D, d):
    R = D / 2
    return math.pi * d * (3 * R * R + d * d) / 6


def perfil(r, D, d):
    """Altura del suelo del bol respecto del borde (z=0 en el borde, negativo hacia abajo)."""
    R = D / 2
    rho = (R * R + d * d) / (2 * d)  # radio de curvatura de la esfera
    return -(d - (rho - math.sqrt(rho * rho - r * r)))


def volumen_numerico(D, d, n=20000):
    R = D / 2
    dr = R / n
    v = 0.0
    for i in range(n):
        r = (i + 0.5) * dr
        prof = -perfil(r, D, d)  # profundidad bajo el borde
        v += 2 * math.pi * r * prof * dr
    return v


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    razon = 0.20
    print("Datos sinteticos: d/D = 0.20 ; D_aparente = 1.25 D_transitorio ; bulking 1.15 (no medidos)")
    print(f"{'D_ap [m]':>10} {'d [m]':>8} {'V_analit [m3]':>16} {'V_num [m3]':>16} {'dif rel':>10} {'rho/R':>7}")
    for D in (100.0, 1000.0, 10000.0):
        d = razon * D
        va, vn = volumen_casquete(D, d), volumen_numerico(D, d)
        R = D / 2
        rho = (R * R + d * d) / (2 * d)
        print(f"{D:10.0f} {d:8.1f} {va:16.6e} {vn:16.6e} {abs(vn/va-1):10.2e} {rho/R:7.4f}")
        assert abs(vn / va - 1) < 1e-6
    # balance: V_exc (transitorio) -> bol aparente + relleno de brecha + elevacion del borde
    Dt = 800.0
    Da = 1.25 * Dt
    dt = razon * Dt
    da_ap = razon * Da
    V_t = volumen_casquete(Dt, dt)
    V_a = volumen_casquete(Da, da_ap)
    bulk = 1.15
    # el material excavado, con abultamiento, ocupa bulk*V_t; lo que no cabe en el relleno
    # de brecha y el borde se reparte en: brecha (lente) + elevacion; se define aqui una lente que llena
    # el bol transitorio hasta el bol aparente: V_lente = V_t - V_a si V_t > V_a  (aqui V_a > V_t: el bol crece por colapso del borde)
    V_ens = V_a - V_t
    print(f"Transitorio: D_t={Dt:.0f} m, d_t={dt:.0f} m, V_t={V_t:.4e} m3")
    print(f"Aparente: D_a={Da:.0f} m, d_a={da_ap:.0f} m, V_a={V_a:.4e} m3 ; V_a/V_t={V_a/V_t:.4f}")
    print(f"Volumen extra por ensanchamiento = {V_ens:.4e} m3")
    # relleno de brecha con fraccion f del bol aparente: profundidad real d_real = d_ap*(1-f') (casquete de relleno
    # con la misma geometria): se busca por biseccion la profundidad d_r tal que V(Da,d_ap)-V(Da,d_r)=f*V_a con f=0.25
    f = 0.25
    lo, hi = 0.0, da_ap
    for _ in range(200):
        mid = (lo + hi) / 2
        if volumen_casquete(Da, da_ap) - volumen_casquete(Da, mid) > f * V_a:
            lo = mid
        else:
            hi = mid
    d_real = (lo + hi) / 2
    print(f"Con lente de brecha del 25 % del volumen del bol aparente: profundidad residual = {d_real:.2f} m (d/D={d_real/Da:.4f})")
    cierre = volumen_casquete(Da, da_ap) - volumen_casquete(Da, d_real) - f * V_a
    print(f"Cierre del balance de volumen = {cierre:.3e} m3")
    assert abs(cierre) < 1e-6 * V_a
    # abultamiento: volumen de eyecta depositada fuera del borde minimo
    V_eyecta_min = (bulk - 1) * V_t
    print(f"Volumen minimo de eyecta por abultamiento (bulking {bulk}) = {V_eyecta_min:.4e} m3")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
