#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C20: proyecto mecanico completo: presupuesto de frente de onda y de apuntado con RSS y Monte Carlo, y comprobacion de la frecuencia estructural.

Datos: ILUSTRATIVOS todos (telescopio de 200 mm f/5, lambda = 550 nm; contribuciones de error de los componentes; requisito de Strehl >= 0,8; rigidez lateral 2,54e6 N/m y masa 8 kg tomadas del ejemplo de C10; ancho de banda del servo de C15).
No se usan datos medidos ni de instrumentos reales. Semilla 20261109.
Modelo: errores independientes de media nula se suman en cuadratura (RSS); Strehl de Marechal S = exp(-(2 pi sigma/lambda)^2); sigma maximo para S = 0,8 es lambda sqrt(-ln 0,8)/(2 pi).
Las distribuciones de la simulacion son mezcla de gaussianas y uniformes (sigma = a/sqrt(3)); la RSS no depende de la forma. Frecuencia estructural f = sqrt(k/m)/(2 pi), con criterio f >= 4 f_servo.
Supuestos: independencia estadistica, errores pequenos, sin terminos cruzados. Validez: presupuesto de primer orden.
Tolerancia: Monte Carlo (400000 muestras) frente a RSS, 0,5 % relativo.
"""
from __future__ import annotations
import math, platform, random

LAM = 550.0
FRENTE = [  # (nombre, sigma de frente de onda en nm RMS, distribucion)
    ("figura del primario (superficie 8 nm x 2)", 16.0, "g"), ("figura del secundario plano", 10.0, "g"),
    ("apoyo axial del primario", 8.0, "g"), ("deformacion termica", 10.0, "u"),
    ("colimacion residual", 12.0, "u"), ("flexion del tubo", 6.0, "u")]
APUNTADO = [  # arcsec RMS
    ("error periodico residual", 2.0, "g"), ("alineacion polar residual", 1.5, "u"), ("codificador y cuantizacion", 0.5, "g"),
    ("flexion de la montura", 1.0, "u"), ("viento", 1.2, "g")]

def rss(lst):
    return math.sqrt(sum(v * v for _, v, _ in lst))

def mc(lst, n=400000, seed=20261109):
    rng = random.Random(seed)
    acc = 0.0
    for _ in range(n):
        s = 0.0
        for _, v, d in lst:
            s += rng.gauss(0, v) if d == "g" else rng.uniform(-v * math.sqrt(3), v * math.sqrt(3))
        acc += s * s
    return math.sqrt(acc / n)

def calc():
    r = {}
    r["frente_rss"] = rss(FRENTE); r["frente_mc"] = mc(FRENTE)
    r["strehl"] = math.exp(-(2 * math.pi * r["frente_rss"] / LAM) ** 2)
    r["sigma_max"] = LAM * math.sqrt(-math.log(0.8)) / (2 * math.pi)
    r["margen_nm"] = r["sigma_max"] - r["frente_rss"]
    r["apunt_rss"] = rss(APUNTADO); r["apunt_mc"] = mc(APUNTADO, seed=20261110)
    r["f_estructura_hz"] = math.sqrt(2.54e6 / 8.0) / (2 * math.pi)
    wn = math.sqrt(1.0 / 0.01)  # servo C15
    r["f_servo_hz"] = wn / (2 * math.pi)
    r["razon_f"] = r["f_estructura_hz"] / r["f_servo_hz"]
    mayor = max(FRENTE, key=lambda x: x[1])
    r["mayor"] = mayor[0]; r["fraccion_mayor"] = mayor[1] ** 2 / r["frente_rss"] ** 2
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    print("fuente | sigma (nm) | cuota de varianza")
    t = r["frente_rss"] ** 2
    for n, v, d in FRENTE:
        print(f"{n} | {v:.1f} | {v * v / t * 100:.1f} %")
    for k in ("frente_rss", "frente_mc", "strehl", "sigma_max", "margen_nm", "apunt_rss", "apunt_mc", "f_estructura_hz", "f_servo_hz", "razon_f", "fraccion_mayor"):
        print(f"{k} = {r[k]:.6g}")
    assert abs(r["frente_mc"] - r["frente_rss"]) / r["frente_rss"] < 0.005
    assert abs(r["apunt_mc"] - r["apunt_rss"]) / r["apunt_rss"] < 0.005
    assert r["strehl"] > 0.8 and r["razon_f"] > 4
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
