#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B106-C15: probabilidad de no penetracion por impactos (Poisson) con un flujo y un escudo SINTETICOS.

NINGUN parametro procede de una fuente consultada (la pagina de la NASA sobre desechos orbitales devolvio 404). Flujo SINTETICO e inventado: N(>d) = N0 (d/1 mm)^-b impactos
por m2 y ano con N0 = 1e-4 y b = 2.5. Diametro critico ILUSTRATIVO: d_c = alpha t (1 + S/S0) con alpha = 0.3, S0 = 2 cm (t espesor de pared; S separacion entre parachoques y pared).
Superficie expuesta de 100 m2. Monte Carlo con semilla 106 para comprobar el calculo exponencial. Los numeros NO describen el riesgo real de ningun vehiculo.
Verificacion: P = exp(-N) coincide con la frecuencia del Monte Carlo (dentro de 4 desviaciones tipicas) y mas espesor o mas separacion aumentan P.
"""
from __future__ import annotations
import math
import platform
import numpy as np

N0, B, AREA, ALPHA, S0 = 1e-4, 2.5, 100.0, 0.3, 2.0


def d_crit(t_mm, s_cm):
    return ALPHA * t_mm * (1 + s_cm / S0)


def n_esperado(t_mm, s_cm, T_anos, area=AREA):
    return area * T_anos * N0 * d_crit(t_mm, s_cm) ** (-B)


def main():
    print(f"Python {platform.python_version()}; numpy {np.__version__}")
    print("DATOS: flujo y escudo SINTETICOS e inventados (no consultados); NO describen el riesgo de un vehiculo real")
    R = {}
    print(f"Superficie {AREA:.0f} m2; flujo N(>d) = {N0:.0e} (d/1 mm)^-{B} /m2/ano")
    print("  pared t [mm]  separacion [cm]  d_critico [mm]  impactos esperados en 1 ano  P(sin penetracion) 1 ano  5 anos")
    casos = ((2.0, 0.0), (2.0, 10.0), (4.0, 0.0), (4.0, 10.0))
    P1 = {}
    for t, s in casos:
        N = n_esperado(t, s, 1.0)
        P1[(t, s)] = math.exp(-N)
        print(f"  {t:11.1f}  {s:14.1f}  {d_crit(t,s):14.2f}  {N:26.3e}  {math.exp(-N):24.6f}  {math.exp(-5*N):7.6f}")
    R["N_2_0"], R["P_2_0"], R["P_2_10"], R["P_4_10"], R["dc_2_0"], R["dc_2_10"] = n_esperado(2, 0, 1), P1[(2.0, 0.0)], P1[(2.0, 10.0)], P1[(4.0, 10.0)], d_crit(2, 0), d_crit(2, 10)
    R["P5_2_0"] = math.exp(-5 * n_esperado(2, 0, 1))
    assert P1[(4.0, 10.0)] > P1[(2.0, 10.0)] > P1[(2.0, 0.0)] and P1[(4.0, 0.0)] > P1[(2.0, 0.0)]
    # Monte Carlo
    rng = np.random.default_rng(106)
    N = n_esperado(2.0, 0.0, 5.0)
    M = 200000
    k = rng.poisson(N, M)
    f = float(np.mean(k == 0))
    sd = math.sqrt(f * (1 - f) / M)
    an = math.exp(-N)
    R.update(f=f, an=an, sd=sd, N5=N)
    print(f"Monte Carlo (5 anos, pared 2 mm sin parachoques, {M} misiones): P(sin penetracion) = {f:.5f} +- {sd:.5f}; analitico {an:.5f}")
    assert abs(f - an) < 4 * sd
    # espesor para P >= 0.99 en 5 anos sin parachoques
    t = 0.1
    while math.exp(-n_esperado(t, 0.0, 5.0)) < 0.99 and t < 100:
        t += 0.01
    R["t99"] = t
    print(f"Espesor de pared sin parachoques para P >= 0.99 en 5 anos: {t:.2f} mm")
    s = 0.0
    while math.exp(-n_esperado(2.0, s, 5.0)) < 0.99 and s < 100:
        s += 0.05
    R["s99"] = s
    print(f"Separacion con pared de 2 mm para P >= 0.99 en 5 anos: {s:.2f} cm")
    print("Pruebas superadas.")
    return R


if __name__ == "__main__":
    main()
