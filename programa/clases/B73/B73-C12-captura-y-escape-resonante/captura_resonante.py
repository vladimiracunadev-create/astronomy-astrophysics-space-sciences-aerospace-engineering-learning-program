#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B73-C12: captura y escape resonante en el modelo de pendulo con intensidad variable.

Datos: TODOS SINTETICOS (adimensionales). No se usa ningun dato publicado: el modelo es el pendulo H = q^2/2 - eps(t) cos(phi),
con phi' = q y q' = -eps(t) sin(phi); eps(t) es la intensidad de la resonancia (proporcional a la potencia de la excentricidad) y
varia linealmente en el tiempo. Area dentro de la separatriz: A_s = 16 sqrt(eps). Invariante adiabatico de una orbita atrapada: J = area encerrada.
Semilla 73 para los angulos iniciales; paso de tiempo 0.5 (leapfrog); 100 particulas por tasa.
Verificaciones: (a) area de la separatriz por cuadratura frente a 16 sqrt(eps); (b) invariancia de J al aumentar eps lentamente de 0.01 a 0.04
(J calculada con la integral de q(phi) a la energia instantanea, promediada sobre un ciclo); (c) escape cuando A_s(eps) = J: eps* = (J/16)^2 frente a la simulacion (eps baja de 0.04 a 0.0005, phi0 = 2.0);
(d) fraccion de particulas circulantes (q0 = 0.20) capturadas cuando eps crece de 0.001 a 0.04 en T_c = 3000 con una deriva constante nu (q' = -eps sin phi - nu).
Tolerancias: area 1e-6 ; invariancia: error relativo < 0.2 % con T = 1000, 4000 y 16000 ; escape: eps* simulado dentro del 5 % del teorico.
"""
from __future__ import annotations
import json, math, platform, random, sys

DT = 0.5


def energia(phi, q, eps):
    return 0.5 * q * q - eps * math.cos(phi)


def J_de(E, eps, n=4000):
    """Area encerrada por la orbita atrapada de energia E (libracion): 2 * integral de q dphi entre los puntos de retorno."""
    c = -E / eps
    if c >= 1.0 or c <= -1.0:
        raise ValueError("no atrapada")
    phi_m = math.acos(c)
    tot = 0.0
    h = 2 * phi_m / n
    for i in range(n):
        phi = -phi_m + (i + 0.5) * h
        tot += math.sqrt(max(0.0, 2 * (E + eps * math.cos(phi)))) * h
    return 2 * tot


def paso(phi, q, t, eps_fn):
    q -= 0.5 * DT * eps_fn(t) * math.sin(phi)
    phi += DT * q
    q -= 0.5 * DT * eps_fn(t + DT) * math.sin(phi)
    return phi, q


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    out = {"python": platform.python_version()}
    # (a) area de la separatriz
    eps = 0.04
    n = 20000
    h = 2 * math.pi / n
    A = sum(2 * 2 * math.sqrt(eps) * math.cos(-math.pi + (i + 0.5) * h) / 1.0 if False else 0.0 for i in range(1))
    A = 0.0
    for i in range(n):
        phi = -math.pi + (i + 0.5) * h
        A += 2 * 2 * math.sqrt(eps) * math.cos(phi / 2) * h
    print(f"(a) Area de la separatriz para eps = {eps}: cuadratura = {A:.8f} ; 16 sqrt(eps) = {16 * math.sqrt(eps):.8f} ; diferencia = {abs(A - 16 * math.sqrt(eps)):.1e}")
    out["areaA"], out["areaT"], out["areadiff"] = A, 16 * math.sqrt(eps), abs(A - 16 * math.sqrt(eps))
    # (b) invariante adiabatico
    print("(b) Invariante adiabatico: eps crece de 0.01 a 0.04 durante T; J(t=0) frente a J(t=T):")
    res_b = {}
    for T in (1000, 4000, 16000):
        ef = lambda t, T=T: 0.01 + 0.03 * min(t, T) / T
        phi, q = 1.0, 0.0
        E0 = energia(phi, q, ef(0))
        J0 = J_de(E0, ef(0))
        t = 0.0
        for _ in range(int(T / DT)):
            phi, q = paso(phi, q, t, ef)
            t += DT
        # promediar la energia sobre un ciclo con eps constante no hace falta: J se calcula con (E, eps) instantaneos y la fase se promedia con otro ciclo final
        Es = []
        for _ in range(int(120 / DT)):
            phi, q = paso(phi, q, t, ef)
            t += DT
            Es.append(energia(phi, q, ef(t)))
        E1 = sum(Es) / len(Es)
        J1 = J_de(E1, ef(T))
        res_b[T] = abs(J1 / J0 - 1)
        print(f"    T = {T:6d}: J0 = {J0:.5f} ; J(T) = {J1:.5f} ; |dJ/J| = {res_b[T]:.2e} ; E0 = {E0:.5f} -> E = {E1:.5f}")
    out.update(b1000=res_b[1000], b4000=res_b[4000], b16000=res_b[16000])
    # (c) escape
    T = 20000
    ef = lambda t: 0.04 - 0.0395 * min(t, T) / T
    phi, q = 2.0, 0.0
    J0 = J_de(energia(phi, q, ef(0)), ef(0))
    eps_pred = (J0 / 16) ** 2
    t = 0.0
    eps_esc = None
    while t < T:
        phi, q = paso(phi, q, t, ef)
        t += DT
        if abs(phi) > math.pi:
            eps_esc = ef(t)
            break
    print(f"(c) Escape: J0 = {J0:.5f} -> eps* = (J/16)^2 = {eps_pred:.5f} ; eps simulado al cruzar la separatriz = {eps_esc:.5f} ; diferencia relativa = {abs(eps_esc / eps_pred - 1):.2%}")
    out.update(J0c=J0, eps_pred=eps_pred, eps_esc=eps_esc, esc_rel=abs(eps_esc / eps_pred - 1))
    # (d) captura con deriva constante nu (q' = -eps sin phi - nu)
    print("(d) Captura con deriva: 100 particulas circulantes (q0 = +0.20, phi0 uniforme, semilla 73); eps crece de 0.001 a 0.04 en T_c = 3000; q' = -eps sin(phi) - nu:")
    print("    nu          capturadas (rango de phi en los ultimos 400 < 2 pi)")
    rnd = random.Random(73)
    phis0 = [rnd.uniform(-math.pi, math.pi) for _ in range(100)]
    Tc = 3000
    ef = lambda t: 0.001 + 0.039 * min(t, Tc) / Tc
    caps = []
    for nu in (0.0, 3e-4, 1e-3, 3e-3):
        cap = 0
        for p0 in phis0:
            phi, q, t = p0, 0.20, 0.0
            n = int((Tc + 600) / DT)
            lo, hi = 1e9, -1e9
            for i in range(n):
                q -= 0.5 * DT * (ef(t) * math.sin(phi) + nu)
                phi += DT * q
                q -= 0.5 * DT * (ef(t + DT) * math.sin(phi) + nu)
                t += DT
                if i >= n - int(400 / DT):
                    lo, hi = min(lo, phi), max(hi, phi)
            if hi - lo < 2 * math.pi:
                cap += 1
        caps.append(cap / 100)
        print(f"    {nu:8.1e}   {cap / 100:6.2f}")
    out.update(cap0=caps[0], cap1=caps[1], cap2=caps[2], cap3=caps[3])
    assert caps[0] > caps[1] > caps[2] > caps[3]
    assert abs(A - 16 * math.sqrt(eps)) < 1e-6
    assert max(res_b.values()) < 2e-3
    assert abs(eps_esc / eps_pred - 1) < 0.05
    print("Pruebas superadas.")
    return out


if __name__ == "__main__":
    R = main()
    if "--json" in sys.argv:
        print("JSON:" + json.dumps(R))
