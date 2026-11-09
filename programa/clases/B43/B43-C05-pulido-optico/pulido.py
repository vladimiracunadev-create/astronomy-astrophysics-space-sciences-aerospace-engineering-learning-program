#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C05: pulido optico: ley de Preston, tiempo de permanencia y paso de la esfera al paraboloide.

Datos: ILUSTRATIVOS (espejo de D = 200 mm, R = 2400 mm; coeficiente de Preston k_P = 1e-12 Pa^-1, presion 5 kPa, velocidad relativa 0,1 m/s; funcion de influencia gaussiana de sigma 8 mm; mapa de errores sintetico con semilla 20261109).
Ninguno es un valor medido ni consultado.
Modelo: ley de Preston dZ/dt = k_P P v. Desviacion paraboloide-esfera por diferencia exacta de sagitas y aproximada y^4/(8 R^3); desviacion minima respecto de la mejor esfera (se permite cambiar R, es decir enfocar) buscando c que minimiza el PV de rho^4 - c rho^2.
Correccion por tiempo de permanencia: removal = g * t (convolucion gaussiana), t >= 0, resuelta por descenso de gradiente proyectado. Verificacion con un caso exacto: el objetivo se construye como g * t_verdadero.
Supuestos: perfil 1D, funcion de influencia invariante, sin bordes. Validez: ilustrativa de la logica de la correccion determinista, no un proceso de taller.
Tolerancia: tasa de Preston analitica; diferencia exacta frente a y^4/(8R^3), 1 % en el borde; caso exacto de permanencia, residuo < 2 % del objetivo; error de forma tras corregir menor que 25 % del inicial.
"""
from __future__ import annotations
import math, platform, random

R = 2.4; A = 0.1
KP = 1e-12; P = 5e3; V = 0.1

def sag(y, R):
    return y * y / (R + math.sqrt(R * R - y * y))

def conv(g, t):
    n = len(t); m = len(g) // 2
    return [sum(g[k] * t[i + k - m] for k in range(len(g)) if 0 <= i + k - m < n) for i in range(n)]

def resolver(g, obj, it=1500):
    n = len(obj); t = [0.0] * n
    gs = sum(g)
    mu = 1.0 / (gs * gs)
    for _ in range(it):
        r = conv(g, t)
        e = [r[i] - obj[i] for i in range(n)]
        gr = conv(g, e)  # g simetrico
        t = [max(0.0, t[i] - mu * 1.0 * gr[i]) for i in range(n)]
    return t

def rms(v):
    m = sum(v) / len(v)
    return math.sqrt(sum((x - m) ** 2 for x in v) / len(v))

def calc():
    r = {}
    r["tasa_nm_s"] = KP * P * V * 1e9; r["tasa_um_h"] = KP * P * V * 3600 * 1e6
    dif_exacta = sag(A, R) - A * A / (2 * R)  # esfera menos paraboloide
    r["dif_borde_nm"] = dif_exacta * 1e9
    r["dif_aprox_nm"] = A ** 4 / (8 * R ** 3) * 1e9
    best = None
    cs = [0.5 + 0.0005 * i for i in range(1500)]
    for c in cs:
        vals = [(u * u - c * u) for u in [k / 400 for k in range(401)]]
        pv = max(vals) - min(vals)
        if best is None or pv < best[1]:
            best = (c, pv)
    r["c_optimo"] = best[0]; r["pv_rel"] = best[1]
    r["pv_mejor_esfera_nm"] = best[1] * A ** 4 / (8 * R ** 3) * 1e9
    r["ondas_pv_550"] = r["pv_mejor_esfera_nm"] / 550.0
    r["tiempo_borde_h"] = r["pv_mejor_esfera_nm"] / r["tasa_nm_s"] / 3600
    # permanencia
    n = 81; dx = 1.0  # mm
    sg = 8.0
    g = [math.exp(-0.5 * ((k - 20) * dx / sg) ** 2) for k in range(41)]
    g = [x / sum(g) for x in g]
    tv = [0.0] * n
    for c, a_ in ((20, 3.0), (45, 5.0), (65, 2.0)):
        for i in range(n):
            tv[i] += a_ * math.exp(-0.5 * ((i - c) / 3.0) ** 2)
    obj = conv(g, tv)
    t = resolver(g, obj)
    res = [conv(g, t)[i] - obj[i] for i in range(n)]
    r["caso_exacto_residuo_rel"] = rms(res) / rms(obj)
    rng = random.Random(20261109)
    suave = [0.0] * n
    for k in range(6):
        a_ = rng.uniform(5, 40); ph = rng.uniform(0, 2 * math.pi); per = rng.uniform(20, 80)
        for i in range(n):
            suave[i] += a_ * math.sin(2 * math.pi * i / per + ph) / 6
    mn = min(suave)
    err = [s - mn for s in suave]
    t2 = resolver(g, err)
    rem = conv(g, t2)
    resid = [err[i] - rem[i] for i in range(n)]
    r["rms_inicial_nm"] = rms(err); r["rms_final_nm"] = rms(resid)
    r["reduccion"] = rms(resid) / rms(err)
    r["tiempo_total_rel"] = sum(t2) / n
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        print(f"{k} = {v:.6g}")
    assert abs(r["tasa_nm_s"] - 0.5) < 1e-12
    assert abs(r["dif_borde_nm"] - r["dif_aprox_nm"]) / r["dif_aprox_nm"] < 0.01
    assert abs(r["pv_rel"] - 0.25) < 1e-3
    assert r["caso_exacto_residuo_rel"] < 0.02
    assert r["reduccion"] < 0.25
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
