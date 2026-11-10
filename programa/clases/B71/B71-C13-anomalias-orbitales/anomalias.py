#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C13: anomalias verdadera (nu), excentrica (E) y media (M).

Datos consultados (2026-11-10): excentricidad de Marte e = 0.0935 (ficha NASA/NSSDC). Otros valores de e son SINTETICOS/ilustrativos:
e = 0.7402 (orbita tipo Molniya de B71-C08, sintetica), e = 0.9 y 1000 pares aleatorios (semilla 13) con e en [0, 0.95] y nu en [0, 360).
Sistema: angulos en radianes dentro del codigo y en grados en la salida; anomalias medidas desde el periapsis. Dos cuerpos.
Modelo: tan(nu/2) = sqrt((1 + e)/(1 - e)) tan(E/2) ; M = E - e sin E ; E se obtiene de M con Newton (tolerancia 1e-14).
Segunda via: viaje de ida y vuelta nu -> E -> M -> E -> nu en 1000 casos; ecuacion del centro nu - M ~ 2 e sin M + 1.25 e^2 sin 2M frente al calculo exacto;
fraccion del periodo hasta nu = 90 grados: M(nu)/(2 pi) frente a la integral numerica de dt = (r^2/h) d nu (regla del punto medio, 20000 intervalos).
Tolerancias: ida y vuelta < 1e-10 rad (e <= 0.95); serie de 2.o orden frente a exacto < 3 e^3 para e <= 0.2.
"""
from __future__ import annotations
import math, platform, random


def nu_a_E(nu, e):
    return 2 * math.atan2(math.sqrt(1 - e) * math.sin(nu / 2), math.sqrt(1 + e) * math.cos(nu / 2))


def E_a_nu(E, e):
    return 2 * math.atan2(math.sqrt(1 + e) * math.sin(E / 2), math.sqrt(1 - e) * math.cos(E / 2))


def E_a_M(E, e):
    return E - e * math.sin(E)


def M_a_E(M, e):
    M = (M + math.pi) % (2 * math.pi) - math.pi
    E = M + e * math.sin(M) if e < 0.8 else math.pi * (1 if M >= 0 else -1)
    for _ in range(100):
        d = (E - e * math.sin(E) - M) / (1 - e * math.cos(E))
        E -= d
        if abs(d) < 1e-14:
            break
    return E


def wrap(x):
    return (x + math.pi) % (2 * math.pi) - math.pi


def calcular():
    R = {}
    rnd = random.Random(13)
    peor = 0.0
    for _ in range(1000):
        e = rnd.uniform(0.0, 0.95)
        nu = rnd.uniform(-math.pi, math.pi)
        E = nu_a_E(nu, e)
        M = E_a_M(E, e)
        E2 = M_a_E(M, e)
        nu2 = E_a_nu(E2, e)
        peor = max(peor, abs(wrap(nu2 - nu)))
    R["ida_vuelta"] = peor
    # tabla para Marte (e = 0.0935) y e = 0.7402
    for etiq, e in (("m", 0.0935), ("x", 0.7402)):
        filas = []
        for Mdeg in (0, 45, 90, 135, 180):
            M = math.radians(Mdeg)
            E = M_a_E(M, e)
            nu = E_a_nu(E, e)
            filas.append((Mdeg, math.degrees(E % (2 * math.pi)), math.degrees(nu % (2 * math.pi)), math.degrees(wrap(nu - M))))
        R["tabla_" + etiq] = filas
        R["max_centro_" + etiq] = max(abs(f[3]) for f in filas)
    # ecuacion del centro
    e = 0.0935
    peor_serie = 0.0
    for k in range(361):
        M = math.radians(k)
        exacta = E_a_nu(M_a_E(M, e), e) - M
        exacta = wrap(exacta)
        serie = 2 * e * math.sin(M) + 1.25 * e * e * math.sin(2 * M)
        peor_serie = max(peor_serie, abs(exacta - serie))
    R["serie_err"] = peor_serie
    R["serie_cota"] = 3 * e ** 3
    # fraccion del periodo hasta nu = 90 grados
    for etiq, e in (("m", 0.0935), ("x", 0.7402)):
        nu = math.pi / 2
        E = nu_a_E(nu, e)
        M = E_a_M(E, e)
        fr = M / (2 * math.pi)
        # segunda via: integral numerica de dt = (r^2/h) dnu en unidades a = mu = 1 -> T = 2 pi
        p = 1 - e * e
        n = 20000
        suma = 0.0
        for k in range(n):
            x = (k + 0.5) * nu / n
            r = p / (1 + e * math.cos(x))
            suma += r * r / math.sqrt(p) * (nu / n)
        R["fr_" + etiq] = fr
        R["fr_num_" + etiq] = suma / (2 * math.pi)
        R["fr_dif_" + etiq] = abs(fr - R["fr_num_" + etiq])
    # anomalia excentrica media en el tiempo = a ; M_mean
    R["M_90_x_deg"] = math.degrees(E_a_M(nu_a_E(math.pi / 2, 0.7402), 0.7402))
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(f"Ida y vuelta nu -> E -> M -> E -> nu en 1000 casos SINTETICOS (semilla 13, e en [0, 0.95]): error maximo = {R['ida_vuelta']:.2e} rad")
    for etiq, nom in (("m", "e = 0.0935 (Marte, ficha)"), ("x", "e = 0.7402 (sintetica)")):
        print(f"Tabla {nom}:")
        print("    M [deg]   E [deg]   nu [deg]   nu - M [deg]")
        for f in R["tabla_" + etiq]:
            print(f"   {f[0]:7.1f}  {f[1]:9.4f}  {f[2]:9.4f}  {f[3]:11.4f}")
    print(f"Ecuacion del centro (e = 0.0935): error de la serie de 2.o orden = {R['serie_err']:.2e} rad (cota 3 e^3 = {R['serie_cota']:.2e})")
    for etiq, nom in (("m", "e = 0.0935"), ("x", "e = 0.7402")):
        print(f"Fraccion del periodo para ir del periapsis a nu = 90 grados, {nom}: kepleriana {R['fr_' + etiq]:.6f} ; integral numerica {R['fr_num_' + etiq]:.6f} ; dif {R['fr_dif_' + etiq]:.1e}")
    assert R["ida_vuelta"] < 1e-10
    assert R["serie_err"] < R["serie_cota"]
    assert R["fr_dif_m"] < 1e-8 and R["fr_dif_x"] < 1e-8
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
