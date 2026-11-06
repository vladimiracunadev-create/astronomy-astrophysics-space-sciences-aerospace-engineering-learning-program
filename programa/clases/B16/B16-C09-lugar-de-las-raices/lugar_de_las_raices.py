#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B16-C09: lugar de las raíces de L(s) = K / (s (s + 1)(s + 2)).

Datos: SINTÉTICOS (parámetros normalizados). K en s^-3.
Modelo: las raíces de s^3 + 3 s^2 + 2 s + K = 0 al variar K >= 0.
Referencias independientes (analíticas):
  - suma de raíces = -3 para todo K (el coeficiente de s^2 no depende de K);
  - asíntotas: centroide -1, ángulos +-60 y 180 grados;
  - punto de ruptura: dK/ds = 0 -> 3 s^2 + 6 s + 2 = 0, s = -1 + 1/sqrt(3)
    = -0.42265, con K = 2/(3 sqrt(3)) = 0.3849;
  - cruce del eje imaginario: K = 6, s = +-j sqrt(2) (Routh, C08);
  - condición de ángulo: en cada raíz, arg L(s) = -180 grados (mod 360).
Supuestos: K real positivo, coeficientes reales. Tolerancia: 1e-9.
"""
from __future__ import annotations
import math, platform, sys
import numpy as np


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def raices(K):
    return np.roots([1.0, 3.0, 2.0, K])


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  numpy {np.__version__}")
    Ks = np.linspace(0.0, 20.0, 2001)
    for K in Ks:
        prueba(abs(raices(K).sum() + 3.0) < 1e-9, f"suma de raíces K={K}")
    print("suma de las tres raíces = -3 en 2001 valores de K")

    # asíntotas: para K grande las raíces se alinean con el centroide -1
    r = raices(1e6)
    print(f"K = 1e6: raíces {np.round(r, 2)}; centroide medio {r.real.mean():.4f}; "
          f"ángulos {np.round(np.degrees(np.angle(r + 1)), 2)}")
    prueba(abs(r.real.mean() + 1) < 1e-6, "centroide")
    ang = sorted(np.degrees(np.angle(r + 1)))
    prueba(abs(ang[0] + 120) < 2.0 or abs(abs(ang[0]) - 60) < 2.0, "ángulos aproximados")

    # punto de ruptura
    s_b = -1 + 1 / math.sqrt(3)
    K_b = -s_b * (s_b + 1) * (s_b + 2)
    rb = raices(K_b)
    print(f"ruptura: s = {s_b:.5f}, K = {K_b:.4f}; raíces en K = K_b: {np.round(np.sort(rb.real), 5)}")
    prueba(abs(K_b - 2 / (3 * math.sqrt(3))) < 1e-12, "K de ruptura")
    prueba(np.sum(np.abs(rb.real - s_b) < 1e-3) == 2, "raíz doble en la ruptura")

    # cruce del eje imaginario
    rc = raices(6.0)
    im = rc[np.abs(rc.real) < 1e-6]
    print(f"cruce: K = 6, raíces sobre el eje imaginario {np.round(im, 6)}")
    prueba(len(im) == 2 and abs(abs(im[0].imag) - math.sqrt(2)) < 1e-6, "cruce en j sqrt 2")

    # condición de ángulo en 5 valores de K
    for K in (0.2, 1.0, 3.0, 5.0, 8.0):
        for s in raices(K):
            L = K / (s * (s + 1) * (s + 2))
            ang = np.degrees(np.angle(L)) % 360
            prueba(abs(ang - 180.0) < 1e-6, f"condición de ángulo K={K}")
    print("condición de ángulo arg L(s) = 180 grados (mod 360) verificada en 5 valores de K")

    # amortiguamiento del par dominante
    print("  K    polos dominantes             zeta")
    for K in (0.2, 0.5, 1.0, 2.0, 4.0):
        r = raices(K)
        par = r[np.abs(r.imag) > 1e-9]
        if len(par):
            p = par[0]
            z = -p.real / abs(p)
            print(f"{K:5.1f}  {p.real:7.4f} ± {abs(p.imag):6.4f}j   {z:6.3f}")
        else:
            print(f"{K:5.1f}  todas reales {np.round(np.sort(r.real), 4)}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
