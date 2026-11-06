#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B18-C03: disposición de arreglos, caché y ancho de banda.

Datos: SINTÉTICOS (arreglos de ceros, unos y np.arange; sin datos observados).
Modelo: un ndarray es un bloque contiguo de bytes con pasos (strides); en
orden C, strides[k] = itemsize * prod(shape[k+1:]) (NumPy, ndarray, sección
de disposición interna). El coste de recorrer depende de cuántas líneas de
caché (típicamente 64 B) se traen por cada valor útil.
Mediciones: tiempo mínimo de varias repeticiones (time.perf_counter).
Supuestos: máquina con otros procesos en marcha (los tiempos son ruidosos);
las razones entre tiempos importan más que los valores absolutos.
Validez: demostración cualitativa del efecto de la localidad; NO es un
benchmark certificado ni equivale a STREAM oficial (otra implementación, otro
compilador y tamaños distintos).
Tolerancias: sumas exactas (enteros representables en float64); fórmulas de
strides exactas; los tiempos no se comparan con umbrales.
"""
from __future__ import annotations
import platform, sys, time
import numpy as np


def mejor(f, rep: int = 5) -> float:
    t = []
    for _ in range(rep):
        t0 = time.perf_counter(); f(); t.append(time.perf_counter() - t0)
    return min(t)


def prueba(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def strides_c(shape, itemsize):
    out, acc = [], itemsize
    for n in reversed(shape):
        out.append(acc); acc *= n
    return tuple(reversed(out))


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  NumPy {np.__version__}")

    # 1) Strides: fórmula frente a lo que informa NumPy.
    a = np.zeros((3000, 2000), dtype="f8")
    prueba(a.strides == strides_c(a.shape, 8) == (16000, 8), "strides C")
    f = np.asfortranarray(a)
    prueba(f.strides == (8, 24000), "strides Fortran")
    prueba(a.T.strides == (8, 16000) and not a.T.flags["C_CONTIGUOUS"], "traspuesta es vista")
    print(f"strides C={a.strides}  Fortran={f.strides}  traspuesta(vista)={a.T.strides}")

    # 2) Recorrido por filas frente a por columnas (misma suma, distinto orden).
    n = 3000
    m = np.arange(n * n, dtype="f8").reshape(n, n)
    exacto = (n * n) * (n * n - 1) / 2          # suma de 0..n^2-1
    prueba(m.sum() == exacto, "suma total exacta")
    t_fil = mejor(lambda: sum(m[i, :].sum() for i in range(n)))
    t_col = mejor(lambda: sum(m[:, j].sum() for j in range(n)))
    print(f"matriz {n}x{n} float64 ({m.nbytes/1e6:.0f} MB): por filas {t_fil*1e3:7.1f} ms | por columnas {t_col*1e3:7.1f} ms | razón {t_col/t_fil:4.2f}")

    # 3) Saltos: leer cada k-ésimo elemento; ¿baja el tiempo como 1/k?
    x = np.ones(2 ** 24)
    t1 = None
    print("saltos k | elementos leídos | tiempo (ms) | ns por elemento leído")
    for k in (1, 2, 4, 8, 16):
        v = x[::k]
        t = mejor(lambda v=v: v.sum())
        prueba(v.sum() == len(v), "suma de unos exacta")
        if t1 is None: t1 = t
        print(f"{k:8d} | {len(v):16d} | {t*1e3:11.2f} | {t/len(v)*1e9:8.2f}")

    # 4) Disposición de estructuras: AoS frente a SoA.
    N = 2 ** 21
    aos = np.zeros(N, dtype=[("x", "f8"), ("y", "f8"), ("vx", "f8"), ("vy", "f8")])
    aos["x"] = np.arange(N)
    soa_x = np.arange(N, dtype="f8")
    prueba(aos.itemsize == 32 and aos["x"].strides == (32,), "AoS: 32 B por registro")
    esperado = N * (N - 1) / 2
    prueba(aos["x"].sum() == esperado and soa_x.sum() == esperado, "suma de x exacta")
    t_aos = mejor(lambda: aos["x"].sum()); t_soa = mejor(lambda: soa_x.sum())
    print(f"suma de x con N={N}: AoS (paso 32 B) {t_aos*1e3:6.2f} ms | SoA (paso 8 B) {t_soa*1e3:6.2f} ms | razón {t_aos/t_soa:4.2f}")

    # 5) Ancho de banda efectivo (nominal): copia y suma de arreglos grandes.
    L = 2 ** 23                                  # 64 MB por arreglo, > caché L3 de la máquina
    b = np.ones(L); c = np.full(L, 2.0); d = np.empty(L)
    t_cp = mejor(lambda: np.copyto(d, b))
    prueba(bool((d == 1.0).all()), "copia correcta")
    t_ad = mejor(lambda: np.add(b, c, out=d))
    prueba(bool((d == 3.0).all()), "suma correcta")
    print(f"copia (16 B/elem): {16*L/t_cp/1e9:5.1f} GB/s | suma d=b+c (24 B/elem): {24*L/t_ad/1e9:5.1f} GB/s  (nominal, 3 arreglos de {b.nbytes/1e6:.0f} MB)")

    # 6) Traspuesta con copia: lee contiguo y escribe con salto.
    t_cc = mejor(lambda: m.copy())
    t_tc = mejor(lambda: np.ascontiguousarray(m.T))
    prueba(np.array_equal(np.ascontiguousarray(m.T).T, m), "traspuesta correcta")
    print(f"copiar {n}x{n}: contigua {t_cc*1e3:6.1f} ms | traspuesta {t_tc*1e3:6.1f} ms | razón {t_tc/t_cc:4.2f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
