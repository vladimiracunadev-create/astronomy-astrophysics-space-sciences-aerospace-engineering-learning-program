#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B54-C18: funciones de peso de un sondeo infrarrojo y recuperacion de la altura de escala por ocultacion.

Datos: TODOS SINTETICOS (no son observaciones): atmosfera isoterma con H = 8.5 km (valor de la ficha NASA/NSSDC de la Tierra, consulta 2026-11-09),
tres canales con coeficientes de absorcion ficticios, ruido gaussiano de semilla fija (12345, generador de Python).
Modelo: nadir, transmision hacia el espacio tau(z) = k n(z) H ; funcion de peso W(z) = d exp(-tau)/dz = (k n(z)) exp(-tau); su maximo esta en tau = 1, z_m = H ln(k n0 H).
Ocultacion: transmision T(p) = exp(-tau(p)) a lo largo de la tangente; densidad exponencial; ajuste lineal de ln(-ln T) frente a la altura tangente.
Supuestos: monocromatico, atmosfera esferica reemplazada por plano-paralela (corregida con el factor sqrt(2 pi R H) en la columna oblicua, formula aproximada).
Tolerancias: maximo de W frente a H ln(k n0 H) 0.5 % de H; H recuperado con ruido 1 % entre 5 repeticiones sin sesgo sistematico (|media - H| < 3 sigma de la media).
"""
import math, platform, random
print(f"Python {platform.python_version()} (biblioteca estandar)")
H, n0 = 8500.0, 2.5e25
print("canal   k [m2]   z_m analitico [km]   z_m numerico [km]   W_max [1/km]")
for nombre, k in (("A", 3 / (n0 * H)), ("B", 20 / (n0 * H)), ("C", 150 / (n0 * H))):
    zm = H * math.log(k * n0 * H)
    best, wb = 0.0, 0.0
    for i in range(0, 80001, 5):
        z = float(i); n = n0 * math.exp(-z / H); tau = k * n * H
        w = k * n * math.exp(-tau)
        if w > wb: wb, best = w, z
    print(f"{nombre:5s} {k:9.2e} {zm/1e3:17.3f} {best/1e3:18.3f} {wb*1e3:13.4f}")
    assert abs(best - zm) < 0.005 * H
    # normalizacion: la integral de W entre 0 y infinito vale 1 - exp(-tau_0)
# normalizacion de W por canal B
k = 20 / (n0 * H)
tot = sum(k * n0 * math.exp(-z / H) * math.exp(-k * n0 * math.exp(-z / H) * H) for z in [float(i) for i in range(0, 200001, 5)]) * 5.0
print(f"Integral de W (canal B) = {tot:.5f} (esperado 1 - exp(-tau0) = {1-math.exp(-k*n0*H):.5f})")
assert abs(tot - (1 - math.exp(-k * n0 * H))) < 1e-3
# ocultacion sintetica
rng = random.Random(12345)
Hest = []
for rep in range(5):
    hs = [10e3 + 2e3 * i for i in range(15)]    # 10-38 km
    y = []
    for h in hs:
        tau = 3.0e-4 * math.exp(-(h - 10e3) / H) * 40.0       # columna oblicua sintetica normalizada
        T = math.exp(-tau) * (1 + rng.gauss(0, 1e-4))
        y.append(math.log(-math.log(T)))
    xm, ym = sum(hs) / len(hs), sum(y) / len(y)
    b = sum((x - xm) * (v - ym) for x, v in zip(hs, y)) / sum((x - xm) ** 2 for x in hs)
    Hest.append(-1 / b)
mu = sum(Hest) / 5; sd = (sum((h - mu) ** 2 for h in Hest) / 4) ** 0.5
print("H recuperado por repeticion [m]:", " ".join(f"{h:.0f}" for h in Hest))
print(f"media = {mu:.1f} m ; desviacion = {sd:.1f} m ; H verdadero (sintetico) = {H:.0f} m")
assert abs(mu - H) < 3 * sd / math.sqrt(5) + 0.01 * H
print("Pruebas superadas.")
