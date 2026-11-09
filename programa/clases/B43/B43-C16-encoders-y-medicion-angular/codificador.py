#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B43-C16: encoders y medicion angular: cuantizacion, codigo Gray e interpolacion seno-coseno.

Datos: ILUSTRATIVOS (codificador incremental de 10000 lineas por vuelta con decodificacion en cuadratura x4; codificador absoluto de 12 bits; errores de desfase de 0,01 y de ganancia 0,02 de los canales seno-coseno).
Semilla 20261109 para los angulos aleatorios. Sin datos de fabricantes. 1 vuelta = 1296000" (definicion).
Modelo: cuentas por vuelta = 4 x lineas; paso q = 1296000"/cuentas; error de cuantizacion RMS = q/sqrt(12). Codigo Gray g = b xor (b >> 1); la lectura a mitad de una transicion binaria puede
mezclar bits y dar un error grande, mientras que en Gray solo cambia un bit. Interpolacion theta = atan2(s, c): un desfase o_s del canal seno da un error de primer orden o_s cos(theta); una diferencia de ganancia g da (g/2) sin(2 theta).
Verificacion independiente: Monte Carlo del RMS de cuantizacion; barrido exhaustivo de las 4096 transiciones con todos los ordenes de cambio de bits (peor caso); barrido de 3600 angulos para el error de interpolacion.
Supuestos: senales ideales salvo las perturbaciones indicadas, sin ruido electronico. Validez: perturbaciones pequenas.
Tolerancia: RMS de cuantizacion 1 % relativo; amplitud de los errores de interpolacion 2 % relativo.
"""
from __future__ import annotations
import itertools, math, platform, random

LINEAS = 10000; BITS = 12

def gray(b):
    return b ^ (b >> 1)

def calc():
    r = {}
    cuentas = 4 * LINEAS
    q = 1296000.0 / cuentas
    r["cuentas"] = cuentas; r["q_arcsec"] = q; r["rms_teorico"] = q / math.sqrt(12)
    rng = random.Random(20261109)
    n = 200000; s = 0.0
    for _ in range(n):
        x = rng.uniform(0, 1296000.0)
        e = x - round(x / q) * q
        s += e * e
    r["rms_mc"] = math.sqrt(s / n)
    # Gray
    N = 1 << BITS
    gray_ok = all(bin(gray(i) ^ gray(i + 1)).count("1") == 1 for i in range(N - 1))
    r["gray_un_bit"] = gray_ok
    peor_bin = 0; peor_gray = 0
    for i in range(N - 1):
        for codigos, peor in ((None, None),):
            pass
        a, b = i, i + 1
        dif = a ^ b
        bits = [k for k in range(BITS) if dif >> k & 1]
        for mask in range(1 << len(bits)):
            v = a
            for j, k in enumerate(bits):
                if mask >> j & 1:
                    v ^= 1 << k
            peor_bin = max(peor_bin, min(abs(v - a), abs(v - b)))
        ga, gb = gray(a), gray(b)
        gd = ga ^ gb
        gbits = [k for k in range(BITS) if gd >> k & 1]
        for mask in range(1 << len(gbits)):
            v = ga
            for j, k in enumerate(gbits):
                if mask >> j & 1:
                    v ^= 1 << k
            # decodificar Gray -> binario
            b_ = 0; t = v
            while t:
                b_ ^= t; t >>= 1
            peor_gray = max(peor_gray, min(abs(b_ - a), abs(b_ - b)))
    r["peor_binario_cuentas"] = peor_bin; r["peor_gray_cuentas"] = peor_gray
    # interpolacion
    periodo = 1296000.0 / LINEAS
    os_ = 0.01; g = 0.02
    mx_o = mx_g = 0.0
    for k in range(3600):
        th = 2 * math.pi * k / 3600
        e1 = math.atan2(math.sin(th) + os_, math.cos(th)) - th
        e2 = math.atan2((1 + g) * math.sin(th), math.cos(th)) - th
        e1 = (e1 + math.pi) % (2 * math.pi) - math.pi; e2 = (e2 + math.pi) % (2 * math.pi) - math.pi
        mx_o = max(mx_o, abs(e1)); mx_g = max(mx_g, abs(e2))
    r["err_desfase_arcsec"] = mx_o / (2 * math.pi) * periodo; r["err_desfase_teorico"] = os_ / (2 * math.pi) * periodo
    r["err_ganancia_arcsec"] = mx_g / (2 * math.pi) * periodo; r["err_ganancia_teorico"] = g / 2 / (2 * math.pi) * periodo
    r["periodo_arcsec"] = periodo
    return r

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    r = calc()
    for k, v in r.items():
        print(f"{k} = {v}" if isinstance(v, (bool, int)) else f"{k} = {v:.6g}")
    assert abs(r["rms_mc"] - r["rms_teorico"]) / r["rms_teorico"] < 0.01
    assert r["gray_un_bit"] and r["peor_gray_cuentas"] <= 1 and r["peor_binario_cuentas"] > 1000
    assert abs(r["err_desfase_arcsec"] / r["err_desfase_teorico"] - 1) < 0.02
    assert abs(r["err_ganancia_arcsec"] / r["err_ganancia_teorico"] - 1) < 0.02
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
