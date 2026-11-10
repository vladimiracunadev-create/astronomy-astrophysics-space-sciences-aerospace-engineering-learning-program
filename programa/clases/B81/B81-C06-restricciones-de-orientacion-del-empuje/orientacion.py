#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C06: restricciones de orientacion del empuje (perdida por coseno entre propulsor, paneles y Sol).

Sin datos externos: geometria SINTETICA y adimensional (angulos en grados). No se consultaron fuentes para esta clase.
Modelo plano: la direccion de empuje deseada es t = (1, 0). El Sol esta en s = (cos psi, sin psi). Los paneles son fijos en el cuerpo con normal n
perpendicular a la direccion real de empuje; el empuje real se desvia un angulo delta de t (rotacion en el plano), y n = (-sin delta, cos delta).
Potencia disponible proporcional a |s . n| = |sin(psi - delta)|; empuje proporcional a la potencia; componente util a lo largo de t: cos(delta).
Eficiencia util E(psi, delta) = cos(delta) |sin(psi - delta)|. Sin desviacion: E = |sin psi|.
Optimo libre: delta* = (psi - 90)/2 con E* = (1 + sin psi)/2 (derivado en la clase). Con cono |delta| <= dmax: maximo sobre el cono.
Segunda via: busqueda en rejilla fina de delta (paso 0,01 grados).
Tolerancias: |E_rejilla - E_analitico| < 1e-6 para el optimo libre; la rejilla respeta el cono.
"""
from __future__ import annotations
import math, platform


def E(psi, delta):
    p, d = math.radians(psi), math.radians(delta)
    return math.cos(d) * abs(math.sin(p - d))


def optimo_rejilla(psi, dmax):
    best = (-1.0, 0.0)
    n = int(round(2 * dmax / 0.01))
    for i in range(n + 1):
        d = -dmax + i * 0.01
        e = E(psi, d)
        if e > best[0]:
            best = (e, d)
    return best[1], best[0]


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Geometria SINTETICA; angulos en grados; E = cos(delta) |sin(psi - delta)|")
    print(" psi   E sin desviar   delta* libre   E* analitico   delta* rejilla   E* rejilla")
    maxerr = 0.0
    for psi in (20, 30, 45, 60, 90, 120):
        d_an = (psi - 90) / 2
        e_an = (1 + math.sin(math.radians(psi))) / 2
        d_g, e_g = optimo_rejilla(psi, 90.0)
        maxerr = max(maxerr, abs(e_an - e_g))
        print(f"{psi:4d}   {E(psi, 0):12.4f}   {d_an:11.2f}   {e_an:12.4f}   {d_g:14.2f}   {e_g:10.4f}")
    print(f"Error maximo del optimo libre (rejilla frente a analitico) = {maxerr:.2e}")
    print("Con cono de orientacion |delta| <= dmax (psi = 30 grados):")
    print(" dmax   delta* [deg]   E*      ganancia sobre sin desviar")
    for dmax in (0, 5, 10, 20, 30, 45):
        d, e = optimo_rejilla(30, float(dmax)) if dmax > 0 else (0.0, E(30, 0))
        print(f"{dmax:5d}   {d:11.2f}   {e:6.4f}   {e/E(30,0):8.3f}")
    # impacto en dv: una espiral que necesita 4000 m/s con acel nominal 1e-3 m/s^2 a E = 1
    for psi in (30, 60, 90):
        e_loc = (1 + math.sin(math.radians(psi))) / 2
        t_nom = 4000 / 1e-3 / 86400
        print(f"psi = {psi:3d}: tiempo con orientacion libre = {t_nom/e_loc:.1f} d frente a {t_nom:.1f} d con E = 1 (acel. nominal ILUSTRATIVA 1e-3 m/s^2, dv 4000 m/s)")
    assert maxerr < 1e-6
    assert abs(E(30, 0) - 0.5) < 1e-12
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
