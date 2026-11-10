#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C10: analisis modal de una viga en voladizo por elementos finitos y masas efectivas.

DATOS ILUSTRATIVOS (no consultados): viga de aluminio de seccion rectangular b = 0,05 m x h = 0,01 m, L = 1,0 m,
E = 69 GPa, rho = 2700 kg/m3. EI = E b h^3/12 = 287,5 N m2; rho A = 1,35 kg/m.
Modelo: elementos de viga de Euler-Bernoulli (masa consistente), 10 elementos, empotrada en x = 0.
Solucion analitica: w_n = (beta_n L)^2 sqrt(EI/(rho A L^4)), con beta_n L = 1,875104; 4,694091; 7,854757 (raices de cos(x) cosh(x) = -1).
Segunda via: las raices se calculan aqui por biseccion de cos(x) cosh(x) + 1 = 0.
Masa efectiva modal (traslacion lateral): M_eff,i = (phi_i^T M r)^2 con phi_i normalizado a masa unitaria y r = 1 en los GDL de desplazamiento y 0 en giros.
Criterio de modo significativo consultado en el GEVS (2021-04-28, p. 2.4-7 del PDF): masa efectiva >= 5 % de la masa total.
Tolerancias: frecuencia del primer modo frente a la analitica < 0,1 %; suma de masas efectivas de todos los modos mas la masa de apoyo (complemento de Schur del nodo empotrado) = masa total a 1e-9.
"""
from __future__ import annotations
import math, platform, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from estructuras_comun import ensamblar_viga, reducir, gen_eig, matvec, solve

E, RHO, B, H, L = 69e9, 2700.0, 0.05, 0.01, 1.0
EI = E * B * H ** 3 / 12
RHOA = RHO * B * H


def raiz_beta(n):
    """n-esima raiz positiva de cos(x) cosh(x) + 1 = 0 por biseccion."""
    f = lambda x: math.cos(x) * math.cosh(x) + 1
    a, b = (n - 0.5) * math.pi, (n + 0.5) * math.pi
    # La raiz esta cerca de (n-1/2) pi; busca cambio de signo en [a-0.5, a+0.5]
    lo, hi = a - 0.6, a + 0.6
    if f(lo) * f(hi) > 0:
        raise RuntimeError("sin cambio de signo")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    n = 10
    K, M = ensamblar_viga(n, L, EI, RHOA)
    libres = list(range(2, 2 * (n + 1)))  # empotrada: se eliminan w0 y th0
    Kr, Mr = reducir(K, libres), reducir(M, libres)
    lam, phi = gen_eig(Kr, Mr)
    f_fe = [math.sqrt(max(l, 0)) / (2 * math.pi) for l in lam]
    masa = RHOA * L
    print(f"Viga ILUSTRATIVA: EI = {EI:.2f} N m2, rho A = {RHOA:.3f} kg/m, masa total = {masa:.3f} kg, {n} elementos")
    print(" modo   beta L    f analitica [Hz]   f FE [Hz]   error [%]   Meff [kg]   Meff/M [%]  significativo (>=5 %)")
    # vector de traslacion rigida de la base: 1 en todos los GDL de desplazamiento (indices pares), 0 en giros; se usa la masa COMPLETA
    # (incluye el acoplamiento con el nodo empotrado) para que la suma de masas efectivas sea la masa total
    rfull = [1.0 if i % 2 == 0 else 0.0 for i in range(2 * (n + 1))]
    Mfull_r = matvec(M, rfull)
    Mr_r = [Mfull_r[i] for i in libres]
    tot = 0.0
    errs = []
    for k in range(6):
        bl = raiz_beta(k + 1)
        fa = bl ** 2 / (2 * math.pi) * math.sqrt(EI / (RHOA * L ** 4))
        gam = sum(phi[i][k] * Mr_r[i] for i in range(len(libres)))
        me = gam ** 2
        errs.append((f_fe[k] - fa) / fa * 100)
        print(f"  {k + 1}   {bl:7.4f}   {fa:14.3f}   {f_fe[k]:10.3f}   {errs[-1]:8.4f}   {me:9.4f}   {me / masa * 100:9.3f}   {'si' if me / masa >= 0.05 else 'no'}")
    for k in range(len(libres)):
        gam = sum(phi[i][k] * Mr_r[i] for i in range(len(libres)))
        tot += gam ** 2
    # masa 'de apoyo': complemento de Schur de la masa del nodo empotrado, S = M00 - M0f Mff^-1 Mf0 (masa que se mueve con la base)
    m0f = [M[0][j] for j in libres]
    S = M[0][0] - sum(a * b for a, b in zip(m0f, solve(Mr, m0f)))
    print(f"Suma de masas efectivas de los {len(libres)} modos = {tot:.9f} kg ; masa de apoyo (Schur) = {S:.9f} kg ; suma = {tot + S:.9f} kg (masa total {masa:.9f} kg)")
    # Convergencia del modo 1 con la malla
    print("Convergencia del modo 1 con el numero de elementos:")
    fa1 = raiz_beta(1) ** 2 / (2 * math.pi) * math.sqrt(EI / (RHOA * L ** 4))
    for ne in (1, 2, 4, 8, 16):
        Kk, Mm = ensamblar_viga(ne, L, EI, RHOA)
        li = list(range(2, 2 * (ne + 1)))
        l2, _ = gen_eig(reducir(Kk, li), reducir(Mm, li))
        print(f"  ne = {ne:2d}  f1 = {math.sqrt(l2[0]) / (2 * math.pi):9.4f} Hz  error = {(math.sqrt(l2[0]) / (2 * math.pi) - fa1) / fa1 * 100:9.5f} %")
    assert abs(errs[0]) < 0.1
    assert abs(tot + S - masa) < 1e-9
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
