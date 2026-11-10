#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""B90-C05: compatibilidad de un ICD SINTETICO (electrico y mecanico).

Electrico: el rango de salida del proveedor debe caber en el de entrada de cada consumidor y la suma de corrientes debe dejar
un margen minimo (20 % DE EJEMPLO). Mecanico: apilamiento de tolerancias en el peor caso (suma) y estadistico (RSS), contrastado
con Monte Carlo (semilla fija, distribuciones uniformes). Unidades: V, A, mm. Tolerancia: Monte Carlo 2e6 muestras.
"""
import math
import sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from b90_comun import cabecera, comprobar, fin

cabecera("Datos SINTETICOS: ICD de un bus regulado de 5 V y de una union atornillada")
proveedor = {"nombre": "EPS riel 5 V", "vmin": 4.80, "vmax": 5.20, "imax": 3.0}
consumidores = [
    {"nombre": "OBC", "vmin": 4.50, "vmax": 5.50, "i": 0.8},
    {"nombre": "COM", "vmin": 4.90, "vmax": 5.50, "i": 1.2},
    {"nombre": "Carga util", "vmin": 4.75, "vmax": 5.25, "i": 0.9},
]
margen_min = 0.20
hallazgos = []
print(f"Proveedor: {proveedor['nombre']} salida {proveedor['vmin']}-{proveedor['vmax']} V, maximo {proveedor['imax']} A")
for c in consumidores:
    ok_min = proveedor["vmin"] >= c["vmin"]
    ok_max = proveedor["vmax"] <= c["vmax"]
    print(f"  {c['nombre']:11s} acepta {c['vmin']}-{c['vmax']} V -> minimo {'OK' if ok_min else 'FALLA'} ; maximo {'OK' if ok_max else 'FALLA'}")
    if not ok_min:
        hallazgos.append(f"{c['nombre']}: tension minima")
    if not ok_max:
        hallazgos.append(f"{c['nombre']}: tension maxima")
itot = sum(c["i"] for c in consumidores)
margen = 1 - itot / proveedor["imax"]
print(f"Corriente total = {itot:.2f} A ; margen = {margen * 100:.1f} % (minimo de ejemplo {margen_min * 100:.0f} %)")
if margen < margen_min:
    hallazgos.append("margen de corriente")
print("Hallazgos:", "; ".join(hallazgos) if hallazgos else "ninguno")
comprobar(hallazgos == ["COM: tension minima", "margen de corriente"], "el ICD de ejemplo debe tener exactamente estos dos hallazgos")

# Mecanica: desplazamiento posicional acumulado de 4 contribuciones (mm, +-)
tol = np.array([0.05, 0.10, 0.10, 0.15])
wc = tol.sum()
rss = math.sqrt((tol**2).sum())
rng = np.random.default_rng(90)
N = 2_000_000
muestras = rng.uniform(-tol, tol, size=(N, 4)).sum(axis=1)
sigma_mc = muestras.std()
print(f"Apilamiento: peor caso = +-{wc:.3f} mm ; RSS = +-{rss:.4f} mm ; sigma Monte Carlo = {sigma_mc:.4f} mm")
comprobar(abs(sigma_mc - rss / math.sqrt(3)) < 5e-4, "la sigma de uniformes debe ser RSS/sqrt(3)")
d_perno, d_agujero = 3.0, 3.5
holgura = (d_agujero - d_perno) / 2
p_falla = float(np.mean(np.abs(muestras) > holgura))
print(f"Holgura radial = {holgura:.2f} mm : peor caso {'CUMPLE' if wc <= holgura else 'NO CUMPLE'} ; RSS {'CUMPLE' if rss <= holgura else 'NO CUMPLE'} ; P(interferencia) Monte Carlo = {p_falla:.2e}")
comprobar(wc > holgura and rss < holgura, "el caso de ejemplo separa el peor caso del estadistico")
# P teorica por convolucion numerica de las 4 uniformes
paso = 0.0002
d = None
for t in tol:
    k = np.ones(int(round(2 * t / paso)) + 1)
    k /= k.sum()
    d = k if d is None else np.convolve(d, k)
x = np.arange(len(d)) * paso - wc
p_conv = float(d[np.abs(x) > holgura + paso / 2].sum())
print(f"P(interferencia) por convolucion numerica = {p_conv:.2e}")
comprobar(abs(p_conv - p_falla) < 6e-4, "convolucion y Monte Carlo deben coincidir")
fin()
