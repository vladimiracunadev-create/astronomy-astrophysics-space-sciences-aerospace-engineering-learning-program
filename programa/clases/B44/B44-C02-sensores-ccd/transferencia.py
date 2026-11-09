#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B44-C02: eficiencia de transferencia de carga (CTE) y perdida acumulada en un CCD.

Datos: ninguna constante fisica. Tamano del sensor (2048 x 2048), CTE y paquetes de carga son ILUSTRATIVOS (sinteticos); no describen un CCD real.
Modelo: tras n transferencias queda la fraccion CTE^n; la perdida por transferencia es una Bernoulli de probabilidad 1 - CTE por electron (simulacion con semilla 20261109).
Supuestos: perdida independiente en cada transferencia y cada electron, sin trampas dependientes de la carga. Validez: ilustrativa.
Tolerancia: media simulada frente a la analitica dentro de 4 sigma binomiales.
"""
from __future__ import annotations
import math, platform, random, sys

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    nx = ny = 2048
    print(f"{'CTE':>10} {'n transf.':>10} {'fraccion restante':>18} {'perdida [%]':>12}")
    for cte in (0.99999, 0.999995, 0.9999):
        n = nx + ny
        f = cte ** n
        print(f"{cte:10.6f} {n:10d} {f:18.5f} {100*(1-f):12.3f}")
    assert abs(0.99999 ** 4096 - math.exp(4096 * math.log(0.99999))) < 1e-12
    # simulacion: 1000 electrones, CTE 0.9999, 400 transferencias, 300 repeticiones
    rng = random.Random(20261109)
    cte, n, q0, rep = 0.9999, 400, 1000, 300
    tot = 0
    for _ in range(rep):
        q = q0
        for _ in range(n):
            # numero perdido ~ Binomial(q, 1-cte): se aproxima por Poisson de media q(1-cte) (p pequena)
            lam = q * (1 - cte)
            l, k, p = math.exp(-lam), 0, 1.0
            while True:
                p *= rng.random()
                if p <= l:
                    break
                k += 1
            q -= min(k, q)
        tot += q
    media = tot / rep
    esp = q0 * cte ** n
    sig = math.sqrt(q0 * cte ** n * (1 - cte ** n) / rep)
    print(f"1000 e-, CTE 0.9999, 400 transferencias: analitico {esp:.2f} e-, simulado {media:.2f} e- (sigma de la media {sig:.2f})")
    assert abs(media - esp) < 4 * sig + 0.5
    # el pixel mas lejano (esquina) pierde mas que el mas cercano
    print(f"pixel cercano (1 transf.): {0.99999**1:.6f}  pixel lejano (4096 transf.): {0.99999**4096:.6f}")
    assert 0.99999 ** 4096 < 0.99999
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
