#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B92-C08: presupuesto de margen, desvanecimiento conjunto y disponibilidad con varias estaciones.

Datos consultados (2026-11-10), Israel et al., SPIE 2024 (NTRS 20230018608), experimento LCRD hasta el 6-dic-2023:
disponibilidad independiente del clima de la carga util 99.3 %, de la estacion optica 1 (OGS-1) 57.8 % y de la 2 (OGS-2) 40.5 %;
disponibilidad por clima de 80 %; tasa de exito de sesiones de 59 %; eficiencia de acoplamiento de la optica adaptativa de 35 % en un
enlace nocturno; el estudio concluye que harian falta mas de dos estaciones para pasar de 99 %. h y c: NIST, CODATA 2022.
ILUSTRATIVOS (sinteticos, no medidos): potencia 0.5 W, distancia 384400 km, cintura 4 cm (theta 12.355 urad), receptor de 0.4 m
de diametro, 100 Mbps, 6 fotones incidentes por bit, perdidas de optica 3 dB, extincion tau 0.05, sigma de apuntamiento 2 urad por eje,
centelleo sigma_I^2 = 0.1, probabilidad de nube 0.2, disponibilidad de hardware por estacion 0.95.
Modelo: P_rx = P G_t A_r / (4 pi d^2), G_t = 8/theta^2; margen M0 = P_rx / P_req en dB sin apuntamiento ni centelleo;
perdida de apuntamiento instantanea 8.686 r^2/theta^2 dB con r de Rayleigh (sigma); desvanecimiento por centelleo log-normal de media 1;
salida de servicio si perdida + desvanecimiento > M0.
Segunda via: Monte Carlo (random.Random(92)) frente a integral numerica de Simpson sobre r con cola log-normal exacta.
Tolerancia: Monte Carlo frente a integral 2e-3 absoluta.
"""
from __future__ import annotations
import math, platform, random
from statistics import NormalDist

C = 299792458.0
H = 6.62607015e-34
LAM = C / 193.1e12
TH = LAM / (math.pi * 0.04)
SIG = 2e-6
S2 = math.log(1.0 + 0.1)
S = math.sqrt(S2)
ND = NormalDist()


def db(x):
    return 10.0 * math.log10(x)


def presupuesto():
    p, d, dr, rate, fpb = 0.5, 384400e3, 0.4, 100e6, 6.0
    gt = 8.0 / TH ** 2
    ar = math.pi * (dr / 2) ** 2
    prx = p * gt * ar / (4.0 * math.pi * d ** 2)
    preq = rate * fpb * H * C / LAM
    items = [("Potencia transmitida 0.5 W", db(p), "dBW"),
             ("Ganancia de transmision 8/theta^2", db(gt), "dBi"),
             ("Dispersion 1/(4 pi d^2), d = 384400 km", -db(4 * math.pi * d ** 2), "dB"),
             ("Area del receptor (0.4 m de diametro)", db(ar), "dB"),
             ("Perdidas de optica", -3.0, "dB"),
             ("Acoplamiento de optica adaptativa 35 %", db(0.35), "dB"),
             ("Extincion clara (tau 0.05)", -db(math.exp(0.05)), "dB")]
    pot_dbw = sum(v for _, v, _ in items)
    return items, pot_dbw, db(preq), prx, preq


def p_salida_integral(m0, n=20000):
    """P(8.686 r^2/theta^2 + F_dB > m0), r ~ Rayleigh(SIG), F_dB = -10 log10 I, ln I ~ N(-S2/2, S2)."""
    rmax = 8.0 * SIG
    h = rmax / n

    def g(r):
        lp = 8.685889638 * r * r / TH ** 2
        resto = m0 - lp
        if resto <= 0:
            cola = 1.0
        else:
            umbral = 10 ** (-resto / 10.0)          # irradiancia relativa por debajo de la cual se sale
            cola = ND.cdf((math.log(umbral) + 0.5 * S2) / S)
        return r / SIG ** 2 * math.exp(-r * r / (2 * SIG ** 2)) * cola

    s = g(0.0) + g(rmax)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * g(i * h)
    return s * h / 3.0 + math.exp(-rmax ** 2 / (2 * SIG ** 2))


def p_salida_mc(m0, n, rng):
    fuera = 0
    for _ in range(n):
        r = math.hypot(rng.gauss(0.0, SIG), rng.gauss(0.0, SIG))
        lp = 8.685889638 * r * r / TH ** 2
        i = math.exp(rng.gauss(-0.5 * S2, S))
        if lp - 10.0 * math.log10(i) > m0:
            fuera += 1
    return fuera / n


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    items, pot, preq_db, prx, preq = presupuesto()
    print("Presupuesto de enlace ILUSTRATIVO (Luna, 100 Mbps, 6 fotones incidentes por bit):")
    for nom, v, u in items:
        print(f"  {nom:42s} {v:+9.2f} {u}")
    print(f"  Potencia recibida (sin apuntamiento ni centelleo)  {pot:+9.2f} dBW = {10 ** (pot / 10):.3e} W")
    print(f"  Potencia requerida (100 Mbps x 6 fotones/bit)      {preq_db:+9.2f} dBW = {preq:.3e} W")
    m0 = pot - preq_db
    print(f"  Margen M0 sin apuntamiento ni centelleo            {m0:+9.2f} dB")
    print("Probabilidad de salida de servicio con cielo despejado (apuntamiento + centelleo):")
    print("  M0 [dB]   integral numerica   Monte Carlo (200000)")
    rng = random.Random(92)
    dmax = 0.0
    for mm in (3.0, 6.0, 9.0, 12.0):
        pi_ = p_salida_integral(mm)
        pm = p_salida_mc(mm, 200000, rng)
        dmax = max(dmax, abs(pi_ - pm))
        print(f"  {mm:7.1f}   {pi_:16.5f}   {pm:12.5f}")
    print(f"Diferencia absoluta maxima integral frente a Monte Carlo = {dmax:.1e}")
    lo, hi = 0.0, 30.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if p_salida_integral(mid) > 0.01:
            lo = mid
        else:
            hi = mid
    print(f"Margen M0 para una salida de servicio de 1 %: {0.5 * (lo + hi):.2f} dB (el presupuesto tiene {m0:.2f} dB)")
    p_out = p_salida_integral(m0)
    print(f"Con el margen del presupuesto: salida de servicio con cielo despejado = {p_out:.4f}")
    print("Reconstruccion de la disponibilidad de LCRD (cifras publicadas; el cruce es una inferencia propia):")
    a1, a2, pay, clima = 0.578, 0.405, 0.993, 0.80
    una_de_dos = 1 - (1 - a1) * (1 - a2)
    comun = pay * una_de_dos * clima
    indep = pay * (1 - (1 - a1 * clima) * (1 - a2 * clima))
    print(f"  Una de dos estaciones disponible (sin clima) = {una_de_dos:.4f}")
    print(f"  Con clima comun a las dos estaciones: {comun:.4f} ; con clima independiente: {indep:.4f} ; publicado: 0.59")
    print("Disponibilidad total con N estaciones (hardware 0.95, nube 0.2 independiente, salida optica con M0 del presupuesto):")
    prev = 0.0
    n99 = None
    for n in range(1, 6):
        est = 0.95 * 0.8
        cob = 1.0 - (1.0 - est) ** n
        tot = cob * (1.0 - p_out)
        print(f"  N = {n}  cobertura {cob:.5f}  disponibilidad total {tot:.5f}")
        if tot >= 0.99 and n99 is None:
            n99 = n
        assert tot > prev
        prev = tot
    print(f"Menor N con disponibilidad total >= 99 %: {n99}")
    assert dmax < 2e-3
    assert abs(comun - 0.59) < 0.01
    assert n99 is not None
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
