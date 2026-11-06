#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B18-C05: experimentos de escalabilidad (Amdahl y Gustafson).

Datos: (a) modelo analítico SIMULADO (tiempos sintéticos T(N) = T1*(s+(1-s)/N));
(b) mediciones REALES en esta máquina de un lote de órbitas circulares
(unidades canónicas, leapfrog en Python puro) repartido con multiprocessing.
Definiciones (se deducen en la clase):
  Amdahl (escalado fuerte, trabajo fijo):  S(N) = 1 / (s + (1-s)/N)
  Gustafson (escalado débil, trabajo ~ N): S_G(N) = N - s*(N-1)
  Karp-Flatt: e(N) = (1/S - 1/N) / (1 - 1/N), estima la fracción serial.
Supuestos: s = fracción serial medida sobre el tiempo en 1 proceso; sin
interferencia entre procesos (no se cumple en una máquina cargada).
Validez: las mediciones reales son ruidosas (la máquina comparte CPU con
otros procesos y solo tiene 4 núcleos físicos); sirven para practicar el
método, no para caracterizar el hardware.
Tolerancias: fórmulas exactas a 1e-12; Karp-Flatt recupera s del modelo
sintético a 1e-12; el resultado numérico del lote real es idéntico en serie
y en paralelo (bit a bit).
"""
from __future__ import annotations
import math, os, platform, sys, time
from multiprocessing import Pool


def amdahl(s: float, n: float) -> float:
    return 1.0 / (s + (1.0 - s) / n)


def gustafson(s: float, n: float) -> float:
    return n - s * (n - 1.0)


def karp_flatt(speedup: float, n: int) -> float:
    return (1.0 / speedup - 1.0 / n) / (1.0 - 1.0 / n)


def propagar(pasos: int) -> tuple[float, float]:
    dt = 2 * math.pi / pasos
    x, y, vx, vy = 1.0, 0.0, 0.0, 1.0
    r3 = 1.0
    ax, ay = -x, -y
    for _ in range(pasos):
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
        x += dt * vx; y += dt * vy
        r3 = (x * x + y * y) ** 1.5
        ax, ay = -x / r3, -y / r3
        vx += 0.5 * dt * ax; vy += 0.5 * dt * ay
    return x, y


def prueba(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"PRUEBA FALLIDA: {msg}")


def tiempo_lote(pool, tareas: int, pasos: int, trozo: int = 1):
    t0 = time.perf_counter()
    r = pool.map(propagar, [pasos] * tareas, chunksize=trozo)
    return r, time.perf_counter() - t0


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    print(f"Python {platform.python_version()}  CPU lógicas={os.cpu_count()}")

    # 1) Fórmulas contra valores exactos.
    prueba(abs(amdahl(0.05, 8) - 1 / (0.05 + 0.95 / 8)) < 1e-12, "Amdahl N=8")
    prueba(abs(amdahl(0.05, 1) - 1.0) < 1e-12, "Amdahl N=1")
    prueba(abs(amdahl(0.05, 1e12) - 20.0) < 1e-6, "límite 1/s = 20")
    prueba(abs(gustafson(0.05, 8) - 7.65) < 1e-12, "Gustafson N=8")
    prueba(abs(gustafson(0.0, 8) - 8.0) < 1e-12, "Gustafson s=0")
    print(f"Amdahl s=0.05: N=8 -> {amdahl(0.05, 8):.4f} ; límite 1/s = {1/0.05:.1f}")
    print(f"Gustafson s=0.05: N=8 -> {gustafson(0.05, 8):.2f}")

    # 2) Modelo sintético: Karp-Flatt recupera la fracción serial.
    s_real = 0.08
    for n in (2, 4, 8, 16):
        S = amdahl(s_real, n)
        prueba(abs(karp_flatt(S, n) - s_real) < 1e-12, f"Karp-Flatt N={n}")
    print("Karp-Flatt sobre tiempos sintéticos recupera s = 0.08 exactamente.")

    # 3) Mediciones reales. Escalado fuerte: 16 órbitas fijas; débil: 2 órbitas por proceso.
    pasos = 100_000
    ref = [propagar(pasos)] * 16
    tiempos_f, tiempos_d = {}, {}
    for n in (1, 2, 4, 8):
        with Pool(processes=n) as pool:
            pool.map(propagar, [1000] * n)                       # calentamiento
            fuerte = min(tiempo_lote(pool, 16, pasos)[1] for _ in range(2))
            r, _ = tiempo_lote(pool, 16, pasos)
            prueba(r == ref, f"resultado en paralelo (N={n}) distinto del serie")
            debil = min(tiempo_lote(pool, 2 * n, pasos)[1] for _ in range(2))
        tiempos_f[n], tiempos_d[n] = fuerte, debil
    t1 = tiempos_f[1]
    print("ESCALADO FUERTE (16 órbitas fijas)")
    print(" N | tiempo (s) | aceleración | eficiencia | Karp-Flatt e")
    for n, t in tiempos_f.items():
        S = t1 / t
        e = karp_flatt(S, n) if n > 1 else float("nan")
        print(f"{n:2d} | {t:10.3f} | {S:11.2f} | {S/n:10.2f} | {e:8.3f}")
    d1 = tiempos_d[1]
    print("ESCALADO DÉBIL (2 órbitas por proceso)")
    print(" N | tiempo (s) | eficiencia débil T(1)/T(N)")
    for n, t in tiempos_d.items():
        print(f"{n:2d} | {t:10.3f} | {d1/t:8.2f}")
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
