#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C07: HDF5 con grupos, atributos, fragmentación y compresión.

Datos: SINTÉTICOS. Curva de luz de 200 000 muestras (cadencia 2 s) de una
fuente ficticia: tránsito trapezoidal de profundidad 0.01, centrado en
t = 200 000 s, duración total 8 000 s con ingreso y egreso de 1 000 s, más
ruido gaussiano de 0.002 (semilla fija 20261105), en flujo relativo
adimensional. No es una observación real.
Modelo: el flujo se guarda en float64 en /curva/flujo con atributos (unidad,
cadencia, procedencia) y se compara una versión sin comprimir con otra
fragmentada y comprimida con gzip.
Supuestos: se usa h5py; la compresión depende de la entropía de los datos
(el ruido comprime mal; el modelo sin ruido comprime bien).
Validez: demostración de estructura; las razones de compresión valen solo
para estos datos.
Tolerancia: ida y vuelta EXACTA (np.array_equal) tras compresión sin pérdida;
lectura parcial idéntica a la rebanada en memoria; profundidad estimada
dentro de 1.5e-3 de la verdadera.
"""
from __future__ import annotations
import os, platform, sys, tempfile
import numpy as np
import h5py


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}  h5py {h5py.__version__}  HDF5 {h5py.version.hdf5_version}")
    rng = np.random.default_rng(20261105)
    n, dt = 200_000, 2.0
    t = np.arange(n) * dt
    medio, dur, ing, prof = 200_000.0, 8000.0, 1000.0, 0.01
    x = np.abs(t - medio)
    modelo = 1.0 - prof * np.clip((dur / 2 - x) / ing, 0.0, 1.0)
    flujo = modelo + rng.normal(0.0, 0.002, n)

    with tempfile.TemporaryDirectory() as td:
        ruta = os.path.join(td, "demo.h5")
        with h5py.File(ruta, "w") as f:
            g = f.create_group("curva")
            g.create_dataset("tiempo", data=t)
            g.create_dataset("flujo_sin_comprimir", data=flujo)
            g.create_dataset("flujo", data=flujo, chunks=(10_000,), compression="gzip", compression_opts=4)
            g.create_dataset("modelo", data=modelo, chunks=(10_000,), compression="gzip", compression_opts=4)
            g["flujo"].attrs["unidad"] = "relativo (adimensional)"
            g["flujo"].attrs["cadencia_s"] = dt
            g["flujo"].attrs["procedencia"] = "sintético, semilla 20261105"
            f.attrs["version_formato"] = "1"
        print(f"tamaño del archivo = {os.path.getsize(ruta)/1e6:.3f} MB")
        with h5py.File(ruta, "r") as f:
            nombres = []
            f.visit(nombres.append)
            print("estructura:", nombres)
            d = f["curva/flujo"]
            print(f"flujo: shape={d.shape} dtype={d.dtype} chunks={d.chunks} compression={d.compression}")
            print("atributos:", dict(d.attrs))
            prueba(np.array_equal(d[...], flujo), "ida y vuelta exacta con gzip")
            lo, hi = 95_000, 105_000
            prueba(np.array_equal(d[lo:hi], flujo[lo:hi]), "lectura parcial")
            m = f["curva/modelo"][...]
            pmax = 1.0 - m.min()
            print(f"profundidad del modelo = {pmax:.6f} (esperada {prof})")
            prueba(abs(pmax - prof) < 1e-12, "profundidad del modelo")
            interior = np.abs(t - medio) < (dur / 2 - ing)
            fuera = np.abs(t - medio) > dur
            est = np.median(flujo[fuera]) - np.median(flujo[interior])
            print(f"profundidad estimada de los datos = {est:.5f} (verdadera {prof})")
            prueba(abs(est - prof) < 1.5e-3, "profundidad estimada")
            b_raw = f["curva/flujo_sin_comprimir"].id.get_storage_size()
            b_gz = d.id.get_storage_size()
            b_mod = f["curva/modelo"].id.get_storage_size()
            print(f"bytes: sin comprimir = {b_raw}; con gzip = {b_gz} (razón {b_raw/b_gz:.2f}); "
                  f"modelo sin ruido con gzip = {b_mod} (razón {b_raw/b_mod:.1f})")
            prueba(b_mod < b_gz, "el modelo sin ruido comprime mejor que el flujo con ruido")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
