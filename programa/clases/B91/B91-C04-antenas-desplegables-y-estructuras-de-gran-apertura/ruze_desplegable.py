#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B91-C04: reflector desplegable, error de superficie (formula de Ruze) y razon de empaquetado.

Sin datos publicados consultados para el reflector: todo es SINTETICO/ILUSTRATIVO (D = 3.0 m, eficiencia sin error eta0 = 0.65,
error rms de superficie eps = 0.5 mm, malla, masa areal 0.5 kg/m2, cada petalo plegado al 20 % del diametro).
Modelo: G = eta0 (pi D / lambda)^2 exp(-(4 pi eps / lambda)^2)  [Ruze; relacion estandar, no consultada en una fuente concreta].
Optimo: dG/dlambda = 0 -> lambda_opt = 4 pi eps  (analitico: con x = 1/lambda^2, G ~ x exp(-a x), maximo en x = 1/a, a = (4 pi eps)^2);  f_opt = c / lambda_opt.
Segunda via: busqueda por seccion aurea sobre G(f) en dB; presupuesto de error rms por suma cuadratica (RSS) de terminos independientes.
Tolerancias: f_opt numerica frente a analitica < 1e-6 relativa.
"""
from __future__ import annotations
import math, platform

C = 299_792_458.0


def ganancia_db(d, f, eta0, eps):
    lam = C / f
    g = eta0 * (math.pi * d / lam) ** 2 * math.exp(-((4 * math.pi * eps / lam) ** 2))
    return 10 * math.log10(g)


def seccion_aurea(fun, a, b, tol=1.0):
    gr = (math.sqrt(5) - 1) / 2
    c, d = b - gr * (b - a), a + gr * (b - a)
    while abs(b - a) > tol:
        if fun(c) > fun(d):
            b = d
        else:
            a = c
        c, d = b - gr * (b - a), a + gr * (b - a)
    return 0.5 * (a + b)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    D, eta0, eps = 3.0, 0.65, 0.5e-3
    print(f"Reflector SINTETICO: D = {D} m, eta0 = {eta0}, error rms eps = {eps*1e3} mm")
    lam_opt = 4 * math.pi * eps
    f_an = C / lam_opt
    f_num = seccion_aurea(lambda f: ganancia_db(D, f, eta0, eps), 1e9, 100e9)
    print(f"Frecuencia optima: analitica = {f_an/1e9:.4f} GHz ; numerica = {f_num/1e9:.4f} GHz ; error relativo = {abs(f_an-f_num)/f_an:.2e}")
    assert abs(f_an - f_num) / f_an < 1e-6
    g_opt = ganancia_db(D, f_an, eta0, eps)
    print(f"Ganancia en el optimo = {g_opt:.2f} dBi (eficiencia por superficie exp(-1) = {math.exp(-1):.4f}, es decir {-10*math.log10(math.exp(-1)):.2f} dB)")
    print("Banda    f [GHz]   lambda [mm]   Ruze exp(-x^2) [dB]   G sin error [dBi]   G con error [dBi]")
    for nom, f in (("S", 2.2e9), ("X", 8.4e9), ("Ku", 14.0e9), ("Ka", 32.0e9), ("Ka-alto", 40.0e9)):
        lam = C / f
        loss = -10 * math.log10(math.exp(-((4 * math.pi * eps / lam) ** 2)))
        print(f" {nom:7s} {f/1e9:7.1f}   {lam*1e3:9.2f}        {-loss:10.3f}            {ganancia_db(D, f, eta0, 0.0):9.2f}          {ganancia_db(D, f, eta0, eps):9.2f}")
    print("Perdida de Ruze segun eps/lambda (relacion estandar):")
    for den in (16, 30, 50, 100):
        x = 4 * math.pi / den
        print(f"   eps = lambda/{den:<3d}: {10*math.log10(math.exp(x*x)):.3f} dB")
    # Presupuesto RSS (SINTETICO)
    terminos = {"fabricacion de la malla": 0.30, "tension de los cables": 0.25, "deformacion termica": 0.20, "tolerancia de despliegue": 0.25}
    rss = math.sqrt(sum(v * v for v in terminos.values()))
    print("Presupuesto de error rms (mm, SINTETICO, terminos independientes):")
    for k, v in terminos.items():
        print(f"   {k:28s} {v:.2f}")
    print(f"   total RSS = {rss:.3f} mm ; suma lineal = {sum(terminos.values()):.2f} mm (cota superior pesimista)")
    assert abs(rss - math.sqrt(0.09 + 0.0625 + 0.04 + 0.0625)) < 1e-12
    print("Empaquetado (SINTETICO): D desplegado frente al diametro de la envolvente plegada")
    print(" D [m]   masa areal 0.5 kg/m2 -> masa [kg]   petalo plegado (20 % D) [m]   razon D/D_plegado")
    for dd in (1.0, 2.0, 3.0, 5.0, 10.0):
        area = math.pi * dd * dd / 4
        print(f" {dd:5.1f}        {0.5*area:8.2f}                    {0.2*dd:8.2f}                {dd/(0.2*dd):6.1f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
