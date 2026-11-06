#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B14-C27: procesar por teselas con borde (halo) y comparar con el cálculo completo.

Datos: SINTÉTICOS. Una imagen de 512 x 512 con una función conocida (rampa +
senoide + ruido gaussiano de 1.0, semilla 20261105). El «gran volumen» se
simula: el cálculo por teselas nunca necesita más de una tesela con su borde en
memoria de trabajo.
Modelo: filtro de promedio 5 x 5 (radio 2) con bordes replicados. Se calcula
(a) sobre la imagen completa y (b) por teselas de 128 x 128 con un borde
(halo) de 2 píxeles, y (c) por teselas SIN borde (error esperado en las costuras).
Supuestos: la imagen cabe en memoria SOLO para poder comparar; el método por
teselas no la necesita entera.
Validez: demostración; cada operación necesita un halo adecuado a su alcance.
Tolerancia: con halo, el resultado por teselas debe ser IDÉNTICO (np.array_equal
hasta 1e-12) al completo; sin halo, el error debe aparecer SOLO en los píxeles
a 2 o menos píxeles de una costura interior.
"""
from __future__ import annotations
import platform, sys
import numpy as np

N, T, R = 512, 128, 2


def datos():
    rng = np.random.default_rng(20261105)
    f, c = np.mgrid[0:N, 0:N].astype(np.float64)
    return 0.1 * c + 0.05 * f + 5.0 * np.sin(c / 30.0) + rng.normal(0, 1.0, (N, N))


def promedio(a, r=R):
    """Promedio (2r+1)x(2r+1) con bordes replicados, solo con NumPy."""
    p = np.pad(a, r, mode="edge")
    out = np.zeros(a.shape, dtype=np.float64)
    for di in range(2 * r + 1):
        for dj in range(2 * r + 1):
            out += p[di:di + a.shape[0], dj:dj + a.shape[1]]
    return out / (2 * r + 1) ** 2


def por_teselas(img, halo):
    out = np.empty_like(img)
    max_elem = 0
    for i in range(0, N, T):
        for j in range(0, N, T):
            i0, i1 = max(0, i - halo), min(N, i + T + halo)
            j0, j1 = max(0, j - halo), min(N, j + T + halo)
            bloque = img[i0:i1, j0:j1]
            max_elem = max(max_elem, bloque.size)
            res = promedio(bloque)
            out[i:i + T, j:j + T] = res[i - i0:i - i0 + T, j - j0:j - j0 + T]
    return out, max_elem


def prueba(cond, msg):
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}")
    img = datos()
    ref = promedio(img)
    con, mc = por_teselas(img, R)
    sin, _ = por_teselas(img, 0)
    print(f"con halo de {R} píxeles: máxima diferencia con el cálculo completo = {np.max(np.abs(con - ref)):.2e}")
    prueba(np.allclose(con, ref, rtol=0, atol=1e-12), "con halo = completo")
    d = np.abs(sin - ref) > 1e-12
    print(f"sin halo: {int(d.sum())} píxeles distintos de {N*N} ({d.sum()/(N*N):.2%}); máxima diferencia = {np.max(np.abs(sin - ref)):.3f}")
    # los píxeles afectados deben estar a <= R píxeles de una costura interior
    costuras = np.arange(T, N, T)
    fil, col = np.nonzero(d)
    def dist_costura(v):
        return np.min(np.abs(v[:, None] - costuras[None, :] + 0.5), axis=1)
    cerca = (dist_costura(fil) <= R + 0.5) | (dist_costura(col) <= R + 0.5)
    prueba(bool(cerca.all()), "las diferencias están solo junto a las costuras")
    prueba(int(d.sum()) > 0, "sin halo debe haber error")
    esperado = 3 * 2 * R * N * 2 - 3 * 3 * 2 * R * 2 * R * 2     # costuras: bandas de 2R en cada sentido menos intersecciones
    print(f"las diferencias están solo a <= {R} píxeles de una costura interior (verificado)")
    print(f"memoria de trabajo por tesela con halo: {mc} elementos = {mc/(N*N):.1%} de la imagen completa")
    prueba(mc == (T + 2 * R) ** 2, "bloque interior de (T+2R)^2")
    # coste del halo
    sobrecoste = (T + 2 * R) ** 2 / T**2 - 1
    print(f"sobrecoste de procesar el halo: {sobrecoste:.1%} (de (T+2R)^2 frente a T^2)")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
