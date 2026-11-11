#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B110-C02: exposicion en cabina con y sin aislamiento (modelo de mezcla, riesgo tipo Wells-Riley).

CONSULTADO (2026-11-10): la ISS tiene mas de una docena de segmentos aislables y la ISS distingue la emergencia de atmosfera toxica
(derrame o liberacion de un material peligroso al aire de cabina) (Tobias y McMillan, SpaceOps 2023, NASA JSC). La forma del modelo de
Wells-Riley (P = 1 - exp(-I q p t / Q)) se vio solo en el resumen de un buscador; la fuente primaria NO se consulto.
ILUSTRATIVOS (sinteticos, no medidos, no son datos clinicos ni toxicologicos): volumenes (zona aislada 10 m3, resto 90 m3), emision
q = 10 quanta/h (mediana; GSD 3 en el Monte Carlo), ritmo respiratorio p = 0,5 m3/h, eliminacion total lambda = 6 + 0,6 /h
en el resto y 6 + 0,6 /h en la zona aislada (+ filtro local de 20 /h en el escenario C), intercambio entre zonas Qx, 3 susceptibles, 72 h,
mascarilla con eficacia de emision 0,5. Modelo: mezcla perfecta en dos zonas, concentracion C en quanta/m3 (o mg/m3 para un contaminante).
Contenido educativo: NO es consejo medico ni un protocolo de aislamiento.
Tolerancias: modelo de dos zonas frente a la formula analitica de una zona < 1 % con Qx = 20000 m3/h (la diferencia viene del gradiente entre zonas); semilla fija 110.
"""
from __future__ import annotations
import math, platform, random

V1, V2 = 10.0, 90.0  # m3
Q_EMIT = 10.0  # quanta/h
P_RESP = 0.5  # m3/h
LAM = 6.6  # 1/h
N_SUSC = 3
T_FIN = 72.0  # h


def exposicion(qx, s, lam1=LAM, lam2=LAM, t_fin=T_FIN, dt=0.002):
    """Integra C1, C2 (quanta/m3) y la dosis acumulada de un susceptible en la zona 2 (quanta)."""
    c1 = c2 = dosis = 0.0
    t = 0.0
    while t < t_fin:
        d1 = s / V1 - qx / V1 * (c1 - c2) - lam1 * c1
        d2 = qx / V2 * (c1 - c2) - lam2 * c2
        c1 += d1 * dt
        c2 += d2 * dt
        dosis += P_RESP * c2 * dt
        t += dt
    return dosis


def una_zona_analitico(s, v, lam, t):
    return P_RESP * s / (lam * v) * (t - (1 - math.exp(-lam * t)) / lam)


def riesgo(dosis):
    return 1.0 - math.exp(-dosis)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Modelo ILUSTRATIVO de dos zonas: V1 = {V1} m3 (zona del tripulante afectado), V2 = {V2} m3; q = {Q_EMIT} quanta/h; lambda = {LAM} /h; {N_SUSC} susceptibles; {T_FIN:.0f} h")
    # verificacion: Qx = 20000 m3/h => una sola zona de 100 m3
    s = Q_EMIT
    dosis_num = exposicion(20000.0, s, dt=0.00005)
    dosis_an = una_zona_analitico(s, V1 + V2, LAM, T_FIN)
    dif = abs(dosis_num - dosis_an) / dosis_an
    print(f"Verificacion (Qx = 20000 m3/h, casi una zona): dosis numerica = {dosis_num:.5f}, analitica = {dosis_an:.5f}, dif relativa = {dif:.2e}")
    esc = [
        ("A  sin aislar (Qx = 2000 m3/h)", 2000.0, 1.0, LAM),
        ("B  puerta cerrada, Qx = 20 m3/h", 20.0, 1.0, LAM),
        ("C  B + filtro local (+20 /h) en zona 1", 20.0, 1.0, LAM + 20.0),
        ("D  C + mascarilla (emision x 0,5)", 20.0, 0.5, LAM + 20.0),
        ("E  D con Qx = 2 m3/h (sellado)", 2.0, 0.5, LAM + 20.0),
    ]
    print(" escenario                                    dosis [quanta]   riesgo por persona   casos esperados (3 pers.)")
    base = None
    resultados = []
    for nom, qx, fe, lam1 in esc:
        d = exposicion(qx, s * fe, lam1=lam1, lam2=LAM, dt=0.002 if qx < 1e3 else 0.0005)
        r = riesgo(d)
        resultados.append((nom, d, r))
        if base is None:
            base = r
        print(f" {nom:42s} {d:12.5f} {r:18.5f} {N_SUSC * r:20.4f}")
    assert all(resultados[i][2] >= resultados[i + 1][2] for i in range(len(resultados) - 1))
    # incertidumbre en q (lognormal): mediana 10, GSD 3; riesgo de la persona en zona 2 con el escenario A y el D
    rng = random.Random(110)
    ra, rd = [], []
    da1 = exposicion(2000.0, 1.0, dt=0.0005)  # dosis por unidad de emision (lineal en s)
    dd1 = exposicion(20.0, 0.5, lam1=LAM + 20.0)
    for _ in range(4000):
        q = Q_EMIT * math.exp(rng.gauss(0.0, math.log(3.0)))
        ra.append(riesgo(q * da1))
        rd.append(riesgo(q * dd1))
    ra.sort(); rd.sort()
    f = lambda v, p: v[int(p * (len(v) - 1))]
    print("Incertidumbre en q (lognormal, mediana 10, GSD 3, 4000 muestras): riesgo por persona")
    print(f"  A: P5 {f(ra,0.05):.4f}  mediana {f(ra,0.5):.4f}  P95 {f(ra,0.95):.4f}")
    print(f"  D: P5 {f(rd,0.05):.4f}  mediana {f(rd,0.5):.4f}  P95 {f(rd,0.95):.4f}")
    # contaminante: liberacion puntual de 100 mg en la zona 1; maximo en la zona 2 y tiempo sobre un umbral ILUSTRATIVO de 0,5 mg/m3
    print("Contaminante (pulso de 100 mg en la zona 1; umbral ILUSTRATIVO 0,5 mg/m3 en la zona 2):")
    for nom, qx, lam1 in (("sin aislar", 2000.0, LAM), ("Qx = 20", 20.0, LAM), ("Qx = 20 + filtro local", 20.0, LAM + 20.0)):
        c1, c2, cmax, tsobre, t = 100.0 / V1, 0.0, 0.0, 0.0, 0.0
        dt = 0.0005 if qx > 1e3 else 0.002
        if qx > 1e3:  # mezcla casi instantanea: se empieza con la concentracion mezclada
            c1 = c2 = 100.0 / (V1 + V2)
        while t < 24.0:
            d1 = -qx / V1 * (c1 - c2) - lam1 * c1
            d2 = qx / V2 * (c1 - c2) - LAM * c2
            c1 += d1 * dt
            c2 += d2 * dt
            cmax = max(cmax, c2)
            if c2 > 0.5:
                tsobre += dt
            t += dt
        print(f"  {nom:24s} C2 maxima = {cmax:6.3f} mg/m3 ; tiempo por encima del umbral = {tsobre:5.2f} h")
    assert dif < 0.01, dif
    assert f(rd, 0.5) < f(ra, 0.5)
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
