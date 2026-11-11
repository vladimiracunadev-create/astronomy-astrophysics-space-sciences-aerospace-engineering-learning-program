#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C06: problema abierto con una curva de luz SINTETICA de transito (profundidad, periodo, radio relativo).

CONTENIDO EDUCATIVO. NO es una observacion: la curva de luz se genera aqui con un modelo de caja y ruido gaussiano (semilla 131).
CONSULTADOS (2026-11-11): IAU 2015 B3 (PDF leido): radio solar nominal 6.957e8 m y radio ecuatorial terrestre nominal 6.3781e6 m (para pasar a radios).
ILUSTRATIVOS: periodo inyectado 3.2 d, Rp/Rs inyectado 0.10, duracion 0.12 d, ruido 0.002 (relativo) por punto, cadencia 30 min, 30 d, estrella de
1 radio solar nominal. Unidades: tiempo en dias, flujo relativo (1 = sin transito).
Metodo: ajuste de caja con barrido de periodos (BLS simplificado) y, como segunda via, mediana dentro frente a fuera del transito.
Tolerancias: periodo recuperado dentro de 0.01 d; profundidad dentro del 10 % relativo del valor inyectado.
"""
from __future__ import annotations
import math, platform, random, statistics

P_INY, K_INY, DUR, SIG, CAD, T_TOT = 3.2, 0.10, 0.12, 0.002, 30 / 1440, 30.0
T0 = 1.1


def curva(seed=131):
    rng = random.Random(seed)
    n = int(T_TOT / CAD)
    t = [i * CAD for i in range(n)]
    f = []
    for ti in t:
        ph = ((ti - T0) % P_INY)
        en = ph < DUR / 2 or ph > P_INY - DUR / 2
        f.append(1 - K_INY ** 2 * en + rng.gauss(0, SIG))
    return t, f


def caja(t, f, per, dur, sd):
    """Mejor profundidad y fase para un periodo de prueba; devuelve (estadistico, profundidad, t0)."""
    nb = max(8, int(per / (dur / 2)))
    sumas, cuentas = [0.0] * nb, [0] * nb
    for ti, fi in zip(t, f):
        b = int(((ti % per) / per) * nb) % nb
        sumas[b] += fi
        cuentas[b] += 1
    media_global = sum(f) / len(f)
    mejor = (0.0, 0.0, 0)
    ancho = max(1, int(round(dur / per * nb)))
    for b0 in range(nb):
        s = c = 0
        for j in range(ancho):
            s += sumas[(b0 + j) % nb]
            c += cuentas[(b0 + j) % nb]
        if c == 0:
            continue
        prof = media_global - s / c
        stat = prof * math.sqrt(c) / sd
        if stat > mejor[0]:
            mejor = (stat, prof, b0)
    return mejor


def main():
    global SIG
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Curva SINTETICA (modelo de caja + ruido gaussiano, semilla 131); radios nominales IAU 2015 B3 CONSULTADOS; parametros ILUSTRATIVOS.")
    t, f = curva()
    n = len(t)
    print(f"Puntos: {n} ; cadencia {CAD * 1440:.0f} min ; duracion {T_TOT:.0f} d ; ruido {SIG}")
    print(f"Inyectado: P = {P_INY} d ; Rp/Rs = {K_INY} ; profundidad = {K_INY ** 2:.4f} ; duracion = {DUR} d")
    # barrido de periodos
    mejor = (0.0, None, None)
    sdf = statistics.pstdev(f)
    p = 1.0
    while p <= 8.0:
        stat, prof, b0 = caja(t, f, p, DUR, statistics.pstdev(f))
        if stat > mejor[0]:
            mejor = (stat, p, prof)
        p += 0.002
    stat, p_rec, prof_rec = mejor
    print(f"Barrido 1.0-8.0 d (paso 0.002 d): mejor periodo = {p_rec:.3f} d ; profundidad de caja = {prof_rec:.5f} ; SNR del mejor periodo = {stat:.1f}")
    # segunda via: mediana en transito frente a fuera
    en, fuera = [], []
    for ti, fi in zip(t, f):
        ph = ((ti - T0) % p_rec)
        (en if ph < DUR / 2 or ph > p_rec - DUR / 2 else fuera).append(fi)
    prof2 = statistics.median(fuera) - statistics.median(en)
    print(f"Segunda via (mediana fuera - mediana dentro, con el periodo recuperado): profundidad = {prof2:.5f} ({len(en)} puntos dentro)")
    k_rec = math.sqrt(max(prof_rec, 0))
    print(f"Rp/Rs recuperado = {k_rec:.4f} (inyectado {K_INY}) ; error relativo {100 * (k_rec / K_INY - 1):+.1f} %")
    rp = k_rec * 6.957e8 / 6.3781e6
    print(f"Radio del planeta SINTETICO = {rp:.1f} radios terrestres nominales (para Rs = 1 radio solar nominal) = {rp / 11.2:.2f} Jupiter aprox.")
    snr = prof_rec / SIG * math.sqrt(len(en))
    print(f"Relacion senal/ruido del transito apilado = {snr:.1f}")
    # sensibilidad: que ruido impide la deteccion
    print("Sensibilidad al ruido (periodo recuperado, SNR del mejor periodo):")
    sig0 = SIG
    for s in (0.002, 0.01, 0.03):
        SIG = s
        tt, ff = curva()
        mj = (0.0, None, None)
        pp = 2.0
        while pp <= 5.0:
            stt, pr, b0 = caja(tt, ff, pp, DUR, statistics.pstdev(ff))
            if stt > mj[0]:
                mj = (stt, pp, pr)
            pp += 0.005
        print(f"  ruido {s:.3f}: periodo {mj[1]:.3f} d ; SNR {mj[0]:.1f}")
    SIG = sig0
    assert abs(p_rec - P_INY) < 0.01
    assert abs(prof_rec / K_INY ** 2 - 1) < 0.10
    assert abs(prof2 / K_INY ** 2 - 1) < 0.10
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
