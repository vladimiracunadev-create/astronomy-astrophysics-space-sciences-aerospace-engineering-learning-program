#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B58-C13: periodo de rotacion de un asteroide a partir de una curva de luz irregularmente muestreada (periodograma de minimos cuadrados tipo Lomb-Scargle).

Datos: curva de luz SINTETICA de un asteroide de periodo verdadero P = 3.2 h: flujo = 1 + 0.12 cos(2 w t) + 0.03 cos(w t + 1.0) + ruido gaussiano de 0.01 (semilla 20261109), w = 2 pi / P;
60 puntos repartidos en tres noches de 6 h con 20 puntos cada una (instantes aleatorios). No es la curva de ningun asteroide real.
Modelo: para cada frecuencia f se ajusta y = c + a cos(2 pi f t) + b sin(2 pi f t) por minimos cuadrados; potencia = 1 - SSE/SS0 (fraccion de varianza explicada; igual a 1 para una sinusoide exacta).
Despues, para decidir entre P_pico y 2 P_pico, se ajusta una serie de Fourier de 2 armonicos y se compara chi2/gl. Unidades: dia, ciclos/dia, horas.
Supuestos: rotacion principal, sin cambio de fase solar ni movimiento de la geometria durante las noches. Validez: ilustrativa.
Tolerancia: potencia de una sinusoide exacta igual a 1 con 1e-9; frecuencia del pico dentro de 1 % de 2/P; chi2/gl del periodo verdadero entre 0.6 y 1.5 y del medio periodo mayor que 5.
"""
import math, platform, random

def resolver(A, b):
    n = len(b); M = [A[i][:] + [b[i]] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n + 1):
                M[r][k] -= f * M[c][k]
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][k] * x[k] for k in range(i + 1, n))) / M[i][i]
    return x

def base(t, f, K):
    v = [1.0]
    for k in range(1, K + 1):
        v += [math.cos(2 * math.pi * k * f * t), math.sin(2 * math.pi * k * f * t)]
    return v

def sse(ts, ys, f, K):
    n = 2 * K + 1
    B = [base(t, f, K) for t in ts]
    A = [[sum(b[i] * b[j] for b in B) for j in range(n)] for i in range(n)]
    r = [sum(b[i] * y for b, y in zip(B, ys)) for i in range(n)]
    c = resolver(A, r)
    return sum((y - sum(ci * bi for ci, bi in zip(c, b))) ** 2 for b, y in zip(B, ys))

def potencia(ts, ys, f):
    m = sum(ys) / len(ys)
    ss0 = sum((y - m) ** 2 for y in ys)
    return 1.0 - sse(ts, ys, f, 1) / ss0

def curva(ts, P, rng, sig):
    w = 2 * math.pi / P
    return [1 + 0.12 * math.cos(2 * w * t) + 0.03 * math.cos(w * t + 1.0) + (rng.gauss(0, sig) if sig else 0.0) for t in ts]

def calcular():
    P = 3.2 / 24
    rng = random.Random(20261109)
    ts = []
    for noche in range(3):
        ts += sorted(noche + rng.uniform(0, 0.25) for _ in range(20))
    sig = 0.01
    ys = curva(ts, P, rng, sig)
    # sinusoide exacta
    y_exacta = [1 + 0.1 * math.cos(2 * math.pi * 7.5 * t + 0.3) for t in ts]
    p_exacta = potencia(ts, y_exacta, 7.5)
    # barrido
    mejor = (0.0, 0.0)
    f = 2.0
    while f <= 20.0:
        pw = potencia(ts, ys, f)
        if pw > mejor[0]:
            mejor = (pw, f)
        f += 0.01
    fpico = mejor[1]
    # refinamiento fino
    fs = [fpico - 0.01 + 0.0005 * k for k in range(41)]
    fpico = max(fs, key=lambda x: potencia(ts, ys, x))
    gl = len(ts) - 5
    chi_pico = sse(ts, ys, fpico, 2) / sig ** 2 / gl
    chi_dob = sse(ts, ys, fpico / 2, 2) / sig ** 2 / gl
    return {"P": P, "fpico": fpico, "Ppico_h": 24 / fpico, "Pdob_h": 48 / fpico, "pot": mejor[0], "p_exacta": p_exacta,
            "chi_pico": chi_pico, "chi_dob": chi_dob, "f_esp": 2 / P, "N": len(ts)}

def main():
    print("Python", platform.python_version(), "(biblioteca estandar)")
    r = calcular()
    print("%d puntos; periodo verdadero sintetico = %.3f h (frecuencia %.3f ciclos/dia ; segundo armonico %.3f)" % (r["N"], r["P"] * 24, 1 / r["P"], r["f_esp"]))
    print("Potencia de una sinusoide exacta = %.12f" % r["p_exacta"])
    print("Pico del periodograma: f = %.4f ciclos/dia (periodo %.4f h) con potencia %.4f" % (r["fpico"], r["Ppico_h"], r["pot"]))
    print("Doble del periodo del pico = %.4f h" % r["Pdob_h"])
    print("chi2/gl con 2 armonicos: en el pico = %.2f ; en la mitad de la frecuencia (periodo doble) = %.2f" % (r["chi_pico"], r["chi_dob"]))
    assert abs(r["p_exacta"] - 1) < 1e-9
    assert abs(r["fpico"] / r["f_esp"] - 1) < 0.01
    assert 0.6 < r["chi_dob"] < 1.5 and r["chi_pico"] > 5
    print("Pruebas superadas.")

if __name__ == "__main__":
    main()
