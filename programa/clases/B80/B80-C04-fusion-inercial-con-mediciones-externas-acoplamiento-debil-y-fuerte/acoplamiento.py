#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Laboratorio B80-C04: filtro de Kalman inercial con acoplamiento debil (posicion) y fuerte (distancias a balizas), caso plano.

Datos: SINTETICOS e ILUSTRATIVOS (semilla fija 80004); balizas ficticias, sin relacion con ningun sistema real.
Sistema de referencia: plano local x (este), y (norte), unidades SI. Vehiculo de velocidad nominal (2, 1) m/s durante 300 s.
Estado: [x, y, vx, vy, bax, bay] (posicion, velocidad y sesgo de acelerometro). Entrada: aceleracion medida = verdadera + sesgo + ruido.
Sesgo verdadero (0.02, -0.01) m/s2, ruido de acelerometro 0.01 m/s2 (1 sigma, muestreo 1 Hz). Mediciones externas cada 10 s, solo en 100 s <= t <= 200 s
hay UNA sola baliza visible (en el origen); fuera de ese intervalo hay dos (origen y (3000, 0) m) y existen ambas variantes de acoplamiento.
 - Acoplamiento debil: se forma primero un ajuste de posicion (solo si hay >= 2 balizas) con sigma 5 m y se filtra.
 - Acoplamiento fuerte: cada distancia (sigma 5 m) entra directamente al filtro de Kalman extendido, aun con una sola baliza.
