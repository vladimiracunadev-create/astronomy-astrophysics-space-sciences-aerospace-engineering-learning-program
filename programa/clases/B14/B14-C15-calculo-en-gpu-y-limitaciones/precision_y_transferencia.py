#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C15: lo que cambia al pasar a GPU, sin GPU.

AVISO: este laboratorio NO USA GPU (la máquina de redacción no tiene una
configurada). Reproduce en CPU dos efectos que la documentación de NVIDIA
señala como causas de diferencias CPU/GPU: (1) el orden de la suma (una
reducción en árbol, como hacen los núcleos paralelos, frente a la secuencial)
y (2) la multiplicación-suma fusionada (FMA, un solo redondeo). Y evalúa con un
MODELO ANALÍTICO con parámetros SINTÉTICOS si compensa transferir los datos.
Datos: SINTÉTICOS. 1 000 000 de números float32 ~ N(1, 0.01), semilla 20261105.
Modelo de transferencia: t_GPU = t_transf + t_calc_GPU; t_CPU = t_calc_CPU;
parámetros inventados: ancho de banda 12 GB/s, 40 operaciones por elemento,
CPU 20 Gflop/s, GPU 2000 Gflop/s. No son medidas de ningún equipo.
Tolerancia: la referencia es float64; la suma en árbol de float32 debe tener
menor error que la secuencial de float32; el FMA simulado debe ser igual al
redondeo único de un cálculo exacto en float64.
"""
from __future__ import annotations
import platform, sys
import numpy as np


def suma_secuencial32(x):
    s = np.float32(0.0)
    for v in x:
        s = np.float32(s + v)
    return s


def suma_arbol32(x):
    v = x.astype(np.float32).copy()
    while v.size > 1:
        if v.size % 2:
            v = np.append(v, np.float32(0.0))
        v = (v[0::2] + v[1::2]).astype(np.float32)
    return v[0]


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  (sin GPU)")
    rng = np.random.default_rng(20261105)
    x = rng.normal(1.0, 0.01, 1_000_000).astype(np.float32)
    ref = float(np.sum(x.astype(np.float64)))
    xs = x[:200_000]                              # el bucle secuencial en Python es lento
    ref_s = float(np.sum(xs.astype(np.float64)))
    s_seq = float(suma_secuencial32(xs))
    s_arb = float(suma_arbol32(xs))
    e_seq, e_arb = abs(s_seq - ref_s) / ref_s, abs(s_arb - ref_s) / ref_s
    print(f"suma de 200 000 float32: referencia float64 = {ref_s:.4f}")
    print(f"  secuencial float32: error relativo = {e_seq:.2e}")
    print(f"  en árbol float32:   error relativo = {e_arb:.2e}")
    prueba(e_arb < e_seq, "la suma en árbol debe ser más exacta que la secuencial en float32")
    prueba(s_seq != s_arb, "distinto orden, distinto resultado")

    # FMA simulado: a*b + c con un solo redondeo frente a dos
    a = rng.normal(1.0, 0.1, 100_000).astype(np.float32)
    b = rng.normal(1.0, 0.1, 100_000).astype(np.float32)
    c = (-a * b).astype(np.float32)               # casi cancela: expone la diferencia
    dos_redondeos = (a * b).astype(np.float32) + c           # multiplicar y redondear, luego sumar
    exacto = a.astype(np.float64) * b.astype(np.float64) + c.astype(np.float64)
    un_redondeo = exacto.astype(np.float32)                    # FMA: un solo redondeo
    err2 = np.max(np.abs(dos_redondeos.astype(np.float64) - exacto))
    err1 = np.max(np.abs(un_redondeo.astype(np.float64) - exacto))
    print(f"a*b+c con casi-cancelación: error máx. con dos redondeos = {err2:.2e}; con un redondeo (FMA simulado) = {err1:.2e}")
    prueba(err1 <= err2, "un solo redondeo no puede ser peor")
    prueba(np.array_equal(un_redondeo, exacto.astype(np.float32)), "FMA simulado = redondeo único")
    print(f"resultados idénticos entre ambos métodos: {bool(np.array_equal(dos_redondeos, un_redondeo))}")

    # modelo de transferencia con parámetros sintéticos
    bw, ops, cpu, gpu = 12e9, 40.0, 20e9, 2000e9
    print("modelo sintético (no medido): n, t_CPU, t_GPU(con transferencia), ¿compensa?")
    resultados = []
    for n in (1e3, 1e5, 1e7, 1e9):
        t_cpu = n * ops / cpu
        t_gpu = (2 * n * 4) / bw + n * ops / gpu        # ida y vuelta de n float32 (4 bytes)
        resultados.append((n, t_cpu, t_gpu))
        print(f"  n={n:.0e}: t_CPU = {t_cpu:.2e} s; t_GPU = {t_gpu:.2e} s; compensa = {t_gpu < t_cpu}")
    # con estos parametros t_gpu/t_cpu es independiente de n; se muestra la razon asintotica
    razon = ((2 * 4) / bw + ops / gpu) / (ops / cpu)
    print(f"razón t_GPU/t_CPU = {razon:.3f} para cualquier n (sin latencias fijas): la transferencia domina si las operaciones por elemento son pocas")
    ops_min = (2 * 4 / bw) / (1 / cpu - 1 / gpu)
    print(f"operaciones por elemento mínimas para que compense = {ops_min:.1f}")
    prueba(abs(((2 * 4) / bw + ops_min / gpu) - ops_min / cpu) < 1e-18, "equilibrio analítico")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
