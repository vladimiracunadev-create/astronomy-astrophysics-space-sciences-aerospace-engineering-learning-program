#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C09: variables de diseno orbital, parametrizacion y escalado.

Datos: GM del Sol = 132712440041.279419 km^3/s^2 y UA = 149597870.7 km (JPL SSD, astro_par, DE440; consultada 2026-11-10).
Problema SINTETICO (ILUSTRATIVO): transferencia de tres impulsos entre orbitas circulares coplanares de radios 1 UA y 8 UA con un cambio de plano total de 30 grados
repartido entre los tres impulsos. Variables de diseno: radio del apoastro intermedio r_b [km], fraccion del cambio de plano en el primer impulso f1 y en el tercero f3
(el segundo recibe 1 - f1 - f3). Cada impulso: dv = sqrt(va^2 + vb^2 - 2 va vb cos(theta)) con theta = fraccion x 30 grados.
Sistema: dos cuerpos heliocentrico, impulsivo, km/s.
Se minimiza dv total con L-BFGS-B (SciPy) sobre (a) las variables sin escalar (r_b en km) y (b) las escaladas x = (r_b/AU, f1, f3).
Segunda via: rejilla fina sobre (r_b, f1, f3) para localizar el minimo aproximado.
Tolerancias: el minimo escalado queda a menos de 1e-3 km/s de la rejilla (o por debajo); la version sin escalar se informa sin exigirle convergencia.
"""
from __future__ import annotations
import math, platform
import numpy as np
import scipy
from scipy.optimize import minimize

MU = 132712440041.279419
AU = 149597870.7
R1, R2 = 1.0 * AU, 8.0 * AU
DI = math.radians(30.0)


def dv_imp(va, vb, th):
    return math.sqrt(max(va * va + vb * vb - 2 * va * vb * math.cos(th), 0.0))


def dv_total(rb, f1, f3):
    f2 = 1.0 - f1 - f3
    vc1, vc2 = math.sqrt(MU / R1), math.sqrt(MU / R2)
    a1 = 0.5 * (R1 + rb)
    a2 = 0.5 * (R2 + rb)
    vp1 = math.sqrt(MU * (2 / R1 - 1 / a1))
    va1 = math.sqrt(MU * (2 / rb - 1 / a1))
    va2 = math.sqrt(MU * (2 / rb - 1 / a2))
    vp2 = math.sqrt(MU * (2 / R2 - 1 / a2))
    return dv_imp(vc1, vp1, f1 * DI) + dv_imp(va1, va2, f2 * DI) + dv_imp(vp2, vc2, f3 * DI)


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    print(f"Problema SINTETICO: r1 = 1 UA, r2 = 8 UA, cambio de plano {math.degrees(DI):.0f} grados en tres impulsos ; dv Hohmann coplanar (referencia) = "
          f"{math.sqrt(MU/R1)*(math.sqrt(2*R2/(R1+R2))-1) + math.sqrt(MU/R2)*(1-math.sqrt(2*R1/(R1+R2))):.4f} km/s")
    lim = [(1.0 * R2, 40 * AU), (0.0, 1.0), (0.0, 1.0)]
    cons = [{"type": "ineq", "fun": lambda x, s=1: 1.0 - x[1] - x[2]}]
    resultados = {}
    for nombre, esc in (("sin escalar (r_b en km)", np.array([1.0, 1.0, 1.0])), ("escalado (r_b en UA)", np.array([AU, 1.0, 1.0]))):
        x0 = np.array([12.0 * AU, 0.3, 0.3]) / esc
        f = lambda x: dv_total(x[0] * esc[0], x[1], x[2]) + 1e3 * max(0.0, x[1] + x[2] - 1.0) ** 2
        b = [(l / esc[0], u / esc[0]) if i == 0 else (l, u) for i, (l, u) in enumerate(lim)]
        r = minimize(f, x0, method="L-BFGS-B", bounds=b, options={"maxiter": 500, "ftol": 1e-14, "gtol": 1e-10})
        resultados[nombre] = r
        print(f"{nombre:26s}: dv = {r.fun:.6f} km/s ; r_b = {r.x[0]*esc[0]/AU:10.2f} UA ; f1 = {r.x[1]:.4f}, f3 = {r.x[2]:.4f} ; iter = {r.nit:3d}, evaluaciones = {r.nfev:4d}")
    # rejilla de referencia
    mejor = (1e9, None)
    for rb_ua in np.geomspace(8.0, 40, 60):
        for f1 in np.linspace(0, 1, 21):
            for f3 in np.linspace(0, 1 - f1, 21):
                d = dv_total(rb_ua * AU, f1, f3)
                if d < mejor[0]:
                    mejor = (d, (rb_ua, f1, f3))
    print(f"Rejilla gruesa (60x21x21): dv minimo = {mejor[0]:.6f} km/s en r_b = {mejor[1][0]:.1f} UA, f1 = {mejor[1][1]:.2f}, f3 = {mejor[1][2]:.2f}")
    a, b = resultados.values()
    assert b.fun < mejor[0] + 1e-3
    print(f"Diferencia entre las dos parametrizaciones: {a.fun - b.fun:.6f} km/s (positivo = la escalada llega mas abajo)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
