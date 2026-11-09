#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B49-C08: ecuacion del radiometro, deriva de ganancia 1/f, desviacion de Allan y conmutacion tipo Dicke.

Datos: ninguna constante fisica. Todo es SINTETICO con semilla 20261109 e ILUSTRATIVO: T_sys = 50 K, ancho de banda de 100 MHz, muestras de 1 ms, fluctuacion relativa de ganancia de 0,5 % rms con espectro
aproximadamente 1/f (suma de 13 procesos AR(1) con constantes de tiempo 2^k ms), 2^17 muestras. No describe ningun radiometro real.
Modelo: potencia detectada y_i = (1 + g_i)(T_sys + n_i), con n_i gaussiano de desviacion T_sys/sqrt(B dt) (ecuacion del radiometro) y g_i la deriva. Receptor de potencia total: se promedian los y_i. Receptor
Dicke: las muestras pares miran el cielo y las impares una carga de referencia a la misma temperatura (se mide, por tanto, cero senal); la salida es y_par - y_impar. Desviacion de Allan
sigma_A(tau) = sqrt(0.5 <(ybar_{k+1} - ybar_k)^2>) con promedios consecutivos de duracion tau.
Supuestos: ruido blanco gaussiano; la deriva comun a muestras adyacentes; el modelo 1/f es aproximado. Validez: ilustrativa; no se mide un instrumento.
Tolerancia: sigma_A del ruido blanco a tau pequena frente a T_sys/sqrt(B tau) a 3 % (tau = 1 ms) y a 5 % (tau = 256 ms); en el receptor de potencia total la desviacion de Allan debe tener un minimo y subir despues; el Dicke debe ganar un factor
de al menos 3 en tau = 16 s; el nivel blanco del Dicke frente a 2 T_sys/sqrt(B tau) a 8 % (tau = 16 ms; la incertidumbre de la estimacion de Allan con n intervalos es del orden de 1/sqrt(2n)).
"""
from __future__ import annotations
import math, platform, random


def allan(y, m):
    """Desviacion de Allan con promedios de m muestras consecutivas."""
    n = len(y) // m
    med = [sum(y[i * m:(i + 1) * m]) / m for i in range(n)]
    s = sum((med[i + 1] - med[i]) ** 2 for i in range(n - 1)) / (2 * (n - 1))
    return math.sqrt(s)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    rng = random.Random(20261109)
    N = 2 ** 17
    dt = 1e-3
    B = 100e6
    Ts = 50.0
    sw = Ts / math.sqrt(B * dt)
    print(f"Ecuacion del radiometro: sigma por muestra = T_sys/sqrt(B dt) = {sw:.5f} K ({100 * sw / Ts:.4f} % de T_sys) ; 1 s: {Ts / math.sqrt(B * 1.0):.6f} K")
    # deriva 1/f aproximada
    comp = [(1 - 1 / 2 ** k, math.sqrt(1 - (1 - 1 / 2 ** k) ** 2)) for k in range(1, 14)]
    x = [0.0] * len(comp)
    g = []
    for _ in range(N):
        s = 0.0
        for j, (a, b) in enumerate(comp):
            x[j] = a * x[j] + b * rng.gauss(0, 1)
            s += x[j]
        g.append(0.005 * s / math.sqrt(len(comp)))
    gm = sum(g) / N
    grms = math.sqrt(sum((v - gm) ** 2 for v in g) / N)
    print(f"Deriva de ganancia sintetica: rms = {100 * grms:.3f} % (objetivo 0,5 % por componente)")
    ruido = [rng.gauss(0, sw) for _ in range(N)]
    solo_blanco = [Ts + r for r in ruido]
    total = [(1 + gi) * (Ts + r) for gi, r in zip(g, ruido)]
    # Dicke: par menos impar, ruido independiente en cada muestra
    dicke = []
    for i in range(0, N - 1, 2):
        yb = (1 + g[i]) * (Ts + ruido[i])
        yr = (1 + g[i + 1]) * (Ts + rng.gauss(0, sw))
        dicke.append(yb - yr)
    print(f"{'tau (s)':>9} {'blanco (K)':>11} {'teoria blanco':>14} {'potencia total (K)':>19} {'Dicke (K)':>10} {'teoria Dicke':>13}")
    res = {}
    for m in (1, 4, 16, 64, 256, 1024, 4096, 16384):
        tau = m * dt
        sb = allan(solo_blanco, m)
        teo = Ts / math.sqrt(B * tau)
        st = allan(total, m)
        # el Dicke tiene un punto cada 2 dt: tau = m dt corresponde a m/2 puntos
        md = max(m // 2, 1)
        sd = allan(dicke, md) if m >= 2 else float("nan")
        tdk = 2 * Ts / math.sqrt(B * tau)
        res[m] = (sb, teo, st, sd, tdk)
        print(f"{tau:9.3f} {sb:11.5f} {teo:14.5f} {st:19.5f} {sd:10.5f} {tdk:13.5f}")
    assert abs(res[1][0] / res[1][1] - 1) < 0.03 and abs(res[256][0] / res[256][1] - 1) < 0.05
    sts = [res[m][2] for m in sorted(res)]
    imin = sts.index(min(sts))
    print(f"Potencia total: minimo de Allan en tau = {sorted(res)[imin] * dt:.3f} s ({min(sts):.5f} K) ; despues sube hasta {sts[-1]:.5f} K")
    assert 0 < imin < len(sts) - 1
    # el Dicke en m = 16384 (tau = 16 s)
    mejora = res[16384][2] / res[16384][3]
    print(f"A tau = 16,384 s: potencia total / Dicke = {mejora:.2f}")
    assert mejora > 3
    assert abs(res[16][3] / res[16][4] - 1) < 0.08
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