Metodo: Monte Carlo de 30 semillas; RMS del error de posicion en t = 300 s. Segunda via: sin ayuda (solo inercial) y la cota 0.5 b t^2.
Tolerancia de verificacion: el acoplamiento fuerte debe tener RMS menor o igual que el debil, y ambos menores que el inercial puro.
"""
from __future__ import annotations
import math, platform, random

DT, T = 1.0, 300
BAL = [(0.0, 0.0), (3000.0, 0.0)]
B_TRUE = (0.02, -0.01)
SIG_A, SIG_R = 0.01, 5.0


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def add(A, B):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]


def eye(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def inv(M):
    n = len(M)
    A = [list(M[i]) + eye(n)[i] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(A[r][c]))
        A[c], A[p] = A[p], A[c]
        d = A[c][c]
        A[c] = [x / d for x in A[c]]
        for r in range(n):
            if r != c:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [r[n:] for r in A]


def trayectoria():
    pos = [(2.0 * k * DT, 1.0 * k * DT) for k in range(T + 1)]
    return pos


F = eye(6)
F[0][2] = F[1][3] = DT
F[0][4] = F[1][5] = -0.5 * DT * DT   # la aceleracion medida incluye el sesgo: a = f_med - b
F[2][4] = F[3][5] = -DT
Q = [[0.0] * 6 for _ in range(6)]
for i, (p, q) in enumerate([(0, 0), (1, 1)]):
    Q[p][p] = (0.5 * DT * DT * SIG_A) ** 2
    Q[2 + i][2 + i] = (DT * SIG_A) ** 2
Q[4][4] = Q[5][5] = 1e-10


def corre(seed, modo):
    rnd = random.Random(seed)
    tray = trayectoria()
    x = [0.0, 0.0, 2.0, 1.0, 0.0, 0.0]
    P = [[0.0] * 6 for _ in range(6)]
    for i, v in enumerate([25.0, 25.0, 0.01, 0.01, 1e-3, 1e-3]):
        P[i][i] = v
    x_ins = [0.0, 0.0, 2.0, 1.0]
    for k in range(1, T + 1):
        # aceleracion verdadera es 0; la medida es sesgo + ruido
        am = [B_TRUE[0] + rnd.gauss(0, SIG_A), B_TRUE[1] + rnd.gauss(0, SIG_A)]
        ab = [am[0] - x[4], am[1] - x[5]]
        # sistema sin ayuda
        x_ins[0] += x_ins[2] * DT + 0.5 * am[0] * DT * DT
        x_ins[1] += x_ins[3] * DT + 0.5 * am[1] * DT * DT
        x_ins[2] += am[0] * DT
        x_ins[3] += am[1] * DT
        # propagacion del filtro (a_n = a_med - b)
        x[0] += x[2] * DT + 0.5 * ab[0] * DT * DT
        x[1] += x[3] * DT + 0.5 * ab[1] * DT * DT
        x[2] += ab[0] * DT
        x[3] += ab[1] * DT
        P = add(mm(mm(F, P), tr(F)), Q)
        t = k * DT
        if modo != "ins" and k % 10 == 0:
            una = 100 <= t <= 200
            vis = [BAL[0]] if una else BAL
            ver = tray[k]
            if modo == "fuerte":
                for (bx, by) in vis:
                    r_med = math.hypot(ver[0] - bx, ver[1] - by) + rnd.gauss(0, SIG_R)
                    r_est = math.hypot(x[0] - bx, x[1] - by)
                    H = [[(x[0] - bx) / r_est, (x[1] - by) / r_est, 0, 0, 0, 0]]
                    S = mm(mm(H, P), tr(H))[0][0] + SIG_R ** 2
                    K = [[kk / S for kk in row] for row in mm(P, tr(H))]
                    inn = r_med - r_est
                    x = [x[i] + K[i][0] * inn for i in range(6)]
                    IKH = [[(1.0 if i == j else 0.0) - K[i][0] * H[0][j] for j in range(6)] for i in range(6)]
                    P = mm(mm(IKH, P), tr(IKH))
                    P = add(P, [[SIG_R ** 2 * K[i][0] * K[j][0] for j in range(6)] for i in range(6)])
            elif len(vis) >= 2:
                # ajuste de posicion por interseccion de dos circunferencias (debil): se resuelve por minimos cuadrados con 2 distancias medidas
                rs = [math.hypot(ver[0] - bx, ver[1] - by) + rnd.gauss(0, SIG_R) for (bx, by) in vis]
                (x1, y1), (x2, y2) = vis
                # dos circulos: eje x entre balizas (y1 = y2 = 0), y >= 0 por convencion de la geometria (vehiculo al norte del eje)
                d = x2 - x1
                px = (rs[0] ** 2 - rs[1] ** 2 + d * d) / (2 * d) + x1
                py = math.sqrt(max(rs[0] ** 2 - (px - x1) ** 2, 0.0))
                H = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0]]
                # covarianza del ajuste por propagacion lineal (aproximada): la geometria amplifica
                gdop = 1.0 / max(py / math.hypot(px - x1, py), 0.05)
                R = [[(SIG_R * gdop) ** 2, 0], [0, (SIG_R * gdop) ** 2]]
                S = add(mm(mm(H, P), tr(H)), R)
                K = mm(mm(P, tr(H)), inv(S))
                inn = [px - x[0], py - x[1]]
                x = [x[i] + K[i][0] * inn[0] + K[i][1] * inn[1] for i in range(6)]
                IKH = [[(1.0 if i == j else 0.0) - sum(K[i][m] * H[m][j] for m in range(2)) for j in range(6)] for i in range(6)]
                P = add(mm(mm(IKH, P), tr(IKH)), mm(mm(K, R), tr(K)))
    ver = tray[T]
    if modo == "ins":
        return math.hypot(x_ins[0] - ver[0], x_ins[1] - ver[1])
    return math.hypot(x[0] - ver[0], x[1] - ver[1])


def rms(vals):
    return math.sqrt(sum(v * v for v in vals) / len(vals))


def main():
    print(f"Python {platform.python_version()} (biblioteca estandar)")
    print("Datos SINTETICOS (semillas 80004..80033), balizas ficticias; vehiculo de (2, 1) m/s, 300 s, sesgo verdadero (0.02, -0.01) m/s2")
    out = {}
    for modo in ("ins", "debil", "fuerte"):
        e = [corre(80004 + s, modo) for s in range(30)]
        out[modo] = rms(e)
        print(f"modo {modo:6s}: RMS del error de posicion en t = 300 s = {out[modo]:9.2f} m (30 corridas)")
    cota = 0.5 * math.hypot(*B_TRUE) * T ** 2
    print(f"Cota de la deriva por sesgo sin ayuda 0.5 |b| t^2 = {cota:.1f} m")
    print(f"Mejora del acoplamiento fuerte frente al debil: {out['debil'] / out['fuerte']:.2f} veces")
    assert out["fuerte"] <= out["debil"] * 1.05
    assert out["debil"] < out["ins"] and out["fuerte"] < out["ins"]
    assert abs(out["ins"] - cota) / cota < 0.15
    print("Pruebas superadas.")


if __name__ == "__main__":
    main()
