#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B71-C14: ecuacion de Kepler M = E - e sin E resuelta con Newton, biseccion y punto fijo; caso hiperbolico.

Datos: ninguno consultado; todos los casos son SINTETICOS (semilla 14). Excentricidades de ejemplo: 0.0935 (valor de la ficha de Marte, NASA/NSSDC, consultada el 2026-11-10),
0.74 (tipo Molniya, sintetica), 0.99 y 0.999 (ilustrativas). 2000 pares (M, e) con e en [0, 0.999] y M en [0, 2 pi).
Sistema: radianes; sin fisica dependiente de marco. Modelo: f(E) = E - e sin E - M = 0.
Segunda via: la solucion de cada metodo se valida sustituyendo en la ecuacion (residuo) y comparando metodos entre si; el caso hiperbolico M = e sinh H - H se valida igual.
Tolerancias: residuo < 1e-12 en Newton con valor inicial adecuado y en biseccion; punto fijo se acepta si converge en <= 500 iteraciones (se cuenta cuantas veces falla);
acuerdo Newton-biseccion < 1e-11 rad; |H| solucion hiperbolica con residuo < 1e-10.
"""
from __future__ import annotations
import math, platform, random


def residuo(E, M, e):
    return E - e * math.sin(E) - M


def newton(M, e, E0, tol=1e-14, maxit=100):
    E = E0
    for k in range(1, maxit + 1):
        d = residuo(E, M, e) / (1 - e * math.cos(E))
        E -= d
        if abs(d) < tol:
            return E, k
    return E, maxit


def biseccion(M, e, tol=1e-14):
    lo, hi = 0.0, 2 * math.pi
    k = 0
    while hi - lo > tol:
        mid = 0.5 * (lo + hi)
        if residuo(mid, M, e) > 0:
            hi = mid
        else:
            lo = mid
        k += 1
    return 0.5 * (lo + hi), k


def punto_fijo(M, e, tol=1e-12, maxit=500):
    E = M
    for k in range(1, maxit + 1):
        En = M + e * math.sin(E)
        if abs(En - E) < tol:
            return En, k, True
        E = En
    return E, maxit, False


def hiperbolico(M, e, tol=1e-14):
    H = math.asinh(M / e) if abs(M / e) < 1e3 else math.copysign(math.log(2 * abs(M) / e + 1.8), M)
    for k in range(1, 200):
        d = (e * math.sinh(H) - H - M) / (e * math.cosh(H) - 1)
        H -= d
        if abs(d) < tol:
            return H, k
    return H, 200


def calcular():
    R = {}
    rnd = random.Random(14)
    casos = [(rnd.uniform(0, 2 * math.pi), rnd.uniform(0, 0.999)) for _ in range(2000)]
    res_n = res_b = dnb = 0.0
    it_n, it_b, it_pf = [], [], []
    fallos_pf = 0
    fallos_n_E0M = 0
    for M, e in casos:
        E0 = M if e < 0.8 else math.pi
        En, kn = newton(M, e, E0)
        Eb, kb = biseccion(M, e)
        Ep, kp, ok = punto_fijo(M, e)
        res_n = max(res_n, abs(residuo(En, M, e)))
        res_b = max(res_b, abs(residuo(Eb, M, e)))
        dnb = max(dnb, abs(En - Eb))
        it_n.append(kn); it_b.append(kb); it_pf.append(kp)
        fallos_pf += (not ok)
        E1, k1 = newton(M, e, M)
        fallos_n_E0M += (abs(residuo(E1, M, e)) > 1e-12)
    R.update(res_n=res_n, res_b=res_b, dnb=dnb, fallos_pf=fallos_pf, fallos_n_E0M=fallos_n_E0M, n_casos=len(casos))
    R["it_n_med"] = sum(it_n) / len(it_n)
    R["it_n_max"] = max(it_n)
    R["it_b"] = it_b[0]
    R["it_pf_med"] = sum(it_pf) / len(it_pf)
    R["it_pf_max"] = max(it_pf)
    # casos concretos
    tabla = []
    for e in (0.0935, 0.74, 0.99, 0.999):
        M = 0.1
        E_pi, k_pi = newton(M, e, math.pi)
        E_m, k_m = newton(M, e, M)
        E_pf, k_pf, ok = punto_fijo(M, e)
        tabla.append((e, E_pi, k_pi, k_m, k_pf, ok, abs(residuo(E_pi, M, e))))
    R["tabla"] = tabla
    # hiperbolico
    peor_h = 0.0
    kmax = 0
    for _ in range(500):
        e = rnd.uniform(1.01, 5.0)
        M = rnd.uniform(-50, 50)
        H, k = hiperbolico(M, e)
        peor_h = max(peor_h, abs(e * math.sinh(H) - H - M) / (1 + abs(M)))
        kmax = max(kmax, k)
    R["res_h"] = peor_h
    R["it_h_max"] = kmax
    return R


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    R = calcular()
    print(f"{R['n_casos']} pares (M, e) SINTETICOS (semilla 14), e en [0, 0.999]")
    print(f"  Newton (E0 = M si e < 0.8, E0 = pi si no): residuo maximo = {R['res_n']:.1e} ; iteraciones medias = {R['it_n_med']:.2f} ; maximas = {R['it_n_max']}")
    print(f"  Biseccion: residuo maximo = {R['res_b']:.1e} ; iteraciones = {R['it_b']} (fijas) ; diferencia maxima con Newton = {R['dnb']:.1e} rad")
    print(f"  Punto fijo: iteraciones medias = {R['it_pf_med']:.1f} ; maximas = {R['it_pf_max']} ; sin converger en 500 iteraciones: {R['fallos_pf']} casos")
    print(f"  Newton con E0 = M para todo e: casos con residuo > 1e-12 = {R['fallos_n_E0M']}")
    print("Caso M = 0.1 rad:  e    E [rad]   iter(E0=pi)  iter(E0=M)  iter(punto fijo)  converge   residuo")
    for e, E, kpi, km, kpf, ok, rs in R["tabla"]:
        print(f"                {e:6.4f} {E:9.6f} {kpi:8d} {km:12d} {kpf:12d}     {'si' if ok else 'no'}     {rs:.1e}")
    print(f"Hiperbolica M = e sinh H - H (500 casos SINTETICOS, e en [1.01, 5], M en [-50, 50]): residuo relativo maximo = {R['res_h']:.1e} ; iteraciones maximas = {R['it_h_max']}")
    assert R["res_n"] < 1e-12 and R["res_b"] < 1e-12 and R["dnb"] < 1e-11
    assert R["res_h"] < 1e-10
    assert R["it_pf_max"] > R["it_n_max"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
