#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B81-C14: presupuesto estadistico de delta-v de correccion (Monte Carlo frente a cuantilas analiticas).

Sin fuentes externas: todas las desviaciones son SINTETICAS e ILUSTRATIVAS. Semilla fija 20260811.
Modelo: cada correccion requiere un delta-v vectorial dv ~ N(0, S) en 3D (m/s). Magnitud |dv|; presupuesto = cuantila al 99 %.
Caso isotropo (sigma = 1 m/s por eje): |dv|/sigma sigue una chi con 3 grados de libertad; cuantila 99 %: sqrt(11,3449) = 3,3682 (valor de la tabla chi-cuadrado 3 g.l.,
se calcula con SciPy y se compara con la simulacion). Caso anisotropo: sigma = (1,0; 0,5; 0,2) m/s; sin formula simple, se usa Monte Carlo con 2e6 muestras y dos semillas.
Varias correcciones independientes: (i) suma de cuantilas (conservadora), (ii) raiz de la suma de cuadrados de las cuantilas, (iii) cuantila MC de la suma de magnitudes.
Tolerancias: cuantila MC isotropa frente a SciPy < 0,5 %; las dos semillas anisotropas coinciden < 0,5 %.
"""
from __future__ import annotations
import math, platform
import numpy as np
import scipy
from scipy.stats import chi


def cuantil(x, q=0.99):
    return float(np.quantile(x, q))


def main():
    print(f"Python {platform.python_version()} | NumPy {np.__version__} | SciPy {scipy.__version__}")
    rng = np.random.default_rng(20260811)
    n = 2_000_000
    sig_iso = 1.0
    dv = np.linalg.norm(rng.normal(0, sig_iso, (n, 3)), axis=1)
    q_mc = cuantil(dv)
    q_an = float(chi.ppf(0.99, 3)) * sig_iso
    print(f"Isotropo sigma = 1 m/s: media |dv| MC = {dv.mean():.4f} (teorico 2 sqrt(2/pi) = {2*math.sqrt(2/math.pi):.4f}) ; cuantila 99 % MC = {q_mc:.4f} ; chi(3) = {q_an:.4f} ; dif. = {abs(q_mc-q_an)/q_an:.2e}")
    sig = np.array([1.0, 0.5, 0.2])
    qs = []
    for sem in (1, 2):
        r = np.random.default_rng(sem)
        d = np.linalg.norm(r.normal(0, 1, (n, 3)) * sig, axis=1)
        qs.append(cuantil(d))
    print(f"Anisotropo sigma = (1,0; 0,5; 0,2) m/s: cuantila 99 % = {qs[0]:.4f} y {qs[1]:.4f} (dos semillas) ; dif. = {abs(qs[0]-qs[1])/qs[0]:.2e}")
    print(f"  cota con la cuantila isotropa del eje mayor: {chi.ppf(0.99,3)*1.0:.4f} m/s (conservadora)")
    # varias correcciones
    print("Varias correcciones independientes (anisotropas, mismas sigma):")
    print("  k   suma de cuantilas   RSS de cuantilas   cuantila 99 % MC de la suma")
    rr = np.random.default_rng(5)
    acum = np.zeros(500_000)
    qk = qs[0]
    res = []
    for k in range(1, 6):
        acum += np.linalg.norm(rr.normal(0, 1, (500_000, 3)) * sig, axis=1)
        qm = cuantil(acum)
        res.append(qm)
        print(f"  {k}   {k*qk:15.4f}   {math.sqrt(k)*qk:16.4f}   {qm:20.4f}")
    print("  (en esta muestra la cuantila de la suma queda entre el RSS y la suma de cuantilas: sumar cuantilas es conservador y el RSS es optimista porque las magnitudes se suman, no sus cuadrados)")
    assert abs(q_mc - q_an) / q_an < 0.005
    assert abs(qs[0] - qs[1]) / qs[0] < 0.005
    assert res[-1] < 5 * qk
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
