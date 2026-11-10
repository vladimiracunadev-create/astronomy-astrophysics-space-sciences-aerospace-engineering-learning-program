#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B97-C22: deteccion autonoma de eventos con CUSUM en una serie de presion sintetica.

Dato consultado (2026-11-10): presion media de superficie de Marte 6.36 mb (636 Pa) en el radio medio, con variacion estacional de 4.0 a 8.7 mb (NASA/NSSDC); se usa 636 Pa como linea base.
ILUSTRATIVOS (sinteticos, no medidos): ruido blanco gaussiano de 0.30 Pa a 1 muestra/s; eventos tipo caida de presion con perfil gaussiano de ancho 5 s y amplitudes de 0.6 y 3.0 Pa;
CUSUM unilateral con k = 0.5 sigma y h = 4 sigma; umbral simple de 3 sigma; semilla fija. NO es una serie medida ni el modelo de un remolino de polvo real.
Modelo: S_t = max(0, S_{t-1} + (mu0 - x_t)/sigma - k); alarma si S_t > h. ARL0 = longitud media hasta una falsa alarma sin evento.
Segunda via: aproximacion de Siegmund, ARL0 = (exp(2 k b) - 2 k b - 1)/(2 k^2) con b = h + 1.166 (resultado estandar, no consultado en una fuente concreta), frente a Monte Carlo (tolerancia 10 %).
Unidades: Pa y segundos. Sin deriva de linea base, sin correlacion temporal del ruido ni efecto del ciclo diurno.
"""
from __future__ import annotations
import math, platform, random

MU0, SIGMA, K, H, ANCHO, SEMILLA = 636.0, 0.30, 0.5, 4.0, 5.0, 20261110               # MU0 consultado; resto ILUSTRATIVO
NARL, NEV = 3000, 2000


def longitud_hasta_alarma(rng, tope=200000):
    s, t = 0.0, 0
    while t < tope:
        t += 1
        s = max(0.0, s + (MU0 - (MU0 + rng.gauss(0, SIGMA))) / SIGMA - K)
        if s > H:
            return t
    return tope


def evento(rng, amp, cusum=True):
    """Devuelve (retardo respecto del inicio del evento en s, detectado). Inicio = centro - 2 anchos; ventana de deteccion hasta centro + 3 anchos.
    Las alarmas antes del inicio son falsas alarmas: se descartan y el acumulador se reinicia."""
    t0 = 100                                   # centro del evento
    inicio, fin = t0 - 2 * ANCHO, t0 + 3 * ANCHO
    s = 0.0
    for t in range(1, 300):
        x = MU0 + rng.gauss(0, SIGMA) - amp * math.exp(-0.5 * ((t - t0) / ANCHO) ** 2)
        if cusum:
            s = max(0.0, s + (MU0 - x) / SIGMA - K)
            alarma = s > H
        else:
            alarma = (MU0 - x) / SIGMA > 3.0
        if alarma:
            if t < inicio:
                s = 0.0
                continue
            if t <= fin:
                return t - inicio, True
            return None, False
    return None, False


def calc():
    rng = random.Random(SEMILLA)
    arl0 = sum(longitud_hasta_alarma(rng) for _ in range(NARL)) / NARL
    b = H + 1.166
    arl_teo = (math.exp(2 * K * b) - 2 * K * b - 1) / (2 * K * K)
    # umbral simple: probabilidad de falsa alarma por muestra = 1 - Phi(3)
    p3 = 0.5 * math.erfc(3 / math.sqrt(2))
    res = {}
    for amp in (0.6, 3.0):
        for cus in (True, False):
            det, retardos = 0, []
            for _ in range(NEV):
                d, ok = evento(rng, amp, cus)
                if ok:
                    det += 1; retardos.append(d)
            res[(amp, cus)] = (det / NEV, sum(retardos) / len(retardos) if retardos else float("nan"))
    return dict(arl0=arl0, arl_teo=arl_teo, rel=abs(arl0 - arl_teo) / arl_teo, arl_umbral=1 / p3, res=res,
                p_c_06=res[(0.6, True)][0], p_u_06=res[(0.6, False)][0], p_c_30=res[(3.0, True)][0], p_u_30=res[(3.0, False)][0],
                d_c_06=res[(0.6, True)][1], d_c_30=res[(3.0, True)][1], d_u_30=res[(3.0, False)][1], falsas_hora=3600.0 / arl0, falsas_hora_u=3600.0 * p3)


def main():
    r = calc()
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Serie SINTETICA: base {MU0:.0f} Pa (consultada), ruido {SIGMA} Pa a 1 Hz; CUSUM k = {K} sigma, h = {H} sigma; evento gaussiano de {ANCHO:.0f} s; semilla {SEMILLA}")
    print(f"ARL0 (falsa alarma) CUSUM: Monte Carlo = {r['arl0']:.1f} s; Siegmund = {r['arl_teo']:.1f} s (diferencia {100*r['rel']:.1f} %); umbral simple de 3 sigma: {r['arl_umbral']:.0f} s")
    print(f"Falsas alarmas por hora: CUSUM {r['falsas_hora']:.2f}; umbral simple {r['falsas_hora_u']:.2f}")
    print(" amplitud [Pa]  metodo    deteccion   retardo medio desde el inicio [s]")
    for (amp, cus), (p, d) in r["res"].items():
        print(f"{amp:12.1f}  {'CUSUM' if cus else 'umbral':8s} {100*p:9.1f} % {d:15.2f}")
    assert r["rel"] < 0.10 and r["p_c_06"] > r["p_u_06"] and r["p_c_30"] > 0.99
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
