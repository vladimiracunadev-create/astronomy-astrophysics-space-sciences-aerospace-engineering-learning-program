#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B112-C01: dosis absorbida y LET en un nucleo celular (modelo ILUSTRATIVO).

Datos ILUSTRATIVOS y SINTETICOS (semilla 112): los LET de cada ion son ordenes de magnitud redondeados para agua/tejido blando y NO se
consultaron en una tabla publicada; los impactos por nucleo son un proceso de Poisson simulado. Unidades SI: dosis en Gy = J/kg, LET
en keV/um, longitudes en m. Modelo: nucleo esferico de 10 um de diametro, densidad 1000 kg/m3; cuerda media de una esfera para trazas
isotropicas = 2d/3; energia por traza = LET * cuerda (sin deltas ni fragmentacion). Relaciones: D = E/m; dosis macroscopica de fluencia
Phi: D = Phi * LET / rho. Verificacion: la dosis media simulada por nucleo debe igualar la dosis macroscopica dentro del 3 %; el
numero medio de impactos por nucleo es nu = Phi * (pi d^2 / 4). Numpy requerido.
"""
from __future__ import annotations
import platform
import numpy as np

KEV = 1.602176634e-16  # J por keV (valor exacto del SI)
D_NUC = 10e-6          # m
RHO = 1000.0           # kg/m3
VOL = np.pi / 6 * D_NUC**3
MASA = RHO * VOL
CUERDA = 2 * D_NUC / 3
AREA = np.pi * D_NUC**2 / 4
# (nombre, LET ilustrativo keV/um)
IONES = [("foton (electrones secundarios)", 0.3), ("proton de alta energia", 0.5), ("helio", 2.0), ("oxigeno", 30.0),
         ("hierro", 150.0)]
DOSIS = 0.1  # Gy macroscopica


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS ILUSTRATIVOS Y SINTETICOS (semilla 112): LET redondeados sin tabla consultada; ninguna cifra es una medicion")
    print(f"Nucleo: diametro {D_NUC*1e6:.0f} um, masa {MASA:.3e} kg, cuerda media {CUERDA*1e6:.2f} um, seccion {AREA:.3e} m2")
    rng = np.random.default_rng(112)
    print(f"Dosis macroscopica fijada: {DOSIS} Gy. Energia por impacto = LET x cuerda; dosis por impacto = energia/masa")
    print(f"{'radiacion':32s} {'LET':>7s} {'D/impacto[Gy]':>14s} {'fluencia[cm-2]':>15s} {'impactos/nucleo':>16s} {'nucleos sin impacto':>20s} {'dosis sim [Gy]':>15s}")
    res = []
    for nombre, let in IONES:
        e_hit = let * CUERDA * 1e6 * KEV           # J (LET keV/um * cuerda en um)
        d_hit = e_hit / MASA                       # Gy
        let_si = let * KEV / 1e-6            # J/m
        fluencia = DOSIS * RHO / let_si            # 1/m2
        nu = fluencia * AREA
        n = 200000
        k = rng.poisson(nu, n)
        dsim = k * d_hit
        sin = float(np.mean(k == 0))
        res.append((nombre, let, d_hit, nu, sin, dsim.mean()))
        print(f"{nombre:32s} {let:7.1f} {d_hit:14.3e} {fluencia/1e4:15.3e} {nu:16.3f} {sin*100:19.1f}% {dsim.mean():15.4f}")
        assert abs(dsim.mean() / DOSIS - 1) < 0.03, "la dosis media simulada no coincide con la macroscopica"
        assert abs(sin - np.exp(-nu)) < 0.01, "la fraccion sin impacto no sigue exp(-nu)"
    # balance de energia: un impacto de hierro en kg y J
    fe = res[-1]
    print(f"Un solo impacto de hierro entrega {fe[2]:.3f} Gy al nucleo; uno de proton, {res[1][2]*1e3:.2f} mGy")
    assert fe[2] > 100 * res[1][2]
    # dosis maxima distinta con la misma dosis media: coeficiente de variacion de la dosis por nucleo
    print("Dispersion de la dosis por nucleo (misma dosis media 0.1 Gy): desviacion tipica / media")
    for r in res:
        let, nu, d_hit = r[1], r[3], r[2]
        cv = 1 / np.sqrt(nu)                       # Poisson: sigma/media = 1/sqrt(nu)
        print(f"  {r[0]:32s} LET {let:6.1f} keV/um -> CV = {cv:6.2f}")
    assert res[-1][4] > 0.5 > res[0][4]
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
