#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B84-C24: factores de seguridad, margenes estructurales y probabilidad de falla implicita.

Datos CONSULTADOS (2026-11-10): GEVS (GSFC-STD-7000B, 2021-04-28), Tabla 2.2-3, factores aplicados a cargas limite (columna estatica): metalico fluencia 1,25 y ultima 1,4;
estabilidad ultima 1,4; berilio fluencia 1,4 y ultima 1,6; compuesto ultima 1,5; union adhesiva/inserto ultima 1,5. Columna aleatoria/acustica: metalico 1,6 y 1,8;
compuesto 1,9. El estandar tambien da 2,0 (fluencia) y 2,6 (ultima) si solo se califica por analisis. La ficha de ECSS-E-ST-32-10C Rev. 1 (2026-11-10) confirma que ECSS
define factores de seguridad deterministas y una alternativa probabilista aprobada por el cliente; sus valores NO se consultaron.
DATOS ILUSTRATIVOS (no consultados): miembros con carga limite y capacidad; coeficientes de variacion de la resistencia v_R = 0,08 y de la carga v_S = 0,20 (lognormales).
Definicion: MS = capacidad_admisible/(FS x carga_limite) - 1.
Probabilidad de falla implicita: la capacidad admisible es el percentil 5 % de la resistencia (lognormal) y la carga limite el percentil 99 % de la carga (lognormal);
el diseno cumple R_5 = FS S_99; P_f = P(R < S) = Phi(-(ln mR - ln mS)/sqrt(sR^2 + sS^2)) con medianas mR, mS y sR = sqrt(ln(1+vR^2)).
Segunda via: Monte Carlo (400000 muestras, semilla 84024) para FS = 1,0 y 1,25. Tolerancia: P_f analitica frente a Monte Carlo dentro de 3 errores estandar binomiales.
"""
from __future__ import annotations
import math, platform, random

VR, VS = 0.08, 0.20
SR, SS = math.sqrt(math.log(1 + VR ** 2)), math.sqrt(math.log(1 + VS ** 2))


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def pf(fs):
    # S99 = 1 (unidad de carga): mS = exp(-2,326 sS); R5 = fs: mR = fs exp(1,645 sR)
    lnmS = -2.3263 * SS
    lnmR = math.log(fs) + 1.6449 * SR
    return phi(-(lnmR - lnmS) / math.sqrt(SR ** 2 + SS ** 2))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Factores de seguridad del GEVS (Tabla 2.2-3, estatico): metalico 1,25/1,4; compuesto 1,5; union adhesiva 1,5; estabilidad 1,4")
    miembros = (("Larguero Al (fluencia)", 8200.0, 14500.0, 1.25), ("Larguero Al (ultima)", 8200.0, 16400.0, 1.4),
                ("Panel CFRP (ultima)", 5600.0, 9800.0, 1.5), ("Union adhesiva (ultima)", 1900.0, 2700.0, 1.5),
                ("Columna (pandeo, estabilidad)", 3100.0, 4200.0, 1.4), ("Larguero Al (aleatoria, ultima)", 4000.0, 8200.0, 1.8))
    print(f"{'miembro (datos ILUSTRATIVOS)':34s} {'carga lim. [N]':>14s} {'capacidad [N]':>14s} {'FS':>5s} {'MS':>8s}")
    for n, c, cap, fs in miembros:
        ms = cap / (fs * c) - 1
        print(f"{n:34s} {c:14.0f} {cap:14.0f} {fs:5.2f} {ms:8.3f}  {'positivo' if ms >= 0 else 'NEGATIVO'}")
    print("Probabilidad de falla implicita (resistencia: percentil 5 %, v_R = 0,08; carga: percentil 99 %, v_S = 0,20; lognormales):")
    print(f"{'FS':>5s} {'P_f analitica':>15s} {'indice beta':>12s}")
    for fs in (1.0, 1.25, 1.4, 1.5, 2.0):
        p = pf(fs)
        # indice de fiabilidad beta = -Phi^-1(p): se resuelve por biseccion
        lo, hi = 0.0, 12.0
        for _ in range(200):
            mid = 0.5 * (lo + hi)
            if phi(-mid) > p:
                lo = mid
            else:
                hi = mid
        print(f"{fs:5.2f} {p:15.3e} {0.5 * (lo + hi):12.3f}")
    rng = random.Random(84024)
    print("Comprobacion por Monte Carlo (400000 muestras):")
    for fs in (1.0, 1.25):
        lnmS = -2.3263 * SS
        lnmR = math.log(fs) + 1.6449 * SR
        n = 400000
        f = 0
        for _ in range(n):
            if lnmR + SR * rng.gauss(0, 1) < lnmS + SS * rng.gauss(0, 1):
                f += 1
        pa = pf(fs)
        print(f"  FS = {fs:4.2f}: P_f MC = {f / n:.4e} ; analitica = {pa:.4e} ; dif relativa = {abs(f / n - pa) / pa * 100:.2f} %")
        assert abs(f / n - pa) < 3 * math.sqrt(pa * (1 - pa) / n)
    assert pf(1.4) < pf(1.25) < pf(1.0)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
