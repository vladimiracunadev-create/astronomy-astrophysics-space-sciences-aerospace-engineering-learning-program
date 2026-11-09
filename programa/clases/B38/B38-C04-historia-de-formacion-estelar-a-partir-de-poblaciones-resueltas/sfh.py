#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B38-C04: historia de formacion estelar a partir de conteos de estrellas resueltas por masa de salida de la secuencia principal.

Datos: ninguna constante fisica ni catalogo. La vida en la secuencia principal t = 10 Gyr (M/Msol)^-2,5, la IMF de Salpeter (indice 2,35), los 13 intervalos de edad de 1 Gyr, la historia
verdadera (SFR constante = 1 con una rafaga de factor 4 entre 3 y 5 Gyr) y la semilla 20261109 son ILUSTRATIVOS (sinteticos). No se ajusta ningun diagrama color-magnitud real.
Modelo: los intervalos de masa se eligen para que su vida sea j Gyr (j = 1..13), de modo que N_j = sum_{i<j} s_i x_j (matriz triangular, x_j = estrellas de ese intervalo por unidad de masa formada).
Dos vias: (a) inversion directa por diferencias s_i = (N_i - N_{i-1})/x ... resuelta por sustitucion; (b) Richardson-Lucy (maxima verosimilitud de Poisson) con 5000 iteraciones.
Supuestos: sin metalicidad, sin binarias, sin errores fotometricos, IMF conocida. Validez: ilustrativa.
Tolerancia: ambas vias recuperan la historia sin ruido a menos del 1 %; con ruido de Poisson la masa total formada se recupera a menos del 10 %.
"""
from __future__ import annotations
import math, platform, random, sys

NB = 13
ALPHA = 2.35
MMIN, MMAX = 0.08, 100.0

def sfr_verdadera():
    return [4.0 if 3 <= i < 5 else 1.0 for i in range(NB)]

def edad_a_masa(t):
    return (10.0 / t) ** (1 / 2.5)

def fraccion_numero(m1, m2):
    a = 1 - ALPHA
    return (m2 ** a - m1 ** a) / (MMAX ** a - MMIN ** a)

def matriz(escala):
    """A[j][i] = estrellas esperadas en el intervalo de masa j (vida entre j y j+1 Gyr) formadas en el intervalo de edad i."""
    norm_masa = (MMAX ** (2 - ALPHA) - MMIN ** (2 - ALPHA)) / (2 - ALPHA) / (MMAX ** (1 - ALPHA) - MMIN ** (1 - ALPHA)) * (1 - ALPHA)
    a = [[0.0] * NB for _ in range(NB)]
    for j in range(NB):
        # intervalo de masa con vida entre (j+1) y (j+2) Gyr, es decir masas de edad_a_masa(j+2) a edad_a_masa(j+1)
        m_lo, m_hi = edad_a_masa(j + 2), edad_a_masa(j + 1)
        x = fraccion_numero(m_lo, m_hi) / norm_masa * escala
        for i in range(NB):
            # estrellas formadas a la edad central i+0,5 Gyr siguen vivas si i+0,5 < j+1,5 (vida central del intervalo)
            vivo = 1.0 if i <= j else 0.0
            a[j][i] = x * vivo
    return a

def aplicar(a, s):
    return [sum(a[j][i] * s[i] for i in range(NB)) for j in range(NB)]

def rl(a, datos, it=5000):
    s = [1.0] * NB
    col = [sum(a[j][i] for j in range(NB)) for i in range(NB)]
    for _ in range(it):
        mod = aplicar(a, s)
        for i in range(NB):
            if col[i] <= 0:
                continue
            num = sum(a[j][i] * datos[j] / mod[j] for j in range(NB) if mod[j] > 0)
            s[i] *= num / col[i]
    return s

def directa(a, datos):
    """a es triangular inferior por el mapa vivo: solo i <= j contribuye (vivo = 0 si i > j+1,5-1)."""
    s = [0.0] * NB
    for j in range(NB):
        resto = sum(a[j][i] * s[i] for i in range(j))
        s[j] = (datos[j] - resto) / a[j][j]
    return s

def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    escala = 2.0e5
    a = matriz(escala)
    ver = sfr_verdadera()
    esperado = aplicar(a, ver)
    # triangularidad: vivo(i>j) = 0
    assert all(a[j][i] == 0.0 for j in range(NB) for i in range(j + 1, NB))
    dir_ = directa(a, esperado)
    rl_ = rl(a, esperado, 20000)
    print(f"{'edad [Gyr]':>10} {'verdadera':>10} {'directa':>9} {'RL':>8}")
    for i in range(NB):
        print(f"{i:4d}-{i + 1:<5d} {ver[i]:10.3f} {dir_[i]:9.3f} {rl_[i]:8.3f}")
    err_d = max(abs(dir_[i] - ver[i]) / ver[i] for i in range(NB))
    err_r = max(abs(rl_[i] - ver[i]) / ver[i] for i in range(NB))
    print(f"error relativo maximo sin ruido: directa {err_d:.2e}, RL {err_r:.3f}")
    assert err_d < 1e-9 and err_r < 0.01
    # con ruido de Poisson (Knuth/gaussiana para media grande)
    rng = random.Random(20261109)
    def poisson(l):
        if l > 30:
            return max(0, round(rng.gauss(l, math.sqrt(l))))
        L, k, p = math.exp(-l), 0, 1.0
        while True:
            p *= rng.random()
            if p <= L:
                return k
            k += 1
    print(f"{'estrellas':>10} {'total RL':>9} {'dispersion total':>17} {'dispersion bin 3-4':>19}")
    disp_bin = {}
    for esc in (2.0e5, 2.0e3, 2.0e2):
        aa = matriz(esc)
        esp = aplicar(aa, ver)
        tot, b3 = [], []
        for _ in range(60):
            d = [poisson(e) for e in esp]
            r = rl(aa, [max(x, 0.5) for x in d], 1500)
            tot.append(sum(r)); b3.append(r[3])
        m_t = sum(tot) / len(tot)
        sd_t = math.sqrt(sum((t - m_t) ** 2 for t in tot) / (len(tot) - 1))
        m_b = sum(b3) / len(b3)
        sd_b = math.sqrt(sum((t - m_b) ** 2 for t in b3) / (len(b3) - 1))
        disp_bin[esc] = sd_b / m_b
        print(f"{sum(esp):10.0f} {m_t:9.2f} {sd_t / m_t:17.4f} {sd_b / m_b:19.4f}")
        assert abs(m_t - sum(ver)) / sum(ver) < 0.1
    assert disp_bin[2.0e2] > disp_bin[2.0e5]
    print(f"masa total formada verdadera {sum(ver):.2f} (SFR x Gyr)")
    print("Pruebas superadas.")

if __name__ == "__main__":
    sys.exit(main())
