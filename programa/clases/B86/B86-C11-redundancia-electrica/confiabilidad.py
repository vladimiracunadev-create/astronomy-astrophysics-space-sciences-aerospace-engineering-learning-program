#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B86-C11: confiabilidad de arquitecturas redundantes de un regulador de potencia SINTETICO.

Datos consultados (2026-11-10): ninguno numerico. Se cita la ficha de ECSS-E-ST-20C Rev.2 (solo existencia, fecha y alcance; no se leyo su texto).
ILUSTRATIVOS (sinteticos, no medidos): tasa de falla de una unidad lambda = 5.0e-6 por hora (constante, modelo exponencial), mision de 5 anos = 43830 h,
probabilidad de conmutacion correcta de la redundancia fria 0.99, factor de causa comun beta = 0.10, semilla 20261110 y 400000 muestras.
Modelo: R(t) = exp(-lambda t); paralelo activo R = 2R - R^2; reserva fria con conmutacion perfecta R = e^{-lt}(1 + lt) y con probabilidad p: R = e^{-lt}(1 + p l t);
2 de 3: R = 3R^2 - 2R^3; paralelo con causa comun: R = exp(-beta l t) [2 e^{-(1-beta) l t} - e^{-2 (1-beta) l t}].
Segunda via: simulacion Monte Carlo de tiempos de falla exponenciales con semilla fija.
Tolerancia: diferencia Monte Carlo - analitico menor que 4 desviaciones tipicas binomiales; MTTF simulado a menos de 1 % del analitico.
"""
from __future__ import annotations
import math, platform, random

LAM, T, P_SW, BETA = 5.0e-6, 5.0 * 8766.0, 0.99, 0.10
N, SEMILLA = 400_000, 20261110


def analitico():
    r = math.exp(-LAM * T)
    lt = LAM * T
    return dict(
        simple=r,
        paralelo=2.0 * r - r * r,
        fria=r * (1.0 + lt),
        fria_imp=r * (1.0 + P_SW * lt),
        dos_de_tres=3.0 * r * r - 2.0 * r ** 3,
        causa_comun=math.exp(-BETA * lt) * (2.0 * math.exp(-(1.0 - BETA) * lt) - math.exp(-2.0 * (1.0 - BETA) * lt)),
    )


def montecarlo():
    rng = random.Random(SEMILLA)
    cnt = dict.fromkeys(("simple", "paralelo", "fria", "fria_imp", "dos_de_tres", "causa_comun"), 0)
    suma = dict.fromkeys(("simple", "paralelo", "fria", "dos_de_tres"), 0.0)
    for _ in range(N):
        a, b, c = (rng.expovariate(LAM) for _ in range(3))
        cnt["simple"] += a > T
        cnt["paralelo"] += max(a, b) > T
        # reserva fria: el segundo equipo arranca cuando falla el primero; si la conmutacion falla, falla el sistema
        cnt["fria"] += (a + b) > T
        cnt["fria_imp"] += (a > T) or ((a + b) > T and rng.random() < P_SW)
        cnt["dos_de_tres"] += sorted((a, b, c))[1] > T
        cc = rng.expovariate(BETA * LAM)
        i1, i2 = rng.expovariate((1.0 - BETA) * LAM), rng.expovariate((1.0 - BETA) * LAM)
        cnt["causa_comun"] += min(cc, max(i1, i2)) > T
        suma["simple"] += a
        suma["paralelo"] += max(a, b)
        suma["fria"] += a + b
        suma["dos_de_tres"] += sorted((a, b, c))[1]
    mc = {k: v / N for k, v in cnt.items()}
    mttf = {k: v / N for k, v in suma.items()}
    return mc, mttf


def resultados():
    an = analitico()
    mc, mttf = montecarlo()
    sig = {k: math.sqrt(an[k] * (1.0 - an[k]) / N) for k in an}
    z = {k: (mc[k] - an[k]) / sig[k] for k in an}
    mttf_an = dict(simple=1.0 / LAM, paralelo=1.5 / LAM, fria=2.0 / LAM, dos_de_tres=5.0 / (6.0 * LAM))
    r = dict(lt=LAM * T, T=T, MTBF_h=1.0 / LAM, MTBF_anos=1.0 / LAM / 8766.0)
    for k in an:
        r[f"R_{k}"], r[f"MC_{k}"], r[f"sig_{k}"], r[f"z_{k}"] = an[k], mc[k], sig[k], z[k]
        r[f"Q_{k}"] = 1.0 - an[k]
    for k in mttf_an:
        r[f"MTTF_{k}"], r[f"MTTFmc_{k}"] = mttf_an[k], mttf[k]
        r[f"errM_{k}"] = abs(mttf[k] - mttf_an[k]) / mttf_an[k] * 100.0
    r["ganancia_par"] = r["Q_simple"] / r["Q_paralelo"]
    r["perdida_cc"] = r["Q_causa_comun"] / r["Q_paralelo"]
    r["ganancia_cc"] = r["Q_simple"] / r["Q_causa_comun"]
    r["q2"] = r["Q_simple"] ** 2
    r["Rs"] = r["R_simple"] ** 2
    r["p_igual"] = ((r["R_paralelo"] / r["R_simple"]) - 1.0) / r["lt"]
    r["R_dobla"] = math.exp(-2.0 * LAM * T)
    return r


def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = resultados()
    print(f"Unidad SINTETICA: lambda = {LAM:.1e} /h (MTBF = {r['MTBF_h']:.0f} h = {r['MTBF_anos']:.2f} anos) ; mision = {T:.0f} h (5 anos) ; lambda t = {r['lt']:.4f}")
    print(f"Monte Carlo: {N} muestras, semilla {SEMILLA}")
    print(" arquitectura           R analitica   R Monte Carlo   sigma      z")
    nombres = dict(simple="una unidad", paralelo="paralelo activo", fria="reserva fria perfecta", fria_imp="reserva fria p = 0.99", dos_de_tres="2 de 3", causa_comun="paralelo con causa comun")
    for k, n in nombres.items():
        print(f" {n:<24} {r[f'R_{k}']:.6f}    {r[f'MC_{k}']:.6f}     {r[f'sig_{k}']:.6f}  {r[f'z_{k}']:+.2f}")
    print(f"Probabilidad de falla: una unidad = {r['Q_simple']:.5f} ; paralelo = {r['Q_paralelo']:.5f} (mejora x{r['ganancia_par']:.1f}) ; con causa comun beta = {BETA} = {r['Q_causa_comun']:.5f} ({r['perdida_cc']:.1f} veces la del paralelo ideal)")
    print(" MTTF [h]       analitico     Monte Carlo   dif [%]")
    for k, n in (("simple", "una unidad"), ("paralelo", "paralelo activo"), ("fria", "reserva fria"), ("dos_de_tres", "2 de 3")):
        print(f" {n:<14} {r[f'MTTF_{k}']:11.0f}   {r[f'MTTFmc_{k}']:11.0f}   {r[f'errM_{k}']:.3f}")
    for k in nombres:
        assert abs(r[f"z_{k}"]) < 4.0, k
    for k in ("simple", "paralelo", "fria", "dos_de_tres"):
        assert r[f"errM_{k}"] < 1.0, k
    assert r["R_paralelo"] > r["R_simple"] and r["R_causa_comun"] < r["R_paralelo"]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
