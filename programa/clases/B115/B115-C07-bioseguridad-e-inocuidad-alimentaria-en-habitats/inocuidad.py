#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B115-C07: carga microbiana, plan de muestreo y contaminacion de un circuito de solucion nutritiva (SINTETICO).

CONSULTADO (Khodadad et al., 2020, Frontiers in Plant Science; texto leido el 2026-11-10): recuentos totales de bacterias y de
levaduras/mohos de 2.14 a 4.86 log10 UFC/g en lechuga de la ISS; limite de la NASA para alimento no termoestabilizado de
<2x10^4 UFC/g en una muestra o <1x10^4 UFC/g en dos de cinco muestras (Perchonok et al., 2012, segun el articulo), que se aplica a
alimento preenvasado; el articulo senala que NO hay norma para producto fresco cultivado en el espacio; cribado de patogenos
humanos negativo. TODO LO DEMAS ES SINTETICO O ILUSTRATIVO: desviacion entre muestras (0.5 log), prevalencia, volumen del
circuito (40 L), flujo de desinfeccion, reduccion por paso (2 log), crecimiento (duplicacion de 6 h a 20 C con Q10 = 2),
nivel de accion (10^4 UFC/mL), limite de deteccion del ensayo (10^2 UFC/mL), contaminacion inicial (10 UFC/mL), semilla 115.
Unidades: UFC/g, UFC/mL, log10, h, dia. La regla de aceptacion implementada es LECTURA PROPIA del texto citado, NO la norma.
Metodo: (1) escala logaritmica; (2) curva de operacion del plan de 5 muestras (analitica y Monte Carlo); (3) deteccion por
prevalencia; (4) dinamica del circuito (Euler frente a analitica) con umbral de flujo de desinfeccion; (5) probabilidad de que un
evento llegue al nivel de accion antes de ser detectado segun el intervalo de muestreo (Monte Carlo frente a analitica).
Verificacion: Monte Carlo dentro de 1.5 puntos de la analitica; Euler dentro del 1 %. Solo numpy y la biblioteca estandar.
"""
from __future__ import annotations
import math
import platform
import numpy as np

SIGMA_MUESTRAS = 0.5
LIM_A, LIM_B = math.log10(2e4), math.log10(1e4)     # 4.301 y 4.000 log10 UFC/g
V_L, N0, NIVEL_ACCION, LIM_DET = 40.0, 10.0, 1e4, 1e2
LR_PASO, DUPL_20C_H, Q10 = 2.0, 6.0, 2.0


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def prob_aceptar(mu, sigma=SIGMA_MUESTRAS, n=5):
    """Acepta si ninguna muestra >= 2e4 UFC/g y como maximo 1 de las 5 >= 1e4 UFC/g (lectura propia)."""
    q0 = phi((LIM_B - mu) / sigma)
    q1 = phi((LIM_A - mu) / sigma) - q0
    return q0 ** n + n * q0 ** (n - 1) * q1


def mc_aceptar(mu, rng, reps=20000, sigma=SIGMA_MUESTRAS, n=5):
    x = rng.normal(mu, sigma, size=(reps, n))
    ok = (x < LIM_A).all(axis=1) & ((x >= LIM_B).sum(axis=1) <= 1)
    return ok.mean()


def tasa_crecimiento(t_c):
    return math.log(2) / DUPL_20C_H * Q10 ** ((t_c - 20.0) / 10.0)      # 1/h


def tasa_eliminacion(q_lmin):
    return q_lmin * 60.0 / V_L * (1 - 10 ** (-LR_PASO))                  # 1/h


def main():
    rng = np.random.default_rng(115)
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: recuentos y limite de NASA citados por Khodadad et al. (2020, consultado); circuito, desinfeccion y muestreo SINTETICOS")
    print("Escala logaritmica")
    for lg in (2.14, 3.0, 4.0, 4.301, 4.86):
        print(f"   {lg:5.3f} log10 UFC/g = {10**lg:9.0f} UFC/g = {10**lg/2e4:5.2f} veces el limite de 2e4 UFC/g")
    assert abs(LIM_A - 4.30103) < 1e-4

    print("Curva de operacion del plan de 5 muestras (sigma entre muestras = 0.5 log, sintetico)")
    print("   media del lote [log]   P(aceptar) analitica   P(aceptar) Monte Carlo   con lavado de -1 log")
    err = 0.0
    for mu in (2.5, 3.0, 3.25, 3.5, 3.75, 4.0, 4.5):
        a, m = prob_aceptar(mu), mc_aceptar(mu, rng)
        err = max(err, abs(a - m))
        print(f"   {mu:19.2f}   {a*100:20.1f}   {m*100:22.1f}   {prob_aceptar(mu-1.0)*100:19.1f}")
    print(f"   error maximo Monte Carlo frente a analitica = {err*100:.2f} puntos")
    assert err < 0.015

    print("Deteccion por muestreo si la prevalencia de unidades contaminadas es p: n = ln(0.05)/ln(1 - p) para 95 % de confianza")
    for p in (0.10, 0.05, 0.01):
        n = math.log(0.05) / math.log(1 - p)
        print(f"   p = {p*100:4.1f} %: n = {math.ceil(n):4d} unidades; con 5 muestras P(detectar) = {(1-(1-p)**5)*100:5.1f} %")

    print(f"Circuito de {V_L:.0f} L: crecimiento y eliminacion (limite = flujo de desinfeccion que iguala el crecimiento)")
    print("   T[C]  duplicacion[h]  mu[1/h]  eliminacion con 0.1 L/min[1/h]  tasa neta[1/h]  t_deteccion[h]  t_accion[h]  sin desinfeccion t_accion[h]")
    resultados = {}
    for t in (20, 23, 26, 29):
        mu_g = tasa_crecimiento(t)
        kill = tasa_eliminacion(0.1)
        r = mu_g - kill
        td = math.log(LIM_DET / N0) / r if r > 0 else float("inf")
        ta = math.log(NIVEL_ACCION / N0) / r if r > 0 else float("inf")
        ta0 = math.log(NIVEL_ACCION / N0) / mu_g
        resultados[t] = (mu_g, r)
        txt = f"{td:14.1f}  {ta:11.1f}" if r > 0 else "           nunca        nunca"
        print(f"   {t:4d}  {math.log(2)/mu_g:14.2f}  {mu_g:7.4f}  {kill:30.4f}  {r:14.4f}  {txt}  {ta0:28.1f}")
    q_crit = lambda t: tasa_crecimiento(t) * V_L / 60.0 / (1 - 10 ** (-LR_PASO))
    print("   flujo critico de desinfeccion [L/min]: " + ", ".join(f"{t} C -> {q_crit(t):.4f}" for t in (20, 23, 26, 29)))

    # Euler frente a analitica a 23 C, 72 h
    r23 = resultados[23][1]
    n_e, dt = N0, 0.01
    for _ in range(int(72 / dt)):
        n_e += r23 * n_e * dt
    n_a = N0 * math.exp(r23 * 72)
    err_e = abs(math.log10(n_e) - math.log10(n_a)) / abs(math.log10(n_a))
    print(f"Euler (dt = 0.01 h) a 23 C, 72 h: log10 N = {math.log10(n_e):.4f} (analitica {math.log10(n_a):.4f}); error relativo = {err_e:.2e}")
    assert err_e < 0.01

    print("Probabilidad de que un evento de contaminacion llegue al nivel de accion antes de ser detectado (20000 eventos por caso)")
    print("   caso                         intervalo de muestreo[dia]   P(escapa) Monte Carlo   analitica")
    max_err = 0.0
    for nombre, r in (("26 C sin desinfeccion", resultados[26][0]), ("26 C con 0.1 L/min", resultados[26][1]),
                      ("29 C sin desinfeccion", resultados[29][0])):
        td = math.log(LIM_DET / N0) / r
        ta = math.log(NIVEL_ACCION / N0) / r
        for s_d in (1, 3, 7):
            s = 24.0 * s_d
            t0 = rng.uniform(0, 10 * s, size=20000)
            det = np.ceil((t0 + td) / s) * s
            mc = np.mean(det - t0 > ta)
            ana = min(1.0, max(0.0, 1 - (ta - td) / s))
            max_err = max(max_err, abs(mc - ana))
            print(f"   {nombre:28s} {s_d:20d}   {mc*100:20.1f}   {ana*100:9.1f}")
    print(f"   error maximo Monte Carlo frente a analitica = {max_err*100:.2f} puntos")
    assert max_err < 0.015
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
