#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B110-C03: tiempo disponible (ASET) frente a tiempo necesario (RSET) para llegar a un refugio.

CONSULTADO (2026-11-10): (a) principio de «camino libre» al vehiculo de retorno: no se cierra una escotilla entre el tripulante y su vehiculo,
porque la diferencia de presion puede impedir reabrirla; (b) todo modulo puede ser refugio si da acceso libre al vehiculo de retorno y aire respirable;
(c) presion minima de 490 mmHg y regla de retirada con T_Res <= 10 min; (d) Orion: un solo volumen y sin vehiculo de escape aparte
(Tobias y McMillan, SpaceOps 2023, NASA JSC).
ILUSTRATIVOS (sinteticos, no medidos, no son tiempos de ningun entrenamiento ni nave): cabina de 100 m3 a 101 kPa con un orificio de 10-40 mm
(modelo de C01), tiempos de deteccion, reunion, traslado, paso por escotilla y verificacion de cierre (lognormales con la mediana y GSD indicadas),
tripulacion de 2 a 6, escotilla de 0,8 m de diametro y una fuerza maxima ILUSTRATIVA de 500 N para reabrirla.
Modelo: ASET = T_Res(d) de C01 (flujo estrangulado, cabina isoterma); RSET = deteccion + max(reunion) + traslado + N * paso por escotilla + verificacion.
Margen = ASET - RSET. Tolerancias: Monte Carlo sin varianza = formula determinista (1e-9); semilla fija 110; 20000 corridas.
Contenido educativo: NO es un procedimiento de evacuacion.
"""
from __future__ import annotations
import math, platform, random

R_ESP, GAMMA, T, CD = 287.05, 1.4, 293.15, 0.8
PSI = (2.0 / (GAMMA + 1.0)) ** ((GAMMA + 1.0) / (2.0 * (GAMMA - 1.0)))
MMHG = 101325.0 / 760.0
P0, PMIN, V = 101.0e3, 490.0 * MMHG, 100.0


def tau(v, d):
    return v / (CD * math.pi * d * d / 4.0 * PSI * math.sqrt(GAMMA * R_ESP * T))


def aset(d, v=V):
    return tau(v, d) * math.log(P0 / PMIN)


# (mediana [s], GSD) de cada fase, ILUSTRATIVOS
DET = (20.0, 1.5)
REU = (60.0, 1.5)
TRAS = (90.0, 1.3)
PASO = (20.0, 1.3)
VERIF = (120.0, 1.4)


def muestra(rng, par, var=True):
    med, gsd = par
    return med * math.exp(rng.gauss(0.0, math.log(gsd))) if var else med


def rset(rng, n, var=True):
    det = muestra(rng, DET, var)
    reu = max(muestra(rng, REU, var) for _ in range(n))
    tras = muestra(rng, TRAS, var)
    paso = sum(muestra(rng, PASO, var) for _ in range(n))
    ver = muestra(rng, VERIF, var)
    return det + reu + tras + paso + ver


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Cabina ILUSTRATIVA V = {V:.0f} m3, P0 = {P0/1e3:.0f} kPa, P_min = 490 mmHg (consultado); tiempos de las fases ILUSTRATIVOS")
    # verificacion: sin varianza, RSET = formula determinista
    rng = random.Random(110)
    n = 4
    det = DET[0] + REU[0] + TRAS[0] + n * PASO[0] + VERIF[0]
    r0 = rset(rng, n, var=False)
    print(f"RSET determinista (n = {n}): formula = {det:.1f} s ; simulacion sin varianza = {r0:.1f} s")
    assert abs(r0 - det) < 1e-9
    print("ASET por diametro de orificio (T_Res de la clase C01):")
    for dmm in (10, 20, 30, 40):
        print(f"  d = {dmm:2d} mm  ASET = {aset(dmm/1000)/60:7.2f} min")
    print(" d [mm]  n   RSET mediana [min]  [P5; P95]    margen mediano [min]   P(margen < 0)   P(margen < 10 min)")
    res = {}
    for dmm in (10, 20, 30, 40):
        a = aset(dmm / 1000)
        for n in (2, 4, 6):
            rng = random.Random(110)
            rs = sorted(rset(rng, n) for _ in range(20000))
            mar = [a - x for x in rs]
            pneg = sum(1 for m in mar if m < 0) / len(mar)
            p10 = sum(1 for m in mar if m < 600.0) / len(mar)
            res[(dmm, n)] = pneg
            if n in (2, 4, 6):
                print(f" {dmm:5d} {n:3d} {rs[len(rs)//2]/60:14.2f}  [{rs[int(0.05*len(rs))]/60:5.2f}; {rs[int(0.95*len(rs))]/60:5.2f}] {(a-rs[len(rs)//2])/60:15.2f} {pneg:16.4f} {p10:18.4f}")
    # camino libre: tiempo hasta que una escotilla cerrada no se pueda reabrir
    area = math.pi * 0.8 ** 2 / 4.0
    dp_max = 500.0 / area
    print(f"Escotilla de 0,8 m: area {area:.3f} m2; fuerza maxima ILUSTRATIVA 500 N => dP maximo reabrible = {dp_max:.0f} Pa = {dp_max/MMHG:.1f} mmHg")
    print("Tiempo desde el cierre hasta que dP supera ese valor (fuga de 10 mm en el volumen del lado que pierde):")
    for vv in (100.0, 30.0, 10.0):
        t = -tau(vv, 0.010) * math.log(1.0 - dp_max / P0)
        print(f"  volumen del lado que pierde = {vv:5.0f} m3 -> {t:6.1f} s")
    assert res[(10, 2)] < 0.001 and res[(40, 6)] > 0.99
    assert res[(20, 6)] >= res[(20, 4)] >= res[(20, 2)]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
