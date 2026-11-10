#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B80-C06: fusion IMU-camara, escala metrica y sesgo del acelerometro (1 eje).

Datos: SINTETICOS e ILUSTRATIVOS (semilla fija 80006); no hay imagenes reales, solo posiciones de camara sinteticas.
Modelo: una camara monocular entrega posiciones relativas SOLO hasta un factor de escala desconocido lambda:
  p_cam(t_k) = lambda * x(t_k) + ruido (sigma_c = 5.0e-4 en unidades de camara).
La IMU mide f_k = a(t_k) + b + ruido (sigma_a = 0.05 m/s2, 50 Hz), con sesgo b = 0.15 m/s2.
Aceleracion de la camara por diferencias finitas centradas: a_cam,k = (p_{k+S} - 2 p_k + p_{k-S}) / (S dt)^2 con S = 5 muestras (separacion que reduce el ruido amplificado) = lambda a_k + ruido amplificado.
Regresion lineal de minimos cuadrados: f_k = (1/lambda) a_cam,k + b  (dos incognitas: 1/lambda y b).
Trayectoria: x(t) = A sin(2 pi f t) con A = 1.0 m (caso excitado) y x(t) = v t (velocidad constante, a = 0: no observable).
Parametros: lambda verdadero = 0.35 (la camara 've' 0.35 unidades por metro); duracion 20 s; dt = 0.02 s; f = 0.5 Hz.
Segunda via: el numero de condicion de la matriz normal 2x2 como medida de observabilidad y la comparacion con el valor verdadero.
La media de las estimaciones de escala debe quedar dentro del 5 % del valor verdadero; el indicador de excitacion es la desviacion tipica de a_cam (unidades de camara por s2).
Tolerancias: escala dentro del 5 % y sesgo dentro de 0.05 m/s2 en el caso excitado.
"""
from __future__ import annotations
import math, platform, random

DT, DUR = 0.02, 20.0
LAM, B, SIG_C, SIG_A = 0.35, 0.15, 5.0e-4, 0.05
STR = 5  # separacion (en muestras) de la segunda diferencia de la camara


def cond2(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    tr, det = a + d, a * d - b * c
    disc = math.sqrt(max(tr * tr / 4 - det, 0.0))
    l1, l2 = tr / 2 + disc, tr / 2 - disc
    return l1 / l2 if l2 > 0 else float("inf")


def ajusta(tray, seed, sig_c=SIG_C):
    rnd = random.Random(seed)
    n = int(DUR / DT) + 1
    t = [k * DT for k in range(n)]
    x = [tray(tk)[0] for tk in t]
    acel = [tray(tk)[1] for tk in t]
    pc = [LAM * xi + rnd.gauss(0, sig_c) for xi in x]
    f = [ai + B + rnd.gauss(0, SIG_A) for ai in acel]
    h = STR * DT
    ac = [(pc[k + STR] - 2 * pc[k] + pc[k - STR]) / h ** 2 for k in range(STR, n - STR)]
    fk = f[STR:n - STR]
    # f = u * ac + b ; u = 1/lambda
    m = len(ac)
    sa = sum(ac)
    saa = sum(v * v for v in ac)
    sf = sum(fk)
    saf = sum(ac[i] * fk[i] for i in range(m))
    N = [[saa, sa], [sa, float(m)]]
    # normalizar columnas antes de calcular la condicion
    sc = math.sqrt(saa / m)
    Nn = [[N[0][0] / sc ** 2, N[0][1] / sc], [N[1][0] / sc, N[1][1]]]
    det = saa * m - sa * sa
    if det <= 0:
        return None
    u = (saf * m - sa * sf) / det
    b = (saa * sf - sa * saf) / det
    exc = math.sqrt(max(saa / m - (sa / m) ** 2, 0.0))
    return (1.0 / u if u != 0 else float("inf")), b, exc


def senoidal(t):
    w = 2 * math.pi * 0.5
    return (1.0 * math.sin(w * t), -1.0 * w * w * math.sin(w * t))


def uniforme(t):
    return (0.8 * t, 0.0)


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print(f"Datos SINTETICOS (semilla 80006): lambda verdadero = {LAM}, sesgo verdadero = {B} m/s2, camara sigma = {SIG_C}, IMU sigma = {SIG_A} m/s2")
    ls, bs = [], []
    for s in range(20):
        r = ajusta(senoidal, 80006 + s)
        ls.append(r[0]); bs.append(r[1])
    lm = sum(ls) / len(ls)
    bm = sum(bs) / len(bs)
    sl = math.sqrt(sum((v - lm) ** 2 for v in ls) / (len(ls) - 1))
    sb = math.sqrt(sum((v - bm) ** 2 for v in bs) / (len(bs) - 1))
    rexc = ajusta(senoidal, 80006)
    print(f"Caso excitado (seno de 1 m a 0.5 Hz), 20 corridas: lambda = {lm:.4f} +- {sl:.4f} ; sesgo = {bm:.4f} +- {sb:.4f} m/s2 ; excitacion (desv. tipica de a_cam) = {rexc[2]:.3f}")
    print(f"  error relativo de escala = {abs(lm - LAM) / LAM * 100:.2f} % ; error de sesgo = {abs(bm - B):.4f} m/s2")
    ru = [ajusta(uniforme, 80006 + s) for s in range(20)]
    ru = [r for r in ru if r is not None]
    rr = ajusta(uniforme, 80006)
    print(f"Caso de velocidad constante (a = 0): excitacion = {rr[2]:.3f} (sin aceleracion la escala NO es observable)")
    lu = [r[0] for r in ru]
    print(f"  dispersion de lambda estimado en esa condicion: min = {min(lu):.1f}, max = {max(lu):.1f} (verdadero 0.35)")
    # Efecto de la excitacion: amplitud menor reduce la observabilidad
    def senoidal_pequena(t):
        w = 2 * math.pi * 0.5
        return (0.02 * math.sin(w * t), -0.02 * w * w * math.sin(w * t))
    lp = [ajusta(senoidal_pequena, 80006 + s)[0] for s in range(20)]
    mp = sum(lp) / len(lp)
    sp = math.sqrt(sum((v - mp) ** 2 for v in lp) / (len(lp) - 1))
    print(f"Amplitud 0.02 m: lambda = {mp:.3f} +- {sp:.3f} (la dispersion crece {sp / sl:.1f} veces)")
    assert abs(lm - LAM) / LAM < 0.05
    assert abs(bm - B) < 0.05
    assert rr[2] < 0.1 * rexc[2]
    assert sp > 3 * sl
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
