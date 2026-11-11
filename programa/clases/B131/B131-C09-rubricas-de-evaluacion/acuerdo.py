#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B131-C09: acuerdo entre dos evaluadores con una rubrica de 4 criterios y 4 niveles (kappa simple y ponderado cuadratico).

CONTENIDO EDUCATIVO. Sin datos consultados: 30 trabajos y dos evaluadores SINTETICOS (semilla 131). Cada trabajo tiene un nivel verdadero
latente (1-4) por criterio; cada evaluador lo observa con sesgo y ruido gaussiano redondeado y recortado a 1-4. Ronda 1: antes de calibrar
(ruido 0.8, sesgo del evaluador B +0.3). Ronda 2: tras calibrar con ejemplares (ruido 0.4, sin sesgo). Parametros ILUSTRATIVOS.
Relaciones estandar NO consultadas en una fuente concreta: kappa de Cohen, kappa ponderado cuadratico por dos vias (matriz de desacuerdo y
formula con covarianza). No se usan umbrales publicados para calificar el acuerdo.
Tolerancias: las dos vias del kappa ponderado coinciden a 1e-9.
"""
from __future__ import annotations
import platform, random, statistics

NIV = 4
CRITERIOS = ["Datos y unidades", "Metodo", "Incertidumbre", "Comunicacion"]


def ronda(sigma, sesgo_b, seed):
    rng = random.Random(seed)
    A, B = [], []
    for _ in range(30):
        fila_a, fila_b = [], []
        for _c in CRITERIOS:
            verd = rng.choices([1, 2, 3, 4], weights=[1, 3, 4, 2])[0]
            ra = min(NIV, max(1, round(verd + rng.gauss(0, sigma))))
            rb = min(NIV, max(1, round(verd + sesgo_b + rng.gauss(0, sigma))))
            fila_a.append(ra)
            fila_b.append(rb)
        A.append(fila_a)
        B.append(fila_b)
    return A, B


def matriz(a, b):
    m = [[0] * NIV for _ in range(NIV)]
    for x, y in zip(a, b):
        m[x - 1][y - 1] += 1
    return m


def kappa(m, ponderado=False):
    n = sum(map(sum, m))
    fa = [sum(f) for f in m]
    fb = [sum(m[i][j] for i in range(NIV)) for j in range(NIV)]
    num = den = 0.0
    for i in range(NIV):
        for j in range(NIV):
            w = ((i - j) ** 2 / (NIV - 1) ** 2) if ponderado else (0.0 if i == j else 1.0)
            num += w * m[i][j] / n
            den += w * fa[i] * fb[j] / n ** 2
    return 1 - num / den


def kappa_cov(a, b):
    """Kappa ponderado cuadratico = 2 s_xy / (s_x^2 + s_y^2 + (media_x - media_y)^2), con varianzas poblacionales."""
    mx, my = statistics.mean(a), statistics.mean(b)
    sxy = sum((x - mx) * (y - my) for x, y in zip(a, b)) / len(a)
    return 2 * sxy / (statistics.pvariance(a) + statistics.pvariance(b) + (mx - my) ** 2)


def resumen(nombre, A, B):
    a = [x for f in A for x in f]
    b = [x for f in B for x in f]
    exact = sum(1 for x, y in zip(a, b) if x == y) / len(a)
    adj = sum(1 for x, y in zip(a, b) if abs(x - y) <= 1) / len(a)
    m = matriz(a, b)
    k, kw, kc = kappa(m), kappa(m, True), kappa_cov(a, b)
    sesgo = statistics.mean(y - x for x, y in zip(a, b))
    print(f"{nombre}: acuerdo exacto {exact:.3f} ; adyacente {adj:.3f} ; kappa {k:.3f} ; kappa ponderado {kw:.3f} (via covarianza {kc:.3f}) ; sesgo B-A {sesgo:+.2f}")
    return kw, kc, exact


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("30 trabajos x 4 criterios, dos evaluadores SINTETICOS (semilla 131); parametros ILUSTRATIVOS; ningun dato consultado.")
    A1, B1 = ronda(0.8, 0.3, 131)
    A2, B2 = ronda(0.4, 0.0, 132)
    kw1, kc1, e1 = resumen("Ronda 1 (sin calibrar)", A1, B1)
    kw2, kc2, e2 = resumen("Ronda 2 (calibrada)   ", A2, B2)
    print("Por criterio, ronda 1 (kappa ponderado):")
    for j, c in enumerate(CRITERIOS):
        a = [f[j] for f in A1]
        b = [f[j] for f in B1]
        print(f"  {c:18s} {kappa(matriz(a, b), True):.3f}   (n = {len(a)} trabajos: estimacion muy inestable)")
    print("Matriz de la ronda 1 (filas A, columnas B):")
    m = matriz([x for f in A1 for x in f], [x for f in B1 for x in f])
    for i, f in enumerate(m, 1):
        print("  nivel " + str(i) + ": " + " ".join(f"{v:3d}" for v in f))
    assert abs(kw1 - kc1) < 1e-9 and abs(kw2 - kc2) < 1e-9
    assert kw2 > kw1 and e2 > e1
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
